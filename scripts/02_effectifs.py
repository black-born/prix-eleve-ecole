"""Effectifs d'élèves : totaux nationaux officiels (DEPP) et sommes des fichiers par établissement.

Sources :
- DEPP, Note d'Information n° 25.58 (1er degré, rentrée 2025) : onglet « Figure 7 en ligne », ligne France ;
- DEPP, Note d'Information n° 25.59 (2nd degré, rentrée 2025) : onglet « Figure 10 en ligne » ;
- data.education.gouv.fr : effectifs par école / collège / lycée (rentrées 2024 et 2025).

Convention du compte de l'éducation (DEPP, Dossier n° 206) : l'effectif d'une année civile N vaut
2/3 de la rentrée N-1 + 1/3 de la rentrée N. Hypothèses : voir hypotheses.md (section E).
"""
import pandas as pd

from commun import BRUT, RESULTATS, Classeur, Journal, ecrire_csv

EFF = BRUT / "effectifs_nationaux"
ETAB = BRUT / "etablissements"
journal = Journal()

ni2558 = Classeur(EFF / "depp_ni_2025-58_effectifs_1er_degre_rentree2025_donnees.xlsx", journal)
ni2559 = Classeur(EFF / "depp_ni_2025-59_effectifs_2nd_degre_rentree2025_donnees.xlsx", journal)

# 1er degré : ligne 42 « France » ; constats 2023, 2024, 2025 ; en-têtes ligne 9.
COL_1D = {"public": {2023: "F", 2024: "G", 2025: "H"},
          "prive_sc": {2023: "O", 2024: "P", 2025: "Q"},
          "ensemble": {2023: "X", 2024: "Y", 2025: "Z"}}
# 2nd degré : en-têtes ligne 4 ; ligne 32 « Ensemble second degré ».
COL_2D = {"public": {2023: "C", 2024: "D", 2025: "E"},
          "prive_sc": {2023: "H", 2024: "I", 2025: "J"},
          "ensemble": {2023: "M", 2024: "N", 2025: "O"}}
LIGNES_2D = {"ensemble_2d": (32, "Ensemble second degré"),
             "college_y_c_segpa": (13, "Formations en collège"),
             "lycee_gt": (30, "Ensemble formations générales et techn"),
             "lycee_pro": (25, "Ensemble formations Professionnelles"),
             "prepa_seconde": (14, "Ensemble classe préparatoire")}

nat = {}
for secteur, cols in COL_1D.items():
    for an, col in cols.items():
        nat[("1d", secteur, an)] = ni2558.lire_cellule(f"1d.{secteur}.{an}", "Figure 7 en ligne", f"{col}42",
                                                       libelle_ligne="France", libelle_colonne=str(an),
                                                       ligne_entete=9)
for cle, (ligne, lib) in LIGNES_2D.items():
    for secteur, cols in COL_2D.items():
        for an, col in cols.items():
            if cle == "prepa_seconde" and secteur != "ensemble":
                continue
            nat[(cle, secteur, an)] = ni2559.lire_cellule(f"2d.{cle}.{secteur}.{an}", "Figure 10 en ligne",
                                                          f"{col}{ligne}", libelle_ligne=lib,
                                                          libelle_colonne=str(an), ligne_entete=4)
for an in (2023, 2024, 2025):
    for secteur in ("public", "prive_sc"):
        assert nat[("1d", secteur, an)] > 0
    assert nat[("1d", "public", an)] + nat[("1d", "prive_sc", an)] == nat[("1d", "ensemble", an)]
    assert nat[("ensemble_2d", "public", an)] + nat[("ensemble_2d", "prive_sc", an)] == nat[("ensemble_2d", "ensemble", an)]


def annee_civile(niv: str, secteur: str, n: int) -> float:
    """Convention DEPP : 2/3 de la rentrée n-1 + 1/3 de la rentrée n."""
    return 2 / 3 * nat[(niv, secteur, n - 1)] + 1 / 3 * nat[(niv, secteur, n)]


lignes = []
for niv, lib in (("1d", "1er degré"), ("ensemble_2d", "2nd degré (Éducation nationale)")):
    for secteur in ("public", "prive_sc", "ensemble"):
        ligne = {"niveau": lib, "secteur": secteur}
        for an in (2023, 2024, 2025):
            ligne[f"rentree_{an}"] = int(nat[(niv, secteur, an)])
        for an in (2024, 2025):
            ligne[f"annee_civile_{an}"] = round(annee_civile(niv, secteur, an))
        lignes.append(ligne)
for cle in ("college_y_c_segpa", "lycee_gt", "lycee_pro", "prepa_seconde"):
    ligne = {"niveau": f"2nd degré — {cle}", "secteur": "ensemble"}
    for an in (2023, 2024, 2025):
        ligne[f"rentree_{an}"] = int(nat[(cle, "ensemble", an)])
    lignes.append(ligne)
tot = {"niveau": "1er + 2nd degrés (Éducation nationale)", "secteur": "ensemble"}
for an in (2023, 2024, 2025):
    tot[f"rentree_{an}"] = int(nat[("1d", "ensemble", an)] + nat[("ensemble_2d", "ensemble", an)])
for an in (2024, 2025):
    tot[f"annee_civile_{an}"] = round(annee_civile("1d", "ensemble", an) + annee_civile("ensemble_2d", "ensemble", an))
lignes.append(tot)
ecrire_csv(RESULTATS / "E1_effectifs_nationaux.csv", lignes)

# Sommes des fichiers par établissement (open data), comparées aux totaux nationaux.
FICHIERS = {
    "ecoles": ("effectifs_ecoles_1d_rentree{an}.csv", "nombre_total_eleves", "1d"),
    "colleges": ("effectifs_colleges_rentree{an}.csv", "nombre_eleves_total", "college_y_c_segpa"),
    "lycees_gt": ("effectifs_lycees_gt_rentree{an}.csv", "nombre_d_eleves", "lycee_gt"),
    "lycees_pro": ("effectifs_lycees_pro_rentree{an}.csv", "nombre_d_eleves", "lycee_pro"),
}
SECTEUR = {"PUBLIC": "public", "PRIVE SOUS CONTRAT": "prive_sc", "PRIVE": "prive_sc"}
# Collectivités d'outre-mer présentes dans l'open data mais hors du champ « France » de la DEPP
# (métropole + DROM, Mayotte comprise) : exclues (hypothèse H-E3).
COM = {"NOUVELLE CALEDONIE", "POLYNESIE FRANCAISE", "WALLIS ET FUTUNA", "ST PIERRE ET MIQUELON"}


def lire_effectifs_etab(motif: str, an: int) -> pd.DataFrame:
    df = pd.read_csv(ETAB / motif.format(an=an), sep=";", low_memory=False).copy()
    df["sect"] = df["secteur"].str.upper().map(SECTEUR)
    assert df["sect"].notna().all(), df["secteur"].unique()
    df["com"] = df["academie"].str.upper().isin(COM)
    return df


comp = []
for an in (2024, 2025):
    for nom, (motif, col, niv_nat) in FICHIERS.items():
        df = lire_effectifs_etab(motif, an)
        for champ, base in (("open data complet", df), ("hors COM (champ DEPP)", df[~df["com"]])):
            for secteur in ("public", "prive_sc", "ensemble"):
                sous = base if secteur == "ensemble" else base[base["sect"] == secteur]
                somme = float(sous[col].sum())
                ref = nat.get((niv_nat, secteur, an))
                comp.append({"rentree": an, "fichier": nom, "champ": champ, "secteur": secteur,
                             "nb_etablissements": len(sous), "somme_eleves_open_data": int(somme),
                             "total_national_DEPP": int(ref) if ref else "",
                             "ecart_%": round(100 * (somme / ref - 1), 2) if ref else ""})
ecrire_csv(RESULTATS / "E2_effectifs_open_data_vs_DEPP.csv", comp)
journal.ecrire(RESULTATS / "tracabilite_E.csv")

if __name__ == "__main__":
    for l in lignes:
        print(l)
    print()
    for c in comp:
        print(f"{c['rentree']} {c['fichier']:10} {c['champ']:22} {c['secteur']:9} {c['nb_etablissements']:6} "
              f"{c['somme_eleves_open_data']:>9} vs {c['total_national_DEPP']:>9} écart {c['ecart_%']} %")
