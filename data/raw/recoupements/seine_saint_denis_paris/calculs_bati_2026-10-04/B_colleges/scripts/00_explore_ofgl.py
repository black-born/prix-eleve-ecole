import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 500)
SRC = 'C:/Users/chret/Documents/EtatEcole/data/raw/collectivites/OFGL_departements_fonctionnelle_fonction2_2022-2025.csv'
df = pd.read_csv(SRC, sep=';', dtype=str, encoding='utf-8-sig')
df['montant'] = df['montant'].astype(float)
# Paris budgets annexes : which functions?
p = df[(df.dep_code=='75')]
print(p.groupby(['type_de_budget','fonction','exer'])['montant'].sum().unstack('exer').div(1e6).round(2).to_string())
print()
for dep in ['93','75']:
    sub = df[(df.dep_code==dep) & (df.type_de_budget=='Budget principal')]
    piv = sub.pivot_table(index=['fonction','nom_fonction','agregat'], columns='exer', values='montant', aggfunc='sum')
    print('=====', dep)
    print((piv/1e6).round(2).to_string())
