"""Extraction des balances DGFiP « présentation croisée nature-fonction » 2012-2025
(data.economie.gouv.fr, API Explore v2.1, export CSV agrégé avec group_by).
Périmètre : budgets principaux (cbudg=1) des départements d'Île-de-France (75 avant 2019, 77, 78, 91, 92, 93, 94, 95),
de la Ville de Paris (categ PARIS, depuis 2019) ; fonctions d'enseignement (2*, 902*, 932*) et comptes de dette 16*
(toutes fonctions) ; + totaux nationaux par catégorie pour les fonctions 2*.
Sortie : sources/dgfip/DGFiP_<annee>_IDF_departements_Paris_fonction2_dette16_par_compte_API.csv
         sources/dgfip/DGFiP_<annee>_national_par_categ_fonction22x_par_compte_API.csv
"""
import json, os, sys, time
import requests
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'sources')
OUT = os.path.join(SRC, 'dgfip')
ds = json.load(open(os.path.join(SRC, 'DGFiP_datasets_par_annee.json')))
BASE = 'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/{}/exports/csv'
SUMS = ('sum(bedeb) as bedeb,sum(becre) as becre,sum(obnetdeb) as obnetdeb,sum(obnetcre) as obnetcre,'
        'sum(onbdeb) as onbdeb,sum(onbcre) as onbcre,sum(oobdeb) as oobdeb,sum(oobcre) as oobcre,sum(sd) as sd,sum(sc) as sc')
IDF = ' or '.join(f'ndept="{d}"' for d in ['075', '077', '078', '091', '092', '093', '094', '095'])
FONC = 'startswith(fonction,"2") or startswith(fonction,"902") or startswith(fonction,"932")'

def get(year, select, where, group_by, fname):
    url = BASE.format(ds[str(year)])
    params = {'select': select, 'where': where, 'group_by': group_by, 'delimiter': ';'}
    for attempt in range(4):
        try:
            r = requests.get(url, params=params, timeout=600)
            if r.status_code == 200 and len(r.content) > 50:
                open(os.path.join(OUT, fname), 'wb').write(r.content)
                print(year, fname, len(r.content), 'octets', '| URL :', r.url[:200], '...')
                return r.url
            print('HTTP', r.status_code, r.text[:300])
        except Exception as e:
            print('erreur', e)
        time.sleep(5)
    raise RuntimeError(f'échec {year} {fname}')

urls = {}
years = [int(a) for a in sys.argv[1:]] or list(range(2012, 2026))
for y in years:
    # 1. IDF départements + Paris : fonctions d'enseignement et dette (16) toutes fonctions
    where = (f'cbudg="1" and ((categ="DEPT" and ({IDF})) or categ="PARIS") '
             f'and (({FONC}) or startswith(compte,"16"))')
    sel = 'categ,ndept,ident,lbudg,nomen,fonction,compte,' + SUMS
    urls[f'{y}_idf'] = get(y, sel, where, 'categ,ndept,ident,lbudg,nomen,fonction,compte',
                           f'DGFiP_{y}_IDF_departements_Paris_fonction2_dette16_par_compte_API.csv')
    # 2. National : départements, Paris, Métropole de Lyon, CTU, régions ; fonctions 2*, par catégorie et compte
    where2 = (f'cbudg="1" and (categ="DEPT" or categ="PARIS" or categ="ML" or categ="CTU" or categ="REG") and ({FONC})')
    sel2 = 'categ,nomen,fonction,compte,' + SUMS
    urls[f'{y}_nat'] = get(y, sel2, where2, 'categ,nomen,fonction,compte',
                           f'DGFiP_{y}_national_DEPT_PARIS_ML_CTU_REG_fonction2_par_compte_API.csv')
json.dump(urls, open(os.path.join(OUT, f'_urls_extraction_{years[0]}_{years[-1]}.json'), 'w'), indent=1)
