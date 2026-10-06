# -*- coding: utf-8 -*-
"""Télécharge des actes complets (JSON) du jeu « Actes administratifs de la Région Île-de-France »."""
import json
import re
import sys
import requests

sys.stdout.reconfigure(encoding='utf-8')
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
API = 'https://data.iledefrance.fr/api/explore/v2.1/catalog/datasets/actes-administratifs/records'

ids = sys.argv[1:]
for i in ids:
    r = requests.get(API, params={'where': f'identifiant="{i}"', 'limit': 10}, timeout=120)
    d = r.json()
    res = d.get('results', [])
    print('=====', i, len(res))
    if not res:
        continue
    x = res[0]
    with open(W + f'raw/IDF_acte_{i}.json', 'w', encoding='utf-8') as f:
        json.dump(x, f, ensure_ascii=False, indent=1)
    for k, v in x.items():
        if v is None:
            continue
        s = re.sub(r'<[^>]+>', ' ', str(v))
        s = re.sub(r'\s+', ' ', s)
        print(f'--- {k} ({len(s)} car.): {s[:600]}')
