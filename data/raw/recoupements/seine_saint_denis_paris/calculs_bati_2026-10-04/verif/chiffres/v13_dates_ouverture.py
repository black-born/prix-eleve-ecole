# Dates d'ouverture (annuaire geolocalise MEN) : part au 01/05/1965, ecoles et lycees publics ouverts de Paris et du 93
import sys, pandas as pd
sys.stdout.reconfigure(encoding='utf-8')
d = pd.read_csv(r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/D_bati/sources/MEN_geoloc_etablissements_075_093_API.csv", sep=';', dtype=str, encoding='utf-8-sig')
print(d.secteur_public_prive_libe.value_counts().to_dict(), d.etat_etablissement_libe.value_counts().to_dict())
d = d[(d.secteur_public_prive_libe=='Public') & (d.etat_etablissement_libe=='OUVERT')]
n = d.nature_uai.astype(int)
cat = pd.Series('autre', index=d.index)
cat[n.between(100, 199)] = 'école'
cat[n == 340] = 'collège'
cat[n.isin([300, 301, 302, 306, 307, 320])] = 'lycée'
d['cat'] = cat
print(d.groupby(['code_departement','cat']).size())
for (dep, c), s in d[d.cat!='autre'].groupby(['code_departement','cat']):
    print(dep, c, len(s), '01/05/1965 :', round(100*(s.date_ouverture=='1965-05-01').mean(),1), '% ; depuis 2000 :', int((s.date_ouverture>='2000-01-01').sum()))
print(d[d.cat=='autre'].nature_uai_libe.value_counts().head(15))
