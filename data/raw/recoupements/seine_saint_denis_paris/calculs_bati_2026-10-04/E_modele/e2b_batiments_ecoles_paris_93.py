"""Tâche E.2 (illustration) — Ce que B « attribuerait » aux bâtiments des écoles publiques de Paris et du 93 si l'on
appliquait la structure nationale (méthode H-D2 du script 05), comparé aux comptes 2025 de la Ville de Paris et des
communes de la Seine-Saint-Denis (investissement, énergie, entretien des fonctions « écoles »).

Fonctions « écoles » : 20, 21x, 28x, 29 (définition de H-B9), y compris les codes 90x / 93x des budgets votés par
fonction. Budget principal (cbudg = 1) pour Paris, comme la clé de B.
Entrées (lecture seule) :
- data/raw/recoupements/seine_saint_denis_paris/officiel/DGFiP_2025_PARIS_fonction2_par_fonction_compte_API.csv
- data/raw/recoupements/seine_saint_denis_paris/officiel/DGFiP_2025_communes_92_93_94_ecoles_par_fonction_compte_API.csv
- data/raw/collectivites/DGFiP_balances_nature-fonction_2025_communes_ecoles_invest_par_commune_API.csv
- resultats/B1 (élèves des écoles publiques, rentrée 2024).
Sortie : e2b_batiments_ecoles_paris_93.csv
"""
import sys
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
R = Path("C:/Users/chret/Documents/EtatEcole")
OFF = R / "data/raw/recoupements/seine_saint_denis_paris/officiel"
OUT = Path(__file__).resolve().parent


def net(df):
    for c in ("obnetdeb", "obnetcre", "oobdeb", "oobcre"):
        df[c] = df[c].fillna(0)
    return (df["obnetdeb"] - df["oobdeb"]) - (df["obnetcre"] - df["oobcre"])


def code_f(f: str) -> str:
    return f[2:] if (f.startswith("90") or f.startswith("93")) and len(f) > 3 else f


ECOLES = ("20", "21", "28", "29")
ENERGIE = ("6061", "60621", "60622")
ENTRETIEN = ("6152", "6156", "6283")

b1 = pd.read_csv(R / "resultats/B1_depense_publique_par_etablissement_2025.csv", sep=";", encoding="utf-8-sig",
                 low_memory=False, dtype={"code_departement": str, "uai": str, "code_commune_norm": str})
ep = b1[b1["degre"].eq("1er degré") & b1["secteur"].eq("public")]
eleves = {"Paris": ep.loc[ep["code_departement"].eq("75"), "eleves"].sum(),
          "Seine-Saint-Denis": ep.loc[ep["code_departement"].eq("93"), "eleves"].sum()}

# Paris
p = pd.read_csv(OFF / "DGFiP_2025_PARIS_fonction2_par_fonction_compte_API.csv", sep=";", encoding="utf-8-sig",
                dtype={"compte": str, "fonction": str, "cbudg": str})
p["m"] = net(p)
p["f"] = p["fonction"].map(code_f)
# Variante : budget annexe de la Ville (cbudg = 3 = « budget annexe » d'après la structure DGFiP 2024), fonctions 211-213.
pa = p[(p["cbudg"] == "3") & p["f"].str.startswith(ECOLES)]
paris_annexe = {
    "énergie et fluides (6061x, 60621, 60622)": pa.loc[pa["compte"].str.startswith(ENERGIE), "m"].sum(),
    "entretien, maintenance, nettoyage (6152x, 6156, 6283)": pa.loc[pa["compte"].str.startswith(ENTRETIEN), "m"].sum(),
    "fonctionnement total (classe 6 hors 66, 675, 676, 68)": pa.loc[pa["compte"].str.startswith("6") & ~pa["compte"].str.startswith(("66", "675", "676", "68")), "m"].sum(),
}
p = p[(p["cbudg"] == "1") & p["f"].str.startswith(ECOLES)]
paris = {
    "investissement (comptes 20, 21, 23)": p.loc[p["fonction"].str.startswith("90") & p["compte"].str[:2].isin(["20", "21", "23"]), "m"].sum(),
    "énergie et fluides (6061x, 60621, 60622)": p.loc[p["compte"].str.startswith(ENERGIE), "m"].sum(),
    "entretien, maintenance, nettoyage (6152x, 6156, 6283)": p.loc[p["compte"].str.startswith(ENTRETIEN), "m"].sum(),
    "fonctionnement total (classe 6 hors 66, 675, 676, 68)": p.loc[p["compte"].str.startswith("6") & ~p["compte"].str.startswith(("66", "675", "676", "68")), "m"].sum(),
}
# Communes du 93 : fonctionnement par compte (fichier 92/93/94), investissement (fichier par commune)
c = pd.read_csv(OFF / "DGFiP_2025_communes_92_93_94_ecoles_par_fonction_compte_API.csv", sep=";", encoding="utf-8-sig",
                dtype={"compte": str, "fonction": str, "ndept": str, "insee": str})
c["m"] = net(c)
c["f"] = c["fonction"].map(code_f)
c = c[c["ndept"].eq("093") & c["f"].str.startswith(ECOLES)]
inv = pd.read_csv(R / "data/raw/collectivites/DGFiP_balances_nature-fonction_2025_communes_ecoles_invest_par_commune_API.csv",
                  sep=";", encoding="utf-8-sig", dtype={"ndept": str, "insee": str})
inv["m"] = net(inv)
ssd = {
    "investissement (comptes 20, 21, 23)": inv.loc[inv["ndept"].eq("093"), "m"].sum(),
    "énergie et fluides (6061x, 60621, 60622)": c.loc[c["compte"].str.startswith(ENERGIE), "m"].sum(),
    "entretien, maintenance, nettoyage (6152x, 6156, 6283)": c.loc[c["compte"].str.startswith(ENTRETIEN), "m"].sum(),
    "fonctionnement total (classe 6 hors 66, 675, 676, 68)": c.loc[c["compte"].str.startswith("6") & ~c["compte"].str.startswith(("66", "675", "676", "68")), "m"].sum(),
}
lignes = []
for terr, d in (("Paris", paris), ("Paris, budget annexe (cbudg 3)", paris_annexe), ("Seine-Saint-Denis", ssd)):
    for k, v in d.items():
        lignes.append({"territoire": terr, "poste": k, "montant_M€": round(v / 1e6, 1),
                       "euros_par_eleve_public": round(v / eleves[terr.split(",")[0]]),
                       "eleves_publics_rentree2024": int(eleves[terr.split(",")[0]])})
    bati = sum(v for k, v in d.items() if not k.startswith("fonctionnement total"))
    lignes.append({"territoire": terr, "poste": "BÂTIMENTS (investissement + énergie + entretien)",
                   "montant_M€": round(bati / 1e6, 1), "euros_par_eleve_public": round(bati / eleves[terr.split(",")[0]]),
                   "eleves_publics_rentree2024": int(eleves[terr.split(",")[0]])})
out = pd.DataFrame(lignes)
out.to_csv(OUT / "e2b_batiments_ecoles_paris_93.csv", sep=";", index=False, encoding="utf-8-sig")
print(out.to_string(index=False))
