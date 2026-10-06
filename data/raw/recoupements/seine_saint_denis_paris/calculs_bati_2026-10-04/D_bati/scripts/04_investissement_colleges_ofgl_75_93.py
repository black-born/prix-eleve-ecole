# -*- coding: utf-8 -*-
"""Dépenses d'équipement des départements pour les collèges (fonction 221), 2022-2025 :
Seine-Saint-Denis et Ville de Paris (compétence départementale), comparées à l'ensemble des
départements de France (budgets principaux et annexes du fichier OFGL).

Entrée : C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/OFGL_departements_fonctionnelle_fonction2_2022-2025.csv
         (OFGL, jeu « ofgl-base-departements-fonctionnelle », extraction du projet ; lecture seule)
Sortie : ../resultats/ofgl_equipement_colleges_75_93.csv

Rapport aux élèves : collégiens du public à la rentrée 2024 (B1 du projet : Paris 50 392 ; 93 78 410).
Ce rapport est un ordre de grandeur (élèves de la rentrée 2024 appliqués aux quatre exercices).
"""
import sys

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
SRC = r"C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/OFGL_departements_fonctionnelle_fonction2_2022-2025.csv"
OUT = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/D_bati/resultats/ofgl_equipement_colleges_75_93.csv"

df = pd.read_csv(SRC, sep=";", dtype=str, encoding="utf-8-sig")
df["montant"] = pd.to_numeric(df.montant, errors="coerce")
sel = df[(df.fonction == "221") & (df.agregat == "Dépenses d'équipement")]
tot = sel.groupby(["exer", "dep_code", "dep_name", "categ"], as_index=False).montant.sum()
eleves = {"93": 78410, "75": 50392}
out = tot[tot.dep_code.isin(["93", "75"])].copy()
out["eleves_public_rentree2024"] = out.dep_code.map(eleves)
out["euros_par_collegien_public"] = (out.montant / out.eleves_public_rentree2024).round(0)
out["montant_M€"] = (out.montant / 1e6).round(1)
nat = sel.groupby("exer", as_index=False).montant.sum().rename(columns={"montant": "total_tous_departements"})
out = out.merge(nat, on="exer")
out["total_tous_departements_M€"] = (out.total_tous_departements / 1e6).round(1)
out = out.sort_values(["dep_code", "exer"])
print(out[["exer", "dep_code", "dep_name", "categ", "montant_M€", "euros_par_collegien_public",
           "total_tous_departements_M€"]].to_string(index=False))
moy = out.groupby("dep_code").montant.mean() / pd.Series(eleves)
print("Moyenne 2022-2025, € par collégien du public :", moy.round(0).to_dict())
out.to_csv(OUT, sep=";", index=False, encoding="utf-8")
