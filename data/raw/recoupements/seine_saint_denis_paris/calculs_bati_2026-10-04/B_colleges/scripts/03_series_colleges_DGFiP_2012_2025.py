"""Séries 2012-2025 des dépenses des départements pour leurs collèges (DGFiP, balances nature-fonction),
Seine-Saint-Denis, Paris, autres départements d'Île-de-France et France entière ; montants par collégien du public.

Entrées (dossier ../sources) :
  dgfip/DGFiP_<annee>_IDF_departements_Paris_fonction2_dette16_par_compte_API.csv  (script 01)
  dgfip/DGFiP_<annee>_national_DEPT_PARIS_ML_CTU_REG_fonction2_par_compte_API.csv  (script 01)
  DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv (rentrées 2019-2025, élèves de niveau collège)
  DEPP_fr-en-effectifs-second-degre_obsolete_par_dep_type_secteur_API.csv (rentrées 2015-2019, élèves des collèges)
Méthode :
  - opérations réelles (obnetdeb - oobdeb ; obnetcre - oobcre) ; natures et postes : script 02 (définitions OFGL M57) ;
  - périmètre « collèges » : fonction 221 (et variantes : + 24 cités scolaires, + 20/22/28/2 non ventilés pour les départements) ;
  - Paris : Département de Paris (DEP PARIS, categ DEPT 075) jusqu'en 2018, Ville de Paris (categ PARIS) depuis 2019 ;
  - France : départements + Paris + Métropole de Lyon + CTU (Corse, Guyane, Martinique), fonction 221 ;
  - dénominateur de l'année civile N : 2/3 x élèves du public à la rentrée N-1 + 1/3 x rentrée N (convention DEPP) ;
    rentrées 2019-2025 : jeu « fr-en-college-effectifs-niveau-sexe-lv » (élèves de niveau collège, public) ;
    rentrées 2015-2018 : jeu « fr-en-effectifs-second-degre » (élèves des établissements de type COLLEGE, public),
    raccordé à la rentrée 2019 par le rapport des deux jeux à la rentrée 2019 (coefficient par département).
Sorties (../sorties) : 03_series_221_par_entite_annee_poste.csv ; 03_series_221_par_eleve.csv ; 03_denominateurs.csv
"""
import os
import sys
from importlib import import_module

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 40)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
m02 = import_module('02_comptes_221_93_Paris')
SRC = os.path.join(HERE, '..', 'sources')
OUT = os.path.join(HERE, '..', 'sorties')
YEARS = list(range(2012, 2026))
IDF = {'075': 'Paris', '077': 'Seine-et-Marne', '078': 'Yvelines', '091': 'Essonne', '092': 'Hauts-de-Seine',
       '093': 'Seine-Saint-Denis', '094': 'Val-de-Marne', '095': "Val-d'Oise"}


def groupe_fonction(f):
    if f.startswith('221'):
        return '221 Collèges'
    if f.startswith(('222', '223', '224')):
        return '222-224 Lycées'
    if f.startswith('24'):
        return '24 Cités scolaires'
    if f.startswith('20'):
        return '20 Services communs'
    if f.startswith('21'):
        return '21 Premier degré'
    if f.startswith('22'):
        return '22 Second degré non ventilé'
    if f.startswith('28'):
        return '28 Services annexes'
    if f.startswith(('23', '25', '26', '27')):
        return '23-27 Hors scolaire'
    if f.startswith('29'):
        return '29 Sécurité'
    if f == '2':
        return '2 Enseignement non ventilé'
    return 'autre (' + f + ')'


def sous_poste(r):
    """Postes « bâti » et autres, à partir du compte (et de la nature)."""
    return m02.poste(r)


rows = []
for y in YEARS:
    d = m02.prepare(y, 'idf')
    d = d[d.nature.str.startswith(('F_', 'I_'))].copy()
    d['entite'] = None
    d.loc[(d.categ == 'DEPT') & d.ndept.isin(IDF.keys()), 'entite'] = d.ndept.map(IDF)
    d.loc[d.categ == 'PARIS', 'entite'] = 'Paris'
    d = d[d.entite.notna()]
    d['groupe'] = d.f.map(groupe_fonction)
    # 1675 hors fonction 2 (ex. Paris, chapitre 923) : gardé à part, groupe « dette (hors fonction 2) »
    d.loc[d.compte.str.startswith('1675') & ~d.f.str.startswith('2'), 'groupe'] = 'dette 1675 (hors fonction 2)'
    g = d.groupby(['entite', 'groupe', 'nature', 'poste']).montant.sum().reset_index()
    g['annee'] = y
    rows.append(g)
    # national
    n = m02.prepare(y, 'nat')
    n = n[n.nature.str.startswith(('F_', 'I_')) & n.categ.isin(['DEPT', 'PARIS', 'ML', 'CTU'])].copy()
    n['groupe'] = n.f.map(groupe_fonction)
    n = n[n.groupe == '221 Collèges']
    gn = n.groupby(['groupe', 'nature', 'poste']).montant.sum().reset_index()
    gn['entite'] = 'France (départements, Paris, ML, CTU)'
    gn['annee'] = y
    rows.append(gn)
    # national : départements seuls (categ DEPT) et Paris
    gd = n.groupby(['categ', 'groupe', 'nature', 'poste']).montant.sum().reset_index()
    gd['entite'] = 'France catégorie ' + gd.categ
    gd = gd.drop(columns='categ')
    gd['annee'] = y
    rows.append(gd)

S = pd.concat(rows, ignore_index=True)
S.to_csv(os.path.join(OUT, '03_series_221_par_entite_annee_poste.csv'), sep=';', index=False, encoding='utf-8-sig')

# ------------------------------------------------------------------ dénominateurs
e = pd.read_csv(os.path.join(SRC, 'DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv'), sep=';', dtype={'code_dept': str})
e['r'] = e.rentree_scolaire.str[:4].astype(int)
e = e[e.secteur == 'PUBLIC']
e['dep'] = e.code_dept.str.zfill(3)
new = e.groupby(['dep', 'r']).eleves.sum().unstack('r')
o = pd.read_csv(os.path.join(SRC, 'DEPP_fr-en-effectifs-second-degre_obsolete_par_dep_type_secteur_API.csv'), sep=';', dtype=str)
o['eleves'] = o.eleves.astype(float)
o = o[(o.type_d_etablissement == 'COLLEGE') & (o.secteur_d_enseignement == 'Public')]
o['r'] = o.annee_scolaire.str[:4].astype(int)
o['dep'] = o.code_departement.str.zfill(3)
old = o.groupby(['dep', 'r']).eleves.sum().unstack('r')
coef = (new[2019] / old[2019]).rename('coef_raccord_2019')
old_adj = old[[2015, 2016, 2017, 2018]].mul(coef, axis=0)
den = pd.concat([old_adj, new], axis=1)
COM = ['975', '977', '978', '986', '987', '988']
fr = den[~den.index.isin(COM)].sum()
den.loc['FRA'] = fr
den.to_csv(os.path.join(OUT, '03_denominateurs_collegiens_public_par_rentree.csv'), sep=';', encoding='utf-8-sig')
coef.to_csv(os.path.join(OUT, '03_coef_raccord_2019.csv'), sep=';', encoding='utf-8-sig')


def denom_civil(dep, y):
    if (y - 1) not in den.columns or y not in den.columns:
        return np.nan
    return 2 / 3 * den.loc[dep, y - 1] + 1 / 3 * den.loc[dep, y]


codes = {v: k for k, v in IDF.items()}
codes['France (départements, Paris, ML, CTU)'] = 'FRA'
# ------------------------------------------------------------------ tableau par élève
S221 = S[S.groupe == '221 Collèges']
piv_n = S221.pivot_table(index=['entite', 'annee'], columns='nature', values='montant', aggfunc='sum').fillna(0)
piv_p = S221.pivot_table(index=['entite', 'annee'], columns='poste', values='montant', aggfunc='sum').fillna(0)
P = pd.concat([piv_n, piv_p], axis=1)
P['F_total_fonctionnement'] = P[[c for c in piv_n.columns if c.startswith('F_')]].sum(axis=1)
P['I_total_hors_PPP'] = P[[c for c in piv_n.columns if c.startswith('I_') and 'PPP' not in c]].sum(axis=1)
P['I_PPP'] = P['I_PPP_remboursement_capital_1675'] if 'I_PPP_remboursement_capital_1675' in P.columns else 0.0
P = P.reset_index()
P['eleves_public_annee_civile'] = [denom_civil(codes.get(en, None), y) if codes.get(en) else np.nan for en, y in zip(P.entite, P.annee)]
P.to_csv(os.path.join(OUT, '03_series_221_montants.csv'), sep=';', index=False, encoding='utf-8-sig')
num = [c for c in P.columns if c not in ('entite', 'annee', 'eleves_public_annee_civile')]
Q = P.copy()
for c in num:
    Q[c] = Q[c] / Q['eleves_public_annee_civile']
Q.to_csv(os.path.join(OUT, '03_series_221_par_eleve.csv'), sep=';', index=False, encoding='utf-8-sig')

# ------------------------------------------------------------------ affichage
show = ['F_personnel', 'F_achats_charges_externes', 'F_interventions', 'F_charges_financieres', 'F_autres', 'F_total_fonctionnement',
        'I_equipement', 'I_subventions_equipement_versees', 'I_autres', 'I_total_hors_PPP', 'I_PPP']
print('=== Fonction 221, M€ ===')
for en in ['Seine-Saint-Denis', 'Paris', 'France (départements, Paris, ML, CTU)']:
    print('---', en)
    print(P[P.entite == en].set_index('annee')[show + ['eleves_public_annee_civile']].div(
        [1e6] * len(show) + [1]).round(2).to_string())
print('=== Fonction 221, € par collégien du public (année civile) ===')
for en in ['Seine-Saint-Denis', 'Paris', 'France (départements, Paris, ML, CTU)'] + [v for v in IDF.values() if v not in ('Paris', 'Seine-Saint-Denis')]:
    print('---', en)
    print(Q[(Q.entite == en) & (Q.annee >= 2016)].set_index('annee')[show].round(0).to_string())
# autres groupes de fonctions (93 et Paris)
print('=== Autres fonctions (M€), 93 et Paris ===')
G = S[S.entite.isin(['Seine-Saint-Denis', 'Paris'])].pivot_table(index=['entite', 'groupe', 'annee'], columns='nature', values='montant', aggfunc='sum').fillna(0).div(1e6).round(2)
print(G.to_string())
print(den.loc[['075', '093', '092', '094', 'FRA']].round(0).to_string())
print(coef.loc[['075', '093']])
