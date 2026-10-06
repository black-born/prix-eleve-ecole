# -*- coding: utf-8 -*-
"""
G1 - Decomposition officielle (Eurostat UOE, donnees transmises par la DEPP) de la depense
d'education par NATURE et par NIVEAU, et de la depense PUBLIQUE par NIVEAU D'ADMINISTRATION.

Entrees (fichiers bruts, non modifies) dans data/raw/depp_compte_education/ :
  eurostat_educ_uoe_fini01_FR_MIO_EUR_2019-.csv  (depenses des etablissements, par nature)
  eurostat_educ_uoe_fine02_FR_MIO_EUR_2019-.csv  (depenses publiques par niveau d'administration)
  eurostat_educ_uoe_fine10_FR_NR_2019-.csv       (effectifs ETP alignes sur l'annee financiere)
  eurostat_educ_uoe_fine09_FR_EUR_2019-.csv      (depense publique par eleve ETP, publiee)
Sorties : CSV prefixes _derive_G1_ dans le dossier passe en argument (par defaut le dossier brut, convention _derive_).

Conventions (voir NOTES.md, section G1) :
  - TOTAL = CUR + CAP ; CUR = CUR_COMPT + CUR_COMPO + CUR_OTH (verifie a l'arrondi pres).
  - ASERV (services annexes : cantine, internat, transport...) est un "dont" transversal,
    NON additif avec les natures (il est deja inclus dans CUR/CAP).
  - ADJ (ajustements de fonds) est hors TOTAL ; non utilise.
  - Vision "finale" par niveau d'administration = DIR (depense directe pour les etablissements)
    + TRF_PAY vers le secteur prive (bourses, aides aux menages) ; somme exacte = S13.
    S1|TOTAL d'un niveau inclut en plus les transferts verses aux autres administrations
    (non consolide) : il n'est PAS additif entre niveaux.
"""
import os
import sys
import pandas as pd

RAW = r"C:/Users/chret/Documents/EtatEcole/data/raw/depp_compte_education"
OUT = sys.argv[1] if len(sys.argv) > 1 else RAW
os.makedirs(OUT, exist_ok=True)

fini = pd.read_csv(os.path.join(RAW, "eurostat_educ_uoe_fini01_FR_MIO_EUR_2019-.csv"))
fine02 = pd.read_csv(os.path.join(RAW, "eurostat_educ_uoe_fine02_FR_MIO_EUR_2019-.csv"))
fine10 = pd.read_csv(os.path.join(RAW, "eurostat_educ_uoe_fine10_FR_NR_2019-.csv"))
fine09 = pd.read_csv(os.path.join(RAW, "eurostat_educ_uoe_fine09_FR_EUR_2019-.csv"))

V_fini = fini.set_index(["sector", "expend", "isced11", "TIME_PERIOD"])["OBS_VALUE"]
V_f02 = fine02.set_index(["sector", "sector2", "expend", "isced11", "TIME_PERIOD"])["OBS_VALUE"]
V_f10 = fine10.set_index(["worktime", "sector", "isced11", "TIME_PERIOD"])["OBS_VALUE"]
V_f09 = fine09.set_index(["isced11", "TIME_PERIOD"])["OBS_VALUE"]

YEARS = sorted(fini.TIME_PERIOD.unique())
# Niveaux elementaires CITE et agregats construits par somme
LEVELS = {
    "ED02 preelementaire": ["ED02"],
    "ED1 elementaire (primaire)": ["ED1"],
    "1D = ED02+ED1 (premier degre)": ["ED02", "ED1"],
    "ED2 college (= ED24)": ["ED2"],
    "ED34 lycee general et techno": ["ED34"],
    "ED35 lycee pro + apprentis CITE 35": ["ED35"],
    "ED3 second cycle (ED34+ED35)": ["ED3"],
    "ED4 post-secondaire non superieur": ["ED4"],
    "2D = ED2+ED3 (second degre hors CITE 4)": ["ED2", "ED3"],
    "SCOL = ED02+ED1+ED2+ED3 (scolaire hors CITE 4)": ["ED02", "ED1", "ED2", "ED3"],
    "SCOL4 = ED02+ED1+ED2+ED3+ED4": ["ED02", "ED1", "ED2", "ED3", "ED4"],
}
NATURES = ["CUR_COMPT", "CUR_COMPO", "CUR_OTH", "CAP"]
LAB = {"CUR_COMPT": "remun_enseignants", "CUR_COMPO": "remun_autres_personnels",
       "CUR_OTH": "autres_dep_courantes", "CAP": "capital", "ASERV": "dont_services_annexes",
       "TOTAL": "total", "CUR": "courant"}
SECTORS = {"PUB": ["PUB"], "PRV_DEP": ["PRV_DEP"], "PUB+PRV_DEP": ["PUB", "PRV_DEP"],
           "PRV_IND": ["PRV_IND"], "TOT_SEC": ["TOT_SEC"]}


def g(series, key):
    v = series.get(key)
    return float("nan") if v is None or pd.isna(v) else float(v)


def rnd(x):
    return float("nan") if pd.isna(x) else round(x)


def ssum(vals):
    if any(pd.isna(x) for x in vals):
        return float("nan")
    return float(sum(vals))


# ---------------------------------------------------------------- 1. Structure par nature
rows = []
for yr in YEARS:
    for lname, comps in LEVELS.items():
        for sname, secs in SECTORS.items():
            r = {"annee": yr, "niveau": lname, "secteur_etab": sname}
            for e in ["TOTAL", "CUR"] + NATURES + ["ASERV"]:
                r[LAB[e] + "_MEUR"] = ssum([g(V_fini, (s, e, c, yr)) for s in secs for c in comps])
            fte = ssum([g(V_f10, ("TOT_FTE", s, c, yr)) for s in secs for c in comps])
            r["eleves_ETP"] = fte
            tot = r["total_MEUR"]
            somme = ssum([r[LAB[e] + "_MEUR"] for e in NATURES])
            r["controle_somme_natures_moins_total_MEUR"] = round(somme - tot, 1)
            for e in NATURES + ["ASERV"]:
                r[LAB[e] + "_pct"] = round(100 * r[LAB[e] + "_MEUR"] / tot, 2) if tot else float("nan")
            r["remun_personnels_pct"] = round(r["remun_enseignants_pct"] + r["remun_autres_personnels_pct"], 2)
            for e in ["TOTAL"] + NATURES + ["ASERV"]:
                r[LAB[e] + "_EUR_par_eleve_ETP"] = round(1e6 * r[LAB[e] + "_MEUR"] / fte) if fte else float("nan")
            rows.append(r)
struct = pd.DataFrame(rows)
struct.to_csv(os.path.join(OUT, "_derive_G1_uoe_structure_nature_par_niveau_2019-2023.csv"), sep=";", index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------- 2. Public par niveau d'administration
GOV = {"S1311": "Etat_central (S1311)", "S1312": "niveau_regional (S1312 : departements+regions, deduit)",
       "S1313": "niveau_local (S1313 : communes, deduit)", "S13": "ensemble_APU (S13)"}
rows = []
for yr in YEARS:
    for lname, comps in LEVELS.items():
        fte = ssum([g(V_f10, ("TOT_FTE", "TOT_SEC", c, yr)) for c in comps])
        s13_tot = ssum([g(V_f02, ("S13", "S1", "TOTAL", c, yr)) for c in comps])
        for code, glabel in GOV.items():
            dirr = ssum([g(V_f02, (code, "TOT_SEC", "DIR", c, yr)) for c in comps])
            dir_pub = ssum([g(V_f02, (code, "PUB", "DIR", c, yr)) for c in comps])
            dir_prvdep = ssum([g(V_f02, (code, "PRV_DEP", "DIR", c, yr)) for c in comps])
            dir_prvind = ssum([g(V_f02, (code, "PRV_IND", "DIR", c, yr)) for c in comps])
            trf = ssum([g(V_f02, (code, "S1D", "TRF_PAY", c, yr)) for c in comps])
            grants = ssum([g(V_f02, (code, "S14", "FA_GRNT", c, yr)) for c in comps])
            cap = ssum([g(V_f02, (code, "TOT_SEC", "CAP", c, yr)) for c in comps])
            tot_brut = ssum([g(V_f02, (code, "S1", "TOTAL", c, yr)) for c in comps])
            final = dirr + trf
            rows.append({
                "annee": yr, "niveau": lname, "administration": glabel,
                "dep_directe_etab_DIR_MEUR": dirr, "dont_vers_etab_publics_MEUR": dir_pub,
                "dont_vers_prive_sous_contrat_PRV_DEP_MEUR": dir_prvdep,
                "dont_vers_prive_independant_MEUR": dir_prvind,
                "dont_capital_CAP_MEUR": cap,
                "transferts_au_prive_TRF_PAY_MEUR": trf, "dont_bourses_aides_menages_FA_GRNT_MEUR": grants,
                "depense_finale_DIR+TRF_MEUR": final,
                "S1_TOTAL_publie_MEUR": tot_brut,
                "transferts_verses_autres_APU_MEUR(S1_TOTAL-DIR-TRF)": round(tot_brut - final, 1),
                "part_de_S13_final_pct": round(100 * final / s13_tot, 2) if s13_tot else float("nan"),
                "eleves_ETP_tous_secteurs": fte,
                "EUR_par_eleve_ETP_final": round(1e6 * final / fte) if fte else float("nan"),
            })
gov = pd.DataFrame(rows)
gov.to_csv(os.path.join(OUT, "_derive_G1_uoe_depense_publique_par_niveau_administration_2019-2023.csv"), sep=";", index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------- 3. Par eleve : publie vs recalcule ; part publique
rows = []
for yr in YEARS:
    for lname, comps in LEVELS.items():
        fte_tot = ssum([g(V_f10, ("TOT_FTE", "TOT_SEC", c, yr)) for c in comps])
        s13 = ssum([g(V_f02, ("S13", "S1", "TOTAL", c, yr)) for c in comps])
        s13_dir = ssum([g(V_f02, ("S13", "TOT_SEC", "DIR", c, yr)) for c in comps])
        inst = ssum([g(V_fini, ("TOT_SEC", "TOTAL", c, yr)) for c in comps])
        pub09 = g(V_f09, (comps[0], yr)) if len(comps) == 1 else float("nan")
        rows.append({
            "annee": yr, "niveau": lname, "eleves_ETP_tous_secteurs": fte_tot,
            "dep_publique_totale_S13_MEUR": s13, "dont_directe_etab_MEUR": s13_dir,
            "dep_etablissements_toutes_sources_MEUR": inst,
            "part_publique_directe_dans_dep_etab_pct": round(100 * s13_dir / inst, 2) if inst else float("nan"),
            "dep_publique_par_eleve_ETP_recalc_EUR": round(1e6 * s13 / fte_tot) if fte_tot else float("nan"),
            "dep_publique_par_eleve_ETP_publiee_fine09_EUR": pub09,
            "dep_etab_par_eleve_ETP_recalc_EUR": round(1e6 * inst / fte_tot) if fte_tot else float("nan"),
        })
pe = pd.DataFrame(rows)
pe.to_csv(os.path.join(OUT, "_derive_G1_uoe_depense_par_eleve_ETP_2019-2023.csv"), sep=";", index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------- 4. Ventilation ESTIMEE de la depense publique par nature
# Calcul derive (non publie). Deux variantes :
#  V1 proportionnelle : depense publique S13 par eleve ETP x parts par nature des etablissements (TOT_SEC).
#  V2 attribution : remunerations (enseignants, autres personnels) des etablissements PUB + PRV_DEP supposees
#     financees a 100 % sur fonds publics ; capital = capital public (fine02 S13 TOT_SEC CAP) ;
#     autres depenses courantes publiques = DIR publique - remunerations - capital public (residu) ;
#     transferts publics au prive (bourses, ARS...) = TRF_PAY.
rows = []
for yr in YEARS:
    for lname, comps in LEVELS.items():
        fte = ssum([g(V_f10, ("TOT_FTE", "TOT_SEC", c, yr)) for c in comps])
        s13_tot = ssum([g(V_f02, ("S13", "S1", "TOTAL", c, yr)) for c in comps])
        s13_dir = ssum([g(V_f02, ("S13", "TOT_SEC", "DIR", c, yr)) for c in comps])
        s13_cap = ssum([g(V_f02, ("S13", "TOT_SEC", "CAP", c, yr)) for c in comps])
        s13_trf = ssum([g(V_f02, ("S13", "S1D", "TRF_PAY", c, yr)) for c in comps])
        inst = {e: ssum([g(V_fini, ("TOT_SEC", e, c, yr)) for c in comps]) for e in ["TOTAL"] + NATURES}
        pp = {e: ssum([g(V_fini, (s, e, c, yr)) for s in ["PUB", "PRV_DEP"] for c in comps]) for e in NATURES}
        r = {"annee": yr, "niveau": lname, "eleves_ETP": fte, "dep_publique_S13_MEUR": s13_tot,
             "dep_publique_par_eleve_ETP_EUR": round(1e6 * s13_tot / fte) if fte else float("nan")}
        for e in NATURES:
            r["V1_" + LAB[e] + "_EUR_par_eleve"] = round(1e6 * s13_tot * inst[e] / inst["TOTAL"] / fte) if fte else float("nan")
        v2 = {"remun_enseignants": pp["CUR_COMPT"], "remun_autres_personnels": pp["CUR_COMPO"],
              "capital_public": s13_cap,
              "autres_dep_courantes_publiques_residu": s13_dir - pp["CUR_COMPT"] - pp["CUR_COMPO"] - s13_cap,
              "transferts_au_prive_bourses_ARS": s13_trf}
        for k, val in v2.items():
            r["V2_" + k + "_MEUR"] = round(val, 1)
            r["V2_" + k + "_EUR_par_eleve"] = round(1e6 * val / fte) if fte else float("nan")
            r["V2_" + k + "_pct"] = round(100 * val / s13_tot, 2) if s13_tot else float("nan")
        r["V2_controle_somme_moins_total_MEUR"] = round(sum(v2.values()) - s13_tot, 1)
        rows.append(r)
pubnat = pd.DataFrame(rows)
pubnat.to_csv(os.path.join(OUT, "_derive_G1_estimation_depense_publique_par_nature_2019-2023.csv"), sep=";", index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------- 5. Remuneration par ETP d'enseignant (derive)
# Effectifs d'enseignants (educ_uoe_perp02, "classroom teachers", ETP) : l'etiquette Eurostat t = annee scolaire (t-1)/t.
# Annee financiere N ~ 2/3 x etiquette N + 1/3 x etiquette N+1 (meme convention que la DEPP pour les eleves).
perp_path = os.path.join(RAW, "eurostat_educ_uoe_perp02_FR_enseignants_2019-.csv")
if os.path.exists(perp_path):
    perp = pd.read_csv(perp_path)
    V_p = perp[(perp.sex == "T")].set_index(["worktime", "sector", "isced11", "TIME_PERIOD"])["OBS_VALUE"]
    rows = []
    for yr in [y for y in YEARS if (y + 1) in set(perp.TIME_PERIOD)]:
        for lname, comps in LEVELS.items():
            for sname, secs in {"PUB": ["PUB"], "PRV_DEP": ["PRV_DEP"], "PUB+PRV_DEP": ["PUB", "PRV_DEP"]}.items():
                comp_t = ssum([g(V_fini, (s, "CUR_COMPT", c, yr)) for s in secs for c in comps])
                e_n = ssum([g(V_p, ("TOT_FTE", s, c, yr)) for s in secs for c in comps])
                e_n1 = ssum([g(V_p, ("TOT_FTE", s, c, yr + 1)) for s in secs for c in comps])
                etp = 2 / 3 * e_n + 1 / 3 * e_n1
                rows.append({"annee_financiere": yr, "niveau": lname, "secteur_etab": sname,
                             "remun_enseignants_MEUR": comp_t,
                             "ETP_enseignants_annee_scolaire_N-1_N (etiquette N)": e_n,
                             "ETP_enseignants_annee_scolaire_N_N+1 (etiquette N+1)": e_n1,
                             "ETP_enseignants_annee_civile_2/3-1/3": rnd(etp),
                             "remun_par_ETP_enseignant_EUR": rnd(1e6 * comp_t / etp) if etp else float("nan")})
    cpt = pd.DataFrame(rows)
    cpt.to_csv(os.path.join(OUT, "_derive_G1_remuneration_par_ETP_enseignant.csv"), sep=";", index=False, encoding="utf-8-sig")
    print(cpt[(cpt.annee_financiere == 2023)][["niveau", "secteur_etab", "remun_enseignants_MEUR", "ETP_enseignants_annee_civile_2/3-1/3", "remun_par_ETP_enseignant_EUR"]].to_string(index=False))

# ---------------------------------------------------------------- Affichage de controle
print(pubnat[pubnat.annee == 2023].T.to_string())
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 200)
print("Controle ED1 PUB 2023 TOTAL =", g(V_fini, ("PUB", "TOTAL", "ED1", 2023)))
c = struct[(struct.annee == 2023)]
print(c[["niveau", "secteur_etab", "total_MEUR", "remun_enseignants_pct", "remun_autres_personnels_pct",
         "autres_dep_courantes_pct", "capital_pct", "dont_services_annexes_pct", "eleves_ETP", "total_EUR_par_eleve_ETP",
         "controle_somme_natures_moins_total_MEUR"]].to_string(index=False))
c = gov[(gov.annee == 2023)]
print(c[["niveau", "administration", "depense_finale_DIR+TRF_MEUR", "part_de_S13_final_pct", "EUR_par_eleve_ETP_final",
         "transferts_verses_autres_APU_MEUR(S1_TOTAL-DIR-TRF)"]].to_string(index=False))
c = pe[(pe.annee == 2023)]
print(c.to_string(index=False))
