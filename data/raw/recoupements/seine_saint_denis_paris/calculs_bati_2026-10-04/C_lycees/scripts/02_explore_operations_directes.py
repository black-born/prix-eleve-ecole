# -*- coding: utf-8 -*-
"""Exploration du jeu « Données budgétaires des lycées - opérations directes votées » (Région IdF)."""
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_rows', 400)

W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
o = pd.read_csv(W + 'raw/IDF_opendata_donnees-budgetaires-lycees-operations-directes.csv', sep=';', encoding='utf-8-sig', dtype=str)
o['m'] = pd.to_numeric(o['montant_vote'], errors='coerce')
print(o.shape, o['m'].isna().sum())
print(o.columns.tolist())
print(o.groupby('annee_de_la_decision')['m'].agg(['sum', 'count']))
print(o['type_de_decision'].value_counts())
print(o['type_de_tiers'].value_counts(dropna=False))
print(o['direction_du_gestionnaire_de_l_operation_reference'].value_counts(dropna=False))
print('UAI renseigne:', o['code_uai_ex_rne'].notna().sum(), 'montant avec UAI', o.loc[o['code_uai_ex_rne'].notna(), 'm'].sum(), 'total', o['m'].sum())
g = o.groupby(['procedure_de_l_operation_code', 'procedure_de_l_operation_libelle'])['m'].agg(['sum', 'count']).sort_values('sum', ascending=False)
print(g)
print(o['date_deliberation'].min(), o['date_deliberation'].max())
print(o.sort_values('m', ascending=False).head(40)[['annee_de_la_decision', 'code_uai_ex_rne', 'tiers', 'dossier', 'procedure_de_l_operation_libelle', 'objet_de_l_operation', 'm']])
print(o.sample(30, random_state=1)[['annee_de_la_decision', 'code_uai_ex_rne', 'tiers', 'dossier', 'procedure_de_l_operation_libelle', 'objet_de_l_operation', 'm']])
