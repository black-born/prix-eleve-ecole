"""Corrections issues de la vérification du récapitulatif des approximations (05/10/2026).
Chaque remplacement vérifie que le texte d'origine est présent exactement une fois."""
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:/Users/chret/Documents/EtatEcole")
SAUV = pathlib.Path(r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/final/sauvegarde_avant_rundown")
SAUV.mkdir(exist_ok=True)


def rep(t, old, new, n=1):
    c = t.count(old)
    assert c == n, f"{c} occurrence(s) au lieu de {n} : {old[:150]!r}"
    return t.replace(old, new)


def corriger(nom, paires):
    p = ROOT / nom
    if not (SAUV / nom).exists():
        shutil.copy2(p, SAUV / nom)
    t = p.read_text(encoding="utf-8")
    for old, new in paires:
        t = rep(t, old, new)
    p.write_text(t, encoding="utf-8", newline="\n")
    print("corrigé :", nom, len(paires))


corriger("analyse_seine_saint_denis_paris.md", [
    # § 2.3 : la fiche 22 sert de clé, recalée sur les comptes 2025
    ("(*Géographie de l'École* 2026, fiche 22, onglets 22.1 à 22.3 [DEPP-5]). B reprend ces montants (H-B10).",
     "(*Géographie de l'École* 2026, fiche 22, onglets 22.1 à 22.3 [DEPP-5]). B s'en sert comme clé de répartition, recalée sur les comptes 2025 des départements : 1 692 € à Paris et 2 504 € dans le 93 (H-B10)."),
    # § 2.4 : type de lycée et vie scolaire
    ("à structure égale (même type de lycée), l'écart est de −2,6 %, alors que Paris est à +3,9 %.",
     "à structure égale (même type de lycée), l'écart est de −2,6 %, alors que Paris est à +3,9 % : à type de lycée égal, le lycéen du 93 reçoit donc environ 6 % de moins que le lycéen parisien. L'écart brut (−3,7 %) est plus faible parce que deux tiers des lycéens parisiens sont en lycée général et technologique, le type le moins coûteux, contre 40 % dans le 93 (calcul de l'auteur, B1)."),
    ("La vie scolaire et la direction pèsent moins dans ses grands lycées (−19 % à structure égale).",
     "La vie scolaire et la direction pèsent moins dans ses grands lycées (−19 % à structure égale) : cette ligne fait presque tout l'écart avec Paris (1 313 € contre 1 667 €). Elle dépend d'une convention : dans les lycées, on retire la part des étudiants de BTS et de classes préparatoires au prorata de leur nombre (H-B7), ce qui pèse surtout sur Paris (environ un étudiant pour deux lycéens à la rentrée 2025, contre un pour onze dans le 93 [DEPP-17])."),
    # § 3.5 : pages du rapport du Sénat
    ("(Sénat, rapport n° 730, juin 2025, p. 7 et 30 [PAR-6])", "(Sénat, rapport n° 730, juin 2025, p. 7, 31 et 33 [PAR-6])"),
    # § 3.6 : calendrier au collège et au lycée
    ("B sous-estime Paris d'environ 0,8 % et le 93 d'environ 0,4 %.",
     "B sous-estime Paris d'environ 0,8 % et le 93 d'environ 0,4 %. Au collège et au lycée, l'effet joue contre le 93, qui gagne des élèves à la rentrée 2025 (collégiens du public +0,6 %, lycéens pré-bac +2,9 %) quand Paris perd des collégiens (−2,5 %) : en divisant par les élèves de l'année civile 2025, l'écart de la part de l'État entre le 93 et Paris passerait d'environ +3 % à +2 % au collège et de −4 % à −5 % au lycée (calcul de l'auteur, séries [DEPP-17])."),
    # § 4.4, point 2 : calendrier de la hausse des collégiens
    ("De 2015 à 2025, les collégiens du public augmentent de 9,7 % dans le 93 et baissent de 12,6 % à Paris ;",
     "De 2015 à 2025, les collégiens du public augmentent de 9,7 % dans le 93 (surtout avant 2019 : +8,1 % de 2015 à 2019, puis +1,5 %) et baissent de 12,6 % à Paris ;"),
    # § 4.4, point 3 : taille des lycées avec les étudiants
    ("un lycée général et technologique, 1 078 contre 695 (B1).",
     "un lycée général et technologique, 1 078 contre 695 (B1). En comptant les étudiants de BTS et de classes préparatoires, nombreux à Paris, l'écart de taille des lycées se réduit : 1 023 contre 902 élèves par lycée général, technologique ou polyvalent (rentrée 2025 [DEPP-17])."),
    # § 4.4, point 5 : la dotation de l'État par collégien
    ("contre 15,61 % en France (RPA 2023, p. 342-343 [CDC-15]).",
     "contre 15,61 % en France (RPA 2023, p. 342-343 [CDC-15]). Ce taux est bas surtout parce que le 93 investit beaucoup : rapportée au nombre de collégiens du public, la dotation est proche de la moyenne (environ 108 € par an dans le 93, 106 € en France, en 2015-2019 ; calcul de l'auteur, H-B22)."),
    # § 4.7
    ("Les locaux du 93 sont bien plus sollicités : élèves en hausse au collège et au lycée, établissements plus grands, salles manquantes pour dédoubler les classes. Pour les lycées, le seul taux de remplissage constaté (2017) était toutefois proche : 88 % contre 86 %.",
     "Les locaux du 93 sont bien plus sollicités : élèves en hausse (au lycée encore aujourd'hui, au collège surtout avant 2019), collèges plus grands, salles manquantes pour dédoubler les classes des écoles. Pour les lycées, l'écart de taille est faible si l'on compte les étudiants, et le seul taux de remplissage constaté (2017) était proche : 88 % contre 86 %."),
])

corriger("sources.md", [
    ("- **Utilisé** : p. 7 et 30 (efficacité du remplacement en 2023-2024",
     "- **Utilisé** : p. 7 et 31 (efficacité du remplacement en 2023-2024"),
    ("remplacement des absences courtes du 2nd degré faible à Paris, en Seine-Saint-Denis et dans les Hauts-de-Seine).",
     "p. 33 : remplacement des absences courtes du 2nd degré faible à Paris, en Seine-Saint-Denis et dans les Hauts-de-Seine)."),
])

corriger("hypotheses.md", [
    ("B sous-estime donc la dépense par élève d'environ **0,3 %** (environ 35 €).",
     "B sous-estime donc la dépense par élève d'environ **0,3 %** (environ 35 €). L'effet n'est pas le même partout : là où les effectifs augmentent, B surestime au contraire la dépense par élève (Seine-Saint-Denis : environ +0,2 % au collège et +0,9 % au lycée ; Paris : environ −0,8 % au collège ; analyse, § 3.6)."),
    ("Paris : Département de Paris jusqu'en 2018, Ville de Paris ensuite ;",
     "**Dotation de l'État pour l'équipement des collèges (DDEC) par collégien** : cumul 2015-2019 du tableau n° 1 de la Cour des comptes (RPA 2023, p. 343 : 40,1 M€ pour le 93, 1 401,6 M€ pour la France) / 5 / collégiens du public moyens des rentrées 2015-2019 (DEPP) : environ 108 € dans le 93 et 106 € en France. Paris : Département de Paris jusqu'en 2018, Ville de Paris ensuite ;"),
])
