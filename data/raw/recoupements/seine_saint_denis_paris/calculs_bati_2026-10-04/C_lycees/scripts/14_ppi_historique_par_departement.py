# -*- coding: utf-8 -*-
"""Opérations de construction et de rénovation des lycées programmées dans les PPI (Région Île-de-France, open data
« Opérations de construction et de rénovation dans les lycées franciliens », mis à jour le 26/01/2018) :
montant des autorisations de programme (AP) votées par lycée (M€ courants), années d'individualisation 1995 à 2018,
PPI 2001/2006, 2012/2022 et 2017/2027 (12 opérations seulement pour ce dernier). Ce ne sont pas des paiements.
Rapport aux élèves accueillis en 2015 (lycées publics, pré-bac + post-bac, jeu DEPP « obsolète » 2015-2016), avec et
sans les collégiens des cités mixtes régionales.
Sortie : resultats/ppi_historique_par_departement.csv
"""
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
DEPS = ['75', '77', '78', '91', '92', '93', '94', '95']
p = pd.read_csv(W + 'raw/IDF_opendata_operations-de-construction-et-de-renovation-dans-les-lycees-francilens.csv', sep=';', encoding='utf-8-sig', dtype=str)
for c in ['enveloppe_prev_en_meur', 'montant_des_ap_votes_en_meur']:
    p[c] = pd.to_numeric(p[c].str.replace(',', '.'), errors='coerce')
p['dep'] = p['codeuai'].str[1:3]
p['annee'] = pd.to_numeric(p['annee_d_individualisation'], errors='coerce')
ob = pd.read_csv(W + 'raw/DEPP_fr-en-effectifs-second-degre_obsolete_IDF.csv', sep=';', dtype=str)
ob['n'] = pd.to_numeric(ob['nombre_d_eleves'], errors='coerce')
ob15 = ob[(ob['annee_scolaire'] == '2015-2016') & (ob['secteur_d_enseignement'] == 'Public')]
lyc15 = ob15[ob15['type_d_etablissement'].str.startswith('LYCEE')]
lyc15 = lyc15.assign(dep=lyc15['code_departement'].str[-2:]).groupby('dep')['n'].sum()
# collégiens des cités mixtes régionales (liste CR 2025-030) en 2015-2016
dc = pd.read_csv(W + 'resultats/dotation_consolidee_2016_2026_par_UAI.csv', sep=';', dtype={'uai': str, 'dep': str})
c = pd.read_csv(W + 'raw/DEPP_fr-en-cites_scolaires_IDF.csv', sep=';', dtype=str)
cmr = dc.loc[dc['section'] == 'CMR', 'uai'].tolist()
cites = c[c['uai'].isin(cmr)]['code_cite_scolaire']
col_uai = c[c['code_cite_scolaire'].isin(cites) & c['libelle_nature'].str.contains('COLLEGE', na=False)]['uai']
col15 = ob15[ob15['numero_d_etablissement'].isin(col_uai)]
col15 = col15.assign(dep=col15['code_departement'].str[-2:]).groupby('dep')['n'].sum()
rows = []
for d in DEPS:
    g = p[p['dep'] == d]
    n1 = lyc15.get(d, 0)
    n2 = n1 + col15.get(d, 0)
    rows.append({'dep': d, 'n_operations': len(g), 'n_lycees': g['codeuai'].nunique(), 'AP_votees_MEUR': g['montant_des_ap_votes_en_meur'].sum(),
                 'enveloppe_prev_MEUR': g['enveloppe_prev_en_meur'].sum(),
                 'dont_PPI_2001_2006_AP': g.loc[g['ppi'] == '2001/2006', 'montant_des_ap_votes_en_meur'].sum(),
                 'dont_PPI_2012_2022_AP': g.loc[g['ppi'] == '2012/2022', 'montant_des_ap_votes_en_meur'].sum(),
                 'dont_PPI_2017_2027_AP': g.loc[g['ppi'] == '2017/2027', 'montant_des_ap_votes_en_meur'].sum(),
                 'eleves_lycees_publics_2015': n1, 'collegiens_CMR_2015': col15.get(d, 0),
                 'AP_EUR_par_eleve_lycee_2015': g['montant_des_ap_votes_en_meur'].sum() * 1e6 / n1,
                 'AP_EUR_par_eleve_accueilli_2015': g['montant_des_ap_votes_en_meur'].sum() * 1e6 / n2})
t = pd.DataFrame(rows)
tot = t[['n_operations', 'AP_votees_MEUR', 'enveloppe_prev_MEUR', 'eleves_lycees_publics_2015', 'collegiens_CMR_2015']].sum()
print(t.round(1).to_string())
print('IDF : AP %.1f M€ ; %.0f € par élève des lycées 2015 ; %.0f € par élève accueilli' % (
    tot['AP_votees_MEUR'], tot['AP_votees_MEUR'] * 1e6 / tot['eleves_lycees_publics_2015'],
    tot['AP_votees_MEUR'] * 1e6 / (tot['eleves_lycees_publics_2015'] + tot['collegiens_CMR_2015'])))
print(p.groupby('ppi')['montant_des_ap_votes_en_meur'].agg(['sum', 'count']))
print(p.groupby(['dep', 'etat_d_avancement']).size().unstack(fill_value=0))
t.to_csv(W + 'resultats/ppi_historique_par_departement.csv', sep=';', index=False, encoding='utf-8-sig')
