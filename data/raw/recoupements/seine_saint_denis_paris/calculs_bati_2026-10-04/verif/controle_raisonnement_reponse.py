# -*- coding: utf-8 -*-
"""Contrôles de la relecture critique de synthese/reponse.md et synthese/section_analyse.md (04/10/2026).

1. Longueur : mots de reponse.md, du § 2.8, de la section 4 et des remplacements ; phrases de plus de 35 et 50 mots.
2. Investissement « écoles » de Paris en 2024 (DGFiP, balances nature-fonction, extraction Q1 de la recherche A) :
   débit réel (obnetdeb - oobdeb) des comptes 20, 21, 23, fonctions 20, 21x, 28x, 29 (codes 90x/93x compris).
3. Taux de remplissage, places vacantes et manquantes des lycées (CRC IDF, IDR2021-39, PDF p. 21-23), par pdfplumber.
4. Passage de la CRC sur la double tutelle (IDR2023-57, PDF p. 23).
5. Déclarations de la Région du 28/03/2024 (« plus de 200 lycées vétustes en 2016 », « divisé par 7 »).
"""
import re
import sys
import html
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
BASE = Path(__file__).resolve().parents[1]          # analyse_bati/
SYN = BASE / "synthese"
PROJET = Path(r"C:/Users/chret/Documents/EtatEcole")


def phrases(bloc):
    out = []
    for ligne in bloc.split("\n"):
        if ligne.strip().startswith("|"):
            continue
        ligne = re.sub(r"^\s*(-|\d+\.)\s*", "", ligne)
        for x in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ÝÉ«*(])", ligne):
            if x.strip():
                out.append(x.strip())
    return out


# 1. Longueur
rep = (SYN / "reponse.md").read_text(encoding="utf-8")
sec = (SYN / "section_analyse.md").read_text(encoding="utf-8")
ana = (PROJET / "analyse_seine_saint_denis_paris.md").read_text(encoding="utf-8")
mots_alnum = len(re.findall(r"[A-Za-zÀ-ÿœŒ0-9][A-Za-zÀ-ÿœŒ0-9'’\-,]*", rep))
print("reponse.md :", mots_alnum, "mots ;", len(rep.split()), "éléments séparés par des espaces")
i28 = sec.find("### 2.8")
i39 = sec.find("## Texte à insérer : nouvelle section 4")
i4 = sec.find("## 4. Dépense")
irem = sec.find("## Remplacements")
print("§ 2.8 :", len(sec[i28:i39].split()), "mots ; section 4 :", len(sec[i4:irem].split()),
      "mots ; remplacements :", len(sec[irem:].split()), "mots ; analyse existante :", len(ana.split()), "mots")
for nom, bloc in [("§ 2.8", sec[i28:i39]), ("section 4", sec[i4:irem]), ("reponse", rep)]:
    n = [len(p.split()) for p in phrases(bloc)]
    print(f"{nom} : {len(n)} phrases, {sum(k > 35 for k in n)} de plus de 35 mots, {sum(k > 50 for k in n)} de plus de 50")

# 2. Paris 2024
for an in ["2023", "2024", "2025"]:
    f = BASE / "A_ecoles" / "brut" / f"DGFiP_{an}_Q1_communes_75_92_93_94_fonction2_budget_fonction_compte_API.csv"
    d = pd.read_csv(f, sep=";", dtype=str)
    for c in ["obnetdeb", "obnetcre", "oobdeb", "oobcre"]:
        d[c] = d[c].astype(float)
    p = d[d.ndept == "075"].copy()
    p["deb"] = p.obnetdeb - p.oobdeb
    p["fc"] = p.fonction.apply(lambda x: x[2:] if len(x) >= 4 and x[:2] in ("90", "93") else x)
    inv = p[p.compte.str.match(r"^(20|21|23)")]
    eco = inv[inv.fc.str.match(r"^(20|21|28|29)") | (inv.fc == "2")]
    cites = inv[inv.fc.str.startswith("24")]
    print(f"Paris {an} : investissement « écoles » {eco.deb.sum() / 1e6:.2f} M€ (budget principal : "
          f"{eco[eco.cbudg == '1'].deb.sum() / 1e6:.2f} M€) ; avec la fonction 24 : {(eco.deb.sum() + cites.deb.sum()) / 1e6:.2f} M€")

# 3. CRC IDR2021-39, p. 21-23
try:
    import pdfplumber
    pdf_path = BASE / "C_lycees" / "raw" / "CRC_IDF_IDR2021-39_Region_IDF_construction_renovation_entretien_lycees.pdf"
    with pdfplumber.open(pdf_path) as pdf:
        for i in (21, 22, 23):
            t = pdf.pages[i - 1].extract_text() or ""
            for l in t.split("\n"):
                if re.match(r"^(93|75|PARIS|Total général|Académie de Paris)\b", l):
                    print(f"CRC IDR2021-39, PDF p. {i} :", l)
except Exception as e:  # pragma: no cover
    print("pdfplumber indisponible :", e)

# 4. Double tutelle (CRC IDR2023-57)
txt = (BASE / "D_bati" / "txt" / "_CRC_IDR2023-57_paged.txt").read_text(encoding="utf-8")
m = re.search(r"Le département estime que cette double.*?du\s+territoire\.", txt, flags=re.S)
print("CRC IDR2023-57, PDF p. 23 :", re.sub(r"\s+", " ", m.group(0)) if m else "passage introuvable")
m = re.search(r"Quelques points noirs[^.]*\.", txt)
print("CRC IDR2023-57, PDF p. 5 :", re.sub(r"\s+", " ", m.group(0)) if m else "passage introuvable")

# 5. Région, 28/03/2024
h = (BASE / "C_lycees" / "web" / "IDF_1milliard_lycees.html").read_text(encoding="utf-8", errors="ignore")
h = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
h = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h)))
for kw in ["Plus de 200 lycées publics étaient vétustes en 2016", "divisé par 7"]:
    i = h.find(kw)
    print("Région, 28/03/2024 :", h[max(0, i - 120): i + len(kw) + 40] if i >= 0 else f"« {kw} » introuvable")
