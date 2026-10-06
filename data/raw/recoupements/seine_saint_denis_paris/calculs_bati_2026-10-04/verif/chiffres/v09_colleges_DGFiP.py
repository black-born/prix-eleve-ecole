# Recalcul independant (DGFiP) : series colleges 93 / Paris 2012-2025, PPP (1675, 6618, 235), energie
import sys, pandas as pd, numpy as np, glob
sys.stdout.reconfigure(encoding='utf-8')
SRC = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/B_colleges/sources/"
def sf(f):
    f = '' if not isinstance(f,str) else f
    return f[2:] if f.startswith(('902','932','904','934')) and len(f) > 3 else f
rows = {}
for y in range(2012, 2026):
    q = pd.read_csv(glob.glob(SRC+f'dgfip/DGFiP_{y}_IDF_departements_Paris_fonction2_dette16_par_compte_API.csv')[0], sep=';', dtype=str, encoding='utf-8-sig')
    for k in ['bedeb','becre','obnetdeb','obnetcre','onbdeb','onbcre','oobdeb','oobcre','sd','sc']: q[k] = pd.to_numeric(q[k]).fillna(0)
    q['f'] = q.fonction.map(sf)
    q['dr'] = q.obnetdeb - q.oobdeb; q['cr'] = q.obnetcre - q.oobcre
    for ent, m in [('93', q.ndept=='093'), ('75', (q.ndept=='075'))]:
        s = q[m]
        c = s.compte
        f221 = s.f.str.startswith('221')
        eq = f221 & c.str.startswith(('20','21','23')) & ~c.str.startswith(('204','2324'))
        # equipement OFGL-like : D20+D21+D23-D204-D2324 - C236-C237-C238
        equip = s[eq].dr.sum() - s[f221 & c.str.startswith(('236','237','238'))].cr.sum()
        sub = s[f221 & c.str.startswith(('204','2324'))].dr.sum()
        cap = s[f221 & c.str.startswith('1675')].dr.sum()
        p235 = s[f221 & c.str.startswith('235')].dr.sum()
        f24 = s.f.str.startswith('24') & c.str.startswith(('20','21','23'))
        cites = s[f24 & ~c.str.startswith(('204','2324'))].dr.sum() - s[f24 & c.str.startswith(('236','237','238'))].cr.sum() + s[f24 & c.str.startswith(('204','2324'))].dr.sum()
        interets = s[f221 & c.str.startswith('6618')].dr.sum() - s[f221 & c.str.startswith('6618')].cr.sum()
        energie = s[f221 & c.str.startswith(('60611','60612','60613','60621','60622'))]
        energie = (energie.dr - energie.cr).sum()
        all1675 = s[c.str.startswith('1675')]
        rows[(ent, y)] = dict(equip=equip/1e6, sub=sub/1e6, cap=cap/1e6, p235=p235/1e6, cites=cites/1e6, interets=interets/1e6, energie=energie/1e6,
                              be1675=all1675.becre.sum()/1e6, onbcre1675=all1675.onbcre.sum()/1e6, dr1675_all=all1675.dr.sum()/1e6, sc1675=all1675.sc.sum()/1e6)
r = pd.DataFrame(rows).T
pd.set_option('display.width', 250)
pass
r['bati'] = r['equip'] + r['sub'] + r['cap']
for ent in ['93','75']:
    s = r.loc[ent]
    print(ent, 'total 2012-2025 : equip', round(s.equip.sum(),1), 'sub', round(s['sub'].sum(),1), 'cap', round(s.cap.sum(),1), 'cites', round(s.cites.sum(),1), 'p235', round(s.p235.sum(),1), 'bati+cites', round((s.bati+s.cites).sum(),1), 'bati', round(s.bati.sum(),1), 'onbcre1675', round(s.onbcre1675.sum(),1), 'interets', round(s.interets.sum(),1))
    print(ent, 'moyenne 2022-2025 energie', round(s.loc[2022:2025].energie.mean(),2), 'interets', round(s.loc[2022:2025].interets.mean(),2), 'cap', s.loc[2022:2025].cap.round(2).to_dict())
r.to_csv('v09_series.csv', sep=';')
