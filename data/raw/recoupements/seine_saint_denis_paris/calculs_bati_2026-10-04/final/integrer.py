"""Intègre l'analyse « collèges, lycées et bâtiments » dans les documents du projet et archive les sources.

Lit les textes définitifs de final/ et les ajouts de sources de synthese/ (corrigés ici d'après les relectures),
sauvegarde les documents avant modification (final/sauvegarde_avant/), puis :
- analyse_seine_saint_denis_paris.md : § 2.8, partie 4, en-tête, « En bref », § 2.3, § 3, conclusion (§ 5), pistes (§ 6) ;
- hypotheses.md : H-B22, H-B23, compléments de H-B9 et H-B21, anomalies 15 à 18, récapitulatif ;
- sources.md : § 11 (compléments, fiches, débat, non archivé), annexe A.5 ;
- rapport.md et README.md : résumés ;
- data/raw/recoupements/seine_saint_denis_paris/ : copie des fichiers et SOURCES.md ; calculs de l'auteur.
Chaque remplacement vérifie que le texte d'origine est présent exactement une fois.
"""
import hashlib
import pathlib
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:/Users/chret/Documents/EtatEcole")
SP = pathlib.Path(r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad")
W = SP / "analyse_bati"
F = W / "final"
ARCH = ROOT / "data/raw/recoupements/seine_saint_denis_paris"
DOCS = ["analyse_seine_saint_denis_paris.md", "hypotheses.md", "sources.md", "rapport.md", "README.md"]


def lire(p):
    return pathlib.Path(p).read_text(encoding="utf-8")


def ecrire(p, t):
    pathlib.Path(p).write_text(t, encoding="utf-8", newline="\n")


def rep(t, old, new, n=1):
    c = t.count(old)
    assert c == n, f"{c} occurrence(s) au lieu de {n} : {old[:150]!r}"
    return t.replace(old, new)


# --- Sauvegarde ------------------------------------------------------------------------------------------------
SAUV = F / "sauvegarde_avant"
SAUV.mkdir(exist_ok=True)
for d in DOCS:
    if not (SAUV / d).exists():
        shutil.copy2(ROOT / d, SAUV / d)
if not (SAUV / "SOURCES_dossier.md").exists():
    shutil.copy2(ARCH / "SOURCES.md", SAUV / "SOURCES_dossier.md")
# Repart toujours des versions sauvegardées : le script peut être relancé.
txt = {d: lire(SAUV / d) for d in DOCS}

s2_8 = lire(F / "s2_8.md").strip()
s4 = lire(F / "s4.md").strip()
hyp = lire(F / "hyp_B22_B23.md").strip()

# --- 1. Analyse --------------------------------------------------------------------------------------------------
a = txt["analyse_seine_saint_denis_paris.md"]
a = rep(a, "Hypothèses propres à cette analyse : H-B19 à H-B21", "Hypothèses propres à cette analyse : H-B19 à H-B23")
a = rep(a, "L'écart vient presque entièrement de la commune : la Ville de Paris dépense beaucoup plus par écolier. Notre clé communale grossit cet écart, surtout parce qu'elle répartit l'investissement comme le fonctionnement : corrigé, l'écart serait plutôt de 3 500 à 4 200 € par élève (2 500 à 6 700 € selon les variantes), au lieu de 6 100 €.",
        "L'écart vient presque entièrement de la commune : la Ville de Paris dépense beaucoup plus par écolier, surtout pour son personnel. Pour investir dans les bâtiments, ce sont au contraire les communes du 93 qui dépensent le plus (1 223 € contre 624 € par écolier et par an, moyenne 2023-2025). Notre clé communale grossit donc l'écart, parce qu'elle répartit l'investissement comme le fonctionnement : corrigé, il serait plutôt de 3 500 à 4 250 € par élève (2 500 à 6 700 € selon les variantes), au lieu de 6 100 €.")
a = rep(a, "11 902 € dans le 93, 10 841 € à Paris (B) ; 500 à 1 000 € de plus après corrections, avec la prime de fidélisation (200 à 700 € sans). L'écart vient surtout de l'investissement du département (Paris investit peu dans ses collèges), de la prime de fidélisation et des aides sociales.",
        "11 902 € dans le 93, 10 841 € à Paris (B) ; 550 à 1 050 € de plus après corrections, avec la prime de fidélisation (200 à 700 € sans). Le financeur local n'est plus la commune mais le département, et la Ville de Paris investit peu dans ses collèges. L'écart vient surtout de l'investissement du département, de la prime de fidélisation et des aides sociales. B ne compte pas les remboursements des partenariats public-privé du Département de la Seine-Saint-Denis (environ 207 € par collégien du public et par an), qui l'augmenteraient.")
a = rep(a, "et sous le lycéen parisien. Il l'est davantage encore une fois corrigé l'âge des enseignants.",
        "et sous le lycéen parisien. Il l'est davantage encore une fois corrigé l'âge des enseignants. La région Île-de-France finance les lycées de Paris et du 93 avec les mêmes barèmes, et il n'y a pas d'éducation prioritaire au lycée : l'écart des écoles ne se retrouve pas au lycée, pour ce que l'on peut observer (§ 2.8).")
a = rep(a, "les absences y sont moins bien remplacées ; des postes restent vacants. Une dépense par élève ne le montre pas.",
        "les absences y sont moins bien remplacées ; des postes restent vacants. Une dépense par élève ne le montre pas.\n"
        "> - **Une dépense par élève ne dit pas l'état des bâtiments.** Les bâtiments n'en font qu'environ un dixième. Pour investir dans ses écoles et ses collèges, le 93 dépense plus par élève que Paris ; pour les lycées, les montants publiés par la Région ne montrent pas d'écart net. Aucune donnée officielle ne mesure l'état du bâti par département : un délabrement plus grand dans le 93 n'est ni confirmé ni démenti. Les sources officielles montrent des locaux bien plus sollicités dans le 93 et des problèmes précis des deux côtés ; l'entretien courant, fait par du personnel, n'est pas isolable dans les comptes (§ 4).")
a = rep(a, "Ce n'est donc pas le 93 qui investit beaucoup, c'est Paris qui investit peu.",
        "Sur 2021-2023, d'après la DEPP, le 93 est même un peu sous la moyenne pour l'investissement ; sur 2022-2025, d'après les comptes, il est au-dessus, même sans ses partenariats public-privé (§ 4.2). Dans les deux cas, c'est surtout Paris qui investit peu.")
a = rep(a, "Après corrections (§ 3.8)", "Après corrections (§ 3.7)")
a = rep(a, "\n\n## 3. Ce que nos hypothèses ne voient pas", "\n\n" + s2_8 + "\n\n## 3. Ce que nos hypothèses ne voient pas")
a = rep(a, "| 4 | Clé départementale (H-B10) | part du privé parmi les collégiens | collèges : +250 € | collèges : −150 € | B sous-estime Paris au collège |",
        "| 4 | Clé départementale (H-B10, H-B23) | part du privé parmi les collégiens ; partenariats public-privé (PPP) du 93 | collèges : +250 € | collèges : −150 € (privé) ; +207 € de capital, vraisemblablement +79 € d'intérêts (PPP, non additionnés) | B sous-estime Paris au collège ; il ne compte pas les PPP du 93 |")
a = rep(a, "en 2024 aussi, les communes du 93 ont investi 242 M€ dans leurs écoles et Paris 64 M€.",
        "en 2024 aussi, les communes du 93 ont investi 242 M€ dans leurs écoles et Paris 62 à 64 M€ selon le périmètre ; en moyenne 2023-2025, 1 223 € par écolier du public contre 624 € (§ 4.2).")
a = rep(a, "et de 2 504 € à environ 2 350 € dans le 93 (−154 €) (calcul de l'auteur, fiche 22, onglet 22.1, et B1).",
        "et de 2 504 € à environ 2 350 € dans le 93 (−154 €) (calcul de l'auteur, fiche 22, onglet 22.1, et B1). B ne compte pas non plus les remboursements des partenariats public-privé (PPP) qui ont financé 18 collèges du 93 : environ 207 € de capital par collégien du public et par an en 2022-2025, et vraisemblablement environ 79 € d'intérêts (H-B23, § 4.2). Aucun remboursement de PPP n'apparaît dans les comptes des collèges de Paris.")
a = rep(a, "Calculs : scratchpad de l'auteur, repris dans H-B21.*",
        "Calculs : scratchpad de l'auteur, repris dans H-B21.*\n\n*Ces fourchettes ne comptent pas les remboursements des PPP des collèges du 93 (environ 207 € de capital par collégien du public et par an, et vraisemblablement environ 79 € d'intérêts, H-B23) : avec eux, l'avance du collégien du 93 serait plus grande d'à peu près autant.*")
a = rep(a, "\n\n## 4. Conclusion prudente", "\n\n" + s4 + "\n\n## 5. Conclusion prudente")
a = rep(a, "4. Pour l'ensemble des administrations, l'écolier parisien coûte nettement plus, à cause de la Ville de Paris. L'écart est réel, mais notre modèle le grossit, surtout parce qu'il répartit l'investissement comme le fonctionnement : il serait plutôt de 3 500 à 4 200 € par élève que de 6 100 €.",
        "4. Pour l'ensemble des administrations, l'écolier parisien coûte nettement plus, à cause de la Ville de Paris, et surtout de son personnel (4 743 € par écolier du public contre au moins 1 462 € dans les communes du 93, moyenne 2023-2025). L'écart est réel, mais notre modèle le grossit, surtout parce qu'il répartit l'investissement comme le fonctionnement : il serait plutôt de 3 500 à 4 250 € par élève que de 6 100 €. Dans les comptes, ce n'est pas un écart d'investissement : les communes du 93 investissent environ deux fois plus par écolier que la Ville (§ 4.2).")
a = rep(a, "5. Au collège, l'élève du 93 coûte plus que l'élève parisien, surtout grâce à l'investissement du département, à la prime de fidélisation et aux aides sociales.",
        "5. Au collège, l'élève du 93 coûte plus que l'élève parisien, surtout grâce à l'investissement du département, à la prime de fidélisation et aux aides sociales. En comptant les remboursements des partenariats public-privé du département, que B ignore, l'écart serait plus grand d'environ 207 € par collégien du public et par an (H-B23).")
a = rep(a, "et leurs absences sont moins bien remplacées (rapports de l'Assemblée nationale de 2018 et 2023 ; Sénat, 2025).",
        "et leurs absences sont moins bien remplacées (rapports de l'Assemblée nationale de 2018 et 2023 ; Sénat, 2025).\n"
        "7. L'écart des écoles ne se prolonge pas au collège et au lycée parce que le financeur local change (le département au collège, la région au lycée) et y pèse moins : 16 à 23 % de la dépense, contre 35 à 60 % à l'école. Le Département de la Seine-Saint-Denis dépense plus par collégien que la Ville de Paris ; la Région applique les mêmes barèmes à Paris et au 93 ; l'éducation prioritaire, qui ajoute des heures de cours au collège, n'existe pas au lycée (§ 2.8).\n"
        "8. Pour investir dans leurs bâtiments, le 93 et ses communes ne dépensent pas moins que Paris : ils dépensent plus par élève pour les écoles (1 223 € contre 624 €, moyenne 2023-2025) et pour les collèges (1 235 € contre 333 €, moyenne 2022-2025, partenariats public-privé compris). Pour les lycées, les montants publiés par la Région ne montrent pas d'écart net. Les sources officielles montrent aussi des locaux bien plus sollicités dans le 93 et des problèmes de bâti précis (§ 4).")
a = rep(a, "- Le nombre d'heures de cours perdues par les élèves du 93 par rapport à ceux de Paris : aucune série récente n'est publiée par département.",
        "- Le nombre d'heures de cours perdues par les élèves du 93 par rapport à ceux de Paris : aucune série récente n'est publiée par département.\n"
        "- Que le bâti scolaire du 93 est, dans l'ensemble, plus dégradé que celui de Paris, ou l'inverse : aucune donnée officielle ne mesure l'état des bâtiments par département. Le seul décompte publié, l'audit des lycées de la Région en 2016, comptait plus de lycées « très vétustes » à Paris (10) que dans le 93 (1), mais il ne porte que sur les 30 cas les plus graves, alors que la Région jugeait vétustes plus de 200 lycées (§ 4.3).")
a = rep(a, "6. Le nombre d'élèves par division au lycée, par département, pour vérifier le 28,6.",
        "6. Le nombre d'élèves par division au lycée, par département, pour vérifier le 28,6.\n"
        "7. Un état des bâtiments par établissement : diagnostics des communes, du Département de la Seine-Saint-Denis et de la Ville de Paris ; fiches par lycée du diagnostic régional de 2017 ; résultats territoriaux de l'enquête de la DEPP sur les bâtiments scolaires, dont seule une publication nationale est prévue.")
a = rep(a, "## 5. Pistes pour le projet", "## 6. Pistes pour le projet")
a = rep(a, "4. **Clé départementale par collégien du public**, et clés selon les besoins",
        "4. **Clé départementale par collégien du public**, avec les remboursements des partenariats public-privé (H-B23), et clés selon les besoins")
a = rep(a, "remplaçants, absences non remplacées quand elles sont publiées.",
        "remplaçants, absences non remplacées quand elles sont publiées.\n"
        "7. **Bâtiments, à côté de la dépense et non dedans** : dans la fiche département de la carte, l'investissement dans les bâtiments par élève et par niveau sur plusieurs années (communes 2023-2025, départements 2022-2025 avec les partenariats public-privé, région pour la part rattachable), et des indicateurs d'usage des locaux (évolution des effectifs, taille des établissements). Ne pas lire la décomposition par poste (H-D2) établissement par établissement.")
assert "3 500 à 4 200" not in a and "§ 3.8" not in a
txt["analyse_seine_saint_denis_paris.md"] = a

# --- 2. Hypothèses -----------------------------------------------------------------------------------------------
h = txt["hypotheses.md"]
h = rep(h, "Ces trois hypothèses servent l'analyse [analyse_seine_saint_denis_paris.md](analyse_seine_saint_denis_paris.md). Elles ne changent pas B.",
        "Ces cinq hypothèses (H-B19 à H-B23) servent l'analyse [analyse_seine_saint_denis_paris.md](analyse_seine_saint_denis_paris.md). Elles ne changent pas B.")
h = rep(h, "Paris 610 €, l'ensemble des communes à comptes fonctionnels environ 920 € (H-B21).",
        "Paris 610 €, l'ensemble des communes à comptes fonctionnels environ 920 € (H-B21). En moyenne 2023-2025 : 1 223 € dans le 93, 624 € à Paris, 837 € pour les communes à comptes fonctionnels (H-B22).")
h = rep(h, "| 14. Clé communale | Variantes ci-dessous (DGFiP 2025 ; CRC Île-de-France, IDR2025-64). | −2 461 à +942 € | +93 à +1 013 € |",
        "| 14. Clé communale | Variantes ci-dessous (DGFiP 2025 ; CRC Île-de-France, IDR2025-64). | −2 461 à +942 € | +93 à +1 013 € |\n"
        "| 15. Partenariats public-privé des collèges du 93 (H-B23) | Capital (compte 1675) et intérêts (compte 6618) de la fonction 221, 2022-2025, DGFiP. **Non additionné.** | — | collèges : +207 € (capital), vraisemblablement +79 € (intérêts) |")
h = rep(h, "(242 et 249 M€, contre 64 et 63 M€ pour Paris). Bilan des effets 1 à 14, sans croisement : voir le § 3.7 de l'analyse.",
        "(242 et 249 M€, contre 62 à 64 M€ selon le périmètre et 63 M€ pour Paris ; en moyenne 2023-2025, 1 223 € par écolier du public contre 624 €, H-B22). Bilan des effets 1 à 14, sans croisement : voir le § 3.7 de l'analyse ; l'effet 15 n'y est pas additionné.\n\n" + hyp)
h = rep(h, "14. **Date de la déclaration du ministre** : le message X et l'entretien sur BFMTV datent du 28/09/2026 au soir (et non du 29/09, date des premiers relais).",
        "14. **Date de la déclaration du ministre** : le message X et l'entretien sur BFMTV datent du 28/09/2026 au soir (et non du 29/09, date des premiers relais).\n"
        "15. **Dette des partenariats public-privé des collèges du 93** : en 2015, la chambre régionale des comptes écrivait que le Département devait intégrer à sa dette, fin 2014, « plus de 300 M€ » au titre des investissements des partenaires privés (CRC 2015, p. 20) ; les balances DGFiP montrent 239,7 M€ inscrits en 2014 au compte 1675. Piste (déduction, à vérifier) : les 239,7 M€ correspondent à peu près aux montants nets financés par les partenaires (203,1 M€ HT, p. 114-116), TVA comprise ; les « plus de 300 M€ » compteraient aussi les participations du Département (114,6 M€ HT).\n"
        "16. **BDNB (CSTB)** : 243 des 723 bâtiments principaux d'établissements parisiens dont l'année est connue sont datés de 2020 ou après (180 de 2023, 50 de 2024), presque tous propriété de la Ville de Paris (exemple : école Tanger, 19e, datée de 2023 dans les fichiers fonciers et de 1948 dans son diagnostic de performance énergétique). Ces dates sont traitées comme inconnues (H-B22).\n"
        "17. **Annuaire de l'éducation, date d'ouverture** : le 01/05/1965, date de création de la base, est la date d'ouverture de 64,8 % des écoles publiques parisiennes et de 82,7 % des lycées publics parisiens. Ce champ, sur lequel l'OFGL fonde son indicateur d'âge des établissements (*Cap sur…* n° 21), ne date pas les bâtiments.\n"
        "18. **Places des lycées (CRC Île-de-France, IDR2021-39, p. 20-23)** : les valeurs de 2018 à 2020 sont des prévisions de la Région « à partir du constat de rentrée 2017 », dont la chambre n'a pas obtenu d'actualisation ; seul 2017 est un constat (remplissage 88 % dans le 93 et 86 % à Paris ; places manquantes 924 et 933). Le tableau des taux de remplissage est illisible en extraction texte (pdftotext) ; il a été lu avec pdfplumber.")
h = rep(h, "collèges publics : 93 − Paris de +1 061 € dans B, +200 à +1 050 € après corrections | — |",
        "collèges publics : 93 − Paris de +1 061 € dans B, +200 à +1 050 € après corrections, sans les remboursements des partenariats public-privé du Département de la Seine-Saint-Denis (environ +207 € par collégien du public, H-B23) | — |")
txt["hypotheses.md"] = h

# --- 3. Sources : ajouts de la synthèse, corrigés d'après les relectures ---------------------------------------
sa = lire(W / "synthese/sources_ajouts.md")


def entre(t, debut, fin):
    i = t.index(debut) + len(debut)
    return t[i:t.index(fin, i)]


comp = entre(sa, "## § 11.1 Compléments à des fiches existantes\n", "\n## § 11.2").strip()
fiches = entre(sa, "## § 11.2 Nouvelles fiches (sources officielles)\n", "\n## § 11.3").strip()
s113 = entre(sa, "## § 11.3 Débat public : lignes à ajouter au tableau\n", "\n## § 11.4")
s114 = entre(sa, "## § 11.4 Non archivé, introuvable ou à vérifier : lignes à ajouter\n", "\n---\n\n## Fichiers à archiver")
deb_rows = [l for l in s113.splitlines() if l.startswith("| DEB-")]
r114 = [l for l in s114.splitlines() if l.startswith("| ") and not l.startswith("| Point ")]
assert len(deb_rows) == 4 and len(r114) == 12, (len(deb_rows), len(r114))

# Compléments (§ 11.1)
comp_l = [l for l in comp.splitlines() if l.strip()]
comp_l = [l for l in comp_l if not l.startswith("- **LOC-2")]  # page de la préfecture : la DSIL vient du rapport n° 1938
comp = "\n".join(comp_l)
comp = rep(comp, "p. 52, tableau n° 21 (ETP d'agents de la Ville intervenant dans les écoles en 2023 : 7 853,6, dont 700 professeurs de la Ville, 1 910,1 ASEM, 1 730 agents d'entretien, 481,8 gardiens, 2 472,1 animateurs) ; p. 57, tableau n° 26 (« total dépenses d'équipement scolaires » : 112 473 823 € en 2019, 89 553 885 € en 2023, source Ville de Paris).",
           "p. 44 (premier contrat de partenariat de performance énergétique, signé en 2011, pour 100 écoles) ; p. 52 (tableau des ETP d'agents de la Ville intervenant dans les écoles en 2023 : 7 853,6, dont 700 professeurs de la Ville, 1 910,1 ASEM, 1 730 agents d'entretien, 481,8 gardiens, 2 472,1 animateurs) ; p. 53 (répartition du temps de travail des agents d'entretien : 34,76 % scolaire, 52,14 % périscolaire, 13,10 % extrascolaire) ; p. 57 (tableau des dépenses d'équipement scolaires : 112 473 823 € en 2019, 89 553 885 € en 2023, source Ville de Paris, soit −20,4 % ; le texte écrit « 21 % ») ; p. 58 (écoliers du public : 122 759 en 2019, 106 180 en 2023).")
comp = rep(comp, "onglets 2.1 et 2.2, lignes 87, 105 et 113, colonne C (évolution", "onglet 2.2, lignes 87, 105 et 113, colonne C (évolution")

# Fiches (§ 11.2)
fx = [
    ("p. 13-15 (transfert de 1985-1986 : 66 ou 67 collèges, 23 ans d'âge moyen, 735 élèves en moyenne, états « mauvais » ou « médiocres », parc",
     "p. 13-15 (transfert de 1985-1986 : selon les procès-verbaux transmis, incomplets, 66 ou 67 équipements, 23 ans d'âge moyen, 735 élèves en moyenne, qualifiés le plus souvent de « mauvais » et « médiocres », parc"),
    ("p. 15 et 24 (depuis 1986 : 25 collèges créés, 40 reconstruits, 34 rénovations lourdes) ; p. 18 (18 collèges en PPP) ;",
     "p. 15 (depuis 1986 : 25 collèges créés, 40 reconstruits, 34 rénovations lourdes) ; p. 18 (18 collèges en PPP) ; p. 19 (objectifs des plans précédents atteints, « mis à part quelques retards ») ;"),
    ("p. 23 (double autorité qui « complexifie et dégrade le suivi de l'entretien ») ;",
     "p. 23 (intertitre : la double tutelle « complexifie et dégrade le suivi de l'entretien » ; texte : selon le Département, elle rend plus complexe le suivi de l'entretien, avec une « forte rotation des gestionnaires d'établissements, du fait de la faible attractivité de la fonction et du territoire ») ;"),
    ("- **Utilisé** : p. 38 (capacité d'autofinancement brute de 76 € par habitant, contre 151 € pour les départements d'Île-de-France et 130 € pour les départements de plus d'un million d'habitants ; tableau mal extrait en texte, lecture de la recherche D) ; p. 45",
     "- **Utilisé** : p. 45"),
    ("- **Où** : [T] § 4.2, 4.4 ; H-B23.", "- **Où** : [T] § 4.2 ; H-B23."),
    ("**Publication** : 30/06/2015 (rapport", "**Publication** : délibéré le 26/05/2015, publié le 30/06/2015 (rapport"),
    ("p. 114-116 (« plus de 300 M€ » de dette de PPP annoncés pour fin 2014, anomalie 15).",
     "p. 20 (« soit plus de 300 M€ » à intégrer à la dette fin 2014) ; p. 114-116 (participations du Département de 39,5, 36,9 et 38,2 M€ HT ; montants nets à financer par les partenaires de 69,6, 65,6 et 67,9 M€ HT) (anomalie 15)."),
    ("p. 21-23 (places vacantes, taux de remplissage et places manquantes par département, 2017-2020, d'après les données de la Région : lycées remplis à 90 % dans le 93 et 85 % à Paris en 2020 ; places manquantes 1 360 et 760 ; places vacantes à Paris 9 928 ; tableaux lus avec pdfplumber)",
     "p. 20-23 (places vacantes, taux de remplissage et places manquantes par département, d'après les données de la Région : constat de la rentrée 2017 et prévisions pour 2018-2020 ; constat 2017 : lycées remplis à 88 % dans le 93 et à 86 % à Paris, 924 et 933 places manquantes, 6 761 et 9 093 places vacantes ; prévisions 2020 : 90 % et 85 %, 1 360 et 760 places manquantes ; tableaux lus avec pdfplumber)"),
    ("n° 2613 (R. Pilato), amiante dans les établissements scolaires, JO AN du 22/07/2025, p. 6657 ; n° 4744 (C. Guetté), amiante, JO AN du 28/10/2025, p. 8772",
     "n° 2613 (R. Pilato), « Scandale de l'amiante dans les établissements scolaires », JO AN du 22/07/2025, p. 6657 ; n° 4744 (C. Guetté), « Urgence du désamiantage en France », JO AN du 28/10/2025, p. 8772"),
    ("n° 14292 (suppression de l'observatoire ; recherche d'un « état des lieux objectivé ») ; n° 2613 et 4744 (enquête amiante d'avril 2024, présentée en mars 2025 au comité social d'administration ministériel et aux associations d'élus, non publiée)",
     "n° 14292 (question : suppression de l'observatoire par la loi n° 2020-1525, selon le député ; réponse : enquête amiante et recherche d'un « état des lieux objectivé ») ; n° 2613 (enquête amiante lancée en avril 2024, résultats « restitués … prochainement ») et n° 4744 (résultats présentés en mars 2025 au comité social d'administration ministériel et aux associations d'élus) ; aucune publication trouvée au 04/10/2026"),
    ("https://www.education.gouv.fr/les-notes-d-information-de-la-depp-89612",
     "https://www.education.gouv.fr/depp/les-notes-d-information-de-la-depp (ancienne adresse, redirigée : https://www.education.gouv.fr/les-notes-d-information-de-la-depp-89612)"),
    ("avis (collecte en 2026 auprès d'environ 3 500 écoles et établissements ; point de vue des directeurs et chefs d'établissement, pas de description technique du bâti)",
     "avis d'opportunité (enquête issue de la fusion et de l'extension de deux enquêtes annuelles, MicroTIC 1D et Immobilier – Cadre de vie ; collecte en 2026 auprès d'environ 3 500 écoles et établissements ; point de vue des directeurs et chefs d'établissement, pas de description technique du bâti ; données accessibles aux chercheurs)"),
    ("(73 extractions, requêtes et métadonnées)", "(74 extractions ; 85 fichiers avec les requêtes et les métadonnées)"),
    ("départements, Paris et Métropole de Lyon 9 730 M€, 928 € (calcul de l'auteur)",
     "départements, Paris et Métropole de Lyon 9 730 M€, 928 € ; 939 € sans Mayotte, dont l'OFGL ne donne pas de fonction 221 (calcul de l'auteur)"),
    ("« l'âge d'un bâtiment ne révèle pas son état »).",
     "« l'âge d'un bâtiment ne révèle pas son état ») ; p. 5-6 (plus haut niveau d'investissement scolaire des communes en 2019, avant les élections municipales de 2020)."),
    ("- **Où** : [T] § 4.3 ; anomalie 17.", "- **Où** : [T] § 4.2, 4.3 ; anomalie 17."),
    ("15,4, 29,0 et 36,5 M€ en 2023, 2024 et 2025 (CA 2023, p. 77, 105 et 129 ; CA 2024, p. 70, 95 et 118 ; CA 2025, p. 33, 68, 88 et 105)",
     "15,4, 35,0 et 36,5 M€ en 2023, 2024 et 2025 (CA 2023, p. 77, 105 et 129 ; CA 2024, p. 29, 70, 95 et 118, dont 6,0 M€ en 2024 pour l'école de l'équipement Pinard, ZAC Saint-Vincent-de-Paul, p. 29 ; CA 2025, p. 33, 68, 88 et 105)"),
    ("contrat de partenariat de 2011 pour la rénovation énergétique de 100 écoles (CA 2025, p. 23, 27 et 33)",
     "contrat de partenariat de performance énergétique des écoles : encours de 14,6 M€ fin 2025 (CA 2025, p. 23) et intérêts de 0,8 M€ (p. 27) ; contrat signé en 2011 pour 100 écoles selon la CRC (CDC-7, p. 44)"),
    (" et p. 41 (rénovation énergétique du lycée Paul-Éluard, 43,4 M€, lancée à l'été 2026) ; page du 28/03/2024 (« le nombre de lycées vétustes a été divisé par 7 » dans le 93).",
     " ; page du 28/03/2024 (« Plus de 200 lycées publics étaient vétustes en 2016 » ; pour la Seine-Saint-Denis, « Le nombre de lycées vétustes a été divisé par 7 »)."),
    ("- **Où** : [T] § 4.3, 4.6.", "- **Où** : [T] § 4.3."),
    ("subventions de l'ANRU, de la Région et de la Métropole, financement proche de 80 % du montant hors taxes",
     "acomptes de l'ANRU (11,08 M€), de la Région (1,6 M€) et de la Métropole (0,4 M€) ; avec la dotation politique de la ville de l'État, financement proche de 80 % du montant hors taxes"),
]
for old, new in fx:
    fiches = rep(fiches, old, new)

deb_rows = [rep(r, "Café pédagogique (D. Gani, dépêche AFP), 28/09/2026", "Café pédagogique (D. Gani, citant l'AFP), 28/09/2026")
            if r.startswith("| DEB-12") else r for r in deb_rows]
deb_rows = [rep(rep(r, "Orange Actualités (AFP), 03/10/2026", "Orange Actualités (P. Rouvière Flamand, 6Médias avec L'Express, d'après franceinfo), 03/10/2026"),
                "`orange_AFP_2026-10-03_Geffray_plan_action.html`", "`orange_6medias_2026-10-03_Geffray_plan_action.html`")
            if r.startswith("| DEB-13") else r for r in deb_rows]


def fix114(r):
    if r.startswith("| Résultats de l'enquête de la DEPP"):
        return rep(r, "| Pas d'indicateur par département, même à terme |",
                   "| Pas d'indicateur départemental publié ; données ouvertes aux chercheurs selon l'avis d'opportunité |")
    if r.startswith("| Code de l'éducation, art. L. 239-2"):
        return rep(r, "| Suppression de l'observatoire attestée aussi par la réponse à la question n° 14292 (PAR-9) |",
                   "| Suppression mentionnée aussi dans le texte de la question n° 14292 (déclaration du député), pas dans la réponse du ministère (PAR-9) ; la section réglementaire D. 239-25 à D. 239-33 reste affichée « en vigueur » sur Légifrance |")
    if r.startswith("| Investissement « écoles » de Paris en 2024"):
        return ("| Investissement « écoles » de Paris en 2024 cité au § 3.1 et en H-B21 (64 M€) | 62,4 M€ sur le périmètre des fonctions 20, 21x, 28x et 29 ; 63,7 M€ avec la sous-fonction 258, origine probable des 64 M€ "
                "| Écrit « 62 à 64 M€ selon le périmètre » (analyse, § 3.1 ; H-B21 ; H-B22) |")
    return r


r114 = [fix114(r) for r in r114]

s = txt["sources.md"]
s = rep(s, "et des hypothèses H-B19 à H-B21.", "et des hypothèses H-B19 à H-B23.")
s = rep(s, "\n\n### 11.2 Nouvelles fiches (sources officielles)",
        "\n\n**Compléments pour le § 2.8 et la partie 4 de l'analyse (collèges, lycées et bâtiments ; H-B22, H-B23)** :\n\n" + comp + "\n\n### 11.2 Nouvelles fiches (sources officielles)")
s = rep(s, "\n\n### 11.3 Débat public (non officiel, cité comme tel)", "\n\n" + fiches + "\n\n### 11.3 Débat public (non officiel, cité comme tel)")
i = s.index("| DEB-9 |")
j = s.index("\n", i)
s = s[:j] + "\n" + "\n".join(deb_rows) + s[j:]
k = s.index("### 11.4 Non archivé, introuvable ou à vérifier")
m = s.index("\n\n## Annexe A.", k)
s = s[:m] + "\n" + "\n".join(r114) + s[m:]
A5 = ("### A.5 Requêtes du dossier « collèges, lycées et bâtiments » (COL-4, COL-5, DEPP-17, LOC-7, AUT-8)\n\n"
      "Les requêtes exactes sont archivées avec les extractions, dans `data/raw/recoupements/seine_saint_denis_paris/officiel/` :\n"
      "- DGFiP, balances 2012-2025 : `DGFiP_balances_2012-2025/_urls_requetes_ecoles_2021-2025.txt` (écoles, et effectifs de la DEPP), "
      "`_urls_extraction_colleges_2012_2024.json` et `_urls_extraction_colleges_2025.json` (collèges) ; identifiants des jeux annuels : `DGFiP_identifiants_jeux_2012-2025.json` ;\n"
      "- OFGL : export de COL-5 (voir § 4) et requêtes de méthodologie données dans la fiche COL-5 ;\n"
      "- data.education.gouv.fr, Région Île-de-France (data.iledefrance.fr) et CSTB (api.bdnb.io) : URL de chaque export dans le `SOURCES.md` du dossier (colonne URL).\n\n")
s = rep(s, "## Annexe B. Vérification des liens", A5 + "## Annexe B. Vérification des liens")
txt["sources.md"] = s

# --- 4. Rapport et README ----------------------------------------------------------------------------------------
r = txt["rapport.md"]
r = rep(r, "(hypothèses H-B19 à H-B21, sources", "(hypothèses H-B19 à H-B23, sources")
r = rep(r, "il serait plutôt de 3 500 à 4 200 € par élève.",
        "il serait plutôt de 3 500 à 4 250 € par élève. Pour investir dans les bâtiments, ce sont au contraire les communes du 93 qui dépensent le plus.")
r = rep(r, "- **Ce qu'une dépense ne dit pas** : les enseignants du 93 sont plus jeunes, plus souvent contractuels, et leurs absences sont moins bien remplacées.",
        "- **Ce qu'une dépense ne dit pas** : les enseignants du 93 sont plus jeunes, plus souvent contractuels, et leurs absences sont moins bien remplacées.\n"
        "- **Collèges, lycées et bâtiments** : l'écart des écoles ne se prolonge pas au collège et au lycée, parce que le financeur local change (département, région) et y pèse moins. Une dépense par élève ne dit pas l'état des bâtiments : pour leurs écoles et leurs collèges, le 93 et ses communes investissent plus par élève que Paris ; aucune donnée officielle ne mesure l'état du bâti par département.")
txt["rapport.md"] = r
rd = txt["README.md"]
rd = rep(rd, "ce que nos hypothèses ne voient pas (salaires réels, primes, clés des collectivités) |",
         "ce que nos hypothèses ne voient pas (salaires réels, primes, clés des collectivités) ; pourquoi l'écart des écoles ne se prolonge pas au collège et au lycée ; dépense et état des bâtiments |")
txt["README.md"] = rd

# --- 5. Archivage --------------------------------------------------------------------------------------------------
rows = {"officiel": [], "debat_public": []}
for l in lire(W / "synthese/archives_table.md").splitlines():
    if not l.startswith("| `"):
        continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    dest, src, titre, prod, date, url, octets, sha, fiche = c
    dest, src, url = dest.strip("`"), src.strip("`"), url.strip("<>")
    if dest.endswith("orange_AFP_2026-10-03_Geffray_plan_action.html"):
        dest = "debat_public/orange_6medias_2026-10-03_Geffray_plan_action.html"
        titre = titre.replace("DÉBAT PUBLIC (presse, dépêche AFP)", "DÉBAT PUBLIC (presse)")
        prod = "Orange Actualités / 6Médias avec L'Express (P. Rouvière Flamand), d'après franceinfo"
    if dest.endswith("cafepedagogique_2026-09-28_mobilisation_lyceenne_IDF.html"):
        titre = titre.replace("DÉBAT PUBLIC (presse, dépêche AFP)", "DÉBAT PUBLIC (presse, citant l'AFP)")
    if url == "https://www.education.gouv.fr/les-notes-d-information-de-la-depp-89612":
        url = "https://www.education.gouv.fr/depp/les-notes-d-information-de-la-depp"
    source = SP / src
    assert source.exists(), source
    h16 = hashlib.sha256(source.read_bytes()).hexdigest()[:16]
    assert h16 == sha, (src, h16, sha)
    cible = ARCH / dest
    cible.parent.mkdir(parents=True, exist_ok=True)
    if cible.exists():
        assert hashlib.sha256(cible.read_bytes()).hexdigest()[:16] == sha, f"collision : {dest}"
    else:
        shutil.copy2(source, cible)
    rows[dest.split("/")[0]].append(f"| `{dest}` | {titre} | {prod} | {date} | <{url}> | {octets} | {sha} |")

so = lire(SAUV / "SOURCES_dossier.md")
so = rep(so, "et par les hypothèses H-B19 à H-B21.", "et par les hypothèses H-B19 à H-B23 (collèges, lycées et bâtiments : § 2.8 et partie 4 de l'analyse, ajoutés le 2026-10-04).")
so = rep(so, "- `officiel/` : publications d'administrations, d'assemblées, de juridictions financières et de la DEPP ; textes officiels (Légifrance, Bulletin officiel) ; données ouvertes (DGFiP, CNAF).",
         "- `officiel/` : publications d'administrations, d'assemblées, de juridictions financières et de la DEPP ; textes officiels (Légifrance, Bulletin officiel) ; données ouvertes (DGFiP, CNAF, OFGL, DEPP, Région Île-de-France, CSTB, ADEME) ; publications officielles des collectivités (Ville de Paris, Département de la Seine-Saint-Denis, Région Île-de-France, communes de Bobigny et de Pantin), du CNIS et de la Banque des Territoires. Les déclarations des collectivités sur leurs propres plans sont citées comme telles. Sous-dossiers : `officiel/DGFiP_balances_2012-2025/` (extractions et requêtes exactes) et `officiel/DEPP_opendata_effectifs/` (effectifs et annuaires).\n"
         "- `calculs_bati_2026-10-04/` : scripts et résultats intermédiaires de l'auteur pour le § 2.8 et la partie 4 de l'analyse (H-B22, H-B23). **Ce ne sont pas des sources** ; les chemins des scripts sont ceux du dossier de travail et doivent être adaptés.")
parts = so.split("\n## ")
assert parts[1].startswith("Sources officielles") and parts[2].startswith("Débat public"), [p[:30] for p in parts]
parts[1] = parts[1].rstrip("\n") + "\n" + "\n".join(rows["officiel"]) + "\n\n"
parts[2] = parts[2].rstrip("\n") + "\n" + "\n".join(rows["debat_public"]) + "\n"
so = "\n## ".join(parts)

# Calculs de l'auteur (non officiels) : scripts et sorties
CALC = ARCH / "calculs_bati_2026-10-04"
n_calc = 0
for sous, motifs in (("A_ecoles", ["*.py", "sorties/*"]), ("B_colleges", ["scripts/*", "sorties/*"]),
                     ("C_lycees", ["scripts/*", "resultats/*"]), ("D_bati", ["scripts/*", "resultats/*"]),
                     ("E_modele", ["*.py", "*.csv"]), ("verif", ["chiffres/*.py", "*.py"]), ("final", ["*.md", "*.py"])):
    for mot in motifs:
        for p in (W / sous).glob(mot):
            if p.is_file():
                d = CALC / sous / p.relative_to(W / sous)
                d.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, d)
                n_calc += 1

for d in DOCS:
    ecrire(ROOT / d, txt[d])
ecrire(ARCH / "SOURCES.md", so)
print("documents écrits :", DOCS)
print("fichiers archivés :", {k: len(v) for k, v in rows.items()}, "; calculs copiés :", n_calc)
