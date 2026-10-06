# -*- coding: utf-8 -*-
"""Recherche dans le jeu « Actes administratifs de la Région Île-de-France » (data.iledefrance.fr)."""
import json
import sys
import requests

sys.stdout.reconfigure(encoding='utf-8')
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
API = 'https://data.iledefrance.fr/api/explore/v2.1/catalog/datasets/actes-administratifs/records'

QUERIES = sys.argv[1:] or [
    'titre like "%PLAN PLURIANNUEL%" and titre like "%LYC%"',
    'titre like "%PLAN D\'URGENCE%" and titre like "%LYC%"',
    'titre like "%PPI%" and titre like "%LYC%"',
    'titre like "%PROGRAMME PREVISIONNEL%" and titre like "%LYC%"',
    'titre like "%PATRIMOINE%" and titre like "%LYC%"',
    'titre like "%SCHEMA%" and titre like "%LYC%"',
]
for q in QUERIES:
    r = requests.get(API, params={'where': q, 'select': 'identifiant,numero,titre,type_acte,type,date_decision,type_seance,url_acte',
                                  'limit': 100, 'order_by': 'date_decision'}, timeout=60)
    d = r.json()
    print('=====', q, d.get('total_count'), d.get('message', ''))
    for x in d.get('results', []):
        print(x['date_decision'], '|', x['numero'], '|', x['type_acte'], '|', x.get('type'), '|', (x['titre'] or '')[:170].replace('\n', ' '), '|', x['identifiant'])
