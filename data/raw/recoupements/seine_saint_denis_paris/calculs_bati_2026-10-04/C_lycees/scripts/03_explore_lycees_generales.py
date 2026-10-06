# -*- coding: utf-8 -*-
"""Exploration des jeux « Lycées – données générales » et « Lycées – données pédagogiques » (Région IdF)."""
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 40)
pd.set_option('display.max_colwidth', 60)
pd.set_option('display.max_rows', 400)

W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
g = pd.read_csv(W + 'raw/IDF_opendata_lycees-donnees-generales.csv', sep=';', encoding='utf-8-sig', dtype=str)
print(g.shape)
print(g.columns.tolist())
print(g.head(3).T)
for c in ['dep', 'nature_uai', 'statut', 'contrat_etablissement', 'ministere_tutelle', 'internat', 'date_maj']:
    print(g[c].value_counts(dropna=False).head(30))
print(g['annee_construction'].describe())
print(g['annee_construction'].value_counts(dropna=False).head(30))
print(pd.crosstab(g['dep'], g['statut']))

p = pd.read_csv(W + 'raw/IDF_opendata_lycees-donnees-pedagogiques.csv', sep=';', encoding='utf-8-sig', dtype=str)
print(p.shape)
print(p.columns.tolist())
print(p['annee_scolaire'].value_counts().sort_index())
print(p.head(5).T)
