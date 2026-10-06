# -*- coding: utf-8 -*-
"""
Tâche A - Paris : investissements liés aux bâtiments scolaires que la Ville impute HORS des fonctions « écoles »
(lus dans les rapports financiers des comptes administratifs 2023, 2024 et 2025 de la Ville de Paris), et
comparaison avec le tableau n° 26 du rapport de la CRC Île-de-France (2025).
Montants saisis à la main depuis les documents officiels (page indiquée) ; tout le reste est calculé.
"""
import os
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'sorties')

# (année, poste, M€, fonction comptable probable, source)
ITEMS = [
    (2023, "Budget participatif d'arrondissement : projets liés aux affaires scolaires (écoles et collèges)", 8.9,
     '0 (services généraux, 038)', 'Ville de Paris, CA 2023, rapport financier, p. 129'),
    (2023, 'Budget participatif des écoles', 2.1, '0 (services généraux, 038)', 'Ville de Paris, CA 2023, rapport financier, p. 129'),
    (2023, 'Mise en accessibilité des bâtiments scolaires', 3.4, '4 (action sociale, handicap)', 'Ville de Paris, CA 2023, rapport financier, p. 77'),
    (2023, 'Contrats de performance énergétique (écoles et collèges)', 1.0, '7 (environnement, actions transverses du PCAET)',
     'Ville de Paris, CA 2023, rapport financier, p. 105'),
    (2024, "Budget participatif d'arrondissement : projets liés aux affaires scolaires (écoles et collèges)", 10.5,
     '0 (services généraux, 038)', 'Ville de Paris, CA 2024, rapport financier, p. 118'),
    (2024, 'Budget participatif des écoles', 2.1, '0 (services généraux, 038)', 'Ville de Paris, CA 2024, rapport financier, p. 118'),
    (2024, 'Mise en accessibilité des bâtiments scolaires', 6.3, '4 (action sociale, handicap)', 'Ville de Paris, CA 2024, rapport financier, p. 70'),
    (2024, 'Contrats de performance énergétique (écoles et collèges)', 10.1, '7 (environnement, actions transverses du PCAET)',
     'Ville de Paris, CA 2024, rapport financier, p. 95'),
    (2025, "Budget participatif d'arrondissement : projets liés aux affaires scolaires (écoles et collèges)", 13.8,
     '0 (services généraux, 038)', 'Ville de Paris, CA 2025, rapport financier, p. 105'),
    (2025, 'Budget participatif des écoles', 3.0, '0 (services généraux, 038)', 'Ville de Paris, CA 2025, rapport financier, p. 105'),
    (2025, 'Mise en accessibilité des bâtiments scolaires', 5.9, '4 (action sociale, handicap)', 'Ville de Paris, CA 2025, rapport financier, p. 68'),
    (2025, 'Contrats de performance énergétique (écoles et collèges)', 9.6, '7 (environnement, actions transverses du PCAET)',
     'Ville de Paris, CA 2025, rapport financier, p. 88'),
    (2025, "Acompte pour l'école de l'équipement mutualisé Pinard, ZAC Saint-Vincent-de-Paul (14e)", 4.2,
     '5 (opérations d\'urbanisme)', 'Ville de Paris, CA 2025, rapport financier, p. 33'),
]
# remboursement en capital du contrat de partenariat de performance énergétique des écoles (CPPE, 2011) :
# compte 1675, chapitre 923 (DGFiP, Q4) ; 2,2 M€ en 2025 (CA 2025, p. 33) ; encours 14,6 M€ fin 2025 (CA 2025, p. 23)
PPP = {2023: 2.41, 2024: 2.33, 2025: 2.22}

it = pd.DataFrame(ITEMS, columns=['annee', 'poste', 'montant_M€', 'fonction_comptable', 'source'])
it.to_csv(os.path.join(OUT, 'A14_Paris_investissements_scolaires_hors_fonctions_ecoles.csv'), sep=';', index=False,
          encoding='utf-8-sig')
syn = pd.read_csv(os.path.join(OUT, 'A3_synthese_territoires_annees.csv'), sep=';', encoding='utf-8-sig')
v = syn[syn.variante == 'tous budgets ; rentrée N-1'].set_index(['territoire', 'annee'])
rows = []
for a in (2023, 2024, 2025):
    p = v.loc[('Paris', a)]
    s = v.loc[('Seine-Saint-Denis', a)]
    hors = it[it.annee == a]['montant_M€'].sum()
    rows.append({'annee': a, 'eleves_Paris': p.eleves, 'Paris_fonctions_ecoles_M€': p['I_total_M€'],
                 'Paris_hors_fonctions_M€': hors, 'Paris_PPP_capital_M€': PPP[a],
                 'Paris_elargi_M€': p['I_total_M€'] + hors, 'Paris_elargi_avec_PPP_M€': p['I_total_M€'] + hors + PPP[a],
                 'Paris_fonctions_€': p['I_total_€_par_eleve'],
                 'Paris_elargi_€': (p['I_total_M€'] + hors) * 1e6 / p.eleves,
                 'Paris_elargi_avec_PPP_€': (p['I_total_M€'] + hors + PPP[a]) * 1e6 / p.eleves,
                 'SSD_€': s['I_total_€_par_eleve'], 'eleves_SSD': s.eleves, 'SSD_M€': s['I_total_M€']})
r = pd.DataFrame(rows)
tot = {'annee': '2023-2025'}
for c in ['eleves_Paris', 'Paris_fonctions_ecoles_M€', 'Paris_hors_fonctions_M€', 'Paris_PPP_capital_M€', 'Paris_elargi_M€',
          'Paris_elargi_avec_PPP_M€', 'eleves_SSD', 'SSD_M€']:
    tot[c] = r[c].sum()
tot['Paris_fonctions_€'] = tot['Paris_fonctions_ecoles_M€'] * 1e6 / tot['eleves_Paris']
tot['Paris_elargi_€'] = tot['Paris_elargi_M€'] * 1e6 / tot['eleves_Paris']
tot['Paris_elargi_avec_PPP_€'] = tot['Paris_elargi_avec_PPP_M€'] * 1e6 / tot['eleves_Paris']
tot['SSD_€'] = tot['SSD_M€'] * 1e6 / tot['eleves_SSD']
r = pd.concat([r, pd.DataFrame([tot])], ignore_index=True)
r['rapport_SSD_Paris_fonctions'] = r['SSD_€'] / r['Paris_fonctions_€']
r['rapport_SSD_Paris_elargi'] = r['SSD_€'] / r['Paris_elargi_€']
pd.set_option('display.width', 250)
print(r.round(2).to_string())
r.to_csv(os.path.join(OUT, 'A15_Paris_investissement_elargi_vs_93.csv'), sep=';', index=False, encoding='utf-8-sig')

# CRC IdF 2025 (IDR2025-64), tableau n° 26, p. 57 : dépenses d'équipement scolaires de la Ville (source : Ville de Paris)
crc = pd.DataFrame({'annee': [2019, 2020, 2021, 2022, 2023],
                    'CRC_total_equipement_scolaire_€': [112473823, 74718436, 70577073, 75726714, 89553885],
                    'CRC_eleves_rentree_N': [122759, 119018, 112875, 108726, 106180]})
crc['CRC_€_par_eleve_rentree_N'] = crc['CRC_total_equipement_scolaire_€'] / crc['CRC_eleves_rentree_N']
crc = crc.merge(syn[(syn.territoire == 'Paris') & (syn.variante == 'tous budgets ; rentrée N-1')][['annee', 'I_total_M€', 'eleves']],
                on='annee', how='left')
crc['ecart_CRC_moins_DGFiP_M€'] = crc['CRC_total_equipement_scolaire_€'] / 1e6 - crc['I_total_M€']
print(crc.round(1).to_string())
crc.to_csv(os.path.join(OUT, 'A16_Paris_CRC_tableau26_vs_DGFiP.csv'), sep=';', index=False, encoding='utf-8-sig')
