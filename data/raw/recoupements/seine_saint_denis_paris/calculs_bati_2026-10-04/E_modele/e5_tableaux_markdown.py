"""Mise en forme (français) des tableaux de la tâche E à partir des CSV produits par e1 à e3. Sortie à l'écran."""
import sys
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
D = Path(__file__).resolve().parent


def fr(x, dec=0):
    if pd.isna(x):
        return "—"
    s = f"{x:,.{dec}f}".replace(",", " ").replace(".", ",")
    return s.replace("-", "−")


m = pd.read_csv(D / "e1_moyennes_par_ligne.csv", sep=";", encoding="utf-8-sig")
LIB = [("depense_publique_par_eleve", "**Total**"), ("etat_par_eleve", "État"),
       ("etat_enseignants_par_eleve", "· enseignants (ETP ou heures × indice, coût moyen national)"),
       ("etat_remplacement_formation_par_eleve", "· remplacement et formation (par élève)"),
       ("etat_vie_scolaire_par_eleve", "· vie scolaire (ETP de l'établissement)"),
       ("etat_pilotage_admin_par_eleve", "· direction, administration, encadrement"),
       ("etat_inclusion_sante_social_par_eleve", "· AESH, santé, social, orientation (par élève)"),
       ("etat_aides_familles_par_eleve", "· bourses et fonds sociaux (par élève)"),
       ("etat_activites_educatives_par_eleve", "· actions éducatives (par élève)"),
       ("etat_forfait_prive_internats_par_eleve", "· internats (par élève)"),
       ("etat_soutien_administration_par_eleve", "· administration centrale et académique (par élève)"),
       ("ct_ecoles_par_eleve", "Commune (clé communale)"), ("ct_colleges_par_eleve", "Département (clé départementale)"),
       ("ct_lycees_par_eleve", "Région (clé régionale)"), ("ct_transports_par_eleve", "Transports scolaires (par élève)"),
       ("apu_par_eleve_par_eleve", "CAF et autres APU"),
       ("part_collectivites_hors_transports_%", "Part de la commune / du département / de la région dans le total (%)"),
       ("part_etat_enseignants_%", "Part de la ligne « enseignants » de l'État (%)")]
for g in ("écoles publiques", "collèges publics", "lycées publics (GT + polyvalents + professionnels)"):
    x = m[m["groupe"] == g].set_index("territoire")
    print(f"\n### {g}\n")
    print("| 2025, € par élève (B1) | Paris | Seine-Saint-Denis | France |")
    print("|---|---|---|---|")
    print(f"| Établissements / élèves (rentrée 2024) | {fr(x.loc['Paris','etablissements'])} / {fr(x.loc['Paris','eleves'])} | "
          f"{fr(x.loc['Seine-Saint-Denis','etablissements'])} / {fr(x.loc['Seine-Saint-Denis','eleves'])} | "
          f"{fr(x.loc['France','etablissements'])} / {fr(x.loc['France','eleves'])} |")
    for col, lib in LIB:
        vals = [x.loc[t, col] for t in ("Paris", "Seine-Saint-Denis", "France")]
        if all(abs(v) < 0.5 for v in vals) and not col.startswith("part"):
            continue
        dec = 1 if col.startswith("part") else 0
        print(f"| {lib} | " + " | ".join(fr(v, dec) for v in vals) + " |")

d = pd.read_csv(D / "e1_dispersion.csv", sep=";", encoding="utf-8-sig")
print("\n### Dispersion\n")
print("| Établissements publics, 2025 (B1) | Territoire | Établissements | Moyenne | P10 | Médiane | P90 | Min | Max |")
print("|---|---|---|---|---|---|---|---|---|")
for _, r in d.iterrows():
    print(f"| {r['groupe']} | {r['territoire']} | {fr(r['etablissements'])} | {fr(r['moyenne'])} | {fr(r['P10'])} | {fr(r['mediane'])} | {fr(r['P90'])} | {fr(r['min'])} | {fr(r['max'])} |")

v = pd.read_csv(D / "e1_variabilite_lignes.csv", sep=";", encoding="utf-8-sig")
print("\n### Variabilité des lignes\n")
print("| Groupe | Territoire | Ligne | Moyenne € | Min € | Max € | Coef. de variation % | Part de la variance du total % |")
print("|---|---|---|---|---|---|---|---|")
for _, r in v.iterrows():
    if r["moyenne_par_eleve"] == 0:
        continue
    print(f"| {r['groupe']} | {r['territoire']} | {r['ligne']} | {fr(r['moyenne_par_eleve'])} | {fr(r['min_par_eleve'])} | {fr(r['max_par_eleve'])} | {fr(r['coef_variation_%'],1)} | {fr(r['part_variance_total_%'],1)} |")

b = pd.read_csv(D / "e2_part_batiments.csv", sep=";", encoding="utf-8-sig")
print("\n### Bâtiments\n")
print("| Niveau | Méthode | Variante | Montant (M€) | Élèves | € par élève | Total B par élève | Part % |")
print("|---|---|---|---|---|---|---|---|")
for _, r in b.iterrows():
    print(f"| {r['niveau']} | {r['methode']} | {r['variante']} | {fr(r['montant_M€'],1)} | {fr(r['eleves'])} | {fr(r['euros_par_eleve'])} | {fr(r['total_B_par_eleve'])} | {fr(r['part_du_total_%'],1)} |")

s = pd.read_csv(D / "e3b_series_effectifs_publics.csv", sep=";", encoding="utf-8-sig")
print("\n### Séries\n")
for niv in ("écoles publiques", "collèges publics (établissements de type collège, ancien jeu)", "collèges publics (niveau collège)",
            "lycées publics (établissements de type lycée, post-bac compris, ancien jeu)", "lycéens du public (GT + pro, niveaux lycée)"):
    x = s[s["niveau"] == niv].pivot_table(index="rentree", columns="territoire", values="eleves")
    print(niv, {int(k): (fr(r['Paris']), fr(r['Seine-Saint-Denis']), fr(r['France'])) for k, r in x.iterrows()})
