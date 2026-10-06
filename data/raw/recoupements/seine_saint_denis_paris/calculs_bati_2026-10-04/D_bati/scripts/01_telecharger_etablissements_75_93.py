# -*- coding: utf-8 -*-
"""Télécharge l'annuaire géolocalisé des établissements (MEN/DEPP) pour Paris (075) et la
Seine-Saint-Denis (093) : jeu « fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre »
(data.education.gouv.fr, API Explore v2.1). Export CSV complet (tous secteurs, tous états) ; le
filtrage est fait dans le script d'analyse.

Sortie : ../sources/MEN_geoloc_etablissements_075_093_API.csv (sep ';', UTF-8).
"""
import sys
import requests

sys.stdout.reconfigure(encoding="utf-8")

BASE = ("https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/"
        "fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre/exports/csv")
params = {
    "where": "code_departement in ('075','093')",
    "delimiter": ";",
    "lang": "fr",
    "timezone": "Europe/Paris",
}
out = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/D_bati/sources/MEN_geoloc_etablissements_075_093_API.csv"
r = requests.get(BASE, params=params, timeout=300)
r.raise_for_status()
with open(out, "wb") as fh:
    fh.write(r.content)
print("URL :", r.url)
print("octets :", len(r.content))
print("lignes :", r.content.count(b"\n"))
