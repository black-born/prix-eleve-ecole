# -*- coding: utf-8 -*-
"""Tableau final : période de construction du bâtiment principal (BDNB, années plausibles < 2020),
rapportée à l'ensemble des établissements publics ouverts de l'annuaire MEN (075, 093).

Entrées : ../sources/MEN_geoloc_etablissements_075_093_API.csv ; ../resultats/bdnb_periodes_par_etablissement.csv
Sortie  : ../resultats/bdnb_tableau_final.csv
"""
import sys

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/D_bati"
men = pd.read_csv(ROOT + "/sources/MEN_geoloc_etablissements_075_093_API.csv", sep=";", dtype=str)
men = men[(men.secteur_public_prive_libe == "Public") & (men.etat_etablissement_libe == "OUVERT")].copy()


def categorie(n):
    n = str(n)
    if n.startswith("ECOLE"):
        return "école"
    if n.startswith("COLLEGE"):
        return "collège"
    if n.startswith("LYCEE") or n.startswith("ETAB REGIONAL"):
        return "lycée"
    return "autre"


men["categorie"] = men.nature_uai_libe.map(categorie)
men = men[men.categorie != "autre"]
tot = men.groupby(["code_departement", "categorie"]).size().rename("etablissements_publics_MEN")

e = pd.read_csv(ROOT + "/resultats/bdnb_periodes_par_etablissement.csv", sep=";", dtype={"code_departement": str})
e["a"] = e.annee_construction.where(e.annee_construction < 2020)
LAB = [("avant 1914", 0, 1914), ("1914-1944", 1914, 1945), ("1945-1969", 1945, 1970),
       ("1970-1979", 1970, 1980), ("1980-1999", 1980, 2000), ("2000-2019", 2000, 2020)]
rows = []
for (dep, cat), g in e.groupby(["code_departement", "categorie"]):
    a = g.a.dropna()
    d = {"departement": dep, "categorie": cat,
         "etablissements_publics_MEN": int(tot.loc[(dep, cat)]),
         "annee_plausible_connue": len(a),
         "couverture_%": round(len(a) / tot.loc[(dep, cat)] * 100, 0),
         "annee_mediane": int(np.median(a))}
    for lab, lo, hi in LAB:
        d[lab + " %"] = round(((a >= lo) & (a < hi)).sum() / len(a) * 100, 0)
    d["avant 1970 %"] = round((a < 1970).sum() / len(a) * 100, 0)
    rows.append(d)
res = pd.DataFrame(rows)
print(res.to_string(index=False))
res.to_csv(ROOT + "/resultats/bdnb_tableau_final.csv", sep=";", index=False, encoding="utf-8")
