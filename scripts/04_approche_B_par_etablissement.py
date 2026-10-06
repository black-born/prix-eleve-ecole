"""Approche B — dépense publique par élève reconstituée ÉTABLISSEMENT PAR ÉTABLISSEMENT (année 2025).

Idée de départ de l'étudiant : pour chaque école, collège et lycée, additionner toutes les dépenses publiques
qui le concernent, puis diviser par son nombre d'élèves. Aucune source publique ne donne ces dépenses
établissement par établissement : on répartit donc chaque enveloppe officielle de 2025 entre établissements
avec la clé la plus fine disponible en open data (hypothèses H-B1 à H-B17 dans hypotheses.md).

  ÉTAT (RAP 2025, crédits de paiement exécutés, mission « Enseignement scolaire », hors outre-mer COM)
    - enseignement du 1er degré : au prorata des ETP d'enseignants de l'école ;
    - enseignement du 2nd degré : actions d'enseignement mutualisées (y compris post-bac et besoins
      particuliers), réparties au prorata des heures d'enseignement de tous niveaux × indice de coût des corps,
      puis retrait de la part des heures post-bac (STS, CPGE), hors champ ;
    - vie scolaire : au prorata des ETP de vie scolaire ; direction-administration : ETP « autres personnels » ;
    - le reste (remplacement, formation, AESH, santé, bourses, soutien…) : à parts égales par élève.
  COLLECTIVITÉS
    - écoles : total du compte de l'éducation (DEPP), plus les fournitures scolaires achetées pour les écoles,
      réparti selon la dépense de fonctionnement « écoles » par élève de la commune (DGFiP 2025) quand elle est
      connue, sinon selon la moyenne ;
    - collèges / lycées : comptes 2025 des départements et des régions (DGFiP), répartis selon la dépense par
      collégien du département / par lycéen de la région (Géographie de l'École 2026) ;
    - transports scolaires : compte de l'éducation (DEPP), par élève.
  AUTRES ADMINISTRATIONS PUBLIQUES (surtout l'allocation de rentrée scolaire des CAF) : par élève, par degré
    (1er degré : élèves de 6 ans et plus, seuls concernés par l'allocation).

Établissements : rentrée 2024 (année scolaire 2024-2025), base construite par 03_base_etablissements.py.
"""
import unicodedata

import numpy as np
import pandas as pd

from commun import BRUT, RACINE, RESULTATS, Classeur, Journal, ecrire_csv, euros

TRAITE = RACINE / "data" / "processed"
journal = Journal()
intrants = []  # paramètres lus dans des extractions CSV (traçabilité hors Excel)


def intrant(cle: str, valeur: float, fichier: str, ligne: str) -> float:
    intrants.append({"cle": cle, "valeur": valeur, "fichier": fichier, "ligne_ou_cellule": ligne})
    return valeur


b1 = pd.read_csv(TRAITE / "base_ecoles_rentree2024.csv", sep=";", low_memory=False, dtype={"code_commune": str})
b2_tous = pd.read_csv(TRAITE / "base_2d_rentree2024.csv", sep=";", low_memory=False, dtype={"code_departement": str})
for b in (b1, b2_tous):
    b["eleves"] = b["eleves"].fillna(0)
    b["etp_enseignants"] = b["etp_enseignants"].fillna(0)

# =================================================================== 1. ÉTAT : enveloppes 2025
F_ACT = "data/raw/budget_etat/extractions/rap2025_execution_par_action_2024_2025.csv"
act = pd.read_csv(RACINE / F_ACT, sep=";").set_index(["programme", "action"])
F_G5 = "data/raw/budget_etat/extractions/passerelle_G5_intrants_RAP_DPT_2024_2025.csv"
g5 = pd.read_csv(RACINE / F_G5, sep=";").set_index("id")["valeur"].astype(float)
# Dépenses de la mission dans les collectivités d'outre-mer (COM), exécution 2024 (DPT Outre-mer 2026),
# retirées au prorata des actions du programme (H-B2) : le champ est la France (métropole + DROM).
COM = {p: intrant(f"com_p{p}_2024", g5[f"com_p{p}_2024"], F_G5, f"id=com_p{p}_2024")
       for p in (139, 140, 141, 214, 230)}
# Allocations de stage des lycéens professionnels (PFMP, hors titre 2) : exclues, comme dans le compte (H-B3).
PFMP = {(141, 3): intrant("pfmp_p141_2025", g5["pfmp_p141_2025"], F_G5, "id=pfmp_p141_2025"),
        (139, 5): intrant("pfmp_p139_2025", g5["pfmp_p139_2025"], F_G5, "id=pfmp_p139_2025")}
TOTAL_PROG = {p: float(act.loc[p, "CP_conso_2025"].sum()) for p in (139, 140, 141, 214, 230)}
COLONNE = {"total": "CP_conso_2025", "T2": "CP_conso_2025_titre2", "HT2": "CP_conso_2025_hors_titre2"}


def credits(prog: int, actions, part: str = "total") -> float:
    """CP exécutés 2025 des actions (titre 2, hors titre 2 ou total), PFMP et part des COM retirées."""
    brut = 0.0
    for a in actions:
        v = float(act.loc[(prog, a), COLONNE[part]])
        intrant(f"P{prog}.a{a:02d}.{part}.CP2025", v, F_ACT, f"programme={prog};action={a};colonne={COLONNE[part]}")
        if part in ("total", "HT2"):
            v -= PFMP.get((prog, a), 0.0)
        brut += v
    return brut * (1 - COM[prog] / TOTAL_PROG[prog])


# Indice de coût relatif des corps (H-B5) — salaires nets moyens 2024 (DEPP NI 26.36 ; Panorama 2025-2026).
cp = BRUT / "couts_personnels"
ni2636 = Classeur(cp / "DEPP_NI_26-36_donnees.xlsx", journal)
pano = Classeur(cp / "DEPP_Panorama_personnels_2025-2026_chapitre7_donnees.xlsx", journal)
sal = {
    "agreges": ni2636.lire_cellule("net.agreges", "Figure 1", "D8", libelle_ligne="Professeurs agrégés"),
    "certifies": ni2636.lire_cellule("net.certifies", "Figure 1", "D5", libelle_ligne="Professeurs certifiés"),
    "eps": ni2636.lire_cellule("net.eps", "Figure 1", "D6", libelle_ligne="Professeurs d'EPS"),
    "plp": ni2636.lire_cellule("net.plp", "Figure 1", "D7", libelle_ligne="Professeurs de lycée professionnel"),
    "pe": ni2636.lire_cellule("net.pe", "Figure 1", "D4", libelle_ligne="Professeurs des écoles"),
    "fonct_2d": ni2636.lire_cellule("net.2d", "Figure 6 - Web ", "H7", libelle_ligne="2d degré"),
}
n_cert = ni2636.lire_cellule("eff.certifies", "Figure 7 - Web", "B6", libelle_ligne="Professeurs certifiés")
n_eps = ni2636.lire_cellule("eff.eps", "Figure 7 - Web", "B7", libelle_ligne="Professeurs d'EPS")
eqtp_contr = pano.lire_cellule("eqtp.contractuels", "7.3", "G21", libelle_ligne="Contractuels et maîtres délégués")
eqtp_fonct2d_pub = pano.lire_cellule("eqtp.fonct2d.public", "7.3", "G19", libelle_ligne="Public")
INDICE = {
    "etp_agreges": sal["agreges"] / sal["fonct_2d"],
    "etp_certifies": (sal["certifies"] * n_cert + sal["eps"] * n_eps) / (n_cert + n_eps) / sal["fonct_2d"],
    "etp_plp": sal["plp"] / sal["fonct_2d"],
    "etp_autres_titulaires": sal["pe"] / sal["fonct_2d"],    # surtout des professeurs des écoles (Segpa, EREA)
    "etp_non_titulaires": eqtp_contr / eqtp_fonct2d_pub,     # rapport en équivalent temps plein
}
corps = list(INDICE)
b2_tous[corps] = b2_tous[corps].fillna(0)
b2_tous["indice_cout_enseignant"] = np.where(
    b2_tous["etp_enseignants"] > 0,
    sum(b2_tous[c] * INDICE[c] for c in corps) / b2_tous["etp_enseignants"].replace(0, np.nan), 1.0)
b2_tous["indice_cout_enseignant"] = b2_tous["indice_cout_enseignant"].fillna(1.0)

# Heures hebdomadaires d'enseignement et élèves par niveau (indicateur H/E), par établissement (H-B4).
ETAB = BRUT / "etablissements"
h = pd.concat([pd.read_csv(ETAB / "moyens_enseignants_2d_public_rentree2024.csv", sep=";", low_memory=False)
               .assign(secteur_he="public"),
               pd.read_csv(ETAB / "moyens_enseignants_2d_prive_rentree2024.csv", sep=";", low_memory=False)
               .assign(secteur_he="prive_sc")])
h = h[h["uai"].astype(str).str.len() == 8].copy()  # retire les lignes de totaux
HCOL = "numerateur_h_e_nb_heures_enseignement_hebdo_devant_eleves"
ECOL = "denominateur_h_e_somme_eleves_en_division"
for c in (HCOL, ECOL):
    h[c] = pd.to_numeric(h[c], errors="coerce").fillna(0)
BLOC = {"Collège": "college", "Prépa seconde": "lycee_gt", "Lycée général et technologique": "lycee_gt",
        "Lycée professionnel": "lycee_pro", "Segpa": "bep", "Établissement régional d'enseignement adapté": "bep",
        "STS": "postbac", "CPGE": "postbac"}
h["bloc"] = h["niveau"].map(BLOC)
assert h["bloc"].notna().all(), h.loc[h["bloc"].isna(), "niveau"].unique()
heures = h.pivot_table(index="uai", columns="bloc", values=HCOL, aggfunc="sum", fill_value=0).add_prefix("h_")
etud_pb = h[h["bloc"].eq("postbac")].groupby("uai")[ECOL].sum().rename("etudiants_postbac")
eleves_he = h[h["bloc"].ne("postbac")].groupby("uai")[ECOL].sum().rename("eleves_he")  # élèves en division publiés
b2_tous = (b2_tous.drop(columns=[c for c in b2_tous.columns if c.startswith("h_")])
           .merge(heures, left_on="uai", right_index=True, how="left")
           .merge(etud_pb, left_on="uai", right_index=True, how="left")
           .merge(eleves_he, left_on="uai", right_index=True, how="left"))
H_SEC = ["h_college", "h_lycee_gt", "h_lycee_pro", "h_bep"]
for c in H_SEC + ["h_postbac", "etudiants_postbac", "eleves_he"]:
    b2_tous[c] = b2_tous[c].fillna(0)
# Sans heures H/E mais avec élèves : élèves de chaque niveau × H/E moyen du niveau et du secteur (H-B6).
sommes = h.groupby(["secteur_he", "bloc"])[[HCOL, ECOL]].sum()
HE_MOYEN = (sommes[HCOL] / sommes[ECOL]).to_dict()
sans_h = b2_tous[H_SEC].sum(axis=1).eq(0) & b2_tous["eleves"].gt(0)
for c, e, bloc in (("h_college", "eleves_college", "college"), ("h_lycee_gt", "eleves_lycee_gt", "lycee_gt"),
                   ("h_lycee_pro", "eleves_lycee_pro", "lycee_pro")):
    b2_tous.loc[sans_h, c] = b2_tous.loc[sans_h, e] * b2_tous.loc[sans_h, "secteur"].map(
        lambda s: HE_MOYEN[(s, bloc)])
# Heures publiées pour moins de 90 % des élèves (niveau masqué « ns » ou absent du fichier H/E) : les heures des
# élèves manquants = élèves manquants × H/E moyen des établissements du même type et du même secteur (H-B6).
b2_tous["couverture_he"] = (b2_tous["eleves_he"] / b2_tous["eleves"].where(b2_tous["eleves"] > 0)).fillna(0)
complet = b2_tous["eleves"].gt(0) & b2_tous["couverture_he"].ge(0.9)
cles = ["type", "secteur"]
he_type = (b2_tous[complet].groupby(cles)[H_SEC].sum().sum(axis=1)
           / b2_tous[complet].groupby(cles)["eleves_he"].sum())
he_secteur = (b2_tous[complet].groupby("secteur")[H_SEC].sum().sum(axis=1)
              / b2_tous[complet].groupby("secteur")["eleves_he"].sum())
partiel = ~sans_h & b2_tous["eleves"].gt(0) & b2_tous["couverture_he"].lt(0.9)
b2_tous["h_impute"] = 0.0
b2_tous.loc[partiel, "h_impute"] = [
    (e - ehe) * he_type.get((t, s), he_secteur[s])
    for e, ehe, t, s in b2_tous.loc[partiel, ["eleves", "eleves_he", "type", "secteur"]].itertuples(index=False)]
b2_tous["h_secondaire"] = b2_tous[H_SEC].sum(axis=1) + b2_tous["h_impute"]
b2_tous["heures_ponderees_secondaire"] = b2_tous["h_secondaire"] * b2_tous["indice_cout_enseignant"]
b2_tous["heures_ponderees_postbac"] = b2_tous["h_postbac"] * b2_tous["indice_cout_enseignant"]

# Seuls les établissements ayant des élèves du secondaire portent des dépenses (H-B12). Les établissements
# post-bac seuls restent dans le dénominateur de la clé d'enseignement (leurs heures sont hors champ).
b1 = b1[b1["eleves"] > 0].copy()
b2 = b2_tous[b2_tous["eleves"] > 0].copy()
pub1, prv1 = b1["secteur"].eq("public"), b1["secteur"].eq("prive_sc")
pub2, prv2 = b2["secteur"].eq("public"), b2["secteur"].eq("prive_sc")

POSTES = ["etat_enseignants", "etat_remplacement_formation", "etat_vie_scolaire", "etat_pilotage_admin",
          "etat_inclusion_sante_social", "etat_activites_educatives", "etat_aides_familles",
          "etat_forfait_prive_internats", "etat_soutien_administration",
          "ct_ecoles", "ct_colleges", "ct_lycees", "ct_transports", "apu_par_eleve"]
for b in (b1, b2):
    for p in POSTES:
        b[p] = 0.0
enveloppes = []


def repartir(montant: float, cible: list[tuple[pd.DataFrame, pd.Series, pd.Series]], poste: str, nom: str,
             cle: str, population: str, denominateur: float | None = None) -> float:
    """Répartit `montant` au prorata de la clé ; `denominateur` > somme des clés = part hors champ non répartie."""
    total = sum(float(c[m].sum()) for _, m, c in cible)
    denom = denominateur if denominateur is not None else total
    assert total > 0 and denom >= total - 1e-6, nom
    for b, m, c in cible:
        b.loc[m, poste] += montant * c[m] / denom
    reparti = montant * total / denom
    enveloppes.append({"poste": poste, "enveloppe": nom, "montant_M€": round(montant / 1e6, 1),
                       "reparti_M€": round(reparti / 1e6, 1), "hors_champ_M€": round((montant - reparti) / 1e6, 1),
                       "cle_de_repartition": cle, "population": population})
    return reparti


E1 = lambda m: (b1, m, b1["eleves"])  # noqa: E731 — clé « élèves » du 1er degré
E2 = lambda m: (b2, m, b2["eleves"])  # noqa: E731
TOUS = [E1(pub1 | prv1), E2(pub2 | prv2)]

# --- 1er degré public (P140)
repartir(credits(140, [1, 2, 3]), [(b1, pub1, b1["etp_enseignants"])], "etat_enseignants",
         "P140 actions 01-03 (enseignement préélémentaire, élémentaire, besoins particuliers dont RASED)",
         "ETP d'enseignants de l'école", "écoles publiques")
repartir(credits(140, [4, 5, 7]), [E1(pub1)], "etat_remplacement_formation",
         "P140 actions 04, 05, 07 (formation, remplacement, situations diverses)", "élèves", "écoles publiques")
repartir(credits(140, [6]), [E1(pub1)], "etat_pilotage_admin",
         "P140 action 06 (pilotage et encadrement pédagogique : inspection, conseillers pédagogiques…)", "élèves",
         "écoles publiques")
# --- 2nd degré public (P141) : actions d'enseignement mutualisées, y compris post-bac (05) et besoins
# éducatifs particuliers (06), réparties sur les heures de tous niveaux × indice ; la part post-bac sort du champ.
# Exclus : 04 apprentissage, 09 formation continue des adultes. (H-B4 ; exclusions : H-B3)
pub2_tous = b2_tous["secteur"].eq("public")
prv2_tous = b2_tous["secteur"].eq("prive_sc")
W_pub = float((b2_tous.loc[pub2_tous, "heures_ponderees_secondaire"] + b2_tous.loc[pub2_tous, "heures_ponderees_postbac"]).sum())
W_prv = float((b2_tous.loc[prv2_tous, "heures_ponderees_secondaire"] + b2_tous.loc[prv2_tous, "heures_ponderees_postbac"]).sum())
repartir(credits(141, [1, 2, 3, 5, 6]), [(b2, pub2, b2["heures_ponderees_secondaire"])], "etat_enseignants",
         "P141 actions 01, 02, 03, 05, 06 (enseignement collège, lycée GT, lycée pro, post-bac, besoins particuliers)",
         "heures d'enseignement × indice de coût des corps ; part post-bac (STS, CPGE) hors champ",
         "collèges et lycées publics", denominateur=W_pub)
# Vie scolaire et direction : ETP de l'établissement × part des élèves du secondaire dans ses élèves et étudiants ;
# la part des étudiants de STS et de CPGE, et celle des établissements post-bac seuls, sort du champ (H-B7).
part_secondaire = b2["eleves"] / (b2["eleves"] + b2["etudiants_postbac"])
ETP_AP_pub = float(b2_tous.loc[pub2_tous, "etp_autres_personnels"].fillna(0).sum())
ETP_VS_pub = float(b2_tous.loc[pub2_tous, "etp_vie_scolaire"].fillna(0).sum())
repartir(credits(141, [12]), [(b2, pub2, b2["etp_autres_personnels"].fillna(0) * part_secondaire)], "etat_pilotage_admin",
         "P141 action 12 (pilotage, administration, encadrement pédagogique)",
         "ETP « autres personnels » (direction, administratifs…) × part des élèves du secondaire ; part post-bac hors champ",
         "collèges et lycées publics", denominateur=ETP_AP_pub)
repartir(credits(141, [10, 11, 13]), [E2(pub2)], "etat_remplacement_formation",
         "P141 actions 10, 11, 13 (formation, remplacement, situations diverses)", "élèves", "collèges et lycées publics")
repartir(credits(141, [7, 8]), [E2(pub2)], "etat_inclusion_sante_social",
         "P141 actions 07-08 (insertion, information et orientation)", "élèves", "collèges et lycées publics")
# --- Privé sous contrat (P139)
repartir(credits(139, [1, 2]), [(b1, prv1, b1["etp_enseignants"])], "etat_enseignants",
         "P139 actions 01-02 (privé, préélémentaire et élémentaire)", "ETP d'enseignants de l'école",
         "écoles privées sous contrat")
repartir(credits(139, [3, 4, 5, 6]), [(b2, prv2, b2["heures_ponderees_secondaire"])], "etat_enseignants",
         "P139 actions 03, 04, 05, 06 (privé : collège, lycée GT, lycée pro, post-bac)",
         "heures d'enseignement × indice de coût des corps ; part post-bac hors champ",
         "collèges et lycées privés sous contrat", denominateur=W_prv)
repartir(credits(139, [7]), [E1(prv1), E2(prv2)], "etat_enseignants",
         "P139 action 07 (dispositifs spécifiques de scolarisation : ULIS, Segpa, UPE2A… des 1er et 2nd degrés)",
         "élèves", "établissements privés sous contrat")
repartir(credits(139, [8]), [E2(prv2)], "etat_aides_familles",
         "P139 action 08 (actions sociales en faveur des élèves du privé : bourses, fonds sociaux)", "élèves",
         "collèges et lycées privés sous contrat")
repartir(credits(139, [9]), [E2(prv2)], "etat_forfait_prive_internats",
         "P139 action 09 (fonctionnement des établissements : forfait d'externat part État, personnels non enseignants)",
         "élèves", "collèges et lycées privés sous contrat")
repartir(credits(139, [10, 11, 12]), [E1(prv1), E2(prv2)], "etat_remplacement_formation",
         "P139 actions 10-12 (formation, remplacement, soutien)", "élèves", "établissements privés sous contrat")
# --- Vie de l'élève (P230)
repartir(credits(230, [1]), [(b2, pub2, b2["etp_vie_scolaire"].fillna(0) * part_secondaire)], "etat_vie_scolaire",
         "P230 action 01 (vie scolaire : CPE, assistants d'éducation)",
         "ETP de vie scolaire de l'établissement × part des élèves du secondaire ; part post-bac hors champ",
         "collèges et lycées publics", denominateur=ETP_VS_pub)
repartir(credits(230, [2]), [E1(pub1), E2(pub2)], "etat_inclusion_sante_social",
         "P230 action 02 (santé scolaire)", "élèves", "élèves du public")
repartir(credits(230, [3, 7]), TOUS, "etat_inclusion_sante_social",
         "P230 actions 03 et 07 (inclusion des élèves handicapés / AESH, scolarisation à 3 ans)", "élèves",
         "tous les élèves")
repartir(credits(230, [4], "T2"), [E2(pub2)], "etat_inclusion_sante_social",
         "P230 action 04, titre 2 (assistants de service social)", "élèves", "élèves du 2nd degré public")
repartir(credits(230, [4], "HT2"), [E2(pub2)], "etat_aides_familles",
         "P230 action 04, hors titre 2 (bourses nationales, primes, fonds sociaux de l'enseignement public)", "élèves",
         "élèves du 2nd degré public")
repartir(credits(230, [5]), [E2(pub2)], "etat_forfait_prive_internats",
         "P230 action 05 (internat, établissements à la charge de l'État)", "élèves", "élèves du 2nd degré public")
repartir(credits(230, [6]), TOUS, "etat_activites_educatives",
         "P230 action 06 (actions éducatives complémentaires aux enseignements)", "élèves", "tous les élèves")
# --- Soutien (P214) — exclu : action 11 (sport, jeunesse, vie associative)
repartir(credits(214, range(1, 11)), TOUS, "etat_soutien_administration",
         "P214 actions 01-10 (administration centrale et académique, examens, systèmes d'information…)",
         "élèves", "tous les élèves")

# =================================================================== 2. COLLECTIVITÉS TERRITORIALES
DEPP = BRUT / "depp_compte_education"
ni2642 = Classeur(DEPP / "depp_ni_2026-42_compte_education_2025_donnees.xlsx", journal)
ni2552 = Classeur(DEPP / "depp_ni_2025-52_compte_education_2024_donnees.xlsx", journal)
rers1004 = Classeur(DEPP / "depp_rers2026_10-04_producteurs_education_donnees.xlsx", journal)
rers1002 = Classeur(DEPP / "depp_rers2026_10-02_financement_DIE_donnees.xlsx", journal)


def ct_degre(cl, annee, cellule_part, cellule_die, lib_die, col):
    part = cl.lire_cellule(f"{annee}.part_ct.{col}", "Figure 4", cellule_part, libelle_ligne="Collectivités territoriales")
    die = cl.lire_cellule(f"{annee}.die.{col}", "Figure 5", cellule_die, libelle_ligne=lib_die)
    return part / 100 * die


# Évolution 2024p → 2025p du financement initial des collectivités (1er + 2nd degrés), DEPP (H-B8).
ct_2025 = ct_degre(ni2642, "2025p", "B33", "B32", "Premier degré", "1d") + ct_degre(ni2642, "2025p", "C33", "B33",
                                                                                   "Second degré", "2d")
ct_2024 = ct_degre(ni2552, "2024p", "B33", "B31", "Premier degré", "1d") + ct_degre(ni2552, "2024p", "C33", "B32",
                                                                                   "Second degré", "2d")
croissance_ct = ct_2025 / ct_2024

# --- Écoles : financement des écoles par les collectivités (RERS 2026, fiche 10.04, 2024p), porté en 2025.
ct_ecoles_pub = rers1004.lire_cellule("2024p.ct.ecoles_publiques", "10.04 Tableau 2", "E9",
                                      libelle_ligne="Écoles maternelles et élémentaires") * 1e6 * croissance_ct
ct_ecoles_prv = rers1004.lire_cellule("2024p.ct.ecoles_privees", "10.04 Tableau 2", "E19",
                                      libelle_ligne="Écoles maternelles et élémentaires") * 1e6 * croissance_ct
# Clé « dépense de fonctionnement écoles par élève de la commune » (DGFiP 2025, communes à comptabilité
# fonctionnelle) ; ailleurs, moyenne des communes retenues (H-B9).
COLL = BRUT / "collectivites"
f = pd.read_csv(COLL / "DGFiP_balances_nature-fonction_2025_communes_ecoles_fonct_par_commune_API.csv", sep=";",
                dtype={"ndept": str, "insee": str}, encoding="utf-8-sig")
for c in ("obnetdeb", "obnetcre", "oobdeb", "oobcre"):
    f[c] = f[c].fillna(0)
f["code"] = [("97" + i) if d.startswith("1") else (d[1:] + i) for d, i in zip(f["ndept"], f["insee"])]
f["depense_fonct"] = (f["obnetdeb"] - f["oobdeb"]) - (f["obnetcre"] - f["oobcre"])
dep_com = f.groupby("code")["depense_fonct"].sum()


def commune_plm(c: str) -> str:
    if not isinstance(c, str):
        return c
    if c.startswith("751") and len(c) == 5:
        return "75056"
    if c.startswith("6938"):
        return "69123"
    if c.startswith("132") and 1 <= int(c[3:]) <= 16:
        return "13055"
    return c


b1["code_commune_norm"] = b1["code_commune"].map(commune_plm)
eleves_pub_com = b1[pub1].groupby("code_commune_norm")["eleves"].sum()
par_eleve = (dep_com / eleves_pub_com).dropna()
n_communes_comptes = int(par_eleve.size)
eleves_communes_comptes = float(eleves_pub_com.reindex(par_eleve.index).sum())
# Communes retenues : au moins 50 élèves du public et au moins 500 € par élève ; en dessous, les écoles sont
# vraisemblablement gérées par un groupement (SIVOS, EPCI) et la commune reçoit la moyenne (H-B9).
SEUIL_ELEVES, SEUIL_PLAUSIBLE = 50, 500
par_eleve = par_eleve[(eleves_pub_com.reindex(par_eleve.index) >= SEUIL_ELEVES) & (par_eleve >= SEUIL_PLAUSIBLE)]
poids = eleves_pub_com.reindex(par_eleve.index)
ordre = par_eleve.sort_values()
cum = poids.reindex(ordre.index).cumsum() / poids.sum()
bas, haut = ordre[cum >= 0.01].iloc[0], ordre[cum <= 0.99].iloc[-1]
statut_commune = pd.Series("propre", index=par_eleve.index)
statut_commune[par_eleve > haut] = "plafond"
statut_commune[par_eleve < bas] = "plancher"
par_eleve = par_eleve.clip(bas, haut)  # écrêtage aux centiles 1 et 99 pondérés par les élèves
moyenne = float((par_eleve * poids).sum() / poids.sum())
b1["cle_commune_par_eleve"] = b1["code_commune_norm"].map(par_eleve).fillna(moyenne)
b1["commune_couverte"] = b1["code_commune_norm"].isin(par_eleve.index)
# Nature de la clé, pour la carte (H-B18) : comptes de la commune (écrêtés ou non) ou moyenne ; privé : montant national.
b1["cle_commune"] = np.where(pub1, b1["code_commune_norm"].map(statut_commune).fillna("moyenne"), "national")
repartir(ct_ecoles_pub, [(b1, pub1, b1["eleves"] * b1["cle_commune_par_eleve"])], "ct_ecoles",
         "Collectivités → écoles publiques (DEPP RERS 2026 10.04, 2024p porté en 2025)",
         "élèves × dépense de fonctionnement « écoles » par élève de la commune (DGFiP 2025)", "écoles publiques")
repartir(ct_ecoles_prv, [E1(prv1)], "ct_ecoles",
         "Collectivités → écoles privées sous contrat (forfait communal ; DEPP 2024p porté en 2025)", "élèves",
         "écoles privées sous contrat")

# --- Collèges et lycées : comptes 2025 des départements et des régions (DGFiP, balances par fonction).
F_SYN = "data/raw/collectivites/extractions/DGFiP_2025_enseignement_synthese_niveau_perimetre_BP.csv"
F_POS = "data/raw/collectivites/extractions/DGFiP_2025_enseignement_postes_cles_budgets_principaux.csv"
F_SSF = "data/raw/collectivites/extractions/DGFiP_2025_enseignement_niveau_sousfonction_nature.csv"
syn = pd.read_csv(RACINE / F_SYN, sep=";").set_index(["niveau", "perimetre"])["total"]
pos = pd.read_csv(RACINE / F_POS, sep=";")
ssf = pd.read_csv(RACINE / F_SSF, sep=";")
PRIVE = "Dotations de fonctionnement aux établissements privés sous contrat (655112, 655122)"


def ligne_syn(niv: str, per: str) -> float:
    return intrant(f"dgfip.{niv}.{per}", float(syn.loc[(niv, per)]) * 1e6, F_SYN, f"niveau={niv};perimetre={per}")


def ligne_prive(niv: str, per: str) -> float:
    v = pos[(pos["niveau"] == niv) & (pos["perimetre"] == per) & (pos["poste"] == PRIVE)]["montant_M€"].sum()
    return intrant(f"dgfip.prive.{niv}.{per}", float(v) * 1e6, F_POS, f"niveau={niv};perimetre={per};poste=655112/655122")


PARIS_LYON = "collèges-lycées (cas particuliers : Paris, Métropole de Lyon)"
colleges_tot = (ligne_syn("Départements", "collèges") + ligne_syn("Régions et CTU", "collèges (CTU : Corse, Guyane, Martinique)")
                + ligne_syn("Communes (y.c. Paris)", PARIS_LYON) + ligne_syn("GFP (y.c. Métropole de Lyon, EPT)", PARIS_LYON))
colleges_prv = (ligne_prive("Départements", "collèges") + ligne_prive("Régions et CTU", "collèges (CTU : Corse, Guyane, Martinique)")
                + ligne_prive("Communes (y.c. Paris)", PARIS_LYON) + ligne_prive("GFP (y.c. Métropole de Lyon, EPT)", PARIS_LYON))
lycees_tot = ligne_syn("Régions et CTU", "lycées")
# Lycées privés : toute la sous-fonction 223 « Lycées privés » des régions (dotations et autres dépenses) (H-B10).
lycees_prv = intrant("dgfip.regions.sousfonction_223", float(ssf[(ssf["niveau"] == "Régions et CTU") & (ssf["perimetre"] == "lycées")
                                                              & ssf["sous_fonction"].str.startswith("223")]["montant_M€"].sum()) * 1e6,
                     F_SSF, "niveau=Régions et CTU;perimetre=lycées;sous_fonction=223 Lycées privés")

# Clés territoriales : dépense par collégien (départements) et par lycéen (régions), 2021-2023 (H-B10).
geo = Classeur(DEPP / "depp_geo_ecole2026_depense_departements_regions_par_collegien_lyceen_donnees.xlsx", journal)
# Chaque valeur est repérée par le code (22.1) ou le nom (22.4) lu sur sa ligne ; on contrôle l'en-tête de la colonne
# lue et celui de la colonne des codes ou des noms, puis que tous les territoires de la base ont une clé.
ws = geo.wb["22.1"]
assert "numéro département" in str(ws["A11"].value).lower(), ws["A11"].value
COL_DEP = {"libelle_colonne": "par collégien", "ligne_entete": 11}
cle_dep = {}
for r in range(12, 113):
    code, val = ws[f"A{r}"].value, ws[f"C{r}"].value
    if isinstance(code, str) and isinstance(val, (int, float)):
        cle_dep[code.strip()] = geo.lire_cellule(f"geo.college.{code.strip()}", "22.1", f"C{r}", **COL_DEP)
fr_col = geo.lire_cellule("geo.college.France", "22.1", "C113", libelle_ligne="France", **COL_DEP)
ws = geo.wb["22.4"]
assert "nom région" in str(ws["B11"].value).lower(), ws["B11"].value
COL_REG = {"libelle_colonne": "par lycéen", "ligne_entete": 11}


def norm(s) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFKD", str(s)) if ch.isalnum()).upper()


cle_reg = {}
for r in range(12, 30):
    nom, val = ws[f"B{r}"].value, ws[f"C{r}"].value
    if isinstance(nom, str) and isinstance(val, (int, float)):
        cle_reg[norm(nom)] = geo.lire_cellule(f"geo.lycee.{nom}", "22.4", f"C{r}", **COL_REG)
fr_lyc = geo.lire_cellule("geo.lycee.France", "22.4", "C29", libelle_ligne="France", **COL_REG)
# Seuls Mayotte (« nd », hors champ des fiches), Saint-Barthélemy et Saint-Martin prennent la moyenne nationale (H-B10).
sans_cle_dep = set(b2.loc[pub2, "code_departement"]) - set(cle_dep)
sans_cle_reg = set(b2.loc[pub2, "region_academique"].map(norm)) - set(cle_reg)
assert sans_cle_dep <= {"976", "977", "978"} and sans_cle_reg <= {"MAYOTTE"}, (sans_cle_dep, sans_cle_reg)
b2["cle_departement_collegien"] = b2["code_departement"].map(cle_dep).fillna(fr_col)
b2["cle_region_lyceen"] = b2["region_academique"].map(norm).map(cle_reg).fillna(fr_lyc)
# Nature des clés, pour la carte (H-B18) : propre au territoire ou moyenne nationale ; privé : montant national.
b2["cle_departement"] = np.where(pub2, np.where(b2["code_departement"].isin(cle_dep), "propre", "moyenne"), "national")
b2["cle_region"] = np.where(pub2, np.where(b2["region_academique"].map(norm).isin(cle_reg), "propre", "moyenne"), "national")
# Lycéens de Saint-Martin et de Saint-Barthélemy : valeur de leur région académique, la Guadeloupe (H-B10).
b2.loc[pub2 & b2["code_departement"].isin(["977", "978"]) & b2["cle_region"].eq("propre"), "cle_region"] = "academie"

# Part des dépenses « lycées » des régions qui sert les lycéens de l'Éducation nationale du champ : hors étudiants
# post-bac des lycées, y compris ceux des établissements post-bac seuls, et hors lycéens agricoles (H-B11).
dger = Classeur(BRUT / "budget_etat" / "DGER_effectifs_enseignement_agricole_rentree2024.xlsx", journal)
ONG = "3- Voie sco par filières"
agri = {
    "public": sum(dger.lire_cellule(f"dger.public.{l}", ONG, f"E{r}", libelle_ligne=l, col_libelle="B",
                                    libelle_colonne="2024", ligne_entete=26)
                  for l, r in (("Total 1er cycle", 29), ("Total 2ème cycle général", 33), ("Total 2ème cycle professionnel", 37))),
    "prive_sc": sum(dger.lire_cellule(f"dger.prive.{l}", ONG, f"E{r}", libelle_ligne=l, col_libelle="B",
                                      libelle_colonne="2024", ligne_entete=45)
                    for l, r in (("Total 1er cycle", 48), ("Total 2ème cycle général", 52), ("Total 2ème cycle professionnel", 56))),
}
eleves_lycee = b2["eleves_lycee_gt"] + b2["eleves_lycee_pro"]
part_champ = {}
for s, m, m_tous in (("public", pub2, pub2_tous), ("prive_sc", prv2, prv2_tous)):
    lyc = float(eleves_lycee[m].sum())
    part_champ[s] = lyc / (lyc + float(b2_tous.loc[m_tous, "etudiants_postbac"].sum()) + agri[s])
repartir(colleges_tot - colleges_prv, [(b2, pub2, b2["eleves_college"] * b2["cle_departement_collegien"])],
         "ct_colleges", "Départements (et CTU, Paris, Métropole de Lyon) → collèges publics, DGFiP 2025",
         "collégiens × dépense par collégien du département (Géographie de l'École 2026)", "collèges publics")
repartir(colleges_prv, [(b2, prv2, b2["eleves_college"])], "ct_colleges",
         "Départements → collèges privés sous contrat (dotations), DGFiP 2025", "collégiens",
         "collèges privés sous contrat")
repartir((lycees_tot - lycees_prv) * part_champ["public"], [(b2, pub2, eleves_lycee * b2["cle_region_lyceen"])],
         "ct_lycees", "Régions → lycées publics, DGFiP 2025 (hors part post-bac et lycées agricoles)",
         "lycéens × dépense par lycéen de la région (Géographie de l'École 2026)", "lycées publics")
repartir(lycees_prv * part_champ["prive_sc"], [(b2, prv2, eleves_lycee)], "ct_lycees",
         "Régions → lycées privés sous contrat (sous-fonction 223), DGFiP 2025 (hors post-bac et agricole)",
         "lycéens", "lycées privés sous contrat")

# --- Fournitures et livres scolaires payés par les collectivités (RERS 2026, 10.02 tableau 4, 2024p, porté en 2025).
# Le compte de l'éducation les classe hors des producteurs : ils manquent donc au montant des écoles ci-dessus (H-B8).
# On garde la part des écoles dans les achats de fournitures scolaires des collectivités (compte 6067, DGFiP 2025) ;
# celle des départements et des régions figure déjà dans les comptes des collèges et lycées utilisés ci-dessus.
COL_CT = {"libelle_colonne": "Collectivités territoriales", "ligne_entete": 6}
fournitures = rers1002.lire_cellule("2024p.ct.fournitures", "10.02 Tableau 4", "F18", col_libelle="B",
                                    libelle_ligne="Fournitures et livres scolaires", **COL_CT) * 1e6 * croissance_ct
f6067 = pos[pos["poste"].eq("Fournitures scolaires (6067)")]
part_ecoles_6067 = intrant("dgfip.6067.part_ecoles",
                           float(f6067.loc[f6067["perimetre"].eq("écoles (1er degré)"), "montant_M€"].sum()
                                 / f6067["montant_M€"].sum()),
                           F_POS, "poste=Fournitures scolaires (6067);perimetre=écoles (1er degré) / tous périmètres")
repartir(fournitures * part_ecoles_6067, [(b1, pub1, b1["eleves"] * b1["cle_commune_par_eleve"])], "ct_ecoles",
         "Collectivités → fournitures et livres scolaires des écoles publiques (DEPP 2024p porté en 2025 × part des "
         "écoles dans le compte 6067, DGFiP 2025)",
         "élèves × dépense de fonctionnement « écoles » par élève de la commune (DGFiP 2025)", "écoles publiques")

# --- Transports scolaires : financement final des collectivités (RERS 2026, 10.02 tableau 4, 2024p), porté en 2025.
transports = rers1002.lire_cellule("2024p.ct.transports", "10.02 Tableau 4", "F17",
                                   libelle_ligne="Achats de biens et services liés", **COL_CT) * 1e6 * croissance_ct
repartir(transports, TOUS, "ct_transports", "Collectivités → transports scolaires (DEPP 2024p porté en 2025)",
         "élèves", "tous les élèves")

# =================================================================== 3. AUTRES ADMINISTRATIONS PUBLIQUES
dme_1d = ni2642.lire_cellule("2025p.dme.1d", "Figure 7", "C82", libelle_ligne="2025p")
dme_2d = ni2642.lire_cellule("2025p.dme.2d", "Figure 7", "D82", libelle_ligne="2025p")
apu_1d = ni2642.lire_cellule("2025p.part_apu.1d", "Figure 4", "B34", libelle_ligne="Autres administrations publiques")
apu_2d = ni2642.lire_cellule("2025p.part_apu.2d", "Figure 4", "C34", libelle_ligne="Autres administrations publiques")
# Premier degré : l'allocation de rentrée scolaire, l'essentiel du montant (H-A4), n'est versée que pour les enfants de
# 6 ans et plus. Le montant du degré (élèves × dépense moyenne × part « autres APU ») est donc réparti sur les seuls
# élèves d'élémentaire, d'ULIS et d'UEEA, et sur aucun élève des écoles maternelles. Écoles sans effectifs par niveau,
# typées d'après l'annuaire ou leur nom (script 03) : élémentaire, tous les élèves ; primaire, la part nationale des
# élèves de 6 ans et plus dans les écoles primaires ; maternelle, aucun (H-B13).
niveaux_1d = b1["eleves_preelementaire"].notna() | b1["eleves_elementaire"].notna()
six_ans = (b1["eleves"] - b1["eleves_preelementaire"].fillna(0)).clip(lower=0)
prim = b1["type_ecole"].eq("P") & niveaux_1d
part_six_ans_primaire = float(six_ans[prim].sum() / b1.loc[prim, "eleves"].sum())
eligibles_1d = pd.Series(np.select([b1["type_ecole"].eq("M"), niveaux_1d, b1["type_ecole"].eq("P")],
                                   [0.0, six_ans, b1["eleves"] * part_six_ans_primaire], b1["eleves"]), index=b1.index)
b1["apu_par_eleve"] = float(b1["eleves"].sum()) * dme_1d * apu_1d / 100 * eligibles_1d / float(eligibles_1d.sum())
b2["apu_par_eleve"] = b2["eleves"] * dme_2d * apu_2d / 100
total_apu = b1["apu_par_eleve"].sum() + b2["apu_par_eleve"].sum()
enveloppes.append({"poste": "apu_par_eleve", "enveloppe": "Autres administrations publiques (surtout allocation de "
                   "rentrée scolaire des CAF) : dépense moyenne × part « autres APU » (DEPP 2025p)",
                   "montant_M€": round(total_apu / 1e6, 1), "reparti_M€": round(total_apu / 1e6, 1),
                   "hors_champ_M€": 0.0, "cle_de_repartition": "élèves (1er degré : élèves de 6 ans et plus)",
                   "population": "tous les élèves"})

# =================================================================== 4. Résultats par établissement
ETAT = [p for p in POSTES if p.startswith("etat_")]
CT = [p for p in POSTES if p.startswith("ct_")]
for b in (b1, b2):
    b["etat"] = b[ETAT].sum(axis=1)
    b["collectivites"] = b[CT].sum(axis=1)
    b["depense_publique"] = b["etat"] + b["collectivites"] + b["apu_par_eleve"]
    b["depense_publique_par_eleve"] = b["depense_publique"] / b["eleves"]
    b["degre"] = "1er degré" if b is b1 else "2nd degré"

COLS = ["uai", "nom", "degre", "type", "secteur", "academie", "code_departement", "departement", "commune",
        "code_commune_norm", "rep", "rep_plus", "ips", "eleves", "etp_enseignants", "indice_cout_enseignant",
        *POSTES, "etat", "collectivites", "depense_publique", "depense_publique_par_eleve",
        "cle_commune", "cle_departement", "cle_region"]
b1["indice_cout_enseignant"] = 1.0
etab = pd.concat([b1.reindex(columns=COLS), b2.reindex(columns=COLS)], ignore_index=True)
etab.to_csv(RESULTATS / "B1_depense_publique_par_etablissement_2025.csv", sep=";", index=False,
            encoding="utf-8-sig", float_format="%.2f")


def resume(df: pd.DataFrame, libelle: dict) -> dict:
    n = df["eleves"].sum()
    ligne = dict(libelle)
    ligne.update({"etablissements": len(df), "eleves": int(n),
                  "depense_publique_M€": round(df["depense_publique"].sum() / 1e6, 1),
                  "depense_publique_par_eleve_€": round(df["depense_publique"].sum() / n)})
    for p in POSTES + ["etat", "collectivites"]:
        ligne[f"{p}_€_par_eleve"] = round(df[p].sum() / n)
    # Distribution entre établissements, pondérée par les élèves (chaque élève porte le coût de son établissement).
    x = df.sort_values("depense_publique_par_eleve")
    w = x["eleves"].cumsum() / n
    for q in (0.10, 0.25, 0.50, 0.75, 0.90):
        ligne[f"P{int(q * 100)}_€"] = round(float(x.loc[w >= q, "depense_publique_par_eleve"].iloc[0]))
    return ligne


LYCEES = ("lycée général et technologique", "lycée polyvalent", "lycée professionnel")
agregats = [resume(etab, {"groupe": "Ensemble 1er + 2nd degrés", "modalite": "tous"})]
for deg in ("1er degré", "2nd degré"):
    agregats.append(resume(etab[etab["degre"].eq(deg)], {"groupe": "Degré", "modalite": deg}))
    for s in ("public", "prive_sc"):
        agregats.append(resume(etab[etab["degre"].eq(deg) & etab["secteur"].eq(s)],
                               {"groupe": f"{deg} × secteur", "modalite": s}))
for (t, s), d in etab.groupby(["type", "secteur"]):
    agregats.append(resume(d, {"groupe": "Type d'établissement × secteur", "modalite": f"{t} | {s}"}))
for s in ("public", "prive_sc"):
    agregats.append(resume(etab[etab["type"].isin(LYCEES) & etab["secteur"].eq(s)],
                           {"groupe": "Lycées (GT, polyvalents, professionnels) × secteur", "modalite": s}))
# Comparaisons sociales à type d'établissement constant (l'éducation prioritaire ne concerne que écoles et collèges).
paris = etab["code_commune_norm"].eq("75056")
GROUPES_SOCIAUX = {
    "écoles publiques": etab["degre"].eq("1er degré") & etab["secteur"].eq("public"),
    "écoles publiques hors Paris": etab["degre"].eq("1er degré") & etab["secteur"].eq("public") & ~paris,
    "collèges publics": etab["type"].eq("collège") & etab["secteur"].eq("public"),
    "lycées publics": etab["type"].isin(LYCEES) & etab["secteur"].eq("public"),
}
for nom, masque in GROUPES_SOCIAUX.items():
    d = etab[masque]
    if nom in ("écoles publiques", "collèges publics"):
        ep = np.select([d["rep_plus"].eq(1), d["rep"].eq(1)], ["REP+", "REP"], "hors éducation prioritaire")
        for m in ("REP+", "REP", "hors éducation prioritaire"):
            agregats.append(resume(d[ep == m], {"groupe": f"{nom} × éducation prioritaire", "modalite": m}))
    # Quintiles d'établissements (même nombre d'établissements par quintile), IPS numérique seulement (H-B15).
    q = pd.qcut(pd.to_numeric(d["ips"], errors="coerce"), 5,
                labels=["Q1 (plus défavorisés)", "Q2", "Q3", "Q4", "Q5 (plus favorisés)"])
    for m in q.cat.categories:
        agregats.append(resume(d[q == m], {"groupe": f"{nom} × quintile d'IPS", "modalite": str(m)}))
# Effet de taille des collèges publics.
c = etab[etab["type"].eq("collège") & etab["secteur"].eq("public")]
tranche = pd.cut(c["eleves"], [0, 200, 400, 500, 600, 800, 10_000], right=False,
                 labels=["moins de 200", "200 à 399", "400 à 499", "500 à 599", "600 à 799", "800 et plus"])
for m in tranche.cat.categories:
    agregats.append(resume(c[tranche == m], {"groupe": "collèges publics × taille (élèves)", "modalite": str(m)}))
ecrire_csv(RESULTATS / "B2_agregats_et_distribution.csv", agregats)
ecrire_csv(RESULTATS / "B0_enveloppes_reparties.csv", enveloppes)
ecrire_csv(RESULTATS / "B3_intrants_extractions.csv", intrants)

# Indicateurs de méthode (repris dans le rapport).
# Enveloppes réparties avec des données propres à chaque établissement (ETP et heures d'enseignement, ETP de vie
# scolaire et d'autres personnels) ; les enveloppes de ces postes réparties par élève sont exclues.
specifique = sum(e["reparti_M€"] for e in enveloppes
                 if e["poste"] in ("etat_enseignants", "etat_vie_scolaire", "etat_pilotage_admin")
                 and e["cle_de_repartition"] != "élèves") * 1e6
methode = [
    {"indicateur": "Communes publiant des comptes par fonction et ayant des écoles publiques", "valeur": n_communes_comptes},
    {"indicateur": "Part des élèves du public dans ces communes (rentrée 2024)",
     "valeur": round(eleves_communes_comptes / b1.loc[pub1, "eleves"].sum(), 4)},
    {"indicateur": "Communes retenues pour la clé communale (≥ 50 élèves, ≥ 500 €/élève)", "valeur": int(par_eleve.size)},
    {"indicateur": "Part des élèves du public dans les communes retenues",
     "valeur": round(float(b1.loc[pub1 & b1["commune_couverte"], "eleves"].sum() / b1.loc[pub1, "eleves"].sum()), 4)},
    {"indicateur": "Clé communale : moyenne (€ par élève, fonctionnement)", "valeur": round(moyenne)},
    {"indicateur": "Clé communale : écrêtage bas / haut (€)", "valeur": f"{bas:.0f} / {haut:.0f}"},
    {"indicateur": "Part de B répartie avec des données propres à l'établissement (ETP et heures d'enseignement, "
                   "ETP de vie scolaire et d'autres personnels)",
     "valeur": round(specifique / float(etab["depense_publique"].sum()), 4)},
    {"indicateur": "Part de B reprise du compte de l'éducation (écoles, transports, autres APU)",
     "valeur": round(float((etab["ct_ecoles"].sum() + etab["ct_transports"].sum() + etab["apu_par_eleve"].sum())
                           / etab["depense_publique"].sum()), 4)},
    {"indicateur": "Part « champ » des dépenses lycées des régions (public / privé)",
     "valeur": f"{part_champ['public']:.4f} / {part_champ['prive_sc']:.4f}"},
    {"indicateur": "Élèves agricoles du secondaire, rentrée 2024 (public / privé), DGER",
     "valeur": f"{agri['public']:.0f} / {agri['prive_sc']:.0f}"},
    {"indicateur": "Croissance du financement des collectivités 2024p → 2025p (DEPP)", "valeur": round(croissance_ct, 4)},
    {"indicateur": "Part des écoles dans les achats de fournitures scolaires des collectivités (compte 6067, DGFiP 2025)",
     "valeur": round(part_ecoles_6067, 4)},
    {"indicateur": "Établissements du 2nd degré sans heures H/E, avec élèves (nombre / élèves)",
     "valeur": f"{int(sans_h.sum())} / {int(b2_tous.loc[sans_h, 'eleves'].sum())}"},
    {"indicateur": "Établissements dont les heures H/E couvrent moins de 90 % des élèves (nombre / élèves manquants / heures imputées)",
     "valeur": f"{int(partiel.sum())} / {int((b2_tous.loc[partiel, 'eleves'] - b2_tous.loc[partiel, 'eleves_he']).sum())} / {b2_tous['h_impute'].sum():.0f}"},
    {"indicateur": "Crédits de l'État hors champ (part post-bac des actions d'enseignement, de la vie scolaire et de la direction), M€",
     "valeur": round(sum(e["hors_champ_M€"] for e in enveloppes), 1)},
    {"indicateur": "1er degré : élèves de 6 ans et plus comptés pour les autres APU (allocation de rentrée scolaire) / "
                   "part des élèves de 6 ans et plus dans les écoles primaires",
     "valeur": f"{eligibles_1d.sum():.0f} / {part_six_ans_primaire:.4f}"},
]
ecrire_csv(RESULTATS / "B4_indicateurs_methode.csv", methode)
journal.ecrire(RESULTATS / "tracabilite_B.csv")

if __name__ == "__main__":
    print(f"Enveloppes : {sum(e['montant_M€'] for e in enveloppes):,.1f} M€, dont réparties "
          f"{sum(e['reparti_M€'] for e in enveloppes):,.1f} M€")
    print(f"Indices de coût : { {k: round(v, 3) for k, v in INDICE.items()} }")
    for m in methode:
        print(f"  {m['indicateur']} : {m['valeur']}")
    for a in agregats:
        if a["groupe"] in ("Ensemble 1er + 2nd degrés", "Degré", "1er degré × secteur", "2nd degré × secteur"):
            print(f"  {a['groupe']:28} {a['modalite']:10} élèves {a['eleves']:>10,}  "
                  f"{euros(a['depense_publique_par_eleve_€']):>9}/élève  (État {euros(a['etat_€_par_eleve'])}, "
                  f"CT {euros(a['collectivites_€_par_eleve'])}, APU {euros(a['apu_par_eleve_€_par_eleve'])})  "
                  f"P10-P90 : {a['P10_€']:,}-{a['P90_€']:,}")
