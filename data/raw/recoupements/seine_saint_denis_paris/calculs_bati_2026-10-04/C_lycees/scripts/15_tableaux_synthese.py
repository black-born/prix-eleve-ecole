# -*- coding: utf-8 -*-
"""Tableaux de synthèse (Markdown, format français) à partir des résultats des scripts 10 à 14.
Sortie : resultats/tableaux_synthese.txt
"""
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'


def f(x, d=0):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return '—'
    s = f'{x:,.{d}f}'
    return s.replace(',', ' ').replace('.', ',').replace('-', '−')


def pct(x, d=0):
    return f(x * 100, d) + ' %'


dc = pd.read_csv(W + 'resultats/dotation_consolidee_par_departement.csv', sep=';', dtype={'dep': str}).set_index('dep')
ev = pd.read_csv(W + 'resultats/dotation_consolidee_evolution_2016_2026_par_departement.csv', sep=';', dtype={'dep': str}).set_index('dep')
af = pd.read_csv(W + 'resultats/affectations_2021_2023_par_departement.csv', sep=';', dtype={'dep': str}).set_index('dep')
af = af.rename(index={'IDF (attribuable)': 'IDF'})
pp = pd.read_csv(W + 'resultats/ppi_historique_par_departement.csv', sep=';', dtype={'dep': str}).set_index('dep')
pp.loc['IDF'] = pp.sum(numeric_only=True)
pp.loc['IDF', 'AP_EUR_par_eleve_lycee_2015'] = pp.loc['IDF', 'AP_votees_MEUR'] * 1e6 / pp.loc['IDF', 'eleves_lycees_publics_2015']
pp.loc['IDF', 'AP_EUR_par_eleve_accueilli_2015'] = pp.loc['IDF', 'AP_votees_MEUR'] * 1e6 / (pp.loc['IDF', 'eleves_lycees_publics_2015'] + pp.loc['IDF', 'collegiens_CMR_2015'])
cols = ['75', '93', 'IDF']
lines = ['| Région Île-de-France, dépense par élève des lycées publics | Paris | Seine-Saint-Denis | Île-de-France |', '|---|---|---|---|']


def row(label, vals):
    lines.append('| ' + label + ' | ' + ' | '.join(vals) + ' |')


tot = dc['prebac_2025'] + dc['postbac_2025'] + dc['college_cmr_2025']
row('Élèves accueillis, rentrée 2025 : lycéens pré-bac / post-bac (BTS, CPGE) / collégiens des cités mixtes régionales',
    [f(dc.loc[c, 'prebac_2025']) + ' / ' + f(dc.loc[c, 'postbac_2025']) + ' / ' + f(dc.loc[c, 'college_cmr_2025']) for c in cols])
row('Part des élèves accueillis qui ne sont pas des lycéens pré-bac', [pct((dc.loc[c, 'postbac_2025'] + dc.loc[c, 'college_cmr_2025']) / tot[c], 1) for c in cols])
row('**Dotation de fonctionnement consolidée 2026** (DGFL, internat, contrôles et contrats obligatoires, énergie, EPI), M€', [f(dc.loc[c, 'dot2026_MEUR'], 1) for c in cols])
row('· par élève accueilli', [f(dc.loc[c, 'EUR_par_eleve_accueilli']) + ' €' for c in cols])
row('· par lycéen pré-bac et post-bac (hors collégiens des cités mixtes)', [f(dc.loc[c, 'EUR_par_lyceen_postbac_inclus']) + ' €' for c in cols])
row('· par lycéen pré-bac (dénominateur de B)', [f(dc.loc[c, 'EUR_par_lyceen_prebac']) + ' €' for c in cols])
row('Même dotation en 2016 (DGFL, énergie, contrôles), par élève accueilli (effectifs 2016-2017), établissements présents en 2016 et 2026', [f(ev.loc[c, 'EUR_par_eleve_2016 (effectifs 2016-2017, + collégiens CMR)']) + ' €' for c in cols])
row('Évolution 2016-2026 de cette dotation (mêmes établissements)', ['+' + f(ev.loc[c, 'evolution_pct']) + ' %' for c in cols])
row('Subventions votées 2021-2023 : DGF et maintenance, contrôles, entretien (fonctionnement), par élève accueilli et par an', [f(af.loc[c, 'EUR_par_eleve_par_an_DGF_entretien']) + ' €' for c in cols])
row('Subventions votées 2021-2023 : travaux de maintenance et équipements pédagogiques (investissement), par élève accueilli et par an', [f(af.loc[c, 'EUR_par_eleve_par_an_subv_invest']) + ' €' for c in cols])
row('**Opérations directes votées 2021-2023, part attribuable à un département** (AP/AE affectées), M€', [f(af.loc[c, 'operations_directes_attribuees_MEUR'], 1) for c in cols])
row('· par élève accueilli et par an', [f(af.loc[c, 'EUR_par_eleve_par_an_operations_directes']) + ' €' for c in cols])
row('· par lycéen pré-bac et par an', [f(af.loc[c, 'EUR_par_lyceen_prebac_par_an_operations_directes']) + ' €' for c in cols])
row('**PPI 1995-2018 : autorisations de programme votées** (opérations individualisées, surtout PPI 2001-2006), M€ courants', [f(pp.loc[c, 'AP_votees_MEUR'], 1) for c in cols])
row('· par élève des lycées publics en 2015 (pré-bac et post-bac)', [f(pp.loc[c, 'AP_EUR_par_eleve_lycee_2015']) + ' €' for c in cols])
row('· par élève accueilli en 2015 (avec les collégiens des cités mixtes)', [f(pp.loc[c, 'AP_EUR_par_eleve_accueilli_2015']) + ' €' for c in cols])
row('Repère : ligne « région » de B (2025), par lycéen pré-bac', ['2 566 €', '2 583 €', '2 581 €'])
t1 = '\n'.join(lines)

# ---- tableau 2 : bâti et programmes
lo = pd.read_csv(W + 'resultats/listes_officielles_par_departement.csv', sep=';', dtype={'dep': str}).set_index('dep')
lo.loc['IDF'] = lo.sum(numeric_only=True)
yc = pd.read_csv(W + 'resultats/annee_construction_par_departement.csv', sep=';', dtype={'dep': str}).set_index('dep')
ta = pd.read_csv(W + 'resultats/taille_lycees_publics_2025.csv', sep=';', dtype={'dep': str})
lines = ['| Bâti des lycées publics : indicateurs officiels | Paris | Seine-Saint-Denis | Île-de-France |', '|---|---|---|---|']
row('Lycées publics (Région, rentrée 2026)', [f(lo.loc[c, 'lycees_publics_DP2026']) for c in cols])
row('Lycées « très vétustes » en 2016 (audit régional)', [f(lo.loc[c, 'tres_vetustes_2016']) for c in cols])
row('Plan d\'urgence 2017 : rénovations globales / opérations ciblées / « toit-façade » / internats (opérations listées)',
    [' / '.join(f(lo.loc[c, k]) for k in ['PPI2017_rénovation globale', 'PPI2017_opérations ciblées', 'PPI2017_toit-façade', 'PPI2017_internats']) for c in cols])
row('Plan d\'urgence 2017 : places nouvelles programmées', [f(lo.loc[c, 'PPI2017_places_nouvelles_nb']) for c in cols])
row('Grandes opérations lancées ou livrées de 2016 à fin 2020 (bilan d\'étape 2021)', [f(lo.loc[c, 'grandes_operations_2016_2021']) for c in cols])
row('Lycées ayant eu plus de 1 M€ de travaux depuis 2016 (Région, 2026)',
    [f(lo.loc[c, 'lycees_plus_1MEUR_travaux_depuis_2016_DP2026']) + ' (' + pct(lo.loc[c, 'lycees_plus_1MEUR_travaux_depuis_2016_DP2026'] / lo.loc[c, 'lycees_publics_DP2026']) + ')' for c in cols])
row('Année de construction médiane (open data Région ; renseignée / lycées)', [str(int(yc.loc[c, 'mediane'])) + ' (' + f(yc.loc[c, 'annee_renseignee']) + ' / ' + f(yc.loc[c, 'lycees_publics']) + ')' for c in cols])
row('Part construite avant 1900 / avant 1970 / depuis 2000', [pct(yc.loc[c, 'part_avant_1900']) + ' / ' + pct(yc.loc[c, 'part_avant_1970']) + ' / ' + pct(yc.loc[c, 'part_2000_et_apres']) for c in cols])
for typ, lab in [('lycées (LEGT, LPO)', 'Taille moyenne 2025, lycées généraux, technologiques et polyvalents : élèves pré-bac / pré-bac et post-bac'),
                 ('lycées professionnels', 'Taille moyenne 2025, lycées professionnels : élèves pré-bac')]:
    v = []
    for c in cols:
        r = ta[(ta['dep'] == c) & (ta['type'] == typ)].iloc[0]
        v.append(f(r['moy_prebac']) + (' / ' + f(r['moy_prebac_postbac']) if 'LEGT' in typ else '') + ' (' + f(r['n']) + ' lycées)')
    row(lab, v)
t2 = '\n'.join(lines)

# ---- tableau 3 : effectifs
e = pd.read_csv(W + 'resultats/effectifs_lycees_publics_2015_2025.csv', sep=';', header=[0, 1], index_col=0)
A = e['tous_eleves_lycees_publics_prebac_postbac']
B = e['lyceens_prebac_GT_pro']
lines = ['| Élèves des lycées publics | Paris | Seine-Saint-Denis | Île-de-France |', '|---|---|---|---|']
for y in [2015, 2017, 2019]:
    row(f'Tous élèves (pré-bac et post-bac), rentrée {y} — série 1', [f(A.loc[y, c]) for c in cols])
row('Évolution 2015-2019 (série 1)', [('+' if A.loc[2019, c] >= A.loc[2015, c] else '') + f((A.loc[2019, c] / A.loc[2015, c] - 1) * 100, 1) + ' %' for c in cols])
for y in [2020, 2025]:
    row(f'Tous élèves (pré-bac et post-bac), rentrée {y} — série 2', [f(A.loc[y, c]) for c in cols])
row('Évolution 2020-2025 (série 2)', [('+' if A.loc[2025, c] >= A.loc[2020, c] else '') + f((A.loc[2025, c] / A.loc[2020, c] - 1) * 100, 1) + ' %' for c in cols])
for y in [2019, 2022, 2025]:
    row(f'Lycéens pré-bac (voies GT et pro), rentrée {y}', [f(B.loc[y, c]) for c in cols])
row('Évolution 2019-2025 (pré-bac)', [('+' if B.loc[2025, c] >= B.loc[2019, c] else '') + f((B.loc[2025, c] / B.loc[2019, c] - 1) * 100, 1) + ' %' for c in cols])
t3 = '\n'.join(lines)

out = '# Tableaux de synthèse (tâche C)\n\n## T1\n\n' + t1 + '\n\n## T2\n\n' + t2 + '\n\n## T3\n\n' + t3 + '\n'
open(W + 'resultats/tableaux_synthese.txt', 'w', encoding='utf-8').write(out)
print(out)
