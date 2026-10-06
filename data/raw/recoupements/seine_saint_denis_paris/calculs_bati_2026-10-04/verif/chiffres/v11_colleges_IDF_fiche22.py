# Classement IDF 2022-2025 (equipement + subventions OFGL + capital PPP DGFiP) et releves fiche 22 DEPP
import sys, pandas as pd, numpy as np, glob, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
O = r"C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/OFGL_departements_fonctionnelle_fonction2_2022-2025.csv"
SRC = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/B_colleges/sources/"
o = pd.read_csv(O, sep=';', dtype=str, encoding='utf-8-sig'); o['montant'] = pd.to_numeric(o.montant)
o = o[(o.fonction=='221') & (o.type_de_budget=='Budget principal')]
d = pd.read_csv(SRC+'DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv', sep=';', dtype=str, encoding='utf-8-sig')
d['eleves'] = pd.to_numeric(d.eleves); d['r'] = d.rentree_scolaire.str[:4].astype(int)
pub = d[d.secteur=='PUBLIC'].pivot_table(index='code_dept', columns='r', values='eleves', aggfunc='sum')
cap = {}
for y in range(2022, 2026):
    q = pd.read_csv(glob.glob(SRC+f'dgfip/DGFiP_{y}_IDF_departements_Paris_fonction2_dette16_par_compte_API.csv')[0], sep=';', dtype=str, encoding='utf-8-sig')
    for k in ['obnetdeb','oobdeb']: q[k] = pd.to_numeric(q[k]).fillna(0)
    q['f'] = q.fonction.fillna('').map(lambda f: f[2:] if f.startswith(('902','932','904','934')) and len(f)>3 else f)
    m = q.f.str.startswith('221') & q.compte.str.startswith('1675')
    for dep, v in (q[m].obnetdeb - q[m].oobdeb).groupby(q[m].ndept).sum().items(): cap[(dep[1:], y)] = v
for dep in ['92','94','77','93','91','78','95','75']:
    den = sum(2/3*pub.loc[dep, y-1] + 1/3*pub.loc[dep, y] for y in range(2022, 2026))
    eq = o[(o.dep_code==dep) & (o.agregat=="Dépenses d'équipement")].montant.sum()
    sb = o[(o.dep_code==dep) & (o.agregat=="Subventions d'équipement versées")].montant.sum()
    cp = sum(cap.get((dep, y), 0) for y in range(2022, 2026))
    print(dep, 'equip', round(eq/den), 'sub', round(sb/den), 'cap', round(cp/den), 'total', round((eq+sb+cp)/den))
# Fiche 22
X = r"C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/DEPP_GeoEcole2026_fiche22_depense_departements_regions_donnees.xlsx"
wb = openpyxl.load_workbook(X, data_only=True)
print(wb.sheetnames)
for sh in wb.sheetnames:
    ws = wb[sh]
    for row in (16, 29, 87, 104, 105, 106, 113):
        try:
            vals = [ws.cell(row=row, column=c).value for c in range(1, 5)]
        except Exception as e:
            vals = str(e)
        print(sh, row, vals)
