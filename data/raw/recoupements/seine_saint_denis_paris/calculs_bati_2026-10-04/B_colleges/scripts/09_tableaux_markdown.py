"""Mise en forme des tableaux (Markdown, nombres à la française) à partir des sorties 03 à 07.
Sortie : ../sorties/09_tableaux_markdown.txt (texte à reprendre dans le rendu).
"""
import os
import sys

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'sorties')


def fr(x, d=0):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return '—'
    s = f'{x:,.{d}f}'.replace(',', ' ').replace('.', ',')
    return s.replace(' ', ' ') if False else s


lines = []
# ------------------------------------------------------------------ Tableau A : 2022-2025 par collégien du public
T = pd.read_csv(os.path.join(OUT, '07_tableau_principal.csv'), sep=';', encoding='utf-8-sig').set_index('entite')
order = ['Seine-Saint-Denis', 'Paris (Ville de Paris)', 'Hauts-de-Seine', 'Val-de-Marne', 'Seine-et-Marne', 'Essonne',
         'Yvelines', "Val-d'Oise", 'France (départements + Paris + Métropole de Lyon, hors CTU)']
lines.append('TABLEAU A')
lines.append('| € par collégien du public et par an, fonction 221 | Équipement 2022-2025 | Subventions d\'équipement | Capital PPP remboursé | Investissement bâti 2022-2025 | Investissement bâti 2016-2025 | Fonctionnement 2022-2025 | dont frais de personnel | Total hors remboursements 2022-2025 |')
lines.append('|---|---|---|---|---|---|---|---|---|')
for e in order:
    r = T.loc[e]
    ppp = r.PPP_capital if not np.isnan(r.PPP_capital) else 11.0
    inv = r.equipement + r.subv_equipement + ppp
    nom = 'France (départements, Paris, Métropole de Lyon)' if e.startswith('France') else e
    pers = fr(r.personnel) if r.personnel > 0 else '0 (imputé ailleurs)'
    lines.append(f'| {nom} | {fr(r.equipement)} | {fr(r.subv_equipement)} | {fr(ppp)} | **{fr(inv)}** | {fr(r.invest_bati_avec_PPP_2016_2025)} | {fr(r.fonctionnement)} | {pers} | {fr(r.total_hors_remb)} |')

# ------------------------------------------------------------------ Tableau B : postes 93 / Paris
t1 = pd.read_csv(os.path.join(OUT, '05_T1_postes_93_Paris_2022_2025.csv'), sep=';', encoding='utf-8-sig', header=[0, 1], index_col=0)
lines.append('')
lines.append('TABLEAU B')
lines.append('| Fonction 221, moyenne 2022-2025 | Seine-Saint-Denis : M€ par an | Seine-Saint-Denis : € par collégien du public | Paris : M€ par an | Paris : € par collégien du public |')
lines.append('|---|---|---|---|---|')
for p in t1.index:
    a = t1.loc[p]
    def g(k, ent):
        try:
            v = a[(k, ent)]
            return 0.0 if (isinstance(v, float) and np.isnan(v)) else float(v)
        except KeyError:
            return 0.0
    lines.append(f'| {p} | {fr(g("moy_annuelle_MEUR", "Seine-Saint-Denis"), 1)} | {fr(g("euros_par_collegien_public", "Seine-Saint-Denis"))} | {fr(g("moy_annuelle_MEUR", "Paris"), 1)} | {fr(g("euros_par_collegien_public", "Paris"))} |')

# ------------------------------------------------------------------ Tableau C : séries
S = pd.read_csv(os.path.join(OUT, '05_T2_series_bati.csv'), sep=';', encoding='utf-8-sig')
lines.append('')
lines.append('TABLEAU C')
lines.append('| Année | 93 : équipement (M€) | dont participations PPP (235) | 93 : capital PPP remboursé (M€) | 93 : investissement bâti (M€) | 93 : € par collégien du public | Paris : équipement + subventions (M€) | Paris : cités scolaires (M€) | Paris : € par collégien du public (avec cités scolaires) | France : € par collégien du public |')
lines.append('|---|---|---|---|---|---|---|---|---|---|')
for y in range(2012, 2026):
    a = S[(S.entite == 'Seine-Saint-Denis') & (S.annee == y)].iloc[0]
    b = S[(S.entite == 'Paris') & (S.annee == y)].iloc[0]
    c = S[(S.entite.str.startswith('France')) & (S.annee == y)].iloc[0]
    paris_eq = b.equipement_221 + b.subventions_equipement_221
    lines.append(f'| {y} | {fr(a.equipement_221 / 1e6, 1)} | {fr(a.dont_235_part_invest_PPP / 1e6, 1)} | {fr(a.PPP_capital_1675_221 / 1e6, 1)} | {fr(a.invest_bati_221_24_avec_PPP / 1e6, 1)} | {fr(a.invest_bati_221_24_avec_PPP_par_eleve)} | {fr(paris_eq / 1e6, 1)} | {fr(b.equipement_24_cites_scolaires / 1e6, 1)} | {fr(b.invest_bati_221_avec_PPP_par_eleve)} ({fr(b.invest_bati_221_24_avec_PPP_par_eleve)}) | {fr(c.invest_bati_221_avec_PPP_par_eleve)} |')

# ------------------------------------------------------------------ Tableau D : dette PPP
q = pd.read_csv(os.path.join(OUT, '05_T3_dette_PPP_93.csv'), sep=';', encoding='utf-8-sig').set_index('annee')
lines.append('')
lines.append('TABLEAU D')
lines.append('| Année | Encours au 1er janvier (M€) | Dette inscrite à la livraison (M€) | Capital remboursé (M€) | Encours au 31 décembre (M€) |')
lines.append('|---|---|---|---|---|')
for y, r in q.iterrows():
    lines.append(f'| {y} | {fr(r.iloc[0], 1)} | {fr(r.iloc[1], 1)} | {fr(r.iloc[2], 1)} | {fr(r.iloc[3], 1)} |')

# ------------------------------------------------------------------ Tableau E : effectifs et taille
R = pd.read_csv(os.path.join(OUT, '06_evolution_effectifs.csv'), sep=';', encoding='utf-8-sig').set_index('entite')
Z = pd.read_csv(os.path.join(OUT, '06_taille_colleges.csv'), sep=';', encoding='utf-8-sig')
lines.append('')
lines.append('TABLEAU E')
lines.append('| Collégiens du public | Seine-Saint-Denis | Paris | France (hors COM) |')
lines.append('|---|---|---|---|')
for lab, col in [('Rentrée 2015 (établissements de type collège)', 'R2015 (jeu obsolète, type COLLEGE)'),
                 ('Rentrée 2019 (même champ)', 'R2019 (jeu obsolète)'), ('Rentrée 2019 (élèves de niveau collège)', 'R2019'),
                 ('Rentrée 2025 (élèves de niveau collège)', 'R2025')]:
    lines.append(f'| {lab} | {fr(R.loc["Seine-Saint-Denis", col])} | {fr(R.loc["Paris", col])} | {fr(R.loc["France (hors COM)", col])} |')
for lab, col in [('Évolution 2015-2019', 'evol_2015_2019_jeu_obsolete'), ('Évolution 2019-2025', 'evol_2019_2025'), ('Évolution 2015-2025 (raccordée)', 'evol_2015_2025_raccordee')]:
    lines.append(f'| {lab} | {fr(100 * R.loc["Seine-Saint-Denis", col], 1)} % | {fr(100 * R.loc["Paris", col], 1)} % | {fr(100 * R.loc["France (hors COM)", col], 1)} % |')
z = Z[Z.rentree == 2025].set_index('entite')
lines.append(f'| Élèves par établissement, rentrée 2025 | {fr(z.loc["Seine-Saint-Denis", "eleves_par_etablissement"])} | {fr(z.loc["Paris", "eleves_par_etablissement"])} | {fr(z.loc["France (hors COM)", "eleves_par_etablissement"])} |')
lines.append(f'| Part des collégiens dans un établissement de 700 élèves ou plus, rentrée 2025 | {fr(100 * z.loc["Seine-Saint-Denis", "part_eleves_etab_700_plus"], 1)} % | {fr(100 * z.loc["Paris", "part_eleves_etab_700_plus"], 1)} % | {fr(100 * z.loc["France (hors COM)", "part_eleves_etab_700_plus"], 1)} % |')
lines.append(f'| Part des collégiens dans un établissement de moins de 400 élèves, rentrée 2025 | {fr(100 * z.loc["Seine-Saint-Denis", "part_eleves_etab_moins_400"], 1)} % | {fr(100 * z.loc["Paris", "part_eleves_etab_moins_400"], 1)} % | {fr(100 * z.loc["France (hors COM)", "part_eleves_etab_moins_400"], 1)} % |')
open(os.path.join(OUT, '09_tableaux_markdown.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines))
