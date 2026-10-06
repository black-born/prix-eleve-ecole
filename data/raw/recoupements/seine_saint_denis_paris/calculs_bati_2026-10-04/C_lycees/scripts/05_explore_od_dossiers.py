# -*- coding: utf-8 -*-
"""Opérations directes : repérage du département dans le libellé du dossier quand l'UAI manque."""
import re
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_colwidth', 110)
pd.set_option('display.max_rows', 2000)

W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
o = pd.read_csv(W + 'raw/IDF_opendata_donnees-budgetaires-lycees-operations-directes.csv', sep=';', encoding='utf-8-sig', dtype=str)
o['m'] = pd.to_numeric(o['montant_vote'], errors='coerce')
na = o[o['code_uai_ex_rne'].isna()].copy()
print(len(na), na['m'].sum() / 1e6)
na = na.sort_values('m', ascending=False)
for _, r in na.iterrows():
    print(f"{r['annee_de_la_decision']} | {r['direction_du_gestionnaire_de_l_operation_reference']} | {r['m']/1e6:9.3f} | {r['dossier']} | {str(r['objet_de_l_operation'])[:80]!r}")
