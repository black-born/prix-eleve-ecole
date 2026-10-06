# -*- coding: utf-8 -*-
"""
Tâche A (bâti scolaire, écoles) - extraction des balances DGFiP « présentation croisée nature-fonction », 2021 à 2025.
Source : data.economie.gouv.fr (DGFiP), API Explore v2.1, export CSV agrégé. Consulté le 2026-10-04.

Requêtes, pour chaque exercice :
  Q1 : communes de Paris (Ville de Paris, budget principal ET budgets annexes d'arrondissement), des Hauts-de-Seine (92),
       de la Seine-Saint-Denis (93) et du Val-de-Marne (94) ; fonction 2 (y c. codes 902x / 932x des budgets votés par
       fonction) ; comptes des classes 1, 2, 6, 7 ; tous budgets ; agrégé par collectivité x budget x fonction x compte.
  Q2 : mêmes communes, toutes fonctions ; trois agrégats par collectivité x budget x fonction :
       personnel (64), fonctionnement (classe 6 hors 66, 675, 676, 68), équipement (20, 21, 23).
  Q2d : mêmes communes, toutes fonctions, comptes « bâti » (6061x, 60621, 60631, 6152x, 6156, 6283, 6132, 614, 616),
       par collectivité x budget x fonction x compte (part imputée aux fonctions « écoles »).
  Q3 : toutes les communes de France (catégories Commune et PARIS), tous budgets, fonctions « écoles » du périmètre
       du projet (20, 21, 28, 29 et 9020/9021/9028/9029/9320/9321/9328/9329), comptes 6, 20, 21, 23 ; agrégé par
       collectivité x budget x nomenclature x compte.
  Q3b : idem pour les fonctions 25x (M14 : services annexes de l'enseignement ; M57 : formation professionnelle),
        agrégé aussi par fonction (le traitement dépend de la nomenclature).
  Q3c : idem pour la fonction 2 « non ventilée » (codes exacts 2, 902, 932).
Opérations réelles = OBNETDEB - OOBDEB (débit) et OBNETCRE - OOBCRE (crédit), comme dans le projet
(data/raw/collectivites/extractions/_script_extractions_collectivites.py).
"""
import os
import sys
import time
import requests

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'brut')
os.makedirs(OUT, exist_ok=True)

BASE = 'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/{}/exports/csv'
DS = {
    2021: 'balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec8',
    2022: 'balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-2022',
    2023: 'balances-comptables-des-collectivites-et-des-epl-avec-fonction-2023',
    2024: 'balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2024',
    2025: 'balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025',
}
SUMS = 'sum(obnetdeb) as obnetdeb,sum(obnetcre) as obnetcre,sum(oobdeb) as oobdeb,sum(oobcre) as oobcre,count(*) as nb_lignes'
COMMUNES = '(categ="Commune" or categ="PARIS")'
IDF = '(ndept="075" or ndept="092" or ndept="093" or ndept="094")'
F2 = '(startswith(fonction,"2") or startswith(fonction,"902") or startswith(fonction,"932"))'
F_ECOLES = ['20', '21', '28', '29', '9020', '9021', '9028', '9029', '9320', '9321', '9328', '9329']
FW_ECOLES = '(' + ' or '.join(f'startswith(fonction,"{f}")' for f in F_ECOLES) + ')'
FW_25 = '(startswith(fonction,"25") or startswith(fonction,"9025") or startswith(fonction,"9325"))'
FW_2NV = '(fonction="2" or fonction="902" or fonction="932")'
C_1267 = '(startswith(compte,"1") or startswith(compte,"2") or startswith(compte,"6") or startswith(compte,"7"))'
C_6_EQ = '(startswith(compte,"6") or startswith(compte,"20") or startswith(compte,"21") or startswith(compte,"23"))'
C_FONCT = ('(startswith(compte,"6") and not startswith(compte,"66") and not startswith(compte,"675") '
           'and not startswith(compte,"676") and not startswith(compte,"68"))')
C_EQ = '(startswith(compte,"20") or startswith(compte,"21") or startswith(compte,"23"))'
C_64 = 'startswith(compte,"64")'
# comptes « bâti » (énergie et fluides, entretien et réparations, maintenance, nettoyage, loyers, charges locatives, assurances)
C_BATI = '(' + ' or '.join(f'startswith(compte,"{c}")' for c in
                           ['6061', '60621', '60631', '6152', '6156', '6283', '6132', '614', '616']) + ')'

QUERIES = {
    'Q1_communes_75_92_93_94_fonction2_budget_fonction_compte': dict(
        select=f'categ,ndept,insee,siren,lbudg,cbudg,nomen,fonction,compte,{SUMS}',
        where=f'{COMMUNES} and {IDF} and {F2} and {C_1267}',
        group_by='categ,ndept,insee,siren,lbudg,cbudg,nomen,fonction,compte'),
    'Q2a_communes_75_92_93_94_toutes_fonctions_personnel64': dict(
        select=f'categ,ndept,insee,siren,lbudg,cbudg,fonction,{SUMS}',
        where=f'{COMMUNES} and {IDF} and {C_64}',
        group_by='categ,ndept,insee,siren,lbudg,cbudg,fonction'),
    'Q2b_communes_75_92_93_94_toutes_fonctions_fonctionnement': dict(
        select=f'categ,ndept,insee,siren,lbudg,cbudg,fonction,{SUMS}',
        where=f'{COMMUNES} and {IDF} and {C_FONCT}',
        group_by='categ,ndept,insee,siren,lbudg,cbudg,fonction'),
    'Q2c_communes_75_92_93_94_toutes_fonctions_equipement_20_21_23': dict(
        select=f'categ,ndept,insee,siren,lbudg,cbudg,fonction,{SUMS}',
        where=f'{COMMUNES} and {IDF} and {C_EQ}',
        group_by='categ,ndept,insee,siren,lbudg,cbudg,fonction'),
    'Q2d_communes_75_92_93_94_toutes_fonctions_comptes_bati': dict(
        select=f'categ,ndept,insee,siren,lbudg,cbudg,fonction,compte,{SUMS}',
        where=f'{COMMUNES} and {IDF} and {C_BATI}',
        group_by='categ,ndept,insee,siren,lbudg,cbudg,fonction,compte'),
    'Q3_communes_France_fonctions_ecoles_par_commune_compte': dict(
        select=f'categ,ndept,insee,siren,cbudg,nomen,compte,{SUMS}',
        where=f'{COMMUNES} and {FW_ECOLES} and {C_6_EQ}',
        group_by='categ,ndept,insee,siren,cbudg,nomen,compte'),
    'Q3b_communes_France_fonctions_25x_par_commune_fonction_compte': dict(
        select=f'categ,ndept,insee,siren,cbudg,nomen,fonction,compte,{SUMS}',
        where=f'{COMMUNES} and {FW_25} and {C_6_EQ}',
        group_by='categ,ndept,insee,siren,cbudg,nomen,fonction,compte'),
    'Q3c_communes_France_fonction2_non_ventilee_par_commune_compte': dict(
        select=f'categ,ndept,insee,siren,cbudg,nomen,fonction,compte,{SUMS}',
        where=f'{COMMUNES} and {FW_2NV} and {C_6_EQ}',
        group_by='categ,ndept,insee,siren,cbudg,nomen,fonction,compte'),
}


def fetch(year, name, q, retries=3):
    path = os.path.join(OUT, f'DGFiP_{year}_{name}_API.csv')
    if os.path.exists(path) and os.path.getsize(path) > 100:
        print('déjà là :', os.path.basename(path))
        return path
    params = dict(q, delimiter=';')
    for k in range(retries):
        try:
            t = time.time()
            r = requests.get(BASE.format(DS[year]), params=params, timeout=1800)
            r.raise_for_status()
            with open(path, 'wb') as f:
                f.write(r.content)
            print(f'{year} {name}: {len(r.content)/1e6:.1f} Mo en {time.time()-t:.0f} s')
            with open(os.path.join(OUT, '_urls_requetes.txt'), 'a', encoding='utf-8') as f:
                f.write(f'{os.path.basename(path)}\t{r.url}\n')
            return path
        except Exception as e:  # noqa
            print('erreur', year, name, e)
            time.sleep(10)
    raise RuntimeError(f'échec {year} {name}')


if __name__ == '__main__':
    years = [int(a) for a in sys.argv[1:]] or sorted(DS)
    for y in years:
        for name, q in QUERIES.items():
            fetch(y, name, q)
