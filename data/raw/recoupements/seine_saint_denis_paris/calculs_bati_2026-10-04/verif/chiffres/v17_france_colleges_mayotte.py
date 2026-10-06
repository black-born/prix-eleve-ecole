# Moyenne "France" des colleges (OFGL, fonction 221, 2022-2025) : effet de Mayotte, present au denominateur
# (collegiens du public) mais sans depense en fonction 221 dans l'OFGL (la construction des colleges y releve de l'Etat).
import sys, pandas as pd
sys.stdout.reconfigure(encoding='utf-8')
O = r"C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/OFGL_departements_fonctionnelle_fonction2_2022-2025.csv"
D = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/B_colleges/sources/DEPP_effectifs_colleges_par_departement_secteur_rentree_API.csv"
o = pd.read_csv(O, sep=';', dtype=str, encoding='utf-8-sig'); o['montant'] = pd.to_numeric(o.montant)
print('Mayotte (976), fonctions presentes dans l OFGL :', sorted(o[o.dep_code=='976'].fonction.unique()))
b = o[(o.fonction=='221') & (o.type_de_budget=='Budget principal')]
eq = b[b.agregat=="Dépenses d'équipement"].montant.sum(); sb = b[b.agregat=="Subventions d'équipement versées"].montant.sum()
d = pd.read_csv(D, sep=';', dtype=str, encoding='utf-8-sig'); d['eleves'] = pd.to_numeric(d.eleves); d['r'] = d.rentree_scolaire.str[:4].astype(int)
pub = d[d.secteur=='PUBLIC'].pivot_table(index='code_dept', columns='r', values='eleves', aggfunc='sum')
COM = ['975','977','978','986','987','988']; CTU = ['2A','2B','972','973']
civ = lambda s: sum(2/3*s[y-1] + 1/3*s[y] for y in range(2022, 2026))
den_B = civ(pub[~pub.index.isin(COM+CTU)].sum()); den_sansMay = civ(pub[~pub.index.isin(COM+CTU+['976'])].sum())
print('denominateur B (avec Mayotte) :', round(den_B), '; sans Mayotte :', round(den_sansMay), '; collegiens de Mayotte :', round(den_B-den_sansMay))
print('equipement France : B', round(eq/den_B, 1), '-> sans Mayotte', round(eq/den_sansMay, 1))
print('subventions : B', round(sb/den_B, 1), '-> sans Mayotte', round(sb/den_sansMay, 1))
