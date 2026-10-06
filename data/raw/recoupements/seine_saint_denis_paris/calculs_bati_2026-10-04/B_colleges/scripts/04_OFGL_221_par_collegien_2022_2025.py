"""Dépenses des départements (et de la Ville de Paris) pour leurs collèges, fonction 221 « Collèges »,
par agrégat OFGL, 2022-2025, en M€ et en euros par collégien du public.

Source des montants : OFGL, « Comptes des départements 2012-2025 – Présentation fonctionnelle »
  (data/raw/collectivites/OFGL_departements_fonctionnelle_fonction2_2022-2025.csv ; budgets principaux) ;
  définitions des agrégats : sources/OFGL_methodologie_formules_agregats_departements_2022-2025.csv.
Compléments DGFiP (balances nature-fonction, script 01) : remboursement en capital des marchés de partenariat
  (compte 1675), absent des agrégats OFGL ; CTU (Corse, Guyane, Martinique), absentes du jeu OFGL.
Dénominateur (année civile N) : 2/3 x collégiens du public à la rentrée N-1 + 1/3 x rentrée N
  (DEPP, open data « fr-en-college-effectifs-niveau-sexe-lv », élèves de niveau collège, secteur public).
Moyenne 2022-2025 : somme des montants / somme des dénominateurs (moyenne pondérée).
Sorties : ../sorties/04_OFGL_221_par_collegien_2022_2025.csv (long) et affichage.
"""
import os
import sys
from importlib import import_module

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 40)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
m02 = import_module('02_comptes_221_93_Paris')
SRC = os.path.join(HERE, '..', 'sources')
OUT = os.path.join(HERE, '..', 'sorties')
OFGL = 'C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/OFGL_departements_fonctionnelle_fonction2_2022-2025.csv'
YEARS = [2022, 2023, 2024, 2025]
IDF = ['75', '77', '78', '91', '92', '93', '94', '95']
NOMS = {'75': 'Paris (Ville de Paris)', '77': 'Seine-et-Marne', '78': 'Yvelines', '91': 'Essonne', '92': 'Hauts-de-Seine',
        '93': 'Seine-Saint-Denis', '94': 'Val-de-Marne', '95': "Val-d'Oise"}
AGR = ["Dépenses d'équipement", "Subventions d'équipement versées", "Autres dépenses d'investissement",
       "Dépenses d'investissement hors remb", 'Frais de personnel', 'Achats et charges externes',
       "Dépenses d'intervention", 'Charges financières', 'Autres dépenses de fonctionnement',
       'Dépenses de fonctionnement', 'Dépenses totales hors remb']

# ------------------------------------------------------------------ dénominateurs
e = pd.read_csv(os.path.join(SRC, 'DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv'), sep=';', dtype={'code_dept': str})
e['r'] = e.rentree_scolaire.str[:4].astype(int)
e = e[e.secteur == 'PUBLIC'].copy()
e['dep'] = e.code_dept
rent = e.groupby(['dep', 'r']).eleves.sum().unstack('r')
COM = ['975', '977', '978', '986', '987', '988']
CTU = ['2A', '2B', '972', '973']
rent_fr_ofgl = rent[~rent.index.isin(COM + CTU)].sum()   # périmètre OFGL : DEPT + Paris + ML
rent_fr_all = rent[~rent.index.isin(COM)].sum()          # + CTU


def civ(series, y):
    return 2 / 3 * series[y - 1] + 1 / 3 * series[y]


den = {}
for y in YEARS:
    for d in IDF:
        den[(d, y)] = civ(rent.loc[d], y)
    den[('FR_OFGL', y)] = civ(rent_fr_ofgl, y)
    den[('FR_ALL', y)] = civ(rent_fr_all, y)

# ------------------------------------------------------------------ OFGL
df = pd.read_csv(OFGL, sep=';', dtype=str, encoding='utf-8-sig')
df['montant'] = df['montant'].astype(float)
df['annee'] = df.exer.str[:4].astype(int)
bp = df[df.type_de_budget == 'Budget principal']
rows = []
for fonc in ['221', '22', '24', '20', '201', '28', '2']:
    x = bp[bp.fonction == fonc]
    for y in YEARS:
        xy = x[x.annee == y]
        for d in IDF:
            s = xy[xy.dep_code == d].groupby('agregat').montant.sum()
            for a in AGR:
                rows.append({'entite': NOMS[d], 'code': d, 'fonction': fonc, 'annee': y, 'agregat': a,
                             'montant': s.get(a, 0.0), 'eleves_public': den[(d, y)]})
        s = xy.groupby('agregat').montant.sum()
        for a in AGR:
            rows.append({'entite': 'France (départements + Paris + Métropole de Lyon, hors CTU)', 'code': 'FR_OFGL',
                         'fonction': fonc, 'annee': y, 'agregat': a, 'montant': s.get(a, 0.0),
                         'eleves_public': den[('FR_OFGL', y)]})
L = pd.DataFrame(rows)

# ------------------------------------------------------------------ compléments DGFiP : 1675 (PPP) et CTU
add = []
for y in YEARS:
    d = m02.prepare(y, 'idf')
    for code in IDF:
        if code == '75':
            mask = (d.categ == 'PARIS')
        else:
            mask = (d.categ == 'DEPT') & (d.ndept == '0' + code)
        ppp221 = d[mask & d.compte.str.startswith('1675') & d.f.str.startswith('221')].montant.sum()
        pppall = d[mask & d.compte.str.startswith('1675')].montant.sum()
        add.append({'entite': NOMS[code], 'code': code, 'fonction': '221', 'annee': y,
                    'agregat': 'Remboursement en capital des marchés de partenariat (1675, fonction 221) [DGFiP]',
                    'montant': ppp221, 'eleves_public': den[(code, y)]})
        add.append({'entite': NOMS[code], 'code': code, 'fonction': 'toutes', 'annee': y,
                    'agregat': 'Remboursement en capital des marchés de partenariat (1675, toutes fonctions) [DGFiP]',
                    'montant': pppall, 'eleves_public': den[(code, y)]})
    n = m02.prepare(y, 'nat')
    n = n[n.f.str.startswith('221') & n.nature.str.startswith(('F_', 'I_'))]
    nn = n[n.categ.isin(['DEPT', 'PARIS', 'ML', 'CTU'])]
    for lab, sel in [("Dépenses d'équipement [DGFiP, avec CTU]", nn.nature == 'I_equipement'),
                     ('Dépenses de fonctionnement [DGFiP, avec CTU]', nn.nature.str.startswith('F_')),
                     ('Remboursement en capital des marchés de partenariat (1675, fonction 221) [DGFiP, avec CTU]',
                      nn.nature == 'I_PPP_remboursement_capital_1675')]:
        add.append({'entite': 'France (départements + Paris + ML + CTU) [DGFiP]', 'code': 'FR_ALL', 'fonction': '221',
                    'annee': y, 'agregat': lab, 'montant': nn[sel].montant.sum(), 'eleves_public': den[('FR_ALL', y)]})
L = pd.concat([L, pd.DataFrame(add)], ignore_index=True)
L['euros_par_collegien_public'] = L.montant / L.eleves_public
L.to_csv(os.path.join(OUT, '04_OFGL_221_par_collegien_2022_2025.csv'), sep=';', index=False, encoding='utf-8-sig')

# ------------------------------------------------------------------ tableaux
def tab(fonc, agrs, entites=None):
    x = L[(L.fonction == fonc) & L.agregat.isin(agrs)]
    if entites is not None:
        x = x[x.entite.isin(entites)]
    g = x.groupby(['entite', 'agregat', 'annee'])[['montant', 'eleves_public']].sum().reset_index()
    pe = g.pivot_table(index=['entite', 'agregat'], columns='annee', values='montant').div(1e6)
    el = g.pivot_table(index=['entite', 'agregat'], columns='annee', values='eleves_public')
    per = (pe * 1e6 / el)
    per['moy_2022_2025'] = pe[YEARS].sum(axis=1) * 1e6 / el[YEARS].sum(axis=1)
    pe['total_2022_2025'] = pe[YEARS].sum(axis=1)
    return pe.round(2), per.round(0)


print('=== Dénominateurs (collégiens du public, année civile) ===')
print(pd.Series({k: v for k, v in den.items()}).unstack().round(0).to_string())
print('=== Rentrées (collégiens du public) ===')
print(rent.loc[IDF].to_string())
print('France hors COM :', rent_fr_all.to_dict())
for fonc in ['221']:
    pe, per = tab(fonc, AGR)
    print(f'=== Fonction {fonc} : M€ ===')
    print(pe.to_string())
    print(f'=== Fonction {fonc} : € par collégien du public ===')
    print(per.to_string())
pe, per = tab('221', [a for a in L.agregat.unique() if 'DGFiP' in a])
print(pe.to_string()); print(per.to_string())
pe, per = tab('toutes', [a for a in L.agregat.unique() if 'DGFiP' in a])
print(pe.to_string()); print(per.to_string())
for fonc in ['24', '20', '201', '22', '28', '2']:
    pe, per = tab(fonc, ["Dépenses d'équipement", 'Frais de personnel', 'Dépenses de fonctionnement', "Dépenses d'investissement hors remb"],
                  entites=[NOMS['93'], NOMS['75']])
    print(f'=== Fonction {fonc} (93 et Paris), M€ ===')
    print(pe.to_string())
