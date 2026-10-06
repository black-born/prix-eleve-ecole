"""Tableau principal : fonction 221 « Collèges », moyenne 2022-2025, euros par collégien du public (année civile),
départements d'Île-de-France, Ville de Paris et France ; + moyennes 2016-2025 (DGFiP).
Entrées : ../sorties/04_OFGL_221_par_collegien_2022_2025.csv (script 04) ; ../sorties/03_series_221_montants.csv (script 03).
Sortie : ../sorties/07_tableau_principal.csv
"""
import os
import sys

import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'sorties')
L = pd.read_csv(os.path.join(OUT, '04_OFGL_221_par_collegien_2022_2025.csv'), sep=';', encoding='utf-8-sig')
keep = {"Dépenses d'équipement": 'equipement', "Subventions d'équipement versées": 'subv_equipement',
        'Remboursement en capital des marchés de partenariat (1675, fonction 221) [DGFiP]': 'PPP_capital',
        'Frais de personnel': 'personnel', 'Achats et charges externes': 'achats', "Dépenses d'intervention": 'interventions',
        'Charges financières': 'charges_fin', 'Dépenses de fonctionnement': 'fonctionnement',
        'Dépenses totales hors remb': 'total_hors_remb'}
x = L[(L.fonction == '221') & L.agregat.isin(keep)]
g = x.groupby(['entite', 'agregat'])[['montant', 'eleves_public']].sum()
g['par_eleve'] = g.montant / g.eleves_public
T = g.par_eleve.unstack('agregat').rename(columns=keep)
T['invest_bati_avec_PPP'] = T[['equipement', 'subv_equipement', 'PPP_capital']].fillna(0).sum(axis=1)
# moyennes 2016-2025 (DGFiP)
P = pd.read_csv(os.path.join(OUT, '03_series_221_montants.csv'), sep=';', encoding='utf-8-sig')
P = P[(P.annee >= 2016) & P.eleves_public_annee_civile.notna()]
m = P.groupby('entite')[['I_equipement', 'I_subventions_equipement_versees', 'I_PPP', 'eleves_public_annee_civile']].sum()
m['equipement_2016_2025'] = m.I_equipement / m.eleves_public_annee_civile
m['invest_bati_avec_PPP_2016_2025'] = (m.I_equipement + m.I_subventions_equipement_versees + m.I_PPP) / m.eleves_public_annee_civile
rename = {'Paris': 'Paris (Ville de Paris)', 'France (départements, Paris, ML, CTU)': 'France (départements + Paris + Métropole de Lyon, hors CTU)'}
m = m.rename(index=rename)
T = T.join(m[['equipement_2016_2025', 'invest_bati_avec_PPP_2016_2025']], how='left')
T = T.sort_values('invest_bati_avec_PPP', ascending=False)
T.to_csv(os.path.join(OUT, "07_tableau_principal.csv"), sep=";", encoding="utf-8-sig")
print(T.round(0).to_string())
print('Note : la ligne France 2016-2025 vient de la DGFiP avec CTU (script 03) ; 2022-2025 vient de l’OFGL hors CTU.')
