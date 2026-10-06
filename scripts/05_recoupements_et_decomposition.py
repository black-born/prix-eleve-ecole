"""Recoupements indépendants, sensibilité aux pensions et décomposition de la dépense publique par élève.

1. Comptabilité nationale (INSEE, COFOG 2024) : fourchette de dépense publique par élève.
2. Collecte internationale UOE (Eurostat, données DEPP 2023) et OCDE (Regards sur l'éducation 2026).
3. Comparaison des approches A (compte de l'éducation) et B (par établissement).
4. Sensibilité à la convention des pensions de l'État (CAS Pensions).
5. Décomposition de la dépense publique par élève (approche B) en postes lisibles :
   enseignants, autres personnels, bâtiments, fonctionnement, activités annexes, aides, administration.
Hypothèses : H-C1 à H-C4 et H-D1 à H-D3 dans hypotheses.md.
"""
import pandas as pd

from commun import BRUT, RACINE, RESULTATS, Classeur, Journal, ecrire_csv

journal = Journal()
REC = BRUT / "recoupements"
DEPP = BRUT / "depp_compte_education"

a1 = pd.read_csv(RESULTATS / "A1_depense_publique_par_eleve.csv", sep=";")
a6 = pd.read_csv(RESULTATS / "A6_variantes_de_perimetre.csv", sep=";")
e1 = pd.read_csv(RESULTATS / "E1_effectifs_nationaux.csv", sep=";")
b2 = pd.read_csv(RESULTATS / "B2_agregats_et_distribution.csv", sep=";")
etab = pd.read_csv(RESULTATS / "B1_depense_publique_par_etablissement_2025.csv", sep=";", low_memory=False)

# ------------------------------------------------------------------ 1. COFOG 2024 (INSEE, tableau 3.307)
cofog = Classeur(REC / "insee_cofog2024_T_3307.xlsx", journal)
COFOG = {code: cofog.lire_cellule(f"cofog.2024.{code}", "T_3307", f"T{r}", libelle_ligne=code, col_libelle="C",
                                  libelle_colonne="2024", ligne_entete=4) * 1e9
         for code, r in (("GF0901", 68), ("GF0902", 69), ("GF0905", 72), ("GF0906", 73), ("GF0908", 75))}
eff_civ_2024_men = float(e1.loc[e1["niveau"].str.startswith("1er + 2nd"), "annee_civile_2024"].iloc[0])
eff_depp_2024 = float(a1.loc[(a1["annee"] == "2024p") & a1["niveau"].str.startswith("Ensemble"),
                             "effectif_implicite_annee_civile"].iloc[0])
bas = COFOG["GF0901"] + COFOG["GF0902"]
haut = bas + COFOG["GF0906"] + COFOG["GF0908"]
c1 = [
    {"indicateur": "COFOG 09.1 + 09.2 (préélémentaire, primaire, secondaire)", "montant_Md€": round(bas / 1e9, 2),
     "par_eleve_MEN_€": round(bas / eff_civ_2024_men), "par_eleve_champ_DEPP_€": round(bas / eff_depp_2024),
     "lecture": "borne basse : exclut les services annexes (cantines, internats, transports, bourses)"},
    {"indicateur": "… + 09.6 (services annexes) + 09.8 (n.c.a.)", "montant_Md€": round(haut / 1e9, 2),
     "par_eleve_MEN_€": round(haut / eff_civ_2024_men), "par_eleve_champ_DEPP_€": round(haut / eff_depp_2024),
     "lecture": "borne haute : 09.6 inclut aussi des services du supérieur (CROUS, bourses)"},
]
a_2024 = float(a1.loc[(a1["annee"] == "2024p") & a1["niveau"].str.startswith("Ensemble"),
                      "depense_publique_par_eleve_€"].iloc[0])
c1.append({"indicateur": "Approche A, même année (2024p), pour comparaison", "montant_Md€": "",
           "par_eleve_MEN_€": "", "par_eleve_champ_DEPP_€": a_2024, "lecture": "compte de l'éducation (DEPP)"})
ecrire_csv(RESULTATS / "C1_recoupement_COFOG_2024.csv", c1)

# ------------------------------------------------------------------ 2. UOE (Eurostat) et OCDE, données 2023
f09 = pd.read_csv(DEPP / "eurostat_educ_uoe_fine09_FR_EUR_2019-.csv")
f09 = f09[f09["TIME_PERIOD"] == 2023].set_index("isced11")["OBS_VALUE"]
f10 = pd.read_csv(DEPP / "eurostat_educ_uoe_fine10_FR_NR_2019-.csv")
f10 = f10[(f10["TIME_PERIOD"] == 2023)]
if "worktime" in f10.columns:
    f10 = f10[f10["worktime"] == "TOT_FTE"]
if "sector" in f10.columns:
    f10 = f10[f10["sector"] == "TOT_SEC"]
fte = f10.groupby("isced11")["OBS_VALUE"].sum()
c2 = []
for lib, cites in (("Préélémentaire", ["ED02"]), ("Élémentaire", ["ED1"]), ("Collège", ["ED2"]),
                   ("Lycée (y c. apprentis)", ["ED3"]), ("1er degré", ["ED02", "ED1"]), ("2nd degré", ["ED2", "ED3"]),
                   ("Ensemble scolaire", ["ED02", "ED1", "ED2", "ED3"])):
    v = sum(f09[c] * fte[c] for c in cites) / sum(fte[c] for c in cites)
    c2.append({"source": "Eurostat UOE fine09 (DEPP), dépense publique par élève ETP", "annee": 2023, "niveau": lib,
               "euros": round(v), "remarque": "valeur publiée" if len(cites) == 1 else "moyenne calculée ici, pondérée par les élèves ETP"})
oe = pd.read_csv(REC / "oecd_sdmx_EAG_depense_par_eleve_FRA_OCDE_UE25_2019-2023.csv", low_memory=False)
oe = oe[(oe["EXP_SOURCE"] == "S13") & (oe["EXP_DESTINATION"] == "INST_EDU") & (oe["EXPENDITURE_TYPE"] == "DIR_EXP")
        & (oe["TIME_PERIOD"] == 2023)]
for lib, lev in (("Préélémentaire", "ISCED11_02"), ("Élémentaire", "ISCED11_1"), ("Collège", "ISCED11_2"),
                 ("Lycée (y c. apprentis)", "ISCED11_3")):
    for zone in ("FRA", "OECD", "EU25"):
        for unite, lib_u in (("USD_PPP_ST", "dollars PPA"), ("XDC_ST", "euros")):
            x = oe[(oe["REF_AREA"] == zone) & (oe["EDUCATION_LEV"] == lev) & (oe["UNIT_MEASURE"] == unite)]
            if len(x) and pd.notna(x["OBS_VALUE"].iloc[0]) and not (zone != "FRA" and unite == "XDC_ST"):
                c2.append({"source": f"OCDE EAG 2026, dépense publique directe par élève ETP ({lib_u})", "annee": 2023,
                           "niveau": f"{lib} — {zone}", "euros": round(float(x["OBS_VALUE"].iloc[0])),
                           "remarque": lib_u})
ecrire_csv(RESULTATS / "C2_recoupement_UOE_OCDE_2023.csv", c2)

# ------------------------------------------------------------------ 3. Comparaison des approches A et B (2025)
def a_val(niveau_debut):
    return float(a1.loc[(a1["annee"] == "2025p") & a1["niveau"].str.startswith(niveau_debut),
                        "depense_publique_par_eleve_€"].iloc[0])


def b_val(groupe, modalite):
    return float(b2.loc[(b2["groupe"] == groupe) & (b2["modalite"] == modalite), "depense_publique_par_eleve_€"].iloc[0])


hors_app = a6[a6["variante"].str.contains("centrale")].iloc[0]
c3 = []
for lib, a, ah, b in (("1er degré", a_val("1er"), hors_app["1er_degre_€"], b_val("Degré", "1er degré")),
                      ("2nd degré", a_val("2nd"), hors_app["2nd_degre_€"], b_val("Degré", "2nd degré")),
                      ("Ensemble", a_val("Ensemble"), hors_app["ensemble_€"],
                       b_val("Ensemble 1er + 2nd degrés", "tous"))):
    c3.append({"niveau": lib, "A_convention_DEPP_€": round(a), "A_hors_apprentis_€": int(ah),
               "B_par_etablissement_€": round(b), "ecart_B_vs_A_hors_apprentis_%": round(100 * (b / ah - 1), 1)})
ecrire_csv(RESULTATS / "C3_comparaison_A_B.csv", c3)

# ------------------------------------------------------------------ 4. Sensibilité : convention des pensions
# Contributions au CAS Pensions 2025 par programme (RAP 2025) ; part « dans le champ » = part des crédits du
# programme réellement répartis dans B. Taux alternatifs (H-C3) : 34,7 % (IPP : taux d'équilibre 2020 d'un compte
# corrigé du déséquilibre démographique ; borne haute du CAE) et 25,44 % (borne basse du CAE), au lieu de 78,28 % + 0,32 %.
cas = pd.read_csv(BRUT / "couts_personnels" / "TRANSCRIPTION_titre2_par_programme_CAS_Pensions.csv", sep=";")
cas = cas[(cas["annee"] == 2025) & (cas["nature"] == "execution")].set_index("programme")
env = pd.read_csv(RESULTATS / "B0_enveloppes_reparties.csv", sep=";")
act = pd.read_csv(RACINE / "data/raw/budget_etat/extractions/rap2025_execution_par_action_2024_2025.csv", sep=";")
total_prog = act.groupby("programme")["CP_conso_2025"].sum()
reparti_prog = {p: env.loc[env["enveloppe"].str.startswith(f"P{p}"), "reparti_M€"].sum() * 1e6
                for p in (139, 140, 141, 214, 230)}
cas_champ = sum(float(cas.loc[p, "contributions_CAS_Pensions_total_EUR"]) * reparti_prog[p] / total_prog[p]
                for p in reparti_prog)
TAUX_CAS = 78.28 + 0.32
eleves_b = float(etab["eleves"].sum())
eleves_a = float(a1.loc[(a1["annee"] == "2025p") & a1["niveau"].str.startswith("Ensemble"),
                        "effectif_implicite_annee_civile"].iloc[0])
c4 = [{"indicateur": "Contributions au CAS Pensions dans le champ de l'approche B (2025)",
       "valeur": round(cas_champ / 1e9, 2), "unite": "Md€"}]
for taux, lib in ((34.7, "34,7 % (IPP, taux d'équilibre corrigé 2020 ; borne haute du CAE)"),
                  (25.44, "25,44 % (borne basse du CAE)")):
    baisse = cas_champ * (1 - taux / TAUX_CAS)
    c4 += [{"indicateur": f"Baisse avec un taux de {lib}", "valeur": round(baisse / 1e9, 2), "unite": "Md€"},
           {"indicateur": f"  effet par élève de B (11,9 M d'élèves) — taux {taux}", "valeur": round(-baisse / eleves_b),
            "unite": "€"},
           {"indicateur": f"  effet par élève de A (12,6 M d'élèves, même montant) — taux {taux}",
            "valeur": round(-baisse / eleves_a), "unite": "€"}]
ecrire_csv(RESULTATS / "C4_sensibilite_pensions.csv", c4)

# ------------------------------------------------------------------ 5. Décomposition (approche B, 2025)
# Répartition des dépenses des collectivités par nature : structure 2025 des balances DGFiP (H-D2).
COLL_EXTR = RACINE / "data/raw/collectivites/extractions"
pos = pd.read_csv(COLL_EXTR / "DGFiP_2025_enseignement_postes_cles_budgets_principaux.csv", sep=";")
ssf = pd.read_csv(COLL_EXTR / "DGFiP_2025_enseignement_niveau_sousfonction_nature.csv", sep=";")
BATIMENTS = "Bâtiments : construction, rénovation, grosses réparations, équipement"
FONCTIONNEMENT = "Dotations et autres frais de fonctionnement (fournitures, caisses des écoles…)"


def structure(niv, per, exclure="établissements privés|6558", retrait=None):
    """Parts de chaque classe de dépense ; `retrait` = montants (M€) à retirer de certaines classes."""
    x = pos[(pos["niveau"] == niv) & (pos["perimetre"] == per)].copy()
    x = x[~x["poste"].str.contains(exclure)]  # le privé est traité à part
    def classe(r):
        if r["section"] == "investissement":
            return BATIMENTS
        if r["poste"].startswith("Personnel"):
            return "Personnels des collectivités (ATSEM, agents d'entretien et de restauration)"
        if r["poste"].startswith(("Entretien", "Énergie")):
            return "Entretien, énergie et fluides des bâtiments"
        if r["poste"].startswith("Alimentation"):
            return "Restauration scolaire et activités (achats, prestations)"
        return FONCTIONNEMENT
    x["classe"] = x.apply(classe, axis=1)
    s = x.groupby("classe")["montant_M€"].sum()
    for c, m in (retrait or {}).items():
        s[c] -= m
    return s / s.sum()


# Écoles : le montant DEPP est hors fournitures scolaires (compte 6067), ajoutées à part dans B (H-B8) ; on le ventile
# donc avec la structure hors 6067, et la part « fournitures » des écoles publiques va aux frais de fonctionnement.
# Lycées : le script 04 retire des lycées publics toute la sous-fonction 223 « Lycées privés » ; on retire donc aussi de
# la structure la partie de cette sous-fonction autre que les dotations au privé (déjà exclues par leur compte).
s223 = ssf[(ssf["niveau"] == "Régions et CTU") & (ssf["perimetre"] == "lycées") & (ssf["budget"] == "budget principal")
           & ssf["sous_fonction"].str.startswith("223")]
dotations_prv_lycees = pos[(pos["niveau"] == "Régions et CTU") & (pos["perimetre"] == "lycées")
                           & pos["poste"].str.contains("établissements privés")]["montant_M€"].sum()
RETRAIT_223 = {BATIMENTS: s223.loc[s223["section"] == "investissement", "montant_M€"].sum(),
               FONCTIONNEMENT: s223.loc[s223["section"] == "fonctionnement", "montant_M€"].sum() - dotations_prv_lycees}
STRUCT = {"ct_ecoles": structure("Communes (y.c. Paris)", "écoles (1er degré)", "établissements privés|6558|6067"),
          "ct_colleges": structure("Départements", "collèges"),
          "ct_lycees": structure("Régions et CTU", "lycées", retrait=RETRAIT_223)}
ecoles_pub = env[(env["poste"] == "ct_ecoles") & (env["population"] == "écoles publiques")]
PART_FOURNITURES = float(ecoles_pub.loc[ecoles_pub["enveloppe"].str.contains("fournitures"), "reparti_M€"].sum()
                         / ecoles_pub["reparti_M€"].sum())
ETAT = {
    "etat_enseignants": "Enseignants affectés dans les établissements (salaires et pensions)",
    "etat_remplacement_formation": "Remplacement et formation des enseignants",
    "etat_vie_scolaire": "Vie scolaire (CPE, assistants d'éducation)",
    "etat_pilotage_admin": "Direction, administration et encadrement pédagogique",
    "etat_inclusion_sante_social": "AESH, santé et service social scolaires, orientation",
    "etat_activites_educatives": "Actions éducatives complémentaires",
    "etat_aides_familles": "Bourses et fonds sociaux",
    "etat_forfait_prive_internats": "Forfait d'externat versé par l'État au privé, internats",
    "etat_soutien_administration": "Administration centrale et académique, examens",
}
lignes = []
for (deg, sect), d in etab.groupby(["degre", "secteur"]):
    n = d["eleves"].sum()
    for col, lib in ETAT.items():
        lignes.append({"degre": deg, "secteur": sect, "financeur": "État", "poste": lib, "euros_par_eleve": d[col].sum() / n})
    for col in ("ct_ecoles", "ct_colleges", "ct_lycees"):
        montant = d[col].sum()
        if montant == 0:
            continue
        if sect == "prive_sc":
            lignes.append({"degre": deg, "secteur": sect, "financeur": "Collectivités",
                           "poste": "Forfait communal / départemental / régional versé au privé", "euros_par_eleve": montant / n})
            continue
        if col == "ct_ecoles":
            lignes.append({"degre": deg, "secteur": sect, "financeur": "Collectivités", "poste": FONCTIONNEMENT,
                           "euros_par_eleve": montant * PART_FOURNITURES / n})
            montant *= 1 - PART_FOURNITURES
        for classe, part in STRUCT[col].items():
            lignes.append({"degre": deg, "secteur": sect, "financeur": "Collectivités", "poste": classe,
                           "euros_par_eleve": montant * part / n})
    lignes.append({"degre": deg, "secteur": sect, "financeur": "Collectivités", "poste": "Transports scolaires",
                   "euros_par_eleve": d["ct_transports"].sum() / n})
    lignes.append({"degre": deg, "secteur": sect, "financeur": "Autres administrations publiques",
                   "poste": "Allocation de rentrée scolaire et autres (CAF…)", "euros_par_eleve": d["apu_par_eleve"].sum() / n})
dec = pd.DataFrame(lignes).groupby(["degre", "secteur", "financeur", "poste"], as_index=False)["euros_par_eleve"].sum()
# Version tous secteurs, pondérée par les élèves.
poids = etab.groupby(["degre", "secteur"])["eleves"].sum()
dec["montant"] = dec.apply(lambda r: r["euros_par_eleve"] * poids[(r["degre"], r["secteur"])], axis=1)
tous = dec.groupby(["degre", "financeur", "poste"], as_index=False)["montant"].sum()
tous["euros_par_eleve"] = tous.apply(lambda r: r["montant"] / poids[r["degre"]].sum(), axis=1)
tous["secteur"] = "public + privé"
dec = pd.concat([dec, tous], ignore_index=True)
# D1 est arrondi à l'euro (colonne non arrondie conservée pour les regroupements de la figure 1) ;
# les regroupements (D2) sont calculés sur les valeurs non arrondies.
dec[["degre", "secteur", "financeur", "poste"]].assign(
    euros_par_eleve=dec["euros_par_eleve"].round(), euros_par_eleve_non_arrondi=dec["euros_par_eleve"].round(2)).to_csv(
    RESULTATS / "D1_decomposition_par_poste.csv", sep=";", index=False, encoding="utf-8-sig")

# Regroupement dans les catégories de départ de l'étudiant (H-D3).
CATEGORIES = {
    "1. Enseignants (« profs »)": ["Enseignants affectés dans les établissements (salaires et pensions)",
                                   "Remplacement et formation des enseignants"],
    "2. Bâtiments et équipement (« réparations ») : construction, rénovation, grosses réparations, équipement, entretien, énergie": [
        "Bâtiments : construction, rénovation, grosses réparations, équipement",
        "Entretien, énergie et fluides des bâtiments"],
    "3. Activités et fonctionnement : cantine, transports, actions éducatives, fournitures, forfaits du privé": [
        "Restauration scolaire et activités (achats, prestations)", "Transports scolaires",
        "Actions éducatives complémentaires",
        "Dotations et autres frais de fonctionnement (fournitures, caisses des écoles…)",
        "Forfait communal / départemental / régional versé au privé",
        "Forfait d'externat versé par l'État au privé, internats"],
    "4. Autres : autres personnels (État, collectivités), aides aux familles, administration": [
        "Vie scolaire (CPE, assistants d'éducation)", "Direction, administration et encadrement pédagogique",
        "AESH, santé et service social scolaires, orientation",
        "Personnels des collectivités (ATSEM, agents d'entretien et de restauration)",
        "Bourses et fonds sociaux", "Allocation de rentrée scolaire et autres (CAF…)",
        "Administration centrale et académique, examens"],
}
tous_postes = set(sum(CATEGORIES.values(), []))
assert tous_postes == set(dec["poste"]), set(dec["poste"]) ^ tous_postes
d2 = []
for sect in ("public + privé", "public", "prive_sc"):
    for deg in ("1er degré", "2nd degré"):
        x = dec[(dec["secteur"] == sect) & (dec["degre"] == deg)]
        total = x["euros_par_eleve"].sum()
        for cat, postes in CATEGORIES.items():
            v = x.loc[x["poste"].isin(postes), "euros_par_eleve"].sum()
            d2.append({"secteur": sect, "degre": deg, "categorie": cat, "euros_par_eleve": round(v),
                       "part_%": round(100 * v / total, 2)})
ecrire_csv(RESULTATS / "D2_decomposition_4_categories.csv", d2)
journal.ecrire(RESULTATS / "tracabilite_C.csv")

if __name__ == "__main__":
    for r in c1:
        print("COFOG :", r)
    for r in c3:
        print("A/B   :", r)
    for r in c4:
        print("CAS   :", r)
    print(dec[dec["secteur"].eq("public + privé")].pivot_table(index="poste", columns="degre", values="euros_par_eleve")
          .round().to_string())
