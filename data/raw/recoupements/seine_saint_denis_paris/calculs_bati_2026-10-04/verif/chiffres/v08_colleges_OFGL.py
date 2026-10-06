# Recalcul independant : equipement des colleges (fonction 221, OFGL) par collegien du public, 2022-2025
import sys, pandas as pd, numpy as np
sys.stdout.reconfigure(encoding='utf-8')
O = r"C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/OFGL_departements_fonctionnelle_fonction2_2022-2025.csv"
D = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/B_colleges/sources/DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv"
o = pd.read_csv(O, sep=';', dtype=str, encoding='utf-8-sig')
o['montant'] = pd.to_numeric(o.montant)
o = o[(o.fonction=='221') & (o.type_de_budget=='Budget principal')]
d = pd.read_csv(D, sep=';', dtype=str, encoding='utf-8-sig')
d['eleves'] = pd.to_numeric(d.eleves); d['r'] = d.rentree_scolaire.str[:4].astype(int)
pub = d[d.secteur=='PUBLIC'].pivot_table(index='code_dept', columns='r', values='eleves', aggfunc='sum')
def den(dep, y):
    return 2/3*pub.loc[dep, y-1] + 1/3*pub.loc[dep, y]
codes = {'93':'93', '75':'75', '92':'92', '94':'94', '77':'77', '91':'91', '78':'78', '95':'95'}
for ag in ["Dépenses d'équipement", "Subventions d'équipement versées", "Dépenses de fonctionnement", "Charges financières"]:
    s = o[o.agregat==ag]
    for dep in ['93','75']:
        m = s[s.dep_code==dep]
        tot = m.montant.sum(); dd = sum(den(dep, y) for y in range(2022,2026))
        print(ag, dep, 'M EUR par annee', m.groupby('exer').montant.sum().div(1e6).round(2).to_dict(), 'total', round(tot/1e6,1), 'den', round(dd), '->', round(tot/dd,1))
    # France : DEPT + PARIS + ML ; denominateur : departements presents ; Lyon : 69 (Rhone + ML)
    tot = s.montant.sum()
    deps = [c for c in pub.index if c not in ('971','972','973','974','976','975','977','978','986','987','988')]
    # CTU : Corse 2A/2B ? Guyane 973, Martinique 972 sont des CTU absentes de l'OFGL ; Mayotte 976 ?
    present = set(s.dep_code.unique())
    print('  departements presents dans OFGL', len(present), sorted(present)[-12:])
    dd = sum(den(dep, y) for y in range(2022,2026) for dep in pub.index if dep in present or (dep=='69'))
    print(ag, 'France total', round(tot/1e6,1), 'den', round(dd), '->', round(tot/dd,1))
