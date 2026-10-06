# Series par collegien du public 2016-2025 (93, Paris) ; raccord 2015-2018 (ancien jeu) sur 2019
import sys, pandas as pd, numpy as np
sys.stdout.reconfigure(encoding='utf-8')
SRC = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/B_colleges/sources/"
new = pd.read_csv(SRC+'DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
new['eleves'] = pd.to_numeric(new.eleves); new['r'] = new.rentree_scolaire.str[:4].astype(int)
new = new[new.secteur=='PUBLIC'].pivot_table(index='code_dept', columns='r', values='eleves', aggfunc='sum')
old = pd.read_csv(SRC+'DEPP_fr-en-effectifs-second-degre_obsolete_par_dep_type_secteur_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
old['eleves'] = pd.to_numeric(old.eleves); old['r'] = old.annee_scolaire.str[:4].astype(int)
print(old.type_d_etablissement.unique(), old.secteur_d_enseignement.unique())
old = old[(old.type_d_etablissement=='COLLEGE') & (old.secteur_d_enseignement=='Public')]
old['dep'] = old.code_departement.str.lstrip('0').str.zfill(2)
old = old.pivot_table(index='dep', columns='r', values='eleves', aggfunc='sum')
r = pd.read_csv('v09_series.csv', sep=';', index_col=[0,1])
for dep, key in [('93', 93), ('75', 75)]:
    o = old.loc[dep]; n = new.loc[dep]
    k = n[2019] / o[2019]
    rent = {y: o[y]*k for y in range(2015, 2019)}
    rent.update({y: n[y] for y in range(2019, 2026)})
    print(dep, 'ancien jeu', o.to_dict(), 'nouveau 2019', n[2019], 'coef', round(k,4))
    ev = (o[2019]/o[2015]) * (n[2025]/n[2019]) - 1
    print(dep, 'evolution 2015-2025 raccordee', round(100*ev,2), '%')
    s = r.loc[key]
    pe = {}
    for y in range(2016, 2026):
        den = 2/3*rent[y-1] + 1/3*rent[y]
        tot = s.loc[y,'equip'] + s.loc[y,'sub'] + s.loc[y,'cap'] + (s.loc[y,'cites'] if dep=='93' else 0)
        pe[y] = (tot*1e6/den, den, tot, (s.loc[y,'equip'] + s.loc[y,'sub'] + s.loc[y,'cap'] + s.loc[y,'cites'])*1e6/den)
    df = pd.DataFrame(pe, index=['pe','den','M','pe_cites']).T
    print(df.round(1).to_string())
    print(dep, 'moyenne 2016-2025', round(df.M.sum()*1e6/df.den.sum(),1), 'avec cites', round((df.pe_cites*df.den).sum()/df.den.sum(),1), ' 2022-2025', round(df.loc[2022:2025].M.sum()*1e6/df.loc[2022:2025].den.sum(),1))
    globals()['df'+dep] = df
print('ratio 93/Paris par annee (Paris sans cites) :', (df93.pe/df75.pe).round(2).to_dict())
