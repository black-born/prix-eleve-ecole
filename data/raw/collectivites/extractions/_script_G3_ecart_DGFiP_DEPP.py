# -*- coding: utf-8 -*-
"""
Tâche G3 (consulté le 2026-10-04) : écart entre la dépense communale reconstituée à partir des balances DGFiP 2025
et le compte de l'éducation de la DEPP (1er degré).

Lit UNIQUEMENT des fichiers bruts (dossier parent data/raw/collectivites/ et, pour l'IPS des écoles,
data/raw/etablissements/ips_ecoles_2024-2025.csv) ; écrit des CSV dérivés préfixés « G3_ » dans extractions/.
Aucun fichier brut n'est modifié. Montants en millions d'euros courants (M€) sauf mention contraire.

Étapes :
  1. appariement école (UAI) -> commune Insee, y compris les écoles fermées depuis (absentes de l'annuaire actuel) ;
  2. couverture de la comptabilité fonctionnelle, hors COM (975, 986, 987, 988) ;
  3. extrapolation aux communes non couvertes selon plusieurs méthodes (moyenne, classes de taille, strate de
     population, méthode « à la DEPP » décrite par la Cour des comptes) ;
  4. recouvrement avec les GFP (écoles gérées par l'intercommunalité) ;
  5. quote-part d'administration générale selon la règle du Dossier DEPP n° 206 ;
  6. tableau de passage DGFiP -> DEPP.

Usage : python _script_G3_ecart_DGFiP_DEPP.py
"""
import os
import re
import unicodedata

import numpy as np
import openpyxl
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.dirname(HERE)
ETAB = os.path.join(os.path.dirname(RAW), 'etablissements')
DEPPDIR = os.path.join(os.path.dirname(RAW), 'depp_compte_education')
OUT = HERE
COM = ('975', '986', '987', '988')       # collectivités d'outre-mer hors champ (Saint-Pierre-et-Miquelon, Wallis-et-Futuna,
                                         # Polynésie française, Nouvelle-Calédonie) : hors compte de l'éducation et hors DGFiP


def raw(name):
    return os.path.join(RAW, name)


_WB = {}


def xl(path, sheet, cell):
    if path not in _WB:
        _WB[path] = openpyxl.load_workbook(path, data_only=True)
    return _WB[path][sheet][cell].value


# ---------------------------------------------------------------------------------------------------------------
# Outils
# ---------------------------------------------------------------------------------------------------------------
def insee_code(nd, ins):
    """Code commune Insee à partir des champs DGFiP ndept (3 caractères) et insee (3 caractères)."""
    if nd.startswith('1'):          # DROM : 101 Guadeloupe ... 106 Mayotte -> 971.. 976..
        return '97' + ins
    return nd[1:] + ins


def norm_plm(c):
    """Arrondissements de Paris, Lyon, Marseille -> commune."""
    if not isinstance(c, str):
        return c
    if c.startswith('751') and len(c) == 5:
        return '75056'
    if c.startswith('6938'):
        return '69123'
    if c in MARSEILLE_ARR:
        return '13055'
    return c


MARSEILLE_ARR = {f'132{i:02d}' for i in range(1, 17)}


def norm_lib(s):
    """Libellé de commune normalisé : majuscules sans accents, ponctuation -> espace, ST/STE développés."""
    if not isinstance(s, str):
        return None
    for a, b in (('Œ', 'OE'), ('œ', 'oe'), ('Æ', 'AE'), ('æ', 'ae')):
        s = s.replace(a, b)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii').upper()
    s = re.sub(r"[^A-Z0-9]+", ' ', s).strip()
    s = re.sub(r'\bSTE\b', 'SAINTE', s)
    s = re.sub(r'\bST\b', 'SAINT', s)
    return re.sub(r'\s+', ' ', s)


def dep_of(code):
    if not isinstance(code, str):
        return None
    return code[:3] if code.startswith('97') else code[:2]


# ---------------------------------------------------------------------------------------------------------------
# 1. Dépense « écoles » des communes à comptabilité fonctionnelle (DGFiP 2025, budgets principaux, opérations réelles)
# ---------------------------------------------------------------------------------------------------------------
def depense_ecoles_communes():
    dep = {}
    for kind, fname in [('fonct', 'DGFiP_balances_nature-fonction_2025_communes_ecoles_fonct_par_commune_API.csv'),
                        ('invest', 'DGFiP_balances_nature-fonction_2025_communes_ecoles_invest_par_commune_API.csv')]:
        f = pd.read_csv(raw(fname), sep=';', dtype={'ndept': str, 'insee': str, 'siren': str}, encoding='utf-8-sig')
        for c in ['obnetdeb', 'obnetcre', 'oobdeb', 'oobcre']:
            f[c] = f[c].fillna(0)
        f['code'] = [insee_code(a, b) for a, b in zip(f.ndept, f.insee)]
        f['m'] = (f.obnetdeb - f.oobdeb) - (f.obnetcre - f.oobcre) if kind == 'fonct' else (f.obnetdeb - f.oobdeb)
        dep[kind] = f.groupby('code').m.sum()
    dep = pd.DataFrame(dep).fillna(0)
    dep['total'] = dep.fonct + dep.invest
    return dep


def depense_totale_communes_fonctionnelles():
    """Dépense totale (toutes fonctions) des communes présentes dans la balance fonctionnelle (F hors 66/675/676/68 ;
    I = 20, 21, 23 hors 204), par commune."""
    tot = {}
    for kind, fname in [('fonct', 'DGFiP_balances_nature-fonction_2025_communes_BP_total_toutes_fonctions_fonct_par_commune_API.csv'),
                        ('invest', 'DGFiP_balances_nature-fonction_2025_communes_BP_total_toutes_fonctions_invest_par_commune_API.csv')]:
        f = pd.read_csv(raw(fname), sep=';', dtype={'ndept': str, 'insee': str, 'siren': str}, encoding='utf-8-sig')
        for c in ['obnetdeb', 'obnetcre', 'oobdeb', 'oobcre']:
            f[c] = f[c].fillna(0)
        f['code'] = [insee_code(a, b) for a, b in zip(f.ndept, f.insee)]
        f['m'] = (f.obnetdeb - f.oobdeb) - (f.obnetcre - f.oobcre) if kind == 'fonct' else (f.obnetdeb - f.oobdeb)
        tot[kind] = f.groupby('code').m.sum()
    tot = pd.DataFrame(tot).fillna(0)
    tot['total'] = tot.fonct + tot.invest
    return tot


# ---------------------------------------------------------------------------------------------------------------
# 2. Appariement école -> commune, y compris les écoles fermées
# ---------------------------------------------------------------------------------------------------------------
def appariement():
    e = pd.read_csv(raw('MEN_effectifs_par_ecole_rentrees2024-2025_libelles_communes_API.csv'), sep=';', dtype=str,
                    encoding='utf-8-sig')
    e['n'] = pd.to_numeric(e.nombre_total_eleves)
    e['annee'] = e.rentree_scolaire.str[:4].astype(int)
    pub = e[e.secteur.str.upper().str.startswith('PUBLIC')].copy()
    a = pd.read_csv(raw('MEN_annuaire_education_ecoles_UAI_commune_extrait_API.csv'), sep=';', dtype=str,
                    encoding='utf-8-sig').drop_duplicates('identifiant_de_l_etablissement').set_index('identifiant_de_l_etablissement')
    pub['code'] = pub.numero_ecole.map(a.code_commune)
    pub['methode'] = np.where(pub.code.notna(), '1 annuaire actuel (UAI)', None)

    # (2) IPS des écoles 2024-2025 (DEPP) : code Insee de la commune par UAI, écoles ouvertes à la rentrée 2024
    ips = pd.read_csv(os.path.join(ETAB, 'ips_ecoles_2024-2025.csv'), sep=';', dtype=str, encoding='utf-8-sig')
    ips = ips.drop_duplicates('uai').set_index('uai').code_insee_de_la_commune
    m = pub.code.isna() & pub.numero_ecole.isin(ips.index)
    pub.loc[m, 'code'] = pub.loc[m, 'numero_ecole'].map(ips)
    pub.loc[m, 'methode'] = '2 IPS écoles 2024-2025 (UAI)'

    # (3) libellé de commune du jeu d'effectifs + département -> code, appris sur les écoles appariées
    pub['lib'] = pub.commune.map(norm_lib)
    pub['dep'] = pub.code_departement.str.upper()
    ok = pub[pub.code.notna()]
    learn = (ok.groupby(['dep', 'lib']).code.agg(lambda s: s.map(norm_plm).value_counts().index[0]))
    m = pub.code.isna()
    keys = list(zip(pub.loc[m, 'dep'], pub.loc[m, 'lib']))
    found = [learn.get(k) for k in keys]
    pub.loc[m, 'code'] = found
    pub.loc[m & pub.code.notna(), 'methode'] = '3 libellé commune + département (écoles ouvertes de la même commune)'

    # (4) Code officiel géographique 2026 (Insee) : communes, communes déléguées et associées (-> commune parente)
    cog = pd.read_csv(raw('INSEE_COG2026_v_commune_2026.csv'), dtype=str)
    cog['lib'] = cog.LIBELLE.map(norm_lib)
    cog['dep2'] = cog.DEP.fillna('')
    cog['cible'] = np.where(cog.TYPECOM.isin(['COMD', 'COMA']), cog.COMPARENT, cog.COM)
    cog['cible'] = np.where(cog.TYPECOM == 'ARM', cog.COMPARENT, cog.cible)
    # département des communes déléguées : celui de la commune parente
    depmap = cog[cog.TYPECOM == 'COM'].set_index('COM').DEP
    cog['dep2'] = np.where(cog.dep2 == '', cog.cible.map(depmap), cog.dep2)
    cogk = cog.groupby(['dep2', 'lib']).cible.agg(lambda s: s.iloc[0] if s.nunique() == 1 else None)
    m = pub.code.isna()

    def depnorm(d):
        return d.zfill(2) if d.isdigit() and len(d) < 2 else d
    found = [cogk.get((depnorm(d), l)) for d, l in zip(pub.loc[m, 'dep'], pub.loc[m, 'lib'])]
    pub.loc[m, 'code'] = found
    pub.loc[m & pub.code.notna(), 'methode'] = '4 libellé + département dans le COG 2026 (Insee)'

    # (5) libellés historiques (COG depuis 1943) : seulement si le libellé désigne une commune encore existante
    hist = pd.read_csv(raw('INSEE_COG2026_v_commune_depuis_1943.csv'), dtype=str)
    hist['lib'] = hist.LIBELLE.map(norm_lib)
    hist['dep2'] = hist.COM.map(dep_of)
    actuels = set(cog.loc[cog.TYPECOM == 'COM', 'COM'])
    hist = hist[hist.COM.isin(actuels)]
    hk = hist.groupby(['dep2', 'lib']).COM.agg(lambda s: s.iloc[0] if s.nunique() == 1 else None)
    m = pub.code.isna()
    found = [hk.get((depnorm(d), l)) for d, l in zip(pub.loc[m, 'dep'], pub.loc[m, 'lib'])]
    pub.loc[m, 'code'] = found
    pub.loc[m & pub.code.notna(), 'methode'] = '5 libellé historique (COG depuis 1943)'
    pub['methode'] = pub.methode.fillna('6 non apparié')
    pub['code'] = pub.code.map(norm_plm)
    return pub


# ---------------------------------------------------------------------------------------------------------------
# 3. Principales étapes
# ---------------------------------------------------------------------------------------------------------------
def main():
    res = []          # (bloc, indicateur, valeur, unité, source / emplacement)

    def add(bloc, ind, val, unit, src):
        res.append((bloc, ind, val, unit, src))

    dep = depense_ecoles_communes()
    tot_fonc = depense_totale_communes_fonctionnelles()
    pub = appariement()

    # ---- statistiques d'appariement
    st = pub.groupby(['methode', 'annee']).n.sum().unstack().fillna(0)
    st['annee_civile_2025'] = 2 / 3 * st[2024] + 1 / 3 * st[2025]
    st['nb_uai'] = pub.groupby('methode').numero_ecole.nunique()
    st.reset_index().to_csv(os.path.join(OUT, 'G3_appariement_ecoles_communes.csv'), sep=';', index=False,
                            encoding='utf-8-sig')

    pub['com_outremer'] = pub.code_departement.isin(COM) | pub.code.fillna('').str[:3].isin(COM)
    hc = pub[~pub.com_outremer & pub.code.notna()]
    pc = hc.pivot_table(index='code', columns='annee', values='n', aggfunc='sum').fillna(0)
    pc['civil2025'] = 2 / 3 * pc[2024] + 1 / 3 * pc[2025]
    n_com = pub[pub.com_outremer].groupby('annee').n.sum()
    add('A. Effectifs', 'Élèves du public, rentrée 2024, jeu fr-en-ecoles-effectifs-nb_classes (toutes écoles)', pub[pub.annee == 2024].n.sum(), 'élèves', 'MEN open data')
    add('A. Effectifs', 'Élèves du public, rentrée 2025', pub[pub.annee == 2025].n.sum(), 'élèves', 'MEN open data')
    add('A. Effectifs', 'dont COM 975, 986, 987, 988 (exclus), rentrée 2024 | rentrée 2025', f"{n_com.get(2024, 0):.0f} | {n_com.get(2025, 0):.0f}", 'élèves', 'MEN open data')
    na = pub[~pub.com_outremer & pub.code.isna()]
    add('A. Effectifs', 'Élèves du public non appariés à une commune après les 5 méthodes (hors COM), année civile 2025',
        2 / 3 * na[na.annee == 2024].n.sum() + 1 / 3 * na[na.annee == 2025].n.sum(), 'élèves', 'calcul')
    tot = pc.civil2025.sum()
    add('A. Effectifs', 'Élèves du public appariés, hors COM, année civile 2025 (2/3 R2024 + 1/3 R2025)', tot, 'élèves', 'calcul')
    e_all = pd.read_csv(raw('MEN_effectifs_par_ecole_rentrees2024-2025_libelles_communes_API.csv'), sep=';', dtype=str,
                        encoding='utf-8-sig')
    e_all['n'] = pd.to_numeric(e_all.nombre_total_eleves)
    pv = e_all[e_all.secteur.str.upper().str.startswith('PRIVE') & ~e_all.code_departement.isin(COM)]
    priv = 2 / 3 * pv[pv.rentree_scolaire.str[:4] == '2024'].n.sum() + 1 / 3 * pv[pv.rentree_scolaire.str[:4] == '2025'].n.sum()
    add('A. Effectifs', 'Élèves du privé sous contrat, hors COM, année civile 2025', priv, 'élèves', 'MEN open data')

    # ---- couverture
    pc['couverte'] = pc.index.isin(dep.index[dep.fonct > 0])
    pc['dans_balance_fonctionnelle'] = pc.index.isin(tot_fonc.index)
    cov = pc.loc[pc.couverte, 'civil2025'].sum()
    j = dep.join(pc[['civil2025']], how='left').fillna({'civil2025': 0})
    jc = j[j.civil2025 > 0]
    dep_cov_total = dep.total.sum() / 1e6
    dep_cov_eleves = jc.total.sum() / 1e6
    cout_moyen = jc.total.sum() / cov
    add('B. Couverture', 'Communes ayant au moins un élève du public (hors COM)', len(pc), 'communes', 'calcul')
    add('B. Couverture', 'dont communes couvertes (dépense de fonctionnement « écoles » > 0 en 2025)', int(pc.couverte.sum()), 'communes', 'DGFiP 2025')
    add('B. Couverture', 'Élèves du public des communes couvertes', cov, 'élèves', 'calcul')
    add('B. Couverture', 'Part des élèves du public couverts (hors COM)', cov / tot, 'ratio', 'calcul')
    add('B. Couverture', 'Élèves du public des communes non couvertes', tot - cov, 'élèves', 'calcul')
    add('B. Couverture', 'dont communes présentes dans la balance fonctionnelle mais sans dépense « écoles » (écoles gérées ailleurs)',
        pc.loc[~pc.couverte & pc.dans_balance_fonctionnelle, 'civil2025'].sum(), 'élèves', 'calcul')
    add('B. Couverture', 'Dépense « écoles » des communes couvertes (toutes, y.c. sans élève du public)', dep_cov_total, 'M€', 'DGFiP 2025')
    add('B. Couverture', 'dont communes couvertes ayant des élèves du public', dep_cov_eleves, 'M€', 'DGFiP 2025')
    add('B. Couverture', 'Dépense moyenne par élève du public des communes couvertes', cout_moyen, '€', 'calcul')
    nonc = tot - cov

    # ---- population, strates (OFGL base communes 2025)
    of = pd.read_csv(raw('OFGL_base_communes_2025_BP_population_EPCI_depenses_API.csv'), sep=';', dtype=str,
                     encoding='utf-8-sig')
    of['montant'] = pd.to_numeric(of.montant)
    of['ptot'] = pd.to_numeric(of.ptot)
    ofw = of.pivot_table(index='com_code', columns='agregat', values='montant', aggfunc='sum').fillna(0)
    info = of.drop_duplicates('com_code').set_index('com_code')[['com_name', 'ptot', 'epci_code', 'epci_name', 'dep_code']]
    ofw = ofw.join(info)
    ofw['dep_tot_hors_chfi'] = ofw['Dépenses totales hors remb'] - ofw['Charges financières']
    pc = pc.join(ofw[['ptot', 'epci_code', 'dep_tot_hors_chfi']], how='left')
    j2 = j.join(ofw[['ptot', 'dep_tot_hors_chfi']], how='left')

    # ---- extrapolations
    ext = []
    # M1 : moyenne (méthode OFGL Cap sur n° 21)
    m1 = nonc * cout_moyen / 1e6
    ext.append(('M1 moyenne des communes couvertes (méthode OFGL)', cout_moyen, m1))
    # M2 : 8 classes d'élèves du public (comme l'extraction précédente)
    bins = [0, 100, 200, 300, 500, 1000, 2000, 5000, 1e9]
    jc = jc.assign(classe=pd.cut(jc.civil2025, bins, right=False))
    g = jc.groupby('classe', observed=True).agg(nb=('total', 'size'), el=('civil2025', 'sum'), d=('total', 'sum'))
    g['cout'] = g.d / g.el
    unc = pc[~pc.couverte]
    gu = unc.groupby(pd.cut(unc.civil2025, bins, right=False), observed=True).civil2025.agg(['size', 'sum'])
    tab = g.join(gu.rename(columns={'size': 'nb_nc', 'sum': 'el_nc'}))
    tab['extrapolation'] = tab.el_nc * tab.cout / 1e6
    m2 = tab.extrapolation.sum()
    ext.append(("M2 8 classes d'élèves du public (coût de la classe appliqué aux non couverts)", m2 / nonc * 1e6, m2))
    # M3 : 3 classes regroupées (< 300 ; 300-999 ; >= 1 000)
    bins3 = [0, 300, 1000, 1e9]
    g3 = jc.groupby(pd.cut(jc.civil2025, bins3, right=False), observed=True).agg(el=('civil2025', 'sum'), d=('total', 'sum'))
    gu3 = unc.groupby(pd.cut(unc.civil2025, bins3, right=False), observed=True).civil2025.sum()
    m3 = float((gu3 * g3.d / g3.el).sum() / 1e6)
    ext.append(("M3 3 classes regroupées (< 300 ; 300-999 ; >= 1 000 élèves)", m3 / nonc * 1e6, m3))
    # M4 : coût par élève des communes couvertes de 3 500 à 9 999 habitants
    s = jc.join(ofw[['ptot']], how='left')
    s4 = s[(s.ptot >= 3500) & (s.ptot < 10000)]
    c4 = s4.total.sum() / s4.civil2025.sum()
    m4 = nonc * c4 / 1e6
    ext.append(('M4 coût par élève des communes couvertes de 3 500 à 9 999 habitants', c4, m4))
    # M5 : méthode « à la DEPP » (Cour des comptes, mai 2025, p. 31-32) : part de la dépense « écoles » dans la dépense
    # totale des communes de 3 500 à 9 999 hab. (couvertes), appliquée à la dépense totale des communes non couvertes
    j2c = j2[(j2.ptot >= 3500) & (j2.ptot < 10000) & j2.index.isin(dep.index[dep.fonct > 0])]
    ratio5 = j2c.total.sum() / (j2c.dep_tot_hors_chfi.sum())
    noncov_communes = ofw[~ofw.index.isin(dep.index[dep.fonct > 0]) & ~ofw.dep_code.isin(COM)]
    m5 = ratio5 * noncov_communes.dep_tot_hors_chfi.sum() / 1e6
    ext.append(("M5 « à la DEPP » : part « écoles » des communes de 3 500-9 999 hab. x dépense totale des communes non couvertes",
                m5 / nonc * 1e6, m5))
    add('C. Extrapolation', 'Part de la dépense « écoles » dans la dépense totale (hors charges financières), communes couvertes de 3 500 à 9 999 hab.', ratio5, 'ratio', 'DGFiP 2025 / OFGL 2025')
    add('C. Extrapolation', 'Dépense totale (hors charges financières, BP) des communes non couvertes', noncov_communes.dep_tot_hors_chfi.sum() / 1e6, 'M€', 'OFGL base communes 2025')
    add('C. Extrapolation', 'Nombre de communes non couvertes (OFGL 2025, hors COM)', len(noncov_communes), 'communes', 'OFGL base communes 2025')
    # M5bis : montant DEPP des petites collectivités cité par la Cour des comptes (4,2 Md€, année non précisée,
    # vraisemblablement 2022 ou 2023), porté en 2025 avec la dépense totale des communes < 3 500 hab. (DGCL 4F, F1 Série l. 228)
    f6x = raw('DGCL_CLC2026_4F_Ventilation_fonctionnelle_CG25.xlsx')
    pc22, pc23, pc25 = xl(f6x, 'F1 Série', 'K228'), xl(f6x, 'F1 Série', 'L228'), xl(f6x, 'F1 Série', 'N228')
    m5b_22 = 4200 * pc25 / pc22
    m5b_23 = 4200 * pc25 / pc23
    add('C. Extrapolation', 'Dépense totale des communes < 3 500 hab. (DGCL 4F, F1 Série l. 228) : 2022 | 2023 | 2025',
        f'{pc22:.1f} | {pc23:.1f} | {pc25:.1f}', 'M€', 'DGCL CLC 2026')
    ext.append(('M5bis DEPP (Cour des comptes 2025 : 4,2 Md€) porté en 2025, si base 2022', m5b_22 / nonc * 1e6, m5b_22))
    ext.append(('M5bis DEPP (Cour des comptes 2025 : 4,2 Md€) porté en 2025, si base 2023', m5b_23 / nonc * 1e6, m5b_23))
    # M6 : facteur OFGL Cap sur n° 21 (1/0,62), pour mémoire
    m6 = dep_cov_total * (1 / 0.62 - 1)
    ext.append(('M6 pour mémoire : facteur OFGL 2023 (1/0,62), couverture 2022', None, m6))
    for lab, c, v in ext:
        add('C. Extrapolation', lab + ' : coût par élève non couvert retenu (€)', c, '€', 'calcul')
        add('C. Extrapolation', lab + ' : dépense extrapolée des communes non couvertes', v, 'M€', 'calcul')
    tab = tab.reset_index()
    tab['classe'] = tab.classe.astype(str)
    tab.to_csv(os.path.join(OUT, 'G3_extrapolation_par_classe_taille.csv'), sep=';', index=False, encoding='utf-8-sig')

    # ---- distribution par strate de population des communes non couvertes
    pc['strate'] = pd.cut(pc.ptot, [0, 500, 1000, 2000, 3500, 10000, 1e9], right=False,
                          labels=['< 500', '500-999', '1 000-1 999', '2 000-3 499', '3 500-9 999', '>= 10 000'])
    dist = pc.groupby(['couverte', 'strate'], observed=True).agg(communes=('civil2025', 'size'), eleves=('civil2025', 'sum')).reset_index()
    dist.to_csv(os.path.join(OUT, 'G3_eleves_par_strate_et_couverture.csv'), sep=';', index=False, encoding='utf-8-sig')
    add('C. Extrapolation', 'Élèves du public non couverts sans population OFGL (communes absentes de la base OFGL 2025)',
        pc.loc[~pc.couverte & pc.ptot.isna(), 'civil2025'].sum(), 'élèves', 'calcul')

    # ---- 4. GFP : dépense « écoles » par GFP et part relative aux communes non couvertes
    gf = pd.read_csv(raw('DGFiP_balances_nature-fonction_2025_GFP_ecoles_par_GFP_et_compte_API.csv'), sep=';',
                     dtype={'compte': str, 'siren': str, 'ndept': str, 'insee': str}, encoding='utf-8-sig')
    for c in ['obnetdeb', 'obnetcre', 'oobdeb', 'oobcre']:
        gf[c] = gf[c].fillna(0)
    isF = gf.compte.str.startswith('6') & ~gf.compte.str.startswith(('66', '675', '676', '68'))
    isI = gf.compte.str[:2].isin(['20', '21', '23']) & ~gf.compte.str.startswith('204')
    gf['m'] = np.where(isF, (gf.obnetdeb - gf.oobdeb) - (gf.obnetcre - gf.oobcre), 0.0) + \
        np.where(isI, gf.obnetdeb - gf.oobdeb, 0.0)
    gfs = gf.groupby(['categ', 'siren']).m.sum()
    add('D. GFP', 'Dépense « écoles » des GFP, ML et EPT (fonctions 20, 21, 28, 29 ; BP), total', gfs.sum() / 1e6, 'M€', 'DGFiP 2025')
    el_epci = pc.groupby(['epci_code', 'couverte']).civil2025.sum().unstack().fillna(0)
    el_epci.columns = ['el_non_couverts' if not c else 'el_couverts' for c in el_epci.columns]
    gfd = gfs.reset_index().set_index('siren').join(el_epci, how='left').fillna(0)
    gfd['part_nc'] = np.where((gfd.el_couverts + gfd.el_non_couverts) > 0,
                              gfd.el_non_couverts / (gfd.el_couverts + gfd.el_non_couverts), 0)
    gfd.loc[gfd.categ.isin(['ML', 'EPT']), 'part_nc'] = 0.0
    gfd['m_nc'] = gfd.m * gfd.part_nc
    add('D. GFP', 'dont imputable aux élèves des communes non couvertes (au prorata des élèves de chaque GFP)', gfd.m_nc.sum() / 1e6, 'M€', 'calcul')
    add('D. GFP', 'dont imputable aux élèves des communes couvertes', (gfd.m - gfd.m_nc).sum() / 1e6, 'M€', 'calcul')
    add('D. GFP', 'GFP non rattachés à un EPCI de la base OFGL (ML, EPT ou SIREN absent)', gfd.loc[(gfd.el_couverts + gfd.el_non_couverts) == 0, 'm'].sum() / 1e6, 'M€', 'calcul')
    gfd.reset_index().to_csv(os.path.join(OUT, 'G3_GFP_ecoles_par_GFP_part_non_couverte.csv'), sep=';', index=False, encoding='utf-8-sig')
    gfp_total = gfs.sum() / 1e6
    gfp_nc = gfd.m_nc.sum() / 1e6

    # ---- 5. quote-part d'administration générale (Dossier DEPP n° 206, p. 34 imprimée)
    tf = pd.read_csv(raw('DGFiP_balances_nature-fonction_2025_communes_BP_toutes_fonctions_agrege_API.csv'), sep=';',
                     dtype={'fonction': str, 'compte': str}, encoding='utf-8-sig', keep_default_na=False, na_values=[''])
    for c in ['obnetdeb', 'obnetcre', 'oobdeb', 'oobcre']:
        tf[c] = pd.to_numeric(tf[c]).fillna(0)
    tf['fonction'] = tf.fonction.fillna('')
    cpt = tf.compte
    F = cpt.str.startswith('6') & ~cpt.str.startswith(('66', '675', '676', '68'))
    I = cpt.str[:2].isin(['20', '21', '23']) & ~cpt.str.startswith('204')
    tf['F'] = np.where(F, (tf.obnetdeb - tf.oobdeb) - (tf.obnetcre - tf.oobcre), 0.0)
    tf['I'] = np.where(I, (tf.obnetdeb - tf.oobdeb) - np.where(cpt.str[:3].isin(['236', '237', '238']), tf.obnetcre - tf.oobcre, 0.0), 0.0)
    tf['f'] = [x[2:] if (x.startswith('90') or x.startswith('93')) else x for x in tf.fonction]
    T = (tf.F.sum() + tf.I.sum()) / 1e6
    E2 = (tf.loc[tf.f.str.startswith('2'), 'F'].sum() + tf.loc[tf.f.str.startswith('2'), 'I'].sum()) / 1e6
    ag_mask = tf.f.isin(['0', '02', '020', '021', '028'])     # A00 « Administration générale (indéterminé) » (table DGCL M14/M57)
    ag020F = tf.loc[tf.f == '020', 'F'].sum() / 1e6
    agF = tf.loc[ag_mask, 'F'].sum() / 1e6
    agFI = (tf.loc[ag_mask, 'F'].sum() + tf.loc[ag_mask, 'I'].sum()) / 1e6
    sgFI = (tf.loc[tf.f.str.startswith('0'), 'F'].sum() + tf.loc[tf.f.str.startswith('0'), 'I'].sum()) / 1e6
    ratio_ag = E2 / T
    share_ecoles = dep_cov_total / E2
    add('E. Administration générale', 'Communes à comptabilité fonctionnelle : dépense totale toutes fonctions (BP, F + I)', T, 'M€', 'DGFiP 2025')
    add('E. Administration générale', 'dont fonction 2 « Enseignement »', E2, 'M€', 'DGFiP 2025')
    add('E. Administration générale', 'Ratio dépense d\'éducation identifiée / dépense totale (règle DEPP)', ratio_ag, 'ratio', 'calcul')
    add('E. Administration générale', 'Administration générale, fonction 020, fonctionnement', ag020F, 'M€', 'DGFiP 2025')
    add('E. Administration générale', 'Administration générale indéterminée (0, 02, 020, 021, 028), fonctionnement', agF, 'M€', 'DGFiP 2025')
    add('E. Administration générale', 'Administration générale indéterminée (0, 02, 020, 021, 028), F + I', agFI, 'M€', 'DGFiP 2025')
    add('E. Administration générale', 'Services généraux (fonction 0 entière), F + I', sgFI, 'M€', 'DGFiP 2025')
    qp = {'bas (020, F)': ratio_ag * ag020F, 'central (A00, F)': ratio_ag * agF, 'haut (A00, F + I)': ratio_ag * agFI}
    for k, v in qp.items():
        add('E. Administration générale', f'Quote-part d\'administration générale, communes couvertes, variante {k}', v, 'M€', 'calcul')
        add('E. Administration générale', f'dont part « écoles » (au prorata écoles / fonction 2 = {share_ecoles:.3f}), variante {k}', v * share_ecoles, 'M€', 'calcul')
    pd.DataFrame([(k, v, v * share_ecoles) for k, v in qp.items()],
                 columns=['variante', 'quote_part_AG_M€', 'dont_ecoles_M€']).to_csv(
        os.path.join(OUT, 'G3_quote_part_administration_generale_2025.csv'), sep=';', index=False, encoding='utf-8-sig')

    # ---- 6. DEPP : repères
    rers = raw('DEPP_RERS2026_10-04_producteurs_education_donnees.xlsx')
    ecoles_pub = xl(rers, '10.04 Tableau 2', 'E9')
    ecoles_priv = xl(rers, '10.04 Tableau 2', 'E19')
    menages_pub = xl(rers, '10.04 Tableau 2', 'G9')
    ni = raw('DEPP_NI_26-42_compte_education_2025_donnees.xlsx')
    die24, die25 = xl(ni, 'Figure 3bis', 'E10'), xl(ni, 'Figure 3bis', 'F10')
    com24, com25 = xl(ni, 'Figure 2', 'B7'), xl(ni, 'Figure 2', 'C7')
    ct1_25 = xl(ni, 'Figure 4', 'B33') / 100 * xl(ni, 'Figure 5', 'B32') * 1000
    ni25 = os.path.join(DEPPDIR, 'depp_ni_2025-52_compte_education_2024_donnees.xlsx')
    ct1_24p = xl(ni25, 'Figure 4', 'B33') / 100 * xl(ni25, 'Figure 5', 'B31') * 1000
    g_comm = (com25 * die25) / (com24 * die24) - 1
    g_ct1 = ct1_25 / ct1_24p - 1
    depp24 = ecoles_pub + ecoles_priv
    depp25 = depp24 * (1 + g_comm)
    add('F. DEPP', 'CT, financement final 2024p, écoles publiques (RERS 2026, 10.04 T2 E9)', ecoles_pub, 'M€', 'DEPP')
    add('F. DEPP', 'CT, financement final 2024p, écoles privées sous contrat (E19)', ecoles_priv, 'M€', 'DEPP')
    add('F. DEPP', 'Ménages, financement final 2024p, écoles publiques (G9)', menages_pub, 'M€', 'DEPP')
    add('F. DEPP', 'Croissance 2024-2025 du financement initial des communes (NI 26.42, Fig. 2 B7/C7 x Fig. 3bis E10/F10)', g_comm, 'ratio', 'DEPP')
    add('F. DEPP', 'Croissance 2024p-2025p du financement initial CT du 1er degré (NI 25.52 -> NI 26.42, Fig. 4 x Fig. 5)', g_ct1, 'ratio', 'DEPP')
    add('F. DEPP', 'CT, financement initial 1er degré 2025p (NI 26.42 : 38,41 % x 60,0 Md€)', ct1_25, 'M€', 'DEPP')
    add('F. DEPP', 'Écoles publiques + privées, CT, financement final, porté en 2025 (x croissance des communes)', depp25, 'M€', 'calcul')

    # ---- 7. Tableau de passage
    synth = pd.read_csv(os.path.join(OUT, 'DGFiP_2025_enseignement_synthese_niveau_perimetre_BP.csv'), sep=';', encoding='utf-8-sig')
    base = float(synth.loc[(synth.niveau == 'Communes (y.c. Paris)') & (synth.perimetre == 'écoles (1er degré)'), 'total'].iloc[0])
    f6 = raw('DGCL_CLC2026_4F_Ventilation_fonctionnelle_CG25.xlsx')
    synd = xl(f6, 'F6 BA et Synd', 'D30')
    ba = xl(f6, 'F6 BA et Synd', 'D8')
    # recettes « familles » et fournitures, recalculées depuis la balance agrégée (fonction 2 et 81)
    ag = pd.read_csv(raw('DGFiP_balances_nature-fonction_2025_fonction2_et_81_agrege_API.csv'), sep=';', encoding='utf-8-sig',
                     dtype={'ctype': str, 'cstyp': str, 'cacti': str, 'cbudg': str, 'fonction': str, 'compte': str})
    for c in ['obnetdeb', 'obnetcre', 'oobdeb', 'oobcre']:
        ag[c] = ag[c].fillna(0)
    ag['f'] = [x[2:] if (x.startswith('90') or x.startswith('93')) else x for x in ag.fonction]
    ag['ecoles'] = ag.f.str[:2].isin(['20', '21', '28', '29'])
    ag['cred'] = (ag.obnetcre - ag.oobcre) - (ag.obnetdeb - ag.oobdeb)
    ag['debt'] = (ag.obnetdeb - ag.oobdeb) - (ag.obnetcre - ag.oobcre)
    famc = ag.compte.isin(['7067', '7066', '74881'])
    bp = ag.cbudg == '1'
    fam_cov = ag.loc[famc & bp & ag.ecoles & ag.categ.isin(['Commune', 'PARIS']), 'cred'].sum() / 1e6
    fam_gfp = ag.loc[famc & bp & ag.ecoles & ag.categ.isin(['GFP', 'ML', 'EPT']), 'cred'].sum() / 1e6
    fam_synd = ag.loc[famc & bp & ag.f.str.startswith('2') & (ag.categ == 'SYND'), 'cred'].sum() / 1e6
    fourn = ag.loc[ag.compte.str.startswith('6067') & bp & ag.ecoles & ag.categ.isin(['Commune', 'PARIS']), 'debt'].sum() / 1e6
    c6558 = ag.loc[ag.compte.str.startswith('6558') & bp & ag.ecoles & ag.categ.isin(['Commune', 'PARIS']), 'debt'].sum() / 1e6
    c65748 = ag.loc[ag.compte.str.startswith('65748') & bp & ag.ecoles & ag.categ.isin(['Commune', 'PARIS']), 'debt'].sum() / 1e6
    k_nc = nonc / cov                            # rapport élèves non couverts / couverts
    caisses = (631 - 434 - 148)                  # OFGL 2026, annexe 7A : dépenses totales - dotations et participations - ventes
    qpc = qp['central (A00, F)'] * share_ecoles
    lignes = []

    def L(etape, lib, val, note):
        lignes.append((etape, lib, round(float(val), 1) if val is not None else None, note))

    # Variante A : reconstitution comptable (sans quote-part d'administration générale)
    L('A0', 'DGFiP 2025 : communes couvertes, périmètre « écoles » (fonctions 20, 21x, 28x, 29), BP, F + I', base,
      'extractions/DGFiP_2025_enseignement_synthese_niveau_perimetre_BP.csv')
    L('A1', '+ communes non couvertes, extrapolation M1 (coût moyen par élève, hors COM, écoles fermées appariées)', m1, 'bloc C')
    L('A2', '+ GFP, part imputable aux élèves des communes couvertes (la part des non couverts est réputée comprise dans M1)', gfp_total - gfp_nc, 'bloc D')
    L('A3', "+ syndicats (code activité 03/23) : réputés compris dans M1 (SIVOS des petites communes)", 0.0,
      f'pour mémoire {synd:.1f} M€ (DGCL 4F, F6 D30)')
    L('A4', '+ budgets annexes à code activité 03/23 (tous niveaux, toutes collectivités)', ba, 'DGCL 4F, F6 D8')
    L('A5', '+ caisses des écoles : dépenses non financées par les communes ni par les familles', caisses,
      'OFGL rapport 2026, annexe 7A (631 - 434 - 148)')
    L('A6', '- participations des familles (7067, 7066, 74881) des communes couvertes', -fam_cov, 'balance agrégée, fonctions 20, 21, 28, 29')
    L('A7', '- participations des familles des GFP (périmètre écoles) et des syndicats (fonction 2)', -(fam_gfp + fam_synd), 'balance agrégée')
    L('A8', '- participations des familles des communes non couvertes (même montant par élève)', -fam_cov * k_nc, 'calcul')
    L('A9', '- fournitures scolaires (6067 ; activité « fournitures et livres », hors producteurs DEPP), y.c. extrapolation', -fourn * (1 + k_nc), 'calcul')
    totA = sum(v for e, _, v, _ in lignes if e.startswith('A') and v is not None)
    L('A=', 'TOTAL A : reconstitution comptable 2025 (net des familles, sans quote-part d\'administration générale)', totA, 'somme A0-A9')
    L("A'", "Sensibilité : si M1 ne couvre que la part communale, ajouter GFP non couverts et syndicats", gfp_nc + synd, 'bloc D + F6 D30')
    # Variante B : à la DEPP
    L('B1', 'Remplacer M1 par le bloc « petites communes » de la DEPP (4,2 Md€ cité par la Cour des comptes, porté en 2025, base 2022)', m5b_22 - m1, 'bloc C, M5bis')
    L('B2', '+ GFP imputables aux élèves des communes non couvertes', gfp_nc, 'bloc D')
    L('B3', '+ syndicats (code activité 03/23)', synd, 'DGCL 4F, F6 D30')
    L('B4', "+ quote-part d'administration générale des communes couvertes (règle du Dossier DEPP n° 206), variante centrale, part « écoles »", qpc, 'bloc E')
    totB = totA + (m5b_22 - m1) + gfp_nc + synd + qpc
    L('B=', 'TOTAL B : reconstitution « à la DEPP » 2025', totB, 'A= + B1 à B4')
    L('B-bas', "Variante basse de B : bloc petites communes M5 (ratio 2025 des communes de 3 500-9 999 hab.) et quote-part AG basse (020, F)",
      totA + (m5 - m1) + gfp_nc + synd + qp['bas (020, F)'] * share_ecoles, 'blocs C, D, E')
    L('B-haut', "Variante haute de B : bloc petites communes base 2022, quote-part AG haute (A00, F + I) appliquée aussi au bloc des petites communes",
      totA + (m5b_22 - m1) + gfp_nc + synd + qp['haut (A00, F + I)'] * share_ecoles + m5b_22 * qp['haut (A00, F + I)'] / E2, 'blocs C, D, E')
    L('P1', 'Pour mémoire : versements des communes couvertes identifiables vers le privé ou d\'autres communes (6558 + 65748, périmètre écoles), compris dans A0', c6558 + c65748,
      f'6558 = {c6558:.1f} ; 65748 = {c65748:.1f}')
    L('P2', 'Pour mémoire : DEPP, CT -> écoles privées sous contrat 2024p (forfait communal ; loi Goblet : pas d\'autre aide communale)', ecoles_priv, 'RERS 2026, 10.04 T2 E19')
    L('D1', 'DEPP : CT, écoles publiques + privées, financement final 2024p (RERS 2026, 10.04)', depp24, 'E9 + E19')
    L('D2', 'DEPP : même agrégat porté en 2025 (croissance du financement initial des communes, NI 26.42)', depp25, 'bloc F')
    L('D3', 'Pour mémoire : DEPP, CT, financement initial du 1er degré 2025p (y.c. transports, fournitures ; hors subventions reçues de l\'État)', ct1_25, 'NI 26.42, Fig. 4 B33 x Fig. 5 B32')
    L('R1', 'Écart D2 - TOTAL A (reconstitution comptable)', depp25 - totA, 'M€')
    L('R2', 'Écart D2 - TOTAL B (reconstitution « à la DEPP »)', depp25 - totB, 'M€')
    L('R3', 'Écart D2 - TOTAL A, par élève du public (5,38 M, année civile 2025)', (depp25 - totA) * 1e6 / tot, '€ par élève')
    L('R4', 'Écart D2 - TOTAL A, par élève du 1er degré public + privé sous contrat (année civile 2025)', (depp25 - totA) * 1e6 / (tot + priv), '€ par élève')
    L('R5', 'Écart D2 - TOTAL B, par élève du 1er degré public + privé sous contrat', (depp25 - totB) * 1e6 / (tot + priv), '€ par élève')
    pd.DataFrame(lignes, columns=['etape', 'libelle', 'M€', 'source_ou_note']).to_csv(
        os.path.join(OUT, 'G3_tableau_passage_DGFiP_DEPP_2025.csv'), sep=';', index=False, encoding='utf-8-sig')

    pd.DataFrame(res, columns=['bloc', 'indicateur', 'valeur', 'unite', 'source']).to_csv(
        os.path.join(OUT, 'G3_couverture_extrapolation_communes_2025_horsCOM.csv'), sep=';', index=False, encoding='utf-8-sig')
    return res, lignes


if __name__ == '__main__':
    r, l = main()
    for x in r:
        print(x)
    print()
    for x in l:
        print(x)
