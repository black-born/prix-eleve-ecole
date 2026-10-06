# -*- coding: utf-8 -*-
"""Dates d'ouverture administrative (champ date_ouverture de l'annuaire géolocalisé MEN/DEPP) des
établissements publics ouverts de Paris (075) et de la Seine-Saint-Denis (093).

But : (1) montrer la limite de l'indicateur « âge des établissements » utilisé par l'OFGL (Cap sur n° 21,
2023, partie 4.1), fondé sur cette date ; (2) compter les établissements ouverts récemment.

Entrée  : ../sources/MEN_geoloc_etablissements_075_093_API.csv (script 01)
Sortie  : ../resultats/dates_ouverture_75_93.csv (+ affichage console)
"""
import sys

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/D_bati"

df = pd.read_csv(ROOT + "/sources/MEN_geoloc_etablissements_075_093_API.csv", sep=";", dtype=str)
df = df[(df.secteur_public_prive_libe == "Public") & (df.etat_etablissement_libe == "OUVERT")].copy()


def categorie(n):
    n = str(n)
    if n.startswith("ECOLE"):
        return "école"
    if n.startswith("COLLEGE"):
        return "collège"
    if n.startswith("LYCEE") or n.startswith("ETAB REGIONAL"):
        return "lycée"
    return "autre"


df["categorie"] = df.nature_uai_libe.map(categorie)
df = df[df.categorie != "autre"].copy()
df["date"] = pd.to_datetime(df.date_ouverture, errors="coerce")
df["annee"] = df.date.dt.year

# Date la plus fréquente (date de création de la base, pas date de construction)
mode = df.date_ouverture.value_counts().idxmax()
print("Date d'ouverture la plus fréquente :", mode)

bins = [0, 1965, 1966, 1973, 1990, 2000, 2010, 2100]
labels = ["avant le 01/05/1965", "1965 (dont 01/05/1965)", "1966-1972", "1973-1989",
          "1990-1999", "2000-2009", "2010 et après"]
df["tranche"] = pd.cut(df.annee, bins=bins, labels=labels, right=False)

rows = []
for (dep, cat), g in df.groupby(["code_departement", "categorie"]):
    n = len(g)
    d = {
        "departement": dep, "categorie": cat, "etablissements": n,
        "part_date_01_05_1965": round((g.date_ouverture == "1965-05-01").mean() * 100, 1),
        "part_ouverts_avant_1973 (critère OFGL > 50 ans en 2023)": round((g.annee < 1973).mean() * 100, 1),
        "ouverts_depuis_1990": int((g.annee >= 1990).sum()),
        "ouverts_depuis_2000": int((g.annee >= 2000).sum()),
        "part_ouverts_depuis_2000": round((g.annee >= 2000).mean() * 100, 1),
    }
    rows.append(d)
res = pd.DataFrame(rows)
print(res.to_string(index=False))
res.to_csv(ROOT + "/resultats/dates_ouverture_75_93.csv", sep=";", index=False, encoding="utf-8")

tab = pd.crosstab([df.code_departement, df.categorie], df.tranche)
print(tab)
tab.to_csv(ROOT + "/resultats/dates_ouverture_75_93_tranches.csv", sep=";", encoding="utf-8")
