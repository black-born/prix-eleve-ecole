"""Tâche E.1 — Ce que le modèle B montre pour Paris, la Seine-Saint-Denis et la France (lecture seule de B1).

1. Moyennes par élève (pondérées par les élèves = somme des montants / somme des élèves) de chaque ligne de B1,
   pour les écoles, collèges et lycées publics (GT, polyvalents, professionnels, et les trois réunis).
2. Dispersion entre établissements à l'intérieur de Paris et du 93 (P10, médiane, P90 pondérés par les élèves,
   même méthode que resume() du script 04, lignes 527-531).
3. Quelles lignes varient d'un établissement à l'autre dans un même département (min, max, écart-type pondéré,
   et part de la variance du total expliquée par chaque ligne : cov(ligne, total) / var(total), pondérées).

Entrée : C:/Users/chret/Documents/EtatEcole/resultats/B1_depense_publique_par_etablissement_2025.csv (non modifié).
Sorties (dossier de travail) : e1_moyennes_par_ligne.csv, e1_dispersion.csv, e1_variabilite_lignes.csv.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
B1 = Path("C:/Users/chret/Documents/EtatEcole/resultats/B1_depense_publique_par_etablissement_2025.csv")
OUT = Path(__file__).resolve().parent

b = pd.read_csv(B1, sep=";", encoding="utf-8-sig", low_memory=False,
                dtype={"code_departement": str, "uai": str, "code_commune_norm": str})
ETAT = ["etat_enseignants", "etat_remplacement_formation", "etat_vie_scolaire", "etat_pilotage_admin",
        "etat_inclusion_sante_social", "etat_activites_educatives", "etat_aides_familles",
        "etat_forfait_prive_internats", "etat_soutien_administration"]
CT = ["ct_ecoles", "ct_colleges", "ct_lycees", "ct_transports"]
LIGNES = ETAT + CT + ["apu_par_eleve", "etat", "collectivites", "depense_publique"]

# Contrôle : les montants sont des euros par établissement (et non par élève).
ecart = (b["depense_publique"] / b["eleves"] - b["depense_publique_par_eleve"]).abs().max()
somme = (b[ETAT].sum(axis=1) - b["etat"]).abs().max(), (b[CT].sum(axis=1) - b["collectivites"]).abs().max(), \
        (b["etat"] + b["collectivites"] + b["apu_par_eleve"] - b["depense_publique"]).abs().max()
print(f"Contrôle : max |depense_publique/eleves - depense_publique_par_eleve| = {ecart:.3f} € ; "
      f"écarts de sommes (État, CT, total) = {somme}")

LYCEES = ["lycée général et technologique", "lycée polyvalent", "lycée professionnel"]
pub = b["secteur"].eq("public")
GROUPES = {
    "écoles publiques": pub & b["type"].eq("école"),
    "collèges publics": pub & b["type"].eq("collège"),
    "lycées publics (GT + polyvalents + professionnels)": pub & b["type"].isin(LYCEES),
    "lycées GT publics": pub & b["type"].eq("lycée général et technologique"),
    "lycées polyvalents publics": pub & b["type"].eq("lycée polyvalent"),
    "lycées professionnels publics": pub & b["type"].eq("lycée professionnel"),
}
TERRITOIRES = {"Paris": b["code_departement"].eq("75"), "Seine-Saint-Denis": b["code_departement"].eq("93"),
               "France": pd.Series(True, index=b.index)}


def quantile_pondere(x: pd.Series, w: pd.Series, q: float) -> float:
    """Même règle que resume() du script 04 : première valeur dont le poids cumulé atteint q."""
    o = x.sort_values().index
    cw = w.loc[o].cumsum() / w.sum()
    return float(x.loc[o][cw.values >= q].iloc[0])


moy, disp, var = [], [], []
for g, mg in GROUPES.items():
    for t, mt in TERRITOIRES.items():
        d = b[mg & mt]
        n = d["eleves"].sum()
        ligne = {"groupe": g, "territoire": t, "etablissements": len(d), "eleves": int(n)}
        for c in LIGNES:
            ligne[f"{c}_par_eleve"] = d[c].sum() / n
        tot = d["depense_publique"].sum()
        ligne["part_etat_%"] = 100 * d["etat"].sum() / tot
        ligne["part_collectivites_%"] = 100 * d["collectivites"].sum() / tot
        ligne["part_collectivites_hors_transports_%"] = 100 * (d["collectivites"].sum() - d["ct_transports"].sum()) / tot
        ligne["part_apu_%"] = 100 * d["apu_par_eleve"].sum() / tot
        ligne["part_etat_enseignants_%"] = 100 * d["etat_enseignants"].sum() / tot
        moy.append(ligne)
        # Dispersion entre établissements (élèves > 0), pondérée par les élèves.
        x, w = d["depense_publique_par_eleve"], d["eleves"]
        disp.append({"groupe": g, "territoire": t, "etablissements": len(d), "eleves": int(n),
                     "moyenne": tot / n, "P10": quantile_pondere(x, w, 0.10), "mediane": quantile_pondere(x, w, 0.50),
                     "P90": quantile_pondere(x, w, 0.90), "min": x.min(), "max": x.max()})
        # Variabilité de chaque ligne par élève entre établissements du territoire.
        if t == "France":
            continue
        tot_pe = d["depense_publique"] / d["eleves"]
        m_tot = np.average(tot_pe, weights=w)
        v_tot = np.average((tot_pe - m_tot) ** 2, weights=w)
        for c in ETAT + CT + ["apu_par_eleve"]:
            pe = d[c] / d["eleves"]
            m = np.average(pe, weights=w)
            sd = np.sqrt(np.average((pe - m) ** 2, weights=w))
            cov = np.average((pe - m) * (tot_pe - m_tot), weights=w)
            var.append({"groupe": g, "territoire": t, "ligne": c, "moyenne_par_eleve": m, "min_par_eleve": pe.min(),
                        "max_par_eleve": pe.max(), "ecart_type_pondere": sd,
                        "coef_variation_%": 100 * sd / m if m else np.nan,
                        "part_variance_total_%": 100 * cov / v_tot if v_tot else np.nan})

moy = pd.DataFrame(moy)
disp = pd.DataFrame(disp)
var = pd.DataFrame(var)
moy.round(2).to_csv(OUT / "e1_moyennes_par_ligne.csv", sep=";", index=False, encoding="utf-8-sig")
disp.round(2).to_csv(OUT / "e1_dispersion.csv", sep=";", index=False, encoding="utf-8-sig")
var.round(3).to_csv(OUT / "e1_variabilite_lignes.csv", sep=";", index=False, encoding="utf-8-sig")

pd.set_option("display.width", 250, "display.max_columns", 40, "display.max_rows", 400)
cols = ["groupe", "territoire", "etablissements", "eleves", "depense_publique_par_eleve", "etat_par_eleve",
        "etat_enseignants_par_eleve", "ct_ecoles_par_eleve", "ct_colleges_par_eleve", "ct_lycees_par_eleve",
        "ct_transports_par_eleve", "apu_par_eleve_par_eleve", "part_collectivites_%",
        "part_collectivites_hors_transports_%", "part_etat_%", "part_etat_enseignants_%"]
print(moy[cols].round(1).to_string(index=False))
print()
print(disp.round(0).to_string(index=False))
print()
print(var[var["groupe"].isin(["collèges publics", "lycées publics (GT + polyvalents + professionnels)", "écoles publiques"])]
      .round(1).to_string(index=False))
