"""Approche A — référence officielle : part PUBLIQUE de la dépense d'éducation par élève.

Source principale : DEPP, Note d'Information n° 26.42 (septembre 2026), compte de l'éducation,
année 2025 (provisoire). Comparaison : NI 25.52 (2024 provisoire) et RERS 2026 (fiches 10.04, 10.05).

Principe : dépense publique par élève = dépense moyenne par élève (tous financeurs, publiée par la DEPP)
× part des financeurs publics (État + collectivités territoriales + autres administrations publiques)
en financement initial. Hypothèses : voir hypotheses.md (section A).
"""
import pandas as pd

from commun import BRUT, RESULTATS, Classeur, Journal, ecrire_csv, euros

DEPP = BRUT / "depp_compte_education"
journal = Journal()

ni2642 = Classeur(DEPP / "depp_ni_2026-42_compte_education_2025_donnees.xlsx", journal)
ni2552 = Classeur(DEPP / "depp_ni_2025-52_compte_education_2024_donnees.xlsx", journal)
rers1005 = Classeur(DEPP / "depp_rers2026_10-05_depense_par_eleve_donnees.xlsx", journal)
rers1004 = Classeur(DEPP / "depp_rers2026_10-04_producteurs_education_donnees.xlsx", journal)

FINANCEURS = [  # (clé, libellé de ligne dans la Figure 4)
    ("etat", "État"),
    ("collectivites", "Collectivités territoriales"),
    ("autres_apu", "Autres administrations publiques"),
    ("entreprises", "Entreprises"),
    ("menages", "Ménages"),
]
PUBLICS = ("etat", "collectivites", "autres_apu")

# Emplacement des cellules dans chaque édition (vérifié à la main, puis contrôlé par libellé).
EDITIONS = {
    "2025p": dict(
        cl=ni2642, source="DEPP, NI 26.42 (sept. 2026)",
        die={"1d": "B32", "2d": "B33"},
        # Moyennes par degré lues dans la Figure 7 (année 2025p, euros 2025 = euros courants) :
        # la Figure 6 contient une coquille de libellé (« Supérieur » au lieu de « Second degré » en D33).
        dme=dict(onglet="Figure 7", cells={"1d": "C82", "2d": "D82"}, entete=36,
                 col={"1d": "1er degré", "2d": "2d degré"}, ligne="2025p"),
        sous_niveaux=dict(onglet="Figure 6", ligne0=31),
        fig4_lignes=range(32, 37), fig4_cols={"1d": "B", "2d": "C"}, fig4_entete=31,
    ),
    "2024p": dict(
        cl=ni2552, source="DEPP, NI 25.52 (sept. 2025)",
        die={"1d": "B31", "2d": "B32"},
        dme=dict(onglet="Figure 6", cells={"1d": "E32", "2d": "E34"}, entete=None,
                 col=None, ligne=None, libelle_d={"1d": "Premier degré", "2d": "Second degré"}),
        sous_niveaux=dict(onglet="Figure 6", ligne0=32),
        fig4_lignes=range(32, 37), fig4_cols={"1d": "B", "2d": "C"}, fig4_entete=31,
    ),
}
SOUS_NIVEAUX = [
    ("preelementaire", "1d", "Préélémentaire"),
    ("elementaire", "1d", "Élémentaire"),
    ("college", "2d", "Formations en collège"),
    ("lycee_gt", "2d", "Formations générales et technologiques en lycée"),
    ("lycee_pro", "2d", "Formations professionnelles en lycée"),
]
NOM = {"1d": "1er degré", "2d": "2nd degré (y c. apprentis du secondaire)"}


def lire_edition(annee: str) -> dict:
    e = EDITIONS[annee]
    cl = e["cl"]
    out = {}
    for niv in ("1d", "2d"):
        lib = "Premier degré" if niv == "1d" else "Second degré"
        die = cl.lire_cellule(f"{annee}.die.{niv}", "Figure 5", e["die"][niv], libelle_ligne=lib)
        d = e["dme"]
        if d["entete"]:
            dme = cl.lire_cellule(f"{annee}.dme.{niv}", d["onglet"], d["cells"][niv], libelle_ligne=d["ligne"],
                                  libelle_colonne=d["col"][niv], ligne_entete=d["entete"])
        else:
            dme = cl.lire_cellule(f"{annee}.dme.{niv}", d["onglet"], d["cells"][niv],
                                  libelle_ligne=d["libelle_d"][niv], col_libelle="D")
        parts = {}
        col = e["fig4_cols"][niv]
        for (cle, lib_f), ligne in zip(FINANCEURS, e["fig4_lignes"]):
            parts[cle] = cl.lire_cellule(f"{annee}.part.{niv}.{cle}", "Figure 4", f"{col}{ligne}",
                                         libelle_ligne=lib_f, libelle_colonne=lib, ligne_entete=e["fig4_entete"])
        out[niv] = dict(die_md=die, dme=dme, parts=parts)
    sn = e["sous_niveaux"]
    out["sous_niveaux"] = {}
    for i, (cle, niv, lib) in enumerate(SOUS_NIVEAUX):
        out["sous_niveaux"][cle] = (niv, cl.lire_cellule(f"{annee}.dme.{cle}", sn["onglet"], f"B{sn['ligne0'] + i}",
                                                         libelle_ligne=lib))
    return out


lignes_a1, lignes_a2 = [], []
resume = {}
for annee in ("2025p", "2024p"):
    d = lire_edition(annee)
    total_pub_md, total_die_md, total_eff = 0.0, 0.0, 0.0
    for niv in ("1d", "2d"):
        x = d[niv]
        p = x["parts"]
        somme = sum(p.values())
        assert abs(somme - 100) < 0.05, f"parts {annee} {niv} = {somme}"
        part_pub = sum(p[k] for k in PUBLICS)
        effectif = x["die_md"] * 1e9 / x["dme"]  # effectif implicite (année civile) = DIE / dépense moyenne
        ligne = {
            "annee": annee, "niveau": NOM[niv],
            "DIE_Md€": round(x["die_md"], 3),
            "depense_moyenne_tous_financeurs_€": round(x["dme"]),
            "effectif_implicite_annee_civile": round(effectif),
        }
        for k, _ in FINANCEURS:
            ligne[f"part_{k}_%"] = round(p[k], 2)
        ligne["part_publique_%"] = round(part_pub, 2)
        ligne["depense_publique_par_eleve_€"] = round(x["dme"] * part_pub / 100)
        for k in PUBLICS:
            ligne[f"dont_{k}_€"] = round(x["dme"] * p[k] / 100)
        ligne["depense_privee_par_eleve_€ (ménages+entreprises)"] = round(x["dme"] * (100 - part_pub) / 100)
        ligne["source"] = EDITIONS[annee]["source"]
        lignes_a1.append(ligne)
        total_pub_md += x["die_md"] * part_pub / 100
        total_die_md += x["die_md"]
        total_eff += effectif
    # « Élève moyen » des 1er et 2nd degrés : moyenne pondérée par les effectifs implicites.
    ligne = {
        "annee": annee, "niveau": "Ensemble 1er + 2nd degrés",
        "DIE_Md€": round(total_die_md, 3),
        "depense_moyenne_tous_financeurs_€": round(total_die_md * 1e9 / total_eff),
        "effectif_implicite_annee_civile": round(total_eff),
        "part_publique_%": round(100 * total_pub_md / total_die_md, 2),
        "depense_publique_par_eleve_€": round(total_pub_md * 1e9 / total_eff),
        "source": EDITIONS[annee]["source"] + " ; moyenne pondérée calculée",
    }
    for k in PUBLICS:
        ligne[f"dont_{k}_€"] = round(sum(d[n]["die_md"] * d[n]["parts"][k] / 100 for n in ("1d", "2d")) * 1e9 / total_eff)
    lignes_a1.append(ligne)
    resume[annee] = ligne


# Contrôle : la DEPP publie la moyenne 1er + 2nd degrés pour 2024p (RERS 2026, 10.05, tableau 2, J13).
publie_2024 = rers1005.lire_cellule("2024p.dme.1d2d.publie", "10.05 Tableau 2", "J13",
                                    libelle_ligne="Sous-total premier et second degrés",
                                    libelle_colonne="2024p", ligne_entete=5)
calcule_2024 = resume["2024p"]["depense_moyenne_tous_financeurs_€"]
assert abs(calcule_2024 - publie_2024) <= 10, (calcule_2024, publie_2024)

# Structure de la dépense par élève selon l'activité (2024p, tous financeurs).
lignes_a3 = []
for ligne_xl, niv in ((8, "Premier degré"), (9, "Second degré")):
    ligne = {"annee": "2024p", "niveau": niv}
    for col, act in (("B", "Enseignement"), ("C", "Activités annexes"), ("D", "Administration générale"),
                     ("E", "Achats de biens et services liés")):
        ligne[f"{act}_%"] = rers1005.lire_cellule(f"2024p.activite.{niv}.{act}", "10.05 Graphique 4",
                                                  f"{col}{ligne_xl}", libelle_ligne=niv,
                                                  libelle_colonne=act, ligne_entete=6)
    ligne["source"] = "DEPP, RERS 2026, fiche 10.05, graphique 4"
    lignes_a3.append(ligne)

# Structure par nature des dépenses des producteurs d'éducation (2024p, tous niveaux confondus).
lignes_a4 = []
for ref, lib in (("B9", "Rémunérations"), ("B10", "des personnels enseignants"),
                 ("B11", "des personnels non enseignants"), ("B7", "Autres dépenses de fonctionnement"),
                 ("B8", "Investissement")):
    lignes_a4.append({"annee": "2024p", "nature": lib,
                      "part_%": rers1004.lire_cellule(f"2024p.nature.{lib}", "10.04 Graphique 4", ref,
                                                      libelle_ligne=lib),
                      "champ": "tous niveaux, tous producteurs (non publié par niveau)",
                      "source": "DEPP, RERS 2026, fiche 10.04, graphique 4 (fichier Excel)"})

# Série longue de la dépense moyenne (tous financeurs), euros constants 2025.
lignes_a5 = []
ws = ni2642.wb["Figure 7"]
for r in range(37, 83):
    an = str(ws[f"A{r}"].value).strip()
    lignes_a5.append({"annee": an,
                      "1er_degre_€2025": ni2642.lire_cellule(f"serie.{an}.1d", "Figure 7", f"C{r}", libelle_ligne=an,
                                                             libelle_colonne="1er degré", ligne_entete=36),
                      "2nd_degre_€2025": ni2642.lire_cellule(f"serie.{an}.2d", "Figure 7", f"D{r}", libelle_ligne=an,
                                                             libelle_colonne="2d degré", ligne_entete=36)})

# ------------------------------------------------------------------ Variantes de périmètre (2025p sauf mention)
series_fin = Classeur(DEPP / "depp_series_chrono_die_financeur_initial_final_par_niveau_366603.xlsx", journal)
series_str = Classeur(DEPP / "depp_series_chrono_structure_die_par_niveau_366606.xlsx", journal)
series_die = Classeur(DEPP / "depp_series_chrono_die_par_niveau_part_pib_508145.xlsx", journal)
d25, d24 = lire_edition("2025p"), lire_edition("2024p")
N = {a: {n: d[n]["die_md"] * 1e9 / d[n]["dme"] for n in ("1d", "2d")} for a, d in (("2025p", d25), ("2024p", d24))}


def pub(d, niv, financeurs=PUBLICS):
    return d[niv]["die_md"] * 1e9 * sum(d[niv]["parts"][k] for k in financeurs) / 100


variantes = []


def variante(nom, p1, p2, n1, n2, note):
    variantes.append({"variante": nom, "1er_degre_€": round(p1 / n1), "2nd_degre_€": round(p2 / n2),
                      "ensemble_€": round((p1 + p2) / (n1 + n2)), "note": note})


variante("Référence : financement initial, apprentis compris (convention DEPP)", pub(d25, "1d"), pub(d25, "2d"),
         N["2025p"]["1d"], N["2025p"]["2d"], "NI 26.42, figures 4, 5 et 7")
variante("Sans les « autres administrations publiques » (allocation de rentrée scolaire des CAF…)",
         pub(d25, "1d", ("etat", "collectivites")), pub(d25, "2d", ("etat", "collectivites")),
         N["2025p"]["1d"], N["2025p"]["2d"], "H-A4")
# Hors apprentis du 2nd degré (élèves sous statut scolaire) — H-A3.
part_app = series_str.lire_cellule("2024p.part_apprentissage_2d_dans_DIE", "Structure DIE par niveau fin", "U19",
                                   libelle_ligne="Apprentissage du second degré", col_libelle="B",
                                   libelle_colonne="2024p", ligne_entete=9)
die_tot_24 = series_die.lire_cellule("2024p.die_totale", "Part DIE dans PIB par niveau ", "AU10",
                                     libelle_ligne="DIE en Md€", col_libelle="B", libelle_colonne="2024p",
                                     ligne_entete=9)
die_app_24 = part_app / 100 * die_tot_24 * 1e9
die_app_25 = die_app_24 * d25["2d"]["die_md"] / d24["2d"]["die_md"]  # même évolution que la DIE du 2nd degré
# Apprentis de niveaux 3 et 4 (secondaire) au 31/12, enquête SIFA : DEPP, NI 26.35 (juillet 2026), figure 2.
ni2635 = Classeur(BRUT / "effectifs_nationaux" / "depp_ni_2026-35_apprentissage_31-12-2025_donnees.xlsx", journal)
APPRENTIS_31_12 = {an: ni2635.lire_cellule(f"apprentis_secondaire_31-12-{an}", "Figure 2", cell, libelle_ligne="Secondaire",
                                           libelle_colonne=str(an), ligne_entete=4)
                   for an, cell in ((2024, "C12"), (2025, "D12"))}
apprentis_25 = 2 / 3 * APPRENTIS_31_12[2024] + 1 / 3 * APPRENTIS_31_12[2025]
for s, lib in ((0.175, "centrale"), (0.135, "basse"), (0.23, "haute")):
    p2 = pub(d25, "2d") - s * die_app_25
    variante(f"Hors apprentis (élèves sous statut scolaire), part publique de l'apprentissage {s:.1%} ({lib})",
             pub(d25, "1d"), p2, N["2025p"]["1d"], N["2025p"]["2d"] - apprentis_25,
             "H-A3 ; DIE d'apprentissage du 2nd degré 2024p (séries DEPP) portée en 2025")
# Financement final (après transferts aux ménages : bourses, allocation de rentrée scolaire), 2024p — H-A2.
fin = {}
for niv, onglet in (("1d", "DIE 1er degré"), ("2d", "DIE 2nd degré")):
    fin[niv] = sum(series_fin.lire_cellule(f"2024p.final.{niv}.{k}", onglet, f"U{r}", libelle_ligne=lib,
                                           col_libelle="B")
                   for k, r, lib in (("etat", 28, "État (%)"), ("ct", 30, "Collectivités territoriales (%)"),
                                     ("apu", 31, "Autres administrations publiques (%)")))
variante("Financement final, 2024 provisoire (séries chronologiques DEPP)",
         d24["1d"]["die_md"] * 1e9 * fin["1d"] / 100, d24["2d"]["die_md"] * 1e9 * fin["2d"] / 100,
         N["2024p"]["1d"], N["2024p"]["2d"], "parts publiques arrondies à 0,1 point dans la source")
variante("Financement initial, 2024 provisoire (pour comparaison)", pub(d24, "1d"), pub(d24, "2d"),
         N["2024p"]["1d"], N["2024p"]["2d"], "NI 25.52")
# Convention de l'apprentissage (H-A8) : la DEPP classe le financement de l'apprentissage via les OPCO dans les
# « entreprises », alors que l'Insee classe ces organismes parmi les administrations publiques. Borne haute :
# toute la part « entreprises » du 2nd degré comptée comme publique (1er degré inchangé).
variante("Si l'on comptait comme publics les financements « entreprises » du 2nd degré (OPCO) — borne haute",
         pub(d25, "1d"), pub(d25, "2d", PUBLICS + ("entreprises",)),
         N["2025p"]["1d"], N["2025p"]["2d"], "H-A8 ; la part « entreprises » du 2nd degré ne contient pas que l'apprentissage")
ecrire_csv(RESULTATS / "A6_variantes_de_perimetre.csv", variantes)

# ------------------------------------------------------------------ Sous-niveaux (H-A5)
# La part publique n'est publiée que par degré. Pour les sous-niveaux du 2nd degré (formations sous statut
# scolaire), on applique la part publique du 2nd degré HORS apprentissage (paramètres de H-A3, s = 17,5 %).
S_CENTRAL = 0.175
DIE_APP = {"2025p": die_app_25, "2024p": die_app_24}
for annee, d in (("2025p", d25), ("2024p", d24)):
    parts = {"1d": sum(d["1d"]["parts"][k] for k in PUBLICS),
             "2d": 100 * (pub(d, "2d") - S_CENTRAL * DIE_APP[annee]) / (d["2d"]["die_md"] * 1e9 - DIE_APP[annee])}
    for cle, niv, lib in SOUS_NIVEAUX:
        _, dme = d["sous_niveaux"][cle]
        lignes_a2.append({
            "annee": annee, "sous_niveau": lib, "degre": "1er degré" if niv == "1d" else "2nd degré (hors apprentis)",
            "depense_moyenne_tous_financeurs_€": round(dme),
            "part_publique_appliquee_%": round(parts[niv], 2),
            "depense_publique_par_eleve_approx_€": round(dme * parts[niv] / 100),
            "avertissement": "part publique connue seulement par degré ; 2nd degré : hors apprentissage (H-A5)",
        })

# ------------------------------------------------------------------ Décomposition par nature (structure UOE 2023)
uoe = pd.read_csv(DEPP / "eurostat_educ_uoe_fini01_FR_MIO_EUR_2019-.csv")
uoe = uoe[(uoe["sector"] == "TOT_SEC") & (uoe["TIME_PERIOD"] == 2023)]
NATURES = {"CUR_COMPT": "Rémunération des enseignants", "CUR_COMPO": "Rémunération des autres personnels",
           "CUR_OTH": "Autres dépenses courantes (fonctionnement)", "CAP": "Investissement (bâtiments, équipement)"}
lignes_a7 = []
for niv, cites, dme_pub in (("1er degré", ["ED02", "ED1"], lignes_a1[0]["depense_publique_par_eleve_€"]),
                            ("2nd degré", ["ED2", "ED3"], lignes_a1[1]["depense_publique_par_eleve_€"])):
    sous = uoe[uoe["isced11"].isin(cites)]
    total = sous.loc[sous["expend"] == "TOTAL", "OBS_VALUE"].sum()
    for code, lib in NATURES.items():
        part = sous.loc[sous["expend"] == code, "OBS_VALUE"].sum() / total
        lignes_a7.append({"niveau": niv, "nature": lib, "part_UOE_2023_%": round(100 * part, 1),
                          "euros_par_eleve_2025p_approx": round(part * dme_pub)})
    aserv = sous.loc[sous["expend"] == "ASERV", "OBS_VALUE"].sum() / total
    lignes_a7.append({"niveau": niv, "nature": "dont services annexes (cantine, internat, transport) — transversal",
                      "part_UOE_2023_%": round(100 * aserv, 1), "euros_par_eleve_2025p_approx": round(aserv * dme_pub)})
ecrire_csv(RESULTATS / "A7_decomposition_par_nature_UOE.csv", lignes_a7)

ecrire_csv(RESULTATS / "A1_depense_publique_par_eleve.csv", lignes_a1)
ecrire_csv(RESULTATS / "A2_sous_niveaux.csv", lignes_a2)
ecrire_csv(RESULTATS / "A3_structure_par_activite.csv", lignes_a3)
ecrire_csv(RESULTATS / "A4_structure_par_nature.csv", lignes_a4)
ecrire_csv(RESULTATS / "A5_serie_longue_euros_constants.csv", lignes_a5)
journal.ecrire(RESULTATS / "tracabilite_A.csv")

if __name__ == "__main__":
    print("Approche A — dépense publique par élève (financement initial, État + collectivités + autres APU)")
    for l in lignes_a1:
        print(f"  {l['annee']:6} {l['niveau']:42} total {euros(l['depense_moyenne_tous_financeurs_€']):>9}"
              f"  public {euros(l['depense_publique_par_eleve_€']):>9} ({l['part_publique_%']:.1f} %)")
    print(f"  Contrôle 2024p 1er+2nd : calculé {calcule_2024} € / publié {publie_2024:.0f} €")
    print(f"  {len(journal.lignes)} valeurs tracées -> resultats/tracabilite_A.csv")
