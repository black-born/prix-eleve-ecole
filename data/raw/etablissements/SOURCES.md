# SOURCES — Axe B : données officielles par établissement

Dossier : `data/raw/etablissements/`. Toutes les sources ont été consultées le **2026-10-04**.

Les fichiers bruts ne sont jamais modifiés. Les fichiers préfixés `_` sont produits par le script `_exploration.py` (voir la fin du document).

## Contrôle de reproductibilité des exports

Chaque export CSV d'open data provient de l'API Opendatasoft v2.1 de data.education.gouv.fr. Les exports ont été relancés le 2026-10-04 avec les URL indiquées ci-dessous :

- tous redonnent un fichier **identique octet pour octet** (même MD5) ;
- seule exception, l'annuaire : son contenu est identique, mais l'ordre des lignes change d'un export à l'autre.

Les empreintes MD5 sont imprimées dans `_exploration_output.txt`, section 1.

Pour retrouver la page d'un jeu, l'URL est `https://data.education.gouv.fr/explore/dataset/<identifiant>/information/`.

Abréviation utilisée dans les tableaux : `API` = `https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets`.

## 1. Open data par établissement (data.education.gouv.fr, Licence Ouverte v2.0)

### 1.1 Personnels (DEPP, bureau des études statistiques sur les personnels ; source : panel des personnels issu de BSA)

Observation au 30 novembre de chaque rentrée.

| Fichier | URL exacte | Jeu, éditeur, dates | Ce qui est utilisé |
|---|---|---|---|
| `personnels_2d_rentree2024.csv` (10 697 lignes) | `API/fr-en-indicateurs_personnels_etablissements2d/exports/csv?delimiter=%3B&where=annee_de_la_rentree_scolaire%3D%222024%22` | « Les personnels dans les établissements du second degré », DEPP. Jeu créé le 16/07/2025, mis à jour le 23/07/2026 (données traitées le 29/01/2026). **Seule la rentrée 2024 est publiée** : l'API ne renvoie que 10 697 enregistrements, tous de 2024. | Toutes les colonnes `etp_*`, à savoir `etp_total`, `etp_de_personnels_de_vie_scolaire`, `etp_enseignants_hommes_et_femmes`, `etp_d_enseignants_agreges`, `etp_d_enseignants_certifies_peps`, `etp_d_enseignants_plp`, `etp_d_enseignants_titulaires_d_un_autre_corps` et `etp_d_enseignants_non_titulaires`. Également `secteur`, `nature_de_l_etablissement`, `identifiant_de_l_etablissement` (UAI) et `code_departement`. |
| `personnels_1d_rentree2025.csv` (47 077 lignes) | `API/fr-en-indicateurs_personnels_etablissements1d/exports/csv?delimiter=%3B&where=annee_de_la_rentree_scolaire%3D%222025%22` | « Les personnels dans les établissements du premier degré », DEPP. Créé le 16/07/2025, mis à jour le 24/06/2026. Rentrées 2024 et 2025. | `etp_d_enseignants_hommes_et_femmes`, `secteur`, `identifiant_de_l_etablissement`, `code_departement`. |
| `personnels_1d_rentree2024.csv` (47 507 lignes) | Même URL avec `%222024%22` | Idem (rentrée précédente) | Idem |

### 1.2 Effectifs d'élèves (DEPP, bureau des études statistiques sur les élèves)

| Fichier | URL exacte | Jeu, dates, observation | Ce qui est utilisé |
|---|---|---|---|
| `effectifs_ecoles_1d_rentree2025.csv` (47 418 lignes) et `..._rentree2024.csv` (47 855 lignes) | `API/fr-en-ecoles-effectifs-nb_classes/exports/csv?delimiter=%3B&where=year(rentree_scolaire)%3D2025` (ou `2024`) | « Effectifs d'élèves par école ». Mis à jour le 27/08/2026. Observation à la mi-septembre (15/09/2025). Couvre France + COM + Nouvelle-Calédonie. | `numero_ecole` (UAI), `secteur`, `code_departement`, `nombre_total_eleves`, `nombre_total_classes`, `nombre_eleves_preelementaire_hors_ulis`, `nombre_eleves_elementaire_hors_ulis`, `nombre_eleves_ulis`, `nombre_eleves_ueea`, `rep`, `rep_plus`. |
| `effectifs_colleges_rentree{2023,2024,2025}.csv` (8 373 / 8 386 / 8 395 lignes) | `API/fr-en-college-effectifs-niveau-sexe-lv/exports/csv?delimiter=%3B&where=year(rentree_scolaire)%3D<année>` | « Effectifs d'élèves en collège ». Mis à jour le 27/07/2026. Observation le 01/10. | `numero_college` (UAI), `nombre_eleves_total` (formations du 1er cycle, SEGPA et ULIS comprises), `nombre_d_eleves_total_segpa`, `nombre_d_eleves_total_ulis`, `rep`, `rep0` (= REP+). |
| `effectifs_lycees_gt_rentree{2023,2024,2025}.csv` (2 523 / 2 532 / 2 537 lignes) | `API/fr-en-lycee_gt-effectifs-niveau-sexe-lv/exports/csv?delimiter=%3B&where=year(rentree_scolaire)%3D<année>` | « Effectifs d'élèves en lycée d'enseignement général et technologique ». Mis à jour le 27/07/2026. | `numero_lycee` (UAI), `nombre_d_eleves` |
| `effectifs_lycees_pro_rentree{2023,2024,2025}.csv` (2 206 / 2 206 / 2 214 lignes) | `API/fr-en-lycee_pro-effectifs-niveau-sexe-lv/exports/csv?delimiter=%3B&where=year(rentree_scolaire)%3D<année>` | « Effectifs d'élèves en lycée professionnel ». Mis à jour le 27/07/2026. Les « autres formations professionnelles » sont ajoutées à partir de 2025. | `numero_lycee` (UAI), `nombre_d_eleves` |
| `effectifs_hebergement_2d_rentree{2023,2024,2025}.csv` (10 847 / 10 846 / 10 860 lignes) | `API/fr-en-mode-hebergement-eleves-etablissements-2d/exports/csv?delimiter=%3B&where=rentree%3D<année>` | « Le mode d'hébergement des élèves dans les établissements du second degré ». Mis à jour le 05/08/2026. Observation le 01/10. **Une ligne par UAI pour tout le 2nd degré.** | `uai`, `type_d_etablissement`, `secteur`, `code_departement`, `nombre_d_eleves_dans_une_formation_du_second_degre`, `nombre_d_eleves_dans_une_formation_du_superieur` (post-bac en lycée), effectifs par mode d'hébergement. |

### 1.3 Moyens d'enseignement H/E (DEPP ; source : bases-relais)

Ces deux jeux donnent les heures hebdomadaires d'enseignement financées par le ministère, par UAI et par niveau de formation. Observation fixée au 01/11 (elle varie selon l'établissement entre le 1er septembre et le 15 décembre).

| Fichier | URL exacte | Jeu, dates | Ce qui est utilisé |
|---|---|---|---|
| `moyens_enseignants_2d_public_rentree2024.csv` (12 868 lignes) et `..._rentree2025.csv` (12 872 lignes) | `API/fr-en-moyens_enseignants_2d_public/exports/csv?delimiter=%3B&where=year(annee)%3D2024` (ou `2025`) | « Indicateurs d'encadrement H/E et E/S à la rentrée dans le secteur public ». Mis à jour le 09/06/2026. Rentrées 2023 à 2025. | Lignes d'établissement uniquement (on exclut `niveau` = « Total Département … » ou « Total Académie … »). Colonnes `uai`, `niveau` (Collège, Segpa, Lycée général et technologique, Lycée professionnel, EREA, STS, CPGE, Prépa seconde), `numerateur_h_e_nb_heures_enseignement_hebdo_devant_eleves` (H) et `denominateur_h_e_somme_eleves_en_division` (E). La valeur « ns » est traitée comme manquante. |
| `moyens_enseignants_2d_prive_rentree2024.csv` (4 134 lignes) et `..._rentree2025.csv` (4 107 lignes) | `API/fr-en-moyens_enseignants_2d_prive/exports/csv?delimiter=%3B&where=year(annee)%3D2024` (ou `2025`) | Équivalent pour le privé sous contrat. Mis à jour le 09/06/2026. Les métadonnées indiquent « 2023-2024 », mais les données contiennent 2025. | Idem |

### 1.4 Caractéristiques des établissements

| Fichier | URL exacte | Jeu, dates | Ce qui est utilisé |
|---|---|---|---|
| `annuaire_education_extrait_2026-10-04.csv` (68 564 lignes) | `API/fr-en-annuaire-education/exports/csv?delimiter=%3B` (export complet) | « Annuaire de l'éducation », DNE. Mise à jour quotidienne (dernière le 03/10/2026). Instantané : il ne contient que les établissements ouverts au 03/10/2026. | Contrôle des UAI (99,7 % des UAI 2d et 99,2 % des UAI 1d 2025 s'y retrouvent). Attributs `type_etablissement`, `statut_public_prive`, `ulis`, `segpa`, `appartenance_education_prioritaire`. 77 UAI apparaissent en double. Pour la carte des établissements (`scripts/07_carte_etablissements.py`) : `latitude`, `longitude` (WGS84), `precision_localisation`, `nom_etablissement`, `type_etablissement`, `nom_commune`, `ecole_maternelle`, `ecole_elementaire` (type des écoles sans effectifs par niveau), `type_contrat_prive` (écoles sous contrat pour une partie des classes). |
| `cites_scolaires_extrait_2026-10-04.csv` (1 742 lignes) | `API/fr-en-cites_scolaires/exports/csv?delimiter=%3B` | « Liste des cités scolaires », MEN. Mise à jour quotidienne (03/10/2026). | `code_cite_scolaire`, `uai` : 806 cités, 1 742 UAI. |
| `etablissements_education_prioritaire_extrait_2026-10-04.csv` (8 501 lignes) | `API/fr-en-etablissements-ep/exports/csv?delimiter=%3B` | « Etablissements de l'éducation prioritaire », DGESCO. Mis à jour le 02/02/2026. Carte `ep_2022_2023` (rentrée 2023). | Contrôle seulement : on préfère les indicateurs REP/REP+ des fichiers d'effectifs, actualisés à chaque rentrée. |
| `ips_colleges_2024-2025.csv` (6 987) et `ips_colleges_2025-2026.csv` (7 089) | `API/fr-en-ips-colleges-ap2023/exports/csv?delimiter=%3B&where=rentree_scolaire%3D%222024-2025%22` (ou `2025-2026`) | « Indices de position sociale des collèges (à partir de 2023) », DEPP. Mis à jour le 01/09/2026. | `uai`, `ips` |
| `ips_lycees_2024-2025.csv` (3 631) et `ips_lycees_2025-2026.csv` (3 662) | `API/fr-en-ips-lycees-ap2023/exports/csv?delimiter=%3B&where=rentree_scolaire%3D%22<année>%22` | « Indices de position sociale des lycées (à partir de 2023) », DEPP. Mis à jour le 10/06/2026. | `uai`, `ips_etab` |
| `ips_ecoles_2024-2025.csv` (32 494) | `API/fr-en-ips-ecoles-ap2022/exports/csv?delimiter=%3B&where=rentree_scolaire%3D%222024-2025%22` | « Indices de position sociale des écoles (à partir de 2022) », DEPP. **N'est plus actualisé.** Seules les écoles ayant des élèves de CM2 sont couvertes (les maternelles sont exclues). | `uai`, `ips` |
| `ips_erea_2024-2025.csv` (77) et `ips_erea_2025-2026.csv` (77) | `API/fr-en-ips-erea-ap2022/exports/csv?delimiter=%3B&where=rentree_scolaire%3D%22<année>%22` | « Indices de position sociale des EREA (à partir de 2022) », DEPP | `uai`, `ips` |

### 1.5 Métadonnées (dossier `_metadata/`)

Chaque fichier JSON est la réponse de `API/<identifiant>` (description, champ, date d'observation, licence, définition des champs) :

- personnels : `fr-en-indicateurs_personnels_etablissements1d.json`, `…2d.json` ;
- effectifs : `fr-en-ecoles-effectifs-nb_classes.json`, `fr-en-college-effectifs-niveau-sexe-lv.json`, `fr-en-lycee_gt-…json`, `fr-en-lycee_pro-…lv.json`, `fr-en-lycee_pro-effectifs-niveau-sexe-mef.json` (jeu non téléchargé : inutile, car le jeu hébergement sépare déjà le second degré du supérieur), `fr-en-mode-hebergement-eleves-etablissements-2d.json` ;
- moyens H/E : `fr-en-moyens_enseignants_2d_public.json`, `…_prive.json` ;
- caractéristiques : `fr-en-annuaire-education.json`, `fr-en-cites_scolaires.json`, `fr-en-etablissements-ep.json`, les quatre `fr-en-ips-*.json` ;
- autres :
  - `fr-en-budget-missions.json` : budget de l'État de 2007 à 2020, non utilisé ici ;
  - `RegionCVL_dotations-de-fonctionnement-versees-aux-lycees-2025.json` : métadonnées du jeu régional (voir § 3).

## 2. Références nationales DEPP (education.gouv.fr) pour la couverture

| Fichier | URL exacte | Titre, date | Ce qui est utilisé (emplacement) |
|---|---|---|---|
| `DEPP_Panorama_personnels_2024-2025.pdf` (380 p.) | https://www.education.gouv.fr/sites/default/files/document/panorama-statistique-des-personnels-de-l-enseignement-scolaire-2024-2025-475342.pdf | DEPP, *Panorama statistique des personnels de l'enseignement scolaire 2024-2025*, cité « Panorama 2025 ». PDF créé le 22/09/2025, modifié le 03/10/2025. **Seule source au 30/11/2024** au format ETP. | **Figure 2.1, p. 32** : effectifs et « Nombre en ETP » des enseignants au 30/11/2024 par secteur et degré. **Figure 2.14, p. 47** : ETP par corps, public. **Figure 2.16, p. 50** : ETP par corps, privé. |
| `DEPP_Panorama_personnels_2025-2026_chapitre2_enseignants_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/document/chapitre-2-les-enseignants-520474.xlsx (page : https://www.education.gouv.fr/depp/panorama-statistique-des-personnels-de-l-enseignement-scolaire-2025-2026-504389) | DEPP, Panorama 2025-2026 (« Panorama 2026 »), chapitre 2 « Les enseignants ». Classeur modifié le 03/09/2026. Édition la plus récente. | **Onglet 2.1** : colonne L « Nombre en ETP » au 30/11/2025, lignes 6 (public 1er degré, 342 449), 9 (public 2nd degré, 377 093), 21 (privé 1er degré, 42 231), 24 (privé 2nd degré, 87 222), 42 (ensemble, 848 996). Onglets 2.15 et 2.16 : ventilation par corps. Fichier identique (même MD5) à celui de `../couts_personnels/`. |
| `DEPP_RERS2025_chapitre9_personnels.pdf` (64 p.) | https://www.education.gouv.fr/sites/default/files/2025-07/rers2025-chapitre-9-441738.pdf | DEPP, RERS 2025, chapitre 9 « Les personnels ». PDF du 29/07/2025. | **Fiche 9.01, p. 2 du PDF (p. 331)** : « Total des ETP consacrés à la mission » à la rentrée 2024 (enseignement en classe, remplacement, besoins spécifiques, documentation, direction, éducation, assistance éducative). **Fiche 9.02, p. 4 du PDF (p. 333)** : effectifs physiques par mission et par corps. |
| `DEPP_RERS2026_chapitre9_personnels.pdf` (67 p.) | https://www.education.gouv.fr/sites/default/files/document/9-les-personnelspdf-519300.pdf (page : https://www.education.gouv.fr/depp/reperes-et-references-statistiques-2026-505320) | DEPP, RERS 2026, chapitre 9. PDF du 27/07/2026. Édition la plus récente. | **Fiche 9.01, p. 3 du PDF (p. 341)** : ETP par mission à la rentrée 2025. Les sous-totaux du 1er degré y sont **incohérents** (voir NOTES). |
| `DEPP_NI_25-58_effectifs_1er_degre_rentree2025_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/2025-11/depp-ni-2025-58-donnees-229890-les-effectifs-dans-le-premier-degr--473912.xlsx | Données de la NI 25.58, octobre 2025 (classeur du 16/10/2025) | Onglet « Figure 7 en ligne », **ligne 42 (France)**, colonnes G/H (public 2024/2025), P/Q (privé), Y/Z (ensemble). Identique au fichier de `../effectifs_nationaux/`. |
| `DEPP_NI_25-59_effectifs_2nd_degre_rentree2025_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/2025-11/depp-ni-2025-59-donn-es-les-effectifs-dans-le-second-degr-5-621-millions-d-l-ves-scolaris-s-la-rentr-e-2025-473906.xlsx | Données de la NI 25.59, octobre 2025 (classeur du 15/10/2025) | Onglet « Figure 10 en ligne », **ligne 32 (Ensemble second degré)**, colonnes D/E (public 2024/2025), I/J (privé), N/O (ensemble). Identique au fichier de `../effectifs_nationaux/`. |

## 3. Dépenses par établissement : open data local (partiel)

| Fichier | URL exacte | Éditeur, titre, date | Ce qui est utilisé |
|---|---|---|---|
| `RegionCVL_dotations_fonctionnement_lycees_2025.csv` (293 lignes) | https://data.centrevaldeloire.fr/api/explore/v2.1/catalog/datasets/dotations-de-fonctionnement-versees-aux-lycees-de-la-region-centre-val-de-loire-en-2025/exports/csv?delimiter=%3B (fiche data.gouv.fr : https://www.data.gouv.fr/datasets/dotations-de-fonctionnement-versees-aux-lycees-de-la-region-centre-val-de-loire-en-2025) | Région Centre-Val de Loire, « Dotations de fonctionnement versées aux lycées … en 2025 », publié le 27/01/2026 | Exemple de dépense de collectivité par UAI : 98 lycées publics, 37 426 870 € au total, dont DGF 34 544 007 €. Colonnes `code_uai`, `type_dotations`, `montant_2025`. |

Jeux recensés mais **non téléchargés** (couverture trop partielle ou trop ancienne) :

- Région Île-de-France :
  - « Données budgétaires des lycées – subventions votées » (data.iledefrance.fr, jeu `subventions-votees-pour-les-lycees`) : montants votés de 2021 à 2023, soit 212 980 277 € (2021), 222 201 682 € (2022) et 219 942 394 € (2023) ; jeu non mis à jour depuis le 20/03/2024 ;
  - « Données budgétaires des lycées – opérations directes votées » (data.iledefrance.fr, jeu `donnees-budgetaires-lycees-operations-directes`) ;
  - ces deux jeux sont référencés sur data.gouv.fr (`donnees-budgetaires-des-lycees-subventions-votees` et `donnees-budgetaires-des-lycees-operations-directes-votees`).
- Département de la Gironde, « Montant des dotations des collèges publics de Gironde », 2015-2017 : https://www.data.gouv.fr/datasets/montant-des-dotations-des-colleges-publics-de-gironde-1
- Région Centre-Val de Loire, mêmes dotations pour 2017 à 2024 (un jeu par année sur data.gouv.fr).

## 4. Recherches effectuées (sans téléchargement)

- **Catalogue complet de data.education.gouv.fr**, soit 306 jeux, listé via `API?limit=100&offset=…&order_by=dataset_id` :
  - aucun jeu de budget, de compte financier d'EPLE, de dotation horaire globale (DHG) ou de dotation des collectivités par établissement ;
  - seuls jeux financiers par établissement, très partiels : `fr-en-aap-snee-ecoles` (subventions de l'État au « socle numérique » des écoles) et `fr-en-hybridation_lycees_par_lycee` (subventions à l'hybridation) ;
  - `fr-en-budget-missions` donne le budget de l'État par mission de 2007 à 2020, et non par établissement.
- **API de recherche de data.gouv.fr** (`https://www.data.gouv.fr/api/1/datasets/?q=…`), requêtes « comptes financiers EPLE », « budget EPLE », « dotation collèges », « dotation lycées », « dotation horaire globale », « fonds de roulement EPLE » : aucun jeu national, seulement les jeux locaux du § 3.
- Recherche web sur les comptes financiers des EPLE (Op@le) : on ne trouve que des circulaires académiques de transmission (par exemple ac-creteil.fr, ac-nantes.fr). Aucune diffusion publique des données.

## 5. Fichiers produits par le script (dérivés, ce ne sont pas des sources)

| Fichier | Contenu |
|---|---|
| `_exploration.py` | Script reproductible : inventaire, appariements, totaux, couverture, distributions, exports. Il relit et contrôle les valeurs recopiées des PDF avec pypdf. |
| `_exploration_output.txt` | Sortie complète du script (sections 1 à 6) |
| `_derive_ecoles_1d_rentree2025.csv`, `_derive_ecoles_1d_rentree2024.csv` | Une ligne par UAI d'école (personnels et effectifs réunis, jointure externe) : élèves par niveau, classes, REP/REP+, ETP enseignants, statut d'appariement, indicateur de champ France, IPS 2024-2025 |
| `_derive_etablissements_2d_rentree2024.csv` | Une ligne par UAI du 2nd degré : élèves du second degré et du post-bac, élèves par niveau (collège, SEGPA, ULIS, LGT, LP), ETP par corps, ETP de vie scolaire, ETP total, ETP enseignants imputés « ss », heures H/E par niveau, part post-bac et sa source, ETP hors post-bac, cité scolaire, appariement, champ France, IPS 2024-2025 |
