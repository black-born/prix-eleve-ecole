"""Tâche E.3 (suite) — Relevé, avec références de cellules, des chiffres officiels DEPP sur la démographie scolaire :
1. Projections 2025-2035 (DEPP, document de travail n° 2026-E08, avril 2026, fichiers Excel par académie : Paris, Créteil ;
   scénario intermédiaire d'après le texte du document ; champ public / privé sous contrat).
2. Géographie de l'École 2026 : évolutions 2015-2025 (fiches 2, 6, 7, 8, 9), élèves par classe (fiche 19),
   élèves devant un professeur et taille des établissements (fiche 20).
Sortie : e3c_releves_officiels.csv (valeur, fichier, onglet, cellule).
"""
import sys
from pathlib import Path

import openpyxl
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
SRC = Path(__file__).resolve().parent / "sources"
OUT = Path(__file__).resolve().parent
rel = []


def lire(fichier, onglet, cellule_lib, cellule_val, attendu=None, note=""):
    wb = openpyxl.load_workbook(SRC / fichier, data_only=True, read_only=True)
    ws = wb[onglet]
    lib, val = ws[cellule_lib].value, ws[cellule_val].value
    if attendu:
        assert attendu.lower() in str(lib).lower(), (fichier, onglet, cellule_lib, lib)
    rel.append({"fichier": fichier, "onglet": onglet, "cellule": cellule_val, "libelle": str(lib).strip(),
                "valeur": val, "note": note})
    return val


# ---- 1. Projections par département (public), lignes « Total premier degré », « Collège », « Formations … en lycée »
PAR = "DEPP_projections-des-effectifs-d-l-ves-2025-2035---acad-mie-de-paris-515360.xlsx"
CRE = "DEPP_projections-des-effectifs-d-l-ves-2025-2035---acad-mie-de-cr-teil-xlsx-515312.xlsx"
for fichier, dep in ((PAR, "075"), (CRE, "093")):
    wb = openpyxl.load_workbook(SRC / fichier, data_only=True, read_only=True)
    for deg in ("1D", "2D"):
        ws = wb[f"{dep}_{deg}"]
        lignes = list(ws.iter_rows(min_row=1, max_row=ws.max_row, values_only=True))
        assert str(lignes[4][1]) == "2025" and str(lignes[4][11]) == "2035", lignes[4]
        secteur = None
        for i, row in enumerate(lignes, start=1):
            lab = row[0]
            if lab in ("PUBLIC", "PRIVE SOUS CONTRAT", "Total PUBLIC et PRIVE SOUS CONTRAT"):
                secteur = lab
                continue
            if lab in ("Total premier degré", "Collège", "Formations professionnelles en lycée",
                       "Formations générales et technologiques en lycée", "Total 2nd degré"):
                v25, v35 = row[1], row[11]
                pic = max(row[1:12])
                annee_pic = 2025 + list(row[1:12]).index(pic)
                rel.append({"fichier": fichier, "onglet": f"{dep}_{deg}", "cellule": f"B{i} / L{i}",
                            "libelle": f"{dep} {secteur} {lab} : 2025 / 2035", "valeur": f"{v25} / {v35}",
                            "note": f"évolution 2025-2035 : {100 * (v35 / v25 - 1):+.1f} % ; maximum {pic} en {annee_pic}"})
# National (Tableau 1 du fichier de données du document de travail)
DT = "DEPP_donn-es-associ-es-au-document-de-travail-n-2026-e08-515384.xlsx"
for r, lib in ((6, "Premier degré public, total"), (13, "Collège public"), (14, "GT public"), (15, "Pro public"),
               (16, "Second degré public, total")):
    wb = openpyxl.load_workbook(SRC / DT, data_only=True, read_only=True)
    ws = wb["Tableau 1"]
    rel.append({"fichier": DT, "onglet": "Tableau 1", "cellule": f"D{r} / E{r} / G{r}",
                "libelle": f"France, {lib} : constat 2025 / projection 2035 / variation %",
                "valeur": f"{ws[f'D{r}'].value} / {ws[f'E{r}'].value} / {ws[f'G{r}'].value}", "note": "scénario intermédiaire"})

# ---- 2. Géographie de l'École 2026
G = "GeoEcole2026_"
for onglet, r, attendu in (("2.2", 87, "Paris"), ("2.2", 105, "Seine-Saint-Denis"), ("2.2", 113, "France")):
    lire(G + "la-demographie-des-0-25-ans-518369.xlsx", onglet, f"B{r}" if attendu != "France" else f"A{r}", f"C{r}", attendu,
         "évolution de la population de 0 à 17 ans entre 2015 et 2025 (%), Insee")
for onglet in ("6.1", "6.2", "6.3"):
    for r, att in ((87, "Paris"), (105, "Seine-Saint"), (113, "France")):
        lire(G + "la-scolarisation-dans-le-premier-degre-518471.xlsx", onglet, f"B{r}" if att != "France" else f"A{r}", f"C{r}", att,
             {"6.1": "élèves du 1er degré, rentrée 2025, public + privé", "6.2": "évolution du préélémentaire 2015-2025 (%), public + privé",
              "6.3": "évolution de l'élémentaire 2015-2025 (%), public + privé"}[onglet])
for r, att in ((87, "Paris"), (105, "Seine-Saint-Denis"), (113, "France")):
    lire(G + "la-scolarisation-au-college-518480.xlsx", "7.1", f"B{r}" if att != "France" else f"A{r}", f"C{r}", att, "collégiens 2025, public + privé")
    lire(G + "la-scolarisation-au-college-518480.xlsx", "7.1", f"B{r}" if att != "France" else f"A{r}", f"D{r}", att, "évolution des collégiens 2015-2025 (%), public + privé")
for r, att in ((12, "Paris"), (33, "Créteil"), (42, "France")):
    lire(G + "la-scolarisation-en-voie-g-n-rale-et-technologique-au-lyc-e-518483.xlsx", "8.1", f"B{r}" if att != "France" else f"A{r}", f"C{r}", att, "lycéens GT 2025 (académie), public + privé")
    lire(G + "la-scolarisation-en-voie-g-n-rale-et-technologique-au-lyc-e-518483.xlsx", "8.1", f"B{r}" if att != "France" else f"A{r}", f"D{r}", att, "évolution des lycéens GT 2015-2025 (%), académie, public + privé")
    lire(G + "la-scolarisation-en-voie-professionnelle-scolaire-518486.xlsx", "9.2", f"B{r}" if att != "France" else f"A{r}", f"C{r}", att, "lycéens professionnels 2025 (académie), public + privé")
    lire(G + "la-scolarisation-en-voie-professionnelle-scolaire-518486.xlsx", "9.2", f"B{r}" if att != "France" else f"A{r}", f"D{r}", att, "évolution des lycéens professionnels 2015-2025 (%), académie, public + privé")
for onglet in ("19.2", "19.3"):
    for r, att in ((87, "PARIS"), (105, "SEINE-SAINT-DENIS"), (113, "France")):
        lire(G + "les-conditions-d-accueil-dans-le-premier-degre-518525.xlsx", onglet, f"B{r}" if att != "France" else f"A{r}", f"C{r}", att,
             {"19.2": "élèves par classe, 1er degré, rentrée 2025, public + privé, hors Ulis",
              "19.3": "évolution du nombre d'élèves par classe 2015-2025 (élèves), public + privé"}[onglet])
for onglet, lignes in (("20.1", ((87, "Paris"), (105, "Seine-Saint-Denis"), (113, "France"))),
                       ("20.2", ((88, "Paris"), (106, "Seine-Saint-Denis"), (114, "France"))),
                       ("20.3", ((88, "Paris"), (106, "Seine-Saint-Denis"), (114, "France"))),
                       ("20.4", ((88, "Paris"), (106, "Seine-Saint-Denis"), (114, "France"))),
                       ("20.5", ((87, "Paris"), (105, "Seine-Saint-Denis"), (113, "France"))),
                       ("20.6", ((87, "Paris"), (105, "Seine-Saint-Denis"), (113, "France")))):
    for r, att in lignes:
        lire(G + "les-conditions-d-accueil-dans-le-second-degre-518528.xlsx", onglet, f"B{r}" if att != "France" else f"A{r}", f"C{r}", att,
             {"20.1": "élèves devant un professeur, collège (y c. Segpa), rentrée 2024, public + privé",
              "20.2": "élèves devant un professeur, formations GT en lycée, rentrée 2024",
              "20.3": "élèves devant un professeur, formations professionnelles en lycée, rentrée 2024",
              "20.4": "part des collèges de moins de 250 élèves (%), rentrée 2025",
              "20.5": "part des LGT et LPO de moins de 500 élèves (%), rentrée 2025",
              "20.6": "part des LP de moins de 200 élèves (%), rentrée 2025"}[onglet])
out = pd.DataFrame(rel)
out.to_csv(OUT / "e3c_releves_officiels.csv", sep=";", index=False, encoding="utf-8-sig")
pd.set_option("display.width", 250, "display.max_colwidth", 120, "display.max_rows", 300)
print(out.to_string(index=False))
