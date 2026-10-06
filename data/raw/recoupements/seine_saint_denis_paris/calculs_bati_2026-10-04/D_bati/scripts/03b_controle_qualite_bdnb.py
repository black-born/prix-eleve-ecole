# -*- coding: utf-8 -*-
"""Contrôle de qualité des années de construction BDNB (script 03) et variante « hors artefact ».

Constat : pour les bâtiments dont le propriétaire est la Ville de Paris, la BDNB (champ
annee_construction, source fichiers fonciers) indique très souvent 2023 ou 2024, y compris pour des
écoles anciennes (ex. école élémentaire Tanger, 19e : 2023 dans les fichiers fonciers, 1948 dans le DPE).
Ces années sont traitées comme inconnues dans la variante ci-dessous (années >= 2020).

Entrée  : ../resultats/bdnb_periodes_par_etablissement.csv, ../resultats/etab_rnb_bdnb.csv
Sorties : ../resultats/bdnb_controle_qualite.csv, ../resultats/bdnb_periodes_synthese_hors_artefact.csv
"""
import sys

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/D_bati/resultats"
e = pd.read_csv(ROOT + "/bdnb_periodes_par_etablissement.csv", sep=";", dtype={"code_departement": str})
l = pd.read_csv(ROOT + "/etab_rnb_bdnb.csv", sep=";", dtype={"code_departement": str})

# Contrôle : années >= 2020 par département et propriétaire « VILLE DE PARIS »
q = []
for dep, g in e.groupby("code_departement"):
    y = g.annee_construction.dropna()
    q.append({"departement": dep, "batiments_principaux_annee_connue": len(y),
              "annee_2023": int((y == 2023).sum()), "annee_2024": int((y == 2024).sum()),
              "annees_>=2020": int((y >= 2020).sum()),
              "part_>=2020_%": round((y >= 2020).mean() * 100, 1)})
qc = pd.DataFrame(q)
print(qc.to_string(index=False))
own = l[(l.code_departement == "075") & (l.annee_construction >= 2020)].l_denomination_proprietaire.value_counts()
print("\nPropriétaires des constructions parisiennes datées >= 2020 :\n", own.head(5))
qc.to_csv(ROOT + "/bdnb_controle_qualite.csv", sep=";", index=False, encoding="utf-8")

# Variante : années >= 2020 traitées comme inconnues
LAB = ["avant 1914", "1914-1944", "1945-1969", "1970-1979", "1980-1999", "2000-2019"]


def periode(a):
    if pd.isna(a) or a >= 2020:
        return "inconnue"
    a = int(a)
    for lim, lab in zip([1914, 1945, 1970, 1980, 2000, 2020], LAB):
        if a < lim:
            return lab
    return "inconnue"


e["periode_v2"] = e.annee_construction.map(periode)
rows = []
for (dep, cat), g in e.groupby(["code_departement", "categorie"]):
    connu = (g.periode_v2 != "inconnue").sum()
    d = {"departement": dep, "categorie": cat, "etablissements": len(g), "annee_plausible_connue": int(connu),
         "part_%": round(connu / len(g) * 100, 1),
         "annee_mediane": int(np.nanmedian(g.annee_construction.where(g.annee_construction < 2020)))}
    for lab in LAB:
        d[lab + " (%)"] = round((g.periode_v2 == lab).sum() / connu * 100, 1) if connu else None
    rows.append(d)
syn = pd.DataFrame(rows)
print("\n", syn.to_string(index=False))
syn.to_csv(ROOT + "/bdnb_periodes_synthese_hors_artefact.csv", sep=";", index=False, encoding="utf-8")
