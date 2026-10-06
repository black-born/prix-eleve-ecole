"""Détail par compte des dépenses réelles des fonctions d'enseignement (DGFiP, balances nature-fonction)
pour le Département de la Seine-Saint-Denis et la Ville de Paris (ou le Département de Paris avant 2019).
Opérations réelles = obnetdeb - oobdeb (débit) et obnetcre - oobcre (crédit) (méthode du projet, NOTES.md § 2).
Fonctionnement : débit net (débit - crédit) des comptes 6 hors 675, 676, 68, 65882.
Investissement : débit des comptes 20, 21, 23 (moins crédit 236-238), 204, 13, 26, 27, 45x, 481 ;
+ 1675 (remboursement en capital des marchés de partenariat, PPP), compté à part.
Usage : python 02_comptes_221_93_Paris.py 2025
"""
import os
import sys

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_colwidth', 80)
HERE = os.path.dirname(os.path.abspath(__file__))
DG = os.path.join(HERE, '..', 'sources', 'dgfip')
LIB = 'C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/OFGL_nomenclature_M57_2025_libelles_comptes.csv'
NUM = ['bedeb', 'becre', 'obnetdeb', 'obnetcre', 'onbdeb', 'onbcre', 'oobdeb', 'oobcre', 'sd', 'sc']


def load(year, kind='idf'):
    if kind == 'idf':
        fn = f'DGFiP_{year}_IDF_departements_Paris_fonction2_dette16_par_compte_API.csv'
    else:
        fn = f'DGFiP_{year}_national_DEPT_PARIS_ML_CTU_REG_fonction2_par_compte_API.csv'
    df = pd.read_csv(os.path.join(DG, fn), sep=';',
                     dtype={'ndept': str, 'fonction': str, 'compte': str, 'ident': str, 'categ': str, 'nomen': str})
    for c in NUM:
        df[c] = df[c].fillna(0.0).astype(float)
    df['fonction'] = df['fonction'].fillna('')
    df['compte'] = df['compte'].astype(str)
    df['deb'] = df.obnetdeb - df.oobdeb
    df['cre'] = df.obnetcre - df.oobcre
    df['f'] = [x[2:] if (x.startswith('90') or x.startswith('93')) and len(x) > 2 else x for x in df.fonction]
    df['annee'] = year
    return df


def nature(c):
    if c.startswith('6'):
        if c.startswith(('675', '676', '68', '65882', '6715')):
            return 'exclu'
        if c.startswith('66'):
            return 'F_charges_financieres'
        if c.startswith(('621', '631', '633', '64')):
            return 'F_personnel'
        if c[:2] in ('60', '61', '62'):
            return 'F_achats_charges_externes'
        if c.startswith(('651', '652', '655', '656', '657')):
            return 'F_interventions'
        return 'F_autres'
    if c.startswith('1675'):
        return 'I_PPP_remboursement_capital_1675'
    if c.startswith('16'):
        return 'dette_autre'
    if c.startswith(('204', '2324')):
        return 'I_subventions_equipement_versees'
    if c[:2] in ('20', '21', '23'):
        return 'I_equipement'
    if c[:2] in ('26', '27'):
        return 'exclu' if c.startswith(('269', '2768', '279')) else 'I_autres'
    if c.startswith('102'):
        return 'exclu' if c.startswith(('10229', '1027')) else 'I_autres'
    if c.startswith('13'):
        return 'exclu' if c.startswith('139') else 'I_autres'
    if c[:3] in ('454', '455', '456', '458') or c.startswith('481'):
        return 'I_autres'
    return 'hors_depense'


def montant(r):
    n = r.nature
    if n.startswith('F_'):
        return r.deb - r.cre
    if n == 'I_equipement':
        return r.deb - (r.cre if r.compte[:3] in ('236', '237', '238') else 0.0)
    if n.startswith('I_'):
        return r.deb
    return np.nan


def poste(c):
    if c.startswith(('621', '631', '633', '64')):
        return 'F1 Personnel (621, 631, 633, 64)'
    if c.startswith(('60611', '60612', '60613', '60621', '60622')):
        return 'F2 Énergie et eau (60611-60613, 60621-60622)'
    if c.startswith(('6152', '6155', '6156', '6283')):
        return 'F3 Entretien, réparations, maintenance, nettoyage (6152x, 6155, 6156, 6283)'
    if c.startswith('611'):
        return 'F4 Contrats de prestations de services (611)'
    if c.startswith(('613', '614')):
        return 'F5 Locations et charges locatives (613, 614)'
    if c[:2] in ('60', '61', '62'):
        return 'F6 Autres achats et charges externes (60-62)'
    if c.startswith('655111'):
        return 'F7 Dotations de fonctionnement aux collèges publics (655111)'
    if c.startswith('655112'):
        return 'F8 Dotations de fonctionnement aux collèges privés (655112)'
    if c.startswith('65512'):
        return 'F8b Dotations aux lycées (65512x)'
    if c == '65511':
        return 'F7b Dotations de fonctionnement collèges non subdivisées (65511)'
    if c.startswith('65'):
        return 'F9 Autres subventions et participations (65x)'
    if c.startswith('66'):
        return 'F10 Charges financières (66)'
    if c.startswith('6'):
        return 'F11 Autres charges de fonctionnement'
    if c.startswith('1675'):
        return 'I0 Remboursement en capital des marchés de partenariat (1675)'
    if c.startswith(('204', '2324')):
        return "I5 Subventions d'équipement versées (204, 2324)"
    if c.startswith(('211', '212', '213', '214', '217', '231', '236', '237', '238')):
        return 'I1 Terrains, constructions, rénovations, gros travaux, avances (211-214, 217, 231x, 236-238)'
    if c.startswith('455'):
        return 'I2 Opérations sous mandat des EPLE (455)'
    if c.startswith(('215', '218')):
        return 'I3 Mobilier, informatique, matériel (215x, 218x)'
    if c.startswith('20'):
        return 'I4 Études, logiciels, incorporels (20 hors 204)'
    if c[:2] in ('21', '23'):
        return 'I6 Autres immobilisations (21, 23)'
    return 'I7 Autres investissements (13, 26, 27, 45x hors 455, 481)'


def poste_nomen(c, nomen):
    """En M52, 65511 = dotation des collèges publics et 65512 = dotation des collèges privés
    (cf. CRC Île-de-France, IDR2023-24, p. 33 : « collèges publics (65511) », « collèges privés (65512) ») ;
    en M57, 655111 = publics, 655112 = privés, 65512 = lycées."""
    if str(nomen) == 'M52':
        if c == '65511':
            return 'F7 Dotations de fonctionnement aux collèges publics (655111)'
        if c == '65512':
            return 'F8 Dotations de fonctionnement aux collèges privés (655112)'
    return poste(c)


def prepare(year, kind='idf'):
    df = load(year, kind)
    df['nature'] = df.compte.map(nature)
    df['montant'] = df.apply(montant, axis=1)
    df['poste'] = [poste_nomen(c, n) for c, n in zip(df.compte, df.nomen)]
    return df


def labels():
    lib = pd.read_csv(LIB, sep=';', dtype=str, encoding='utf-8-sig')
    lib = lib[lib.nomenclature.str.contains('M57', na=False)].drop_duplicates('numero_compte')
    return lib.set_index('numero_compte')['libelle_compte']


if __name__ == '__main__':
    year = int(sys.argv[1]) if len(sys.argv) > 1 else 2025
    df = prepare(year)
    df['libelle'] = df.compte.map(labels())
    is93 = (df.ndept == '093') & (df.categ == 'DEPT')
    isParis = (df.categ == 'PARIS') | ((df.categ == 'DEPT') & (df.ndept == '075'))
    for ent, mask in [('93', is93), ('Paris', isParis)]:
        d = df[mask & df.nature.str.startswith(('F_', 'I_'))]
        print('=' * 30, ent, year, d.lbudg.unique())
        print('--- par sous-fonction (M€) ---')
        t = d.pivot_table(index='f', columns='nature', values='montant', aggfunc='sum').fillna(0).div(1e6).round(2)
        print(t.to_string())
        dd = d[d.f.str.startswith('221') | d.compte.str.startswith('1675')]
        print('--- 221 Collèges (et 1675 toutes fonctions), par poste (M€) ---')
        print(dd.groupby(['poste']).montant.sum().div(1e6).round(2).to_string())
        print('--- 221, par compte (M€, |montant| >= 0,1 M€) ---')
        g = dd.groupby(['nature', 'compte', 'libelle', 'f'], dropna=False).montant.sum().div(1e6).round(2)
        print(g[g.abs() >= 0.1].to_string())
        # Dette PPP : soldes
        p = df[mask & df.compte.str.startswith('1675')]
        print('--- 1675 : lignes brutes ---')
        print(p[['f', 'compte', 'bedeb', 'becre', 'obnetdeb', 'obnetcre', 'onbdeb', 'onbcre', 'oobdeb', 'oobcre', 'sd', 'sc']].to_string())
