"""Taille des collèges publics et évolution des effectifs (Seine-Saint-Denis, Paris, France).
Sources (DEPP, data.education.gouv.fr, téléchargées dans ../sources) :
  - DEPP_effectifs_par_college_public_2019_2025_API.csv : « Effectifs d'élèves en collège »
    (fr-en-college-effectifs-niveau-sexe-lv), secteur public, rentrées 2019 et 2025, par établissement (UAI) ;
  - DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv : même jeu, agrégé (rentrées 2019-2025) ;
  - DEPP_fr-en-effectifs-second-degre_obsolete_par_dep_type_secteur_API.csv : jeu « obsolète » (rentrées 2015-2019),
    établissements de type COLLEGE, secteur public.
Champ : établissements accueillant des élèves de niveau collège (6e-3e), y c. SEGPA et ULIS.
Sorties : ../sorties/06_taille_colleges.csv ; ../sorties/06_evolution_effectifs.csv
"""
import os
import sys

import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'sources')
OUT = os.path.join(HERE, '..', 'sorties')
COM = ['975', '977', '978', '986', '987', '988']

d = pd.read_csv(os.path.join(SRC, 'DEPP_effectifs_par_college_public_2019_2025_API.csv'), sep=';',
                dtype={'code_dept': str, 'numero_college': str, 'rentree_scolaire': str})
d['r'] = d.rentree_scolaire.astype(str).str[:4].astype(int)
rows = []
for r in [2019, 2025]:
    x = d[d.r == r]
    for nom, sel in [('Seine-Saint-Denis', x.code_dept == '93'), ('Paris', x.code_dept == '75'),
                     ('France (hors COM)', ~x.code_dept.isin(COM))]:
        y = x[sel]
        n = len(y)
        e = y.nombre_eleves_total.sum()
        rows.append({'entite': nom, 'rentree': r, 'etablissements': n, 'eleves': e, 'eleves_par_etablissement': e / n,
                     'mediane': y.nombre_eleves_total.median(),
                     'nb_etab_700_plus': int((y.nombre_eleves_total >= 700).sum()),
                     'part_eleves_etab_700_plus': y[y.nombre_eleves_total >= 700].nombre_eleves_total.sum() / e,
                     'nb_etab_moins_400': int((y.nombre_eleves_total < 400).sum()),
                     'part_eleves_etab_moins_400': y[y.nombre_eleves_total < 400].nombre_eleves_total.sum() / e,
                     'max': y.nombre_eleves_total.max()})
T = pd.DataFrame(rows)
T.to_csv(os.path.join(OUT, '06_taille_colleges.csv'), sep=';', index=False, encoding='utf-8-sig')
print(T.round(3).to_string())

# Évolution des effectifs du public : rentrées 2015-2025 (raccord 2019)
e = pd.read_csv(os.path.join(SRC, 'DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv'), sep=';', dtype={'code_dept': str})
e['r'] = e.rentree_scolaire.str[:4].astype(int)
e = e[e.secteur == 'PUBLIC']
new = e.groupby(['code_dept', 'r']).eleves.sum().unstack('r')
o = pd.read_csv(os.path.join(SRC, 'DEPP_fr-en-effectifs-second-degre_obsolete_par_dep_type_secteur_API.csv'), sep=';', dtype=str)
o['eleves'] = o.eleves.astype(float)
o = o[(o.type_d_etablissement == 'COLLEGE') & (o.secteur_d_enseignement == 'Public')]
o['r'] = o.annee_scolaire.str[:4].astype(int)
o['code_dept'] = o.code_departement.str.lstrip('0').str.zfill(2)
o.loc[o.code_departement.str.len() == 3, 'code_dept'] = o.code_departement.str[1:]
old = o.groupby(['code_dept', 'r']).eleves.sum().unstack('r')
res = []
for nom, codes in [('Seine-Saint-Denis', ['93']), ('Paris', ['75']), ('France (hors COM)', [c for c in new.index if c not in COM])]:
    nw = new.loc[[c for c in codes if c in new.index]].sum()
    od = old.loc[[c for c in codes if c in old.index]].sum()
    r = {'entite': nom}
    for y in [2015, 2016, 2017, 2018]:
        r[f'R{y} (jeu obsolète, type COLLEGE)'] = od[y]
    r['R2019 (jeu obsolète)'] = od[2019]
    for y in range(2019, 2026):
        r[f'R{y}'] = nw[y]
    r['evol_2019_2025'] = nw[2025] / nw[2019] - 1
    r['evol_2015_2019_jeu_obsolete'] = od[2019] / od[2015] - 1
    r['evol_2015_2025_raccordee'] = (1 + r['evol_2015_2019_jeu_obsolete']) * (1 + r['evol_2019_2025']) - 1
    res.append(r)
R = pd.DataFrame(res)
R.to_csv(os.path.join(OUT, '06_evolution_effectifs.csv'), sep=';', index=False, encoding='utf-8-sig')
print(R.T.to_string())
