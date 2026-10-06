"""Tâche E.3 — Séries d'effectifs d'élèves du PUBLIC, Paris / Seine-Saint-Denis / France, à partir des exports
de e3a (sources/). France = métropole + DROM (codes 01-95, 2A, 2B, 971-974, 976) ; sont exclus Saint-Pierre-et-Miquelon
(975), Wallis-et-Futuna (986), Polynésie (987), Nouvelle-Calédonie (988). Saint-Martin et Saint-Barthélemy sont codés
971 dans ces fichiers (H-B18) : ils restent dans la France.

- Écoles publiques : jeu « Effectifs d'élèves par école », rentrées 2009-2025 (élèves, écoles, classes).
- Collèges publics : 2015-2019 jeu obsolète (élèves des établissements publics de type COLLEGE*, toutes formations) ;
  2019-2025 jeu « Effectifs d'élèves en collège » (élèves de niveau collège, SEGPA et ULIS comprises, des
  établissements publics). Raccord en 2019 (rentrée commune) par les taux d'évolution.
- Lycées publics : 2015-2019 jeu obsolète (élèves des établissements publics de type LYCEE*, post-bac compris) ;
  2019-2025 jeux « lycée GT » + « lycée professionnel » (élèves des niveaux lycée, hors post-bac). Même raccord.
Taux annuels moyens = (fin / début)^(1/n) − 1.
Sorties : e3b_series_effectifs_publics.csv, e3b_evolutions.csv
"""
import sys
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
SRC = Path(__file__).resolve().parent / "sources"
OUT = Path(__file__).resolve().parent
HORS = {"975", "986", "987", "988", "977", "978"}


def norm_dep(c):
    c = str(c).strip()
    if c.isdigit() and len(c) == 3 and c.startswith("0"):
        c = c[1:]
    if c.startswith("02") and c[2:] in ("A", "B"):
        c = c[1:]
    return c


def territoires(df, col):
    d = df.copy()
    d["dep"] = d[col].map(norm_dep)
    d = d[~d["dep"].isin(HORS)]
    out = {"Paris": d[d["dep"] == "75"], "Seine-Saint-Denis": d[d["dep"] == "93"], "France": d}
    return out


lignes = []
# ---- Écoles
e = pd.read_csv(SRC / "DEPP_opendata_ecoles_effectifs_par_rentree_departement_secteur_2009-2025.csv", sep=";",
                encoding="utf-8-sig", dtype={"code_departement": str})
e["rentree"] = e["rentree_scolaire"].str[:4].astype(int)
e = e[e["secteur"].eq("PUBLIC")]
for t, d in territoires(e, "code_departement").items():
    g = d.groupby("rentree")[["ecoles", "eleves", "classes"]].sum()
    for y, r in g.iterrows():
        lignes.append({"niveau": "écoles publiques", "territoire": t, "rentree": y, "source": "fr-en-ecoles-effectifs-nb_classes",
                       "eleves": r["eleves"], "etablissements": r["ecoles"], "classes": r["classes"]})
# ---- Collèges et lycées, nouveaux jeux 2019-2025
c = pd.read_csv(SRC / "DEPP_opendata_colleges_effectifs_par_rentree_departement_secteur_2019-2025.csv", sep=";",
                encoding="utf-8-sig", dtype={"code_dept": str})
c["rentree"] = c["rentree_scolaire"].str[:4].astype(int)
c = c[c["secteur"].eq("PUBLIC")]
for t, d in territoires(c, "code_dept").items():
    g = d.groupby("rentree")[["etablissements", "eleves"]].sum()
    for y, r in g.iterrows():
        lignes.append({"niveau": "collèges publics (niveau collège)", "territoire": t, "rentree": y,
                       "source": "fr-en-college-effectifs-niveau-sexe-lv", "eleves": r["eleves"],
                       "etablissements": r["etablissements"], "classes": None})
lg = pd.read_csv(SRC / "DEPP_opendata_lycees_gt_effectifs_par_rentree_departement_secteur_2019-2025.csv", sep=";",
                 encoding="utf-8-sig", dtype={"code_departement_pays": str}).rename(columns={"code_departement_pays": "code_departement"})
lp = pd.read_csv(SRC / "DEPP_opendata_lycees_pro_effectifs_par_rentree_departement_secteur_2019-2025.csv", sep=";",
                 encoding="utf-8-sig", dtype={"code_departement": str})
for nom, df in (("lycéens GT du public", lg), ("lycéens professionnels du public", lp)):
    df["rentree"] = df["rentree_scolaire"].str[:4].astype(int)
    df = df[df["secteur"].eq("PUBLIC")]
    for t, d in territoires(df, "code_departement").items():
        g = d.groupby("rentree")[["etablissements", "eleves"]].sum()
        for y, r in g.iterrows():
            lignes.append({"niveau": nom, "territoire": t, "rentree": y, "source": "lycee_gt / lycee_pro",
                           "eleves": r["eleves"], "etablissements": r["etablissements"], "classes": None})
# ---- Ancien jeu 2015-2019
o = pd.read_csv(SRC / "DEPP_opendata_second_degre_obsolete_par_annee_departement_type_secteur_2015-2019.csv", sep=";",
                encoding="utf-8-sig", dtype={"code_departement": str})
o["rentree"] = o["annee_scolaire"].str[:4].astype(int)
o = o[o["secteur_d_enseignement"].eq("Public")]
for nom, masque in (("collèges publics (établissements de type collège, ancien jeu)", o["type_d_etablissement"].str.startswith("COLLEGE")),
                    ("lycées publics (établissements de type lycée, post-bac compris, ancien jeu)", o["type_d_etablissement"].str.startswith("LYCEE"))):
    for t, d in territoires(o[masque], "code_departement").items():
        g = d.groupby("rentree")[["etablissements", "eleves"]].sum()
        for y, r in g.iterrows():
            lignes.append({"niveau": nom, "territoire": t, "rentree": y, "source": "fr-en-effectifs-second-degre (obsolète)",
                           "eleves": r["eleves"], "etablissements": r["etablissements"], "classes": None})
s = pd.DataFrame(lignes)
# Lycéens GT + pro
lyc = (s[s["niveau"].isin(["lycéens GT du public", "lycéens professionnels du public"])]
       .groupby(["territoire", "rentree"], as_index=False)["eleves"].sum().assign(niveau="lycéens du public (GT + pro, niveaux lycée)",
                                                                                source="lycee_gt + lycee_pro"))
s = pd.concat([s, lyc], ignore_index=True)
s["eleves_par_etablissement"] = s["eleves"] / s["etablissements"]
s["eleves_par_classe"] = s["eleves"] / s["classes"]
s.sort_values(["niveau", "territoire", "rentree"]).round(2).to_csv(OUT / "e3b_series_effectifs_publics.csv", sep=";",
                                                                    index=False, encoding="utf-8-sig")


def val(niv, t, y):
    x = s[(s["niveau"] == niv) & (s["territoire"] == t) & (s["rentree"] == y)]["eleves"]
    return float(x.iloc[0]) if len(x) else float("nan")


ev = []
for t in ("Paris", "Seine-Saint-Denis", "France"):
    E = "écoles publiques"
    for a, b in ((2009, 2025), (2010, 2025), (2010, 2019), (2019, 2025), (2015, 2025), (2024, 2025)):
        v0, v1 = val(E, t, a), val(E, t, b)
        ev.append({"niveau": E, "territoire": t, "debut": a, "fin": b, "eleves_debut": v0, "eleves_fin": v1,
                   "evolution_%": 100 * (v1 / v0 - 1), "taux_annuel_%": 100 * ((v1 / v0) ** (1 / (b - a)) - 1), "methode": "série directe"})
    for niv_new, niv_old, lib in (("collèges publics (niveau collège)", "collèges publics (établissements de type collège, ancien jeu)", "collèges publics"),
                                  ("lycéens du public (GT + pro, niveaux lycée)", "lycées publics (établissements de type lycée, post-bac compris, ancien jeu)", "lycées publics")):
        o15, o19 = val(niv_old, t, 2015), val(niv_old, t, 2019)
        n19, n25 = val(niv_new, t, 2019), val(niv_new, t, 2025)
        n24 = val(niv_new, t, 2024)
        chain = (o19 / o15) * (n25 / n19)
        ev.append({"niveau": lib, "territoire": t, "debut": 2015, "fin": 2019, "eleves_debut": o15, "eleves_fin": o19,
                   "evolution_%": 100 * (o19 / o15 - 1), "taux_annuel_%": 100 * ((o19 / o15) ** 0.25 - 1), "methode": "ancien jeu"})
        ev.append({"niveau": lib, "territoire": t, "debut": 2019, "fin": 2025, "eleves_debut": n19, "eleves_fin": n25,
                   "evolution_%": 100 * (n25 / n19 - 1), "taux_annuel_%": 100 * ((n25 / n19) ** (1 / 6) - 1), "methode": "nouveau jeu"})
        ev.append({"niveau": lib, "territoire": t, "debut": 2024, "fin": 2025, "eleves_debut": n24, "eleves_fin": n25,
                   "evolution_%": 100 * (n25 / n24 - 1), "taux_annuel_%": 100 * (n25 / n24 - 1), "methode": "nouveau jeu"})
        ev.append({"niveau": lib, "territoire": t, "debut": 2015, "fin": 2025, "eleves_debut": None, "eleves_fin": n25,
                   "evolution_%": 100 * (chain - 1), "taux_annuel_%": 100 * (chain ** 0.1 - 1),
                   "methode": f"raccord en 2019 (ancien jeu 2019 : {o19:.0f} ; nouveau jeu 2019 : {n19:.0f})"})
ev = pd.DataFrame(ev)
ev.round(2).to_csv(OUT / "e3b_evolutions.csv", sep=";", index=False, encoding="utf-8-sig")
pd.set_option("display.width", 250, "display.max_colwidth", 90, "display.max_rows", 500)
piv = s[s["niveau"].isin(["écoles publiques", "collèges publics (niveau collège)", "lycéens du public (GT + pro, niveaux lycée)",
                          "collèges publics (établissements de type collège, ancien jeu)",
                          "lycées publics (établissements de type lycée, post-bac compris, ancien jeu)"])]
print(piv.pivot_table(index=["niveau", "rentree"], columns="territoire", values="eleves").round(0).to_string())
print(s[s["niveau"].eq("écoles publiques")].pivot_table(index="rentree", columns="territoire",
      values=["etablissements", "eleves_par_etablissement", "eleves_par_classe"]).round(1).to_string())
print(ev.round(1).to_string(index=False))
