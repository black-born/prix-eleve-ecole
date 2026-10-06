"""Applique les corrections de la vérification finale (chiffres-sources, cohérence-raisonnement) aux documents intégrés.
Chaque remplacement vérifie que le texte d'origine est présent exactement une fois."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:/Users/chret/Documents/EtatEcole")
ARCH = ROOT / "data/raw/recoupements/seine_saint_denis_paris"


def rep(t, old, new, n=1):
    c = t.count(old)
    assert c == n, f"{c} occurrence(s) au lieu de {n} : {old[:150]!r}"
    return t.replace(old, new)


def corriger(chemin, paires):
    t = chemin.read_text(encoding="utf-8")
    for old, new in paires:
        t = rep(t, old, new)
    chemin.write_text(t, encoding="utf-8", newline="\n")
    print("corrigé :", chemin.name, len(paires))


corriger(ROOT / "analyse_seine_saint_denis_paris.md", [
    # En bref
    ("Pour investir dans les bâtiments, ce sont au contraire les communes du 93 qui dépensent le plus (1 223 € contre 624 € par écolier et par an, moyenne 2023-2025).",
     "Pour investir, en revanche, ce sont les communes du 93 qui dépensent le plus : 1 223 € contre 624 € par écolier et par an (moyenne 2023-2025), dont 1 102 € contre 506 € pour les bâtiments."),
    ("La région Île-de-France finance les lycées de Paris et du 93 avec les mêmes barèmes, et il n'y a pas d'éducation prioritaire au lycée",
     "La région Île-de-France finance les lycées de Paris comme ceux du 93 (sa dotation de fonctionnement suit les mêmes barèmes), et il n'y a pas d'éducation prioritaire au lycée"),
    # § 2.8
    ("1 707 € en France (moyenne 2023-2025, tous budgets [COL-4] ; H-B22 ;",
     "1 707 € dans les communes à comptes par fonction de toute la France (moyenne 2023-2025, tous budgets [COL-4] ; H-B22 ;"),
    ("Paris range aussi dans ces fonctions une partie du périscolaire, que les communes du 93 rangent ailleurs (§ 3.1).",
     "Paris range aussi vraisemblablement dans ces fonctions une partie du périscolaire, que les communes du 93 rangent ailleurs (déduction à vérifier, § 3.1)."),
    # § 4.2
    ("de 133 € par élève et par an à Bondy à 3 799 € à Pantin (médiane pondérée par les élèves : 974 €).",
     "de 133 € par élève et par an à Bondy, qui impute peu de son équipement à ses écoles (H-B22), à 3 799 € à Pantin (médiane pondérée par les élèves : 974 €)."),
    ("(1 029 € contre 979 € par an en 2022-2025, subventions d'équipement comprises)",
     "(1 028 € contre 979 € par an en 2022-2025, subventions d'équipement comprises)"),
    # § 4.3
    ("(années connues pour 70 lycées sur 92 et 59 sur 68, parfois inexactes selon la chambre) [LOC-7].",
     "(années connues pour 70 lycées sur 92 et 59 sur 68, parfois inexactes selon la chambre : CRC, 2021, p. 19 [CDC-13]) [LOC-7]."),
    # § 4.4
    ("La Ville de Paris emploie dans ses écoles 1 730 agents d'entretien et 482 gardiens (2023)",
     "La Ville de Paris emploie dans ses écoles l'équivalent de 1 730 agents d'entretien et de 482 gardiens à temps plein (2023)"),
    ("Ses établissements, plus grands et plus remplis, s'usent plus vite. L'écart le plus net en sa défaveur porte sur le fonctionnement des écoles, donc en partie sur l'entretien courant, que les comptes ne séparent pas. Paris investit peu dans un parc plus ancien dont les élèves diminuent, et la chambre y signale aussi des lycées vétustes.",
     "Ses établissements, plus grands et aux effectifs en hausse, s'usent vraisemblablement plus vite. L'écart le plus net en sa défaveur porte sur le fonctionnement des écoles, donc en partie sur l'entretien courant, que les comptes ne séparent pas. Paris investit peu dans des écoles et des collèges vraisemblablement plus anciens (indication fragile de la BDNB), dont les élèves diminuent, et la chambre y signale aussi des lycées vétustes."),
    # § 4.6
    ("D'après franceinfo, le mouvement est parti à la mi-septembre 2026 du lycée Saint-Exupéry de Créteil (Val-de-Marne) ;",
     "D'après franceinfo, après de premiers blocus en Bretagne, dans le Nord et le Calvados, le mouvement s'est cristallisé à la mi-septembre 2026 au lycée Saint-Exupéry de Créteil (Val-de-Marne), son « épicentre » ;"),
    ("(4,37 M€, 2019) [LOC-6, LOC-7].",
     "(4,37 M€, 2019) [LOC-6, LOC-7] ; un programme de travaux ne dit pas l'état actuel d'un lycée."),
    # § 4.7
    ("Les locaux du 93 sont bien plus sollicités : élèves en hausse au collège et au lycée, établissements plus grands, salles manquantes pour dédoubler les classes.",
     "Les locaux du 93 sont bien plus sollicités : élèves en hausse au collège et au lycée, établissements plus grands, salles manquantes pour dédoubler les classes. Pour les lycées, le seul taux de remplissage constaté (2017) était toutefois proche : 88 % contre 86 %."),
    # Conclusion
    ("les communes du 93 investissent environ deux fois plus par écolier que la Ville (§ 4.2).",
     "les communes du 93 investissent 1,4 à 2 fois plus par écolier que la Ville, selon que l'on compte ou non les investissements scolaires qu'elle range hors des fonctions « écoles » (§ 4.2)."),
    ("la Région applique les mêmes barèmes à Paris et au 93",
     "la Région finance les lycées de Paris et du 93, avec les mêmes barèmes pour sa dotation de fonctionnement"),
    ("ils dépensent plus par élève pour les écoles (1 223 € contre 624 €, moyenne 2023-2025)",
     "ils dépensent plus par élève pour les écoles (1 223 € contre 624 € d'investissement, dont 1 102 € contre 506 € pour le bâti, moyenne 2023-2025)"),
])

corriger(ROOT / "hypotheses.md", [
    ("(242 et 249 M€, contre 62 à 64 M€ selon le périmètre et 63 M€ pour Paris ;",
     "(242 et 249 M€, contre, pour Paris, 62 à 64 M€ selon le périmètre et 63 M€ ;"),
    ("environ +2 550 à +6 750 € après corrections (+3 550 à +4 250 € si l'investissement suit chaque commune)",
     "environ +2 500 à +6 700 € après corrections (+3 500 à +4 250 € si l'investissement suit chaque commune)"),
    ("**Personnel** : comptes 621, 631, 633 et 64.",
     "**Personnel** : comptes 621, 631, 633 et 64. **Subventions d'investissement reçues** : crédit réel net des comptes 13 (hors 139), enregistré l'année où la subvention est titrée, pas celle de la dépense ; origine lue dans le compte, l'ANRU étant comptée avec l'État (1321)."),
    ("ou lycéens pré-bac (comme B). Moyenne 2021-2023",
     "ou lycéens pré-bac (comme B) ; élèves de la rentrée 2025 pour la dotation 2026, moyenne des rentrées 2021 à 2023 pour les opérations votées en 2021-2023 (B, lui, divise par les élèves de la rentrée 2024). Moyenne 2021-2023"),
    ("les dépenses courantes « bâti » (287 € des deux côtés) sont deux minimums.",
     "les dépenses courantes « bâti » (287 € des deux côtés) sont deux minimums. Bondy et Aulnay-sous-Bois imputent peu de leur équipement aux écoles (Bondy : 6 à 9 % en 2021-2025 ; Aulnay-sous-Bois : 8 à 9 % en 2024-2025 ; 30,4 % pour l'ensemble des communes du 93 en 2023-2025) : leur faible investissement « écoles » peut tenir en partie à ce choix."),
])

corriger(ROOT / "sources.md", [
    ("Effet de H-B14 pour Paris et le 93 non chiffré |\n\n---\n| Indicateur officiel de l'état du bâti scolaire",
     "Effet de H-B14 pour Paris et le 93 non chiffré |\n| Indicateur officiel de l'état du bâti scolaire"),
    ("(DEB-2, DEB-11 à DEB-13) |\n\n## Annexe A. URL exactes des requêtes d'API",
     "(DEB-2, DEB-11 à DEB-13) |\n\n---\n\n## Annexe A. URL exactes des requêtes d'API"),
    ("départ du mouvement au lycée Saint-Exupéry de Créteil ;",
     "Créteil (lycée Saint-Exupéry), « épicentre » du mouvement après de premiers blocus en Bretagne, dans le Nord et le Calvados ;"),
    ("- **Où** : [T] § 2.8, 4.2 ; H-B22.", "- **Où** : [T] § 4.2 ; H-B22."),
    ("- **Où** : [T] § 4.3 ; H-B22, anomalie 16.", "- **Où** : [T] § 4.4 ; H-B22, anomalie 16."),
    ("| `franceinfo_2026-10-02_plan_remplacements.html` | contexte (§ 1.1) |",
     "| `franceinfo_2026-10-02_plan_remplacements.html` | contexte (§ 1.1) ; sur le « bâti scolaire », pas de décision possible « pour la rentrée 2027 » (§ 4.6) |"),
])

corriger(ARCH / "SOURCES.md", [
    ("les chemins des scripts sont ceux du dossier de travail et doivent être adaptés.",
     "les chemins des scripts sont ceux du dossier de travail et doivent être adaptés. Deux sorties précèdent les corrections des vérifications : `A_ecoles/sorties/A15_Paris_investissement_elargi_vs_93.csv` (Paris « au plus » : 879 € ; 898 € en ajoutant les 6,0 M€ de l'école Pinard en 2024, voir `verif/chiffres/v16_paris_elargi_corrige.py`) ; `B_colleges/sorties/07_tableau_principal.csv` et `09_tableaux_markdown.txt` (« France » des collèges avec Mayotte : 928 €, et 979 € PPP compris ; sans Mayotte : 939 €, 979 € avec les subventions, environ 990 € avec les PPP, voir `verif/chiffres/v17_france_colleges_mayotte.py`)."),
])
