"""Tâche E.3 (suite) — Taille moyenne des établissements publics, Paris / Seine-Saint-Denis / France, rentrée 2024.

1. B1 : élèves (du secondaire pour les collèges et lycées, post-bac exclu) / établissements, par type.
2. Pour les lycées, ajout des étudiants post-bac (STS, CPGE) accueillis dans les mêmes UAI, d'après le jeu DEPP
   « Le mode d'hébergement des élèves dans les établissements du second degré », rentrée 2024 (archivé par le projet :
   data/raw/etablissements/effectifs_hebergement_2d_rentree2024.csv ; colonne
   nombre_d_eleves_dans_une_formation_du_superieur), pour mesurer l'occupation des bâtiments.
3. Moyenne pondérée par les élèves (taille de l'établissement d'un élève moyen) en plus de la moyenne simple.
Sortie : e3d_taille_etablissements_2024.csv
"""
import sys
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
R = Path("C:/Users/chret/Documents/EtatEcole")
OUT = Path(__file__).resolve().parent
b1 = pd.read_csv(R / "resultats/B1_depense_publique_par_etablissement_2025.csv", sep=";", encoding="utf-8-sig",
                 low_memory=False, dtype={"code_departement": str, "uai": str})
h = pd.read_csv(R / "data/raw/etablissements/effectifs_hebergement_2d_rentree2024.csv", sep=";", encoding="utf-8-sig",
                low_memory=False, dtype={"uai": str, "code_departement": str})
h = h[["uai", "nombre_d_eleves_dans_une_formation_du_superieur"]].rename(
    columns={"nombre_d_eleves_dans_une_formation_du_superieur": "postbac"})
h["postbac"] = pd.to_numeric(h["postbac"], errors="coerce")
b = b1[b1["secteur"].eq("public")].merge(h, on="uai", how="left")
LYC = ["lycée général et technologique", "lycée polyvalent", "lycée professionnel"]
GROUPES = {"écoles": b["type"].eq("école"), "collèges": b["type"].eq("collège"),
           "lycées (GT + polyvalents + professionnels)": b["type"].isin(LYC),
           "lycées GT": b["type"].eq("lycée général et technologique"), "lycées polyvalents": b["type"].eq("lycée polyvalent"),
           "lycées professionnels": b["type"].eq("lycée professionnel")}
TERR = {"Paris": b["code_departement"].eq("75"), "Seine-Saint-Denis": b["code_departement"].eq("93"),
        "France": pd.Series(True, index=b.index)}
lignes = []
for g, mg in GROUPES.items():
    for t, mt in TERR.items():
        d = b[mg & mt]
        n, e = len(d), d["eleves"].sum()
        ligne = {"type (public)": g, "territoire": t, "etablissements": n, "eleves": int(e),
                 "eleves_par_etablissement": round(e / n, 1),
                 "taille_moyenne_ponderee_par_eleves": round((d["eleves"] ** 2).sum() / e, 1)}
        if g != "écoles":
            pb = d["postbac"].fillna(0).sum()
            ligne.update({"etudiants_postbac_dans_ces_UAI": int(pb), "UAI_sans_donnee_hebergement": int(d["postbac"].isna().sum()),
                          "eleves_et_etudiants_par_etablissement": round((e + pb) / n, 1)})
        lignes.append(ligne)
out = pd.DataFrame(lignes)
out.to_csv(OUT / "e3d_taille_etablissements_2024.csv", sep=";", index=False, encoding="utf-8-sig")
pd.set_option("display.width", 250)
print(out.to_string(index=False))
