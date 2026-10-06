# -*- coding: utf-8 -*-
"""Exploration du jeu « Données budgétaires des lycées - subventions votées » (Région IdF)."""
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_colwidth', 80)
pd.set_option('display.max_rows', 300)

W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
s = pd.read_csv(W + 'raw/IDF_opendata_subventions-votees-pour-les-lycees.csv', sep=';', encoding='utf-8-sig', dtype=str)
s['m'] = pd.to_numeric(s['montant_vote'], errors='coerce')
print(s.shape, s['m'].isna().sum())
print(s.groupby('annee_de_la_decision')['m'].agg(['sum', 'count']))
print(s['type_de_decision'].value_counts())
print(s['type_de_tiers'].value_counts())
print(s['direction_du_gestionnaire_du_dossier_reference'].value_counts())
print(s['procedure_du_dossier_son_profil_code'].value_counts())
g = s.groupby(['procedure_du_dossier_code', 'procedure_du_dossier', 'procedure_du_dossier_son_profil_code'])['m'].agg(['sum', 'count']).sort_values('sum', ascending=False)
print(g)
print(s['date_deliberation'].min(), s['date_deliberation'].max())
