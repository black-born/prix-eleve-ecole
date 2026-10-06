"""Tâche E.1 (contrôle) — Retrouve les chiffres collés par l'utilisateur (écoles publiques maternelles, élémentaires,
primaires : Paris 15 676 / 16 047 / 15 797 € ; Seine-Saint-Denis 9 417 / 9 911 / 9 969 €) dans le CSV de la carte
(resultats/carte_etablissements_2025.csv, lecture seule) : moyenne = somme(dépense par élève × élèves) / somme(élèves),
par département, type et secteur ; décomposition de l'écart Paris − 93 par composante.
Sortie : e1c_types_ecoles_carte.csv
"""
import sys
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
c = pd.read_csv("C:/Users/chret/Documents/EtatEcole/resultats/carte_etablissements_2025.csv", sep=";",
                encoding="utf-8-sig", low_memory=False, dtype={"code_departement": str, "uai": str})
OUT = Path(__file__).resolve().parent
COMP = ["dont_enseignants_€", "dont_vie_scolaire_direction_encadrement_€", "dont_autres_credits_etat_€", "dont_commune_€",
        "dont_departement_€", "dont_region_€", "dont_transports_scolaires_€", "dont_caf_autres_apu_€"]
c = c[c["secteur"].eq("public")]
lignes = []
for dep_lib, m in (("Paris", c["code_departement"].eq("75")), ("Seine-Saint-Denis", c["code_departement"].eq("93")),
                   ("France", pd.Series(True, index=c.index))):
    for t in ("école maternelle", "école élémentaire", "école primaire", "collège", "lycée général et technologique", "lycée polyvalent",
              "lycée professionnel"):
        d = c[m & c["type"].eq(t)]
        if d.empty:
            continue
        w = d["eleves_rentree2024"].astype(float)
        ligne = {"territoire": dep_lib, "type": t, "etablissements": len(d), "eleves": int(w.sum()),
                 "depense_par_eleve": round((d["depense_publique_par_eleve_€"].astype(float) * w).sum() / w.sum())}
        for k in COMP:
            ligne[k] = round((d[k].astype(float) * w).sum() / w.sum())
        lignes.append(ligne)
out = pd.DataFrame(lignes)
out.to_csv(OUT / "e1c_types_ecoles_carte.csv", sep=";", index=False, encoding="utf-8-sig")
pd.set_option("display.width", 250)
print(out.to_string(index=False))
