# Annee de construction des lycees publics (open data Region IDF, lycees-donnees-generales, maj 08/09/2026)
import sys, pandas as pd, numpy as np
sys.stdout.reconfigure(encoding='utf-8')
d = pd.read_csv(r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/raw/IDF_opendata_lycees-donnees-generales.csv", sep=';', dtype=str, encoding='utf-8-sig')
d = d[d.statut=='public'].copy()
d['a'] = pd.to_numeric(d.annee_construction, errors='coerce')
for dep, s in list(d.groupby('dep')) + [('IDF', d)]:
    a = s.a.dropna()
    print(dep, 'lycees publics', len(s), 'renseignes', len(a), 'manquants %', round(100*(1-len(a)/len(s)),1), 'mediane', a.median(), 'avant 1900', round(100*(a<1900).mean(),1), 'avant 1970', round(100*(a<1970).mean(),1), 'depuis 2000', round(100*(a>=2000).mean(),1))
