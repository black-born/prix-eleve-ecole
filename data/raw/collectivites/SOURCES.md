# SOURCES — Axe « Dépenses des collectivités territoriales pour l'enseignement scolaire »

Dossier : `data/raw/collectivites/`. Tous les fichiers ont été consultés ou téléchargés le **2026-10-04**, avec `curl` (en-têtes de navigateur) ou l'API Opendatasoft. Ils sont conservés **sans modification**.

**Contrôles effectués**
- Type réel de chaque fichier vérifié (signature `%PDF`, `PK` pour xlsx/ods, CSV UTF-8) : aucune page HTML d'erreur.
- Fichiers laissés par l'exécution interrompue précédente : 17 fichiers, tous valides et tous conservés. Aucun fichier `_tmp_` ni corrompu à supprimer.
- Provenance de ces 17 fichiers confirmée par un **re-téléchargement à l'URL officielle le 2026-10-04, avec md5 identique** :
  - fichiers DGCL : retéléchargés depuis les liens de la page CLC 2026 ;
  - CSV OFGL : export rejoué via l'API ;
  - notice DGFiP : pièce jointe du jeu 2025 ;
  - fichiers DEPP : md5 identiques aux copies du dossier voisin `depp_compte_education/`, dont les URL y sont documentées.
- « Date » = date de publication indiquée par l'éditeur ou, à défaut, en-tête HTTP `Last-Modified`.

## 1. DGCL — « Les collectivités locales en chiffres 2026 » (DESL, ministère chargé des collectivités territoriales)

Page de l'édition : https://www.collectivites-locales.gouv.fr/les-collectivites-locales-en-chiffres-2026. Copie brute : `DGCL_CLC2026_page_web.html`. Mises à jour indiquées : chapitre 4 « septembre 2026 », chapitre 3 « août 2026 », chapitre 6 « septembre 2026 ».

Préfixe commun des URL : `https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/DESL/2026/CLC/`

| Fichier | URL (après le préfixe) | Titre | Date | Ce qui est utilisé |
|---|---|---|---|---|
| `DGCL_CLC2026_4F_Ventilation_fonctionnelle_CG25.xlsx` | `4F%20-%20Ventilation%20fonctionnelle%20CG25.xlsx` | 4F – Ventilation fonctionnelle des dépenses, comptes de gestion 2025 | Last-Modified 24/06/2026 | Onglets F1 Comm (l. 16-22, 54, 65-67), F2 GFP (mêmes lignes), F3 Dept (l. 13-18, 53, 65), F4 Reg+CTU (l. 12-21, 42, 61), F5 Ens (l. 11-16, 37, 47-49), F6 BA et Synd (l. 8, 30). Colonnes B-D = 2025, P-R (F1-F4) ou M-O (F5-F6) = 2024. Onglets « Série » 2013-2025 (F1 Série l. 5-6 et 72-74 : population et budgets dans/hors champ) |
| `DGCL_CLC2026_Chap4_finances_collectivites_2022-2025.xlsx` | `Chapitre%204%20-%202026-%20Les%20finances%20des%20collectivit%C3%A9s%20locales-2022-2025.xlsx` | Chapitre 4 – Les finances des collectivités locales 2022-2025 | 25/08/2026 | Onglet « Définitions » (agrégats comptables par nomenclature) ; onglets 4.13a-e (= 4F) |
| `DGCL_CLC2026_4A_Budgets_principaux_2022-2025.xlsx` | `4A%20-%20Budgets%20principaux%202022-2025.xlsx` | 4A – Budgets principaux 2022-2025 | 24/06/2026 | Contexte (comptes par niveau) ; non exploité en détail |
| `DGCL_CLC2026_4A_Presentation_Budgets_principaux_CG25.pdf` | `4A_Pr%C3%A9sentation%20Budgets%20principaux%20CG25.pdf` | Présentation du chapitre 4 (CG 2025) | 03/09/2026 | p. 1-2 : « Enseignement, formation et apprentissage » −1,2 % en 2025 ; principe de consolidation (fiche 4.12) ; définitions. PDF image : lu visuellement |
| `DGCL_CLC2026_Chap3_finances_APUL_2026.xlsx` | `Chapitre%203%20-%20Les%20finances%20des%20administrations%20publiques%20locales-2026.xlsx` | Chapitre 3 – Les finances des APUL (comptes nationaux Insee, base 2020) | 25/08/2026 | Onglet « 3.5 » (titre interne « 3.6 Les dépenses des administrations publiques par fonction »), année 2024 : l. 15 Enseignement B15 (APUC), C15 (APUL), E15 (ensemble APU consolidé) ; notes l. 17-19 |
| `DGCL_CLC2026_Chap3_finances_APUL_2026.pdf` | `Chapitre%203_2026.pdf` | Chapitre 3 – Présentation et définitions | 25/08/2026 | p. 1 (part de l'enseignement dans les dépenses APUL) ; p. 2 (les ODAL incluent les EPLE, hors masse salariale des enseignants) |
| `DGCL_CLC2026_Chap6_Transferts_financiers_2026.xlsx` | `Chapitre%206%20-%20Transferts%20financiers%202026.xlsx` | Chapitre 6 – Les concours financiers de l'État | 03/09/2026 | « 6.1 » l. 12-14 : DDEC, DRES, DGCES en LFI 2022-2026 (B-F). « 6.2 » l. 12-14 : exécution 2022-2024 (B-D). « 6.1 version_web » : l. 10 DSI, l. 50-54 DGD, l. 71 subventions des autres ministères, l. 78-83 fiscalité transférée acte II |
| `DGCL_CLC2026_Chap6_Transferts_financiers_texte_2026.pdf` | `Chapitre%206%20transferts%20financiers%20Texte%202026.pdf` | Chapitre 6 – Présentation et définitions | 03/09/2026 | p. 1-2 : définitions (PSR, compensations, fiscalité transférée, DGD). PDF image : lu visuellement |
| `DGCL_CLC2026_Chap10_Series_longues_2026.xlsx` | `Chapitre%2010_S%C3%A9ries%20longues%20int%C3%A9grales_2026.xlsx` | Chapitre 10 – Séries longues | 06/07/2026 | Non exploité (disponible pour des séries APUL par fonction, onglet 10.3) |

## 2. DGFiP — balances comptables des collectivités et établissements publics locaux, présentation croisée nature-fonction 2025 (data.economie.gouv.fr)

- Jeu : https://data.economie.gouv.fr/explore/dataset/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/
- Mise à jour : 13/07/2026 ; 5 326 293 lignes. Type de balance « DEF » (définitive).
- Seules des **requêtes agrégées et filtrées** ont été exportées, pas le flux complet.
- Préfixe des exports : `https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/exports/csv?`

| Fichier | Requête (paramètres après le préfixe, encodés) | Contenu |
|---|---|---|
| `DGFiP_balances_nature-fonction_2025_fonction2_et_81_agrege_API.csv` | `select=categ,ctype,cstyp,cacti,cbudg,nomen,fonction,compte,sum(obnetdeb) as obnetdeb,sum(obnetcre) as obnetcre,sum(oobdeb) as oobdeb,sum(oobcre) as oobcre,count(*) as nb_lignes` & `where=(startswith(fonction,"2") or startswith(fonction,"902") or startswith(fonction,"932") or startswith(fonction,"81") or startswith(fonction,"9081") or startswith(fonction,"9381"))` & `group_by=categ,ctype,cstyp,cacti,cbudg,nomen,fonction,compte` & `delimiter=;` | Fonction 2 « Enseignement, formation professionnelle et apprentissage » et 81 « Transports scolaires », y compris les codes des budgets votés par fonction (90x en investissement, 93x en fonctionnement), agrégés par catégorie de collectivité, budget, fonction et compte (27 361 lignes) |
| `DGFiP_balances_nature-fonction_2025_communes_ecoles_fonct_par_commune_API.csv` | `select=categ,ndept,insee,siren,sum(obnetdeb)…,count(*)` & `where=(categ="Commune" or categ="PARIS") and cbudg="1" and (fonction commence par 20, 21, 28, 29, 9020, 9021, 9028, 9029, 9320, 9321, 9328, 9329) and compte commence par 6 sauf 66, 675, 676, 68` & `group_by=categ,ndept,insee,siren` | Dépenses de fonctionnement « écoles » par commune (3 340 communes) |
| `DGFiP_balances_nature-fonction_2025_communes_ecoles_invest_par_commune_API.csv` | idem, avec `compte` commençant par 20, 21 ou 23 | Dépenses d'investissement « écoles » par commune |
| `DGFiP_Notice_balance_fonctionnelle_2025.pdf` | Pièce jointe : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/attachments/notice_balance_fonctionnelle_pdf | Notice DGFiP (datée octobre 2018, jointe au jeu 2025) : périmètre (budgets ayant renseigné au moins un code fonctionnel), codes 9x des budgets votés par fonction |
| `DGFiP_Structure_fichier_balance_fonction_2024.ods` | Pièce jointe du jeu 2024 : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2024/attachments/structurebalfonctiond2024_dec2025_ods | Structure des variables (OBNETDEB inclut les opérations d'ordre ; OOBDEB ; CATEG ; CTYPE ; CACTI 03/04/23 = scolaire) ; aucune structure n'est jointe au jeu 2025 |

Les URL complètes, encodées, figurent dans la sortie du script `extractions/_script_extractions_collectivites.py`. Elles sont aussi reproductibles à partir des paramètres ci-dessus (`urllib.parse.urlencode`).

## 3. OFGL — Observatoire des finances et de la gestion publique locales

| Fichier | URL exacte | Titre | Date | Ce qui est utilisé |
|---|---|---|---|---|
| `OFGL_departements_fonctionnelle_fonction2_2022-2025.csv` | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/ofgl-base-departements-fonctionnelle/exports/csv?delimiter=%3B&where=startswith(fonction%2C%222%22)%20and%20exer%3E%3Ddate%272022%27 | Comptes des départements 2012-2025 – présentation fonctionnelle (extraction fonction 2, 2022-2025 ; 22 936 lignes) | Jeu modifié le 05/08/2026 | Agrégats OFGL (frais de personnel, achats, intervention, équipement…) des fonctions 2, 20, 22 et 221 « Collèges », 2022-2025 ; contrôle croisé avec la DGFiP |
| `OFGL_departements_fonctionnelle_metadata.json` | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/ofgl-base-departements-fonctionnelle | Métadonnées du jeu | 05/08/2026 | Définition des champs |
| `OFGL_nomenclature_M57_2025_libelles_comptes.csv` | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/nomenclatures-budgetaires/exports/csv?delimiter=%3B&where=nomenclature%3D%22M57%22%20and%20year(annee)%3D2025&select=annee,nomenclature,numero_compte,libelle_compte,chemin | Nomenclatures budgétaires 2012-2026 (M57, 2025 : 2 552 comptes) | Jeu modifié le 28/03/2024 | Libellés officiels des comptes (6558, 657364, 655111/655112, 655121/655122, 2317, 238…) |
| `OFGL_Rapport2026_Annexe2F_Ventilation_fonctionnelle_2020-2025.xlsx` | https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/pre%20rapport%202026/Annexe%202F%20-%20Ventilation%20fonctionnelle%202020-2025.xlsx | Rapport OFGL 2026, annexe 2F | 06/07/2026 | **Contenu identique, cellule par cellule, au fichier DGCL 4F** (vérifié) : même source |
| `OFGL_page_rapports_web.html` | https://www.collectivites-locales.gouv.fr/etudes-et-statistiques/rapports-de-lobservatoire-des-finances-et-de-la-gestion-publique-locales-ofgl | Page des rapports OFGL (pré-rapport du 9/6/2026, rapport 2026) | consultée le 2026-10-04 | Preuve de l'édition 2026 et des annexes |
| `OFGL_CapSur21_investissements_scolaires_2023.pdf` | https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/Les%20chantiers%20de%20l'OFGL/OFGL_cap_sur_21_investissements_scolaires_collectivites_30-10-2023.pdf | « Cap sur… n° 21 : Les investissements scolaires des collectivités locales » (oct.-nov. 2023, données 2012-2022) | Octobre 2023 | p. 3, 5 (tableau 1 et méthode d'extrapolation aux communes hors comptabilité fonctionnelle), 8 (coûts par élève), 10-12 (subventions reçues) |
| `OFGL_CapSur10_cout_enseignement_2019.pdf` | https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/Cap%20sur/ofgl_num10_cap_sur_cout_enseignement_nov19_0.pdf | « Cap sur… n° 10 : Les coûts locaux de l'éducation, enseignement et périscolaire » (novembre 2019, données 2018) | Novembre 2019 | p. 5, 7-12 : coût communal médian par élève du primaire public, structure des coûts, échantillon et méthode |

## 4. DEPP (ministère de l'Éducation nationale) — part des collectivités dans la DIE

Les md5 sont identiques aux fichiers du dossier `depp_compte_education/`, dont `SOURCES.md` documente les pages web.

| Fichier | URL exacte | Titre | Date | Ce qui est utilisé |
|---|---|---|---|---|
| `DEPP_NI_26-42_compte_education_2025.pdf` | https://www.education.gouv.fr/sites/default/files/document/educationnationaledepp-ni-2026-42pdf-520993.pdf | NI n° 26.42, « En 2025, 199,2 milliards d'euros consacrés à l'éducation, soit 6,7 % du PIB » | Septembre 2026 | p. 1-2 (CT deuxième financeur, 23 % ; 57 % communes / 16 % départements / 27 % régions) ; p. 3 (évolution 2025 des dépenses des CT) |
| `DEPP_NI_26-42_compte_education_2025_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/document/educationnationaledepp-ni-2026-42donneesxlsx-521029.xlsx | Données de la NI 26.42 | Septembre 2026 | Figure 2 (B6:C9), Figure 2bis (B6:F9), Figure 3bis (B6:F6, E10:F10), Figure 4 (B33:E33), Figure 5 (B32:B36), Figure 6 (E31, E33) |
| `DEPP_RERS2026_10-02_financement_DIE_donnees.xlsx` | https://rers.depp.education.fr/data/2026/10_BUD/02_FINDIE/dataExcel.fr.xlsx | RERS 2026, fiche 10.02 « Le financement de la DIE » (2024 provisoire) | Édition du 25/08/2026 (Last-Modified 14/09/2026) | « 10.02 Tableau 3 » (B9:C9) ; « 10.02 Tableau 4 », colonne F (CT, l. 8-20) |
| `DEPP_RERS2026_10-04_producteurs_education_donnees.xlsx` | https://rers.depp.education.fr/data/2026/10_BUD/04_PRODEDUC/dataExcel.fr.xlsx | RERS 2026, fiche 10.04 « Le financement des producteurs d'éducation » (2024p) | idem | « 10.04 Tableau 2 », colonne E (l. 9-31) ; « 10.04 Graphique 3 » (C6:C7, J6:J7) |
| `DEPP_GeoEcole2026_fiche22_depense_departements_regions_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/document/la-depense-d-education-par-eleve-ou-etudiant-prise-en-charge-par-les-ministeres-charges-de-l_0.xlsx | Géographie de l'École 2026, fiche 22 « La dépense d'éducation des départements et des régions par collégien et par lycéen » | 29/06/2026 | Onglets 22.1-22.3 cellule C113 (« France ») ; 22.4-22.6 cellule C29 ; lignes 4-6 (lecture, champ, source) |

## 5. Ministère de l'Éducation nationale — open data (data.education.gouv.fr), pour la couverture par élève

| Fichier | URL exacte | Jeu | Date du jeu | Utilisation |
|---|---|---|---|---|
| `MEN_effectifs_par_ecole_rentrees2024-2025_extrait_API.csv` | https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ecoles-effectifs-nb_classes/exports/csv?select=rentree_scolaire%2Cnumero_ecole%2Csecteur%2Ccode_departement%2Cnombre_total_eleves%2Cnombre_eleves_preelementaire_hors_ulis%2Cnombre_total_classes&where=year%28rentree_scolaire%29%3E%3D2024&delimiter=%3B | « Effectifs d'élèves par école » (fr-en-ecoles-effectifs-nb_classes) | 27/08/2026 | Élèves du public par école, rentrées 2024 et 2025 (95 273 lignes). Attention : le champ `code_commune_insee` de ce jeu est en réalité le code postal, d'où le passage par l'annuaire |
| `MEN_annuaire_education_ecoles_UAI_commune_extrait_API.csv` | https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-annuaire-education/exports/csv?select=identifiant_de_l_etablissement%2Ctype_etablissement%2Cstatut_public_prive%2Ccode_commune%2Cnom_commune%2Ccode_departement%2Cetat%2Crpi_concentre%2Crpi_disperse&where=type_etablissement%3D%22Ecole%22&delimiter=%3B | « Annuaire de l'éducation » (fr-en-annuaire-education) | 03/10/2026 | Correspondance UAI → code commune Insee (48 345 écoles ouvertes) |

## 6. Données par établissement côté collectivités (point 5)

| Fichier | URL exacte | Éditeur / titre | Date | Utilisation |
|---|---|---|---|---|
| `RegionCVL_dotations_fonctionnement_lycees_2025.csv` | https://data.centrevaldeloire.fr/api/explore/v2.1/catalog/datasets/dotations-de-fonctionnement-versees-aux-lycees-de-la-region-centre-val-de-loire-en-2025/exports/csv?use_labels=true (fiche : https://www.data.gouv.fr/datasets/dotations-de-fonctionnement-versees-aux-lycees-de-la-region-centre-val-de-loire-en-2025) | Région Centre-Val de Loire, « Dotations de fonctionnement versées aux lycées … en 2025 » (ODbL) | 27/01/2026 | Exemple : dotations par lycée et par type (UAI) ; série annuelle 2017-2025 sur data.gouv.fr |
| `RegionCVL_dotations_fonctionnement_lycees_2025_metadata.json` | https://data.centrevaldeloire.fr/api/explore/v2.1/catalog/datasets/dotations-de-fonctionnement-versees-aux-lycees-de-la-region-centre-val-de-loire-en-2025 | Métadonnées | 27/01/2026 | Licence, date |

Sources consultées mais non téléchargées (métadonnées lues via les API le 2026-10-04) :
- **Gironde, collèges.** « Montant des dotations des collèges publics de Gironde », Ressourcerie datalocale. Fiche : https://www.data.gouv.fr/datasets/montant-des-dotations-des-colleges-publics-de-gironde-1 ; ressource : https://datacat.datalocale.fr/distribution/1625121/raw/DotationsCollegeGironde-2015-2017.csv. Années 2015-2017, mise à jour 17/12/2021.
- **Académie de Normandie, masse salariale.** « Masse salariale des établissements scolaires » (coût employeur de l'État par établissement, 2016-2020) : https://data.normandie.education.gouv.fr/explore/dataset/fr-en-normandie-masse-salariale-des-etablissements-scolaires/
- **Académie de Normandie, finances des EPLE.** « Données financières des EPLE » (comptes financiers agrégés par catégorie, 2018) : https://data.normandie.education.gouv.fr/explore/dataset/fr-en-normandie-donnees-financieres-des-eple/
- **Socle numérique dans les écoles élémentaires (SNEE).** Subventions de l'État par collectivité, plan de relance 2021-2022 : https://data.education.gouv.fr/explore/dataset/fr-en-aap-snee-collectivites/ et https://data.education.gouv.fr/explore/dataset/fr-en-aap-snee-ecoles/
- **Recherches sans résultat.** Aucun jeu national de comptes financiers d'EPLE ni de dotations par collège n'a été trouvé (catalogue data.education.gouv.fr, recherches « financier », « dotation », « EPLE » ; API data.gouv.fr).

## 7. Fichiers d'autres dossiers du projet utilisés (non dupliqués)

| Fichier | Dossier | Emplacement utilisé |
|---|---|---|
| `RAP2025_Enseignement_scolaire_EC.pdf` (RAP 2025, mission Enseignement scolaire ; URL dans `budget_etat/SOURCES.md`) | `data/raw/budget_etat/` | p. 168 (P230 action 01 : subventions aux EPLE pour les AED) ; p. 170 (tableau par nature de l'action 01) ; p. 60 (P140 : transferts aux CT, service minimum d'accueil) ; p. 171 (P230 action 02 : villes à régime autonome) |
| `extractions/plrg2025_execution_titre_categorie_MIES.csv` (issu de PLRG 2025, annexe 1 « Etat_Titre_Cat », data.economie.gouv.fr) | `data/raw/budget_etat/` | Catégorie 63 « Transferts aux collectivités territoriales », exécution 2025, par programme |
| `NOTES.md` § 6 (PLRG 2025, état des recettes : DRES, DDEC, DGCES, logement des instituteurs, exécution 2025 ; PAP 2027 RCT p. 36-37 : DGD « instruction obligatoire à 3 ans ») | `data/raw/budget_etat/` | Montants exécutés 2025 des prélèvements sur recettes |
| `depp_dossier206_2016_compte_education_methodologie.pdf` (DEPP, Les dossiers n° 206, avril 2016) | `data/raw/depp_compte_education/` | p. 17 (garderie et étude dans l'enseignement), p. 18 (traitement des transferts, DRES/DDEC, DGD), p. 20 (financeur « Communes » = communes, groupements, syndicats, caisses des écoles), p. 33-36 (sources ; administration générale ; cantines nettes des familles) |
| `depp_geographie_de_l_ecole_2026.pdf` (DEPP, juin 2026) | `data/raw/depp_compte_education/` | PDF p. 54 (= p. 52 imprimée, fiche 22 : 14,5 Md€ en 2023, transports scolaires) ; PDF p. 108 (méthodologie des fiches 21-22) |
| `NOTES.md` § 3 et § 7 (NI 25.59, effectifs du 2nd degré aux rentrées 2024-2025 ; effectifs pondérés en année civile) | `data/raw/effectifs_nationaux/` | Dénominateurs collégiens et lycéens (calculs dérivés) |

## 8. Extractions dérivées (calculs, pas des sources)

Dossier `extractions/`. Elles sont produites par `extractions/_script_extractions_collectivites.py` (Python 3.11, pandas, openpyxl), qui ne lit que les fichiers bruts ci-dessus.
- `DGCL_4F_enseignement_transport_2024_2025.csv` : lignes enseignement et transport scolaire de 4F, avec les cellules sources.
- `DGFiP_2025_enseignement_niveau_sousfonction_nature.csv` : niveau × budget × sous-fonction × nature, en M€.
- `DGFiP_2025_enseignement_synthese_niveau_perimetre_BP.csv` : budgets principaux, périmètres écoles / collèges / lycées / transport / hors scolaire.
- `DGFiP_2025_enseignement_postes_cles_budgets_principaux.csv` : personnel, énergie, restauration, entretien, dotations aux EPLE, constructions, etc.
- `DGFiP_2025_enseignement_recettes_par_niveau_BP.csv` : participations des familles, subventions de l'État et des autres CT, avec libellés M57.
- `DGFiP_MEN_2025_communes_couverture_et_depense_par_eleve.csv` : part des élèves du public couverts par la comptabilité fonctionnelle, dépense par élève, extrapolation.
- `DEPP_collectivites_parts_montants_par_niveau.csv` : parts et montants des CT par niveau (publiés et dérivés), avec les cellules sources.

## 9. Ajouts de la tâche G3 (2026-10-04) : écart DGFiP / DEPP pour les communes

Tous les fichiers ont été consultés ou téléchargés le **2026-10-04**, avec `curl` (en-têtes de navigateur) ou l'API Opendatasoft. Leur type a été vérifié (`%PDF`, CSV UTF-8, en-tête `D0CF11E0` pour le xls). Les fichiers temporaires `_tmp_*` de cette exécution ont été supprimés.

### 9.1 Documents

| Fichier | URL exacte | Éditeur / titre | Date | Ce qui est utilisé |
|---|---|---|---|---|
| `OFGL_Rapport2026_complet_V24aout2026.pdf` | https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/2026/Rapport%20OFGL%202026%20complet%20V24ao%C3%BBt2026.pdf | OFGL, *Les finances des collectivités locales en 2026*, rapport complet (289 p.) | Last-Modified 25/08/2026 | Annexe 7A, p. 211 (caisses des écoles 2025 : 772 ; dépenses totales 631 ; dotations et participations 434 ; ventes 148). Annexe 8, tableau 6, p. 220 (redevances « périscolaire » 2025 : communes 2 161, syndicats 149, GFP 202, ensemble 2 530). Dossier « bilan du mandat » (PDF p. 80-96) |
| `OFGL_dossier_2026_Bilan_mandat_communal_intercommunal_2020-2025_juillet2026.pdf` | https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/rapport%202026/dossier%202026%20Bilan%20de%20mandat_VF%20juillet%202026.pdf | OFGL / DGCL, *Dossier : bilan du mandat communal et intercommunal 2020-2025* (28 p.) | Last-Modified 27/07/2026 | p. 13 (recettes tarifaires du périscolaire). Aucune estimation de la dépense scolaire |
| `DEPP_NI_19-07_depense_education_CT_2017.pdf` | https://www.education.gouv.fr/sites/default/files/document/T%C3%A9l%C3%A9charger%20la%20version%20imprimable%20au%20format%20PDF-246936.pdf (page : https://www.education.gouv.fr/depp/la-depense-d-education-des-collectivites-territoriales-362-milliards-d-euros-en-2017-11945) | DEPP, NI n° 19.07, « La dépense d'éducation des collectivités territoriales : 36,2 milliards d'euros en 2017 » | Mars 2019 | p. 3, figure 4 (communes 2017 : écoles 12 197,5 M€ ; hébergement-restauration 3 211,6 ; total 18 680,2) |
| `DEPP_NI_19-07_depense_education_CT_2017_donnees.xls` | https://www.education.gouv.fr/sites/default/files/document/T%C3%A9l%C3%A9charger%20les%20donn%C3%A9es%20au%20format%20XLS-246939.xls | Données de la NI 19.07 | Last-Modified 04/02/2020 | Onglet « Figure 4 ». Onglet « Définitions et méthodologie » : texte en zone de dessin, lu dans le flux binaire (financeur final ; comptes définitifs ; compte provisoire estimé par les budgets primitifs ou des indices de prix) |
| `AN_rapport_information_2423_financement_prive_sous_contrat_2024.pdf` | https://www.assemblee-nationale.fr/dyn/16/rapports/cion-cedu/l16b2423_rapport-information.pdf | Assemblée nationale, commission des affaires culturelles, rapport d'information n° 2423 (P. Vannier, C. Weissberg), « financement public de l'enseignement privé sous contrat » | 02/04/2024 | p. 7 et 43 (DEPP : 1,9 Md€ des CT vers le privé en 2022 ; absence de données consolidées) ; p. 25 (circulaire 2012-025 : quote-part des services généraux) ; p. 45 (proposition n° 7 sur la nomenclature des CT) |
| `INSEE_COG2026_v_commune_2026.csv`, `INSEE_COG2026_v_commune_depuis_1943.csv`, `INSEE_COG2026_page_web.html` | https://www.insee.fr/fr/statistiques/fichier/8740222/v_commune_2026.csv ; https://www.insee.fr/fr/statistiques/fichier/8740222/v_commune_depuis_1943.csv (page : https://www.insee.fr/fr/information/8740222) | Insee, Code officiel géographique au 1er janvier 2026 | 2026 | Appariement des écoles fermées par libellé de commune (communes, communes déléguées et associées → commune parente) |

### 9.2 Extractions par API

**Éducation nationale (data.education.gouv.fr).** `MEN_effectifs_par_ecole_rentrees2024-2025_libelles_communes_API.csv` :
- URL : https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ecoles-effectifs-nb_classes/exports/csv?select=rentree_scolaire%2Cnumero_ecole%2Csecteur%2Ccode_departement%2Ccode_commune_insee%2Ccommune%2Cdenomination_principale%2Cpatronyme%2Cnombre_total_eleves&where=year%28rentree_scolaire%29%3E%3D2024&delimiter=%3B ;
- jeu « Effectifs d'élèves par école », modifié le 27/08/2026 ;
- 95 273 lignes, mêmes lignes que l'extrait précédent, avec en plus le libellé de commune et le code postal (champ `code_commune_insee`).

**OFGL (data.ofgl.fr).** `OFGL_base_communes_2025_BP_population_EPCI_depenses_API.csv` :
- URL : https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/ofgl-base-communes/exports/csv?select=exer%2Ccateg%2Ccom_code%2Ccom_name%2Cinsee%2Csiren%2Cdep_code%2Cptot%2Ctranche_population%2Crural%2Cepci_code%2Cepci_name%2Cagregat%2Cmontant&where=year%28exer%29%3D2025+and+type_de_budget%3D%22Budget+principal%22+and+agregat+in+%28%22D%C3%A9penses+totales+hors+remb%22%2C%22D%C3%A9penses+de+fonctionnement%22%2C%22D%C3%A9penses+d%27investissement+hors+remb%22%2C%22Charges+financi%C3%A8res%22%2C%22Frais+de+personnel%22%29&delimiter=%3B ;
- jeu « Comptes des communes 2018-2025 », modifié le 29/07/2026 ;
- 173 890 lignes, 34 778 communes ;
- utilisé pour la population (`ptot`), l'EPCI de rattachement et la dépense totale du budget principal.

**DGFiP (data.economie.gouv.fr).** Balance nature-fonction 2025 (DEF, mise à jour le 13/07/2026), même préfixe d'export qu'au § 2. Requêtes agrégées et filtrées :

| Fichier | Paramètres (avant encodage) | Contenu |
|---|---|---|
| `DGFiP_balances_nature-fonction_2025_communes_BP_toutes_fonctions_agrege_API.csv` | `select=categ,fonction,compte,sum(obnetdeb),sum(obnetcre),sum(oobdeb),sum(oobcre),count(*)` ; `where=(categ="Commune" or categ="PARIS") and cbudg="1" and (compte commence par 6, 20, 21 ou 23)` ; `group_by=categ,fonction,compte` | Communes, BP, toutes fonctions (39 858 lignes). Sert au ratio et à l'administration générale |
| `DGFiP_balances_nature-fonction_2025_communes_BP_total_toutes_fonctions_fonct_par_commune_API.csv` | même `select` avec `ndept,insee,siren` ; `where=` communes, BP, compte 6 sauf 66, 675, 676, 68 ; `group_by=categ,ndept,insee,siren` | Fonctionnement total par commune (3 395 communes de la balance fonctionnelle) |
| `DGFiP_balances_nature-fonction_2025_communes_BP_total_toutes_fonctions_invest_par_commune_API.csv` | idem avec compte 20, 21 ou 23, sauf 204 | Investissement total par commune |
| `DGFiP_balances_nature-fonction_2025_GFP_ecoles_par_GFP_et_compte_API.csv` | `where=(categ="GFP" or "ML" or "EPT") and cbudg="1"` ; fonctions 20, 21, 28, 29 (et 90x, 93x) ; compte 6, 20, 21 ou 23 ; `group_by=categ,ndept,insee,siren,lbudg,compte` | Dépense « écoles » par GFP (13 451 lignes, 635 GFP) |

### 9.3 Fichiers d'autres dossiers utilisés (non dupliqués)

| Fichier | Dossier | Emplacement utilisé |
|---|---|---|
| `CdC_RPT_Enseignement_primaire_mai2025.pdf` (https://www.ccomptes.fr/sites/default/files/2025-05/20250520-Enseignement-primaire.pdf, 20/05/2025) | `recoupements/` | **p. 31-32** (méthode DEPP des petites communes : bloc homogène, ratio des communes de 3 500-10 000 hab. établi en 2010, 31 % des élèves, 4,2 Md€) ; p. 29 (CT : 19 Md€ pour le 1er degré en 2022 ; note 11 : 20,6 en 2023) ; p. 44 (de 250 à 4 500 € par élève selon les communes) |
| `CdC_RPT_Enseignement_prive_sous_contrat_juin2023.pdf` (URL dans `recoupements/SOURCES.md`) | `recoupements/` | p. 22 (loi Goblet : aucune aide communale aux écoles privées hors forfait communal) |
| `depp_dossier206_2016_compte_education_methodologie.pdf` | `depp_compte_education/` | PDF p. 17, 20, 21, 25, 32, 33 et 36 (voir NOTES § 8.1) |
| `depp_ni_2025-52_compte_education_2024_donnees.xlsx` | `depp_compte_education/` | Figure 4 B33 (38,33 %) et Figure 5 B31 (58,52 Md€) : CT 1er degré 2024p |
| `ips_ecoles_2024-2025.csv` (API `fr-en-ips-ecoles-ap2022`, voir `etablissements/SOURCES.md`) | `etablissements/` | UAI → code Insee de la commune, pour 256 écoles fermées depuis |

### 9.4 Consultés, non conservés

- **NI 24.45** (« En 2023, 189,9 milliards d'euros consacrés à l'éducation… », novembre 2024) :
  - la page education.gouv.fr renvoie 404 ;
  - le DOI https://doi.org/10.48464/ni-24-45 renvoie vers HAL (halshs-04793427), protégé par captcha ;
  - une copie du PDF (base documentaire du Céreq, pmb.cereq.fr, explnum_id=11297) a été lue pour vérification : elle ne contient pas d'encadré méthodologique (« voir définitions et méthodologie en ligne »).
- **DEPP, Document de travail n° 2024-E08** (« Le financement de l'éducation en 2023 », septembre 2024 ; https://www.education.gouv.fr/media/196890/download → DT2024-E08-403287.pdf) : il ne décrit pas la méthode des communes.
- **NI 17.32 et NI 18.01** (copies du Céreq, explnum_id=4145 et 4259) : leurs encadrés « Définitions et méthodologie » reprennent le texte de la NI 19.07.

### 9.5 Extractions dérivées G3 (`extractions/`, produites par `_script_G3_ecart_DGFiP_DEPP.py`)

- `G3_appariement_ecoles_communes.csv` : élèves et UAI par méthode d'appariement.
- `G3_couverture_extrapolation_communes_2025_horsCOM.csv` : effectifs, couverture, méthodes d'extrapolation, GFP, administration générale, repères DEPP (blocs A à F).
- `G3_extrapolation_par_classe_taille.csv` ; `G3_eleves_par_strate_et_couverture.csv`.
- `G3_GFP_ecoles_par_GFP_part_non_couverte.csv` : 635 GFP, dépense, élèves couverts et non couverts.
- `G3_quote_part_administration_generale_2025.csv` : 3 variantes.
- `G3_tableau_passage_DGFiP_DEPP_2025.csv` : tableau de passage (étapes A0 à R5).
