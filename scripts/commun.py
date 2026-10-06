"""Outils communs aux scripts de calcul du coût moyen d'un élève.

Chaque valeur lue dans un fichier officiel passe par `lire_cellule` ou `chercher`,
qui vérifient le libellé de la ligne et de la colonne avant de renvoyer la valeur,
puis l'enregistrent dans le journal de traçabilité (fichier, onglet, cellule, libellés).
"""
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
import warnings
from dataclasses import dataclass, field
from pathlib import Path

import openpyxl

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")
try:
    sys.stdout.reconfigure(encoding="utf-8")  # sortie lisible même redirigée vers un fichier (Windows)
except (AttributeError, ValueError):
    pass

RACINE = Path(__file__).resolve().parents[1]
BRUT = RACINE / "data" / "raw"
RESULTATS = RACINE / "resultats"
RESULTATS.mkdir(exist_ok=True)


def _norm(texte) -> str:
    return " ".join(str(texte).replace("\xa0", " ").split()).lower()


@dataclass
class Trace:
    cle: str
    valeur: object
    fichier: str
    onglet: str
    cellule: str
    libelle: str


@dataclass
class Journal:
    lignes: list[Trace] = field(default_factory=list)

    def ajouter(self, trace: Trace) -> None:
        self.lignes.append(trace)

    def ecrire(self, chemin: Path) -> None:
        with chemin.open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["cle", "valeur", "fichier", "onglet", "cellule", "libelle_verifie"])
            for t in self.lignes:
                w.writerow([t.cle, t.valeur, t.fichier, t.onglet, t.cellule, t.libelle])


class Classeur:
    """Classeur Excel officiel ouvert en lecture seule (valeurs calculées)."""

    def __init__(self, chemin: Path, journal: Journal):
        self.chemin = chemin
        self.wb = openpyxl.load_workbook(chemin, data_only=True, read_only=False)
        self.journal = journal

    def _rel(self) -> str:
        return self.chemin.relative_to(RACINE).as_posix()

    def lire_cellule(self, cle: str, onglet: str, ref: str, *, libelle_ligne: str | None = None,
                     col_libelle: str = "A", libelle_colonne: str | None = None,
                     ligne_entete: int | None = None):
        """Lit une cellule précise et contrôle les libellés de sa ligne et de sa colonne."""
        ws = self.wb[onglet]
        cell = ws[ref]
        controles = []
        if libelle_ligne is not None:
            lab = ws[f"{col_libelle}{cell.row}"].value
            if _norm(libelle_ligne) not in _norm(lab):
                raise ValueError(f"{self.chemin.name}/{onglet}/{ref} : ligne '{lab}' ≠ '{libelle_ligne}'")
            controles.append(str(lab).strip())
        if libelle_colonne is not None:
            lab = ws.cell(row=ligne_entete, column=cell.column).value
            if _norm(libelle_colonne) not in _norm(lab):
                raise ValueError(f"{self.chemin.name}/{onglet}/{ref} : colonne '{lab}' ≠ '{libelle_colonne}'")
            controles.append(str(lab).strip())
        valeur = cell.value
        if not isinstance(valeur, (int, float)):
            raise ValueError(f"{self.chemin.name}/{onglet}/{ref} : valeur non numérique '{valeur}'")
        self.journal.ajouter(Trace(cle, valeur, self._rel(), onglet, ref, " | ".join(controles)))
        return float(valeur)


def ecrire_csv(chemin: Path, lignes: list[dict]) -> None:
    """Écrit une liste de dictionnaires en CSV (séparateur ;, UTF-8 avec BOM pour Excel)."""
    if not lignes:
        return
    colonnes = list(lignes[0].keys())
    for ligne in lignes[1:]:
        for c in ligne:
            if c not in colonnes:
                colonnes.append(c)
    with chemin.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=colonnes, delimiter=";")
        w.writeheader()
        w.writerows(lignes)


def euros(x: float) -> str:
    """Format français : 9 440 €."""
    return f"{x:,.0f} €".replace(",", " ")


# ---------------------------------------------------------------------------------------------- communes (API Géo)
def cle(s) -> str:
    """Texte sans accents ni ponctuation, en minuscules (comparaisons et recherche)."""
    s = str(s).replace("œ", "oe").replace("Œ", "OE").replace("æ", "ae").replace("Æ", "AE")
    s = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def cle_commune(s) -> str:
    """Clé d'un nom de commune : comme cle(), avec « St » et « Ste » écrits en entier."""
    return re.sub(r"\bst\b", "saint", re.sub(r"\bste\b", "sainte", cle(s)))


class Communes:
    """Communes, arrondissements municipaux et communes déléguées de l'API Découpage administratif (fichiers archivés
    dans data/raw/cartographie). trouver() rattache un établissement à une commune par son code, à défaut par son nom
    dans le département (hypothèses H-E4 et H-B18)."""

    FICHIERS = ("api_geo_communes_2026-10-04.json", "api_geo_arrondissements_municipaux_2026-10-04.json")
    DELEGUEES = "api_geo_communes_associees_deleguees_2026-10-04.json"

    def __init__(self):
        dossier = BRUT / "cartographie"
        self.actuelles = [c for f in self.FICHIERS for c in json.loads((dossier / f).read_text(encoding="utf-8"))]
        self.deleguees = json.loads((dossier / self.DELEGUEES).read_text(encoding="utf-8"))
        self.par_code = {c["code"]: c for c in self.actuelles}
        self.par_nom, self.par_nom_deleguee = {}, {}
        for ix, liste in ((self.par_nom, self.actuelles), (self.par_nom_deleguee, self.deleguees)):
            for c in liste:
                ix.setdefault((c["codeDepartement"], cle_commune(c["nom"])), []).append(c)
        self.mots_chef = {}
        for c in self.deleguees:
            self.mots_chef.setdefault((c["codeDepartement"], c["chefLieu"]), []).extend(cle_commune(c["nom"]).split())
        # Une mairie partagée (mairies de secteur de Marseille, Paris Centre) ne situe pas un arrondissement : on garde
        # alors le centre.
        compte = {}
        for c in self.actuelles:
            if c.get("mairie"):
                k = tuple(c["mairie"]["coordinates"])
                compte[k] = compte.get(k, 0) + 1
        self.mairie_unique = {c["code"] for c in self.actuelles
                              if c.get("mairie") and compte[tuple(c["mairie"]["coordinates"])] == 1}

    def position(self, c) -> tuple:
        """((lon, lat), nature) : mairie si elle est propre à la commune, sinon centre (communes déléguées comprises)."""
        if c.get("type") is None and c["code"] in self.mairie_unique:
            return c["mairie"]["coordinates"], "mairie"
        return c["centre"]["coordinates"], "centre"

    def trouver(self, code, dep, nom):
        """(commune trouvée, règle) ou (None, None). Règles, dans l'ordre : code ; nom d'une commune actuelle du
        département ; nom d'une commune déléguée ou associée ; seule commune actuelle du département dont le nom contient
        l'ancien ; chef-lieu dont les communes déléguées forment ensemble l'ancien nom. Un nom ambigu ne donne rien."""
        if isinstance(code, str) and code in self.par_code:
            return self.par_code[code], "code"
        k = (dep, cle_commune(nom))
        if len(self.par_nom.get(k, [])) == 1:
            return self.par_nom[k][0], "nom"
        if len(self.par_nom_deleguee.get(k, [])) == 1:
            return self.par_nom_deleguee[k][0], "déléguée"
        motif = re.compile(r"\b" + re.escape(k[1]) + r"\b")
        m = [c for c in self.actuelles if c["codeDepartement"] == dep and motif.search(cle_commune(c["nom"]))]
        if len(m) == 1:
            return m[0], "inclusion"
        m = [chef for (dp, chef), mots in self.mots_chef.items() if dp == dep and sorted(mots) == sorted(k[1].split())]
        if len(m) == 1 and m[0] in self.par_code:
            return self.par_code[m[0]], "chef-lieu"
        return None, None

    @staticmethod
    def code_actuel(c) -> str:
        """Code de la commune actuelle (chef-lieu pour une commune déléguée ou associée)."""
        return c["chefLieu"] if c.get("type") in ("commune-deleguee", "commune-associee") else c["code"]
