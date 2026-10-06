# Recherche de l'origine possible des "64 M EUR" d'investissement 2024 de Paris (analyse, par. 3.1)
import sys, pandas as pd
sys.stdout.reconfigure(encoding='utf-8')
BR = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/A_ecoles/brut/"
for y in (2024, 2025):
    q = pd.read_csv(BR + f'DGFiP_{y}_Q1_communes_75_92_93_94_fonction2_budget_fonction_compte_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
    for c in ['obnetdeb','obnetcre','oobdeb','oobcre']: q[c] = pd.to_numeric(q[c])
    p = q[q.categ=='PARIS'].copy()
    p['sf'] = p.fonction.map(lambda f: ('2'+f[3:]) if (len(f)>=3 and f[:3] in ('902','932')) else f)
    c = p.compte
    inv = c.str.startswith(('20','21','23'))
    ecol = p.sf.str.startswith(('20','21','28','29')) | (p.sf=='2')
    print(y, 'Paris par sous-fonction, debit reel 20/21/23 (M EUR):')
    g = p[inv].assign(dr=lambda d: d.obnetdeb-d.oobdeb).groupby('sf').dr.sum()/1e6
    print(g.round(2).to_dict())
    base = p[inv & ecol]
    print('  debit reel ecoles', round((base.obnetdeb-base.oobdeb).sum()/1e6,2))
    print('  debit total (reel+ordre) ecoles', round(base.obnetdeb.sum()/1e6,2))
    print('  net des credits reels ecoles', round(((base.obnetdeb-base.oobdeb)-(base.obnetcre-base.oobcre)).sum()/1e6,2))
    b2 = p[inv & (ecol | p.sf.str.startswith('24'))]
    print('  + cites scolaires (24)', round((b2.obnetdeb-b2.oobdeb).sum()/1e6,2))
    allf2 = p[inv]
    print('  toute la fonction 2', round((allf2.obnetdeb-allf2.oobdeb).sum()/1e6,2))
    q4 = pd.read_csv(BR + f'DGFiP_{y}_Q4_communes_75_92_93_94_comptes_1675_235_marches_partenariat_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
    for c2 in ['obnetdeb','obnetcre','oobdeb','oobcre']: q4[c2] = pd.to_numeric(q4[c2])
    q4p = q4[q4.categ=='PARIS']
    print('  Q4 Paris:', q4p[['lbudg','fonction','compte','obnetdeb','oobdeb','obnetcre','oobcre']].to_string())
