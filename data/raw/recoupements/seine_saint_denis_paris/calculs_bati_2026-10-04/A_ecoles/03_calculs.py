# -*- coding: utf-8 -*-
"""
Tâche A (2026-10-04) - Écoles publiques : ce que les communes dépensent pour leurs bâtiments scolaires,
Paris / Seine-Saint-Denis (contexte : Hauts-de-Seine, Val-de-Marne, ensemble des communes à comptabilité fonctionnelle).

Entrées (toutes officielles) :
  - brut/DGFiP_<année>_Q*.csv : balances DGFiP « présentation croisée nature-fonction », 2021-2025 (01_extraction_dgfip.py) ;
  - brut/DEPP_effectifs_par_ecole_rentrees2020-2025_API.csv : effectifs par école (DEPP) (02_extraction_effectifs.py) ;
  - brut/MEN_annuaire_education_ecoles_UAI_commune_API.csv : annuaire de l'éducation (UAI -> commune Insee) ;
  - projet (lecture seule) : résultats/B1 (effectifs rentrée 2024, Paris = 75056), Insee COG 2026 (communes,
    communes déléguées), nomenclature M57 (OFGL) pour les libellés de comptes.

Conventions (identiques au projet, data/raw/collectivites/extractions/_script_extractions_collectivites.py) :
  - opérations réelles : débit = OBNETDEB - OOBDEB ; crédit = OBNETCRE - OOBCRE ;
  - fonctionnement : classe 6 hors 66, 675, 676, 68 ; montant = débit - crédit ;
  - investissement (« équipement », définition du fichier par commune du projet, qui donne 1 357 / 610 / 920 €) :
    débit réel des comptes 20 (y c. 204), 21 et 23 ; remboursements d'emprunts (16) exclus par construction ;
    variante « DGCL » : débit 20 hors 204, 21, 23 - crédit 236-238 (+ 204 à part) ;
  - périmètre « écoles » : fonctions 20, 21x, 28x, 29 (y c. codes 90x / 93x des budgets votés par fonction),
    plus, pour les années où une commune est en M14, les fonctions 25x sauf 252 (services annexes de l'enseignement,
    dont 251 restauration), plus la fonction 2 « non ventilée » ;
  - dénominateur principal : élèves des écoles publiques de la commune à la rentrée N-1 (comme B1 pour 2025).
"""
import os
import re
import sys
import glob
import unicodedata
import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)

HERE = os.path.dirname(os.path.abspath(__file__))
BRUT = os.path.join(HERE, 'brut')
OUT = os.path.join(HERE, 'sorties')
os.makedirs(OUT, exist_ok=True)
PROJ = r'C:/Users/chret/Documents/EtatEcole'
RAWC = os.path.join(PROJ, 'data', 'raw', 'collectivites')
B1 = os.path.join(PROJ, 'resultats', 'B1_depense_publique_par_etablissement_2025.csv')
YEARS = [2021, 2022, 2023, 2024, 2025]
DEPTS = {'75': 'Paris', '92': 'Hauts-de-Seine', '93': 'Seine-Saint-Denis', '94': 'Val-de-Marne'}


def wcsv(df, name):
    df.to_csv(os.path.join(OUT, name), sep=';', index=False, encoding='utf-8-sig')


# ------------------------------------------------------------------------------------------------------------
# 0. Codes communes
# ------------------------------------------------------------------------------------------------------------
COG = pd.read_csv(os.path.join(RAWC, 'INSEE_COG2026_v_commune_2026.csv'), dtype=str)
PARENT = {r.COM: r.COMPARENT for r in COG.itertuples() if r.TYPECOM in ('COMD', 'COMA', 'ARM')
          and isinstance(r.COMPARENT, str) and r.COMPARENT != r.COM}
LIBCOM = COG[COG.TYPECOM == 'COM'].set_index('COM').LIBELLE.to_dict()
MARSEILLE = {f'132{i:02d}' for i in range(1, 17)}


def norm_code(c):
    if not isinstance(c, str) or c == '':
        return None
    if c.startswith('751') and len(c) == 5:
        return '75056'
    if c.startswith('6938'):
        return '69123'
    if c in MARSEILLE:
        return '13055'
    return PARENT.get(c, c)


def insee_code(nd, ins):
    if not isinstance(ins, str) or not isinstance(nd, str):
        return None
    if nd.startswith('1'):
        return '97' + ins
    return nd[1:] + ins


def code_dgfip(categ, nd, ins):
    if categ == 'PARIS':
        return '75056'
    return norm_code(insee_code(nd, ins))


def norm_lib(s):
    if not isinstance(s, str):
        return None
    for a, b in (('Œ', 'OE'), ('œ', 'oe')):
        s = s.replace(a, b)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii').upper()
    s = re.sub(r'[^A-Z0-9]+', ' ', s).strip()
    s = re.sub(r'\bSTE\b', 'SAINTE', s)
    s = re.sub(r'\bST\b', 'SAINT', s)
    return re.sub(r'\s+', ' ', s)


# ------------------------------------------------------------------------------------------------------------
# 1. Effectifs du public par commune et par rentrée (DEPP)
# ------------------------------------------------------------------------------------------------------------
def effectifs():
    e = pd.read_csv(os.path.join(BRUT, 'DEPP_effectifs_par_ecole_rentrees2020-2025_API.csv'), sep=';', dtype=str,
                    encoding='utf-8-sig')
    e['eleves'] = pd.to_numeric(e.nombre_total_eleves).fillna(0)
    e['rentree'] = e.rentree_scolaire.str[:4].astype(int)
    pub = e[e.secteur.str.upper().str.startswith('PUBLIC')].copy()
    a = pd.read_csv(os.path.join(BRUT, 'MEN_annuaire_education_ecoles_UAI_commune_API.csv'), sep=';', dtype=str,
                    encoding='utf-8-sig').drop_duplicates('identifiant_de_l_etablissement')
    a = a.set_index('identifiant_de_l_etablissement').code_commune
    pub['code'] = pub.numero_ecole.map(a)
    pub['methode'] = np.where(pub.code.notna(), '1 annuaire (UAI)', None)
    b1 = pd.read_csv(B1, sep=';', encoding='utf-8-sig', usecols=['uai', 'code_commune_norm'],
                     dtype={'uai': str, 'code_commune_norm': str}).drop_duplicates('uai').set_index('uai').code_commune_norm
    m = pub.code.isna() & pub.numero_ecole.isin(b1.index)
    pub.loc[m, 'code'] = pub.loc[m, 'numero_ecole'].map(b1)
    pub.loc[m, 'methode'] = '2 B1 (UAI, rentrée 2024)'
    pub['lib'] = pub.commune.map(norm_lib)
    pub['dep'] = pub.code_departement.str.upper().str.zfill(2)
    ok = pub[pub.code.notna()]
    learn = ok.groupby(['dep', 'lib']).code.agg(lambda s: s.map(norm_code).value_counts().index[0])
    m = pub.code.isna()
    pub.loc[m, 'code'] = [learn.get(k) for k in zip(pub.loc[m, 'dep'], pub.loc[m, 'lib'])]
    pub.loc[m & pub.code.notna(), 'methode'] = '3 libellé + département (écoles appariées)'
    cog = COG.copy()
    cog['lib'] = cog.LIBELLE.map(norm_lib)
    cog['cible'] = np.where(cog.TYPECOM == 'COM', cog.COM, cog.COMPARENT)
    depmap = cog[cog.TYPECOM == 'COM'].set_index('COM').DEP
    cog['dep2'] = cog.DEP.fillna(cog.cible.map(depmap))
    cogk = cog.groupby(['dep2', 'lib']).cible.agg(lambda s: s.iloc[0] if s.nunique() == 1 else None)
    m = pub.code.isna()
    pub.loc[m, 'code'] = [cogk.get(k) for k in zip(pub.loc[m, 'dep'], pub.loc[m, 'lib'])]
    pub.loc[m & pub.code.notna(), 'methode'] = '4 libellé + département (COG 2026)'
    pub['methode'] = pub.methode.fillna('5 non apparié')
    pub['code'] = pub.code.map(norm_code)
    st = pub.groupby(['rentree', 'methode']).eleves.sum().unstack().fillna(0).astype(int)
    st.reset_index().to_csv(os.path.join(OUT, 'A0b_appariement_ecoles_communes.csv'), sep=';', index=False,
                            encoding='utf-8-sig')
    pc = pub.dropna(subset=['code']).groupby(['code', 'rentree']).agg(eleves=('eleves', 'sum'),
                                                                      ecoles=('numero_ecole', 'nunique')).reset_index()
    return pc, st


# ------------------------------------------------------------------------------------------------------------
# 2. Classements : périmètre fonctionnel et catégories de comptes
# ------------------------------------------------------------------------------------------------------------
def fnorm(x):
    x = str(x)
    return x[2:] if x.startswith(('902', '932')) else x


def perimetre(f, nomen):
    if f.startswith(('20', '21', '28', '29')):
        return 'ecoles'
    if f == '2':
        return 'ecoles'          # fonction 2 non ventilée
    if f.startswith('25') and str(nomen).startswith('M14') and not f.startswith('252'):
        return 'ecoles'          # M14 : services annexes de l'enseignement (hors 252 transports scolaires)
    return None


def sous_perimetre(f, nomen):
    if f.startswith('21'):
        return '21x premier degré (211-213)'
    if f.startswith('20'):
        return '20 services communs'
    if f.startswith('281') or (str(nomen).startswith('M14') and f.startswith('251')):
        return '281 restauration scolaire (M14 : 251)'
    if f == '2':
        return '2 non ventilé'
    return '28x / 29 autres services annexes (M14 : 25x)'


def categorie(c):
    c = str(c)
    if c.startswith('6'):
        if c.startswith(('66', '675', '676', '68')):
            return None
        if c.startswith(('621', '631', '633', '64')):
            return 'F_personnel'
        if c == '6152' or c.startswith(('61521', '61522')):
            return 'F_entretien_batiments_terrains'
        if c.startswith('6156'):
            return 'F_maintenance'
        if c.startswith('6283'):
            return 'F_nettoyage_prestations'
        if c.startswith('60631'):
            return 'F_fournitures_entretien'
        if c.startswith(('6061', '60621')):
            return 'F_energie_fluides'
        if c.startswith(('6132', '614')):
            return 'F_loyers_charges_locatives'
        if c.startswith('616'):
            return 'F_assurances'
        if c.startswith('615'):
            return 'F_autres_entretiens_hors_bati'
        return 'F_autres'
    if c[:2] in ('20', '21', '23'):
        if c.startswith(('204', '2324')):
            return 'I_subventions_equipement_versees'
        if c.startswith(('20', '2328')):
            return 'I_etudes_incorporels'
        if c.startswith(('236', '237', '238')):
            return 'I_avances_sur_travaux'
        if c.startswith(('211', '212', '2171', '2172', '2311', '2312')):
            return 'I_terrains_amenagements'
        if c.startswith(('2131', '2132', '2135', '2138', '214', '2173', '2174', '2181', '2313', '2314', '2317', '235')):
            return 'I_batiments'
        if c.startswith(('215', '218', '2175', '2178', '2315')):
            return 'I_materiel_mobilier'
        return 'I_autres'
    if c.startswith('13') and not c.startswith('139'):
        return 'R_subventions_investissement_recues'
    if c.startswith('7'):
        return 'R_recettes_fonctionnement'
    return None


def montant(cat, deb, cre):
    if not isinstance(cat, str):
        return np.nan
    if cat.startswith('F_'):
        return deb - cre
    if cat.startswith('I_'):
        return deb
    return cre - deb


F_BATI = ['F_entretien_batiments_terrains', 'F_maintenance', 'F_nettoyage_prestations', 'F_fournitures_entretien',
          'F_energie_fluides', 'F_loyers_charges_locatives', 'F_assurances']
I_BATI = ['I_batiments', 'I_avances_sur_travaux', 'I_terrains_amenagements']


def lire(path):
    q = pd.read_csv(path, sep=';', dtype=str, encoding='utf-8-sig')
    for c in ['obnetdeb', 'obnetcre', 'oobdeb', 'oobcre']:
        q[c] = pd.to_numeric(q[c], errors='coerce').fillna(0.0)
    q['deb'] = q.obnetdeb - q.oobdeb
    q['cre'] = q.obnetcre - q.oobcre
    return q


def classer(q):
    q['code'] = [code_dgfip(a, b, c) for a, b, c in zip(q.categ, q.ndept, q.insee)]
    if 'fonction' in q:
        q['f'] = q.fonction.map(fnorm)
    q['cat'] = q.compte.map(categorie)
    q['montant'] = [montant(a, b, c) for a, b, c in zip(q.cat, q.deb, q.cre)]
    # variante « DGCL » de l'équipement : débit 20 hors 204, 21, 23 - crédit 236-238
    q['eq_dgcl'] = np.where(q.compte.str[:2].isin(['20', '21', '23']) & ~q.compte.str.startswith(('204', '2324')),
                            q.deb - np.where(q.compte.str.startswith(('236', '237', '238')), q.cre, 0.0), 0.0)
    return q


# ------------------------------------------------------------------------------------------------------------
# 3. Île-de-France (Paris, 92, 93, 94) : détail par commune, budget, fonction, compte
# ------------------------------------------------------------------------------------------------------------
def idf():
    rows = []
    for y in YEARS:
        q = lire(glob.glob(os.path.join(BRUT, f'DGFiP_{y}_Q1_*.csv'))[0])
        q['annee'] = y
        rows.append(q)
    q = classer(pd.concat(rows, ignore_index=True))
    q['perim'] = [perimetre(f, n) for f, n in zip(q.f, q.nomen)]
    q['sous_perim'] = [sous_perimetre(f, n) for f, n in zip(q.f, q.nomen)]
    q['dep'] = q.code.str[:2]
    return q


# ------------------------------------------------------------------------------------------------------------
# 4. France : communes à comptabilité fonctionnelle
# ------------------------------------------------------------------------------------------------------------
def france():
    rows = []
    for y in YEARS:
        a = lire(glob.glob(os.path.join(BRUT, f'DGFiP_{y}_Q3_*.csv'))[0])
        a['f'] = '20/21/28/29'
        b = lire(glob.glob(os.path.join(BRUT, f'DGFiP_{y}_Q3b_*.csv'))[0])
        b['f'] = b.fonction.map(fnorm)
        b = b[b.nomen.str.startswith('M14') & ~b.f.str.startswith('252')]
        c = lire(glob.glob(os.path.join(BRUT, f'DGFiP_{y}_Q3c_*.csv'))[0])
        c['f'] = '2'
        for d, src in ((a, 'Q3'), (b, 'Q3b M14 25x hors 252'), (c, 'Q3c fonction 2 non ventilée')):
            d['annee'] = y
            d['source'] = src
            rows.append(d)
    q = classer(pd.concat(rows, ignore_index=True))
    return q


def main():
    pc, st = effectifs()
    print('Appariement des écoles (élèves du public par méthode) :')
    print(st)
    wcsv(pc.assign(libelle=pc.code.map(LIBCOM)), 'A0_effectifs_publics_par_commune_rentrees2020-2025.csv')
    el = pc.pivot_table(index='code', columns='rentree', values='eleves', aggfunc='sum').fillna(0)

    # ---- contrôle : rentrée 2024 (DEPP, appariement) contre B1
    b1 = pd.read_csv(B1, sep=';', encoding='utf-8-sig', dtype={'code_departement': str, 'uai': str, 'code_commune_norm': str},
                     usecols=['uai', 'type', 'secteur', 'code_departement', 'code_commune_norm', 'commune', 'eleves'])
    b1e = b1[(b1.type == 'école') & (b1.secteur == 'public')]
    b1c = b1e.groupby('code_commune_norm').eleves.sum()
    cmp = pd.DataFrame({'B1_rentree2024': b1c, 'DEPP_apparie_rentree2024': el[2024]}).fillna(0)
    cmp['ecart'] = cmp.DEPP_apparie_rentree2024 - cmp.B1_rentree2024
    cmp['dep'] = cmp.index.str[:2]
    print('Contrôle B1 / DEPP rentrée 2024 (75, 92, 93, 94, France) :')
    print(cmp[cmp.dep.isin(DEPTS)].groupby('dep')[['B1_rentree2024', 'DEPP_apparie_rentree2024', 'ecart']].sum())
    print(cmp[['B1_rentree2024', 'DEPP_apparie_rentree2024']].sum())

    # ---- IDF
    q = idf()
    e = q[q.perim == 'ecoles'].copy()
    # communes du 93 et de Paris : contrôle des nomenclatures et des fonctions 25x en M57 (non retenues)
    m57_25 = q[(q.f.str.startswith('25')) & q.nomen.str.startswith('M57') & q.dep.isin(['75', '92', '93', '94'])]
    print('Fonctions 25x en M57 (formation professionnelle, non retenues) :',
          m57_25.groupby(['annee', 'dep']).montant.sum().div(1e6).round(2).to_dict())
    nv2 = e[e.f == '2'].groupby(['annee', 'dep']).montant.sum().div(1e6).round(2)
    print('Fonction 2 non ventilée retenue (M€) :', nv2.to_dict())
    m14 = e[e.nomen.str.startswith('M14') & e.f.str.startswith('25')].groupby(['annee', 'dep']).montant.sum().div(1e6).round(2)
    print('M14 25x retenues (M€) :', m14.to_dict())

    # agrégat par commune x année x catégorie
    g = e.groupby(['dep', 'code', 'annee', 'cbudg', 'sous_perim', 'cat']).agg(montant=('montant', 'sum'),
                                                                              eq_dgcl=('eq_dgcl', 'sum')).reset_index()
    g['libelle'] = g.code.map(LIBCOM)
    wcsv(g, 'A1_IDF_depenses_ecoles_par_commune_annee_budget_sousfonction_categorie.csv')

    # ---- tableau large commune x année
    def large(df):
        w = df.pivot_table(index=['dep', 'code', 'annee'], columns='cat', values='montant', aggfunc='sum').fillna(0)
        for c in F_BATI + I_BATI + ['F_personnel', 'F_autres', 'F_autres_entretiens_hors_bati', 'I_materiel_mobilier',
                                     'I_etudes_incorporels', 'I_subventions_equipement_versees', 'I_autres',
                                     'R_subventions_investissement_recues', 'R_recettes_fonctionnement']:
            if c not in w:
                w[c] = 0.0
        w['F_total'] = w[[c for c in w.columns if c.startswith('F_')]].sum(axis=1)
        w['F_bati'] = w[F_BATI].sum(axis=1)
        w['F_entretien_maintenance'] = w[['F_entretien_batiments_terrains', 'F_maintenance']].sum(axis=1)
        w['F_nettoyage'] = w[['F_nettoyage_prestations', 'F_fournitures_entretien']].sum(axis=1)
        w['I_total'] = w[[c for c in w.columns if c.startswith('I_')]].sum(axis=1)
        w['I_bati'] = w[I_BATI].sum(axis=1)
        return w
    w_all = large(e)
    w_bp = large(e[e.cbudg == '1'])
    eqd = e.groupby(['dep', 'code', 'annee']).eq_dgcl.sum()
    w_all['I_equipement_DGCL'] = eqd
    # sous-périmètre strict (211-213), comme le Cap sur n° 21 de l'OFGL
    w_strict = large(e[e.sous_perim.str.startswith('21x')])

    # effectifs rentrée N-1 et année civile (2/3 R(N-1) + 1/3 R(N))
    def eleves_for(idx):
        n1 = [el.loc[c, a - 1] if c in el.index else np.nan for c, a in zip(idx.get_level_values('code'), idx.get_level_values('annee'))]
        civ = [(2 / 3 * el.loc[c, a - 1] + 1 / 3 * el.loc[c, a]) if c in el.index else np.nan
               for c, a in zip(idx.get_level_values('code'), idx.get_level_values('annee'))]
        return np.array(n1, dtype=float), np.array(civ, dtype=float)
    for w in (w_all, w_bp, w_strict):
        w['eleves_rentree_N_1'], w['eleves_annee_civile'] = eleves_for(w.index)
    w_all.reset_index().assign(libelle=lambda d: d.code.map(LIBCOM)).to_csv(
        os.path.join(OUT, 'A2_IDF_communes_annee_categories_euros.csv'), sep=';', index=False, encoding='utf-8-sig')

    # ---- France : communes couvertes
    fr = france()
    fr = fr[fr.cat.notna()]
    wf = fr.pivot_table(index=['code', 'annee'], columns='cat', values='montant', aggfunc='sum').fillna(0)
    wfb = fr[fr.cbudg == '1'].pivot_table(index=['code', 'annee'], columns='cat', values='montant', aggfunc='sum').fillna(0)
    wf_q3bp = fr[(fr.cbudg == '1') & (fr.source == 'Q3')].pivot_table(index=['code', 'annee'], columns='cat',
                                                                       values='montant', aggfunc='sum').fillna(0)
    for w in (wf, wfb, wf_q3bp):
        for c in F_BATI + I_BATI:
            if c not in w:
                w[c] = 0.0
        w['F_total'] = w[[c for c in w.columns if c.startswith('F_')]].sum(axis=1)
        w['F_bati'] = w[F_BATI].sum(axis=1)
        w['F_entretien_maintenance'] = w[['F_entretien_batiments_terrains', 'F_maintenance']].sum(axis=1)
        w['F_nettoyage'] = w[['F_nettoyage_prestations', 'F_fournitures_entretien']].sum(axis=1)
        w['I_total'] = w[[c for c in w.columns if c.startswith('I_')]].sum(axis=1)
        w['I_bati'] = w[I_BATI].sum(axis=1)
        w['eleves_rentree_N_1'], w['eleves_annee_civile'] = eleves_for(w.index)
    unm = fr[fr.code.isna()].groupby('annee').montant.sum().div(1e6).round(2)
    print('France : montants sans code commune (M€) :', unm.to_dict())

    # ---- replication des chiffres du projet (2025 ; BP ; fonctions 20/21/28/29 ; B1)
    rep = []
    r25 = wf_q3bp.xs(2025, level='annee')
    r25 = r25.join(b1c.rename('B1'), how='left').fillna({'B1': 0})
    cov = r25[(r25.F_total > 0) & (r25.B1 > 0)]
    rep.append(('France, communes couvertes (F > 0 et élèves B1 > 0) : investissement 20/21/23, € par élève B1',
                cov.I_total.sum() / cov.B1.sum(), 'environ 920 € (analyse § 3.1)'))
    cov2 = r25[(r25.F_total > 0) & (r25.eleves_annee_civile > 0)]
    rep.append(('France, communes couvertes : investissement, € par élève, année civile 2025 (2/3 R2024 + 1/3 R2025)',
                cov2.I_total.sum() / cov2.eleves_annee_civile.sum(), '931 € (NOTES.md § 3)'))
    rep.append(('France, communes couvertes : fonctionnement, € par élève, année civile 2025',
                cov2.F_total.sum() / cov2.eleves_annee_civile.sum(), '2 821 € (NOTES.md § 3)'))
    for dep, lib in (('93', 'Seine-Saint-Denis'), ('75', 'Paris')):
        s = r25[r25.index.str[:2] == dep]
        den = b1e[b1e.code_departement == dep].eleves.sum()
        rep.append((f'{lib} : investissement 20/21/23 (BP), M€', s.I_total.sum() / 1e6, '249 M€ (93) ; 63 M€ (Paris) (H-B21)'))
        rep.append((f'{lib} : investissement, € par élève B1', s.I_total.sum() / den, '1 357 € (93) ; 610 € (Paris)'))
        rep.append((f'{lib} : fonctionnement (BP), € par élève B1', s.F_total.sum() / den, '2 552 € (93) ; 7 046 € (Paris)'))
    r24 = wf_q3bp.xs(2024, level='annee')
    for dep, lib in (('93', 'Seine-Saint-Denis'), ('75', 'Paris')):
        rep.append((f'{lib} : investissement 2024 (BP, 20/21/28/29), M€', r24[r24.index.str[:2] == dep].I_total.sum() / 1e6,
                    '242 M€ (93) ; 64 M€ (Paris) (analyse § 3.1)'))
    rep = pd.DataFrame(rep, columns=['indicateur', 'valeur_recalculee', 'valeur_du_projet'])
    print(rep.to_string())
    wcsv(rep, 'A5_replication_chiffres_projet_2025.csv')

    # ---- synthèse par territoire et par année (€ par élève du public, rentrée N-1)
    cols = ['F_entretien_batiments_terrains', 'F_maintenance', 'F_entretien_maintenance', 'F_nettoyage_prestations',
            'F_fournitures_entretien', 'F_nettoyage', 'F_energie_fluides', 'F_loyers_charges_locatives', 'F_assurances',
            'F_bati', 'F_autres_entretiens_hors_bati', 'F_personnel', 'F_total',
            'I_batiments', 'I_avances_sur_travaux', 'I_terrains_amenagements', 'I_bati', 'I_etudes_incorporels',
            'I_materiel_mobilier', 'I_subventions_equipement_versees', 'I_autres', 'I_total']
    syn = []

    def ajoute(terr, w, den_col, variante):
        for a in YEARS:
            s = w.xs(a, level='annee') if 'annee' in w.index.names else w
            den = s[den_col].sum()
            d = {'territoire': terr, 'variante': variante, 'annee': a, 'eleves': den, 'nb_communes': len(s)}
            for c in cols + [k for k in ('R_subventions_investissement_recues', 'I_equipement_DGCL') if k in s]:
                d[c + '_M€'] = s[c].sum() / 1e6 if c in s else 0.0
                d[c + '_€_par_eleve'] = s[c].sum() / den if c in s else 0.0
            syn.append(d)

    wa = w_all.reset_index().set_index(['code', 'annee'])
    for dep, lib in DEPTS.items():
        sub = wa[wa.dep == dep]
        sub = sub[sub.eleves_rentree_N_1 > 0]
        ajoute(lib, sub, 'eleves_rentree_N_1', 'tous budgets ; rentrée N-1')
        ajoute(lib, sub, 'eleves_annee_civile', 'tous budgets ; année civile')
    wbp = w_bp.reset_index().set_index(['code', 'annee'])
    ajoute('Paris', wbp[wbp.dep == '75'], 'eleves_rentree_N_1', 'budget principal seul ; rentrée N-1')
    ws = w_strict.reset_index().set_index(['code', 'annee'])
    for dep, lib in DEPTS.items():
        sub = ws[(ws.dep == dep) & (ws.eleves_rentree_N_1 > 0)]
        ajoute(lib, sub, 'eleves_rentree_N_1', 'sous-fonctions 211-213 seules ; rentrée N-1')
    # France : communes couvertes (F > 0) ayant des élèves
    for a in YEARS:
        pass
    cv = wf[(wf.F_total > 0) & (wf.eleves_rentree_N_1 > 0)]
    ajoute('France (communes à comptabilité fonctionnelle)', cv, 'eleves_rentree_N_1', 'tous budgets ; rentrée N-1')
    cvb = wfb[(wfb.F_total > 0) & (wfb.eleves_rentree_N_1 > 0)]
    ajoute('France (communes à comptabilité fonctionnelle)', cvb, 'eleves_rentree_N_1', 'budget principal seul ; rentrée N-1')
    cvc = wf[(wf.F_total > 0) & (wf.eleves_annee_civile > 0)]
    ajoute('France (communes à comptabilité fonctionnelle)', cvc, 'eleves_annee_civile', 'tous budgets ; année civile')
    # France hors Paris et petite couronne
    cvx = cv[~cv.index.get_level_values('code').str[:2].isin(['75', '92', '93', '94'])]
    ajoute('France hors Paris, 92, 93, 94 (communes à comptabilité fonctionnelle)', cvx, 'eleves_rentree_N_1',
           'tous budgets ; rentrée N-1')
    syn = pd.DataFrame(syn)
    wcsv(syn, 'A3_synthese_territoires_annees.csv')

    # ---- 93 : dispersion communale
    w93 = w_all.reset_index()
    w93 = w93[w93.dep == '93']
    # personnel : part imputée aux écoles (Q2a), énergie et entretien : part imputée aux écoles (Q2d)
    flags = []
    # nomenclature (M14 / M57) de chaque commune et de chaque année, lue dans Q1
    nom = q.dropna(subset=['code']).groupby(['code', 'annee']).nomen.agg(lambda s: s.value_counts().index[0])
    for y in YEARS:
        p = lire(glob.glob(os.path.join(BRUT, f'DGFiP_{y}_Q2a_*.csv'))[0])
        p['code'] = [code_dgfip(a, b, c) for a, b, c in zip(p.categ, p.ndept, p.insee)]
        p['f'] = p.fonction.fillna('').map(fnorm)
        p['nomen'] = [nom.get((c, y), 'M57') for c in p.code]
        p['pers'] = p.deb - p.cre
        tot = p.groupby('code').pers.sum()
        isec_p = np.array([perimetre(f, n) == 'ecoles' for f, n in zip(p.f, p.nomen)])
        ec = p[isec_p].groupby('code').pers.sum()
        d2 = classer(lire(glob.glob(os.path.join(BRUT, f'DGFiP_{y}_Q2d_*.csv'))[0]))
        d2['f'] = d2.fonction.fillna('').map(fnorm)
        d2['nomen'] = [nom.get((c, y), 'M57') for c in d2.code]
        d2['m'] = d2.deb - d2.cre
        d2['grp'] = np.where(d2.cat == 'F_energie_fluides', 'energie',
                             np.where(d2.cat.isin(['F_entretien_batiments_terrains', 'F_maintenance']), 'entretien', 'autres'))
        isec = np.array([perimetre(f, n) == 'ecoles' for f, n in zip(d2.f, d2.nomen)])
        en_tot = d2[d2.grp == 'energie'].groupby('code').m.sum()
        en_ec = d2[(d2.grp == 'energie') & isec].groupby('code').m.sum()
        et_tot = d2[d2.grp == 'entretien'].groupby('code').m.sum()
        et_ec = d2[(d2.grp == 'entretien') & isec].groupby('code').m.sum()
        # équipement (20, 21, 23) toutes fonctions (Q2c) : part consacrée aux écoles
        c2 = lire(glob.glob(os.path.join(BRUT, f'DGFiP_{y}_Q2c_*.csv'))[0])
        c2['code'] = [code_dgfip(a, b, c) for a, b, c in zip(c2.categ, c2.ndept, c2.insee)]
        c2['f'] = c2.fonction.fillna('').map(fnorm)
        c2['nomen'] = [nom.get((c, y), 'M57') for c in c2.code]
        eq_tot = c2.groupby('code').deb.sum()
        isec_c = np.array([perimetre(f, n) == 'ecoles' for f, n in zip(c2.f, c2.nomen)])
        eq_ec = c2[isec_c].groupby('code').deb.sum()
        fl = pd.DataFrame({'personnel_total': tot, 'personnel_ecoles': ec, 'energie_total': en_tot, 'energie_ecoles': en_ec,
                           'entretien_total': et_tot, 'entretien_ecoles': et_ec,
                           'equipement_total': eq_tot, 'equipement_ecoles': eq_ec}).fillna(0)
        fl.index.name = 'code'
        fl['annee'] = y
        flags.append(fl)
    flags = pd.concat(flags).reset_index().rename(columns={'index': 'code'})
    flags['part_personnel_ecoles'] = flags.personnel_ecoles / flags.personnel_total
    flags['part_energie_ecoles'] = flags.energie_ecoles / flags.energie_total
    flags['part_entretien_ecoles'] = flags.entretien_ecoles / flags.entretien_total
    flags['part_equipement_ecoles'] = flags.equipement_ecoles / flags.equipement_total
    wcsv(flags.assign(libelle=flags.code.map(LIBCOM)), 'A6_IDF_parts_imputees_aux_ecoles_personnel_energie_entretien.csv')

    w93 = w93.merge(flags, on=['code', 'annee'], how='left')
    keep = ['code', 'annee', 'eleves_rentree_N_1', 'F_bati', 'F_energie_fluides', 'F_entretien_maintenance', 'F_nettoyage',
            'F_personnel', 'F_total', 'I_total', 'I_bati', 'I_batiments', 'I_avances_sur_travaux', 'I_terrains_amenagements',
            'R_subventions_investissement_recues', 'part_personnel_ecoles', 'part_energie_ecoles', 'part_entretien_ecoles']
    d93 = w93[keep].copy()
    d93['libelle'] = d93.code.map(LIBCOM)
    for c in ['F_bati', 'F_energie_fluides', 'F_entretien_maintenance', 'F_nettoyage', 'F_personnel', 'F_total', 'I_total',
              'I_bati', 'R_subventions_investissement_recues']:
        d93[c + '_par_eleve'] = d93[c] / d93.eleves_rentree_N_1
    wcsv(d93, 'A4_93_communes_par_annee.csv')

    # moyenne 2023-2025 (somme des dépenses / somme des élèves) et 2021-2025
    def moy(d, ys, suffix):
        s = d[d.annee.isin(ys)].groupby(['code', 'libelle'])[['eleves_rentree_N_1', 'F_bati', 'F_energie_fluides',
                                                              'F_entretien_maintenance', 'F_personnel', 'F_total',
                                                              'I_total', 'I_bati', 'R_subventions_investissement_recues']].sum()
        o = pd.DataFrame(index=s.index)
        for c in ['F_bati', 'F_energie_fluides', 'F_entretien_maintenance', 'F_personnel', 'F_total', 'I_total', 'I_bati',
                  'R_subventions_investissement_recues']:
            o[c + suffix] = s[c] / s.eleves_rentree_N_1
        return o
    m3 = moy(d93, [2023, 2024, 2025], '_moy2023_2025')
    m5 = moy(d93, YEARS, '_moy2021_2025')
    a25 = d93[d93.annee == 2025].set_index(['code', 'libelle'])
    flag25 = a25[['eleves_rentree_N_1', 'part_personnel_ecoles', 'part_energie_ecoles', 'part_entretien_ecoles',
                  'I_bati_par_eleve', 'F_bati_par_eleve', 'F_energie_fluides_par_eleve']]
    flag25.columns = [c + '_2025' if not c.startswith('eleves') else 'eleves_rentree2024' for c in flag25.columns]
    # années 2023-2025 par commune pour l'investissement
    piv = d93[d93.annee.isin(YEARS)].pivot_table(index=['code', 'libelle'], columns='annee', values='I_total_par_eleve')
    piv.columns = [f'I_total_par_eleve_{c}' for c in piv.columns]
    disp = flag25.join(m3).join(m5).join(piv).reset_index()
    disp['alerte'] = ''
    disp.loc[disp.part_personnel_ecoles_2025 < 0.10, 'alerte'] += 'personnel des écoles < 10 % du personnel communal ; '
    disp.loc[disp.part_energie_ecoles_2025 < 0.10, 'alerte'] += 'énergie des écoles < 10 % de l\'énergie communale ; '
    disp.loc[disp.part_entretien_ecoles_2025 < 0.05, 'alerte'] += 'entretien des écoles < 5 % de l\'entretien communal ; '
    disp = disp.sort_values('I_total_moy2023_2025', ascending=False)
    wcsv(disp, 'A4b_93_dispersion_communale_2023-2025.csv')
    print(disp.to_string())

    # ---- Paris : détail BP / budgets d'arrondissement
    p = e[e.dep == '75']
    pd_ = p.groupby(['annee', 'cbudg', 'sous_perim', 'cat']).montant.sum().div(1e6).round(3).reset_index()
    wcsv(pd_, 'A7_Paris_detail_budget_sousfonction_categorie.csv')
    # fluides des budgets d'arrondissement (à comparer au tableau n° 17 du rapport de la CRC, 2025)
    esa = p[(p.cbudg != '1') & p.compte.str.startswith(('60611', '60612', '60613'))].groupby(['annee', 'compte']).montant.sum().unstack()
    print('Paris, budgets d\'arrondissement, fluides des écoles (€) :')
    print(esa.round(2))
    esa.reset_index().to_csv(os.path.join(OUT, 'A7b_Paris_ESA_fluides_ecoles.csv'), sep=';', index=False, encoding='utf-8-sig')
    return syn, disp, rep


if __name__ == '__main__':
    main()
