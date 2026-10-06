# -*- coding: utf-8 -*-
"""
Tâche A - compléments (2026-10-04) : sensibilités et indicateurs de contexte, à partir des sorties de 03_calculs.py
et des fichiers bruts DGFiP / DEPP du dossier brut/.
  1. Fonctionnement « bâti » restreint aux communes qui imputent au moins 10 % de leur énergie aux écoles.
  2. Subventions d'investissement reçues (comptes 13) dans les fonctions « écoles », par origine.
  3. Dispersion communale dans le 93 (moyenne 2023-2025 et 2021-2025).
  4. Communes du 93 qui imputent moins de 10 % de leur personnel aux écoles (2025).
  5. Rapport 93 / Paris par année.
  6. Effectifs et classes des écoles publiques, 2017-2025 (DEPP), Paris et 93.
"""
import os
import sys
import glob
import io
import requests
import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 60)
HERE = os.path.dirname(os.path.abspath(__file__))
BRUT = os.path.join(HERE, 'brut')
OUT = os.path.join(HERE, 'sorties')
sys.path.insert(0, HERE)
import importlib.util
spec = importlib.util.spec_from_file_location('calc', os.path.join(HERE, '03_calculs.py'))
calc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calc)
YEARS = calc.YEARS
DEPTS = calc.DEPTS


def wcsv(df, name):
    df.to_csv(os.path.join(OUT, name), sep=';', index=False, encoding='utf-8-sig')


w = pd.read_csv(os.path.join(OUT, 'A2_IDF_communes_annee_categories_euros.csv'), sep=';', encoding='utf-8-sig',
                dtype={'code': str, 'dep': str})
fl = pd.read_csv(os.path.join(OUT, 'A6_IDF_parts_imputees_aux_ecoles_personnel_energie_entretien.csv'), sep=';',
                 encoding='utf-8-sig', dtype={'code': str})
w = w.merge(fl[['code', 'annee', 'part_energie_ecoles', 'part_personnel_ecoles', 'part_equipement_ecoles']],
            on=['code', 'annee'], how='left')
w = w[w.eleves_rentree_N_1 > 0]
w['dep'] = w.code.str[:2]

# ---------------------------------------------------------------------------------------------------------
# 1. Sensibilité : communes qui imputent l'énergie aux écoles
# ---------------------------------------------------------------------------------------------------------
res = []
toujours = w.groupby('code').part_energie_ecoles.min()
toujours = set(toujours[toujours >= 0.10].index)
for dep, lib in DEPTS.items():
    for a in YEARS:
        s = w[(w.dep == dep) & (w.annee == a)]
        for nom, sub in (('toutes les communes', s),
                         ('communes imputant >= 10 % de leur énergie aux écoles cette année', s[s.part_energie_ecoles >= 0.10]),
                         ('communes imputant >= 10 % de leur énergie aux écoles chaque année 2021-2025', s[s.code.isin(toujours)])):
            el = sub.eleves_rentree_N_1.sum()
            res.append({'territoire': lib, 'annee': a, 'sous_ensemble': nom, 'nb_communes': len(sub), 'eleves': el,
                        'part_eleves_du_territoire': el / s.eleves_rentree_N_1.sum(),
                        'F_bati_€_par_eleve': sub.F_bati.sum() / el, 'F_energie_€_par_eleve': sub.F_energie_fluides.sum() / el,
                        'F_entretien_maintenance_€_par_eleve': sub.F_entretien_maintenance.sum() / el,
                        'F_nettoyage_€_par_eleve': sub.F_nettoyage.sum() / el,
                        'F_personnel_€_par_eleve': sub.F_personnel.sum() / el,
                        'I_total_€_par_eleve': sub.I_total.sum() / el, 'I_bati_€_par_eleve': sub.I_bati.sum() / el})
res = pd.DataFrame(res)
wcsv(res, 'A8_sensibilite_imputation_energie.csv')
r3 = res[res.annee.isin([2023, 2024, 2025])].copy()
for c in ['F_bati', 'F_energie', 'F_entretien_maintenance', 'F_nettoyage', 'F_personnel', 'I_total', 'I_bati']:
    r3[c + '_M'] = r3[c + '_€_par_eleve'] * r3.eleves
agg = r3.groupby(['territoire', 'sous_ensemble']).agg(eleves=('eleves', 'sum'), nb=('nb_communes', 'mean'),
                                                     part=('part_eleves_du_territoire', 'mean'),
                                                     **{c: (c + '_M', 'sum') for c in ['F_bati', 'F_energie', 'F_entretien_maintenance',
                                                                                       'F_nettoyage', 'F_personnel', 'I_total', 'I_bati']})
for c in ['F_bati', 'F_energie', 'F_entretien_maintenance', 'F_nettoyage', 'F_personnel', 'I_total', 'I_bati']:
    agg[c] = agg[c] / agg.eleves
print('1. Moyenne 2023-2025, € par élève, selon l\'imputation de l\'énergie :')
print(agg.round(2).to_string())
wcsv(agg.reset_index(), 'A8b_sensibilite_imputation_energie_moy2023-2025.csv')

# ---------------------------------------------------------------------------------------------------------
# 2. Subventions d'investissement reçues par origine (fonctions « écoles »)
# ---------------------------------------------------------------------------------------------------------
q = calc.idf()
e = q[(q.perim == 'ecoles') & (q.cat == 'R_subventions_investissement_recues')].copy()
lab = pd.read_csv(os.path.join(calc.RAWC, 'OFGL_nomenclature_M57_2025_libelles_comptes.csv'), sep=';', dtype=str,
                  encoding='utf-8-sig').drop_duplicates('numero_compte').set_index('numero_compte').libelle_compte


def origine(c):
    c = str(c)
    if c.startswith(('1311', '1321', '1331', '1341', '1342', '1345', '1346', '1347', '1348')):
        return 'État, établissements publics nationaux (dont ANRU) et dotations de l\'État (1311, 1321, 1331, 134x : DETR, DSIL, etc.)'
    if c.startswith(('1312', '1322', '1332')):
        return 'Région (1312, 1322, 1332)'
    if c.startswith(('1313', '1323', '1333')):
        return 'Département (1313, 1323, 1333)'
    if c.startswith(('1314', '1324', '1334')):
        return 'Communes (1314, 1324, 1334)'
    if c.startswith(('1315', '1325', '1335')):
        return 'Groupements de collectivités : EPT, Métropole, etc. (1315, 1325, 1335)'
    if c.startswith(('1317', '1327', '1337')):
        return 'Union européenne (1317, 1327, 1337)'
    if c.startswith(('1316', '1326', '1336')):
        return 'Autres établissements publics locaux (1316, 1326)'
    return 'Autres (1318, 1328, 1338, 138x...)'


e['origine'] = e.compte.map(origine)
e['dep'] = e.code.str[:2]
sub = e.groupby(['dep', 'annee', 'origine']).montant.sum().div(1e6).round(2).reset_index()
wcsv(sub, 'A9_subventions_investissement_recues_ecoles_par_origine.csv')
print('2. Subventions d\'investissement reçues (M€) :')
print(sub.pivot_table(index=['dep', 'origine'], columns='annee', values='montant').round(1).to_string())
det = e.groupby(['dep', 'compte']).montant.sum().div(1e6).round(2)
det = det[det.abs() > 0.5].reset_index()
det['libelle'] = det.compte.map(lambda c: lab.get(c, ''))
print(det.to_string())

# ---------------------------------------------------------------------------------------------------------
# 3. Dispersion communale dans le 93
# ---------------------------------------------------------------------------------------------------------
d = pd.read_csv(os.path.join(OUT, 'A4b_93_dispersion_communale_2023-2025.csv'), sep=';', encoding='utf-8-sig',
                dtype={'code': str})
syn = pd.read_csv(os.path.join(OUT, 'A3_synthese_territoires_annees.csv'), sep=';', encoding='utf-8-sig')
v = syn[syn.variante == 'tous budgets ; rentrée N-1']


def moy(terr, c, ys):
    s = v[(v.territoire == terr) & v.annee.isin(ys)]
    return s[c + '_M€'].sum() * 1e6 / s.eleves.sum()


paris3 = moy('Paris', 'I_total', [2023, 2024, 2025])
fr3 = moy('France (communes à comptabilité fonctionnelle)', 'I_total', [2023, 2024, 2025])
paris3b = moy('Paris', 'I_bati', [2023, 2024, 2025])


def wquant(x, wts, qs):
    o = np.argsort(x)
    x, wts = np.asarray(x)[o], np.asarray(wts)[o]
    cw = np.cumsum(wts) / wts.sum()
    return [x[np.searchsorted(cw, qq)] for qq in qs]


stats = []
for col, lab_ in (('I_total_moy2023_2025', 'investissement 20/21/23, moyenne 2023-2025'),
                  ('I_bati_moy2023_2025', 'investissement « bâti », moyenne 2023-2025'),
                  ('I_total_moy2021_2025', 'investissement 20/21/23, moyenne 2021-2025'),
                  ('F_bati_moy2023_2025', 'fonctionnement « bâti », moyenne 2023-2025')):
    x = d[col].values
    wt = d.eleves_rentree2024.values
    p10, p25, p50, p75, p90 = wquant(x, wt, [0.10, 0.25, 0.50, 0.75, 0.90])
    stats.append({'indicateur': lab_, 'nb_communes': len(x), 'mediane_communale_non_ponderee': np.median(x),
                  'P10_pondere_eleves': p10, 'P25_pondere': p25, 'mediane_ponderee': p50, 'P75_pondere': p75,
                  'P90_pondere': p90, 'min': x.min(), 'max': x.max(),
                  'nb_communes_au_dessus_Paris_moy2023_2025': int((x > (paris3 if 'I_total' in col else paris3b)).sum()) if col.startswith('I_') and '2023' in col else None,
                  'part_eleves_au_dessus_Paris': wt[x > (paris3 if 'I_total' in col else paris3b)].sum() / wt.sum() if col.startswith('I_') and '2023' in col else None,
                  'nb_communes_au_dessus_France': int((x > fr3).sum()) if col == 'I_total_moy2023_2025' else None,
                  'part_eleves_au_dessus_France': wt[x > fr3].sum() / wt.sum() if col == 'I_total_moy2023_2025' else None})
stats = pd.DataFrame(stats)
print('3. Dispersion dans le 93 (Paris 2023-2025 : investissement', round(paris3), '€, bâti', round(paris3b), '€ ; France', round(fr3), '€)')
print(stats.round(2).to_string())
wcsv(stats, 'A10_93_statistiques_dispersion.csv')

# ---------------------------------------------------------------------------------------------------------
# 4. Personnel et énergie non imputés (2025)
# ---------------------------------------------------------------------------------------------------------
low = d[d.part_personnel_ecoles_2025 < 0.10]
print('4. Communes du 93 imputant < 10 % de leur personnel aux écoles (2025) :', len(low), 'communes,',
      int(low.eleves_rentree2024.sum()), 'élèves :', ', '.join(low.libelle))
lowe = d[d.part_energie_ecoles_2025 < 0.10]
print('   Communes du 93 imputant < 10 % de leur énergie aux écoles (2025) :', len(lowe), 'communes,',
      int(lowe.eleves_rentree2024.sum()), 'élèves :', ', '.join(lowe.libelle))

# ---------------------------------------------------------------------------------------------------------
# 5. Rapport 93 / Paris par année
# ---------------------------------------------------------------------------------------------------------
rows = []
for a in YEARS:
    s = v[v.annee == a].set_index('territoire')
    rows.append({'annee': a,
                 'I_total_93': s.loc['Seine-Saint-Denis', 'I_total_€_par_eleve'], 'I_total_Paris': s.loc['Paris', 'I_total_€_par_eleve'],
                 'rapport_I_total': s.loc['Seine-Saint-Denis', 'I_total_€_par_eleve'] / s.loc['Paris', 'I_total_€_par_eleve'],
                 'I_bati_93': s.loc['Seine-Saint-Denis', 'I_bati_€_par_eleve'], 'I_bati_Paris': s.loc['Paris', 'I_bati_€_par_eleve'],
                 'rapport_I_bati': s.loc['Seine-Saint-Denis', 'I_bati_€_par_eleve'] / s.loc['Paris', 'I_bati_€_par_eleve'],
                 'I_total_93_M€': s.loc['Seine-Saint-Denis', 'I_total_M€'], 'I_total_Paris_M€': s.loc['Paris', 'I_total_M€'],
                 'F_bati_93': s.loc['Seine-Saint-Denis', 'F_bati_€_par_eleve'], 'F_bati_Paris': s.loc['Paris', 'F_bati_€_par_eleve']})
rr = pd.DataFrame(rows)
print('5.'); print(rr.round(2).to_string())
wcsv(rr, 'A11_rapport_93_Paris_par_annee.csv')

# ---------------------------------------------------------------------------------------------------------
# 6. Effectifs et classes des écoles publiques (DEPP), rentrées 2017-2025, Paris et 93 (et France)
# ---------------------------------------------------------------------------------------------------------
URL = 'https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ecoles-effectifs-nb_classes/exports/csv'
path = os.path.join(BRUT, 'DEPP_effectifs_classes_par_departement_secteur_rentrees2015-2025_API.csv')
if not os.path.exists(path):
    p = {'select': 'rentree_scolaire,code_departement,secteur,count(*) as nb_ecoles,sum(nombre_total_classes) as classes,'
                   'sum(nombre_total_eleves) as eleves',
         'where': 'year(rentree_scolaire)>=2015', 'group_by': 'rentree_scolaire,code_departement,secteur', 'delimiter': ';'}
    r = requests.get(URL, params=p, timeout=600)
    r.raise_for_status()
    open(path, 'wb').write(r.content)
    with open(os.path.join(BRUT, '_urls_requetes.txt'), 'a', encoding='utf-8') as f:
        f.write(f'{os.path.basename(path)}\t{r.url}\n')
k = pd.read_csv(path, sep=';', dtype={'code_departement': str}, encoding='utf-8-sig')
k['rentree'] = k.rentree_scolaire.astype(str).str[:4].astype(int)
k = k[k.secteur.str.upper().str.startswith('PUBLIC')]
k['zone'] = np.where(k.code_departement == '75', 'Paris', np.where(k.code_departement == '93', 'Seine-Saint-Denis', 'Autres'))
kk = k.groupby(['zone', 'rentree'])[['nb_ecoles', 'classes', 'eleves']].sum()
fr = k.groupby('rentree')[['nb_ecoles', 'classes', 'eleves']].sum()
fr['zone'] = 'France'
kk = pd.concat([kk.reset_index(), fr.reset_index()])
kk['eleves_par_classe'] = kk.eleves / kk.classes
kk = kk[kk.zone != 'Autres']
print('6. Écoles publiques : écoles, classes, élèves (DEPP)')
print(kk.pivot_table(index='rentree', columns='zone', values=['nb_ecoles', 'classes', 'eleves', 'eleves_par_classe']).round(1).to_string())
wcsv(kk, 'A12_ecoles_publiques_classes_eleves_2015-2025.csv')

# évolution des élèves par commune du 93 (rentrée 2020 -> 2024) et investissement
pc = pd.read_csv(os.path.join(OUT, 'A0_effectifs_publics_par_commune_rentrees2020-2025.csv'), sep=';', encoding='utf-8-sig',
                 dtype={'code': str})
ev = pc[pc.code.str[:2] == '93'].pivot_table(index='code', columns='rentree', values='eleves')
ev['evol_2020_2024'] = ev[2024] / ev[2020] - 1
cl = d.set_index('code').join(ev[['evol_2020_2024']])
print('Corrélation (communes du 93) entre évolution des élèves 2020-2024 et investissement 2023-2025 par élève :',
      round(np.corrcoef(cl.evol_2020_2024, cl.I_total_moy2023_2025)[0, 1], 2))
print(cl[['libelle', 'eleves_rentree2024', 'evol_2020_2024', 'I_total_moy2023_2025']].sort_values('evol_2020_2024').round(3).to_string())
wcsv(cl.reset_index()[['code', 'libelle', 'eleves_rentree2024', 'evol_2020_2024', 'I_total_moy2023_2025', 'I_bati_moy2023_2025']],
     'A13_93_evolution_eleves_et_investissement.csv')
