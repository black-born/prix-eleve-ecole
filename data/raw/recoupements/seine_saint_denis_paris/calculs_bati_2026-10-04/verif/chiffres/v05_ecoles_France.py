# Recalcul independant de la moyenne "France, communes a comptabilite fonctionnelle" (ecoles), 2023-2025
# Appariement des eleves : code_commune_insee du fichier DEPP (et non l'annuaire), ramene a la commune (COG 2026).
import sys, pandas as pd, numpy as np, glob
sys.stdout.reconfigure(encoding='utf-8')
BR = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/A_ecoles/brut/"
COG = pd.read_csv(r"C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/INSEE_COG2026_v_commune_2026.csv", dtype=str)
PARENT = {r.COM: r.COMPARENT for r in COG.itertuples() if r.TYPECOM in ('COMD','COMA','ARM') and isinstance(r.COMPARENT,str)}
def norm(c):
    if not isinstance(c, str) or not c: return None
    if c.startswith('751') and len(c)==5: return '75056'
    if c.startswith('6938'): return '69123'
    if c.startswith('132') and len(c)==5 and 1 <= int(c[3:]) <= 16: return '13055'
    return PARENT.get(c, c)
eff = pd.read_csv(BR + 'DEPP_effectifs_par_ecole_rentrees2020-2025_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
eff = eff[eff.secteur=='PUBLIC'].copy()
eff['n'] = pd.to_numeric(eff.nombre_total_eleves).fillna(0)
ann = pd.read_csv(BR + 'MEN_annuaire_education_ecoles_UAI_commune_API.csv', sep=';', dtype=str, encoding='utf-8-sig').drop_duplicates('identifiant_de_l_etablissement').set_index('identifiant_de_l_etablissement').code_commune
# NB : le champ code_commune_insee du fichier DEPP contient en fait le code postal (ex. Argenteuil 95100) : appariement par l'annuaire
eff['code'] = eff.numero_ecole.map(ann).map(norm)
for r in ['2022','2023','2024']:
    x = eff[eff.rentree_scolaire==r]
    print('rentree', r, 'eleves publics', int(x.n.sum()), 'non apparies par l annuaire', int(x[x.code.isna()].n.sum()))
print('eleves sans code commune :', eff[eff.code.isna()].n.sum())
el = eff.groupby(['code','rentree_scolaire']).n.sum().unstack().fillna(0)
def code_dgfip(categ, nd, ins):
    if categ == 'PARIS': return '75056'
    if not isinstance(ins,str) or not isinstance(nd,str) or not ins: return None
    return norm(('97'+ins) if nd.startswith('1') else (nd[1:]+ins))
def cat(c):
    if c.startswith('6'):
        if c.startswith(('66','675','676','68')): return None
        if c.startswith(('621','631','633','64')): return 'pers'
        if c == '6152' or c.startswith(('61521','61522','6156','6283','60631','6061','60621','6132','614','616')): return 'fbati'
        return 'fautre'
    if c[:2] in ('20','21','23'):
        if c.startswith(('236','237','238','211','212','2171','2172','2311','2312','2131','2132','2135','2138','214','2173','2174','2181','2313','2314','2317','235')):
            return 'ibati'
        return 'iautre'
    return None
tot = {}
for y in (2023, 2024, 2025):
    parts = []
    a = pd.read_csv(glob.glob(BR+f'DGFiP_{y}_Q3_*.csv')[0], sep=';', dtype=str, encoding='utf-8-sig')
    parts.append(a)
    b = pd.read_csv(glob.glob(BR+f'DGFiP_{y}_Q3b_*.csv')[0], sep=';', dtype=str, encoding='utf-8-sig')
    b['f'] = b.fonction.map(lambda x: x[2:] if x.startswith(('902','932')) else x)
    b = b[b.nomen.str.startswith('M14') & ~b.f.str.startswith('252')]
    parts.append(b)
    c = pd.read_csv(glob.glob(BR+f'DGFiP_{y}_Q3c_*.csv')[0], sep=';', dtype=str, encoding='utf-8-sig')
    parts.append(c)
    q = pd.concat(parts, ignore_index=True)
    for k in ['obnetdeb','obnetcre','oobdeb','oobcre']: q[k] = pd.to_numeric(q[k]).fillna(0)
    q['deb'] = q.obnetdeb - q.oobdeb; q['cre'] = q.obnetcre - q.oobcre
    q['code'] = [code_dgfip(a_, b_, c_) for a_, b_, c_ in zip(q.categ, q.ndept, q.insee)]
    q['cat'] = q.compte.map(cat)
    q['m'] = np.where(q.cat.isin(['pers','fbati','fautre']), q.deb - q.cre, np.where(q.cat.isin(['ibati','iautre']), q.deb, 0.0))
    print(y, 'montant sans code (insee vide) M EUR:', round(q[q.code.isna() & q.cat.notna()].m.sum()/1e6,1), 'dont invest', round(q[q.code.isna() & q.cat.isin(['ibati','iautre'])].m.sum()/1e6,1))
    w = q[q.code.notna() & q.cat.notna()].pivot_table(index='code', columns='cat', values='m', aggfunc='sum').fillna(0)
    w['F'] = w[['pers','fbati','fautre']].sum(axis=1)
    w['I'] = w[['ibati','iautre']].sum(axis=1)
    w['el'] = el.reindex(w.index)[str(y-1)].fillna(0)
    cv = w[(w.F > 0) & (w.el > 0)]
    tot[y] = cv[['pers','fbati','I','ibati','el']].sum()
    tot[y]['nb'] = len(cv)
    print(y, 'communes couvertes', len(cv), 'eleves', int(cv.el.sum()), 'I/el', round(cv.I.sum()/cv.el.sum(),1), 'Ibati/el', round(cv.ibati.sum()/cv.el.sum(),1), 'fbati/el', round(cv.fbati.sum()/cv.el.sum(),1), 'pers/el', round(cv.pers.sum()/cv.el.sum(),1))
T = pd.DataFrame(tot).T
print('Moyenne 2023-2025 France : I', round(T.I.sum()/T.el.sum(),1), 'Ibati', round(T.ibati.sum()/T.el.sum(),1), 'Fbati', round(T.fbati.sum()/T.el.sum(),1), 'pers', round(T.pers.sum()/T.el.sum(),1))
print('eleves publics totaux rentree 2024 (DEPP, toutes communes):', int(eff[eff.rentree_scolaire=='2024'].n.sum()), ' part couverte 2025:', round(T.loc[2025,'el']/eff[eff.rentree_scolaire=='2024'].n.sum(),3))
