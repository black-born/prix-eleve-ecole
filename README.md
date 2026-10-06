# Coût moyen d'un élève pour la puissance publique (France, 2025)

**Résultat** : en 2025, l’État, les collectivités et les autres administrations publiques dépensent **environ 9 700 € par élève et par an** (9 710 €, données 2025 provisoires ; calcul à partir du compte de l’éducation de la DEPP, NI 26.42). Cela représente environ 8 960 € au 1er degré et 10 470 € au 2nd degré, apprentis compris (11 060 € pour les seuls collégiens et lycéens). Selon le périmètre, le chiffre va de 9 530 à 9 980 € ; en comptant les bourses et l’allocation de rentrée comme dépenses des familles (financement final), il serait inférieur d’environ 3 % (calcul possible pour 2024 seulement). La reconstitution établissement par établissement (hors apprentis, élèves de l’Éducation nationale) donne 10 203 €, soit +2,4 % par rapport au calcul hors apprentis (9 968 €). Avec une autre convention pour les retraites des fonctionnaires, le chiffre serait inférieur d’environ 1 000 à 1 200 €.

## Par où commencer

| Fichier | Contenu |
|---|---|
| [rapport.md](rapport.md) | Le rapport : résultats, méthodes, graphiques, limites |
| [hypotheses.md](hypotheses.md) | **Toutes les hypothèses**, numérotées (H-…), justifiées et chiffrées |
| [sources.md](sources.md) | Toutes les sources officielles, avec liens et dates |
| [resultats/carte_etablissements.html](resultats/carte_etablissements.html) | Carte interactive des 58 068 écoles, collèges et lycées publics et privés sous contrat : dépense publique estimée par élève, décomposition, comparaison avec les établissements du même type et du même secteur ; affichage au choix par département (avec la fiche de chaque département) ou par établissement ; filtres par type, secteur et région ; l'enseignement supérieur n'est pas couvert (données : `resultats/carte_etablissements_2025.csv`, colonnes décrites dans `resultats/carte_etablissements_2025_colonnes.md`) |
| [note_synthese_93_paris.md](note_synthese_93_paris.md) | **Note de synthèse (2 pages)** : Seine-Saint-Denis et Paris, coût par élève à l'école, au collège et au lycée, avant et après correction du profil des enseignants ; à partager |
| [analyse_seine_saint_denis_paris.md](analyse_seine_saint_denis_paris.md) | Seine-Saint-Denis et Paris : le « +13 % » du ministre et le « rabais de 30 % » des syndicats confrontés à nos estimations, école, collège et lycée ; ce que nos hypothèses ne voient pas (salaires réels, primes, clés des collectivités) ; pourquoi l'écart des écoles ne se prolonge pas au collège et au lycée ; dépense et état des bâtiments |

## Organisation du dossier

```
data/raw/            fichiers officiels téléchargés, non modifiés (un SOURCES.md et un NOTES.md par dossier),
                     et extractions repérables (dossiers extractions/, fichiers TRANSCRIPTION_* et _derive_*) :
                     transcriptions de tableaux de PDF officiels ou exports de bases officielles.
                     Dépôt public : seuls les SOURCES.md, NOTES.md, extractions et calculs y figurent (voir « Données brutes »)
  depp_compte_education/   compte de l'éducation, RERS, séries DEPP, Eurostat, OCDE
  effectifs_nationaux/     effectifs d'élèves (notes DEPP, RERS)
  etablissements/          open data par établissement (élèves, personnels, heures, IPS, annuaire)
  budget_etat/             budget de l'État : RAP, PAP, Cour des comptes, extractions
  couts_personnels/        coûts et salaires des personnels
  collectivites/           comptes des collectivités (DGFiP, DGCL, OFGL)
  recoupements/            INSEE (COFOG), OCDE, Cour des comptes, rapports parlementaires
  cartographie/            fond de carte (contours administratifs Etalab), communes (API Découpage administratif)
data/processed/      base par établissement (rentrée 2024), produite par les scripts
scripts/             calculs (Python) ; run_all.py relance tout
resultats/           tableaux CSV, figures, carte interactive des établissements, traçabilité de chaque valeur lue
```

## Relancer les calculs

```
pip install pandas numpy openpyxl matplotlib
python scripts/run_all.py
```

Le calcul prend environ deux minutes (dont une pour la carte). Chaque valeur lue dans un classeur Excel officiel est d'abord contrôlée : le script vérifie le libellé de sa ligne, celui de sa colonne, ou les deux (212 valeurs sur 396). Elle est ensuite enregistrée dans `resultats/tracabilite_*.csv` (fichier, onglet, cellule, libellés vérifiés). Les montants pris dans les extractions (RAP 2025, balances DGFiP) sont listés dans `resultats/B3_intrants_extractions.csv` et dans `sources.md` (§ 9).

## Données brutes

Le dépôt public ne contient pas les fichiers téléchargés de `data/raw/` (environ 800 Mo). Il contient, pour chaque dossier, le `SOURCES.md` (titre, producteur, date, URL, taille et empreinte de chaque fichier) et le `NOTES.md`, ainsi que les extractions et les calculs de l'auteur. Pour relancer les calculs, retéléchargez les fichiers listés dans ces `SOURCES.md` et à l'annexe A de [sources.md](sources.md) (URL exactes des requêtes d'API), puis placez-les sous le même nom dans le même dossier. Les empreintes permettent de vérifier qu'il s'agit bien des mêmes versions.

Certains documents cités ne seront jamais redistribués ici, parce qu'ils ne sont pas sous licence libre : articles de presse, extraits de télévision, documents syndicaux, publications de l'Institut des politiques publiques, du Conseil d'analyse économique et de la Banque des Territoires. Ils sont seulement référencés (URL, date, empreinte).

## Licence

- **Scripts** (`scripts/`, fichiers `.py` de `data/raw/`) : licence MIT, voir [LICENSE](LICENSE).
- **Textes, tableaux, résultats et carte** : licence Creative Commons Attribution 4.0 International (CC BY 4.0), voir [LICENSE-CC-BY-4.0.txt](LICENSE-CC-BY-4.0.txt). Vous pouvez les réutiliser librement en citant l'auteur et ce dépôt.
- **Données publiques** : elles restent sous leur propre licence, le plus souvent la Licence Ouverte / Open Licence 2.0 d'Etalab. La carte embarque la feuille de style de Leaflet (licence BSD-2-Clause, mention conservée dans le fichier) et charge Leaflet et pako depuis cdnjs.
