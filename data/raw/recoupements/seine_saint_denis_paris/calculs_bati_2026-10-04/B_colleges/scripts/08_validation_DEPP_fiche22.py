"""Validation : investissement et fonctionnement de la fonction 221 (DGFiP) rapportés aux collégiens du public ET du privé,
moyenne 2021-2023, à comparer à DEPP, Géographie de l'École 2026, fiche 22 (onglets 22.1 à 22.3 ; euros constants 2023).
Ici en euros courants (pas de déflateur), d'où un léger écart attendu. Dénominateur : 2/3 R(N-1) + 1/3 R(N), public + privé.
"""
import os, sys
import pandas as pd
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'sources'); OUT = os.path.join(HERE, '..', 'sorties')
e = pd.read_csv(os.path.join(SRC, 'DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv'), sep=';', dtype={'code_dept': str})
e['r'] = e.rentree_scolaire.str[:4].astype(int)
tot = e.groupby(['code_dept', 'r']).eleves.sum().unstack('r')
P = pd.read_csv(os.path.join(OUT, '03_series_221_montants.csv'), sep=';', encoding='utf-8-sig')
res = []
for ent, dep in [('Seine-Saint-Denis', '93'), ('Paris', '75'), ('Hauts-de-Seine', '92'), ('Val-de-Marne', '94')]:
    x = P[(P.entite == ent) & P.annee.isin([2021, 2022, 2023])].set_index('annee')
    den = {y: 2 / 3 * tot.loc[dep, y - 1] + 1 / 3 * tot.loc[dep, y] for y in [2021, 2022, 2023]}
    d = sum(den.values())
    inv = (x.I_equipement + x.I_subventions_equipement_versees + x.I_autres).sum()
    fon = x.F_total_fonctionnement.sum()
    res.append({'entite': ent, 'invest_hors_PPP_par_collegien_pub_priv': inv / d,
                'invest_avec_PPP_par_collegien_pub_priv': (inv + x.I_PPP.sum()) / d,
                'fonct_par_collegien_pub_priv': fon / d})
r = pd.DataFrame(res)
r['DEPP_fiche22_invest'] = [750, 250, 1280, 1300]
r['DEPP_fiche22_fonct'] = [1440, 1230, 1460, 1250]
print(r.round(0).to_string())
r.round(1).to_csv(os.path.join(OUT, '08_validation_DEPP_fiche22.csv'), sep=';', index=False, encoding='utf-8-sig')
