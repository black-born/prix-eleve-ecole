# -*- coding: utf-8 -*-
"""Décompte par département des listes officielles de la Région Île-de-France :
1. CR 2017-059 (plan d'urgence, 10/03/2017), annexes 1 à 5 à la délibération (pages 81 à 93 du rapport) :
   places nouvelles, rénovations globales, opérations ciblées, « toit-façade », internats ;
2. CR 2021-012 (revoyure, 04/02/2021), annexe 2 au rapport : « Lycées très vétustes en 2016 » ;
   annexe 1 : « Point d'étape par département des grandes opérations lancées ou livrées depuis 2016 ».
3. Région, open data « Lycées – données générales » : année de construction (champ ANNEE_CONSTRUCTION, renseigné pour une
   partie des lycées ; la CRC signale des datations inexactes).
Textes extraits avec pdftotext (-raw pour 2017, -layout pour 2021), fichiers txt/ du dossier de travail.
Sorties : resultats/listes_officielles_par_departement.csv, resultats/annee_construction_par_departement.csv
"""
import re
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
DEPS = ['75', '77', '78', '91', '92', '93', '94', '95']

# ---------- 1. CR 2017-059, annexes
t = open(W + 'txt/IDF_CR2017-059RAP_annexes_raw.txt', encoding='utf-8').read().split('\n')
sec, out = None, []
for line in t:
    if 'LISTE DES CREATION DE PLACES' in line:
        sec = 'places nouvelles'
    elif 'LISTE DES OPERATIONS DE RENOVATION GLOBALE' in line:
        sec = 'rénovation globale'
    elif 'LISTE DES OPERATIONS CIBLEES' in line:
        sec = 'opérations ciblées'
    elif 'TOIT-FACADE' in line or 'TOIT FAÇADE' in line:
        sec = 'toit-façade'
    elif "LISTE DES OPERATIONS D'INTERNAT" in line or 'LISTE DES OPERATIONS D’INTERNAT' in line:
        sec = 'internats'
    if re.match(r'^\d+ / 93\s*$', line.strip()):
        continue  # numéro de page « 91 / 93 », « 93 / 93 »… à ne pas lire comme un département
    m = re.match(r'^(75|77|78|91|92|93|94|95)\b\s*(.*)$', line.strip())
    if sec and m:
        places = None
        if sec == 'places nouvelles':
            mm = re.search(r'(\d[\d ]*)$', line.strip())
            places = int(mm.group(1).replace(' ', '')) if mm else None
        out.append({'liste': sec, 'dep': m.group(1), 'ligne': m.group(2), 'places': places})
p17 = pd.DataFrame(out)  # doublons conservés : ils figurent tels quels dans les annexes
# Places nouvelles : plusieurs nombres sont sur la ligne suivante du PDF (lycées neufs à localiser) ; on retient la lecture
# manuelle de l'annexe 1 (txt/IDF_CR2017-059RAP_annexes_raw.txt), contrôlée par le total publié de 21 600 places.
PLACES_2017 = {'75': 0, '77': 800 + 400 + 1200 + 200 + 250 + 500, '78': 300 + 600 + 200 + 300,
               '91': 400 + 600 + 600 + 500 + 1200 + 400 + 400 + 500, '92': 400 + 1200 + 1200 + 400 + 1200 + 200,
               '93': 800 + 400 + 400 + 800 + 800 + 300 + 400 + 250, '94': 1000 + 400, '95': 1200 + 400 + 500}
assert sum(PLACES_2017.values()) == 21600
print(p17.groupby(['liste', 'dep']).size().unstack(fill_value=0))
print(p17.groupby('liste').size())
print('places nouvelles lues :', p17.loc[p17['liste'] == 'places nouvelles'].groupby('dep')['places'].sum().to_dict())

# ---------- 2. CR 2021-012, annexes 1 et 2
t = open(W + 'txt/IDF_CR2021-012RAP_annexes_layout.txt', encoding='utf-8').read().split('\n')
sec, a1, a2 = None, [], []
for line in t:
    if 'Annexe 1 : Point' in line:
        sec = 'a1'
    elif 'Annexe 2' in line and 'vétustes' in line:
        sec = 'a2'
    elif 'Annexe 3' in line:
        sec = None
    m = re.match(r'^\s*(75|77|78|91|92|93|94|95)\s+(.*)$', line)
    if sec == 'a1' and m:
        etat = 'livré' if 'livré' in line else ('en cours' if 'en cours' in line else '')
        a1.append({'dep': m.group(1), 'ligne': re.sub(r'\s+', ' ', m.group(2)).strip(), 'etat': etat})
    if sec == 'a2' and m:
        a2.append({'dep': m.group(1), 'ligne': re.sub(r'\s+', ' ', m.group(2)).strip()})
a1 = pd.DataFrame(a1)
a2 = pd.DataFrame(a2)
print('Annexe 2 (lycées très vétustes en 2016) :', len(a2))
print(a2.groupby('dep').size())
print('Annexe 1 (grandes opérations 2016-2021) :', len(a1))
print(pd.crosstab(a1['dep'], a1['etat']))

rows = []
for d in DEPS:
    r = {'dep': d}
    for l in ['places nouvelles', 'rénovation globale', 'opérations ciblées', 'toit-façade', 'internats']:
        r['PPI2017_' + l] = int(((p17['liste'] == l) & (p17['dep'] == d)).sum())
    r['PPI2017_places_nouvelles_nb'] = PLACES_2017[d]
    r['tres_vetustes_2016'] = int((a2['dep'] == d).sum())
    r['grandes_operations_2016_2021'] = int((a1['dep'] == d).sum())
    rows.append(r)
res = pd.DataFrame(rows)
# Dossier de presse de la Région, rentrée 2026-2027 (07/09/2026), p. 35 : lycées publics et lycées ayant bénéficié de plus de 1 M€ de travaux depuis 2016
dp = {'75': (93, 72), '77': (55, 43), '78': (52, 41), '91': (47, 46), '92': (58, 41), '93': (66, 51), '94': (49, 33), '95': (48, 35)}
res['lycees_publics_DP2026'] = res['dep'].map(lambda d: dp[d][0])
res['lycees_plus_1MEUR_travaux_depuis_2016_DP2026'] = res['dep'].map(lambda d: dp[d][1])
res['part_lycees_travaux_DP2026'] = res['lycees_plus_1MEUR_travaux_depuis_2016_DP2026'] / res['lycees_publics_DP2026']
print(res.to_string())
res.to_csv(W + 'resultats/listes_officielles_par_departement.csv', sep=';', index=False, encoding='utf-8-sig')
a2.to_csv(W + 'resultats/lycees_tres_vetustes_2016_CR2021-012.csv', sep=';', index=False, encoding='utf-8-sig')
p17.to_csv(W + 'resultats/PPI2017_listes_CR2017-059.csv', sep=';', index=False, encoding='utf-8-sig')

# ---------- 3. Année de construction (open data Région)
g = pd.read_csv(W + 'raw/IDF_opendata_lycees-donnees-generales.csv', sep=';', encoding='utf-8-sig', dtype=str)
g = g[g['statut'] == 'public'].copy()
g['annee'] = pd.to_numeric(g['annee_construction'], errors='coerce')
rows = []
for d, gg in list(g.groupby('dep')) + [('IDF', g)]:
    a = gg['annee'].dropna()
    rows.append({'dep': d, 'lycees_publics': len(gg), 'annee_renseignee': len(a), 'mediane': a.median(),
                 'part_avant_1970': (a < 1970).mean(), 'part_1970_1999': ((a >= 1970) & (a < 2000)).mean(), 'part_2000_et_apres': (a >= 2000).mean(),
                 'part_avant_1900': (a < 1900).mean()})
yc = pd.DataFrame(rows)
print(yc.round(2).to_string())
yc.to_csv(W + 'resultats/annee_construction_par_departement.csv', sep=';', index=False, encoding='utf-8-sig')
