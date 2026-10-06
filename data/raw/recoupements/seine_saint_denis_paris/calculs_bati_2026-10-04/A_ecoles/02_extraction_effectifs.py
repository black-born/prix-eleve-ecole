# -*- coding: utf-8 -*-
"""
Tâche A - effectifs d'élèves par école (DEPP, data.education.gouv.fr, jeu « fr-en-ecoles-effectifs-nb_classes »),
rentrées 2020 à 2025, tous secteurs (filtrage du public au calcul). Consulté le 2026-10-04.
Attention : le champ code_commune_insee de ce jeu contient en réalité le code postal (libellé « Code postal ») ;
l'appariement à la commune Insee se fait au calcul (03_calculs.py).
"""
import os
import sys
import requests

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'brut')
os.makedirs(OUT, exist_ok=True)

URL = 'https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ecoles-effectifs-nb_classes/exports/csv'
params = {
    'select': 'rentree_scolaire,numero_ecole,secteur,code_departement,departement,code_commune_insee,commune,'
              'denomination_principale,patronyme,rep,rep_plus,nombre_total_classes,nombre_total_eleves',
    'where': 'year(rentree_scolaire)>=2020',
    'delimiter': ';',
}
path = os.path.join(OUT, 'DEPP_effectifs_par_ecole_rentrees2020-2025_API.csv')
r = requests.get(URL, params=params, timeout=1800, headers={'Accept-Encoding': 'gzip'})
r.raise_for_status()
open(path, 'wb').write(r.content)
print(len(r.content) / 1e6, 'Mo', r.url)
with open(os.path.join(OUT, '_urls_requetes.txt'), 'a', encoding='utf-8') as f:
    f.write(f'{os.path.basename(path)}\t{r.url}\n')

# annuaire de l'éducation (UAI -> code commune Insee), version du jour
URL2 = 'https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-annuaire-education/exports/csv'
p2 = {'select': 'identifiant_de_l_etablissement,type_etablissement,statut_public_prive,code_commune,nom_commune,'
                'code_departement,etat,date_ouverture',
      'where': 'type_etablissement="Ecole"', 'delimiter': ';'}
path2 = os.path.join(OUT, 'MEN_annuaire_education_ecoles_UAI_commune_API.csv')
r2 = requests.get(URL2, params=p2, timeout=1800)
r2.raise_for_status()
open(path2, 'wb').write(r2.content)
print(len(r2.content) / 1e6, 'Mo', r2.url)
with open(os.path.join(OUT, '_urls_requetes.txt'), 'a', encoding='utf-8') as f:
    f.write(f'{os.path.basename(path2)}\t{r2.url}\n')
