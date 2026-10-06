"""Carte interactive de la dépense publique par élève, établissement par établissement (approche B, 2025).

Pour chacun des établissements de l'approche B (écoles maternelles, élémentaires et primaires, collèges, lycées,
EREA ; publics et privés sous contrat), assemble :
- la dépense publique par élève et sa décomposition (resultats/B1, script 04), avec la nature des clés des
  collectivités (comptes du territoire, moyenne, montant national du privé) ;
- les élèves par niveau, les classes (écoles), les heures d'enseignement H/E et les étudiants de STS et de CPGE ;
- la position donnée par l'annuaire de l'éducation ; à défaut, la mairie de la commune (API Découpage administratif) ;
- les cas où la comparaison avec les établissements du même groupe n'a pas de sens (« non classés ») ;
- un fond de carte (contours administratifs Etalab 2025, généralisation à 100 m) et les noms des communes.

Écrit resultats/carte_etablissements_2025.csv (une ligne par établissement), son dictionnaire des colonnes
(resultats/carte_etablissements_2025_colonnes.md) et resultats/carte_etablissements.html (page autonome : données
compressées dans la page ; Leaflet et deux polices chargés en ligne). Option : --artefact CHEMIN écrit en plus la
version « fragment » de la page (sans en-tête HTML), destinée à la publication.
Hypothèses : H-B18 (et H-B1 à H-B17 pour les montants).
"""
import argparse
import base64
import gzip
import json
import re

import numpy as np
import pandas as pd

from commun import BRUT, RACINE, RESULTATS, Communes, cle, cle_commune

ETAB = BRUT / "etablissements"
CARTO = BRUT / "cartographie"
MODELE = RACINE / "scripts" / "carte_etablissements_modele.html"
LEAFLET_CSS = RACINE / "scripts" / "leaflet-1.9.4.min.css"  # feuille de style de Leaflet (licence BSD-2), intégrée à la page

TYPES = {  # code : libellé
    "M": "école maternelle", "E": "école élémentaire", "P": "école primaire", "C": "collège",
    "G": "lycée général et technologique", "V": "lycée polyvalent", "L": "lycée professionnel",
    "A": "EREA", "X": "autre établissement du second degré"}
TYPE_2D = {"collège": "C", "lycée général et technologique": "G", "lycée polyvalent": "V", "lycée professionnel": "L",
           "EREA / LEA": "A"}  # le reste (cité scolaire, école secondaire spécialisée) : « X »
SECTEUR = {"public": 0, "prive_sc": 1}
REGIONS = {
    "AUVERGNE-RHONE-ALPES": "Auvergne-Rhône-Alpes", "BOURGOGNE-FRANCHE-COMTE": "Bourgogne-Franche-Comté",
    "BRETAGNE": "Bretagne", "CENTRE-VAL DE LOIRE": "Centre-Val de Loire", "CORSE": "Corse", "GRAND EST": "Grand Est",
    "GUADELOUPE": "Guadeloupe", "GUYANE": "Guyane", "HAUTS-DE-FRANCE": "Hauts-de-France",
    "ILE-DE-FRANCE": "Île-de-France", "LA REUNION": "La Réunion", "MARTINIQUE": "Martinique", "MAYOTTE": "Mayotte",
    "NORMANDIE": "Normandie", "NOUVELLE-AQUITAINE": "Nouvelle-Aquitaine", "OCCITANIE": "Occitanie",
    "PAYS DE LA LOIRE": "Pays de la Loire", "PROVENCE-ALPES-COTE D'AZUR": "Provence-Alpes-Côte d'Azur"}
OUTRE_MER = ("971", "972", "973", "974", "976", "977", "978")
POSITION_COMMUNE = {"Ville", "COMMUNE", "CENTROIDE (D'EMPRISE)"}       # l'annuaire ne localise qu'à la commune
POSITION_DOUTEUSE = {"Mauvaise", "NE SAIT PAS"}
AUTRES_ETAT = ["etat_remplacement_formation", "etat_inclusion_sante_social", "etat_activites_educatives",
               "etat_aides_familles", "etat_soutien_administration"]
# Comparaison avec le groupe (même type, même secteur) : sans objet dans ces cas (H-B18).
NON_CLASSE = {1: "aucun enseignant publié pour cette école",
              2: "personnels de vie scolaire ou de direction non publiés pour cet établissement (l'une des deux catégories au moins)",
              3: "école sous contrat pour une partie de ses classes seulement, ou plus du tout (annuaire 2026)",
              4: "groupe de moins de 10 établissements en France, pas de comparaison possible",
              5: "type d'école inconnu (effectifs par niveau non publiés)"}
SEUIL_GROUPE = 10
CONTRAT_PARTIEL = r"PARTIE DES CLASSES|HORS CONTRAT"
STATUT_CLE = {"propre": 0, "plafond": 1, "plancher": 2, "moyenne": 3, "national": 4, "academie": 5}
LIB_CLE = {  # libellés du CSV, par ligne de la décomposition ; les montants sont recalés sur le total à répartir
    "cle_commune": {"propre": "réparti selon les comptes 2025 de la commune",
                    "plafond": "réparti selon les comptes 2025 de la commune, dépense par élève plafonnée au 99e centile",
                    "plancher": "réparti selon les comptes 2025 de la commune, dépense par élève relevée au 1er centile",
                    "moyenne": "réparti selon la moyenne des communes (comptes de la commune non utilisables)",
                    "national": "forfait communal : montant national par élève du privé"},
    "cle_departement": {"propre": "réparti selon la dépense par collégien du département (Géographie de l'École)",
                        "moyenne": "moyenne nationale (territoire absent de la Géographie de l'École)",
                        "national": "montant national par collégien du privé"},
    "cle_region": {"propre": "réparti selon la dépense par lycéen de la région (Géographie de l'École)",
                   "moyenne": "moyenne nationale (territoire absent de la Géographie de l'École)",
                   "academie": "réparti selon la dépense par lycéen de la Guadeloupe, même région académique",
                   "national": "montant national par lycéen du privé"}}

def espaces(s):
    return " ".join(str(s).split()) if isinstance(s, str) else s


def arrondi(x) -> int:
    """Arrondi au plus proche, les demis vers le haut (même règle pour le CSV et la page)."""
    return int(np.floor(float(x) + 0.5))


def entiers(s, f=1) -> list:
    """Valeurs × f arrondies au plus proche (demis vers le haut) ; None si la valeur manque."""
    s = pd.to_numeric(pd.Series(s), errors="coerce")
    return [None if pd.isna(x) else int(np.floor(float(x) * f + 0.5)) for x in s]


def decimales(s, f) -> pd.Series:
    """Mêmes valeurs que la page (entiers(s, f) / f), pour le CSV."""
    return pd.Series([None if x is None else x / f for x in entiers(s, f)], index=pd.Series(s).index, dtype="Float64")


def arrondi_somme(parts: np.ndarray, total: int) -> np.ndarray:
    """Arrondit chaque composante en conservant la somme (méthode du plus fort reste)."""
    base = np.floor(parts)
    reste = int(total - base.sum())
    if reste > 0:
        base[np.argsort(-(parts - base), kind="stable")[:reste]] += 1
    elif reste < 0:
        base[np.argsort(parts - base, kind="stable")[:-reste]] -= 1
    return base.astype(int)


# ---------------------------------------------------------------------------------------------- noms
ABREV = [(r"\bGen\.\s*Et Technol\.\s*", "général et technologique "), (r"\bEcole\b", "École"), (r"\bEcoles\b", "Écoles"),
         (r"\bElementaire\b", "élémentaire"), (r"\bMaternelle\b", "maternelle"), (r"\bPrimaire\b", "primaire"),
         (r"\bPublique\b", "publique"), (r"\bPrivee\b", "privée"), (r"\bPrive\b", "privé"), (r"\bLycee\b", "Lycée"),
         (r"\bProfessionnel\b", "professionnel"), (r"\bPolyvalent\b", "polyvalent"), (r"\bGeneral\b", "général"),
         (r"\bProf\b", "professionnel"), (r"\bCollege\b", "Collège"), (r"\bDes Metiers\b", "des métiers"),
         (r"^Lpo Lycée\b", "Lycée"), (r"^Lp Lycée\b", "Lycée"), (r"\bLpo\b", "LPO"), (r"\bLp\b", "LP"), (r"\bSte\b", "Sainte"),
         (r"\bSt\b", "Saint"), (r"\bD Application\b", "d'application"), (r"\bD'Application\b", "d'application"),
         (r"\bDe\b", "de"), (r"\bDu\b", "du"), (r"\bDes\b", "des"), (r"\bLa\b", "la"), (r"\bLe\b", "le"), (r"\bLes\b", "les"),
         (r"\bEt\b", "et"), (r"\bSur\b", "sur"), (r"\bSous\b", "sous"), (r"\bEn\b", "en"), (r"\bAux\b", "aux"),
         (r"\bAu\b", "au"), (r"\bLès\b", "lès"), (r"\bLes\b", "les"), (r"\s+-\s*$", "")]
SIGLES = ["RPI", "RPC", "IME", "ULIS", "SEGPA", "EREA", "CFA", "SIVOS", "SIVU", "EJAP", "ITEP", "DITEP", "IMPRO",
          "ESAT", "UEMA", "UEEA", "RASED", "CMPP", "MFR", "UPE2A", "SESSAD", "LPO", "LGT", "IEM", "EPS", "CNED", "SNCF",
          "PACA", "ABCM", "CIES", "STAM", "ECBG"]
SIGLE_POINTE = re.compile(r"\(?(?:[A-Za-z]\.){2,}[A-Za-z]*\.?\)?,?")  # « R.P.I. », « E.I.B. » : laissés tels quels
SIGLE = re.compile(r"\b(" + "|".join(SIGLES) + r")\b", re.IGNORECASE)
ROMAIN = re.compile(r"\b(Ii|Iii|Iv|Vi|Vii|Viii|Ix|Xi|Xii|Xiii|Xiv|Xv|Xx)\b")  # « Henri Iv » → « Henri IV » (sauf « I » et « V »)
PARTICULE = {"de", "du", "des", "la", "le", "les", "et", "sur", "sous", "en", "aux", "au", "lès", "d", "l"}


def finitions(s: str) -> str:
    """Sigles et chiffres romains en capitales ; élision d' en minuscule après un mot (« Jeanne d'Arc ») ; « L' » est
    laissé tel quel (« Tristan L'Hermite », « L'Isle-Jourdain »)."""
    s = SIGLE.sub(lambda m: m.group(1).upper(), s)
    s = ROMAIN.sub(lambda m: m.group(1).upper(), s)
    s = re.sub(r"(?<=[\w)] )D'(?=\w)", "d'", s)
    s = re.sub(r"(?<=-)D'(?=\w)", "d'", s)
    s = re.sub(r"(?<=\w-)(En|Sur|Sous|Les|Le|La|De|Du|Des|Aux|Au|Et|Lès)(?=-)", lambda m: m.group(1).lower(), s)  # Arc-en-Ciel
    return s


def nom_lisible(nom: str) -> str:
    """Nom en capitales sans accents (base, ou annuaire) → forme lisible ; les accents ne peuvent pas être rétablis."""
    s = espaces(str(nom)).title()
    for motif, rempl in ABREV:
        s = re.sub(motif, rempl, s)
    s = espaces(finitions(s))
    return s[:1].upper() + s[1:]


PREFIXE_ECOLE = re.compile(r"^[EÉ]cole\s+(maternelle|[eé]l[eé]mentaire|primaire)(?:\s+(publique|priv[eé]e?))?\b",
                           re.IGNORECASE)
# « E.P.PU », « E.M.PR », « E.E.A.PU » (application), « E.P.S.PR » (spécialisée), en tête ou après « - »
PREFIXE_SIGLE = re.compile(r"(?:^|(?<=- ))E\.\s?([MPE])\.\s?(?:([AS])\.\s?)?P\.?\s?(U|R)\b\.?\s*", re.IGNORECASE)
NIVEAU = {"M": "maternelle", "P": "primaire", "E": "élémentaire"}


def mot_capitales(t: str) -> bool:
    lettres = [c for c in t if c.isalpha()]
    return len(lettres) >= 2 and all(c.isupper() for c in lettres)


def typographie(nom: str) -> str:
    """Noms de l'annuaire : « E.P.PU X » ou « Ecole Primaire Publique X » → « École primaire publique X » ; mots écrits
    en capitales remis en minuscules (sauf sigles, sigles pointés et chiffres romains)."""
    s = espaces(nom)

    def sigle_ecole(m):
        sorte = {"A": " d'application", "S": " spécialisée"}.get((m.group(2) or "").upper(), "")
        return f"École {NIVEAU[m.group(1).upper()]}{sorte} {'publique' if m.group(3).upper() == 'U' else 'privée'} "
    s = PREFIXE_SIGLE.sub(sigle_ecole, s)
    s = re.sub(r"^Ecoler\b", "École", s)
    s = re.sub(r"^Ecoleprimaire\b", "École primaire", s)
    s = re.sub(r"\bElem\.\s*", "élémentaire ", s, flags=re.IGNORECASE)
    # Suites de mots en capitales (ou mot isolé de 4 lettres et plus) : casse de titre, particules en minuscules.
    mots = espaces(s).split(" ")
    cap = [mot_capitales(t) and not SIGLE.fullmatch(t.strip("(),.")) and not SIGLE_POINTE.fullmatch(t)
           and not ROMAIN.fullmatch(t.strip("(),.").title()) for t in mots]
    for i, t in enumerate(mots):
        voisin = (i > 0 and cap[i - 1]) or (i + 1 < len(mots) and cap[i + 1])
        if cap[i] and (voisin or sum(c.isalpha() for c in t) >= 4):
            u = "-".join(re.sub(r"[^\W\d_]", lambda m: m.group(0).upper(), p.lower(), count=1) for p in t.split("-"))
            u = re.sub(r"(?<=\w)'(\w)", lambda m: "'" + m.group(1).upper(), u)
            if i > 0 and cap[i - 1] and cle(u) in PARTICULE:
                u = u.lower()
            mots[i] = u
    s = " ".join(mots)
    s = re.sub(r"\bEcole(s?)\b", r"École\1", s)

    def rempl(m):
        niveau = m.group(1).lower()
        niveau = niveau if niveau in ("maternelle", "primaire") else "élémentaire"
        sec = (m.group(2) or "").lower()
        return "École " + niveau + (" publique" if sec == "publique" else " privée" if sec else "")
    s = PREFIXE_ECOLE.sub(rempl, s)
    s = re.sub(r"^École (Publique|Privée)\b", lambda m: "École " + m.group(1).lower(), s)
    s = re.sub(r"(\bÉcole\b[^()\-,]*?)\bprivé\b(?!e)", r"\1privée", s)   # « École primaire privé » → « privée »
    return finitions(espaces(s))

# ---------------------------------------------------------------------------------------------- établissements
def etablissements() -> pd.DataFrame:
    b1 = pd.read_csv(RESULTATS / "B1_depense_publique_par_etablissement_2025.csv", sep=";", low_memory=False,
                     dtype={"code_departement": str})
    ec = pd.read_csv(RACINE / "data/processed/base_ecoles_rentree2024.csv", sep=";", low_memory=False,
                     dtype={"code_commune": str}).set_index("uai")
    se = pd.read_csv(RACINE / "data/processed/base_2d_rentree2024.csv", sep=";", low_memory=False,
                     dtype={"code_commune": str}).set_index("uai")
    ann = pd.read_csv(ETAB / "annuaire_education_extrait_2026-10-04.csv", sep=";", low_memory=False, dtype=str,
                      usecols=["identifiant_de_l_etablissement", "nom_etablissement", "type_etablissement", "nom_commune",
                               "latitude", "longitude", "precision_localisation", "ecole_maternelle", "ecole_elementaire",
                               "type_contrat_prive"])
    pr = b1["degre"].eq("1er degré")
    d = b1.copy()
    # Niveaux et classes ; niveaux inconnus (non publiés) laissés vides.
    d["n1"] = np.where(pr, d["uai"].map(ec["eleves_preelementaire"]), d["uai"].map(se["eleves_college"]))
    d["n2"] = np.where(pr, d["uai"].map(ec["eleves_elementaire"]), d["uai"].map(se["eleves_lycee_gt"]))
    d["n3"] = np.where(pr, d["uai"].map(ec["eleves_ulis_ueea"]), d["uai"].map(se["eleves_lycee_pro"]))
    for c in ("n1", "n2", "n3"):
        d[c] = pd.to_numeric(d[c], errors="coerce")
    sans_niveaux = pr & d["n1"].isna() & d["n2"].isna()
    d.loc[sans_niveaux, "n3"] = np.nan
    incomplet = pr & ~sans_niveaux & (d["n1"].fillna(0) + d["n2"].fillna(0) + d["n3"].fillna(0)).round().ne(d["eleves"].round())
    d.loc[incomplet & d["n3"].fillna(0).eq(0), "n3"] = np.nan  # ULIS non renseignées dans la source
    d["classes"] = np.where(pr, d["uai"].map(ec["nb_classes"]), np.nan)
    d["code_commune"] = np.where(pr, d["uai"].map(ec["code_commune"]), d["uai"].map(se["code_commune"]))
    d["region"] = np.where(pr, d["uai"].map(ec["region_academique"]), d["uai"].map(se["region_academique"]))
    d["region"] = d["region"].map(REGIONS)
    assert d["region"].notna().all()
    # Écoles de Saint-Martin et de Saint-Barthélemy, codées 971 (Guadeloupe) dans le fichier des effectifs : département
    # tiré du code commune (978xx, 977xx), comme pour leurs collèges et lycées (H-B18).
    com_iles = d["code_departement"].eq("971") & d["code_commune"].astype(str).str[:3].isin(["977", "978"])
    d.loc[com_iles, "code_departement"] = d.loc[com_iles, "code_commune"].str[:3]

    # Annuaire : pour un UAI à plusieurs lignes (sites), la ligne dont la commune est celle de la base (ou en contient le
    # nom, ou l'inverse), sans annexe ni site post-bac dans le nom ; à égalité, celle dont le type et le nom concordent.
    for c in ("nom_etablissement", "nom_commune"):
        ann[c] = ann[c].map(espaces)
    u = ann["identifiant_de_l_etablissement"]
    base = d.set_index("uai")
    com_b, com_a = u.map(base["commune"].map(cle_commune)), ann["nom_commune"].map(cle_commune)
    exacte = [isinstance(b, str) and a == b for a, b in zip(com_a, com_b)]
    meme_commune = [isinstance(b, str) and (a == b or f" {a} " in f" {b} " or f" {b} " in f" {a} ")
                    for a, b in zip(com_a, com_b)]
    VIDES = {"de", "la", "le", "les", "du", "des", "et", "d", "l", "a", "au", "aux", "en"}
    mots_b = u.map(base["nom"].map(lambda s: set(cle_commune(s).split()) - VIDES))
    commun = [len(set(cle_commune(a).split()) & b) if isinstance(b, set) else 0 for a, b in zip(ann["nom_etablissement"], mots_b)]
    typ_b = u.map(base["degre"].eq("1er degré").map({True: "ecole", False: None}))
    typ_b = typ_b.fillna(u.map(base["type"].map({"collège": "college", "EREA / LEA": "erea"})))
    typ_b = typ_b.fillna(u.map(base["type"].map(lambda t: "lycee" if isinstance(t, str) and t.startswith("lycée") else None)))
    accord = [isinstance(t, str) and isinstance(a, str) and cle(a).startswith(t) for t, a in zip(typ_b, ann["type_etablissement"])]
    annexe = ann["nom_etablissement"].str.contains(r"annexe|site|\(sup\)|prépa|STS|pôle|campus|supérieur", case=False, regex=True)
    ann["_r1"] = (4 * (~pd.Series(meme_commune, index=ann.index)).astype(int)
                  + 2 * (~pd.Series(exacte, index=ann.index)).astype(int) + annexe.astype(int))
    ann["_r2"] = -pd.Series(accord, index=ann.index).astype(int)
    ann["_r3"] = -pd.Series(commun, index=ann.index)
    ann = (ann.sort_values(["identifiant_de_l_etablissement", "_r1", "_r2", "_r3"], kind="stable")
           .drop_duplicates("identifiant_de_l_etablissement").set_index("identifiant_de_l_etablissement"))

    # Type : écoles d'après la base (élèves par niveau, à défaut annuaire puis nom : script 03) ; 2nd degré : nature (H-B16).
    d["type_source"] = np.where(pr, d["uai"].map(ec["type_ecole_source"]), "")
    d["type_inconnu"] = d["type_source"].eq("inconnu")
    d["typ"] = np.where(pr, d["uai"].map(ec["type_ecole"]), d["type"].map(TYPE_2D).fillna("X"))

    # Heures d'enseignement (H/E, niveaux du secondaire), étudiants de STS et de CPGE (« ns » = effectif masqué).
    h = pd.concat([pd.read_csv(ETAB / f"moyens_enseignants_2d_{s}_rentree2024.csv", sep=";", low_memory=False)
                   for s in ("public", "prive")])
    h = h[h["uai"].astype(str).str.len() == 8].copy()
    hc, ecl = "numerateur_h_e_nb_heures_enseignement_hebdo_devant_eleves", "denominateur_h_e_somme_eleves_en_division"
    h["ns"] = h[ecl].astype(str).str.strip().str.lower().eq("ns")
    for c in (hc, ecl):
        h[c] = pd.to_numeric(h[c], errors="coerce").fillna(0)
    postbac = h["niveau"].isin(["STS", "CPGE"])
    sec = h[~postbac].groupby("uai")[[hc, ecl]].sum()
    d["he"] = d["uai"].map(sec[hc] / sec[ecl].replace(0, np.nan))
    d["couverture_he"] = np.where(pr, np.nan, d["uai"].map(sec[ecl]).fillna(0) / d["eleves"])
    d["etudiants_postbac"] = np.where(pr, np.nan, d["uai"].map(h[postbac].groupby("uai")[ecl].sum()).fillna(0))
    d["postbac_masque"] = d["uai"].isin(h.loc[postbac & h["ns"], "uai"]).astype(int)
    # ETP et indice de coût : 0 ETP = donnée absente (H-B12) ; l'indice ne vaut que pour le 2nd degré.
    d["etp"] = d["etp_enseignants"].where(d["etp_enseignants"] > 0)
    d["indice"] = np.where(pr | d["etp"].isna(), np.nan, d["indice_cout_enseignant"])
    # IPS : celui de la base ; EREA, d'après le fichier de la DEPP qui leur est propre ; « NS » : non publié (écoles).
    ips_erea = pd.read_csv(ETAB / "ips_erea_2024-2025.csv", sep=";", dtype={"uai": str}).set_index("uai")["ips"]
    d["ips"] = pd.to_numeric(d["ips"], errors="coerce").fillna(d["uai"].map(ips_erea))
    ips_e = pd.read_csv(ETAB / "ips_ecoles_2024-2025.csv", sep=";", dtype=str, usecols=["uai", "ips"]).drop_duplicates("uai")
    ns = d["uai"].isin(ips_e.loc[ips_e["ips"].str.upper().eq("NS"), "uai"])
    d["ips_statut"] = np.select([d["ips"].notna(), ns], ["publié", "non publié (NS)"], "absent")

    # Position : annuaire ; à défaut, mairie de la commune (ou de l'arrondissement municipal, centre d'une commune déléguée).
    d["lat"] = pd.to_numeric(d["uai"].map(ann["latitude"]), errors="coerce")
    d["lon"] = pd.to_numeric(d["uai"].map(ann["longitude"]), errors="coerce")
    prec = d["uai"].map(ann["precision_localisation"])
    d["ap"] = np.select([prec.isin(POSITION_COMMUNE), prec.isin(POSITION_DOUTEUSE)], [2, 4], 0)
    d["nom_affiche"] = d["uai"].map(ann["nom_etablissement"])
    d["commune_affichee"] = d["uai"].map(ann["nom_commune"])
    d["absent_annuaire"] = d["nom_affiche"].isna()
    manque = d["lat"].isna() | d["lon"].isna()
    trouve = pd.Series(False, index=d.index)
    d["ap_point"] = ""
    communes = Communes()
    par_nom = d["uai"].map(ec["code_commune_source"]).fillna("").str.startswith("nom")
    for i in d.index[manque]:
        # École rattachée par son nom (script 03) : on refait la recherche par le nom, qui peut donner une commune
        # déléguée, plus précise que la commune nouvelle dont la base garde le code.
        code = None if par_nom[i] else d.at[i, "code_commune"]
        c, _ = communes.trouver(code, d.at[i, "code_departement"], d.at[i, "commune"])
        if c is not None:
            (d.at[i, "lon"], d.at[i, "lat"]), d.at[i, "ap_point"] = communes.position(c)
            d.at[i, "commune_affichee"] = c["nom"]
            trouve[i] = True
    d.loc[trouve, "ap"] = 1
    d.loc[manque & ~trouve, "ap"] = 3
    d["nom_affiche"] = d["nom_affiche"].fillna(d["nom"].map(nom_lisible))
    capitales = d["nom_affiche"].str.upper().eq(d["nom_affiche"])  # quelques noms de l'annuaire sont en capitales
    d.loc[capitales, "nom_affiche"] = d.loc[capitales, "nom_affiche"].map(nom_lisible)
    d["nom_affiche"] = d["nom_affiche"].map(typographie)
    d["commune_affichee"] = d["commune_affichee"].fillna(d["commune"].map(lambda s: espaces(str(s)).title()))

    # Dépense par élève, recalculée, et décomposition en cinq groupes (arrondis qui conservent le total).
    d["v_exact"] = d["depense_publique"] / d["eleves"]
    prive_2d = d["secteur"].eq("prive_sc") & ~pr
    forfait = d["etat_forfait_prive_internats"]
    n = d["eleves"]
    exact = np.column_stack([
        d["etat_enseignants"] / n,
        (d["etat_vie_scolaire"] + d["etat_pilotage_admin"] + forfait.where(prive_2d, 0)) / n,
        (d[AUTRES_ETAT].sum(axis=1) + forfait.where(~prive_2d, 0)) / n,
        d["ct_ecoles"] / n, d["ct_colleges"] / n, d["ct_lycees"] / n, d["ct_transports"] / n,
        d["apu_par_eleve"] / n])
    assert np.allclose(exact.sum(axis=1), d["v_exact"], atol=0.01)
    d["v"] = [arrondi(x) for x in d["v_exact"]]
    parts = np.vstack([arrondi_somme(row, tot) for row, tot in zip(exact, d["v"])])
    for j, c in enumerate(["g1", "g2", "g3", "g4c", "g4d", "g4r", "g4t", "g5"]):
        d[c] = parts[:, j]
    # Nature des clés des collectivités (script 04), là où le montant existe.
    for c, g in (("cle_commune", "g4c"), ("cle_departement", "g4d"), ("cle_region", "g4r")):
        d[c] = d[c].where(d[g].gt(0))

    # Établissements non classés : la comparaison avec le groupe n'a pas de sens (H-B18).
    contrat = d["uai"].map(ann["type_contrat_prive"]).fillna("")
    d["nc"] = np.select([
        pr & d["etp"].isna(),
        ~pr & d["secteur"].eq("public") & (d["etat_vie_scolaire"].eq(0) | d["etat_pilotage_admin"].eq(0)),
        pr & d["secteur"].eq("prive_sc") & contrat.str.contains(CONTRAT_PARTIEL),
        d["type_inconnu"]], [1, 2, 3, 5], 0)
    grp = d.groupby(["typ", "secteur"])
    d.loc[d["nc"].eq(0) & grp["uai"].transform("count").lt(SEUIL_GROUPE), "nc"] = 4

    # Comparaison avec le groupe (même type, même secteur) : moyenne de tous ses établissements (comme B2) ; écart et
    # rang pour les seuls établissements classés, le rang sur la dépense arrondie affichée.
    d["moyenne_groupe"] = grp["depense_publique"].transform("sum") / grp["eleves"].transform("sum")
    classe = d["nc"].eq(0)
    d["ecart"] = (100 * (d["v_exact"] / d["moyenne_groupe"] - 1)).where(classe)
    gc = d[classe].groupby(["typ", "secteur"])["v"]
    d["n_comparables"] = gc.transform("count").reindex(d.index)
    d["n_moins_chers"] = (gc.rank(method="min") - 1).reindex(d.index)
    d["rang"] = 100 * d["n_moins_chers"] / d["n_comparables"]
    return d.sort_values("uai").reset_index(drop=True)


# ---------------------------------------------------------------------------------------------- fond de carte
def arrondir_geom(geom, k=4):
    def anneau(a):
        out = []
        for x, y in a:
            p = [round(x, k), round(y, k)]
            if not out or p != out[-1]:
                out.append(p)
        return out if len(out) >= 4 else None
    polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
    res = []
    for poly in polys:
        rings = [r for r in (anneau(a) for a in poly) if r]
        if rings:
            res.append(rings)
    return {"type": "MultiPolygon", "coordinates": res}


def point_etiquette(geom):
    """Position de l'étiquette : barycentre du plus grand polygone s'il est à l'intérieur ; sinon (département en
    croissant, comme les Hauts-de-Seine autour de Paris), milieu du plus long segment intérieur sur la même latitude."""
    best, best_a, best_poly = None, -1, None
    for poly in geom["coordinates"]:
        r = poly[0]
        a = sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(r, r[1:])) / 2
        if abs(a) > best_a:
            cx = sum((x0 + x1) * (x0 * y1 - x1 * y0) for (x0, y0), (x1, y1) in zip(r, r[1:])) / (6 * a)
            cy = sum((y0 + y1) * (x0 * y1 - x1 * y0) for (x0, y0), (x1, y1) in zip(r, r[1:])) / (6 * a)
            best, best_a, best_poly = [cx, cy], abs(a), poly
    cx, cy = best
    xs = sorted(x0 + (cy - y0) * (x1 - x0) / (y1 - y0)
                for ring in best_poly for (x0, y0), (x1, y1) in zip(ring, ring[1:]) if (y0 > cy) != (y1 > cy))
    segments = list(zip(xs[0::2], xs[1::2]))   # parties de la latitude cy situées à l'intérieur (pair-impair)
    if segments and not any(a <= cx <= b for a, b in segments):
        a, b = max(segments, key=lambda s: s[1] - s[0])
        cx = (a + b) / 2
    return [round(cx, 4), round(cy, 4)]


def fond_de_carte() -> dict:
    dep = json.loads((CARTO / "etalab_contours_departements_2025_100m.geojson").read_text(encoding="utf-8"))
    reg = json.loads((CARTO / "etalab_contours_regions_2025_100m.geojson").read_text(encoding="utf-8"))
    garder = lambda c: len(c) == 2 or c in OUTRE_MER  # noqa: E731 — métropole et DROM, Saint-Martin, Saint-Barthélemy
    deps, regs = [], []
    for f in dep["features"]:
        c = f["properties"]["code"]
        if garder(c):
            g = arrondir_geom(f["geometry"])
            deps.append({"type": "Feature", "properties": {"code": c, "nom": f["properties"]["nom"], "lab": point_etiquette(g)},
                         "geometry": g})
    for f in reg["features"]:
        c = f["properties"]["code"]
        if len(c) == 2:  # régions de métropole (11 à 94) et DROM (01 à 06)
            g = arrondir_geom(f["geometry"])
            regs.append({"type": "Feature", "properties": {"code": c, "nom": f["properties"]["nom"], "lab": point_etiquette(g)},
                         "geometry": g})
    communes, api = [], Communes()
    for f, arr in (("api_geo_communes_2026-10-04.json", 0), ("api_geo_arrondissements_municipaux_2026-10-04.json", 1)):
        for c in json.loads((CARTO / f).read_text(encoding="utf-8")):
            dep_c = c.get("codeDepartement") or ""
            if not (len(dep_c) == 2 or dep_c in OUTRE_MER):
                continue
            (x, y), _ = api.position(c)
            nom = re.sub(r"^(Paris|Lyon|Marseille) (\d+)(er|e) Arrondissement$", r"\2\3 arr.", c["nom"]) if arr else c["nom"]
            communes.append([nom, round(x, 4), round(y, 4), int(c.get("population") or 0), arr])
    communes.sort(key=lambda r: -r[3])
    return {"deps": {"type": "FeatureCollection", "features": deps},
            "regs": {"type": "FeatureCollection", "features": regs}, "communes": communes}


# ---------------------------------------------------------------------------------------------- sorties
LIB_AP = {0: "adresse (annuaire)", 1: "mairie de la commune (absent de l'annuaire actuel)",  # ou centre, voir table_csv
          2: "commune seulement (annuaire)", 3: "inconnue", 4: "incertaine (annuaire)"}
COLONNES = [  # (nom, description) : dictionnaire écrit à côté du CSV
    ("uai", "Identifiant national de l'établissement (UAI)."),
    ("nom", "Nom de l'annuaire de l'éducation (typographie harmonisée) ; pour les établissements absents de l'annuaire "
            "actuel, nom de la base reconstitué à partir des capitales (sans accents)."),
    ("commune", "Commune de l'annuaire ; à défaut, commune de l'API Découpage administratif."),
    ("code_commune", "Code Insee de la commune ou de l'arrondissement municipal : annuaire ; à défaut fichier IPS (écoles) ou "
                     "fichiers des collèges et des lycées généraux et technologiques (second degré) ; à défaut nom de la "
                     "commune dans le département (écoles fermées depuis, H-E4)."),
    ("code_departement", "Département (977 et 978 pour les écoles de Saint-Barthélemy et de Saint-Martin)."),
    ("region", "Région académique."),
    ("type", "Type d'établissement : écoles d'après les élèves par niveau, à défaut l'annuaire puis le nom (voir "
             "type_source) ; second degré d'après la nature officielle (H-B16)."),
    ("type_source", "Écoles : source du type (effectifs, annuaire, nom ou inconnu)."),
    ("secteur", "Public ou privé sous contrat."),
    ("latitude", "Latitude WGS84 (5 décimales)."), ("longitude", "Longitude WGS84 (5 décimales)."),
    ("position", "Origine de la position : adresse de l'annuaire, commune seulement, incertaine, ou, pour un établissement "
                 "absent de l'annuaire actuel, mairie de la commune (centre si l'API ne donne pas de mairie propre)."),
    ("eleves_rentree2024", "Élèves de la rentrée 2024 (apprentis et étudiants exclus)."),
    ("dont_maternelle_ou_college", "Écoles : élèves de préélémentaire hors ULIS ; 2nd degré : élèves du collège (Segpa comprise). "
                                   "Vide si non publié."),
    ("dont_elementaire_ou_voie_gt", "Écoles : élèves d'élémentaire hors ULIS ; 2nd degré : voie générale et technologique. "
                                    "Vide si non publié."),
    ("dont_ulis_ecole_ou_voie_pro", "Écoles : élèves d'ULIS et d'UEEA ; 2nd degré : voie professionnelle. Vide si non publié."),
    ("classes_ecole", "Écoles : nombre de classes."),
    ("etudiants_sts_cpge_non_comptes", "Lycées : étudiants de STS et de CPGE (hors champ ; part de leurs heures et personnels retirée)."),
    ("effectif_sts_cpge_masque", "1 si l'effectif post-bac est en partie ou en totalité masqué (« ns ») dans la source."),
    ("etp_enseignants_tous_niveaux", "Équivalents temps plein d'enseignants (post-bac compris) ; vide si non publié."),
    ("heures_enseignement_par_eleve_HE", "Heures d'enseignement hebdomadaires devant élèves par élève (niveaux du secondaire)."),
    ("couverture_HE_%", "Part des élèves présents dans le fichier H/E (peut dépasser 100 : fichiers différents)."),
    ("indice_cout_corps_enseignants", "Coût relatif des corps d'enseignants (1 = moyenne des titulaires du 2nd degré) ; vide "
                                      "si aucun ETP n'est publié (1 dans le calcul)."),
    ("ips", "Indice de position sociale (rentrée 2024)."),
    ("ips_statut", "publié, non publié (NS : effectif trop faible) ou absent."),
    ("education_prioritaire", "REP ou REP+."),
    ("depense_publique_par_eleve_€", "Dépense publique estimée par élève en 2025 (arrondie à l'euro)."),
    ("dont_enseignants_€", "État : enseignants."),
    ("dont_vie_scolaire_direction_encadrement_€", "État : vie scolaire et direction (public), encadrement pédagogique "
                                                  "(écoles publiques), forfait d'externat (privé du 2nd degré)."),
    ("dont_autres_credits_etat_€", "État : remplacement, formation, AESH, santé, actions éducatives, bourses, administration "
                                   "centrale et académique (et internats publics), répartis par élève."),
    ("dont_commune_€", "Commune (écoles) : financement des écoles par les collectivités (compte de l'éducation)."),
    ("dont_departement_€", "Département : collégiens."), ("dont_region_€", "Région : lycéens."),
    ("dont_transports_scolaires_€", "Transports scolaires (même montant par élève)."),
    ("dont_caf_autres_apu_€", "Autres administrations publiques, surtout l'allocation de rentrée scolaire (élèves de 6 ans et plus)."),
    ("cle_commune", "Clé de répartition de la ligne commune (dépense par élève de la commune d'après ses comptes 2025, "
                    "plafonnée ou relevée aux 99e et 1er centiles ; moyenne des communes ; forfait national du privé) ; "
                    "les montants sont recalés sur le total du compte de l'éducation."),
    ("cle_departement", "Clé de la ligne département (dépense par collégien du département, moyenne nationale, montant "
                        "national du privé), recalée sur les comptes 2025 des départements."),
    ("cle_region", "Clé de la ligne région (dépense par lycéen de la région, valeur de la Guadeloupe pour Saint-Martin et "
                   "Saint-Barthélemy, moyenne nationale, montant national du privé), recalée sur les comptes 2025 des régions."),
    ("moyenne_meme_type_et_secteur_€", "Moyenne de la dépense par élève du groupe (même type, même secteur), pondérée par les élèves."),
    ("comparaison", "Vide si l'établissement est comparé à son groupe ; sinon, la raison pour laquelle il ne l'est pas."),
    ("ecart_a_la_moyenne_%", "Écart de la dépense par élève à la moyenne du groupe (établissements comparés seulement)."),
    ("etablissements_comparables", "Établissements comparés dans le groupe."),
    ("dont_moins_chers", "Parmi eux, ceux dont la dépense par élève (arrondie) est strictement plus faible."),
    ("part_moins_chers_%", "dont_moins_chers / etablissements_comparables × 100."),
]


def table_csv(d: pd.DataFrame) -> pd.DataFrame:
    pr = d["degre"].eq("1er degré")
    out = pd.DataFrame({
        "uai": d["uai"], "nom": d["nom_affiche"], "commune": d["commune_affichee"], "code_commune": d["code_commune"],
        "code_departement": d["code_departement"], "region": d["region"], "type": d["typ"].map(TYPES),
        "type_source": d["type_source"],
        "secteur": d["secteur"].map({"public": "public", "prive_sc": "privé sous contrat"}),
        "latitude": decimales(d["lat"].where(d["ap"].ne(3)), 1e5), "longitude": decimales(d["lon"].where(d["ap"].ne(3)), 1e5),
        "position": d["ap"].map(LIB_AP).where(~(d["ap"].eq(1) & d["ap_point"].eq("centre")),
                                              "centre de la commune (absent de l'annuaire actuel)"),
        "eleves_rentree2024": d["eleves"].round().astype("Int64"),
        "dont_maternelle_ou_college": d["n1"].round().astype("Int64"),
        "dont_elementaire_ou_voie_gt": d["n2"].round().astype("Int64"),
        "dont_ulis_ecole_ou_voie_pro": d["n3"].round().astype("Int64"),
        "classes_ecole": pd.to_numeric(d["classes"], errors="coerce").round().astype("Int64"),
        "etudiants_sts_cpge_non_comptes": pd.to_numeric(d["etudiants_postbac"], errors="coerce").round().astype("Int64"),
        "effectif_sts_cpge_masque": pd.Series(np.where(pr, None, d["postbac_masque"]), dtype="Int64"),
        "etp_enseignants_tous_niveaux": decimales(d["etp"], 10),
        "heures_enseignement_par_eleve_HE": decimales(d["he"], 100),
        "couverture_HE_%": decimales(100 * pd.to_numeric(d["couverture_he"], errors="coerce"), 10),
        "indice_cout_corps_enseignants": decimales(d["indice"], 1000),
        "ips": decimales(d["ips"], 10), "ips_statut": d["ips_statut"],
        "education_prioritaire": np.select([d["rep_plus"].eq(1), d["rep"].eq(1)], ["REP+", "REP"], ""),
        "depense_publique_par_eleve_€": d["v"],
        "dont_enseignants_€": d["g1"], "dont_vie_scolaire_direction_encadrement_€": d["g2"],
        "dont_autres_credits_etat_€": d["g3"], "dont_commune_€": d["g4c"], "dont_departement_€": d["g4d"],
        "dont_region_€": d["g4r"], "dont_transports_scolaires_€": d["g4t"], "dont_caf_autres_apu_€": d["g5"],
        "cle_commune": d["cle_commune"].map(LIB_CLE["cle_commune"]),
        "cle_departement": d["cle_departement"].map(LIB_CLE["cle_departement"]),
        "cle_region": d["cle_region"].map(LIB_CLE["cle_region"]),
        "moyenne_meme_type_et_secteur_€": d["moyenne_groupe"].map(arrondi),
        "comparaison": d["nc"].map(NON_CLASSE).fillna(""),
        "ecart_a_la_moyenne_%": decimales(d["ecart"], 10),
        "etablissements_comparables": d["n_comparables"].astype("Int64"),
        "dont_moins_chers": d["n_moins_chers"].astype("Int64"),
        "part_moins_chers_%": decimales(d["rang"], 10),
    })
    assert list(out.columns) == [c for c, _ in COLONNES]
    return out


def dictionnaire() -> str:
    lignes = ["# Colonnes de `carte_etablissements_2025.csv`", "",
              "Une ligne par établissement de l'approche B (script `scripts/07_carte_etablissements.py`). Séparateur « ; », "
              "décimale « . », encodage UTF-8 avec BOM ; case vide = valeur inconnue ou sans objet. Hypothèses : H-B18 "
              "(hypotheses.md).", "", "| Colonne | Contenu |", "|---|---|"]
    lignes += [f"| `{c}` | {t} |" for c, t in COLONNES]
    return "\n".join(lignes) + "\n"


def donnees_page(d: pd.DataFrame) -> dict:
    communes = sorted(d["commune_affichee"].unique())
    idx_c = {c: i for i, c in enumerate(communes)}
    regions = sorted(d["region"].unique(), key=lambda s: s.replace("Î", "I"))
    idx_r = {r: i for i, r in enumerate(regions)}
    deps = sorted(d["code_departement"].unique())
    idx_d = {c: i for i, c in enumerate(deps)}
    pos = d["ap"].ne(3)
    grp = d.groupby(["typ", "secteur"])
    refs = {f"{t}|{SECTEUR[s]}": arrondi(v) for (t, s), v in grp["moyenne_groupe"].first().items()}
    tailles = {f"{t}|{SECTEUR[s]}": int(v) for (t, s), v in grp["uai"].count().items()}
    statut = lambda s: [None if pd.isna(x) else STATUT_CLE[x] for x in s]  # noqa: E731
    return {
        "n": len(d), "types": TYPES, "refs": refs, "tailles": tailles, "seuil_groupe": SEUIL_GROUPE,
        "non_classe": NON_CLASSE, "communes": communes, "regions": regions, "deps": deps,
        "uai": d["uai"].tolist(), "nom": d["nom_affiche"].tolist(), "com": d["commune_affichee"].map(idx_c).tolist(),
        "dep": d["code_departement"].map(idx_d).tolist(), "reg": d["region"].map(idx_r).tolist(),
        "typ": d["typ"].tolist(), "sec": d["secteur"].map(SECTEUR).tolist(),
        "lat": [x if p else None for x, p in zip(entiers(d["lat"], 1e5), pos)],
        "lon": [x if p else None for x, p in zip(entiers(d["lon"], 1e5), pos)],
        "ap": d["ap"].astype(int).tolist(), "apc": (d["ap"].eq(1) & d["ap_point"].eq("centre")).astype(int).tolist(), "e": entiers(d["eleves"]), "n1": entiers(d["n1"]), "n2": entiers(d["n2"]),
        "n3": entiers(d["n3"]), "cls": entiers(d["classes"]), "pb": entiers(d["etudiants_postbac"]),
        "pbns": d["postbac_masque"].astype(int).tolist(), "etp": entiers(d["etp"], 10), "he": entiers(d["he"], 100),
        "cov": entiers(d["couverture_he"], 1000), "ix": entiers(d["indice"], 1000), "ips": entiers(d["ips"], 10),
        "ipsS": d["ips_statut"].map({"publié": 0, "non publié (NS)": 1, "absent": 2}).tolist(),
        "rep": np.select([d["rep_plus"].eq(1), d["rep"].eq(1)], [2, 1], 0).tolist(),
        "v": d["v"].tolist(), "g1": d["g1"].tolist(), "g2": d["g2"].tolist(), "g3": d["g3"].tolist(),
        "g4c": d["g4c"].tolist(), "g4d": d["g4d"].tolist(), "g4r": d["g4r"].tolist(), "g4t": d["g4t"].tolist(),
        "g5": d["g5"].tolist(), "kc": statut(d["cle_commune"]), "kd": statut(d["cle_departement"]),
        "kr": statut(d["cle_region"]), "nc": d["nc"].astype(int).tolist(), "ecart": entiers(d["ecart"], 10),
        "ts": d["type_source"].map({"annuaire": 1, "nom": 2, "inconnu": 3}).fillna(0).astype(int).tolist(),
    }


def comprime(o) -> str:
    brut = json.dumps(o, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return base64.b64encode(gzip.compress(brut, compresslevel=9, mtime=0)).decode("ascii")


def page(d: pd.DataFrame, fond: dict) -> str:
    modele = MODELE.read_text(encoding="utf-8")
    remplacements = {"/*LEAFLET_CSS*/": LEAFLET_CSS.read_text(encoding="utf-8"),
                     "DONNEES_GZ_BASE64": comprime(donnees_page(d)), "FOND_GZ_BASE64": comprime(fond)}
    for jeton, valeur in remplacements.items():
        assert modele.count(jeton) == 1, jeton
        modele = modele.replace(jeton, valeur)
    return modele


def document_complet(fragment: str) -> str:
    """Page autonome pour un usage local : l'en-tête (titre, polices, styles) passe dans <head>."""
    i = fragment.index('<div class="page"')
    return ("<!doctype html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            + fragment[:i] + "</head>\n<body>\n" + fragment[i:] + "\n</body>\n</html>\n")


def main(artefact=None):
    d = etablissements()
    # Contrôles : département cohérent avec la commune ; dépense et décomposition ; positions.
    code = d["code_commune"].astype(str)
    pref = np.where(code.str.startswith("97"), code.str[:3], code.str[:2])
    ok = d["code_commune"].isna() | (pd.Series(pref, index=d.index) == d["code_departement"]) | d["absent_annuaire"]
    print("Contrôle : département ≠ préfixe de la commune pour", int((~ok).sum()), "établissements :",
          d.loc[~ok, ["uai", "code_commune", "code_departement"]].head(5).values.tolist())
    assert (d[["g1", "g2", "g3", "g4c", "g4d", "g4r", "g4t", "g5"]].sum(axis=1) == d["v"]).all()
    table_csv(d).to_csv(RESULTATS / "carte_etablissements_2025.csv", sep=";", index=False, encoding="utf-8-sig")
    (RESULTATS / "carte_etablissements_2025_colonnes.md").write_text(dictionnaire(), encoding="utf-8")
    fragment = page(d, fond_de_carte())
    (RESULTATS / "carte_etablissements.html").write_text(document_complet(fragment), encoding="utf-8")
    if artefact:
        with open(artefact, "w", encoding="utf-8") as f:
            f.write(fragment)
    pos = d[d["ap"].ne(3)]
    meme_point = pos.groupby([pd.Series(entiers(pos["lat"], 1e5), index=pos.index),
                              pd.Series(entiers(pos["lon"], 1e5), index=pos.index)])["uai"].transform("count").gt(1)
    print(f"Carte : {len(d)} établissements ; positions : annuaire {int((d['ap'] == 0).sum())}, commune selon l'annuaire "
          f"{int((d['ap'] == 2).sum())}, incertaine {int((d['ap'] == 4).sum())}, mairie de la commune "
          f"{int((d['ap'] == 1).sum())} ({int(d.loc[d['ap'] == 1, 'eleves'].sum())} élèves), inconnue {int((d['ap'] == 3).sum())} ; "
          f"absents de l'annuaire {int(d['absent_annuaire'].sum())} ; au même point qu'un autre {int(meme_point.sum())} ; "
          f"page de {len(fragment.encode('utf-8')) / 1e6:.2f} Mo")
    print("Écoles typées d'après :", d.loc[d["degre"].eq("1er degré"), "type_source"].value_counts().to_dict())
    print("Non classés :", {NON_CLASSE[k]: int(v) for k, v in d.loc[d["nc"] > 0, "nc"].value_counts().items()},
          "; élèves :", int(d.loc[d["nc"] > 0, "eleves"].sum()))
    print("Clés communales (écoles publiques) :", d.loc[d["degre"].eq("1er degré") & d["secteur"].eq("public"),
                                                       "cle_commune"].value_counts().to_dict())
    print(d.groupby(["typ", "secteur"]).agg(n=("uai", "count"), eleves=("eleves", "sum"),
                                            moyenne=("moyenne_groupe", "first")).round().to_string())


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--artefact", help="chemin de la version « fragment » de la page (publication)")
    main(ap.parse_args().artefact)
