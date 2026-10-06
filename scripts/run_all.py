"""Relance toute la chaîne de calcul, dans l'ordre (environ deux minutes).

    python scripts/run_all.py

Prérequis : Python 3.11+, pandas, numpy, openpyxl, matplotlib (pip install pandas numpy openpyxl matplotlib).
Les fichiers officiels bruts doivent être présents dans data/raw/ (ils le sont dans ce dossier).
"""
import runpy
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")  # sortie lisible même redirigée vers un fichier (Windows)
sys.path.insert(0, str(ICI))
ETAPES = [
    "02_effectifs.py",                       # effectifs nationaux et contrôle de l'open data
    "01_approche_A_compte_education.py",     # approche A : compte de l'éducation (DEPP)
    "03_base_etablissements.py",             # base par établissement (rentrée 2024)
    "04_approche_B_par_etablissement.py",    # approche B : répartition des budgets 2025
    "05_recoupements_et_decomposition.py",   # recoupements, sensibilités, décomposition
    "06_figures.py",                         # graphiques
    "07_carte_etablissements.py",            # carte interactive des établissements (resultats/carte_etablissements.html)
]
for etape in ETAPES:
    print(f"\n=== {etape}")
    runpy.run_path(str(ICI / etape), run_name="__main__")
print("\nTerminé : résultats dans resultats/ (tableaux CSV, figures PNG, traçabilité).")
