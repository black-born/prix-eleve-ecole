# Personnel "ecoles" du 93 (2023-2025) selon la part du personnel communal imputee aux ecoles en 2025
import sys, pandas as pd, numpy as np, glob
sys.stdout.reconfigure(encoding='utf-8')
BR = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/A_ecoles/brut/"
COG = pd.read_csv(r"C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/INSEE_COG2026_v_commune_2026.csv", dtype=str)
PARENT = {r.COM: r.COMPARENT for r in COG.itertuples() if r.TYPECOM in ('COMD','COMA','ARM') and isinstance(r.COMPARENT,str)}
LIB = COG[COG.TYPECOM=='COM'].set_index('COM').LIBELLE.to_dict()
norm = lambda c: PARENT.get(c, c) if isinstance(c, str) and c else None
sf = lambda f: ('2'+f[3:]) if isinstance(f,str) and len(f)>=3 and f[:3] in ('902','932') else (f if isinstance(f,str) else '')
ecole = lambda f: f.startswith(('20','21','28','29')) or f == '2'
def rd(p):
    q = pd.read_csv(p, sep=';', dtype=str, encoding='utf-8-sig')
    for k in ['obnetdeb','obnetcre','oobdeb','oobcre']: q[k] = pd.to_numeric(q[k]).fillna(0)
    q = q[q.ndept=='093'].copy(); q['code'] = (q.ndept.str[1:] + q.insee.fillna('')).map(norm); q['f'] = q.fonction.map(sf)
    q['net'] = (q.obnetdeb-q.oobdeb)-(q.obnetcre-q.oobcre); return q
q2 = rd(glob.glob(BR+'DGFiP_2025_Q2a_*.csv')[0])
part = q2[q2.f.map(ecole)].groupby('code').net.sum() / q2.groupby('code').net.sum()
low = set(part[part < 0.10].index) - {'93'}
eff = pd.read_csv(BR+'DEPP_effectifs_par_ecole_rentrees2020-2025_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
eff = eff[eff.secteur=='PUBLIC'].copy(); eff['n'] = pd.to_numeric(eff.nombre_total_eleves).fillna(0)
ann = pd.read_csv(BR+'MEN_annuaire_education_ecoles_UAI_commune_API.csv', sep=';', dtype=str, encoding='utf-8-sig').drop_duplicates('identifiant_de_l_etablissement').set_index('identifiant_de_l_etablissement').code_commune
eff['code'] = eff.numero_ecole.map(ann).map(norm)
el = eff[eff.code_departement=='93'].groupby(['code','rentree_scolaire']).n.sum().unstack().fillna(0)
pers = {}
for y in (2023, 2024, 2025):
    q = rd(glob.glob(BR+f'DGFiP_{y}_Q1_*.csv')[0])
    m = q.f.map(ecole) & q.compte.str.startswith(('621','631','633','64'))
    pers[y] = q[m].groupby('code').net.sum()
P = pd.DataFrame(pers).fillna(0).sum(axis=1)
E = el.reindex(P.index)[['2022','2023','2024']].sum(axis=1)
grp = pd.Series(np.where(P.index.isin(low), 'impute < 10 % (2025)', 'autres'), index=P.index)
print('communes a faible imputation du personnel (2025) :', sorted(LIB.get(c, c) for c in low))
for g in ['impute < 10 % (2025)', 'autres']:
    s = grp == g
    print(g, 'communes', s.sum(), 'eleves 2024', int(el.reindex(P.index)['2024'][s].sum()), 'personnel par eleve 2023-2025', round(P[s].sum()/E[s].sum()))
print('ensemble', round(P.sum()/E.sum()))
autres = P[grp=='autres'].sum()/E[grp=='autres'].sum()
print('si toutes les communes etaient au niveau des "autres" :', round(autres))
