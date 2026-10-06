"""Tâche E.1 (suite) — Vérifie que, dans B, la part du département est la même par collégien dans tout le département
et la part de la région la même par lycéen dans toute la région ; et que la part de la commune est la même par
écolier du public dans toute la commune (Paris = une seule commune, 75056).

Entrées (lecture seule) : B1 (resultats) et data/processed/base_2d_rentree2024.csv (élèves par niveau, par UAI),
data/processed/base_ecoles_rentree2024.csv n'est pas nécessaire (la clé communale est lue dans B1).
Sortie : e1b_cles_uniformes.csv (dossier de travail).
"""
import sys
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
R = Path("C:/Users/chret/Documents/EtatEcole")
OUT = Path(__file__).resolve().parent
b1 = pd.read_csv(R / "resultats/B1_depense_publique_par_etablissement_2025.csv", sep=";", encoding="utf-8-sig",
                 low_memory=False, dtype={"code_departement": str, "uai": str, "code_commune_norm": str})
b2 = pd.read_csv(R / "data/processed/base_2d_rentree2024.csv", sep=";", low_memory=False,
                 dtype={"code_departement": str, "uai": str})
d = b1[b1["degre"].eq("2nd degré") & b1["secteur"].eq("public")].merge(
    b2[["uai", "eleves_college", "eleves_lycee_gt", "eleves_lycee_pro", "region_academique"]], on="uai", how="left")
assert d["eleves_college"].notna().all()
d["lyceens"] = d["eleves_lycee_gt"].fillna(0) + d["eleves_lycee_pro"].fillna(0)
d["dep_par_collegien"] = d["ct_colleges"] / d["eleves_college"].where(d["eleves_college"] > 0)
d["reg_par_lyceen"] = d["ct_lycees"] / d["lyceens"].where(d["lyceens"] > 0)

lignes = []
for nom, m in (("Paris", d["code_departement"].eq("75")), ("Seine-Saint-Denis", d["code_departement"].eq("93")),
               ("Île-de-France (région académique)", d["region_academique"].str.upper().str.contains("ILE-DE-FRANCE|ÎLE-DE-FRANCE", regex=True))):
    x = d[m]
    for col, lib in (("dep_par_collegien", "part du département par collégien (€)"),
                     ("reg_par_lyceen", "part de la région par lycéen (€)")):
        v = x[col].dropna()
        lignes.append({"territoire": nom, "grandeur": lib, "etablissements": int(v.size),
                       "min": round(v.min(), 2), "max": round(v.max(), 2)})
    # Établissements de type « lycée » ayant aussi des collégiens : cause de la variation de ct_lycees par élève.
    lyc = x[x["type"].str.startswith("lycée")]
    lignes.append({"territoire": nom, "grandeur": "lycées publics ayant des élèves de niveau collège (nombre / élèves de niveau collège)",
                   "etablissements": int((lyc["eleves_college"] > 0).sum()), "min": float(lyc["eleves_college"].sum()),
                   "max": None})
# Écoles publiques : clé communale (par élève) dans Paris et dans le 93, par commune.
e = b1[b1["degre"].eq("1er degré") & b1["secteur"].eq("public")].copy()
e["commune_par_eleve"] = e["ct_ecoles"] / e["eleves"]
for nom, m in (("Paris", e["code_departement"].eq("75")), ("Seine-Saint-Denis", e["code_departement"].eq("93"))):
    x = e[m]
    g = x.groupby("code_commune_norm").agg(eleves=("eleves", "sum"), ct=("ct_ecoles", "sum"),
                                         mini=("commune_par_eleve", "min"), maxi=("commune_par_eleve", "max"),
                                         cle=("cle_commune", "first"), commune=("commune", "first"))
    g["par_eleve"] = g["ct"] / g["eleves"]
    lignes.append({"territoire": nom, "grandeur": "écoles publiques : communes (nombre) ; écart max intra-commune de la part communale par élève (€)",
                   "etablissements": int(len(g)), "min": round(float((g["maxi"] - g["mini"]).max()), 4), "max": None})
    if nom == "Seine-Saint-Denis":
        g.sort_values("par_eleve").round(1).to_csv(OUT / "e1b_93_part_communale_par_commune.csv", sep=";",
                                                    encoding="utf-8-sig")
        print(g.sort_values("par_eleve")[["commune", "eleves", "par_eleve", "cle"]].round(0).to_string())
out = pd.DataFrame(lignes)
out.to_csv(OUT / "e1b_cles_uniformes.csv", sep=";", index=False, encoding="utf-8-sig")
print(out.to_string(index=False))
