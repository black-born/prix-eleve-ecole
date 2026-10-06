# Recalcul independant (sans reutiliser les scripts A) des depenses "ecoles" des communes de Paris et du 93
# Sources : extractions DGFiP Q1 (fonction 2, par budget, fonction, compte) 2021-2025 ; DEPP effectifs par ecole.
import sys, pandas as pd, numpy as np
sys.stdout.reconfigure(encoding='utf-8')
BR = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/A_ecoles/brut/"
def sousfonction(f):
    f = str(f)
    if len(f) >= 3 and (f.startswith('902') or f.startswith('932')):
        r = f[3:]
        return '2' + r if r else '2'
    return f
def est_ecole(sf, nomen):
    if sf == '2': return True
    if sf.startswith('20') or sf.startswith('21') or sf.startswith('28') or sf == '29' or sf.startswith('29'):
        return True
    if nomen == 'M14' and sf.startswith('25') and not sf.startswith('252'):
        return True
    return False
eff = pd.read_csv(BR + 'DEPP_effectifs_par_ecole_rentrees2020-2025_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
eff['n'] = pd.to_numeric(eff.nombre_total_eleves)
eff['cl'] = pd.to_numeric(eff.nombre_total_classes)
eff = eff[eff.secteur == 'PUBLIC']
el = eff.groupby(['rentree_scolaire','code_departement']).n.sum()
cl = eff.groupby(['rentree_scolaire','code_departement']).cl.sum()
res = {}
for y in range(2021, 2026):
    q = pd.read_csv(BR + f'DGFiP_{y}_Q1_communes_75_92_93_94_fonction2_budget_fonction_compte_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
    for c in ['obnetdeb','obnetcre','oobdeb','oobcre']: q[c] = pd.to_numeric(q[c])
    q['sf'] = q.fonction.map(sousfonction)
    q = q[[est_ecole(s, n) for s, n in zip(q.sf, q.nomen)]]
    q['deb_r'] = q.obnetdeb - q.oobdeb
    q['cre_r'] = q.obnetcre - q.oobcre
    q['net'] = q.deb_r - q.cre_r
    c = q.compte
    inv = c.str.startswith('20') | c.str.startswith('21') | c.str.startswith('23')
    pers = c.str.startswith('621') | c.str.startswith('631') | c.str.startswith('633') | c.str.startswith('64')
    bati_f = (c.str.startswith('6152') | c.str.startswith('6156') | c.str.startswith('6283') | c.str.startswith('60631')
              | c.str.startswith('6061') | c.str.startswith('60621') | c.str.startswith('6132') | c.str.startswith('614') | c.str.startswith('616'))
    bati_f_strict = bati_f & ~(c.str.startswith('61523') | c.str.startswith('61524') | c.str.startswith('61528'))
    energie = c.str.startswith('6061') | c.str.startswith('60621')
    fonct = c.str.startswith('6') & ~c.str.startswith('66') & ~c.str.startswith('675') & ~c.str.startswith('676') & ~c.str.startswith('68')
    sub13 = c.str.startswith('13') & ~c.str.startswith('139')
    # bati investissement
    bat_prefixes = ('2313','2314','2131','2135','2138','214','2173','2174','2181','2317','235','236','237','238','211','212','2171','2172','2311','2312')
    ibati = c.map(lambda x: x.startswith(bat_prefixes))
    for d in ['075','093']:
        m = q.ndept == d
        rent = str(y-1)
        n = el.get((rent, d[1:]), np.nan)
        if np.isnan(n): n = el.get((rent, d), np.nan)
        res[(d,y)] = dict(
            eleves=n,
            inv=q[m & inv].deb_r.sum(), inv_net=(q[m & inv].deb_r.sum() - q[m & inv].cre_r.sum()),
            inv_bp=q[m & inv & (q.cbudg=='1')].deb_r.sum(),
            ibati=q[m & inv & ibati].deb_r.sum(),
            pers=q[m & pers].net.sum(), batif=q[m & bati_f].net.sum(), batif_strict=q[m & bati_f_strict].net.sum(),
            energie=q[m & energie].net.sum(), fonct=q[m & fonct].net.sum(),
            sub=-(q[m & sub13].net.sum()),
            classes=cl.get((rent, d[1:]), np.nan))
r = pd.DataFrame(res).T
r.index.names = ['dept','annee']
pd.set_option('display.width', 250)
out = r.copy()
for k in ['inv','inv_net','inv_bp','ibati','pers','batif','batif_strict','energie','fonct','sub']:
    out[k+'_pe'] = r[k]/r.eleves
print((r[['eleves','inv','inv_bp','ibati','pers','batif','energie','fonct','sub']]/[1,1e6,1e6,1e6,1e6,1e6,1e6,1e6,1e6]).round(2))
print(out[[c for c in out.columns if c.endswith('_pe')]].round(0))
for d in ['075','093']:
    s = r.loc[d].loc[2023:2025]
    print(d, 'moyenne 2023-2025 :', {k: round(s[k].sum()/s.eleves.sum(),1) for k in ['inv','inv_net','ibati','pers','batif','batif_strict','energie','fonct','sub']},
          'inv par classe', round(s.inv.sum()/s.classes.sum(),0))
    s5 = r.loc[d]
    print(d, 'moyenne 2021-2025 inv :', round(s5.inv.sum()/s5.eleves.sum(),1))
rat = r.loc['093'].inv/r.loc['093'].eleves / (r.loc['075'].inv/r.loc['075'].eleves)
print('rapport 93/Paris par annee', rat.round(3).to_dict())
s93 = r.loc['093'].loc[2023:2025]; s75 = r.loc['075'].loc[2023:2025]
print('rapport moyen 23-25', (s93.inv.sum()/s93.eleves.sum())/(s75.inv.sum()/s75.eleves.sum()))
