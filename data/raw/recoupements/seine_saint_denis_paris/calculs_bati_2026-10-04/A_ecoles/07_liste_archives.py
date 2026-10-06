# -*- coding: utf-8 -*-
"""Tâche A - liste des fichiers sources à archiver (chemin local, titre, producteur, date, URL, officiel)."""
import sys
import json
import os
import re

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
W = HERE.replace('\\', '/')
urls = {}
for line in open(os.path.join(HERE, 'brut', '_urls_requetes.txt'), encoding='utf-8'):
    a, b = line.rstrip('\n').split('\t')
    urls[a] = b
dsdate = {2021: 'jeu publié le 22/12/2022', 2022: 'jeu mis à jour le 07/12/2023', 2023: 'jeu mis à jour le 06/12/2024',
          2024: 'jeu mis à jour le 09/12/2025', 2025: 'jeu mis à jour le 13/07/2026'}
qlab = {'Q1': "communes de Paris, des Hauts-de-Seine, de la Seine-Saint-Denis et du Val-de-Marne, fonction 2, par budget, fonction et compte (classes 1, 2, 6, 7)",
        'Q2a': "mêmes communes, toutes fonctions, personnel (64) par budget et fonction",
        'Q2b': "mêmes communes, toutes fonctions, fonctionnement (classe 6 hors 66, 675, 676, 68) par budget et fonction",
        'Q2c': "mêmes communes, toutes fonctions, équipement (20, 21, 23) par budget et fonction",
        'Q2d': "mêmes communes, toutes fonctions, comptes liés aux bâtiments (6061x, 60621, 60631, 6152x, 6156, 6283, 6132, 614, 616) par budget, fonction et compte",
        'Q3': "toutes les communes, fonctions « écoles » 20, 21, 28, 29 (et 90x/93x), comptes 6, 20, 21, 23, par commune et compte",
        'Q3b': "toutes les communes, fonctions 25x, par commune, fonction et compte",
        'Q3c': "toutes les communes, fonction 2 non ventilée (2, 902, 932), par commune et compte",
        'Q4': "communes de 75, 92, 93, 94 : comptes 1675 et 235 (marchés de partenariat), par fonction"}
out = []
for f in sorted(os.listdir(os.path.join(HERE, 'brut'))):
    m = re.match(r'DGFiP_(\d{4})_(Q\w+?)_', f)
    if m:
        y = int(m.group(1))
        q = m.group(2)
        out.append({'fichier_local': f'{W}/brut/{f}',
                    'titre': f'Balances comptables des collectivités et des EPL, présentation croisée nature-fonction {y} : extraction API ({qlab[q]})',
                    'producteur': 'DGFiP (data.economie.gouv.fr)', 'date': f'exercice {y} ; {dsdate[y]} ; extrait le 04/10/2026',
                    'url': urls.get(f, ''), 'officiel': True})
for f, t, d in (('DEPP_effectifs_par_ecole_rentrees2020-2025_API.csv',
                 "Effectifs d'élèves par école (fr-en-ecoles-effectifs-nb_classes), rentrées 2020 à 2025, extraction API",
                 'jeu mis à jour le 27/08/2026 ; extrait le 04/10/2026'),
                ('DEPP_effectifs_classes_par_departement_secteur_rentrees2015-2025_API.csv',
                 "Effectifs d'élèves par école : écoles, classes et élèves agrégés par département et secteur, rentrées 2015 à 2025",
                 'jeu mis à jour le 27/08/2026 ; extrait le 04/10/2026')):
    out.append({'fichier_local': f'{W}/brut/{f}', 'titre': t,
                'producteur': "DEPP, ministère de l'Éducation nationale (data.education.gouv.fr)", 'date': d, 'url': urls[f], 'officiel': True})
out.append({'fichier_local': f'{W}/brut/MEN_annuaire_education_ecoles_UAI_commune_API.csv',
            'titre': "Annuaire de l'éducation (fr-en-annuaire-education), écoles : UAI, commune Insee, statut, date d'ouverture",
            'producteur': "Ministère de l'Éducation nationale (data.education.gouv.fr)", 'date': 'extrait le 04/10/2026',
            'url': urls['MEN_annuaire_education_ecoles_UAI_commune_API.csv'], 'officiel': True})
out.append({'fichier_local': f'{W}/brut/_urls_requetes.txt', 'titre': 'Liste des requêtes API (URL complètes) ayant produit les extractions du dossier brut/',
            'producteur': "calcul de l'auteur", 'date': '04/10/2026', 'url': '', 'officiel': False})
meta = [('catalog_search.json', 'Catalogue data.economie.gouv.fr : jeux « balances … nature-fonction » 2012-2025', 'DGFiP (data.economie.gouv.fr)',
         'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets?where=search(%22nature-fonction%22)%20or%20search(%22avec%20fonction%22)&limit=50'),
        ('meta_dgfip_2024.json', 'Métadonnées du jeu DGFiP nature-fonction 2024', 'DGFiP (data.economie.gouv.fr)',
         'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2024'),
        ('meta_dgfip_2025.json', 'Métadonnées du jeu DGFiP nature-fonction 2025', 'DGFiP (data.economie.gouv.fr)',
         'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025'),
        ('meta_balances-comptables-des-collectivites-et-des-epl-avec-fonction-2023.json', 'Métadonnées du jeu DGFiP nature-fonction 2023', 'DGFiP (data.economie.gouv.fr)',
         'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-epl-avec-fonction-2023'),
        ('meta_balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-2022.json', 'Métadonnées du jeu DGFiP nature-fonction 2022', 'DGFiP (data.economie.gouv.fr)',
         'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-2022'),
        ('meta_balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec8.json', 'Métadonnées du jeu DGFiP nature-fonction 2021', 'DGFiP (data.economie.gouv.fr)',
         'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec8'),
        ('meta_effectifs.json', "Métadonnées du jeu DEPP « Effectifs d'élèves par école »", 'DEPP (data.education.gouv.fr)',
         'https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ecoles-effectifs-nb_classes'),
        ('ofgl_catalog.json', 'Catalogue data.ofgl.fr (94 jeux) : aucun jeu « comptes des communes, présentation fonctionnelle »', 'OFGL (data.ofgl.fr)',
         'https://data.ofgl.fr/api/explore/v2.1/catalog/datasets?limit=100')]
for f, t, p, u in meta:
    out.append({'fichier_local': f'{W}/{f}', 'titre': t, 'producteur': p, 'date': 'consulté le 04/10/2026', 'url': u, 'officiel': True})
docs = [('sources_officielles/OFGL_CapSur21_investissements_scolaires_2023.pdf', 'Cap sur… n° 21 : Les investissements scolaires des collectivités locales', 'OFGL',
         'octobre-novembre 2023',
         "https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/Les%20chantiers%20de%20l'OFGL/OFGL_cap_sur_21_investissements_scolaires_collectivites_30-10-2023.pdf"),
        ('sources_officielles/CRC_IDF_VilleParis_ecole_elementaire_2025_IDR2025-64.pdf', "Ville de Paris – L'école élémentaire, rapport d'observations définitives (IDR2025-64)",
         'Chambre régionale des comptes Île-de-France', '20/11/2025', 'https://www.ccomptes.fr/sites/default/files/2025-11/IDR2025-64.pdf'),
        ('sources_officielles/AN_l16b1938_rapport_suivi_SSD_2023.pdf', "Rapport d'information n° 1938 (suivi du rapport n° 1014 sur l'action de l'État en Seine-Saint-Denis)",
         "Assemblée nationale, Comité d'évaluation et de contrôle", '30/11/2023', 'https://www.assemblee-nationale.fr/dyn/16/rapports/cec/l16b1938_rapport-information.pdf'),
        ('sources_officielles/AN_l15b1014_rapport_SSD_2018.pdf', "Rapport d'information n° 1014 sur l'action de l'État en Seine-Saint-Denis",
         "Assemblée nationale, Comité d'évaluation et de contrôle", '31/05/2018', 'https://www.assemblee-nationale.fr/dyn/15/rapports/cec/l15b1014_rapport-information.pdf'),
        ('sources_officielles/DGFiP_Notice_balance_fonctionnelle.pdf', 'Notice : les balances comptables des collectivités et des EPL avec la présentation croisée nature-fonction',
         'DGFiP, service des collectivités locales', 'octobre 2018 (pièce jointe du jeu 2025)',
         'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/attachments/notice_balance_fonctionnelle_pdf'),
        ('docs_communes/Paris_CA2025_rapport_financier.pdf', 'Compte administratif 2025, rapport financier', 'Ville de Paris', '01/07/2026',
         'https://cdn.paris.fr/paris/2026/07/01/ca-2025-rapport-financier_-gk9Q.pdf'),
        ('docs_communes/Paris_CA2024_rapport_financier.pdf', 'Compte administratif 2024, rapport financier', 'Ville de Paris', '30/06/2025',
         'https://cdn.paris.fr/paris/2025/06/30/ca-2024-rapport-financier-rFhS.pdf'),
        ('docs_communes/Paris_CA2023_rapport_financier.pdf', 'Compte administratif 2023, rapport financier', 'Ville de Paris', '03/07/2024',
         'https://cdn.paris.fr/paris/2024/07/03/rapport-ca-2023-consolide-vf-pour-intro-pxNk.pdf'),
        ('docs_communes/paris_ca_page.html', 'Page « Comptes administratifs de la Ville » (liens vers les documents)', 'Ville de Paris', 'consultée le 04/10/2026',
         'https://www.paris.fr/pages/comptes-administratifs-de-la-ville-retrouvez-toutes-les-infos-27793'),
        ('docs_communes/Bobigny_CA2024_memoire_presentation.pdf', 'Budget de la Ville – CA 2024 – Mémoire de présentation (séance du conseil municipal)',
         'Ville de Bobigny, direction des finances et des achats', '2025 (fichier daté du 11/04/2025)',
         'https://www.bobigny.fr/fileadmin/images/PDF/vie_municipale_et_citoyenne/vie_municipale/budget/2025/Budget_de_la_Ville_-_CA_2024_-_M%C3%A9moire_de_pr%C3%A9sentation.pdf'),
        ('docs_communes/Pantin_education_une_priorite.html', "« L'éducation, une priorité » (site officiel de la Ville de Pantin)", 'Ville de Pantin', '30/08/2024',
         'https://www.pantin.fr/la-ville/aller-plus-loin/leducation-une-priorite-5874'),
        ('docs_communes/Pantin_inauguration_ecole_Diderot.html', '« Inauguration de la nouvelle école Diderot » (site officiel de la Ville de Pantin)', 'Ville de Pantin', '23/08/2024',
         'https://www.pantin.fr/la-ville/en-ce-moment/inauguration-de-la-nouvelle-ecole-diderot-5863')]
for f, t, p, d, u in docs:
    out.append({'fichier_local': f'{W}/{f}', 'titre': t, 'producteur': p, 'date': d, 'url': u, 'officiel': True})
for o in out:
    assert os.path.exists(o['fichier_local']), o['fichier_local']
print(len(out))
json.dump(out, open(os.path.join(HERE, 'sorties', '_fichiers_a_archiver.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
