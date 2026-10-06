"""Approche B, étape 1 — base de données par établissement (rentrée 2024).

Croise, par code établissement (UAI), les fichiers officiels de data.education.gouv.fr :
- effectifs d'élèves par école, collège, lycée général et technologique, lycée professionnel ;
- ETP de personnels affectés dans les établissements (panel des personnels issu de BSA) ;
- heures d'enseignement hebdomadaires par niveau (indicateur H/E), pour isoler la part post-bac des lycées ;
- éducation prioritaire (REP, REP+) et indice de position sociale (IPS 2024-2025).

Champ : France = métropole + DROM (Mayotte comprise) ; les collectivités d'outre-mer présentes dans
l'open data sont exclues (hypothèse H-E3). Aucun coût n'est calculé ici (voir 04_approche_B_par_etablissement.py).
"""
import numpy as np
import pandas as pd

from commun import BRUT, RACINE, Communes, cle

ETAB = BRUT / "etablissements"
TRAITE = RACINE / "data" / "processed"
TRAITE.mkdir(parents=True, exist_ok=True)
RENTREE = 2024
COM = {"NOUVELLE CALEDONIE", "POLYNESIE FRANCAISE", "WALLIS ET FUTUNA", "ST PIERRE ET MIQUELON"}
SECTEUR = {"PUBLIC": "public", "PRIVE SOUS CONTRAT": "prive_sc", "PRIVE": "prive_sc",
           "PRIVÉ": "prive_sc", "PRIVÉ SOUS CONTRAT": "prive_sc"}


def lire(nom: str, **kw) -> pd.DataFrame:
    return pd.read_csv(ETAB / nom, sep=";", low_memory=False, **kw).copy()


def hors_com(df: pd.DataFrame, col: str = "academie") -> pd.DataFrame:
    return df[~df[col].astype(str).str.upper().isin(COM)].copy()


# ---------------------------------------------------------------- 1er degré
eco = hors_com(lire(f"effectifs_ecoles_1d_rentree{RENTREE}.csv", dtype={"code_departement": str,
                                                                        "code_commune_insee": str}))
eco = pd.DataFrame({
    "uai": eco["numero_ecole"], "nom": eco["denomination_principale"].fillna("") + " " + eco["patronyme"].fillna(""),
    "secteur": eco["secteur"].str.upper().map(SECTEUR), "academie": eco["academie"],
    "code_departement": eco["code_departement"], "departement": eco["departement"],
    # Attention : la colonne « code_commune_insee » de ce jeu contient en réalité le code postal.
    "code_postal": eco["code_commune_insee"], "commune": eco["commune"],
    "region_academique": eco["region_academique"],
    "rep": eco["rep"].astype(int), "rep_plus": eco["rep_plus"].astype(int),
    "nb_classes": eco["nombre_total_classes"],
    "eleves": eco["nombre_total_eleves"],
    "eleves_preelementaire": eco["nombre_eleves_preelementaire_hors_ulis"],
    "eleves_elementaire": eco["nombre_eleves_elementaire_hors_ulis"],
    "eleves_ulis_ueea": eco["nombre_eleves_ulis"].fillna(0) + eco["nombre_eleves_ueea"].fillna(0),
})
assert eco["secteur"].notna().all() and not eco["uai"].duplicated().any()

pers1 = lire(f"personnels_1d_rentree{RENTREE}.csv")
pers1 = pers1.groupby("identifiant_de_l_etablissement", as_index=False)["etp_d_enseignants_hommes_et_femmes"].sum()
pers1.columns = ["uai", "etp_enseignants"]
ips_e = lire("ips_ecoles_2024-2025.csv", dtype={"code_insee_de_la_commune": str})
ips_e = ips_e[["uai", "ips", "code_insee_de_la_commune"]].drop_duplicates("uai")
# Code commune Insee : annuaire de l'éducation (UAI → commune), à défaut fichier IPS des écoles, à défaut nom de la
# commune dans le département (API Découpage administratif ; commune actuelle, chef-lieu pour une commune déléguée) (H-E4).
ann = lire("annuaire_education_extrait_2026-10-04.csv", dtype=str,
           usecols=["identifiant_de_l_etablissement", "code_commune", "ecole_maternelle", "ecole_elementaire"]
           ).drop_duplicates("identifiant_de_l_etablissement").set_index("identifiant_de_l_etablissement")
eco["code_commune"] = eco["uai"].map(ann["code_commune"])
eco["code_commune_source"] = np.where(eco["code_commune"].notna(), "annuaire", None)
ips_code = ips_e.set_index("uai")["code_insee_de_la_commune"].str.zfill(5)
par_ips = eco["code_commune"].isna() & eco["uai"].map(ips_code).notna()
eco["code_commune"] = eco["code_commune"].fillna(eco["uai"].map(ips_code))
eco.loc[par_ips, "code_commune_source"] = "IPS"
communes = Communes()
for i in eco.index[eco["code_commune"].isna()]:
    c, regle = communes.trouver(None, eco.at[i, "code_departement"], eco.at[i, "commune"])
    if c is not None:
        eco.at[i, "code_commune"] = Communes.code_actuel(c)
        eco.at[i, "code_commune_source"] = "nom (" + regle + ")"
ips_e = ips_e[["uai", "ips"]]

# Type d'école : maternelle (seulement des élèves de préélémentaire), élémentaire (aucun), primaire (les deux), d'après
# les élèves par niveau ; s'ils ne sont pas publiés, d'après l'annuaire (classes maternelles, classes élémentaires), puis
# le nom ; à défaut, élémentaire (H-B18). Sert à la répartition de l'allocation de rentrée scolaire (H-B13) et à la carte.
pre, ele = eco["eleves_preelementaire"], eco["eleves_elementaire"]
niveaux = pre.notna() | ele.notna()
t_niv = np.select([(pre.fillna(0) > 0) & ~(ele.fillna(0) > 0), (pre.fillna(0) > 0) & (ele.fillna(0) > 0)], ["M", "P"], "E")
mat, elem = eco["uai"].map(ann["ecole_maternelle"]), eco["uai"].map(ann["ecole_elementaire"])
t_ann = np.select([mat.eq("1") & elem.eq("1"), mat.eq("1") & elem.eq("0"), mat.eq("0") & elem.eq("1")], ["P", "M", "E"], "")
nom_c = eco["nom"].map(cle)
t_nom = np.select([nom_c.str.contains(r"\bprimaire\b"), nom_c.str.contains(r"\bmaternelle\b"),
                   nom_c.str.contains(r"\belementaire\b")], ["P", "M", "E"], "")
eco["type_ecole"] = np.where(niveaux, t_niv, np.where(t_ann != "", t_ann, np.where(t_nom != "", t_nom, "E")))
eco["type_ecole_source"] = np.where(niveaux, "effectifs", np.where(t_ann != "", "annuaire", np.where(t_nom != "", "nom", "inconnu")))

b1 = eco.merge(pers1, on="uai", how="outer", indicator=True)
b1["appariement"] = b1["_merge"].map({"both": "apparié", "left_only": "élèves sans ETP",
                                      "right_only": "ETP sans élèves"})
b1 = b1.drop(columns="_merge").merge(ips_e, on="uai", how="left")
b1["degre"] = "1d"
b1["type"] = "école"

# ---------------------------------------------------------------- 2nd degré
col = hors_com(lire(f"effectifs_colleges_rentree{RENTREE}.csv", dtype={"code_dept": str, "code_commune": str}))
lgt = hors_com(lire(f"effectifs_lycees_gt_rentree{RENTREE}.csv", dtype={"code_departement_pays": str,
                                                                        "code_commune": str}))
lp = hors_com(lire(f"effectifs_lycees_pro_rentree{RENTREE}.csv", dtype={"code_departement": str,
                                                                        "code_commune": str}))
parts = [
    pd.DataFrame({"uai": col["numero_college"], "eleves_college": col["nombre_eleves_total"],
                  "eleves_segpa": col["nombre_d_eleves_total_segpa"], "rep": col["rep"], "rep_plus": col["rep0"],
                  "secteur": col["secteur"], "academie": col["academie"], "code_departement": col["code_dept"],
                  "departement": col["departement"], "code_commune": col["code_commune"],
                  "commune": col["commune"], "region_academique": col["region_academique"],
                  "nom": col["denomination_principale"].fillna("") + " " + col["patronyme"].fillna("")}),
    pd.DataFrame({"uai": lgt["numero_lycee"], "eleves_lycee_gt": lgt["nombre_d_eleves"], "secteur": lgt["secteur"],
                  "academie": lgt["academie"], "code_departement": lgt["code_departement_pays"],
                  "departement": lgt["departement"], "code_commune": lgt["code_commune"],
                  "commune": lgt["commune"], "region_academique": lgt["region_academique"],
                  "nom": lgt["denomination_principale"].fillna("") + " " + lgt["patronyme"].fillna("")}),
    # La colonne « code_commune » du fichier des lycées professionnels contient en réalité le code postal : on ne la
    # reprend pas (H-E4).
    pd.DataFrame({"uai": lp["numero_lycee"], "eleves_lycee_pro": lp["nombre_d_eleves"], "secteur": lp["secteur"],
                  "academie": lp["academie"], "code_departement": lp["code_departement"],
                  "departement": lp["departement"], "code_commune": pd.NA,
                  "commune": lp["commune"], "region_academique": lp["region_academique"],
                  "nom": lp["denomination_principale"].fillna("") + " " + lp["patronyme"].fillna("")}),
]
el2 = pd.concat(parts, ignore_index=True)
el2["secteur"] = el2["secteur"].str.upper().map(SECTEUR)
assert el2["secteur"].notna().all()
num = ["eleves_college", "eleves_segpa", "eleves_lycee_gt", "eleves_lycee_pro", "rep", "rep_plus"]
el2[num] = el2[num].fillna(0)
agg = {c: "sum" for c in num}
agg.update({c: "first" for c in ["secteur", "academie", "code_departement", "departement", "code_commune",
                                 "commune", "region_academique", "nom"]})
el2 = el2.groupby("uai", as_index=False).agg(agg)
# Code commune Insee : annuaire de l'éducation (UAI → commune), à défaut fichiers des collèges et des lycées GT (H-E4).
el2["code_commune"] = el2["uai"].map(ann["code_commune"]).fillna(el2["code_commune"])
el2[["rep", "rep_plus"]] = el2[["rep", "rep_plus"]].clip(upper=1).astype(int)
el2["eleves"] = el2[["eleves_college", "eleves_lycee_gt", "eleves_lycee_pro"]].sum(axis=1)

p2 = lire(f"personnels_2d_rentree{RENTREE}.csv")
corps = {"etp_d_enseignants_agreges": "etp_agreges", "etp_d_enseignants_certifies_peps": "etp_certifies",
         "etp_d_enseignants_plp": "etp_plp", "etp_d_enseignants_titulaires_d_un_autre_corps": "etp_autres_titulaires",
         "etp_d_enseignants_non_titulaires": "etp_non_titulaires"}
p2 = p2.rename(columns={"identifiant_de_l_etablissement": "uai", "etp_enseignants_hommes_et_femmes": "etp_enseignants",
                        "etp_de_personnels_de_vie_scolaire": "etp_vie_scolaire",
                        "nature_de_l_etablissement": "nature", **corps})
assert not p2["uai"].duplicated().any()
p2["secteur_personnels"] = p2["secteur"].str.upper().map(SECTEUR)
p2 = p2[["uai", "nature", "secteur_personnels", "etp_total", "etp_enseignants", "etp_vie_scolaire", *corps.values()]]
# Contrôle : la somme des corps égale l'ETP enseignant.
ecart = (p2[list(corps.values())].sum(axis=1) - p2["etp_enseignants"]).abs().max()
assert ecart < 0.01, ecart
# ETP « autres personnels » (direction, administratifs, santé-social…) = total − enseignants − vie scolaire (public).
p2["etp_autres_personnels"] = (p2["etp_total"] - p2["etp_enseignants"] - p2["etp_vie_scolaire"].fillna(0)).clip(lower=0)

# Heures d'enseignement hebdomadaires par niveau (H/E) : part des heures post-bac (STS, CPGE).
h = pd.concat([lire(f"moyens_enseignants_2d_public_rentree{RENTREE}.csv"),
               lire(f"moyens_enseignants_2d_prive_rentree{RENTREE}.csv")], ignore_index=True)
h = h[h["uai"].astype(str).str.len() == 8]  # retire les lignes de totaux départementaux et académiques
hcol = "numerateur_h_e_nb_heures_enseignement_hebdo_devant_eleves"
h[hcol] = pd.to_numeric(h[hcol], errors="coerce").fillna(0)
h["postbac"] = h["niveau"].isin(["STS", "CPGE"])
hh = h.groupby(["uai", "postbac"])[hcol].sum().unstack(fill_value=0)
hh.columns = ["heures_secondaire" if not c else "heures_postbac" for c in hh.columns]
hh = hh.reset_index()
hh["part_heures_postbac"] = hh["heures_postbac"] / (hh["heures_postbac"] + hh["heures_secondaire"])

ips_c = lire("ips_colleges_2024-2025.csv")[["uai", "ips"]]
ips_l = lire("ips_lycees_2024-2025.csv")[["uai", "ips_etab"]].rename(columns={"ips_etab": "ips"})
ips2 = pd.concat([ips_c, ips_l]).drop_duplicates("uai")  # cité scolaire : IPS du collège retenu

b2 = el2.merge(p2, on="uai", how="outer", indicator=True)
b2["appariement"] = b2["_merge"].map({"both": "apparié", "left_only": "élèves sans ETP",
                                      "right_only": "ETP sans élèves"})
b2 = b2.drop(columns="_merge").merge(hh, on="uai", how="left").merge(ips2, on="uai", how="left")
b2["part_heures_postbac"] = b2["part_heures_postbac"].fillna(0)
b2[["eleves", "eleves_college", "eleves_segpa", "eleves_lycee_gt", "eleves_lycee_pro"]] = \
    b2[["eleves", "eleves_college", "eleves_segpa", "eleves_lycee_gt", "eleves_lycee_pro"]].fillna(0)
b2["degre"] = "2d"


def type_2d(r) -> str:
    if r["eleves"] == 0:
        return "post-bac uniquement" if r["appariement"] == "ETP sans élèves" else "sans élèves"
    if r["eleves_college"] > 0 and (r["eleves_lycee_gt"] + r["eleves_lycee_pro"]) == 0:
        return "collège"
    if r["eleves_college"] == 0 and r["eleves_lycee_gt"] > 0 and r["eleves_lycee_pro"] == 0:
        return "lycée général et technologique"
    if r["eleves_college"] == 0 and r["eleves_lycee_pro"] > 0 and r["eleves_lycee_gt"] == 0:
        return "lycée professionnel"
    if r["eleves_college"] == 0:
        return "lycée polyvalent"
    return "cité scolaire (collège + lycée)"


NATURE = {
    "Collège": "collège", "Collège spécialisé": "collège", "Collège climatique": "collège",
    "Lycée professionnel": "lycée professionnel",
    "Lycée d'enseignement général et technologique": "lycée général et technologique",
    "Lycée d'enseignement général": "lycée général et technologique",
    "Lycée d'enseignement technologique": "lycée général et technologique",
    "Lycée climatique": "lycée général et technologique",
    "Lycée polyvalent": "lycée polyvalent",
    "Etablissement régional d'enseignement adapté / Lycée d'enseignement adapté": "EREA / LEA",
    "Etablissement composé uniquement de STS et/ou de CPGE": "post-bac uniquement",
    "Ecole secondaire spécialisée (second cycle)": "autre",
}
# Type = nature officielle de l'établissement (fichier des personnels) ; à défaut, type déduit des élèves.
b2["type"] = b2["nature"].map(NATURE).fillna(b2.apply(type_2d, axis=1))
# Les établissements « ETP sans élèves » (STS/CPGE seuls) n'ont pas de secteur dans les fichiers d'élèves :
# on reprend celui du fichier des personnels.
b2["secteur"] = b2["secteur"].fillna(b2["secteur_personnels"])
assert b2["secteur"].notna().all()

b1.to_csv(TRAITE / f"base_ecoles_rentree{RENTREE}.csv", sep=";", index=False, encoding="utf-8-sig")
b2.to_csv(TRAITE / f"base_2d_rentree{RENTREE}.csv", sep=";", index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    for nom, b in (("1er degré", b1), ("2nd degré", b2)):
        print(f"== {nom} : {len(b)} lignes")
        print(b.groupby(["appariement"])[["eleves", "etp_enseignants"]].agg(["count", "sum"]).round(0).to_string())
    print(b2.groupby(["secteur", "type"])[["eleves", "etp_enseignants", "heures_postbac"]].sum().round(0).to_string())
    print("Part des heures post-bac (pondérée) :",
          round(b2["heures_postbac"].sum() / (b2["heures_postbac"].sum() + b2["heures_secondaire"].sum()), 4))
    print("IPS disponible : 1d", b1["ips"].notna().mean().round(3), "| 2d", b2["ips"].notna().mean().round(3))
