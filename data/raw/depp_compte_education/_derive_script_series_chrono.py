# -*- coding: utf-8 -*-
"""
Extraction et calculs dérivés : séries chronologiques DEPP « Les coûts et les financements »
(actualisation septembre 2025 ; données 2006-2024p, euros constants 2024).

Fichiers bruts lus (non modifiés), dans le dossier de ce script :
  - depp_series_chrono_die_financeur_initial_final_par_niveau_366603.xlsx
  - depp_series_chrono_structure_die_par_niveau_366606.xlsx
  - depp_series_chrono_depense_par_eleve_par_niveau_481445.xlsx
  - depp_series_chrono_die_par_niveau_part_pib_508145.xlsx
  - depp_series_chrono_apprentis_cfa_par_niveau_310608.xlsx (SIFA, au 31/12)
  - depp_rers2026_10-04_producteurs_education_donnees.xlsx (financement des CFA en 2024)

Sorties (dérivées, préfixe _derive_) :
  - _derive_series_chrono_extraction_2021_2024.csv : valeurs publiées, avec onglet et cellule
  - _derive_series_chrono_calculs_2021_2025p.csv    : calculs dérivés (non publiés par la DEPP)

Exécution : python _derive_script_series_chrono.py
"""
import csv
import os

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
F_FIN = "depp_series_chrono_die_financeur_initial_final_par_niveau_366603.xlsx"
F_STR = "depp_series_chrono_structure_die_par_niveau_366606.xlsx"
F_DEP = "depp_series_chrono_depense_par_eleve_par_niveau_481445.xlsx"
F_PIB = "depp_series_chrono_die_par_niveau_part_pib_508145.xlsx"
F_APP = "depp_series_chrono_apprentis_cfa_par_niveau_310608.xlsx"
F_RERS = "depp_rers2026_10-04_producteurs_education_donnees.xlsx"

YEARS = ["2021", "2022", "2023", "2024p"]
rows_out = []


def load(f):
    return openpyxl.load_workbook(os.path.join(HERE, f), data_only=True)


def year_cols(ws, header_row):
    """Retourne {'2021': 'R', ...} à partir de la ligne d'en-tête (années en int ou str)."""
    out = {}
    for c in ws[header_row]:
        v = c.value
        if v is None:
            continue
        k = str(v).strip().replace(" (1)", "")
        if k in ("2024", "2024p") and "p" in str(v):
            k = "2024p"
        if k in YEARS or k in ("2019", "2020", "2024"):
            out[k] = c.column_letter
    return out


def grab(wb, fname, sheet, header_row, row, expected_label, indicateur, niveau, unite, label_col="B", years=YEARS):
    ws = wb[sheet]
    lab = ws[f"{label_col}{row}"].value
    assert lab is not None and expected_label.lower() in str(lab).lower(), (sheet, row, lab, expected_label)
    cols = year_cols(ws, header_row)
    res = {}
    for y in years:
        col = cols[y]
        v = ws[f"{col}{row}"].value
        res[y] = v
        rows_out.append({
            "indicateur": indicateur, "niveau": niveau, "annee": y, "valeur": v, "unite": unite,
            "fichier": fname, "onglet": sheet, "cellule": f"{col}{row}", "libelle_ligne": str(lab).strip(),
            "statut": "provisoire" if y == "2024p" else "définitif (euros courants non révisés par la NI 26.42)",
        })
    return res


# ---------------------------------------------------------------- 1. Financement par niveau
wb = load(F_FIN)
fin = {}
for sheet, niv, die_label in [("DIE 1er degré", "1er degré", "DIE pour le premier degré"),
                              ("DIE 2nd degré", "2nd degré (apprentissage compris)", "DIE pour le second degré")]:
    d = {"DIE": grab(wb, F_FIN, sheet, 9, 10, die_label, "DIE du niveau", niv, "Md€ constants 2024")}
    for typ, hdr, r0 in [("initial", 15, 16), ("final", 27, 28)]:
        for off, lab, key in [(0, "État", "Etat"), (1, "dont MENESR", "MEN"), (2, "Collectivités territoriales", "CT"),
                              (3, "Autres administrations publiques", "APU"), (4, "Entreprises", "Ent"), (5, "Ménages", "Men")]:
            d[(typ, key)] = grab(wb, F_FIN, sheet, hdr, r0 + off, lab, f"Part financeur {typ} : {lab}", niv, "% de la DIE du niveau")
    fin[niv] = d

# DIE totale (mise en page différente : final en lignes 29-34)
dt = {"DIE": grab(wb, F_FIN, "DIE totale", 9, 10, "DIE en Md", "DIE totale", "Tous niveaux", "Md€ constants 2024")}
for typ, hdr, r0 in [("initial", 15, 16), ("final", 28, 29)]:
    for off, lab, key in [(0, "État", "Etat"), (1, "dont MENESR", "MEN"), (2, "Collectivités territoriales", "CT"),
                          (3, "Autres administrations publiques", "APU"), (4, "Entreprises", "Ent"), (5, "Ménages", "Men")]:
        dt[(typ, key)] = grab(wb, F_FIN, "DIE totale", hdr, r0 + off, lab, f"Part financeur {typ} : {lab}", "Tous niveaux", "% de la DIE")
fin["Tous niveaux"] = dt

# ---------------------------------------------------------------- 2. Structure par niveau fin
wb = load(F_STR)
st = {}
for row, lab in [(13, "Préélémentaire"), (14, "Élémentaire"), (15, "Total premier degré"), (16, "Premier cycle"),
                 (17, "Second cycle général et technologique"), (18, "Second cycle professionnel"),
                 (19, "Apprentissage du second degré"), (20, "Total second degré"),
                 (21, "Post secondaire et supérieur technique court"), (22, "Supérieur long"),
                 (23, "Apprentissage du supérieur"), (24, "Total enseignement supérieur"), (25, "Formations extrascolaires")]:
    st[lab] = grab(wb, F_STR, "Structure DIE par niveau fin", 12, row, lab, "Part dans la DIE totale", lab, "% de la DIE")
st_die = grab(wb, F_STR, "Structure DIE par niveau fin", 9, 10, "DIE en Md", "DIE totale (onglet structure)", "Tous niveaux", "Md€ constants 2024")

# ---------------------------------------------------------------- 3. Dépense par élève
wb = load(F_DEP)
dep = {}
for row, hdr, lab, key in [(10, 9, "Ensemble", "Ensemble"), (13, 12, "Premier degré", "1er"), (14, 12, "dont Préélémentaire", "Preelem"),
                           (15, 12, "dont Élémentaire", "Elem"), (18, 17, "Second degré", "2nd"), (19, 17, "dont Premier cycle", "College"),
                           (20, 17, "dont Second cycle général et technologique", "LGT"), (21, 17, "dont Second cycle professionnel", "LP"),
                           (22, 17, "dont Apprentissage", "App2nd"), (26, 25, "Enseignement supérieur", "Sup"), (30, 25, "dont Apprentissage", "AppSup")]:
    niv_lab = {"App2nd": "dont Apprentissage (second degré, ligne 22)", "AppSup": "dont Apprentissage (supérieur, ligne 30)"}.get(key, lab)
    dep[key] = grab(wb, F_DEP, "Dépense par élève, niveau", hdr, row, lab, "Dépense moyenne par élève (tous financeurs)", niv_lab, "€ constants 2024")

# ---------------------------------------------------------------- 4. DIE et part dans le PIB (pleine précision)
wb = load(F_PIB)
sh = "Part DIE dans PIB par niveau "
pib = {"DIE": grab(wb, F_PIB, sh, 9, 10, "DIE en Md", "DIE totale (pleine précision)", "Tous niveaux", "Md€ constants 2024"),
       "DIE/PIB": grab(wb, F_PIB, sh, 9, 11, "DIE/PIB", "DIE / PIB", "Tous niveaux", "% du PIB")}
for row, lab in [(15, "Premier degré"), (16, "Second degré"), (17, "Enseignement supérieur"), (18, "Formations extrascolaires")]:
    pib[lab] = grab(wb, F_PIB, sh, 14, row, lab, "DIE du niveau / PIB", lab, "% du PIB")

# ---------------------------------------------------------------- 5. SIFA (apprentis au 31/12)
wb = load(F_APP)
sifa_years = ["2020", "2021", "2022", "2023", "2024"]
ws = wb["Ensemble"]
cols = {str(c.value).replace(" (1)", "").strip(): c.column_letter for c in ws[7] if c.value is not None}
sifa = {}
for row, lab, key in [(11, "Total", "N3"), (15, "Total", "N4"), (24, "Total tous niveaux", "Tous")]:
    sifa[key] = {}
    for y in sifa_years:
        v = ws[f"{cols[y]}{row}"].value
        sifa[key][y] = v
        rows_out.append({"indicateur": "Apprentis en CFA au 31/12 (SIFA)", "niveau": {"N3": "Niveau 3 (CAP...)", "N4": "Niveau 4 (bac pro, BP...)", "Tous": "Tous niveaux"}[key],
                         "annee": f"31/12/{y}", "valeur": v, "unite": "apprentis", "fichier": F_APP, "onglet": "Ensemble",
                         "cellule": f"{cols[y]}{row}", "libelle_ligne": f"{ws[f'B{row}'].value} {ws[f'C{row}'].value or ''}".strip(),
                         "statut": "constat (2024 : Mayotte très partiel, cyclone Chido)"})

# ---------------------------------------------------------------- 6. RERS 2026 10.04 T2 : financement final des CFA en 2024 (M€)
wb = load(F_RERS)
ws = wb["10.04 Tableau 2"]
cfa = {"Etat": 0.0, "CT": 0.0, "APU": 0.0, "Men": 0.0, "Ent": 0.0, "Tot": 0.0}
for r in (11, 21, 27):
    assert "apprentis" in str(ws[f"A{r}"].value).lower(), ws[f"A{r}"].value
    for key, col in [("Etat", "D"), ("CT", "E"), ("APU", "F"), ("Men", "G"), ("Ent", "H"), ("Tot", "I")]:
        cfa[key] += float(ws[f"{col}{r}"].value or 0.0)
s_cfa = (cfa["Etat"] + cfa["CT"] + cfa["APU"]) / cfa["Tot"]

# ---------------------------------------------------------------- 7. Calculs dérivés
calc = []


def add(indic, niveau, annee, valeur, unite, formule, note=""):
    calc.append({"indicateur": indic, "niveau": niveau, "annee": annee, "valeur": round(valeur, 6) if isinstance(valeur, float) else valeur,
                 "unite": unite, "formule": formule, "note": note})


add("Part publique du financement des CFA (tous niveaux), financement final", "CFA (2nd degré + supérieur)", "2024p", s_cfa * 100, "%",
    "(État + CT + APU) / Total, RERS 2026 10.04 T2 lignes 11+21+27 (cols D,E,F / I)",
    f"Total CFA {cfa['Tot']:.1f} M€ ; État {cfa['Etat']:.1f} ; CT {cfa['CT']:.1f} ; APU {cfa['APU']:.1f} ; ménages {cfa['Men']:.1f} ; entreprises {cfa['Ent']:.1f}")
add("Part des entreprises dans le financement des CFA (tous niveaux), financement final", "CFA (2nd degré + supérieur)", "2024p",
    cfa["Ent"] / cfa["Tot"] * 100, "%", "Entreprises / Total, RERS 2026 10.04 T2")

pub = {}
for niv in ["1er degré", "2nd degré (apprentissage compris)", "Tous niveaux"]:
    for typ in ("initial", "final"):
        for y in YEARS:
            p = fin[niv][(typ, "Etat")][y] + fin[niv][(typ, "CT")][y] + fin[niv][(typ, "APU")][y]
            pub[(niv, typ, y)] = p
            add(f"Part publique (État + CT + APU), financement {typ}", niv, y, p, "% de la DIE du niveau", "somme des parts arrondies à 0,1 pt")

# DIE par niveau en Md€ 2024, pleine précision
die = {}
for y in YEARS:
    D = pib["DIE"][y]
    die[("1er", y)] = D * pib["Premier degré"][y] / pib["DIE/PIB"][y]
    die[("2nd", y)] = D * pib["Second degré"][y] / pib["DIE/PIB"][y]
    add("DIE du niveau (pleine précision)", "1er degré", y, die[("1er", y)], "Md€ constants 2024", "DIE (508145 l.10) × (DIE/PIB 1er l.15) / (DIE/PIB l.11)")
    add("DIE du niveau (pleine précision)", "2nd degré (apprentissage compris)", y, die[("2nd", y)], "Md€ constants 2024", "DIE × (DIE/PIB 2nd l.16) / (DIE/PIB l.11)")

# Dépense publique par élève (moyenne publiée × part publique)
for y in YEARS:
    for niv, key in [("1er degré", "1er"), ("2nd degré (apprentissage compris)", "2nd")]:
        for typ in ("initial", "final"):
            add(f"Dépense PUBLIQUE par élève, financement {typ}", niv, y, dep[key][y] * pub[(niv, typ, y)] / 100, "€ constants 2024",
                "dépense par élève (481445) × part publique (366603)")

# Effectifs implicites (année civile) et apprentis
for y in YEARS:
    D = pib["DIE"][y]
    n1 = die[("1er", y)] * 1e9 / dep["1er"][y]
    n2 = die[("2nd", y)] * 1e9 / dep["2nd"][y]
    add("Effectif implicite (année civile)", "1er degré", y, n1, "élèves", "DIE 1er / dépense par élève 1er")
    add("Effectif implicite (année civile)", "2nd degré (apprentissage compris)", y, n2, "élèves", "DIE 2nd / dépense par élève 2nd")
    for lab, key in [("Préélémentaire", "Preelem"), ("Élémentaire", "Elem"), ("Premier cycle", "College"),
                     ("Second cycle général et technologique", "LGT"), ("Second cycle professionnel", "LP"),
                     ("Apprentissage du second degré", "App2nd")]:
        d_fin = st[lab][y] / 100 * D
        add("DIE du sous-niveau", lab, y, d_fin, "Md€ constants 2024", "part (366606, arrondie à 0,1 pt) × DIE totale",
            "incertitude d'arrondi ± 0,05 pt de DIE")
        add("Effectif implicite du sous-niveau", lab, y, d_fin * 1e9 / dep[key][y], "élèves", "DIE du sous-niveau / dépense par élève du sous-niveau",
            "à manier avec prudence (voir NOTES : la part « premier cycle » semble inclure l'enseignement spécial du 2nd degré)" if key == "College" else "")
    d_app = st["Apprentissage du second degré"][y] / 100 * D
    n_app = d_app * 1e9 / dep["App2nd"][y]
    lo = (st["Apprentissage du second degré"][y] - 0.05) / 100 * D * 1e9 / dep["App2nd"][y]
    hi = (st["Apprentissage du second degré"][y] + 0.05) / 100 * D * 1e9 / dep["App2nd"][y]
    yy = int(y[:4])
    sifa_cal = 2 / 3 * (sifa["N3"][str(yy - 1)] + sifa["N4"][str(yy - 1)]) + 1 / 3 * (sifa["N3"][str(yy)] + sifa["N4"][str(yy)])
    add("Apprentis du 2nd degré implicites (DIE apprentissage / dépense par apprenti)", "Apprentissage du second degré", y, n_app, "apprentis",
        "part 366606 l.19 × DIE / dépense par apprenti 481445 l.22", f"fourchette d'arrondi [{lo:,.0f} ; {hi:,.0f}]".replace(",", " "))
    add("Apprentis niveaux 3+4, SIFA, pondération année civile 2/3 (31/12/N-1) + 1/3 (31/12/N)", "Apprentissage du second degré", y, sifa_cal,
        "apprentis", "SIFA 310608 lignes 11+15", f"écart implicite / SIFA : {100 * (n_app / sifa_cal - 1):+.1f} %")

# ---------------------------------------------------------------- 8. Élève hors apprentissage (2024p, et sensibilité)
y = "2024p"
D = pib["DIE"][y]
D1, D2 = die[("1er", y)], die[("2nd", y)]
N1, N2 = D1 * 1e9 / dep["1er"][y], D2 * 1e9 / dep["2nd"][y]
Dapp = st["Apprentissage du second degré"][y] / 100 * D
Napp = Dapp * 1e9 / dep["App2nd"][y]
sifa_cal_2024 = 2 / 3 * (sifa["N3"]["2023"] + sifa["N4"]["2023"]) + 1 / 3 * (sifa["N3"]["2024"] + sifa["N4"]["2024"])
ent2 = fin["2nd degré (apprentissage compris)"][("initial", "Ent")][y] / 100 * D2
add("Financement des entreprises du 2nd degré", "2nd degré (apprentissage compris)", y, ent2, "Md€ constants 2024", "part entreprises (4,5 %) × DIE 2nd")
add("Borne basse de la part non-entreprises de l'apprentissage du 2nd degré", "Apprentissage du second degré", y, 100 * (Dapp - ent2) / Dapp, "%",
    "(DIE apprentissage − financement entreprises de tout le 2nd degré) / DIE apprentissage", "sensible aux arrondis des parts (1,9 % et 4,5 %)")
add("Dépense par élève hors apprentis, tous financeurs", "2nd degré hors apprentissage", y, (D2 - Dapp) * 1e9 / (N2 - Napp), "€ 2024",
    "(DIE 2nd − DIE apprentissage) / (effectif 2nd − apprentis implicites)")
add("Dépense par élève hors apprentis, tous financeurs", "1er + 2nd degrés hors apprentissage", y, (D1 + D2 - Dapp) * 1e9 / (N1 + N2 - Napp), "€ 2024",
    "(DIE 1er + DIE 2nd − DIE apprentissage) / (N1 + N2 − apprentis)")
add("Dépense par élève, tous financeurs (contrôle : RERS 2026 publie 10 350 €)", "1er + 2nd degrés (apprentis compris)", y, (D1 + D2) * 1e9 / (N1 + N2), "€ 2024",
    "(DIE 1er + DIE 2nd) / (N1 + N2)")
for typ in ("initial", "final"):
    p1 = pub[("1er degré", typ, y)] / 100
    p2 = pub[("2nd degré (apprentissage compris)", typ, y)] / 100
    P1, P2 = p1 * D1, p2 * D2
    add(f"Dépense PUBLIQUE par élève apprentis compris, financement {typ}", "1er + 2nd degrés", y, (P1 + P2) * 1e9 / (N1 + N2), "€ 2024",
        "(part pub 1er × DIE 1er + part pub 2nd × DIE 2nd) / (N1 + N2)")
    for s_lab, s in [("s = 0 % (borne théorique)", 0.0), (f"s = {100 * s_cfa:.1f} % (structure des CFA, RERS 2026 10.04 T2)", s_cfa),
                     ("s = 15 % (haut de la fourchette compatible avec la part des entreprises du 2nd degré)", 0.15), ("s = 35 % (borne haute)", 0.35)]:
        for n_lab, n_app in [("apprentis implicites", Napp), ("apprentis SIFA pondérés", sifa_cal_2024)]:
            v2 = (P2 - s * Dapp) * 1e9 / (N2 - n_app)
            v12 = (P1 + P2 - s * Dapp) * 1e9 / (N1 + N2 - n_app)
            add(f"Dépense PUBLIQUE par élève hors apprentis, financement {typ}", "2nd degré hors apprentissage", y, v2, "€ 2024",
                "(part pub 2nd × DIE 2nd − s × DIE apprentissage) / (N2 − apprentis)",
                f"{s_lab} ; {n_lab} ; écart vs apprentis compris {100 * (v2 / (P2 * 1e9 / N2) - 1):+.1f} %")
            add(f"Dépense PUBLIQUE par élève hors apprentis, financement {typ}", "1er + 2nd degrés hors apprentissage", y, v12, "€ 2024",
                "(P1 + P2 − s × DIE apprentissage) / (N1 + N2 − apprentis)",
                f"{s_lab} ; {n_lab} ; écart vs apprentis compris {100 * (v12 / ((P1 + P2) * 1e9 / (N1 + N2)) - 1):+.1f} %")
        # part publique du 2nd degré hors apprentissage, puis par sous-niveau (hypothèse : part uniforme entre sous-niveaux)
        if s == s_cfa:
            p2h = (P2 - s * Dapp) / (D2 - Dapp)
            add(f"Part publique du 2nd degré hors apprentissage, financement {typ}", "2nd degré hors apprentissage", y, 100 * p2h, "%",
                "(P2 − s × DIE apprentissage) / (DIE 2nd − DIE apprentissage)", s_lab)
            for lab, key, pp in [("Préélémentaire", "Preelem", p1), ("Élémentaire", "Elem", p1), ("Premier cycle (collège)", "College", p2h),
                                 ("Second cycle général et technologique", "LGT", p2h), ("Second cycle professionnel", "LP", p2h)]:
                add(f"Dépense PUBLIQUE par élève du sous-niveau, financement {typ}", lab, y, dep[key][y] * pp, "€ 2024",
                    "dépense par élève du sous-niveau × part publique du niveau", "hypothèse : part publique uniforme au sein du niveau")

# ---------------------------------------------------------------- 8bis. Transposition à 2025p (NI 26.42, euros courants 2025)
# Entrées publiées : NI 26.42 xlsx, Figure 4 (parts initiales par niveau), Figure 5 (DIE par niveau), Figure 6 (dépense par élève).
# Apprentis au 31/12/2025 : RERS 2026, fiche 6.09, tableau 2, p. 235 (niveau 3 : 219 666 ; niveau 4 : 172 271), PDF rangé dans
# data/raw/effectifs_nationaux/rers2026_ch06_apprentis.pdf (page 19 du PDF).
# Hypothèses : (H-a) la part de l'apprentissage dans la DIE du 2nd degré reste à son niveau 2024p ;
#              (H-b) l'écart initial -> final de la part publique par niveau reste celui de 2024p (séries chronologiques).
wb = openpyxl.load_workbook(os.path.join(HERE, "depp_ni_2026-42_compte_education_2025_donnees.xlsx"), data_only=True)
f4, f5, f6 = wb["Figure 4"], wb["Figure 5"], wb["Figure 6"]
assert f5["A32"].value == "Premier degré" and f5["A33"].value == "Second degré"
assert f6["D31"].value == "Premier degré" and f6["A31"].value == "Préélémentaire"
D1_25, D2_25 = f5["B32"].value, f5["B33"].value                   # Md€ courants 2025
e1_25, e2_25 = f6["E31"].value, f6["E33"].value                   # 9 440 et 11 780 € (E33 : libellé D33 erroné « Supérieur »)
p1_25 = (f4["B32"].value + f4["B33"].value + f4["B34"].value) / 100   # part publique initiale 1er degré
p2_25 = (f4["C32"].value + f4["C33"].value + f4["C34"].value) / 100   # part publique initiale 2nd degré
N1_25, N2_25 = D1_25 * 1e9 / e1_25, D2_25 * 1e9 / e2_25
Napp_25 = 2 / 3 * 392035 + 1 / 3 * (219666 + 172271)
Dapp_25 = D2_25 * Dapp / D2
gap1 = (pub[("1er degré", "initial", "2024p")] - pub[("1er degré", "final", "2024p")]) / 100
gap2 = (pub[("2nd degré (apprentissage compris)", "initial", "2024p")] - pub[("2nd degré (apprentissage compris)", "final", "2024p")]) / 100
add("Part publique initiale 2025p (NI 26.42 Figure 4, B32:B34 / C32:C34)", "1er degré", "2025p", 100 * p1_25, "%", "État + CT + APU")
add("Part publique initiale 2025p (NI 26.42 Figure 4, B32:B34 / C32:C34)", "2nd degré (apprentissage compris)", "2025p", 100 * p2_25, "%", "État + CT + APU")
add("DIE apprentissage du 2nd degré 2025p (estimée)", "Apprentissage du second degré", "2025p", Dapp_25, "Md€ courants 2025",
    "DIE 2nd 2025p × (DIE apprentissage / DIE 2nd) 2024p", f"hypothèse H-a : part = {100 * Dapp / D2:.2f} % ; coût implicite par apprenti {Dapp_25 * 1e9 / Napp_25:,.0f} €".replace(",", " "))
add("Apprentis niveaux 3+4, SIFA, pondération année civile 2025", "Apprentissage du second degré", "2025p", Napp_25, "apprentis",
    "2/3 × 392 035 (31/12/2024) + 1/3 × 391 937 (31/12/2025)")
for typ, g1, g2 in [("initial", 0.0, 0.0), ("final (estimé, H-b)", gap1, gap2)]:
    P1_25, P2_25 = (p1_25 - g1) * D1_25, (p2_25 - g2) * D2_25
    add(f"Dépense PUBLIQUE par élève 2025p, financement {typ}", "1er degré", "2025p", (p1_25 - g1) * e1_25, "€ courants 2025", "dépense par élève × part publique")
    add(f"Dépense PUBLIQUE par élève 2025p, financement {typ}", "2nd degré (apprentissage compris)", "2025p", (p2_25 - g2) * e2_25, "€ courants 2025", "dépense par élève × part publique")
    base12 = (P1_25 + P2_25) * 1e9 / (N1_25 + N2_25)
    add(f"Dépense PUBLIQUE par élève 2025p, financement {typ}", "1er + 2nd degrés (apprentis compris)", "2025p", base12, "€ courants 2025", "(P1 + P2) / (N1 + N2)")
    for s_lab, s in [("s = 0 %", 0.0), (f"s = {100 * s_cfa:.1f} %", s_cfa), ("s = 15 %", 0.15), ("s = 35 %", 0.35)]:
        v2 = (P2_25 - s * Dapp_25) * 1e9 / (N2_25 - Napp_25)
        v12 = (P1_25 + P2_25 - s * Dapp_25) * 1e9 / (N1_25 + N2_25 - Napp_25)
        add(f"Dépense PUBLIQUE par élève hors apprentis 2025p, financement {typ}", "2nd degré hors apprentissage", "2025p", v2, "€ courants 2025",
            "(P2 − s × DIE apprentissage) / (N2 − apprentis SIFA pondérés)", f"{s_lab} ; écart {100 * (v2 / ((p2_25 - g2) * e2_25) - 1):+.1f} %")
        add(f"Dépense PUBLIQUE par élève hors apprentis 2025p, financement {typ}", "1er + 2nd degrés hors apprentissage", "2025p", v12, "€ courants 2025",
            "(P1 + P2 − s × DIE apprentissage) / (N1 + N2 − apprentis)", f"{s_lab} ; écart {100 * (v12 / base12 - 1):+.1f} %")

# ---------------------------------------------------------------- 9. Écriture
with open(os.path.join(HERE, "_derive_series_chrono_extraction_2021_2024.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()), delimiter=";")
    w.writeheader()
    w.writerows(rows_out)
with open(os.path.join(HERE, "_derive_series_chrono_calculs_2021_2025p.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(calc[0].keys()), delimiter=";")
    w.writeheader()
    w.writerows(calc)
print(f"{len(rows_out)} valeurs extraites ; {len(calc)} calculs dérivés")
for c in calc:
    v = c["valeur"]
    print(f"{c['indicateur'][:95]:95s} | {c['niveau'][:38]:38s} | {c['annee']:5s} | {v:>14,.2f} {c['unite']} | {c['note'][:120]}")
