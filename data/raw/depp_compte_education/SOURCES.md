# SOURCES — Axe A : Compte de l'éducation (DEPP)

Dossier : `data/raw/depp_compte_education/`
Tous les fichiers ont été téléchargés le **2026-10-04** (date de consultation), avec `curl` et des en-têtes de navigateur. Ils n'ont pas été modifiés. Le format a été contrôlé pour chacun (en-tête `%PDF` ou `PK` pour les xlsx).
Éditeur commun, sauf mention contraire : ministère de l'Éducation nationale, Direction de l'évaluation, de la prospective et de la performance (**DEPP**). Le SIES est coéditeur des RERS.

## 1. Publication la plus récente sur le compte de l'éducation (données 2025 provisoires, 2024 définitives)

| Fichier | URL exacte | Titre / référence | Date de publication | Ce qui est utilisé |
|---|---|---|---|---|
| `depp_ni_2026-42_compte_education_2025.pdf` | https://www.education.gouv.fr/sites/default/files/document/educationnationaledepp-ni-2026-42pdf-520993.pdf | Bagot L., Dutey C., de Fornel C., Liogier V., Rousseau S., « En 2025, 199,2 milliards d'euros consacrés à l'éducation, soit 6,7 % du PIB », *Note d'Information* n° 26.42, DEPP, https://doi.org/10.48464/ni-26-42 | Septembre 2026 (page web datée du 29/09/2026) | Texte des p. 1 à 4 ; figures 1 à 7 (DIE, financeurs, dépense par élève, comparaison OCDE) |
| `depp_ni_2026-42_compte_education_2025_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/document/educationnationaledepp-ni-2026-42donneesxlsx-521029.xlsx | Données de la NI 26.42 | Septembre 2026 | Onglets Figure 1 (série DIE et DIE/PIB 1980-2025p), Figure 1bis (révisions 2021-2024), Figure 2 et 2bis (structure en financement initial et final), Figure 3 et 3bis (montants par financeur), Figure 4 (financeurs par niveau), Figure 5 (DIE par niveau en Md€), Figure 6 (dépense par élève par niveau), Figure 7 (série 1980-2025p en euros constants 2025), Figure 7bis (DIE, effectifs et dépense moyenne, base 100 en 2015), Figure 8bis 1-4 (OCDE), « Définitions et méthodologie » (texte dans une zone de texte, fichier `xl/drawings/drawing20.xml`) |

## 2. Édition précédente de la Note d'Information (2024 provisoire, 2023 définitif)

| Fichier | URL exacte | Titre / référence | Date | Utilisation |
|---|---|---|---|---|
| `depp_ni_2025-52_compte_education_2024.pdf` | https://www.education.gouv.fr/sites/default/files/2025-09/depp-ni-2025-52-442155.pdf (lien de la page : https://www.education.gouv.fr/media/229440/download) | « En 2024, 197,1 milliards d'euros consacrés à l'éducation, soit 6,8 % du PIB », *Note d'Information* n° 25.52, DEPP | Septembre 2025 (page datée du 23/09/2025) | Valeurs 2024 provisoires (édition précédente) |
| `depp_ni_2025-52_compte_education_2024_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/2025-09/depp-ni-2025-52-donn-es-442158.xlsx (lien de la page : https://www.education.gouv.fr/media/229443/download) | Données de la NI 25.52 | Septembre 2025 | Onglets Figure 4 (financeurs par niveau 2024p), Figure 5 (DIE par niveau 2024p), Figure 6, Figure 7bis (base 100 en 2014) |

## 3. Repères et références statistiques (RERS) 2026 — chapitre 10 « Budgets, coûts et financements » (données 2024 provisoires)

Page de l'édition : https://www.education.gouv.fr/depp/reperes-et-references-statistiques-2026-505320 (datée du 25/08/2026). Les tableaux Excel sont diffusés par « RERS interactif » (https://rers.depp.education.fr), pas sur la page education.gouv.fr.

| Fichier | URL exacte | Contenu | Utilisation |
|---|---|---|---|
| `depp_rers2026_chap10_budget_couts_financement.pdf` | https://www.education.gouv.fr/sites/default/files/document/10-budget-couts-et-financementpdf-519303.pdf | RERS 2026, chapitre 10, pp. 407-425 | Fiches 10.01 à 10.05 (pp. 408-417). En particulier : p. 411 (tableau « Le financement des activités d'éducation en 2024 »), p. 415 (graphique 4 sur la nature des dépenses), p. 417 (tableau des dépenses par élève) |
| `depp_rers2026_10-01_DIE_donnees.xlsx` | https://rers.depp.education.fr/data/2026/10_BUD/01_DIE/dataExcel.fr.xlsx | Fiche 10.01 La dépense intérieure d'éducation | Onglets « 10.01 Graphique 1 », « Tableau 2 », « Graphique 3 » (DIE par niveau, Md€ aux prix 2024), « Tableau 4 » (structure par niveau) |
| `depp_rers2026_10-02_financement_DIE_donnees.xlsx` | https://rers.depp.education.fr/data/2026/10_BUD/02_FINDIE/dataExcel.fr.xlsx | Fiche 10.02 Le financement de la DIE | « Graphique 1 » (série par financeur final), « Graphique 2 », « Tableau 3 » (financement initial et final 2024), « Tableau 4 » (financement des activités 2024, M€) |
| `depp_rers2026_10-03_budget_donnees.xlsx` | https://rers.depp.education.fr/data/2026/10_BUD/03_BUDEVO/dataExcel.fr.xlsx | Fiche 10.03 Le budget (MIES, Mires) | « Tableau 2 » et « Tableau 3 » (crédits exécutés 2023-2025 et LFI 2026 par programme) |
| `depp_rers2026_10-04_producteurs_education_donnees.xlsx` | https://rers.depp.education.fr/data/2026/10_BUD/04_PRODEDUC/dataExcel.fr.xlsx | Fiche 10.04 Le financement des producteurs d'éducation | « Tableau 2 » (financement par type d'établissement 2024, M€), « Graphique 3 » (origine des fonds public / privé sous contrat), « Graphique 4 » (nature des dépenses) |
| `depp_rers2026_10-05_depense_par_eleve_donnees.xlsx` | https://rers.depp.education.fr/data/2026/10_BUD/05_DEPEL/dataExcel.fr.xlsx | Fiche 10.05 Les dépenses par élève et par étudiant | « Graphique 1 » (série 1980-2024p, prix 2024), « Tableau 2 » (par sous-niveau), « Graphique 3 », « Graphique 4 » (structure par activité) |
| `depp_rers2026_chap01_systeme_educatif.pdf` | https://www.education.gouv.fr/sites/default/files/document/1-le-systeme-educatifpdf-519276.pdf | RERS 2026, chapitre 1 | Fiche 1.02, tableau 2, p. 15 : effectifs aux rentrées 2024 et 2025, utilisés pour contrôler les dénominateurs |
| `depp_rers2026_chap03_eleves_premier_degre.pdf` | https://www.education.gouv.fr/sites/default/files/document/3-les-eleves-du-premier-degrepdf-519282.pdf | RERS 2026, chapitre 3 | Téléchargé pour d'éventuels contrôles d'effectifs ; non exploité ici |
| `depp_rers2026_chap04_eleves_second_degre.pdf` | https://www.education.gouv.fr/sites/default/files/document/4-les-eleves-du-second-degrepdf-521305.pdf | RERS 2026, chapitre 4 | Téléchargé pour d'éventuels contrôles d'effectifs ; non exploité ici |

## 4. RERS 2025 (édition précédente : données 2023 provisoires)

| Fichier | URL exacte | Utilisation |
|---|---|---|
| `depp_rers2025_10-05_depense_par_eleve_donnees.xlsx` | https://rers.depp.education.fr/data/2025/10_BUD/05_DEPEL/dataExcel.fr.xlsx | Onglet « 10.05 Tableau 2 » (dépense par élève 2023p, prix 2023) et « Graphique 4 » ; notice actualisée le 29 août 2025 |
| `depp_rers2025_10-04_producteurs_education_donnees.xlsx` | https://rers.depp.education.fr/data/2025/10_BUD/04_PRODEDUC/dataExcel.fr.xlsx | Onglet « 10.04 Graphique 4 » (nature des dépenses 2023) |

## 5. L'état de l'École 2025 (dernière édition publiée ; données 2024 provisoires)

Page : https://www.education.gouv.fr/depp/l-etat-de-l-ecole-2025-468872 (datée du 14/11/2025). D'après la bibliographie de la NI 26.42, l'édition 2026 est « à paraître ».

| Fichier | URL exacte | Utilisation |
|---|---|---|
| `depp_etat_de_l_ecole_2025.pdf` | https://www.education.gouv.fr/sites/default/files/document/l-tat-de-l-cole-2025-478952.pdf | Fiche 9 « La dépense pour l'éducation » (pp. 30-31 imprimées, pp. 32-33 du PDF), fiche 10 « La dépense moyenne par élève ou étudiant » (pp. 32-33 imprimées, pp. 34-35 du PDF), méthodologie (pp. 97-98 imprimées, pp. 99-100 du PDF) |
| `depp_ede2025_fiche09_depense_pour_education_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/document/474631.xlsx | Figures 9.1 à 9.6web |
| `depp_ede2025_fiche10_depense_moyenne_par_eleve_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/document/474634.xlsx | Figures 10.1 (dépense par élève en euros courants 2018-2024p) à 10.5web |

## 6. Autres publications DEPP utilisées

| Fichier | URL exacte | Titre | Date | Utilisation |
|---|---|---|---|---|
| `depp_education_nationale_en_chiffres_2026.pdf` | https://www.education.gouv.fr/sites/default/files/document/enc-2026pdf-519886.pdf | *L'Éducation nationale en chiffres 2026* | Page datée du 25/08/2026 | p. 3 « Le financement de l'éducation » (2024p ; « Salaires, charges et pensions 72,0 % », 10 350 € par élève des 1er et 2nd degrés) |
| `depp_geographie_de_l_ecole_2026.pdf` | https://www.education.gouv.fr/sites/default/files/document/g-ographie-de-l-cole-2026-519114.pdf | *Géographie de l'École 2026* | Page datée du 30/06/2026 (dépôt légal juin 2026) | Fiche 21 (pp. 50-51 imprimées) : dépense du MEN par élève en 2023 ; fiche 22 (pp. 52-53) : départements et régions par collégien et par lycéen ; méthodologie pp. 106-107 |
| `depp_geo_ecole2026_depense_par_eleve_MEN-MESRE_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/document/la-depense-d-education-par-eleve-ou-etudiant-prise-en-charge-par-les-ministeres-charges-de-l.xlsx | Données de la fiche 21 | Juin 2026 | Onglets 21.1 à 21.4 (par région, ligne « France ») |
| `depp_geo_ecole2026_depense_departements_regions_par_collegien_lyceen_donnees.xlsx` | https://www.education.gouv.fr/sites/default/files/document/la-depense-d-education-par-eleve-ou-etudiant-prise-en-charge-par-les-ministeres-charges-de-l_0.xlsx | Données de la fiche 22 | Juin 2026 | Onglets 22.1 à 22.6 (par département ou région, ligne « France ») |
| `depp_dossier206_2016_compte_education_methodologie.pdf` | https://www.education.gouv.fr/sites/default/files/document/DEPP-dossier-2016-206_567592(1).pdf-270180.pdf | « Le Compte de l'éducation. Principes, méthodes et résultats pour les années 2006 à 2014 », *Les dossiers de la DEPP* n° 206 | Avril 2016 | Méthodologie : niveaux et producteurs (pp. 11-15), nature des dépenses et CAS Pensions (p. 25), effectifs en année civile (p. 35) |

## 7. Pages web sauvegardées (preuve des dates de publication)

`pages_web/page_ni_2026-42.html`, `page_ni_2025-52.html`, `page_rers2026.html`, `page_etat_de_l_ecole_2025.html`, `page_enc2026.html`, `page_geographie_de_l_ecole.html` sont des copies brutes des pages education.gouv.fr correspondantes, consultées le 2026-10-04.

## 8. Séries chronologiques DEPP « Les coûts et les financements » (ajout du 2026-10-04, tâche complémentaire G2)

Page source : « Séries chronologiques de données statistiques sur le système éducatif », DEPP, https://www.education.gouv.fr/depp/series-chronologiques-de-donnees-statistiques-sur-le-systeme-educatif-12530. La page affiche la date du 01/03/2026 ; les 4 fichiers de la rubrique « Les coûts et les financements » y sont signalés « actualisé(e) en septembre 2025 ». Page consultée le 2026-10-04.
Éditeur : ministère de l'Éducation nationale, DEPP. Téléchargement par `curl` avec en-têtes de navigateur, le 2026-10-04. Fichiers non modifiés.
Contrôles : signature `PK` (504b0304), archive zip intègre (`testzip`). Les 4 fichiers de coûts sont **identiques octet pour octet** (même SHA-256) aux copies de contrôle `scratchpad/critique/sc_*.xlsx`. Dans les propriétés Office, la date de modification est le 18/09/2025.

| Fichier | URL exacte | Titre | Date / taille / SHA-256 (début) | Ce qui est utilisé |
|---|---|---|---|---|
| `depp_series_chrono_die_financeur_initial_final_par_niveau_366603.xlsx` | https://www.education.gouv.fr/sites/default/files/document/la-d-pense-int-rieure-d-ducation-par-financeur-initial-et-final-selon-le-niveau-d-enseignement-366603.xlsx | La dépense intérieure d'éducation (DIE), sa structure par financeur initial et final, selon le niveau d'enseignement | Actualisation septembre 2025 ; 69 266 octets ; 9583f5fe… | Onglets « DIE 1er degré » et « DIE 2nd degré » : ligne 10 (DIE en Md€ 2024), lignes 16-21 (financeur initial), lignes 28-33 (financeur final), colonnes R à U (2021 à 2024p). Onglet « DIE totale » : lignes 10, 16-21 et 29-34, colonnes AR à AU. Texte de présentation dans `xl/drawings/drawing1.xml` |
| `depp_series_chrono_structure_die_par_niveau_366606.xlsx` | https://www.education.gouv.fr/sites/default/files/document/la-structure-de-la-d-pense-int-rieure-d-ducation-par-niveau-d-enseignement-366606.xlsx | La structure de la dépense intérieure d'éducation (DIE) par niveau d'enseignement | Actualisation septembre 2025 ; 48 225 octets ; 8db921f3… | Onglet « Structure DIE par niveau fin » : ligne 10 (DIE), lignes 13-25 (parts), colonnes R à U ; en particulier la ligne 19 « Apprentissage du second degré » |
| `depp_series_chrono_depense_par_eleve_par_niveau_481445.xlsx` | https://www.education.gouv.fr/sites/default/files/document/la-d-pense-d-ducation-par-l-ve-ou-tudiant-par-niveau-d-enseignement-481445.xlsx | La dépense d'éducation par élève ou étudiant par niveau d'enseignement | Actualisation septembre 2025 ; 46 344 octets ; 7f2492b1… | Onglet « Dépense par élève, niveau » : lignes 10, 13-15, 18-22 (dont ligne 22 « dont Apprentissage* » du 2nd degré), 26 et 30, colonnes AR à AU |
| `depp_series_chrono_die_par_niveau_part_pib_508145.xlsx` | https://www.education.gouv.fr/sites/default/files/document/La%20d%C3%A9pense%20int%C3%A9rieure%20d%26%23039%3B%C3%A9ducation%20%28DIE%29%20par%20niveau%20d%26%23039%3Benseignement%20et%20sa%20part%20dans%20le%20PIB-508145.xlsx | La dépense intérieure d'éducation (DIE) par niveau d'enseignement et sa part dans le PIB | Actualisation septembre 2025 ; 45 875 octets ; fe67007a… | Onglet « Part DIE dans PIB par niveau » (le nom se termine par une espace) : ligne 10 (DIE en Md€ 2024, pleine précision), ligne 11 (DIE/PIB), lignes 15-18 (DIE du niveau / PIB), colonnes AR à AU |
| `depp_series_chrono_apprentis_cfa_par_niveau_310608.xlsx` | https://www.education.gouv.fr/sites/default/files/document/les-effectifs-dans-les-centres-de-formations-d-apprentis-par-niveau-et-dipl-me-selon-le-sexe-310608_0.xlsx | Les effectifs dans les centres de formations d'apprentis par niveau et diplôme selon le sexe (source DEPP-SIFA, situation au 31/12) | Actualisation octobre 2025 (modifié le 31/10/2025) ; 57 074 octets ; 4d5bf3cb… | Onglet « Ensemble » : ligne 11 (total niveau 3), ligne 15 (total niveau 4), ligne 24 (tous niveaux), colonnes AB à AF (31/12/2020 à 31/12/2024). Sert uniquement au rapprochement avec les apprentis implicites |
| `pages_web/page_series_chronologiques_12530.html` | https://www.education.gouv.fr/depp/series-chronologiques-de-donnees-statistiques-sur-le-systeme-educatif-12530 | Copie brute de la page | Consultée le 2026-10-04 | Preuve des liens et des mentions « actualisé(e) en septembre 2025 » |

Autres entrées mobilisées pour les calculs G2 (fichiers déjà présents, non re-téléchargés) :
- `depp_rers2026_10-04_producteurs_education_donnees.xlsx`, onglet « 10.04 Tableau 2 », lignes 11, 21 et 27 (« Centre(s) de formation d'apprentis » publics, privés subventionnés et non subventionnés), colonnes D à I : financement final des CFA en 2024, en M€.
- `depp_ni_2026-42_compte_education_2025_donnees.xlsx` : Figure 1bis (DIE 2021-2024 en euros courants et constants, révisions), Figure 4 (B32:C36), Figure 5 (B32:B33), Figure 6 (E31, E33), Figure 7 (ligne 81).
- `../effectifs_nationaux/rers2026_ch06_apprentis.pdf` (RERS 2026, chapitre 6, https://www.education.gouv.fr/sites/default/files/document/6-les-apprentispdf-519291.pdf), fiche 6.09, tableau 2, p. 235 imprimée (page 19 du PDF) : apprentis au 31/12/2025, niveau 3 = 219 666 et niveau 4 = 172 271 ; au 31/12/2024, 221 549 et 170 486.

Fichiers **dérivés** (préfixe `_derive_`, ce ne sont pas des fichiers bruts) :
- `_derive_script_series_chrono.py` : script d'extraction et de calcul. Il contrôle chaque libellé de ligne avant lecture.
- `_derive_series_chrono_extraction_2021_2024.csv` : 295 valeurs publiées, chacune avec son fichier, son onglet et sa cellule.
- `_derive_series_chrono_calculs_2021_2025p.csv` : 191 calculs dérivés, chacun avec sa formule et ses hypothèses.

## 9. Financement de l'apprentissage par financeur et par niveau (ajout du 2026-10-04, tâche complémentaire G4)

Objet : encadrer la part publique (État + CT + autres APU) de « l'apprentissage du second degré » du compte de l'éducation, pour retirer les apprentis du calcul de l'approche A. Tous les fichiers ont été consultés et téléchargés le **2026-10-04** (`curl` avec en-têtes de navigateur), puis contrôlés (en-tête `%PDF`, HTML lisible ou CSV SDMX). Ils ne sont pas modifiés.

| Fichier | URL exacte | Éditeur | Titre | Date de publication | Ce qui est utilisé |
|---|---|---|---|---|---|
| `francecompetences_RUF2025_apprentissage.pdf` | https://www.francecompetences.fr/app/uploads/2026/02/RUF25_Apprentissage.pdf | France compétences (EPA, opérateur de l'État) | Rapport sur l'usage des fonds de la formation professionnelle (RUF), édition 2025 (fonds engagés en 2024), fiche « L'apprentissage », 16 p. | Février 2026 (dossier `/uploads/2026/02/` ; communiqué créé le 25/02/2026) | p. 3, note 4 (dotation aux régions : 318 M€ par an de 2020 à 2023, 268 M€ en 2024) ; p. 5, figure 2 (15 594 M€ engagés pour 896 000 contrats en 2024) ; p. 6, figure 3 (origine des fonds 2024 : France compétences 58,5 %, État 36,7 %, entreprises 2,5 %, bénéficiaires 0,5 %, Agefiph 0,1 %, régions 1,8 %, vérifiée sur l'image de la page) ; p. 7, figure 4 (coûts pédagogiques OPCO 8 176 M€, soit 9 125 € par contrat) ; p. 9 (coût unitaire de 17 404 €) ; p. 11, figure 7 (39,5 % des entrants 2024 visent le niveau bac ou infra) |
| `francecompetences_RUF2025_rapport.pdf` | https://www.francecompetences.fr/app/uploads/2026/02/RUF25_VF.pdf | France compétences | RUF édition 2025, rapport complet (81 pages PDF en vis-à-vis) | Février 2026 | Fiche « Le coût de revient de l'apprentissage » : PDF p. 19 (pp. 36-37 imprimées), figure 1 (charges des OFA 9 088 M€, produits 9 557 M€ en 2024) et figure 2 (coût de revient de 8 825 € par apprenti) ; PDF p. 21 (pp. 40-41), figure 5 (coût de revient 2024 par niveau : N3 7 590 €, N4 8 640 €, N5 8 620 €, N6 8 348 €, N7 9 439 €) ; PDF p. 22, figure 8 (taux de marge de 5,1 %) |
| `francecompetences_RUF2025_annexes.pdf` | https://www.francecompetences.fr/app/uploads/2026/02/RUF25_Annexes.pdf | France compétences | RUF 2025, annexes (sources, méthodes, glossaire) | Février 2026 | Description des sources (comptabilité analytique des OFA, suivi conventionnel des subventions régionales). Aucun chiffre repris |
| `francecompetences_RUF2025_panorama.pdf` | https://www.francecompetences.fr/app/uploads/2026/02/RUF25_Panorama.pdf | France compétences | Panorama de l'usage des fonds sur l'année 2024 | Février 2026 | Contexte seulement (21,61 Md€ engagés en 2024, dont 59 % par France compétences et 27 % par l'État) |
| `francecompetences_RUF2025_communique_presse.pdf` | https://www.francecompetences.fr/app/uploads/2026/02/CP_Publication-RUF-2025-1.pdf | France compétences | Communiqué de presse de publication du RUF 2025 | PDF créé le 25/02/2026 | Preuve de la date de publication |
| `jaune_PLF2026_formation_professionnelle_AN.pdf` | https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1089989/file/7-Jaune2026_Formation_Professionnelle.pdf | Gouvernement (DGEFP, Dares, DGAFP, France compétences…), annexe au PLF déposée à l'Assemblée nationale | Annexe au projet de loi de finances pour 2026 « Formation professionnelle » (« jaune »), 301 p. | PDF créé le 21/10/2025 | Partie 2 (Dares : dépense nationale par financeur final, 2024p) : tableau 1 (PDF p. 32) ; tableau 2 (p. 33 : apprentissage 16 035 M€) ; **tableau 3 (p. 35 : apprentis, OPCO 8,71 Md€, État 6,33, régions 0,25, autres CT 0,15, autres organismes de service public 0,22, ménages 0,37 ; total 16,03 Md€)** ; tableau 5 (p. 39 : régions, apprentissage 252 M€, constitués « exclusivement » de subventions aux CFA, p. 40) ; tableau 6 (p. 42 : État, apprentissage 6 332 M€ dont aides aux employeurs 3 908 M€) ; tableau 7 (p. 43 : 222 M€) ; tableau B (p. 48 : transferts). Budget de France compétences (p. 65-66) : ressources 2024 de 13 067 M€, dont contributions des entreprises 10 798 M€ et dotation de l'État 1 350 M€ ; emplois : régions 180 M€ (investissement) et 88 M€ (fonctionnement des CFA), CNFPT 10 M€, OPCO 3 600 + 5 445 M€ |
| `igas_igf_2024-03_revue_depenses_publiques_apprentissage_formation_professionnelle.pdf` | https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas%20-IGF%20Apprentissage-Formation%20(revue%20de%20d%C3%A9penses).pdf | Inspection générale des finances (n° 2023-M-112-04) et Inspection générale des affaires sociales (n° 2023-123R) | Revue des dépenses publiques d'apprentissage et de formation professionnelle | Mars 2024 (mis en ligne en septembre 2024) | Annexe II, **tableau 3, PDF p. 104** : NPEC en vigueur, moyens pondérés par les effectifs (N3 6 630 €, N4 7 699 €, N5 7 932 €, N6 7 751 €, N7 8 428 €) ; même page : marges 2021 par niveau ; annexe I, tableau 9, PDF p. 67 (aides à l'embauche 2020-2023 : 4 726 M€ pour les niveaux 3-4, 6 514 M€ pour les niveaux 5-7, hors champ DEPP) |
| `igas_igf_2023-07_modalites_financement_CFA.pdf` | https://igas.gouv.fr/sites/igas/files/2024-11/Rapport%20Igas-IGF%20Financement%20des%20CFA.pdf | IGF (n° 2023-M-032-02) et IGAS (n° 2023-032R) | Modalités de financement des centres de formation des apprentis (CFA) | Juillet 2023 (mis en ligne en novembre 2024) | Annexe II, p. 7 (PDF p. 80) : « Les produits sont constitués à 87 % par les niveaux de prise en charge (NPEC) » (comptabilités analytiques 2021) ; annexe III, § 3 (PDF p. 118-121) : enveloppes régionales de 138 M€ (fonctionnement) et 180 M€ (investissement), tableau 5 (dépenses régionales 2021 : 99,1 M€ de CP en fonctionnement, 176,6 M€ en investissement) |
| `ccomptes_2023-07_note_thematique_recentrer_soutien_public_formation_apprentissage.pdf` | https://www.ccomptes.fr/system/files/2023-07/20230707-note-thematique-Soutien-public-formation-professionnelle-apprentissage.pdf | Cour des comptes | « Recentrer le soutien public à la formation professionnelle et à l'apprentissage », note thématique (revue des dépenses publiques) | 07/07/2023 | p. 6 (chiffres clés 2022 : 21,8 Md€ de « financements publics », dont France compétences 14,5 Md€ de charges, « principalement financées par les entreprises (10,3 Md€) »). Sert à documenter la convention alternative où France compétences compte comme financeur public |
| `oecd_sdmx_EAG_sources_financement_FRA_ISCED35_34_2019-2023.csv` | https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_UOE_FIN@DF_UOE_FIN_SOURCE_GV_PR_NDOM,3.2/FRA..ISCED11_35SW+ISCED11_35+ISCED11_34+ISCED11_45SW+ISCED11_55SW+ISCED11_25+ISCED11_35_45.......?startPeriod=2019&dimensionAtObservation=AllDimensions&format=csvfilewithlabels | OCDE (données UOE transmises par la DEPP) | Distribution of government, private and non-domestic expenditure on educational institutions | Dernière mise à jour 2026-07-01 | France, CITE 35 (lycée professionnel et apprentis de niveau secondaire) : en 2023, total 12 286,8 M€, public (S13) 8 720,5 M€ (70,97 %), privé 3 552,3 M€ (28,91 %) ; en 2019, public 83,68 %, privé 16,23 %. Le code ISCED11_35SW (« school and work-based ») ne renvoie **aucune donnée** pour la France |
| `pages_web/soltea_premiers_resultats_campagne_2025.html` | https://www.soltea.education.gouv.fr/espace-public/les-premiers-resultats-de-la-campagne-soltea-2025 | Ministères chargés de l'éducation et de l'enseignement supérieur ; plateforme gérée par la Caisse des dépôts | « Les premiers résultats de la campagne SOLTéA 2025 » | Publiée le 29/05/2026, mise à jour le 24/09/2026 | Solde de la taxe d'apprentissage : « plus de 522 millions d'euros » collectés, 394 M€ répartis par les employeurs (75,4 %), 9 970 établissements bénéficiaires. Aucune ventilation par type d'établissement |
| `pages_web/legifrance_arrete_2026-05-28_fonds_soutien_apprentissage_regions_TRSD2614255A.html` | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054151684 | Légifrance (JORF) | Arrêté du 28 mai 2026 fixant le montant et la répartition du fonds de soutien à l'apprentissage aux régions et à la collectivité de Corse, NOR TRSD2614255A | JORF n° 0125 du 30/05/2026, texte n° 5 | Article 1 : 11 M€ (fonctionnement des CFA) et 22 M€ (investissement) pour 2026, contre 88 + 180 M€ en 2024 (jaune PLF 2026, p. 65). L'arrêté du 1er avril 2026 (JORFTEXT000053763937, non téléchargé) fixait 44,1 M€ et 90,0 M€ |

Autres sources mobilisées pour G4 (déjà présentes, non re-téléchargées) :
- `depp_ni_2025-52_compte_education_2024_donnees.xlsx` : Figure 4, C32:C36 (financement initial du 2nd degré en 2024p, dont entreprises 4,51955 %) et Figure 5, B32 et B35 (DIE du 2nd degré 73,122 Md€ ; DIE totale 197,099 Md€).
- `depp_ni_2026-42_compte_education_2025_donnees.xlsx` : Figure 4, C32:C36 et Figure 5, B33 (2025p).
- `depp_rers2026_10-04_producteurs_education_donnees.xlsx`, « 10.04 Tableau 2 » : lignes 10, 15, 20 et 26 (financement privé des producteurs du 2nd degré hors CFA) ; lignes 11, 21 et 27 (CFA).
- `depp_rers2026_10-02_financement_DIE_donnees.xlsx`, « 10.02 Tableau 4 », ligne 9 : enseignement du 2nd degré en 2024p, financement final (entreprises 3 207,6 M€, autres APU 129,1 M€).
- `depp_series_chrono_structure_die_par_niveau_366606.xlsx` (ligne 19) et `depp_series_chrono_depense_par_eleve_par_niveau_481445.xlsx` (ligne 22) : voir § 8.
- `../effectifs_nationaux/rers2026_ch06_apprentis.pdf` (RERS 2026, chapitre 6) :
  - fiche 6.01, tableaux de la PDF p. 3 : apprentis par niveau au 31/12 de 2000 à 2024 ; répartition secondaire / supérieur par type de CFA en 2024-2025 ;
  - fiche 6.08, PDF p. 16-17 : 68 367 apprentis en EPLE, dont 15 222 de niveau 3 et 18 604 de niveau 4 ; effectifs de l'ensemble des apprentis par niveau : N5 236 930, N6 167 738, N7-8 253 262, total 1 049 965.
- `../collectivites/DGCL_CLC2026_4F_Ventilation_fonctionnelle_CG25.xlsx`, onglet « F4 Reg+CTU », ligne 19 « apprentissage » : en 2025, 87,9 M€ de fonctionnement + 163,3 M€ d'investissement = 251,2 M€ (−4,7 % sur 2024).
- Réponse ministérielle à la question écrite n° 06636 (Sénat, JO du 19/03/2026, p. 1424), https://www.senat.fr/questions/base/2025/qSEQ251106636.html (lue en ligne, non téléchargée) : les formations par apprentissage ne sont pas éligibles au solde de la taxe d'apprentissage (art. L. 6241-4 du code du travail).

Sources recherchées mais non obtenues :
- jaune « Formation professionnelle » annexé au PLF 2027 : non trouvé au 04/10/2026 ;
- document méthodologique de la Dares sur la dépense nationale (https://dares.travail-emploi.gouv.fr/sites/default/files/a51153bce65fd8ac616c363b8f20fe74/Document%20m%C3%A9thodologique%20D%C3%A9pense%20nationale%20FPC%20et%20apprentissage_Jaune%202026.pdf) : page de vérification anti-robot, fichier non récupéré.

Fichiers **dérivés** G4 (préfixe `_derive_`, ce ne sont pas des fichiers bruts) :
- `_derive_G4_apprentissage_2nd_degre.py` : script qui lit les fichiers bruts ci-dessus et calcule les bornes ;
- `_derive_G4_part_publique_apprentissage_2nd_degre.csv` : 50 lignes, une par valeur (valeur, unité, source ou formule).

Complément G4 (même jour) :

| Fichier | URL exacte | Éditeur | Titre | Date de publication | Ce qui est utilisé |
|---|---|---|---|---|---|
| `insee_liste_ODAC_SD2024_mai2026.pdf` | https://www.insee.fr/fr/statistiques/fichier/8988934/Liste_ODAC_SD2024.pdf | Insee | Liste des organismes divers d'administration centrale (ODAC), comptes de la Nation 2025 (champ 2024), 15 p. | Mai 2026 (PDF créé le 18/05/2026) | p. 4-5, « Fonction 4 : Affaires économiques » : **FCOMPET France Compétences** et les **11 OPCO** (Afdas, Akto, Atlas, Constructys, L'Opcommerce, Ocapiat, Opco EP, Opco Mobilités, Opco Santé, Opco2i, Uniformation) sont classés en ODAC, donc dans les administrations publiques au sens de la comptabilité nationale. L'édition de mai 2025 (`.../8574832/Liste_ODAC_SD2023.pdf`, vérifiée puis non conservée) les classait déjà ainsi |


## 10. Complément G1 : Eurostat UOE, métadonnées ESMS et OCDE (ajout du 2026-10-04, tâche complémentaire G1)

Fichiers téléchargés le **2026-10-04** (date de consultation), par `curl` avec des en-têtes de navigateur, sauf mention contraire. Ils n'ont pas été modifiés.
Contrôles effectués :
- JSON-stat : clé `"class":"dataset"` ;
- SDMX-CSV : en-tête `DATAFLOW,LAST UPDATE,…` ;
- xlsx et zip : signature `PK` ;
- PDF : signature `%PDF`.

Point de contrôle demandé : `educ_uoe_fini01`, PUB, CITE 1, 2023, TOTAL = 31 676,0 M€. Il est retrouvé.

### 10.1 Eurostat, collecte UOE (Unesco-OCDE-Eurostat), données transmises par la DEPP

Éditeur : Eurostat (Commission européenne). API publique sans clé. Filtre : France (`geo=FR`), années 2019 à 2023 (2024 pour le personnel).
Codes de drapeaux :
- « m » : valeur manquante ; les données ne peuvent pas exister ;
- « d » : définition différente (voir métadonnées).

| Fichier | URL exacte | Titre (libellé Eurostat) et identifiant | Date de mise à jour | Ce qui est utilisé |
|---|---|---|---|---|
| `eurostat_educ_uoe_fini01_FR_MIO_EUR_2019-.json` | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_fini01?geo=FR&unit=MIO_EUR&sinceTimePeriod=2019&format=JSON&lang=fr | « Dépenses des établissement d'enseignement par niveau d'étude, orientation du programme, type d'établissement et catégorie des dépenses » (`educ_uoe_fini01`, DOI 10.2908/EDUC_UOE_FINI01) | 15/09/2026 | Libellés français et drapeaux |
| `eurostat_educ_uoe_fini01_FR_MIO_EUR_2019-.csv` | https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fini01/A.MIO_EUR....FR?startPeriod=2019&format=SDMX-CSV | Idem, au format SDMX-CSV | 15/09/2026 | Calculs. Secteurs PUB, PRV_DEP, PRV_IND, TOT_SEC. Catégories TOTAL, CUR, CUR_COMPT, CUR_COMPO, CUR_OTH, CAP, ASERV. CITE 02, 1, 2, 34, 35, 3, 4 |
| `eurostat_educ_uoe_fine02_FR_MIO_EUR_2019-.json` | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_fine02?geo=FR&unit=MIO_EUR&sinceTimePeriod=2019&format=JSON&lang=fr | « Dépenses publiques au titre de l'éducation par niveau d'étude, orientation du programme, type de source et catégorie des dépenses » (`educ_uoe_fine02`) | 15/09/2026 | Libellés français |
| `eurostat_educ_uoe_fine02_FR_MIO_EUR_2019-.csv` | https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fine02/A.MIO_EUR.....FR?startPeriod=2019&format=SDMX-CSV | Idem, au format SDMX-CSV | 15/09/2026 | Financeurs S13, S1311, S1312, S1313. Rubriques : TOT_SEC/DIR, PUB/DIR, PRV_DEP/DIR, PRV_IND/DIR, TOT_SEC/CAP, S1D/TRF_PAY, S14/FA_GRNT, S1/TOTAL |
| `eurostat_educ_uoe_fine01_FR_MIO_EUR_2019-.json` et `.csv` | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_fine01?geo=FR&unit=MIO_EUR&sinceTimePeriod=2019&format=JSON&lang=fr ; https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fine01/A.MIO_EUR...FR?startPeriod=2019&format=SDMX-CSV | « Dépenses totales au titre de l'éducation par niveau d'étude, orientation du programme et source » (`educ_uoe_fine01`) | 15/09/2026 | Contrôle : S13 = fine02 S13/S1/TOTAL. Le total S1 porte le drapeau « d » et n'est pas utilisé |
| `eurostat_educ_uoe_fine10_FR_NR_2019-.json` et `.csv` | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_fine10?geo=FR&sinceTimePeriod=2019&format=JSON&lang=fr ; https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fine10/A.NR....FR?startPeriod=2019&format=SDMX-CSV | « Élèves et étudiants par niveau d'étude et orientation du programme, corrigés des statistiques sur les dépenses d'éducation et alignés à l'année financière » (`educ_uoe_fine10`) | 11/09/2026 | Dénominateurs TOT_FTE par secteur et par CITE ; temps partiel en CITE 35 (apprentis) |
| `eurostat_educ_uoe_fine09_FR_EUR_2019-.json` et `.csv` | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_fine09?geo=FR&unit=EUR&sinceTimePeriod=2019&format=JSON&lang=fr ; https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fine09/A.EUR..FR?startPeriod=2019&format=SDMX-CSV | « Dépenses publiques au titre de l'éducation par élève/étudiant, calculs fondés sur des équivalents temps plein, par niveau d'étude et orientation du programme » (`educ_uoe_fine09`) | 15/09/2026 | Valeurs publiées par élève ETP ; contrôle du recalcul |
| `eurostat_educ_uoe_fini04_FR_EUR_2019-.json` | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_fini04?geo=FR&unit=EUR&sinceTimePeriod=2019&format=JSON&lang=fr | « Dépenses annuelles au titre des établissements d'enseignement par élève/étudiant, calculs fondés sur des équivalents temps plein… » (`educ_uoe_fini04`) | 15/09/2026 | Contrôle : dépense des établissements par élève ETP (PUB, TOT_SEC) |
| `eurostat_educ_uoe_fine03_FR_MIO_EUR_2019-.json` | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_fine03?geo=FR&unit=MIO_EUR&sinceTimePeriod=2019&format=JSON&lang=fr | « Dépenses privées au titre de l'éducation par niveau d'étude, orientation du programme, type de source et catégorie des dépenses » (`educ_uoe_fine03`) | 15/09/2026 | S1D_OTH (autres entités privées) vers les établissements de CITE 35 : 3 062 M€ en 2023 |
| `eurostat_educ_uoe_perp02_FR_enseignants_2019-.csv` | https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_perp02/A.NR.....FR?startPeriod=2019&format=SDMX-CSV | « Classroom teachers and academic staff by education level, programme orientation, sex, type of institution and employment status » (`educ_uoe_perp02`) | 05/08/2026 | TOT_FTE, sexe T, PUB et PRV_DEP, CITE 02 à 4, étiquettes 2023 et 2024 (années scolaires 2022-23 et 2023-24) |
| `eurostat_educ_uoe_enrp02_FR_ED02_2019-.json` | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_enrp02?geo=FR&isced11=ED02&sex=T&age=TOTAL&sinceTimePeriod=2019&format=JSON&lang=fr | « Élèves de l'éducation de la petite enfance par sexe et âge » (`educ_uoe_enrp02`) | 11/08/2026 | Test de la convention d'étiquetage des années scolaires (comparaison avec RERS 2026, 3.01) |

### 10.2 Métadonnées Eurostat

| Fichier | URL exacte | Titre | Date | Ce qui est utilisé |
|---|---|---|---|---|
| `eurostat_esms_educ_uoe_enr_esms_en.htm` | https://ec.europa.eu/eurostat/cache/metadata/en/educ_uoe_enr_esms.htm | ESMS « Pupils and students - enrolments (educ_uoe_enr) ». C'est la fiche commune à toute la collecte UOE, finance comprise : c'est elle que pointe le lien « Explanatory texts » des jeux fini/fine | Metadata last update : 19 June 2026 | § 3.9 et § 5 (périodes de référence) ; § 14.1 (délai de la finance : 2,5 ans) ; § 15.1 « Ambiguities of classification with regards to levels of government » ; § 18.5 (comptabilité de caisse) ; § 18.6 (alignement des effectifs sur l'exercice) |
| `eurostat_esms_educ_uoe_enr_esms.sdmx.zip` | https://ec.europa.eu/eurostat/api/dissemination/files?file=metadata/educ_uoe_enr_esms.sdmx.zip | Même fiche au format SDMX, avec ses annexes | Fichiers datés du 02/10/2026 dans l'archive | Annexes décrites ci-dessous |

Annexes de l'archive SDMX :
- `Annexes/educ_uoe_enr_esms_an_1.htm` : glossaire (dépenses courantes et en capital, dépenses de personnel, retraites, autres dépenses courantes) ;
- `an_2.pdf` : « finance – accuracy » ;
- `an_4.xlsx` : « Footnote report UOE13-UOE18 ». Son onglet « Finance » contient la seule note France : « FR 2012 -> Household expenditure does not include Payments for goods not required for participation » ;
- `Footnote report UOE19-UOE25` : sans onglet Finance.

Introuvable le 2026-10-04 (réponse 404) :
- la fiche `https://ec.europa.eu/eurostat/cache/metadata/en/educ_uoe_fin_esms.htm` n'existe pas ;
- le rapport qualité national France, `https://ec.europa.eu/eurostat/cache/metadata/en/educ_uoe_enr_esqrs_fr.htm` (variantes `EN` et `FR` testées).

### 10.3 OCDE (*Education at a Glance* / *Regards sur l'éducation*)

| Fichier | URL exacte | Titre | Date | Ce qui est utilisé |
|---|---|---|---|---|
| `oecd_eag2025_sources_methodologies_technical_notes.pdf` | https://www.oecd.org/content/dam/oecd/en/publications/support-materials/2025/09/education-at-a-glance-2025-sources-methodologies-and-technical-notes_0050a1ae/Education%20at%20a%20Glance%20Sources%20Methodologies%20and%20Technical%20Notes.pdf (obtenu par **WebFetch**, copie binaire du PDF) | OCDE, *Education at a Glance 2025: Sources, Methodologies and Technical Notes*, DOI 10.1787/fcfaf2d1-en | 09/09/2025 (PDF créé le 05/09/2025) ; 496 p. | Voir le détail des pages ci-dessous |
| `oecd_eag2025_statlink_o0puiv_metadonnees_UOE_finance.xlsx` | https://stat.link/o0puiv (redirige vers https://stat.link/files/fcfaf2d1-en/o0puiv.xlsx) | « Table Annex C. General information on the data collected through the UOE Finance questionnaire » (EAG 2025, version 1) | 09/09/2025 | Onglet METADATA, ligne 17 (France) : sources publique et privée, année financière 2022 |
| `oecd_eag2026_education_at_a_glance_2026.pdf` | https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/09/education-at-a-glance-2026_3bce4131/b4968bbc-en.pdf | OCDE, *Education at a Glance 2026: OECD Indicators*, DOI 10.1787/b4968bbc-en | Publié le 29/09/2026 (Last-Modified 28/09/2026) ; 558 p. ; gel des données le 17/06/2026 | Lignes France des tableaux C1.1 (p. 297), C1.2 (p. 299), C1.3 (p. 301), C1.4 (p. 303), C2.1 (p. 311), C2.2 (p. 313), C3.1 (p. 326), C3.2 (p. 328), C4.1 (p. 340), C4.2 (p. 342) ; codes de contrôle |
| `oecd_eag2026_statlink_ax7gjn_chapitre_C1.xlsx` | https://stat.link/ax7gjn (redirige vers https://stat.link/files/b4968bbc-en/ax7gjn.xlsx) | EAG 2026, tableaux du chapitre C1 | Version 1, 29/09/2026 | Onglets « Table C1.1. » à « Table C1.8 (web only). », ligne 23 (France) |
| `oecd_eag2026_statlink_4y0jap_chapitre_C2.xlsx` | https://stat.link/4y0jap (redirige vers https://stat.link/files/b4968bbc-en/4y0jap.xlsx) | EAG 2026, chapitre C2 | 29/09/2026 | « Table C2.1. » et « Table C2.2. », ligne 23 |
| `oecd_eag2026_statlink_e0c4fw_chapitre_C3.xlsx` | https://stat.link/e0c4fw (redirige vers https://stat.link/files/b4968bbc-en/e0c4fw.xlsx) | EAG 2026, chapitre C3 | 29/09/2026 | « Table C3.1. » et « Table C3.2. », ligne 23 |
| `oecd_eag2026_statlink_83o9jl_chapitre_C4.xlsx` | https://stat.link/83o9jl (redirige vers https://stat.link/files/b4968bbc-en/83o9jl.xlsx) | EAG 2026, chapitre C4 | 29/09/2026 | « Table C4.1. » et « Table C4.2. », ligne 23 |

Pages utilisées des notes techniques EAG 2025 (pagination imprimée) :
- p. 47-50 : méthodologie commune du chapitre C (cadre « core / peripheral », sources initiales et finales, comptabilité de caisse, imputation des retraites, dépense par ETP) ;
- p. 54-55 : notes France du chapitre C1 ;
- p. 63 : chapitre C2 ;
- p. 78 : chapitre C5 (CPGE et BTS) ;
- p. 165 : personnel, France.

Accès :
- les pages HTML de oecd.org répondent 403 à WebFetch, y compris la page des notes techniques 2026 (https://www.oecd.org/en/publications/education-at-a-glance-2026-sources-methodologies-and-technical-notes_dcf64a14-en.html) ;
- les PDF du répertoire `content/dam` et les fichiers stat.link sont accessibles par curl ;
- le PDF EAG 2026 (16,5 Mo) dépasse la limite de WebFetch (10 Mo) ;
- les notes techniques 2026 n'ont pas été obtenues.

### 10.4 Contrôle de la fiche 10.04 des RERS 2026 (aucun nouveau fichier conservé)

- Retéléchargé le 2026-10-04 depuis https://rers.depp.education.fr/data/2026/10_BUD/04_PRODEDUC/dataExcel.fr.xlsx.
- Résultat : 237 150 octets, MD5 `6db21ad304eaa9f471f9ce553df94818`, **identique** à `depp_rers2026_10-04_producteurs_education_donnees.xlsx`.
- En-têtes HTTP : `Last-Modified: Mon, 14 Sep 2026 14:40:52 GMT`, `ETag: "39e5e-65b726bc0dc3d"`.
- La copie temporaire a été supprimée.

### 10.5 Fichiers déjà présents, mobilisés pour G1 (non retéléchargés)

- `depp_series_chrono_die_financeur_initial_final_par_niveau_366603.xlsx` : onglets « DIE 1er degré » et « DIE 2nd degré », colonne T (2023), lignes 16 à 21 (financeurs initiaux).
- `depp_ni_2025-52_compte_education_2024_donnees.xlsx` : Figure 1bis, cellule F8 (DIE de l'enseignement scolaire 2023, définitive, 126,29 Md€).
- `depp_rers2025_10-05_depense_par_eleve_donnees.xlsx` : dépense par élève 2023p (voir NOTES § 2).
- `depp_geographie_de_l_ecole_2026.pdf` : p. 52 imprimée (p. 54 du PDF), « 14,5 milliards d'euros en 2023 » pour les départements et les régions.
- `depp_rers2026_chap03_eleves_premier_degre.pdf` : fiche 3.01, p. 75, effectifs du préélémentaire par rentrée.

### 10.6 Fichiers dérivés G1

Ils portent le préfixe `_derive_G1_` ; ce ne sont pas des fichiers bruts.
- `_derive_G1_script_uoe_structure.py` : script Python 3.11 (pandas). Il relit les CSV Eurostat bruts et régénère les 5 fichiers ci-dessous.
- `_derive_G1_uoe_structure_nature_par_niveau_2019-2023.csv` : par année, niveau et secteur : montants (M€), parts (%), élèves ETP, euros par élève ETP, contrôle des sommes.
- `_derive_G1_uoe_depense_publique_par_niveau_administration_2019-2023.csv` : par année, niveau et administration : DIR (dont vers PUB, PRV_DEP, PRV_IND), CAP, TRF_PAY, FA_GRNT, dépense finale, S1|TOTAL publié, transferts versés aux autres administrations, part de S13, euros par élève ETP.
- `_derive_G1_uoe_depense_par_eleve_ETP_2019-2023.csv` : dépense publique par élève ETP recalculée et publiée (fine09), dépense des établissements par élève, part publique directe.
- `_derive_G1_estimation_depense_publique_par_nature_2019-2023.csv` : ventilation **estimée** de la dépense publique par nature (variantes V1 et V2 ; hypothèse H-G1-5).
- `_derive_G1_remuneration_par_ETP_enseignant.csv` : rémunération des enseignants par ETP d'enseignant (hypothèse H-G1-7).
