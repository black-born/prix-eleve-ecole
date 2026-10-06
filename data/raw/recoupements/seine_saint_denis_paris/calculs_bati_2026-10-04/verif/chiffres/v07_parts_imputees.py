# Parts imputees aux fonctions "ecoles" : energie 2025 (Q2d), equipement 2023-2025 (Q2c), 93 et Paris
import sys, pandas as pd, numpy as np, glob
sys.stdout.reconfigure(encoding='utf-8')
BR = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/A_ecoles/brut/"
COG = pd.read_csv(r"C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/INSEE_COG2026_v_commune_2026.csv", dtype=str)
PARENT = {r.COM: r.COMPARENT for r in COG.itertuples() if r.TYPECOM in ('COMD','COMA','ARM') and isinstance(r.COMPARENT,str)}
LIB = COG[COG.TYPECOM=='COM'].set_index('COM').LIBELLE.to_dict()
def norm(c):
    if not isinstance(c,str) or not c: return None
    return PARENT.get(c, c)
def sf(f):
    f = '' if not isinstance(f,str) else f
    return ('2'+f[3:]) if (len(f)>=3 and f[:3] in ('902','932')) else f
def ecole(f): return f.startswith(('20','21','28','29')) or f == '2'
def rd(path):
    q = pd.read_csv(path, sep=';', dtype=str, encoding='utf-8-sig')
    for k in ['obnetdeb','obnetcre','oobdeb','oobcre']: q[k] = pd.to_numeric(q[k]).fillna(0)
    q['f'] = q.fonction.map(sf)
    return q
# Equipement : part des ecoles 2023-2025 (debit reel 20/21/23), tous budgets
eq = []
for y in (2023, 2024, 2025):
    q = rd(glob.glob(BR+f'DGFiP_{y}_Q2c_*.csv')[0]); q['y'] = y; eq.append(q)
q = pd.concat(eq)
q['dr'] = q.obnetdeb - q.oobdeb
for d in ['093','075']:
    s = q[q.ndept==d]
    e = s[s.f.map(ecole)].dr.sum(); t = s.dr.sum()
    print('part ecoles dans equipement 2023-2025', d, round(100*e/t,1), '%', round(e/1e6,1), round(t/1e6,1))
# NB : Q2c n'a pas la nomenclature -> en M14 les 25x ne sont pas comptes ici (2023 : quelques communes M14)
# Energie 2025 : part imputee aux ecoles par commune (93)
q = rd(glob.glob(BR+'DGFiP_2025_Q2d_*.csv')[0])
q = q[q.ndept=='093']
q['code'] = (q.ndept.str[1:] + q.insee.fillna('')).map(norm)
q['net'] = (q.obnetdeb-q.oobdeb)-(q.obnetcre-q.oobcre)
en = q[q.compte.str.startswith(('6061','60621'))]
# rattacher les budgets annexes sans insee via le siren ? on garde ceux qui ont un code
tot = en.groupby('code').net.sum(); eco = en[en.f.map(ecole)].groupby('code').net.sum()
part = (eco.reindex(tot.index).fillna(0)/tot).sort_values()
eff = pd.read_csv(BR+'DEPP_effectifs_par_ecole_rentrees2020-2025_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
eff = eff[(eff.secteur=='PUBLIC') & (eff.rentree_scolaire=='2024')].copy(); eff['n'] = pd.to_numeric(eff.nombre_total_eleves).fillna(0)
ann = pd.read_csv(BR+'MEN_annuaire_education_ecoles_UAI_commune_API.csv', sep=';', dtype=str, encoding='utf-8-sig').drop_duplicates('identifiant_de_l_etablissement').set_index('identifiant_de_l_etablissement').code_commune
eff['code'] = eff.numero_ecole.map(ann).map(norm)
el24 = eff.groupby('code').n.sum()
low = part[part < 0.10]
print('communes du 93 imputant < 10 % de leur energie aux ecoles en 2025 :', len(low))
for c, v in low.items(): print('  ', LIB.get(c, c), round(100*v,1), '%', int(el24.get(c,0)))
print('  eleves rentree 2024 (B1 = DEPP apparies) :', int(el24.reindex(low.index).fillna(0).sum()))
