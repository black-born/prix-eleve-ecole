"""Tableaux finaux de la tâche B (collèges) à partir des sorties des scripts 02 à 04.

T1 : Seine-Saint-Denis et Paris, fonction 221, postes détaillés (DGFiP), moyenne 2022-2025, € par collégien du public.
T2 : séries 2012-2025, investissement « bâti » : équipement (221), subventions d'équipement (221),
     remboursement en capital des marchés de partenariat (1675), cités scolaires (24) ; M€ et € par collégien du public.
T3 : dette des marchés de partenariat (PPP) du Département de la Seine-Saint-Denis, 2014-2025 (compte 1675).
T4 : cumuls 2012-2025 et 2016-2025.
Sorties : ../sorties/05_T1_postes_93_Paris_2022_2025.csv ; 05_T2_series_bati.csv ; 05_T3_dette_PPP_93.csv ; 05_T4_cumuls.csv
"""
import os
import sys
from importlib import import_module

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 40)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
m02 = import_module('02_comptes_221_93_Paris')
OUT = os.path.join(HERE, '..', 'sorties')

den = pd.read_csv(os.path.join(OUT, '03_denominateurs_collegiens_public_par_rentree.csv'), sep=';', encoding='utf-8-sig',
                  dtype={0: str}).set_index('dep')
den.columns = [int(c) for c in den.columns]


def civ(dep, y):
    if (y - 1) not in den.columns:
        return np.nan
    return 2 / 3 * den.loc[dep, y - 1] + 1 / 3 * den.loc[dep, y]


# ------------------------------------------------------------------ T1
rows = []
for y in [2022, 2023, 2024, 2025]:
    d = m02.prepare(y, 'idf')
    d = d[d.nature.str.startswith(('F_', 'I_'))]
    for ent, mask, dep in [('Seine-Saint-Denis', (d.categ == 'DEPT') & (d.ndept == '093'), '093'),
                           ('Paris', d.categ == 'PARIS', '075')]:
        x = d[mask & (d.f.str.startswith('221') | d.compte.str.startswith('1675'))]
        if ent == 'Paris':   # 1675 de Paris : chapitre 923, objet non documenté -> exclu de la fonction 221
            x = x[~x.compte.str.startswith('1675')]
        g = x.groupby('poste').montant.sum()
        for p, v in g.items():
            rows.append({'entite': ent, 'annee': y, 'poste': p, 'montant': v, 'eleves': civ(dep, y)})
T1 = pd.DataFrame(rows)
t1 = T1.groupby(['entite', 'poste'])[['montant']].sum()
el = T1.drop_duplicates(['entite', 'annee']).groupby('entite').eleves.sum()
t1['moy_annuelle_MEUR'] = t1.montant / 4 / 1e6
t1['euros_par_collegien_public'] = [m / el[e] for (e, p), m in zip(t1.index, t1.montant)]
t1 = t1.drop(columns='montant').unstack('entite')
t1.to_csv(os.path.join(OUT, '05_T1_postes_93_Paris_2022_2025.csv'), sep=';', encoding='utf-8-sig')
print('=== T1 : fonction 221, postes, moyenne 2022-2025 ===')
print(t1.round(1).to_string())
print('élèves (somme 4 ans) :', el.to_dict())

# ------------------------------------------------------------------ T2
S = pd.read_csv(os.path.join(OUT, '03_series_221_par_entite_annee_poste.csv'), sep=';', encoding='utf-8-sig')
codes = {'Seine-Saint-Denis': '093', 'Paris': '075', 'France (départements, Paris, ML, CTU)': 'FRA'}
rows = []
for en, dep in codes.items():
    s = S[S.entite == en]
    for y in range(2012, 2026):
        sy = s[s.annee == y]
        r = {'entite': en, 'annee': y,
             'equipement_221': sy[(sy.groupe == '221 Collèges') & (sy.nature == 'I_equipement')].montant.sum(),
             'dont_235_part_invest_PPP': np.nan,
             'subventions_equipement_221': sy[(sy.groupe == '221 Collèges') & (sy.nature == 'I_subventions_equipement_versees')].montant.sum(),
             'PPP_capital_1675_221': sy[(sy.groupe == '221 Collèges') & (sy.nature == 'I_PPP_remboursement_capital_1675')].montant.sum(),
             'equipement_24_cites_scolaires': sy[(sy.groupe == '24 Cités scolaires') & (sy.nature.isin(['I_equipement', 'I_subventions_equipement_versees']))].montant.sum(),
             'entretien_energie_221': sy[(sy.groupe == '221 Collèges') & (sy.poste.str.startswith(('F2 ', 'F3 ')))].montant.sum(),
             'eleves_public_annee_civile': civ(dep, y) if dep != 'FRA' else civ('FRA', y)}
        rows.append(r)
T2 = pd.DataFrame(rows)
# 235 (part investissement PPP, Seine-Saint-Denis) : depuis 02b
p = pd.read_csv(os.path.join(OUT, '02b_93_comptes_PPP_constructions_2012_2025.csv'), sep=';', encoding='utf-8-sig', dtype={'compte': str})
p235 = p[p.compte == '235'].set_index('annee').deb_reel
T2.loc[T2.entite == 'Seine-Saint-Denis', 'dont_235_part_invest_PPP'] = T2[T2.entite == 'Seine-Saint-Denis'].annee.map(p235).fillna(0.0).values * 1e6
T2['invest_bati_221_avec_PPP'] = T2.equipement_221 + T2.subventions_equipement_221 + T2.PPP_capital_1675_221
T2['invest_bati_221_24_avec_PPP'] = T2.invest_bati_221_avec_PPP + T2.equipement_24_cites_scolaires
for c in ['equipement_221', 'subventions_equipement_221', 'PPP_capital_1675_221', 'equipement_24_cites_scolaires',
          'invest_bati_221_avec_PPP', 'invest_bati_221_24_avec_PPP', 'entretien_energie_221']:
    T2[c + '_par_eleve'] = T2[c] / T2.eleves_public_annee_civile
T2.to_csv(os.path.join(OUT, '05_T2_series_bati.csv'), sep=';', index=False, encoding='utf-8-sig')
show = ['equipement_221', 'dont_235_part_invest_PPP', 'subventions_equipement_221', 'PPP_capital_1675_221', 'equipement_24_cites_scolaires',
        'invest_bati_221_24_avec_PPP', 'entretien_energie_221']
for en in codes:
    print('=== T2', en, 'M€ ===')
    x = T2[T2.entite == en].set_index('annee')
    print(x[show].div(1e6).round(2).join(x.eleves_public_annee_civile.round(0)).to_string())
    print(x[[c + '_par_eleve' for c in ['equipement_221', 'subventions_equipement_221', 'PPP_capital_1675_221', 'equipement_24_cites_scolaires',
                                        'invest_bati_221_avec_PPP', 'invest_bati_221_24_avec_PPP', 'entretien_energie_221']]].round(0).to_string())

# ------------------------------------------------------------------ T3 dette PPP 93
q = p[p.compte == '1675'].set_index('annee')[['becre', 'onbcre', 'deb_reel']]
q.columns = ['encours_au_1er_janvier_MEUR', 'dette_reconnue_a_la_livraison_MEUR (onbcre)', 'remboursement_capital_MEUR']
q['encours_au_31_decembre_MEUR'] = q.iloc[:, 0] + q.iloc[:, 1] - q.iloc[:, 2]
q.to_csv(os.path.join(OUT, '05_T3_dette_PPP_93.csv'), sep=';', encoding='utf-8-sig')
print('=== T3 dette PPP 93 (M€) ===')
print(q.round(2).to_string())
print('Totaux : dette reconnue', round(q.iloc[:, 1].sum(), 2), '; remboursée 2014-2025', round(q.iloc[:, 2].sum(), 2),
      '; 235 payé 2012-2019', round(p235.sum(), 2))
i66 = p[p.compte == '6618'].set_index('annee').deb_reel
print('Intérêts 6618 (fonction 221) 2014-2025 :', round(i66.sum(), 2), i66.round(2).to_dict())

# ------------------------------------------------------------------ T4 cumuls
rows = []
for en in codes:
    x = T2[T2.entite == en]
    for (a, b) in [(2012, 2025), (2016, 2025), (2022, 2025)]:
        xx = x[(x.annee >= a) & (x.annee <= b)]
        r = {'entite': en, 'periode': f'{a}-{b}'}
        for c in ['equipement_221', 'subventions_equipement_221', 'PPP_capital_1675_221', 'equipement_24_cites_scolaires', 'invest_bati_221_24_avec_PPP']:
            r[c + '_MEUR'] = xx[c].sum() / 1e6
        xe = xx[xx.eleves_public_annee_civile.notna()]
        if len(xe) == len(xx):
            for c in ['equipement_221', 'invest_bati_221_avec_PPP', 'invest_bati_221_24_avec_PPP']:
                r[c + '_par_eleve_an'] = xe[c].sum() / xe.eleves_public_annee_civile.sum()
        rows.append(r)
T4 = pd.DataFrame(rows)
T4.to_csv(os.path.join(OUT, '05_T4_cumuls.csv'), sep=';', index=False, encoding='utf-8-sig')
print('=== T4 cumuls ===')
print(T4.round(1).to_string())
