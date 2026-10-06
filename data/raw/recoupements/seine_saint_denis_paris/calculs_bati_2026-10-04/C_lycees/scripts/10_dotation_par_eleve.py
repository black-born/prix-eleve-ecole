# -*- coding: utf-8 -*-
"""Dotation de fonctionnement consolidée de la Région (CR 2025-030, annexe 1 au rapport) rapportée aux élèves, par département.

Entrées (dossier de travail) :
- resultats/dotation_consolidee_2016_2026_par_UAI.csv (script 09) ;
- raw/DEPP_fr-en-mode-hebergement-eleves-etablissements-2d_IDF_2020-2025.csv : élèves du second degré et du supérieur
  (post-bac) par UAI, rentrées 2020 à 2025 (DEPP, data.education.gouv.fr) ;
- raw/DEPP_fr-en-cites_scolaires_IDF.csv : appariement lycée / collège des cités scolaires (DEPP) ;
- raw/DEPP_fr-en-effectifs-second-degre_obsolete_IDF.csv : effectifs par établissement 2015-2016 à 2019-2020 (DEPP, jeu obsolète).
Dénominateurs :
- « lycéens pré-bac » : élèves du second degré de l'UAI du lycée (rentrée 2025) ;
- « lycéens + post-bac » : + élèves du supérieur (BTS, CPGE) de l'UAI ;
- « tous élèves accueillis » : + collégiens du collège apparié pour les cités mixtes régionales (CMR), que la Région dote en entier.
Sortie : resultats/dotation_consolidee_par_departement.csv et ..._par_lycee_avec_eleves.csv
"""
import sys
import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 40)
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'

d = pd.read_csv(W + 'resultats/dotation_consolidee_2016_2026_par_UAI.csv', sep=';', dtype={'uai': str, 'dep': str})
h = pd.read_csv(W + 'raw/DEPP_fr-en-mode-hebergement-eleves-etablissements-2d_IDF_2020-2025.csv', sep=';', dtype={'uai': str, 'code_departement': str})
h['rentree'] = h['rentree'].astype(int)
c = pd.read_csv(W + 'raw/DEPP_fr-en-cites_scolaires_IDF.csv', sep=';', dtype=str)

S2, SUP = 'nombre_d_eleves_dans_une_formation_du_second_degre', 'nombre_d_eleves_dans_une_formation_du_superieur'


def eleves(uais, annee):
    x = h[(h['rentree'] == annee) & h['uai'].isin(uais)]
    return float(x[S2].sum()), float(x[SUP].sum()), len(x)


# collège apparié des CMR
coll = {}
for cs, g in c.groupby('code_cite_scolaire'):
    lyc = g[~g['libelle_nature'].str.contains('COLLEGE', na=False)]['uai'].tolist()
    col = g[g['libelle_nature'].str.contains('COLLEGE', na=False)]['uai'].tolist()
    for u in lyc:
        coll.setdefault(u, []).extend(col)

rec = []
for _, r in d.iterrows():
    uais = r['uai'].split('+')
    out = {'uai': r['uai'], 'dep': r['dep'], 'section': r['section'], 'patronyme': r['patronyme'], 'commune': r['commune'],
           'type_lycee': r['type_lycee'], 'dot2016': r['dotation_consolidee_2016'], 'dot2026': r['dotation_consolidee_2026']}
    for an in (2020, 2025):
        s2, sup, n = eleves(uais, an)
        out[f'prebac_{an}'], out[f'postbac_{an}'], out[f'n_uai_trouves_{an}'] = s2, sup, n
    col = sum((coll.get(u, []) for u in uais), [])
    out['college_cmr_2025'] = eleves(col, 2025)[0] if r['section'] == 'CMR' else 0.0
    rec.append(out)
x = pd.DataFrame(rec)
print('UAI sans effectifs 2025 :')
print(x[x['n_uai_trouves_2025'] == 0][['uai', 'dep', 'section', 'patronyme', 'dot2026']])
x['lyceens_postbac_2025'] = x['prebac_2025'] + x['postbac_2025']
x['tous_2025'] = x['lyceens_postbac_2025'] + x['college_cmr_2025']
x.to_csv(W + 'resultats/dotation_consolidee_par_lycee_avec_eleves.csv', sep=';', index=False, encoding='utf-8-sig')

ok = x[x['n_uai_trouves_2025'] > 0]
rows = []
for dep, g in list(ok.groupby('dep')) + [('IDF', ok)]:
    e = g[g['section'] == 'EPLE']
    rows.append({'dep': dep, 'n_etab': len(g), 'dot2026_MEUR': g['dot2026'].sum() / 1e6,
                 'prebac_2025': g['prebac_2025'].sum(), 'postbac_2025': g['postbac_2025'].sum(), 'college_cmr_2025': g['college_cmr_2025'].sum(),
                 'EUR_par_lyceen_prebac': g['dot2026'].sum() / g['prebac_2025'].sum(),
                 'EUR_par_lyceen_postbac_inclus': g['dot2026'].sum() / g['lyceens_postbac_2025'].sum(),
                 'EUR_par_eleve_accueilli': g['dot2026'].sum() / g['tous_2025'].sum(),
                 'n_EPLE_seuls': len(e), 'EUR_par_eleve_EPLE_seuls': e['dot2026'].sum() / e['lyceens_postbac_2025'].sum(),
                 'part_CMR_dans_dot2026': g.loc[g['section'] == 'CMR', 'dot2026'].sum() / g['dot2026'].sum(),
                 'taille_moy_eleves_accueillis': g['tous_2025'].mean()})
t = pd.DataFrame(rows)
print(t.round(1).to_string())

# évolution 2016-2026, établissements présents les deux années, et effectifs 2016-2017 (jeu DEPP obsolète)
ob = pd.read_csv(W + 'raw/DEPP_fr-en-effectifs-second-degre_obsolete_IDF.csv', sep=';', dtype=str)
ob['n'] = pd.to_numeric(ob['nombre_d_eleves'], errors='coerce')
e16 = ob[ob['annee_scolaire'] == '2016-2017'].groupby('numero_d_etablissement')['n'].sum()
both = x[x['dot2016'].notna() & (x['dot2016'] > 0)].copy()
both['eleves_2016_obsolete'] = both['uai'].apply(lambda u: sum(e16.get(v, np.nan) for v in u.split('+')))
both['col16'] = both.apply(lambda r: sum(e16.get(v, 0) for v in sum((coll.get(u, []) for u in r['uai'].split('+')), [])) if r['section'] == 'CMR' else 0, axis=1)
rows = []
for dep, g in list(both.groupby('dep')) + [('IDF', both)]:
    g2 = g[g['eleves_2016_obsolete'].notna()]
    rows.append({'dep': dep, 'n_etab_2016_et_2026': len(g), 'dot2016_MEUR': g['dot2016'].sum() / 1e6, 'dot2026_MEUR': g['dot2026'].sum() / 1e6,
                 'evolution_pct': (g['dot2026'].sum() / g['dot2016'].sum() - 1) * 100,
                 'EUR_par_eleve_2016 (effectifs 2016-2017, + collégiens CMR)': g2['dot2016'].sum() / (g2['eleves_2016_obsolete'].sum() + g2['col16'].sum()),
                 'EUR_par_eleve_2026 (rentrée 2025, + post-bac + collégiens CMR)': g2['dot2026'].sum() / g2['tous_2025'].sum()})
t2 = pd.DataFrame(rows)
print(t2.round(1).to_string())
t.to_csv(W + 'resultats/dotation_consolidee_par_departement.csv', sep=';', index=False, encoding='utf-8-sig')
t2.to_csv(W + 'resultats/dotation_consolidee_evolution_2016_2026_par_departement.csv', sep=';', index=False, encoding='utf-8-sig')

# distribution par lycée (EUR par élève accueilli), Paris et 93
x['eur_par_eleve'] = x['dot2026'] / x['tous_2025']
for dep in ['75', '93']:
    g = x[(x['dep'] == dep) & (x['tous_2025'] > 0)]
    print(dep, 'médiane', g['eur_par_eleve'].median().round(0), 'P25', g['eur_par_eleve'].quantile(.25).round(0), 'P75', g['eur_par_eleve'].quantile(.75).round(0))
# effet taille : EUR par élève selon la taille (tous IDF)
x['classe_taille'] = pd.cut(x['tous_2025'], [0, 300, 500, 800, 1200, 5000])
print(x[x['tous_2025'] > 0].groupby('classe_taille', observed=True).apply(lambda g: pd.Series({'n': len(g), 'eur_par_eleve': g['dot2026'].sum() / g['tous_2025'].sum()})))
print(pd.crosstab(x['dep'], x['classe_taille']))
