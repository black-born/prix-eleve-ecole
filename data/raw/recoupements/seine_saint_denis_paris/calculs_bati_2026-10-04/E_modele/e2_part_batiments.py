"""Tâche E.2 — Part de la dépense publique par élève liée aux bâtiments (investissement + entretien + énergie),
par niveau, France, 2025. Lecture seule des fichiers du projet.

Deux méthodes, toutes deux à partir des balances DGFiP 2025 (budgets principaux) extraites par le projet :

M1 « comptes directs » : dépenses de bâtiment des collectivités de rattachement / élèves du public concernés.
   - écoles : communes à comptabilité fonctionnelle (14 145,4 M€) / élèves du public de ces communes
     (3 798 310 en année civile 2025, couverture 70,61 %, NOTES § 8.4). Rapporter au seul champ couvert revient à
     l'extrapolation « coût moyen des communes couvertes » (méthode OFGL, M1 du § 8.5), retenue par le projet.
   - collèges : départements + cas particuliers (Paris, Métropole de Lyon, CTU), comme colleges_tot du script 04
     (lignes 371-372) / collégiens du public (base_2d, élèves de niveau collège des établissements publics).
   - lycées : régions et CTU, hors sous-fonction 223 « Lycées privés », × part « champ » du public (0,8649 : hors
     post-bac et lycées agricoles, H-B11, B4) / lycéens du public (GT + professionnels).
   Variante étroite : constructions et rénovations (231x, 2131x, 2135x, 217x, 2317, 236-238) + énergie + entretien.
   Variante large : tout l'investissement (y compris équipement, études, subventions d'équipement) + énergie + entretien.
M2 « structure de B » (méthode du script 05, H-D2) : part « investissement » + « entretien, énergie » de la structure
   nationale 2025 de chaque niveau, appliquée aux lignes ct_ecoles, ct_colleges, ct_lycees de B1.

Rapports : montants par élève / dépense publique totale par élève de B (B2 ; écoles publiques 9 808 €, collèges
publics 11 451 €, lycées publics 14 354 €). Ordre de grandeur, une seule année (H-G5 : investissement non amorti).
Sorties : e2_part_batiments.csv.
"""
import sys
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
R = Path("C:/Users/chret/Documents/EtatEcole")
EX = R / "data/raw/collectivites/extractions"
OUT = Path(__file__).resolve().parent

pos = pd.read_csv(EX / "DGFiP_2025_enseignement_postes_cles_budgets_principaux.csv", sep=";")
ssf = pd.read_csv(EX / "DGFiP_2025_enseignement_niveau_sousfonction_nature.csv", sep=";")
b1 = pd.read_csv(R / "resultats/B1_depense_publique_par_etablissement_2025.csv", sep=";", encoding="utf-8-sig",
                 low_memory=False, dtype={"code_departement": str, "uai": str, "code_commune_norm": str})
b2 = pd.read_csv(R / "data/processed/base_2d_rentree2024.csv", sep=";", low_memory=False,
                 dtype={"code_departement": str, "uai": str})
env = pd.read_csv(R / "resultats/B0_enveloppes_reparties.csv", sep=";")

CONSTR = "Constructions, rénovations"
ENERGIE = "Énergie et fluides"
ENTRET = "Entretien, maintenance, nettoyage"


def postes(niv, per):
    x = pos[(pos["niveau"] == niv) & (pos["perimetre"] == per)]
    inv = x.loc[x["section"] == "investissement", "montant_M€"].sum()
    get = lambda deb: x.loc[x["poste"].str.startswith(deb), "montant_M€"].sum()  # noqa: E731
    return {"I_total": inv, "constructions": get(CONSTR), "energie": get(ENERGIE), "entretien": get(ENTRET),
            "total": x["montant_M€"].sum(),
            "dotations_EPLE_publics": get("Dotations de fonctionnement aux établissements publics")
            + get("Dotations de fonctionnement collèges/lycées non subdivisées")}


PL = "collèges-lycées (cas particuliers : Paris, Métropole de Lyon)"
ecoles = postes("Communes (y.c. Paris)", "écoles (1er degré)")
col_parts = [postes("Départements", "collèges"), postes("Régions et CTU", "collèges (CTU : Corse, Guyane, Martinique)"),
             postes("Communes (y.c. Paris)", PL), postes("GFP (y.c. Métropole de Lyon, EPT)", PL)]
colleges = {k: sum(p[k] for p in col_parts) for k in col_parts[0]}
lycees = postes("Régions et CTU", "lycées")
s223 = ssf[(ssf["niveau"] == "Régions et CTU") & (ssf["perimetre"] == "lycées") & (ssf["budget"] == "budget principal")
           & ssf["sous_fonction"].str.startswith("223")]
i223 = s223.loc[s223["section"] == "investissement", "montant_M€"].sum()
i223_nat = s223[s223["section"] == "investissement"].groupby("nature")["montant_M€"].sum().round(1).to_dict()
PART_CHAMP_PUBLIC = 0.8649  # B4_indicateurs_methode.csv, « Part champ des dépenses lycées des régions (public) »

# Élèves
ELEVES_COUVERTS_ECOLES = 3_798_310  # NOTES.md § 8.4 (année civile 2025, hors COM, communes couvertes)
pub2 = b2[(b2["secteur"] == "public") & (b2["eleves"] > 0)]
collegiens_pub = float(pub2["eleves_college"].fillna(0).sum())
lyceens_pub = float((pub2["eleves_lycee_gt"].fillna(0) + pub2["eleves_lycee_pro"].fillna(0)).sum())

TOT_B = {"écoles publiques": 9807.8, "collèges publics": 11451.0, "lycées publics": 14353.6}  # e1 / B2
lignes = []


def ajoute(niveau, methode, variante, montant_meur, eleves, detail):
    pe = montant_meur * 1e6 / eleves
    lignes.append({"niveau": niveau, "methode": methode, "variante": variante, "montant_M€": round(montant_meur, 1),
                   "eleves": round(eleves), "euros_par_eleve": round(pe), "total_B_par_eleve": TOT_B[niveau],
                   "part_du_total_%": round(100 * pe / TOT_B[niveau], 1), "detail": detail})


# ---- M1 comptes directs
ajoute("écoles publiques", "M1 comptes directs", "étroite",
       ecoles["constructions"] + ecoles["energie"] + ecoles["entretien"], ELEVES_COUVERTS_ECOLES,
       f"constructions {ecoles['constructions']:.1f} + énergie {ecoles['energie']:.1f} + entretien {ecoles['entretien']:.1f} M€ (communes couvertes)")
ajoute("écoles publiques", "M1 comptes directs", "large",
       ecoles["I_total"] + ecoles["energie"] + ecoles["entretien"], ELEVES_COUVERTS_ECOLES,
       f"investissement {ecoles['I_total']:.1f} + énergie + entretien (communes couvertes)")
ajoute("écoles publiques", "M1 comptes directs", "investissement seul",
       ecoles["I_total"], ELEVES_COUVERTS_ECOLES, "investissement des communes couvertes")
ajoute("collèges publics", "M1 comptes directs", "étroite",
       colleges["constructions"] + colleges["energie"] + colleges["entretien"], collegiens_pub,
       f"constructions {colleges['constructions']:.1f} + énergie {colleges['energie']:.1f} + entretien {colleges['entretien']:.1f} M€ (départements, Paris, ML, CTU)")
ajoute("collèges publics", "M1 comptes directs", "large",
       colleges["I_total"] + colleges["energie"] + colleges["entretien"], collegiens_pub,
       f"investissement {colleges['I_total']:.1f} + énergie + entretien")
ajoute("collèges publics", "M1 comptes directs", "investissement seul", colleges["I_total"], collegiens_pub,
       "investissement (départements, Paris, ML, CTU)")
ajoute("collèges publics", "M1 comptes directs", "large + dotations aux EPLE (majorant)",
       colleges["I_total"] + colleges["energie"] + colleges["entretien"] + colleges["dotations_EPLE_publics"],
       collegiens_pub, f"+ dotations de fonctionnement aux collèges publics et non subdivisées {colleges['dotations_EPLE_publics']:.1f} M€ (elles paient aussi l'énergie et l'entretien courant, mais pas seulement)")
lyc_constr = lycees["constructions"] * PART_CHAMP_PUBLIC
ajoute("lycées publics", "M1 comptes directs", "étroite",
       (lycees["constructions"] + lycees["energie"] + lycees["entretien"]) * PART_CHAMP_PUBLIC, lyceens_pub,
       f"(constructions {lycees['constructions']:.1f} + énergie {lycees['energie']:.1f} + entretien {lycees['entretien']:.1f}) × {PART_CHAMP_PUBLIC} (régions et CTU)")
ajoute("lycées publics", "M1 comptes directs", "large",
       (lycees["I_total"] - i223 + lycees["energie"] + lycees["entretien"]) * PART_CHAMP_PUBLIC, lyceens_pub,
       f"(investissement {lycees['I_total']:.1f} − sous-fonction 223 {i223:.1f} + énergie + entretien) × {PART_CHAMP_PUBLIC}")
ajoute("lycées publics", "M1 comptes directs", "investissement seul",
       (lycees["I_total"] - i223) * PART_CHAMP_PUBLIC, lyceens_pub, "investissement hors 223 × part champ")
ajoute("lycées publics", "M1 comptes directs", "large + dotations aux EPLE (majorant)",
       (lycees["I_total"] - i223 + lycees["energie"] + lycees["entretien"] + lycees["dotations_EPLE_publics"]) * PART_CHAMP_PUBLIC,
       lyceens_pub, f"+ dotations de fonctionnement aux lycées publics {lycees['dotations_EPLE_publics']:.1f} M€ × part champ")

# ---- M2 structure de B (reprise de structure() du script 05, lignes 145-163, et de RETRAIT_223, lignes 170-177)
BAT = "Bâtiments : construction, rénovation, grosses réparations, équipement"
ENT = "Entretien, énergie et fluides des bâtiments"
FONCT = "Dotations et autres frais de fonctionnement (fournitures, caisses des écoles…)"


def structure(niv, per, exclure="établissements privés|6558", retrait=None):
    x = pos[(pos["niveau"] == niv) & (pos["perimetre"] == per)].copy()
    x = x[~x["poste"].str.contains(exclure)]

    def classe(r):
        if r["section"] == "investissement":
            return BAT
        if r["poste"].startswith("Personnel"):
            return "Personnel"
        if r["poste"].startswith(("Entretien", "Énergie")):
            return ENT
        if r["poste"].startswith("Alimentation"):
            return "Restauration"
        return FONCT
    x["classe"] = x.apply(classe, axis=1)
    s = x.groupby("classe")["montant_M€"].sum()
    for c, m in (retrait or {}).items():
        s[c] -= m
    return s / s.sum()


dot_prv_lyc = pos[(pos["niveau"] == "Régions et CTU") & (pos["perimetre"] == "lycées")
                  & pos["poste"].str.contains("établissements privés")]["montant_M€"].sum()
RETRAIT_223 = {BAT: i223, FONCT: s223.loc[s223["section"] == "fonctionnement", "montant_M€"].sum() - dot_prv_lyc}
STRUCT = {"ct_ecoles": structure("Communes (y.c. Paris)", "écoles (1er degré)", "établissements privés|6558|6067"),
          "ct_colleges": structure("Départements", "collèges"),
          "ct_lycees": structure("Régions et CTU", "lycées", retrait=RETRAIT_223)}
eco_pub = env[(env["poste"] == "ct_ecoles") & (env["population"] == "écoles publiques")]
PART_FOURN = float(eco_pub.loc[eco_pub["enveloppe"].str.contains("fournitures"), "reparti_M€"].sum() / eco_pub["reparti_M€"].sum())
print("Structures (part bâtiments / entretien-énergie) :",
      {k: (round(v.get(BAT, 0), 4), round(v.get(ENT, 0), 4)) for k, v in STRUCT.items()}, "part fournitures écoles", round(PART_FOURN, 4))

LYC = ["lycée général et technologique", "lycée polyvalent", "lycée professionnel"]
pub = b1["secteur"].eq("public")
GROUPES = {"écoles publiques": pub & b1["type"].eq("école"), "collèges publics": pub & b1["type"].eq("collège"),
           "lycées publics": pub & b1["type"].isin(LYC)}
TERR = {"France": pd.Series(True, index=b1.index), "Paris": b1["code_departement"].eq("75"),
        "Seine-Saint-Denis": b1["code_departement"].eq("93")}
m2 = []
for g, mg in GROUPES.items():
    for t, mt in TERR.items():
        d = b1[mg & mt]
        n = d["eleves"].sum()
        inv = ent = 0.0
        for col in ("ct_ecoles", "ct_colleges", "ct_lycees"):
            m = d[col].sum() * ((1 - PART_FOURN) if col == "ct_ecoles" else 1)
            inv += m * STRUCT[col].get(BAT, 0)
            ent += m * STRUCT[col].get(ENT, 0)
        tot = d["depense_publique"].sum() / n
        m2.append({"niveau": g, "territoire": t, "eleves": int(n), "investissement_par_eleve": round(inv / n),
                   "entretien_energie_par_eleve": round(ent / n), "batiments_par_eleve": round((inv + ent) / n),
                   "total_B_par_eleve": round(tot), "part_batiments_%": round(100 * (inv + ent) / n / tot, 1),
                   "etat_enseignants_par_eleve": round(d["etat_enseignants"].sum() / n),
                   "part_etat_enseignants_%": round(100 * d["etat_enseignants"].sum() / d["depense_publique"].sum(), 1),
                   "enseignants_y_c_remplacement_formation_par_eleve": round((d["etat_enseignants"].sum() + d["etat_remplacement_formation"].sum()) / n),
                   "part_enseignants_y_c_rempl_%": round(100 * (d["etat_enseignants"].sum() + d["etat_remplacement_formation"].sum()) / d["depense_publique"].sum(), 1),
                   "part_etat_%": round(100 * d["etat"].sum() / d["depense_publique"].sum(), 1)})
        if t == "France":
            ajoute(g, "M2 structure de B (H-D2)", "investissement + entretien et énergie", (inv + ent) / 1e6, n,
                   f"investissement {inv / n:.0f} € + entretien et énergie {ent / n:.0f} € par élève")

# ---- M3 « rapport à A » (compte de l'éducation, DEPP 2025p, public et privé, apprentis compris au 2nd degré) :
# dépense de bâtiment de tous les établissements publics / élèves de l'année civile de A (A1) / dépense publique par
# élève de A (A1 : 8 962 € au 1er degré, 10 470 € au 2nd). Écoles : montant par élève des communes couvertes × élèves du
# public hors COM (année civile 2025 : 5 379 623, NOTES § 8.4), soit l'extrapolation M1 du projet (NOTES § 8.5).
a1 = pd.read_csv(R / "resultats/A1_depense_publique_par_eleve.csv", sep=";", encoding="utf-8-sig")
a = a1[a1["annee"] == "2025p"].set_index("niveau")
A_1D = a.loc["1er degré"]
A_2D = a.loc[[i for i in a.index if i.startswith("2nd degré")][0]]
ELEVES_PUBLIC_1D_HORS_COM = 5_379_623
for var, num in (("étroite", ecoles["constructions"] + ecoles["energie"] + ecoles["entretien"]),
                 ("large", ecoles["I_total"] + ecoles["energie"] + ecoles["entretien"])):
    tot = num * 1e6 / ELEVES_COUVERTS_ECOLES * ELEVES_PUBLIC_1D_HORS_COM
    pe = tot / float(A_1D["effectif_implicite_annee_civile"])
    lignes.append({"niveau": "1er degré (A, public + privé)", "methode": "M3 rapport à A (DEPP 2025p)", "variante": var,
                   "montant_M€": round(tot / 1e6, 1), "eleves": round(float(A_1D["effectif_implicite_annee_civile"])),
                   "euros_par_eleve": round(pe), "total_B_par_eleve": float(A_1D["depense_publique_par_eleve_€"]),
                   "part_du_total_%": round(100 * pe / float(A_1D["depense_publique_par_eleve_€"]), 1),
                   "detail": "écoles : montant par élève des communes couvertes × élèves du public hors COM ; dénominateur : élèves de A (année civile)"})
for var, num in (("étroite", colleges["constructions"] + colleges["energie"] + colleges["entretien"]
                  + (lycees["constructions"] + lycees["energie"] + lycees["entretien"]) * PART_CHAMP_PUBLIC),
                 ("large", colleges["I_total"] + colleges["energie"] + colleges["entretien"]
                  + (lycees["I_total"] - i223 + lycees["energie"] + lycees["entretien"]) * PART_CHAMP_PUBLIC)):
    pe = num * 1e6 / float(A_2D["effectif_implicite_annee_civile"])
    lignes.append({"niveau": "2nd degré (A, public + privé, apprentis compris)", "methode": "M3 rapport à A (DEPP 2025p)", "variante": var,
                   "montant_M€": round(num, 1), "eleves": round(float(A_2D["effectif_implicite_annee_civile"])),
                   "euros_par_eleve": round(pe), "total_B_par_eleve": float(A_2D["depense_publique_par_eleve_€"]),
                   "part_du_total_%": round(100 * pe / float(A_2D["depense_publique_par_eleve_€"]), 1),
                   "detail": "collèges + lycées (part du public hors post-bac et agricole) ; dénominateur : élèves de A"})
m1 = pd.DataFrame(lignes)
m2 = pd.DataFrame(m2)
m1.to_csv(OUT / "e2_part_batiments.csv", sep=";", index=False, encoding="utf-8-sig")
m2.to_csv(OUT / "e2_part_batiments_structure_B_par_territoire.csv", sep=";", index=False, encoding="utf-8-sig")
pd.set_option("display.width", 250, "display.max_colwidth", 140)
print(f"collégiens du public : {collegiens_pub:,.0f} ; lycéens du public : {lyceens_pub:,.0f}")
print(f"Sous-fonction 223 (lycées privés), investissement : {i223:.1f} M€ {i223_nat}")
print("Collèges (somme des 4 périmètres) :", {k: round(v, 1) for k, v in colleges.items()})
print("Lycées :", {k: round(v, 1) for k, v in lycees.items()})
print("Écoles :", {k: round(v, 1) for k, v in ecoles.items()})
print(m1.drop(columns=["detail"]).to_string(index=False))
print(m2.to_string(index=False))
