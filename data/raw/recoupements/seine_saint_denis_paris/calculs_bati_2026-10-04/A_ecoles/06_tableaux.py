# -*- coding: utf-8 -*-
"""
Tâche A - mise en forme des tableaux (format français) à partir des sorties de 03, 04 et 05.
Affiche les tableaux en Markdown sur la sortie standard et les enregistre au format JSON (sorties/A_tableaux.json).
"""
import os
import sys
import json
import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'sorties')


def fr(x, d=0):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return 'n.d.'
    s = f'{x:,.{d}f}'
    return s.replace(',', ' ').replace('.', ',').replace(' ', ' ') if False else s.replace(',', ' ').replace('.', ',')


def md(header, rows):
    out = '| ' + ' | '.join(header) + ' |\n|' + '|'.join(['---'] * len(header)) + '|\n'
    for r in rows:
        out += '| ' + ' | '.join(r) + ' |\n'
    return out


syn = pd.read_csv(os.path.join(OUT, 'A3_synthese_territoires_annees.csv'), sep=';', encoding='utf-8-sig')
v = syn[syn.variante == 'tous budgets ; rentrée N-1']
YEARS = [2021, 2022, 2023, 2024, 2025]
TERR = [('Paris', 'Paris'), ('Seine-Saint-Denis', 'Seine-Saint-Denis (39 communes)'), ('Hauts-de-Seine', 'Hauts-de-Seine'),
        ('Val-de-Marne', 'Val-de-Marne'), ('France (communes à comptabilité fonctionnelle)', 'France, communes à comptabilité fonctionnelle'),
        ('France hors Paris, 92, 93, 94 (communes à comptabilité fonctionnelle)', 'dont hors Paris et petite couronne')]


def val(terr, c, ys, unit='€'):
    s = v[(v.territoire == terr) & v.annee.isin(ys)]
    if unit == 'M€':
        return s[c + '_M€'].sum()
    return s[c + '_M€'].sum() * 1e6 / s.eleves.sum()


tables = {}
# ---- T1 investissement
rows = []
for c, lab in (('I_total', 'Investissement total (comptes 20, 21, 23)'), ('I_bati', 'dont bâtiments, avances sur travaux, terrains')):
    for t, tl in TERR:
        r = [f'{lab} – {tl}'] + [fr(val(t, c, [a])) for a in YEARS] + [fr(val(t, c, [2023, 2024, 2025])), fr(val(t, c, YEARS))]
        rows.append(r)
p15 = pd.read_csv(os.path.join(OUT, 'A15_Paris_investissement_elargi_vs_93.csv'), sep=';', encoding='utf-8-sig')
pe = p15.set_index('annee')
rows.insert(1, ['Investissement total – Paris, en ajoutant les postes scolaires imputés hors des fonctions « écoles » (borne haute)',
                'n.d.', 'n.d.', fr(pe.loc['2023', 'Paris_elargi_€']), fr(pe.loc['2024', 'Paris_elargi_€']),
                fr(pe.loc['2025', 'Paris_elargi_€']), fr(pe.loc['2023-2025', 'Paris_elargi_€']), 'n.d.'])
rows.append(['Pour mémoire, M€ – Paris'] + [fr(val('Paris', 'I_total', [a], 'M€'), 1) for a in YEARS] +
            [fr(val('Paris', 'I_total', [2023, 2024, 2025], 'M€') / 3, 1) + ' (moy.)', fr(val('Paris', 'I_total', YEARS, 'M€') / 5, 1) + ' (moy.)'])
rows.append(['Pour mémoire, M€ – Seine-Saint-Denis'] + [fr(val('Seine-Saint-Denis', 'I_total', [a], 'M€'), 1) for a in YEARS] +
            [fr(val('Seine-Saint-Denis', 'I_total', [2023, 2024, 2025], 'M€') / 3, 1) + ' (moy.)',
             fr(val('Seine-Saint-Denis', 'I_total', YEARS, 'M€') / 5, 1) + ' (moy.)'])
rows.append(['Rapport Seine-Saint-Denis / Paris (investissement total)'] +
            [fr(val('Seine-Saint-Denis', 'I_total', [a]) / val('Paris', 'I_total', [a]), 2) for a in YEARS] +
            [fr(val('Seine-Saint-Denis', 'I_total', [2023, 2024, 2025]) / val('Paris', 'I_total', [2023, 2024, 2025]), 2),
             fr(val('Seine-Saint-Denis', 'I_total', YEARS) / val('Paris', 'I_total', YEARS), 2)])
rows.append(['Élèves du public, rentrée N-1 – Paris'] + [fr(val('Paris', 'I_total', [a], 'M€') * 1e6 / val('Paris', 'I_total', [a])) for a in YEARS] + ['', ''])
rows.append(['Élèves du public, rentrée N-1 – Seine-Saint-Denis'] +
            [fr(val('Seine-Saint-Denis', 'I_total', [a], 'M€') * 1e6 / val('Seine-Saint-Denis', 'I_total', [a])) for a in YEARS] + ['', ''])
tables['T1'] = md(['€ par élève du public (rentrée N-1)', '2021', '2022', '2023', '2024', '2025', 'Moyenne 2023-2025', 'Moyenne 2021-2025'], rows)

# ---- T2 fonctionnement lié au bâti, moyenne 2023-2025
sens = pd.read_csv(os.path.join(OUT, 'A8b_sensibilite_imputation_energie_moy2023-2025.csv'), sep=';', encoding='utf-8-sig')
sub = 'communes imputant >= 10 % de leur énergie aux écoles chaque année 2021-2025'
cols = [t for t, _ in TERR[:5]]
rows = []
for c, lab in (('F_entretien_batiments_terrains', 'Entretien et réparations des bâtiments et terrains (6152, 61521, 61522x)'),
               ('F_maintenance', 'Maintenance (6156)'),
               ('F_nettoyage_prestations', 'Nettoyage des locaux, prestations (6283)'),
               ('F_fournitures_entretien', "Fournitures d'entretien (60631)"),
               ('F_energie_fluides', 'Énergie et fluides (6061x, 60621)'),
               ('F_loyers_charges_locatives', 'Loyers et charges locatives (6132, 614)'),
               ('F_assurances', 'Assurances (616)'),
               ('F_bati', 'Total des dépenses courantes liées aux bâtiments, hors personnel')):
    rows.append([lab] + [fr(val(t, c, [2023, 2024, 2025])) for t in cols])
rows.append(['Total, communes imputant au moins 10 % de leur énergie aux écoles chaque année (part des élèves)'] +
            [f"{fr(sens[(sens.territoire == t) & (sens.sous_ensemble == sub)].F_bati.iloc[0])} ({fr(100 * sens[(sens.territoire == t) & (sens.sous_ensemble == sub)].part.iloc[0])} %)"
             if t in ('Paris', 'Seine-Saint-Denis', 'Hauts-de-Seine', 'Val-de-Marne') else 'n.d.' for t in cols])
rows.append(["dont énergie et fluides, même sous-ensemble"] +
            [fr(sens[(sens.territoire == t) & (sens.sous_ensemble == sub)].F_energie.iloc[0])
             if t in ('Paris', 'Seine-Saint-Denis', 'Hauts-de-Seine', 'Val-de-Marne') else 'n.d.' for t in cols])
rows.append(['Pour mémoire : personnel (621, 631, 633, 64), non ventilable entre entretien et autres tâches'] +
            [fr(val(t, 'F_personnel', [2023, 2024, 2025])) for t in cols])
rows.append(['Pour mémoire : total du fonctionnement « écoles » (classe 6 hors 66, 675, 676, 68)'] +
            [fr(val(t, 'F_total', [2023, 2024, 2025])) for t in cols])
tables['T2'] = md(['€ par élève du public, moyenne 2023-2025', 'Paris', 'Seine-Saint-Denis', 'Hauts-de-Seine', 'Val-de-Marne',
                   'France (communes à compta. fonctionnelle)'], rows)

# ---- T2b fonctionnement bâti par année
rows = []
for c, lab in (('F_bati', 'Dépenses courantes liées aux bâtiments, hors personnel'), ('F_energie_fluides', 'dont énergie et fluides'),
               ('F_entretien_maintenance', 'dont entretien, réparations et maintenance')):
    for t, tl in TERR[:5]:
        rows.append([f'{lab} – {tl}'] + [fr(val(t, c, [a])) for a in YEARS])
tables['T2b'] = md(['€ par élève du public (rentrée N-1)', '2021', '2022', '2023', '2024', '2025'], rows)

# ---- T3 composition de l'investissement, moyenne 2023-2025
rows = []
for c, lab in (('I_batiments', 'Constructions, rénovations, installations des bâtiments (2313, 2314, 2131x, 2135x, 2138, 214x, 2173-2174, 2181, 2317, 235)'),
               ('I_avances_sur_travaux', 'Avances versées sur travaux (236, 237, 238)'),
               ('I_terrains_amenagements', 'Terrains et aménagements de terrains, dont cours (211, 212, 2171-2172, 2311, 2312)'),
               ('I_bati', 'Sous-total « bâti »'),
               ('I_etudes_incorporels', 'Études et incorporels (20 hors 204, 2328)'),
               ('I_materiel_mobilier', 'Matériel, mobilier, informatique (215, 218, 2175, 2178, 2315)'),
               ('I_subventions_equipement_versees', "Subventions d'équipement versées (204, 2324)"),
               ('I_autres', 'Autres (2161, 2318, etc.)'),
               ('I_total', 'Total (débit réel des comptes 20, 21, 23)'),
               ('I_equipement_DGCL', 'Variante DGCL : 20 hors 204, 21, 23, nette des crédits 236-238'),
               ('R_subventions_investissement_recues', "Subventions d'investissement reçues (comptes 13), fonctions « écoles »")):
    r = [lab]
    for t in cols:
        if t.startswith('France') and c in ('R_subventions_investissement_recues', 'I_equipement_DGCL'):
            r.append('n.d.')
        else:
            r.append(fr(val(t, c, [2023, 2024, 2025])))
    rows.append(r)
rows.append(["Investissement net des subventions reçues"] +
            [fr(val(t, 'I_total', [2023, 2024, 2025]) - val(t, 'R_subventions_investissement_recues', [2023, 2024, 2025]))
             if not t.startswith('France') else 'n.d.' for t in cols])
fl = pd.read_csv(os.path.join(OUT, 'A6_IDF_parts_imputees_aux_ecoles_personnel_energie_entretien.csv'), sep=';', encoding='utf-8-sig',
                 dtype={'code': str})
fl['dep'] = fl.code.str[:2]
part = []
for t, dep in (('Paris', '75'), ('Seine-Saint-Denis', '93'), ('Hauts-de-Seine', '92'), ('Val-de-Marne', '94')):
    s = fl[(fl.dep == dep) & fl.annee.isin([2023, 2024, 2025])]
    part.append(fr(100 * s.equipement_ecoles.sum() / s.equipement_total.sum(), 1) + ' %')
rows.append(["Part des écoles dans l'équipement total de la commune (20, 21, 23, toutes fonctions), 2023-2025"] + part + ['n.d.'])
tables['T3'] = md(['€ par élève du public, moyenne 2023-2025', 'Paris', 'Seine-Saint-Denis', 'Hauts-de-Seine', 'Val-de-Marne',
                   'France (communes à compta. fonctionnelle)'], rows)

# ---- T4 Paris hors fonctions
it = pd.read_csv(os.path.join(OUT, 'A14_Paris_investissements_scolaires_hors_fonctions_ecoles.csv'), sep=';', encoding='utf-8-sig')
rows = []
for poste in it.poste.unique():
    s = it[it.poste == poste].set_index('annee')['montant_M€']
    src = '; '.join(sorted(set(it[it.poste == poste].source.str.replace('Ville de Paris, ', ''))))
    rows.append([poste, it[it.poste == poste].fonction_comptable.iloc[0]] + [fr(s.get(a, np.nan), 1) if a in s.index else '–' for a in (2023, 2024, 2025)] + [src])
rows.append(['Total des postes identifiés hors fonctions « écoles »', ''] + [fr(pe.loc[str(a), 'Paris_hors_fonctions_M€'], 1) for a in (2023, 2024, 2025)] + [''])
rows.append(['Investissement dans les fonctions « écoles » (DGFiP)', '20, 21x, 28x'] + [fr(pe.loc[str(a), 'Paris_fonctions_ecoles_M€'], 1) for a in (2023, 2024, 2025)] + ['DGFiP, balances par fonction'])
rows.append(['Investissement « écoles » élargi (borne haute)', ''] + [fr(pe.loc[str(a), 'Paris_elargi_M€'], 1) for a in (2023, 2024, 2025)] + [''])
rows.append(['… en € par élève du public (rentrée N-1)', ''] + [fr(pe.loc[str(a), 'Paris_elargi_€']) for a in (2023, 2024, 2025)] + [''])
rows.append(['Pour mémoire : remboursement en capital du contrat de partenariat de performance énergétique des écoles (2011)', '923 (dette)'] +
            [fr(pe.loc[str(a), 'Paris_PPP_capital_M€'], 2) for a in (2023, 2024, 2025)] + ['DGFiP, compte 1675 ; CA 2025, p. 23 et 33'])
rows.append(['Pour mémoire : CRC, « total dépenses d\'équipement scolaires » (source Ville de Paris)', '–', '89,6', 'n.d.', 'n.d.',
             'CRC Île-de-France, IDR2025-64, tableau n° 26, p. 57'])
tables['T4'] = md(['Paris, M€', 'Fonction comptable', '2023', '2024', '2025', 'Source'], rows)

# ---- T5 93 par commune
d = pd.read_csv(os.path.join(OUT, 'A4b_93_dispersion_communale_2023-2025.csv'), sep=';', encoding='utf-8-sig', dtype={'code': str})
rows = []
for r in d.itertuples():
    al = []
    def pc(x):
        return '0 %' if x < 0.0005 else fr(100 * x, 1) + ' %'
    if r.part_personnel_ecoles_2025 < 0.10:
        al.append(f'personnel {pc(r.part_personnel_ecoles_2025)}')
    if r.part_energie_ecoles_2025 < 0.10:
        al.append(f'énergie {pc(r.part_energie_ecoles_2025)}')
    if r.part_entretien_ecoles_2025 < 0.05:
        al.append(f'entretien {pc(r.part_entretien_ecoles_2025)}')
    lib = r.libelle + (' (y c. Pierrefitte-sur-Seine)' if r.code == '93066' else '')
    rows.append([lib, fr(r.eleves_rentree2024), fr(r.I_total_par_eleve_2023), fr(r.I_total_par_eleve_2024), fr(r.I_total_par_eleve_2025),
                 fr(r.I_total_moy2023_2025), fr(r.I_bati_moy2023_2025), fr(r.I_total_moy2021_2025),
                 fr(r.F_bati_moy2023_2025), fr(r.F_energie_fluides_moy2023_2025),
                 fr(r.R_subventions_investissement_recues_moy2023_2025), ' ; '.join(al) if al else ''])
tables['T5'] = md(['Commune', 'Élèves du public, rentrée 2024', 'Invest. 2023', 'Invest. 2024', 'Invest. 2025', 'Invest. moy. 2023-2025',
                   'dont bâti', 'Invest. moy. 2021-2025', 'Fonct. bâti moy. 2023-2025', 'dont énergie', 'Subv. reçues moy. 2023-2025',
                   'Part imputée aux écoles en 2025, si faible'], rows)

# ---- T6 contexte DEPP
k = pd.read_csv(os.path.join(OUT, 'A12_ecoles_publiques_classes_eleves_2015-2025.csv'), sep=';', encoding='utf-8-sig')
rows = []
for z in ('Paris', 'Seine-Saint-Denis', 'France'):
    s = k[k.zone == z].set_index('rentree')
    for c, lab in (('nb_ecoles', 'écoles publiques'), ('classes', 'classes'), ('eleves', 'élèves'), ('eleves_par_classe', 'élèves par classe')):
        dd = 1 if c == 'eleves_par_classe' else 0
        rows.append([f'{z} – {lab}'] + [fr(s.loc[a, c], dd) for a in (2015, 2017, 2020, 2024, 2025)] +
                    [fr(100 * (s.loc[2024, c] / s.loc[2015, c] - 1), 1) + ' %'])
tables['T6'] = md(['Écoles publiques (DEPP)', 'Rentrée 2015', '2017', '2020', '2024', '2025', 'Évolution 2015-2024'], rows)

# ---- T7 subventions par origine
sb = pd.read_csv(os.path.join(OUT, 'A9_subventions_investissement_recues_ecoles_par_origine.csv'), sep=';', encoding='utf-8-sig', dtype={'dep': str})
sbt = sb.groupby(['dep', 'origine']).montant.sum().unstack(0).fillna(0)
rows = []
for o in sbt.index:
    rows.append([o] + [fr(sbt.loc[o].get(dpt, 0), 1) for dpt in ('75', '93', '92', '94')])
rows.append(['Total'] + [fr(sbt[dpt].sum(), 1) for dpt in ('75', '93', '92', '94')])
tables['T7'] = md(["Subventions d'investissement reçues, fonctions « écoles », cumul 2021-2025 (M€)", 'Paris', 'Seine-Saint-Denis',
                   'Hauts-de-Seine', 'Val-de-Marne'], rows)

# ---- T8 réplication
rep = pd.read_csv(os.path.join(OUT, 'A5_replication_chiffres_projet_2025.csv'), sep=';', encoding='utf-8-sig')
rows = [[r.indicateur, fr(r.valeur_recalculee, 1), r.valeur_du_projet] for r in rep.itertuples()]
tables['T8'] = md(['Indicateur (2025 sauf mention)', 'Recalculé', 'Valeur du projet'], rows)

for k_, t in tables.items():
    print('=====', k_)
    print(t)
json.dump(tables, open(os.path.join(OUT, 'A_tableaux.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
