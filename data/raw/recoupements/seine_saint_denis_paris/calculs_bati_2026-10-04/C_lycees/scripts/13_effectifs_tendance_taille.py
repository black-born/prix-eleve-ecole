# -*- coding: utf-8 -*-
"""Effectifs des lycées publics par département (Île-de-France), 2015-2025, et taille des lycées.
Sources (DEPP, data.education.gouv.fr, fichiers dans raw/) :
- fr-en-effectifs-second-degre (jeu « obsolète ») : élèves par établissement, années 2015-2016 à 2019-2020 ; le champ
  nombre_d_eleves comprend les élèves post-bac (STS, CPGE) : vérifié sur Henri-IV et Louis-le-Grand ;
- fr-en-mode-hebergement-eleves-etablissements-2d : élèves du second degré et du supérieur par UAI, rentrées 2020 à 2025 ;
- fr-en-lycee_gt-effectifs-niveau-sexe-lv et fr-en-lycee_pro-effectifs-niveau-sexe-lv : élèves pré-bac par lycée,
  rentrées 2019 à 2025.
Sorties : resultats/effectifs_lycees_publics_2015_2025.csv, resultats/taille_lycees_publics_2025.csv
"""
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 40)
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
DEPS = ['75', '77', '78', '91', '92', '93', '94', '95']

# --- A. tous élèves des lycées publics (pré-bac + post-bac), 2015-2019 (jeu obsolète) puis 2020-2025 (hébergement)
ob = pd.read_csv(W + 'raw/DEPP_fr-en-effectifs-second-degre_obsolete_IDF.csv', sep=';', dtype=str)
ob['n'] = pd.to_numeric(ob['nombre_d_eleves'], errors='coerce')
ob = ob[(ob['secteur_d_enseignement'] == 'Public') & ob['type_d_etablissement'].str.startswith('LYCEE')]
ob['dep'] = ob['code_departement'].str[-2:]
ob['rentree'] = ob['annee_scolaire'].str[:4].astype(int)
A1 = ob.pivot_table(index='rentree', columns='dep', values='n', aggfunc='sum')
h = pd.read_csv(W + 'raw/DEPP_fr-en-mode-hebergement-eleves-etablissements-2d_IDF_2020-2025.csv', sep=';', dtype={'uai': str, 'code_departement': str})
h['rentree'] = h['rentree'].astype(int)
h = h[(h['secteur'] == 'PUBLIC') & h['type_d_etablissement'].isin(['LYCEE', 'LP'])]
h['dep'] = h['code_departement'].str[-2:]
S2, SUP = 'nombre_d_eleves_dans_une_formation_du_second_degre', 'nombre_d_eleves_dans_une_formation_du_superieur'
h['n'] = h[S2] + h[SUP]
A2 = h.pivot_table(index='rentree', columns='dep', values='n', aggfunc='sum')
A = pd.concat([A1, A2])[DEPS]
A['IDF'] = A.sum(axis=1)
print('Tous élèves des lycées publics (pré-bac + post-bac) :')
print(A.round(0).to_string())
B2 = h.pivot_table(index='rentree', columns='dep', values=S2, aggfunc='sum')[DEPS]
print('Élèves du second degré des lycées publics (hébergement) :')
print(B2.round(0).to_string())

# --- B. lycéens pré-bac (GT + pro), 2019-2025
frames = []
for ds in ['fr-en-lycee_gt-effectifs-niveau-sexe-lv', 'fr-en-lycee_pro-effectifs-niveau-sexe-lv']:
    d = pd.read_csv(W + f'raw/DEPP_{ds}_IDF_toutes_rentrees.csv', sep=';', dtype=str)
    d['n'] = pd.to_numeric(d['nombre_d_eleves'], errors='coerce')
    dc = 'code_departement_pays' if 'code_departement_pays' in d.columns else 'code_departement'
    d['dep'] = d[dc].str[-2:]
    d['voie'] = 'GT' if 'gt' in ds else 'pro'
    frames.append(d[['rentree_scolaire', 'dep', 'secteur', 'numero_lycee', 'voie', 'n']])
L = pd.concat(frames)
L = L[L['secteur'] == 'PUBLIC']
L['rentree'] = L['rentree_scolaire'].astype(int)
B = L.pivot_table(index='rentree', columns='dep', values='n', aggfunc='sum')[DEPS]
B['IDF'] = B.sum(axis=1)
print('Lycéens pré-bac des lycées publics (voies GT + pro) :')
print(B.round(0).to_string())
out = pd.concat({'tous_eleves_lycees_publics_prebac_postbac': A, 'lyceens_prebac_GT_pro': B}, axis=1)
out.to_csv(W + 'resultats/effectifs_lycees_publics_2015_2025.csv', sep=';', encoding='utf-8-sig')
for col in ['75', '93', 'IDF']:
    print(col, 'évolution tous élèves 2015->2019 : %+.1f %% ; 2020->2025 : %+.1f %% ; pré-bac 2019->2025 : %+.1f %%' % (
        (A.loc[2019, col] / A.loc[2015, col] - 1) * 100, (A.loc[2025, col] / A.loc[2020, col] - 1) * 100, (B.loc[2025, col] / B.loc[2019, col] - 1) * 100))

# --- C. taille des lycées publics, rentrée 2025 (hébergement : second degré + post-bac, par UAI)
h25 = h[h['rentree'] == 2025]
rows = []
for dep, g in list(h25.groupby('dep')) + [('IDF', h25)]:
    for typ, gg in [('lycées (LEGT, LPO)', g[g['type_d_etablissement'] == 'LYCEE']), ('lycées professionnels', g[g['type_d_etablissement'] == 'LP']), ('ensemble', g)]:
        rows.append({'dep': dep, 'type': typ, 'n': len(gg), 'moy_prebac': gg[S2].mean(), 'moy_prebac_postbac': gg['n'].mean(),
                     'mediane_prebac_postbac': gg['n'].median(), 'part_moins_500': (gg['n'] < 500).mean()})
T = pd.DataFrame(rows)
print(T[T['dep'].isin(['75', '93', 'IDF'])].round(1).to_string())
T.to_csv(W + 'resultats/taille_lycees_publics_2025.csv', sep=';', index=False, encoding='utf-8-sig')
