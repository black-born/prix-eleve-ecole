# -*- coding: utf-8 -*-
"""Subventions d'investissement de l'État (DETR, DSIL, DSID, DPV ; hors fonds vert) accordées en 2023
aux collectivités de la Seine-Saint-Denis : part des projets scolaires.

Entrée : ../sources/Pref93_programmation_generale_2023_hors_FV.pdf (préfecture de la Seine-Saint-Denis,
         « Tableau général programmation 2023 », page « Bilan programmation 2023 »)
Sortie : ../resultats/pref93_programmation_2023_projets.csv et affichage de la synthèse.

Projet « scolaire » : intitulé contenant école, scolaire, maternel(le), élémentaire, collège, lycée,
classe(s), restauration scolaire (expression régulière ci-dessous, à relire à la main : les
lignes retenues sont imprimées).
"""
import re
import sys

import pandas as pd
import pdfplumber

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/D_bati"
pdf = pdfplumber.open(ROOT + "/sources/Pref93_programmation_generale_2023_hors_FV.pdf")
rows = []
for page in pdf.pages:
    for tb in page.extract_tables():
        for r in tb:
            rows.append([(c or "").replace("\n", " ").strip() for c in r])
cols = rows[0]
data = [r for r in rows[1:] if r[0] != "Arrondissement"]
df = pd.DataFrame(data, columns=["arrondissement", "porteur", "intitule", "dispositif", "travaux_ht",
                                 "fonctionnement_ttc", "subvention", "taux"])


def eur(s):
    s = str(s).replace("€", "").replace("\u202f", "").replace(" ", "").replace(",", ".").strip()
    try:
        return float(s)
    except ValueError:
        return None


for c in ("travaux_ht", "fonctionnement_ttc", "subvention"):
    df[c] = df[c].map(eur)
rx = re.compile(r"(?i)\b(école|ecole|scolaire|maternel|élémentaire|elementaire|collège|college|lycée|lycee|classes?)\b")
df["scolaire"] = df.intitule.map(lambda t: bool(rx.search(t)))
df.to_csv(ROOT + "/resultats/pref93_programmation_2023_projets.csv", sep=";", index=False, encoding="utf-8")

print("Projets :", len(df), "| subventions totales :", round(df.subvention.sum(), 2), "€")
print(df.groupby("dispositif").subvention.agg(["count", "sum"]).round(0))
sc = df[df.scolaire]
print("\nProjets scolaires retenus :", len(sc))
print(sc[["porteur", "intitule", "dispositif", "travaux_ht", "subvention"]].to_string(index=False))
print("\nSubventions aux projets scolaires :", round(sc.subvention.sum(), 2), "€ ;",
      "travaux HT correspondants :", round(sc.travaux_ht.sum(), 2), "€ ;",
      "part des subventions :", round(sc.subvention.sum() / df.subvention.sum() * 100, 1), "%")
print(sc.groupby("dispositif").subvention.agg(["count", "sum"]).round(0))
