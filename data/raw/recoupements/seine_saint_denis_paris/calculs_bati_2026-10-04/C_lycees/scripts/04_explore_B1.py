# -*- coding: utf-8 -*-
"""Lecture de B1 (projet) : lycées publics d'Île-de-France, élèves rentrée 2024 et ligne région."""
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 40)
pd.set_option('display.max_rows', 400)

B1 = 'C:/Users/chret/Documents/EtatEcole/resultats/B1_depense_publique_par_etablissement_2025.csv'
b = pd.read_csv(B1, sep=';', encoding='utf-8-sig', dtype={'code_departement': str, 'uai': str})
print(b.shape)
idf = ['75', '77', '78', '91', '92', '93', '94', '95']
x = b[b['code_departement'].isin(idf) & (b['secteur'] == 'public')]
print(pd.crosstab(x['type'], x['code_departement']))
lyc_types = ['lycée général et technologique', 'lycée professionnel', 'lycée polyvalent', 'EREA / LEA', 'cité scolaire (collège + lycée)']
y = x[x['type'].isin(lyc_types)]
t = y.groupby(['code_departement', 'type']).agg(n=('uai', 'count'), eleves=('eleves', 'sum'), ct_lycees=('ct_lycees', 'sum'))
t['ct_par_eleve'] = t['ct_lycees'] / t['eleves']
t['taille_moy'] = t['eleves'] / t['n']
print(t)
t2 = y[y['type'].isin(lyc_types[:3])].groupby('code_departement').agg(n=('uai', 'count'), eleves=('eleves', 'sum'), ct_lycees=('ct_lycees', 'sum'))
t2['ct_par_eleve'] = t2['ct_lycees'] / t2['eleves']
print(t2)
print(t2.sum())
# cites scolaires : ct_lycees present ?
print(x[x['type'] == 'cité scolaire (collège + lycée)'][['uai', 'nom', 'eleves', 'ct_colleges', 'ct_lycees']].head(20))
