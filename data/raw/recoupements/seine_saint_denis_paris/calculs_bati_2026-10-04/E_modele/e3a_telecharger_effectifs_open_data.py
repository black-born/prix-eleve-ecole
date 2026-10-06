"""Tâche E.3 — Téléchargement (API Opendatasoft v2.1 de data.education.gouv.fr, DEPP) des effectifs d'élèves agrégés
par rentrée × département × secteur (et type d'établissement pour l'ancien jeu du 2nd degré).

Jeux (Licence Ouverte v2.0, producteur DEPP) :
- fr-en-ecoles-effectifs-nb_classes        « Effectifs d'élèves par école », rentrées 2009 à 2025 (mi-septembre)
- fr-en-college-effectifs-niveau-sexe-lv   « Effectifs d'élèves en collège », rentrées 2019 à 2025 (début octobre)
- fr-en-lycee_gt-effectifs-niveau-sexe-lv  « Effectifs d'élèves en lycée d'enseignement général et technologique », 2019-2025
- fr-en-lycee_pro-effectifs-niveau-sexe-lv « Effectifs d'élèves en lycée professionnel », 2019-2025
- fr-en-effectifs-second-degre             « Effectifs d'élèves des établissements du second degré … - Obsolète »,
                                           années scolaires 2015-2016 à 2019-2020, par établissement et type
- fr-en-taille-moyenne-classes-premier-degre « Taille moyenne des classes dans le premier degré » (E/C par département)

Chaque réponse est enregistrée telle quelle (CSV, séparateur ;) dans le sous-dossier sources/ avec l'URL exacte.
"""
import sys
import urllib.parse
from pathlib import Path

import requests

sys.stdout.reconfigure(encoding="utf-8")
OUT = Path(__file__).resolve().parent / "sources"
OUT.mkdir(exist_ok=True)
API = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/{}/exports/csv"

REQ = {
    "DEPP_opendata_ecoles_effectifs_par_rentree_departement_secteur_2009-2025.csv": (
        "fr-en-ecoles-effectifs-nb_classes",
        {"select": "rentree_scolaire, code_departement, departement, secteur, count(*) as ecoles, "
                   "sum(nombre_total_eleves) as eleves, sum(nombre_total_classes) as classes",
         "group_by": "rentree_scolaire, code_departement, departement, secteur"}),
    "DEPP_opendata_colleges_effectifs_par_rentree_departement_secteur_2019-2025.csv": (
        "fr-en-college-effectifs-niveau-sexe-lv",
        {"select": "rentree_scolaire, code_dept, departement, secteur, count(*) as etablissements, "
                   "sum(nombre_eleves_total) as eleves, sum(nombre_d_eleves_total_segpa) as segpa, "
                   "sum(nombre_d_eleves_total_ulis) as ulis",
         "group_by": "rentree_scolaire, code_dept, departement, secteur"}),
    "DEPP_opendata_lycees_gt_effectifs_par_rentree_departement_secteur_2019-2025.csv": (
        "fr-en-lycee_gt-effectifs-niveau-sexe-lv",
        {"select": "rentree_scolaire, code_departement_pays, departement, secteur, "
                   "count(*) as etablissements, sum(nombre_d_eleves) as eleves",
         "group_by": "rentree_scolaire, code_departement_pays, departement, secteur"}),
    "DEPP_opendata_lycees_pro_effectifs_par_rentree_departement_secteur_2019-2025.csv": (
        "fr-en-lycee_pro-effectifs-niveau-sexe-lv",
        {"select": "rentree_scolaire, code_departement, departement, secteur, "
                   "count(*) as etablissements, sum(nombre_d_eleves) as eleves",
         "group_by": "rentree_scolaire, code_departement, departement, secteur"}),
    "DEPP_opendata_second_degre_obsolete_par_annee_departement_type_secteur_2015-2019.csv": (
        "fr-en-effectifs-second-degre",
        {"select": "annee_scolaire, code_departement, libelle_departement, type_d_etablissement, secteur_d_enseignement, "
                   "count(*) as etablissements, sum(nombre_d_eleves) as eleves",
         "group_by": "annee_scolaire, code_departement, libelle_departement, type_d_etablissement, secteur_d_enseignement"}),
}
for nom, (ds, params) in REQ.items():
    p = dict(params, delimiter=";")
    url = API.format(ds) + "?" + urllib.parse.urlencode(p)
    r = requests.get(url, timeout=300)
    r.raise_for_status()
    (OUT / nom).write_bytes(r.content)
    print(nom, len(r.content), "octets ;", r.text.count("\n"), "lignes")
    print("  URL :", url)

# Taille moyenne des classes (E/C) par département : une ligne par école ; les colonnes esurc_dep_* sont constantes
# dans un département. On télécharge les valeurs départementales et nationales, toutes années disponibles.
ds = "fr-en-taille-moyenne-classes-premier-degre"
p = {"select": "annee, libelle_departement, libelle_secteur, avg(esurc_dep_preel) as esurc_dep_preel, "
               "avg(esurc_dep_elem) as esurc_dep_elem, min(esurc_dep_elem) as min_dep_elem, max(esurc_dep_elem) as max_dep_elem, "
               "avg(esurc_fr_preel) as esurc_fr_preel, avg(esurc_fr_elem) as esurc_fr_elem, count(*) as ecoles",
     "group_by": "annee, libelle_departement, libelle_secteur", "delimiter": ";"}
url = API.format(ds) + "?" + urllib.parse.urlencode(p)
r = requests.get(url, timeout=300)
r.raise_for_status()
nom = "DEPP_opendata_taille_moyenne_classes_1er_degre_par_departement.csv"
(OUT / nom).write_bytes(r.content)
print(nom, len(r.content), "octets ; URL :", url)
