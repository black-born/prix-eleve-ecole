# -*- coding: utf-8 -*-
"""Année de construction des bâtiments des établissements scolaires publics de Paris (075) et de la
Seine-Saint-Denis (093), d'après la BDNB (CSTB), via les identifiants RNB fournis par l'annuaire
géolocalisé du ministère (champ « rnb »).

Chaîne :
  1. annuaire MEN (script 01) : établissements publics ouverts, écoles / collèges / lycées ;
     liste des identifiants RNB de chaque établissement ;
  2. API ouverte BDNB, table batiment_construction : rnb_id -> batiment_groupe_id, emprise (s_geom_cstr) ;
  3. API ouverte BDNB, table batiment_groupe_complet : annee_construction (fichiers fonciers),
     annee_construction_dpe, classe DPE, matériaux, nombre de niveaux.

Sorties (dossier ../resultats/) :
  - bdnb_rnb_batiment_construction.csv  (réponses brutes étape 2)
  - bdnb_batiment_groupe.csv            (réponses brutes étape 3)
  - etab_rnb_bdnb.csv                    (une ligne par couple établissement x identifiant RNB)
L'agrégation est faite par 03_agregation_periodes.py.

API : https://api.bdnb.io/v1/bdnb/donnees/<table> (PostgREST, 10 lignes maximum par appel,
quota et limite de débit indiqués dans les en-têtes X-Quota-*, X-Rate-Limit-*).
"""
import ast
import json
import sys
import time

import pandas as pd
import requests

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/D_bati"
SRC = ROOT + "/sources/MEN_geoloc_etablissements_075_093_API.csv"
OUT = ROOT + "/resultats"
API = "https://api.bdnb.io/v1/bdnb/donnees/"
SESSION = requests.Session()
SESSION.headers.update({"Accept": "application/json"})


def categorie(nature):
    n = str(nature)
    if n.startswith("ECOLE"):
        return "école"
    if n.startswith("COLLEGE"):
        return "collège"
    if n.startswith("LYCEE") or n.startswith("ETAB REGIONAL"):
        return "lycée"
    return "autre"


def get_all(table, params):
    """Récupère toutes les lignes (pagination par offset, 10 lignes par appel)."""
    rows, offset = [], 0
    while True:
        p = dict(params)
        p["limit"] = 10
        p["offset"] = offset
        for essai in range(5):
            r = SESSION.get(API + table, params=p, timeout=120)
            if r.status_code == 200:
                break
            print("  HTTP", r.status_code, r.text[:200], "- nouvel essai")
            time.sleep(5 * (essai + 1))
        r.raise_for_status()
        batch = r.json()
        rows.extend(batch)
        time.sleep(0.55)
        if len(batch) < 10:
            break
        offset += 10
    return rows


def main():
    df = pd.read_csv(SRC, sep=";", dtype=str)
    df = df[(df.secteur_public_prive_libe == "Public") & (df.etat_etablissement_libe == "OUVERT")].copy()
    df["categorie"] = df.nature_uai_libe.map(categorie)
    df = df[df.categorie != "autre"].copy()
    df["rnb_list"] = df.rnb.fillna("[]").map(ast.literal_eval)
    pairs = [(r.numero_uai, rid) for r in df.itertuples() for rid in r.rnb_list]
    ids = sorted({rid for _, rid in pairs})
    print("établissements :", len(df), "| couples UAI x RNB :", len(pairs), "| RNB uniques :", len(ids))

    # Étape 2 : RNB -> batiment_construction
    bc_rows = []
    for i in range(0, len(ids), 10):
        chunk = ids[i:i + 10]
        rows = get_all("batiment_construction", {
            "rnb_id": "in.(" + ",".join(chunk) + ")",
            "select": "rnb_id,batiment_construction_id,batiment_groupe_id,code_departement_insee,s_geom_cstr,hauteur",
        })
        bc_rows.extend(rows)
        if (i // 10) % 25 == 0:
            print(f"  batiment_construction : {i + len(chunk)}/{len(ids)} RNB, {len(bc_rows)} lignes")
    bc = pd.DataFrame(bc_rows)
    bc.to_csv(OUT + "/bdnb_rnb_batiment_construction.csv", sep=";", index=False, encoding="utf-8")

    # Étape 3 : batiment_groupe_complet
    gids = sorted(bc.batiment_groupe_id.dropna().unique().tolist())
    print("groupes de bâtiments :", len(gids))
    bg_rows = []
    sel = ("batiment_groupe_id,code_departement_insee,libelle_commune_insee,annee_construction,"
           "annee_construction_dpe,classe_bilan_dpe,classe_conso_energie_dpe_tertiaire,mat_mur_txt,mat_toit_txt,"
           "nb_niveau,hauteur_mean,surface_emprise_sol,usage_niveau_1_txt,usage_principal_bdnb_open,"
           "l_denomination_proprietaire")
    for i in range(0, len(gids), 10):
        chunk = gids[i:i + 10]
        rows = get_all("batiment_groupe_complet", {
            "batiment_groupe_id": "in.(" + ",".join(chunk) + ")",
            "select": sel,
        })
        bg_rows.extend(rows)
        if (i // 10) % 25 == 0:
            print(f"  batiment_groupe_complet : {i + len(chunk)}/{len(gids)}")
    bg = pd.DataFrame(bg_rows)
    for col in ("l_denomination_proprietaire",):
        if col in bg.columns:
            bg[col] = bg[col].map(lambda v: json.dumps(v, ensure_ascii=False) if isinstance(v, list) else v)
    bg.to_csv(OUT + "/bdnb_batiment_groupe.csv", sep=";", index=False, encoding="utf-8")

    # Table de liaison établissement x RNB
    link = pd.DataFrame(pairs, columns=["numero_uai", "rnb_id"])
    link = link.merge(df[["numero_uai", "appellation_officielle", "code_departement", "categorie",
                          "nature_uai_libe", "libelle_commune", "date_ouverture"]], on="numero_uai", how="left")
    link = link.merge(bc, on="rnb_id", how="left")
    link = link.merge(bg.drop(columns=["code_departement_insee"], errors="ignore"), on="batiment_groupe_id", how="left")
    link.to_csv(OUT + "/etab_rnb_bdnb.csv", sep=";", index=False, encoding="utf-8")
    print("terminé :", len(link), "lignes")


if __name__ == "__main__":
    main()
