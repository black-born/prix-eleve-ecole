# Dispersion communale du 93 (investissement ecoles 2023-2025), parts imputees aux ecoles (energie, personnel, equipement)
import sys, pandas as pd, numpy as np, glob
sys.stdout.reconfigure(encoding='utf-8')
BR = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/A_ecoles/brut/"
COG = pd.read_csv(r"C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/INSEE_COG2026_v_commune_2026.csv", dtype=str)
PARENT = {r.COM: r.COMPARENT for r in COG.itertuples() if r.TYPECOM in ('COMD','COMA','ARM') and isinstance(r.COMPARENT,str)}
LIB = COG[COG.TYPECOM=='COM'].set_index('COM').LIBELLE.to_dict()
def norm(c):
    if not isinstance(c,str) or not c: return None
    if c.startswith('751') and len(c)==5: return '75056'
    return PARENT.get(c, c)
eff = pd.read_csv(BR+'DEPP_effectifs_par_ecole_rentrees2020-2025_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
eff = eff[eff.secteur=='PUBLIC'].copy(); eff['n'] = pd.to_numeric(eff.nombre_total_eleves).fillna(0)
ann = pd.read_csv(BR+'MEN_annuaire_education_ecoles_UAI_commune_API.csv', sep=';', dtype=str, encoding='utf-8-sig').drop_duplicates('identifiant_de_l_etablissement').set_index('identifiant_de_l_etablissement').code_commune
eff['code'] = eff.numero_ecole.map(ann).map(norm)
e93 = eff[eff.code_departement.isin(['93','093'])]
print('93 eleves non apparies par rentree:', e93[e93.code.isna()].groupby('rentree_scolaire').n.sum().to_dict())
el = e93.groupby(['code','rentree_scolaire']).n.sum().unstack().fillna(0)
def sf(f): return ('2'+f[3:]) if (len(f)>=3 and f[:3] in ('902','932')) else f
inv = {}; 
for y in range(2021, 2026):
    q = pd.read_csv(glob.glob(BR+f'DGFiP_{y}_Q1_*.csv')[0], sep=';', dtype=str, encoding='utf-8-sig')
    for k in ['obnetdeb','obnetcre','oobdeb','oobcre']: q[k] = pd.to_numeric(q[k]).fillna(0)
    q = q[q.ndept=='093']
    q['code'] = (q.ndept.str[1:] + q.insee).map(norm)
    q['f'] = q.fonction.map(sf)
    ec = q.f.str.startswith(('20','21','28','29')) | (q.f=='2') | ((q.nomen=='M14') & q.f.str.startswith('25') & ~q.f.str.startswith('252'))
    m = ec & q.compte.str.startswith(('20','21','23'))
    inv[y] = (q[m].obnetdeb - q[m].oobdeb).groupby(q[m].code).sum()
I = pd.DataFrame(inv).fillna(0)
d = pd.DataFrame({'inv': I[[2023,2024,2025]].sum(axis=1), 'el': el.reindex(I.index)[['2022','2023','2024']].sum(axis=1), 'el24': el.reindex(I.index)['2024']})
d['pe'] = d.inv/d.el
d['lib'] = d.index.map(LIB)
d = d.sort_values('pe')
print(len(d), 'communes ; total', round(d.inv.sum()/d.el.sum(),1))
print(d[['lib','el24','pe']].round(0).to_string())
# mediane ponderee (eleves 2024) : premiere valeur ou poids cumule >= 50 %
w = d.el24/d.el24.sum(); cw = w.cumsum()
print('mediane ponderee', round(d.pe[cw >= 0.5].iloc[0],1), 'P10', round(d.pe[cw>=0.1].iloc[0],1), 'P90', round(d.pe[cw>=0.9].iloc[0],1))
print('mediane simple', round(d.pe.median(),1))
above = d[d.pe > 624.3]
print('communes > Paris (624):', len(above), 'part eleves 2024', round(above.el24.sum()/d.el24.sum(),3))
above2 = d[d.pe > 837]
print('communes > 837:', len(above2), round(above2.el24.sum()/d.el24.sum(),3), ' > 879:', len(d[d.pe>879]), round(d[d.pe>879].el24.sum()/d.el24.sum(),3))
below = d[d.pe <= 624.3]; print('communes sous Paris:', len(below), int(below.el24.sum()), list(below.lib))
