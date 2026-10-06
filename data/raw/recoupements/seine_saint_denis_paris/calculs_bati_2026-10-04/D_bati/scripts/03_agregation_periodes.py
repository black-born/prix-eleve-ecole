# -*- coding: utf-8 -*-
"""Agrégation des années de construction BDNB par établissement, puis par département et type.

Entrée  : ../resultats/etab_rnb_bdnb.csv (script 02)
Sorties : ../resultats/bdnb_periodes_par_etablissement.csv
          ../resultats/bdnb_periodes_synthese.csv (une ligne par département x type)
          ../resultats/bdnb_periodes_surface.csv  (emprise au sol par période, m²)

Règles :
- « bâtiment principal » d'un établissement = la construction BDNB (identifiant RNB) de plus grande
  emprise au sol (s_geom_cstr) ; son année = annee_construction du groupe de bâtiments BDNB auquel elle
  appartient (source : fichiers fonciers) ;
- année « inconnue » si le RNB n'est pas trouvé dans la BDNB ou si annee_construction est vide ;
- périodes : avant 1914 ; 1914-1944 ; 1945-1969 ; 1970-1979 ; 1980-1999 ; 2000 et après ;
- pondération par l'emprise : somme des emprises des constructions (dédoublonnées par identifiant RNB
  au sein d'un département) selon la période de leur groupe.
"""
import sys

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/D_bati"
link = pd.read_csv(ROOT + "/resultats/etab_rnb_bdnb.csv", sep=";", dtype={"numero_uai": str, "code_departement": str})

LAB = ["avant 1914", "1914-1944", "1945-1969", "1970-1979", "1980-1999", "2000 et après"]


def periode(a):
    if pd.isna(a):
        return "inconnue"
    a = int(a)
    if a < 1914:
        return LAB[0]
    if a < 1945:
        return LAB[1]
    if a < 1970:
        return LAB[2]
    if a < 1980:
        return LAB[3]
    if a < 2000:
        return LAB[4]
    return LAB[5]


link["s_geom_cstr"] = pd.to_numeric(link["s_geom_cstr"], errors="coerce")
link["annee_construction"] = pd.to_numeric(link["annee_construction"], errors="coerce")

# --- bâtiment principal par établissement
etab = link[["numero_uai", "appellation_officielle", "code_departement", "categorie"]].drop_duplicates("numero_uai")
lk = link.dropna(subset=["s_geom_cstr"]).sort_values("s_geom_cstr", ascending=False)
main = lk.drop_duplicates("numero_uai")[["numero_uai", "rnb_id", "batiment_groupe_id", "s_geom_cstr",
                                         "annee_construction", "annee_construction_dpe", "nb_niveau",
                                         "mat_mur_txt", "classe_bilan_dpe"]]
etab = etab.merge(main, on="numero_uai", how="left")
etab["periode_principal"] = etab.annee_construction.map(periode)
etab.to_csv(ROOT + "/resultats/bdnb_periodes_par_etablissement.csv", sep=";", index=False, encoding="utf-8")

rows = []
for (dep, cat), g in etab.groupby(["code_departement", "categorie"]):
    n = len(g)
    trouve = g.batiment_groupe_id.notna().sum()
    connu = g.annee_construction.notna().sum()
    d = {"departement": dep, "categorie": cat, "etablissements": n,
         "batiment_principal_trouve_BDNB": int(trouve),
         "annee_connue": int(connu),
         "part_annee_connue_%": round(connu / n * 100, 1),
         "annee_mediane": (int(np.nanmedian(g.annee_construction)) if connu else None)}
    for lab in LAB:
        d[lab + " (% des connus)"] = round((g.periode_principal == lab).sum() / connu * 100, 1) if connu else None
    rows.append(d)
syn = pd.DataFrame(rows)
syn.to_csv(ROOT + "/resultats/bdnb_periodes_synthese.csv", sep=";", index=False, encoding="utf-8")
print(syn.to_string(index=False))

# --- pondération par l'emprise (constructions dédoublonnées)
cons = link.dropna(subset=["s_geom_cstr"]).drop_duplicates(["code_departement", "categorie", "rnb_id"]).copy()
cons["periode"] = cons.annee_construction.map(periode)
surf = cons.pivot_table(index=["code_departement", "categorie"], columns="periode", values="s_geom_cstr",
                        aggfunc="sum", fill_value=0)
surf["total_m2"] = surf.sum(axis=1)
for c in LAB:
    if c in surf.columns:
        known = surf["total_m2"] - surf.get("inconnue", 0)
        surf[c + " (% emprise connue)"] = (surf[c] / known * 100).round(1)
surf.to_csv(ROOT + "/resultats/bdnb_periodes_surface.csv", sep=";", encoding="utf-8")
print(surf.round(0).to_string())

# --- années « rondes » suspectes (1900, 1950...) : contrôle de qualité
yrs = etab.annee_construction.dropna().astype(int)
print("\nAnnées les plus fréquentes (bâtiment principal) :")
print(etab.groupby("code_departement").annee_construction.value_counts().groupby(level=0).head(8))
