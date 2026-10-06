# Sources officielles : coût moyen d'un élève pour la puissance publique (France, 2025)

**Organisation.** Les sources sont regroupées par producteur (§ 1 à 8), puis viennent les extractions intermédiaires (§ 9), les sources citées mais non archivées ou introuvables (§ 10), les sources de l'analyse « Seine-Saint-Denis et Paris » (§ 11), les URL exactes des requêtes d'API (annexe A) et la méthode de vérification des liens (annexe B). Chaque fiche donne le titre exact, le producteur, la date de publication, l'URL, le fichier local (`data/raw/…`), ce qui est utilisé, et la date de consultation.

**Repères.** **[S]** lu par un script de `scripts/` ; **[R]** cité dans `rapport.md` ; **[H]** cité dans `hypotheses.md` ; **[X]** utilisé à travers une extraction du § 9 ; **[C]** contrôle ou contexte, cité seulement dans les `NOTES.md` de `data/raw/`. Toutes les sources ont été consultées le 2026-10-04 et tous les liens ont été revérifiés ce jour-là (annexe B).

**Pour citer le résultat principal.** « Dépense publique moyenne par élève ou apprenti en 2025 : ≈ 9 700 € (apprentis du secondaire compris ; calcul à partir de DEPP, NI 26.42, 2025 provisoire) ». Forme longue : « Dépense de l'État, des collectivités territoriales et des autres administrations publiques par élève du 1er et du 2nd degré en 2025 : 9 710 €, calcul à partir de DEPP, *Note d'Information* n° 26.42, septembre 2026, figures 4, 5 et 7 (données 2025 provisoires, financement initial, apprentis compris) ».

---

## Sommaire

1. [DEPP / ministère de l'Éducation nationale](#1-depp--ministère-de-léducation-nationale)
2. [data.education.gouv.fr (open data par établissement)](#2-dataeducationgouvfr-open-data-par-établissement)
3. [Budget de l'État](#3-budget-de-létat)
4. [Collectivités territoriales (DGFiP, DGCL, OFGL, collectivités)](#4-collectivités-territoriales-dgfip-dgcl-ofgl-collectivités)
5. [INSEE](#5-insee)
6. [Eurostat](#6-eurostat)
7. [OCDE](#7-ocde)
8. [Cour des comptes et autres organismes publics](#8-cour-des-comptes-et-autres-organismes-publics)
9. [Extractions (transcriptions de sources officielles)](#9-extractions-transcriptions-de-sources-officielles)
10. [Sources citées mais non archivées, introuvables ou à surveiller](#10-sources-citées-mais-non-archivées-introuvables-ou-à-surveiller)
11. [Seine-Saint-Denis et Paris](#11-seine-saint-denis-et-paris)
- [Annexe A. URL exactes des requêtes d'API](#annexe-a-url-exactes-des-requêtes-dapi)
- [Annexe B. Vérification des liens (2026-10-04)](#annexe-b-vérification-des-liens-2026-10-04)

Abréviations : DEPP = Direction de l'évaluation, de la prospective et de la performance (service statistique du ministère de l'Éducation nationale) ; NI = *Note d'Information* ; RERS = *Repères et références statistiques* ; DIE = dépense intérieure d'éducation ; MIES = mission interministérielle « Enseignement scolaire » ; RAP / PAP = rapport / projet annuel de performances ; CT = collectivités territoriales ; APU = administrations publiques.

---

## 1. DEPP / ministère de l'Éducation nationale

### 1.1 Compte de l'éducation (dépense, financeurs, dépense par élève)

#### DEPP-1 · NI 26.42, compte de l'éducation 2025 : [S] [R] [H]
- **Titre exact** : « En 2025, 199,2 milliards d'euros consacrés à l'éducation, soit 6,7 % du PIB », *Note d'Information* n° 26.42.
- **Producteur** : ministère de l'Éducation nationale, DEPP. Auteurs : L. Bagot, C. Dutey, C. de Fornel, V. Liogier, S. Rousseau.
- **Publication** : septembre 2026 (page web datée du 29/09/2026).
- **URL** :
  - page : <https://www.education.gouv.fr/depp/en-2025-1992-milliards-d-euros-consacres-l-education-soit-67-du-pib-506005> ;
  - PDF : <https://www.education.gouv.fr/sites/default/files/document/educationnationaledepp-ni-2026-42pdf-520993.pdf> ;
  - données : <https://www.education.gouv.fr/sites/default/files/document/educationnationaledepp-ni-2026-42donneesxlsx-521029.xlsx> ;
  - DOI affiché sur la page : https://doi.org/10.48464/ni-26-42, **pas encore enregistré au 2026-10-04** (erreur 404, voir § 10).
- **Fichiers locaux** : `data/raw/depp_compte_education/depp_ni_2026-42_compte_education_2025.pdf` et `…/depp_ni_2026-42_compte_education_2025_donnees.xlsx` ; copies identiques : `data/raw/collectivites/DEPP_NI_26-42_compte_education_2025.pdf` et `…_donnees.xlsx`.
- **Utilisé** :
  - onglet « Figure 4 » (structure de la DIE par financeur initial et niveau en 2025, en %), cellules B32:C36 : parts de l'État, des CT, des autres APU, des entreprises et des ménages, 1er et 2nd degrés ;
  - « Figure 5 » (DIE par niveau en 2025, Md€), B32:B33 : 59,999 Md€ au 1er degré et 73,754 Md€ au 2nd degré ;
  - « Figure 6 » (dépense moyenne par élève selon le niveau en 2025), B31:B35 : sous-niveaux ;
  - « Figure 7 » (dépense moyenne par élève en euros constants, prix 2025), C37:D82 : série 1980-2025p, dont C82 = 9 440 € et D82 = 11 780 € ;
  - « Figure 1bis » : révision de 2024 (DIE totale 197,10 Md€ en E5 → 196,76 Md€ en E8, écart −0,34 Md€ en E11 ; enseignement scolaire 131,65 Md€ en E21 → 131,79 Md€ en E25, écart +0,14 Md€ en E29) ;
  - PDF p. 1 à 4 et onglet « Définitions et méthodologie » : État = MEN-MESRE + autres ministères + reste du monde, CAS Pensions inclus, données 2025 provisoires.
- **Où** : scripts 01, 04 (et 06 via A5) ; rapport § 1, 2, 3, 7, 8, 9 ; hypothèses § 0, H-G4, H-A1, H-A5, H-A7, H-B8, H-B13, anomalie 1.
- **Consulté le** : 2026-10-04.

#### DEPP-2 · NI 25.52, compte de l'éducation 2024 (provisoire) : [S] [R] [H]
- **Titre exact** : « En 2024, 197,1 milliards d'euros consacrés à l'éducation, soit 6,8 % du PIB », *Note d'Information* n° 25.52.
- **Producteur** : DEPP. Auteurs : L. Bagot, C. Dutey, C. de Fornel, V. Liogier, S. Rousseau.
- **Publication** : septembre 2025 (page web datée du 23/09/2025).
- **URL** :
  - page : <https://www.education.gouv.fr/depp/en-2024-1971-milliards-d-euros-consacres-l-education-soit-68-du-pib-452853> ;
  - PDF : <https://www.education.gouv.fr/media/229440/download>, qui redirige vers <https://www.education.gouv.fr/sites/default/files/2025-09/depp-ni-2025-52-442155.pdf> ;
  - données : <https://www.education.gouv.fr/media/229443/download>, qui redirige vers <https://www.education.gouv.fr/sites/default/files/2025-09/depp-ni-2025-52-donn-es-442158.xlsx> ;
  - DOI : <https://doi.org/10.48464/ni-25-52>.
- **Fichiers locaux** : `data/raw/depp_compte_education/depp_ni_2025-52_compte_education_2024.pdf` et `…_donnees.xlsx`.
- **Utilisé** : onglets « Figure 4 » (B32:C36, financeurs 2024p), « Figure 5 » (B31:B32, DIE 2024p par degré), « Figure 6 » (B32:B36, E32, E34). Ces cellules servent au calcul 2024p (9 493 € ; contrôle 10 352 € contre 10 350 € publiés) et à la croissance 2024 → 2025 du financement des CT (H-B8).
- **Où** : scripts 01, 04 ; rapport § 3, 9 ; hypothèses H-A2, H-A7, H-B8.
- **Consulté le** : 2026-10-04.

#### DEPP-3 · *Repères et références statistiques* 2026 (RERS 2026) : [S] [R] [H]
- **Titre exact** : *Repères et références statistiques sur les enseignements, la formation et la recherche*, édition 2026.
- **Producteur** : DEPP, avec le SIES (ministère chargé de l'enseignement supérieur).
- **Publication** : page de l'édition datée du 25/08/2026 : <https://www.education.gouv.fr/depp/reperes-et-references-statistiques-2026-505320>. Les tableaux Excel sont diffusés sur « RERS interactif » (<https://rers.depp.education.fr/>).
- **Consulté le** : 2026-10-04.

| Partie | URL exacte | Fichier local | Ce qui est utilisé | Où |
|---|---|---|---|---|
| Chap. 10 « Budgets, coûts et financements » (PDF, p. 407-425 ; PDF du 27/07/2026) | <https://www.education.gouv.fr/sites/default/files/document/10-budget-couts-et-financementpdf-519303.pdf> | `data/raw/depp_compte_education/depp_rers2026_chap10_budget_couts_financement.pdf` (copie identique : `data/raw/budget_etat/DEPP_RERS2026_chapitre10_budgets_couts_financements.pdf`) | Page imprimée = page PDF + 406. Fiche 10.02, p. 411, note 2 : « reste du monde (Union européenne et autres pays étrangers), pour 428,9 millions d'euros en 2024 en financeur final ». Fiche 10.03, p. 413 : P143 exécuté 2025 = 1 731 M€. Fiche 10.04, p. 415 : nature des dépenses (72,0 % / 48,4 % / 8,5 %). Fiche 10.05, p. 417. Fiche 10.06, p. 419, tableau « Montant annuel des aides par nature » : allocation de rentrée scolaire 2 207 791 k€ en 2025 (source CNAF ; champ France + Saint-Pierre-et-Miquelon) | H-G3 (428,9 M€) et H-A4 (2 207,8 M€) ; anomalies 2 et 5 |
| Fiche 10.02 « Le financement de la dépense intérieure d'éducation » (xlsx) | <https://rers.depp.education.fr/data/2026/10_BUD/02_FINDIE/dataExcel.fr.xlsx> | `data/raw/depp_compte_education/depp_rers2026_10-02_financement_DIE_donnees.xlsx` (copie identique dans `collectivites/`) | Onglet « 10.02 Tableau 4 » (financement des activités d'éducation en 2024, financement final, M€), cellules F17 (CT, transports scolaires = 2 484,8 M€) et F18 (CT, fournitures et livres scolaires = 185,8 M€) ; note 2 (reste du monde, 428,9 M€) | script 04 ; H-G3, H-B8, H-B14 |
| Fiche 10.03 « Le budget : analyse et évolution » (xlsx) | <https://rers.depp.education.fr/data/2026/10_BUD/03_BUDEVO/dataExcel.fr.xlsx> | `…/depp_rers2026_10-03_budget_donnees.xlsx` | « 10.03 Tableau 3 », ligne « Programme 143 », colonne 2025 | [X] passerelle G5 ; anomalie 5 |
| Fiche 10.04 « Le financement des producteurs d'éducation » (xlsx) | <https://rers.depp.education.fr/data/2026/10_BUD/04_PRODEDUC/dataExcel.fr.xlsx> | `…/depp_rers2026_10-04_producteurs_education_donnees.xlsx` (copie identique dans `collectivites/`) | « 10.04 Tableau 2 » (financement final 2024p, M€) : E9 = CT → écoles publiques, 20 608,1 M€ ; E19 = CT → écoles privées sous contrat, 1 141,8 M€ ; lignes 11, 21 et 27 (CFA, pour H-A3). « 10.04 Graphique 4 » : B7:B11 (structure par nature) | scripts 01, 04 ; H-B8, anomalie 2 |
| Fiche 10.05 « Les dépenses par élève et par étudiant » (xlsx) | <https://rers.depp.education.fr/data/2026/10_BUD/05_DEPEL/dataExcel.fr.xlsx> | `…/depp_rers2026_10-05_depense_par_eleve_donnees.xlsx` | « 10.05 Tableau 2 », J13 : 10 350 € (sous-total 1er + 2nd degrés, 2024p). « 10.05 Graphique 4 », B8:E9 : structure par activité | script 01 ; rapport § 3 ; H-A7 |
| Chap. 6 « Les apprentis » (PDF) | <https://www.education.gouv.fr/sites/default/files/document/6-les-apprentispdf-519291.pdf> | `data/raw/effectifs_nationaux/rers2026_ch06_apprentis.pdf` | Fiche 6.01, p. 218-219 : apprentis par niveau au 31/12/2024 (niveau 3 : 221 549 ; niveau 4 : 170 486). Fiche 6.09 « Les apprentis et les CFA en 2025-2026 », tableau 2, p. 235 (p. 19 du PDF) : au 31/12/2025, niveau 3 : 219 666 ; niveau 4 : 172 271 | H-A3 (392 035 et 391 937) |
| Chap. 1 « Le système éducatif » (PDF) | <https://www.education.gouv.fr/sites/default/files/document/1-le-systeme-educatifpdf-519276.pdf> | `data/raw/effectifs_nationaux/rers2026_ch01_systeme_educatif.pdf` (copie identique dans `depp_compte_education/`) | Fiche 1.02, tableau 2, p. 15 : effectifs aux rentrées 2024 et 2025, dont apprentis du secondaire (392,0 et 391,9 milliers) | contrôle de H-E2 et H-A3 |
| Chap. 3 « Les élèves du premier degré » (PDF) | <https://www.education.gouv.fr/sites/default/files/document/3-les-eleves-du-premier-degrepdf-519282.pdf> | `data/raw/effectifs_nationaux/rers2026_ch03_eleves_premier_degre.pdf` (copie identique dans `depp_compte_education/`) | Fiche 3.09, note 1 : 5 469 élèves en classes hors contrat dans des écoles sous contrat (rentrée 2025) | H-E5 |

#### DEPP-4 · Séries chronologiques « Les coûts et les financements » : [S] [R] [H]
- **Titre de la page** : « Séries chronologiques de données statistiques sur le système éducatif ».
- **Producteur** : DEPP.
- **Publication** : page datée du 01/03/2026 : <https://www.education.gouv.fr/depp/series-chronologiques-de-donnees-statistiques-sur-le-systeme-educatif-12530>. Les fichiers de coûts y sont « actualisé(e) en septembre 2025 » (2024 provisoire) ; aucune mise à jour de septembre 2026 n'était parue au 04/10/2026.
- **Consulté le** : 2026-10-04.

| Fichier (titre exact) | URL exacte | Fichier local (`data/raw/depp_compte_education/`) | Ce qui est utilisé | Où |
|---|---|---|---|---|
| « La dépense intérieure d'éducation (DIE), sa structure par financeur initial et final, selon le niveau d'enseignement » (366603) | <https://www.education.gouv.fr/sites/default/files/document/la-d-pense-int-rieure-d-ducation-par-financeur-initial-et-final-selon-le-niveau-d-enseignement-366603.xlsx> | `depp_series_chrono_die_financeur_initial_final_par_niveau_366603.xlsx` | Onglets « DIE 1er degré » et « DIE 2nd degré », cellules U28, U30, U31 : parts de l'État, des CT et des autres APU en financement final, 2024p | script 01 ; rapport § 3 ; H-A2 |
| « La structure de la dépense intérieure d'éducation (DIE) par niveau d'enseignement » (366606) | <https://www.education.gouv.fr/sites/default/files/document/la-structure-de-la-d-pense-int-rieure-d-ducation-par-niveau-d-enseignement-366606.xlsx> | `depp_series_chrono_structure_die_par_niveau_366606.xlsx` | Onglet « Structure DIE par niveau fin », U19 : apprentissage du second degré = 1,9 % de la DIE en 2024p | script 01 ; H-A3 |
| « La dépense intérieure d'éducation (DIE) par niveau d'enseignement et sa part dans le PIB » (508145) | <https://www.education.gouv.fr/sites/default/files/document/La%20d%C3%A9pense%20int%C3%A9rieure%20d%26%23039%3B%C3%A9ducation%20%28DIE%29%20par%20niveau%20d%26%23039%3Benseignement%20et%20sa%20part%20dans%20le%20PIB-508145.xlsx> (lien tel qu'il figure sur la page officielle) | `depp_series_chrono_die_par_niveau_part_pib_508145.xlsx` | Onglet « Part DIE dans PIB par niveau » (avec une espace finale), AU10 : DIE 2024p = 197,0994 Md€ | script 01 ; H-A3 |
| « La dépense d'éducation par élève ou étudiant par niveau d'enseignement » (481445) | <https://www.education.gouv.fr/sites/default/files/document/la-d-pense-d-ducation-par-l-ve-ou-tudiant-par-niveau-d-enseignement-481445.xlsx> | `depp_series_chrono_depense_par_eleve_par_niveau_481445.xlsx` | Ligne 22 : dépense par apprenti du 2nd degré (9 500 € en 2024p) | [X] [C] (NOTES § 11-12) |
| « Les effectifs dans les centres de formations d'apprentis par niveau et diplôme selon le sexe » (310608, source SIFA ; actualisation octobre 2025) | <https://www.education.gouv.fr/sites/default/files/document/les-effectifs-dans-les-centres-de-formations-d-apprentis-par-niveau-et-dipl-me-selon-le-sexe-310608_0.xlsx> | `depp_series_chrono_apprentis_cfa_par_niveau_310608.xlsx` | Onglet « Ensemble », lignes 11 et 15 : apprentis de niveaux 3 et 4 au 31/12/2024 (392 035) | H-A3 |

#### DEPP-5 · *Géographie de l'École* 2026 : [S] [R] [H]
- **Titre exact** : *Géographie de l'École*, édition 2026. Fiche 22 : « La dépense d'éducation des départements et des régions par collégien et par lycéen ».
- **Producteur** : DEPP.
- **Publication** : juin 2026 (page datée du 30/06/2026 : <https://www.education.gouv.fr/depp/geographie-de-l-ecole>).
- **URL** :
  - PDF : <https://www.education.gouv.fr/sites/default/files/document/g-ographie-de-l-cole-2026-519114.pdf> ;
  - données de la fiche 22 : <https://www.education.gouv.fr/sites/default/files/document/la-depense-d-education-par-eleve-ou-etudiant-prise-en-charge-par-les-ministeres-charges-de-l_0.xlsx>. Sur la page officielle, c'est bien le lien n° 22 (« La dépense d'éducation des départements et des régions par collégien et par lycéen ») ; seule l'infobulle du lien reprend par erreur le titre de la fiche 21.
- **Fichiers locaux** : `data/raw/depp_compte_education/depp_geographie_de_l_ecole_2026.pdf` ; `…/depp_geo_ecole2026_depense_departements_regions_par_collegien_lyceen_donnees.xlsx` (copie identique : `data/raw/collectivites/DEPP_GeoEcole2026_fiche22_depense_departements_regions_donnees.xlsx`).
- **Utilisé** : onglet 22.1 (dépenses totales annuelles des départements et CTU par collégien), C12:C112 et C113 (« France » : 2 010 €) ; onglet 22.4 (dépenses totales annuelles des régions et CTU par lycéen), C12:C28 et C29 (« France » : 3 000 €) ; chaque valeur est repérée par le code (22.1) ou le nom (22.4) lu sur sa ligne ; le script contrôle l'en-tête de la colonne lue et celui de la colonne des codes ou des noms (ligne 11), puis vérifie que seuls Mayotte, Saint-Barthélemy et Saint-Martin n'ont pas de clé. Moyenne 2021-2023 en euros constants 2023 ; champ France hors Mayotte, public + privé sous contrat. PDF p. 52-53 imprimées (fiche 22) et p. 106-107 (méthodologie).
- **Où** : script 04 ; rapport § 4, 9 ; H-B10.
- **Consulté le** : 2026-10-04.

#### DEPP-6 · Dossier DEPP n° 206 (méthode du compte de l'éducation) : [H] [X]
- **Titre exact** : « Le Compte de l'éducation. Principes, méthodes et résultats pour les années 2006 à 2014 », *Les dossiers de la DEPP*, n° 206.
- **Producteur** : DEPP.
- **Publication** : avril 2016.
- **URL** : <https://www.education.gouv.fr/sites/default/files/document/DEPP-dossier-2016-206_567592(1).pdf-270180.pdf>
- **Fichier local** : `data/raw/depp_compte_education/depp_dossier206_2016_compte_education_methodologie.pdf` (copie identique : `data/raw/effectifs_nationaux/depp_dossier206_2016_compte_education_methodes.pdf`). Page PDF = page imprimée + 2.
- **Utilisé** :
  - p. 35 : effectif de l'année civile = 2/3 de l'année scolaire n−1/n + 1/3 de n/n+1 ;
  - p. 16 : financement initial et final ;
  - p. 18 et 25 : CAS Pensions inclus ;
  - p. 13-15 : niveaux, administration générale ;
  - tableau 2i, p. 152 et 168 (extraction du § 9).
- **Où** : script 02 (docstring) ; hypothèses § 0, H-E1, H-B8 (règle d'imputation de l'administration générale, via G3), H-B17 (ventilation 2013, via la passerelle G5).
- **Consulté le** : 2026-10-04.

### 1.2 Effectifs d'élèves

#### DEPP-7 · NI 25.58, effectifs du 1er degré à la rentrée 2025 : [S] [R] [H]
- **Titre exact** : « Les effectifs dans le premier degré : 6,155 millions d'élèves scolarisés à la rentrée 2025 », *Note d'Information* n° 25.58.
- **Producteur** : DEPP. Auteurs : M. Barhoumi, L. Brun, P. Serre.
- **Publication** : octobre 2025 (page datée du 31/10/2025).
- **URL** :
  - page : <https://www.education.gouv.fr/depp/les-effectifs-dans-le-premier-degre-6155-millions-d-eleves-scolarises-la-rentree-2025-467612> ;
  - PDF : <https://www.education.gouv.fr/sites/default/files/2025-11/depp-ni-2025-58-229887-les-effectifs-dans-le-premier-degr--473909.pdf> ;
  - données : <https://www.education.gouv.fr/sites/default/files/2025-11/depp-ni-2025-58-donnees-229890-les-effectifs-dans-le-premier-degr--473912.xlsx> ;
  - DOI : <https://doi.org/10.48464/ni-25-58>.
- **Fichiers locaux** : `data/raw/effectifs_nationaux/depp_ni_2025-58_effectifs_1er_degre_rentree2025.pdf` et `…_donnees.xlsx` (copie identique : `data/raw/etablissements/DEPP_NI_25-58_effectifs_1er_degre_rentree2025_donnees.xlsx`).
- **Utilisé** : onglet « Figure 7 en ligne », ligne 42 (« France ») ; colonnes F-H (public, rentrées 2023-2025), O-Q (privé sous contrat), X-Z (ensemble).
- **Où** : script 02 (E1, E2) ; rapport § 4, 9 ; H-E1, H-E2, H-E3.
- **Consulté le** : 2026-10-04.

#### DEPP-8 · NI 25.59, effectifs du 2nd degré à la rentrée 2025 : [S] [R] [H]
- **Titre exact** : « Les effectifs dans le second degré : 5,621 millions d'élèves scolarisés à la rentrée 2025 », *Note d'Information* n° 25.59.
- **Producteur** : DEPP. Auteurs : P. Dieusaert, L. Juzdzewski, A. Leduc, N. Miconnet.
- **Publication** : octobre 2025 (page datée du 31/10/2025).
- **URL** :
  - page : <https://www.education.gouv.fr/depp/les-effectifs-dans-le-second-degre-5621-millions-d-eleves-scolarises-la-rentree-2025-467609> ;
  - PDF : <https://www.education.gouv.fr/sites/default/files/2025-11/depp-ni-2025-59-les-effectifs-dans-le-second-degr-5-621-millions-d-l-ves-scolaris-s-la-rentr-e-2025-473903.pdf> ;
  - données : <https://www.education.gouv.fr/sites/default/files/2025-11/depp-ni-2025-59-donn-es-les-effectifs-dans-le-second-degr-5-621-millions-d-l-ves-scolaris-s-la-rentr-e-2025-473906.xlsx> ;
  - DOI : <https://doi.org/10.48464/ni-25-59>.
- **Fichiers locaux** : `data/raw/effectifs_nationaux/depp_ni_2025-59_effectifs_2nd_degre_rentree2025.pdf` et `…_donnees.xlsx` (copie identique dans `data/raw/etablissements/`).
- **Utilisé** : onglet « Figure 10 en ligne » (effectifs du public et du privé sous contrat, rentrées 2022-2025) ; lignes 13 (formations en collège), 14 (classe préparatoire), 25 (formations professionnelles), 30 (formations générales et technologiques), 32 (ensemble du second degré) ; colonnes C-E, H-J, M-O.
- **Où** : script 02 ; rapport § 4, 9 ; H-E1, H-E2, H-E3.
- **Consulté le** : 2026-10-04.

#### DEPP-9 · NI 26.35, apprentis au 31 décembre 2025 (SIFA) : [S] [R] [H]
- **Titre exact** : « L'apprentissage au 31 décembre 2025 : une baisse des effectifs de 2,8 % par rapport à 2024 », *Note d'Information* n° 26.35.
- **Producteur** : DEPP. Auteurs : A. Demongeot, M. Orzoni. Source : enquête SIFA.
- **Publication** : juillet 2026 (page datée du 16/07/2026).
- **URL**, retrouvées et vérifiées le 2026-10-04 :
  - page : <https://www.education.gouv.fr/depp/l-apprentissage-au-31-decembre-2025-une-baisse-des-effectifs-de-28-par-rapport-2024-505299> ;
  - PDF : <https://www.education.gouv.fr/sites/default/files/document/deppni-2026-35sifapdf-519078.pdf> ;
  - données : <https://www.education.gouv.fr/sites/default/files/document/deppni-2026-35sifa-donneesxlsx-519081.xlsx> ;
  - DOI : <https://doi.org/10.48464/ni-26-35>.
- **Fichiers locaux** (archivés le 2026-10-04 après relecture) : `data/raw/effectifs_nationaux/depp_ni_2026-35_apprentissage_31-12-2025.pdf` et `…_donnees.xlsx`.
- **Utilisé** : figure 2, « Répartition et évolution des effectifs d'apprentis par diplôme préparé », ligne « Secondaire, total » : 392 035 (2024) et 391 937 (2025). Ces valeurs sont lues par `scripts/01` dans l'onglet « Figure 2 », cellules C12 et D12 (libellé « Secondaire » et années contrôlés). Elles sont identiques à DEPP-3 (fiches 6.01 et 6.09) et DEPP-4 (série 310608).
- **Où** : script 01 ; rapport § 9 ; H-A3.
- **Consulté le** : 2026-10-04.

### 1.3 Personnels et salaires

#### DEPP-10 · NI 26.36, salaires des enseignants en 2024 : [S] [R] [H]
- **Titre exact** : « L'évolution du salaire des enseignants fonctionnaires ou assimilés entre 2023 et 2024 », *Note d'Information* n° 26.36.
- **Producteur** : DEPP. Auteure : M. Drégoir.
- **Publication** : août 2026 (page datée du 20/08/2026).
- **URL** :
  - page : <https://www.education.gouv.fr/depp/l-evolution-du-salaire-des-enseignants-fonctionnaires-ou-assimiles-entre-2023-et-2024-505401> ;
  - PDF : <https://www.education.gouv.fr/sites/default/files/document/depp-ni-2026-36pdf-519727.pdf> ;
  - données (le nom de fichier « 2026-26-36 » est bien celui du site) : <https://www.education.gouv.fr/sites/default/files/document/depp-ni-2026-26-36-donneesxlsx-519733.xlsx> ;
  - DOI : <https://doi.org/10.48464/ni-26-36>.
- **Fichiers locaux** : `data/raw/couts_personnels/DEPP_NI_26-36_salaire_enseignants_2023-2024.pdf`, `…/DEPP_NI_26-36_donnees.xlsx`, `…/DEPP_NI_26-36_page_web.html`.
- **Utilisé** :
  - onglet « Figure 1 », D4:D8 : salaire net mensuel moyen 2024 (ensemble) des professeurs des écoles (2 850 €), certifiés (3 130 €), EPS (3 180 €), PLP (3 390 €) et agrégés (4 080 €) ;
  - « Figure 6 - Web » (avec une espace finale), H7 : salaire net du 2nd degré, 3 310 € ;
  - « Figure 7 - Web », B6:B7 : effectifs des certifiés et des professeurs d'EPS, pour la pondération.
  - Champ : fonctionnaires ou assimilés, public et privé sous contrat, France hors Mayotte.
- **Où** : script 04 (indices de coût des corps) ; rapport § 9 ; H-B5.
- **Consulté le** : 2026-10-04.

#### DEPP-11 · *Panorama statistique des personnels de l'enseignement scolaire 2025-2026*, chapitre 7 : [S] [R] [H]
- **Titre exact** : *Panorama statistique des personnels de l'enseignement scolaire 2025-2026*, chapitre 7 « Les rémunérations » (données de l'année 2024).
- **Producteur** : DEPP.
- **Publication** : page de l'édition datée du 15/04/2026, avec des chapitres mis en ligne au fil de l'eau ; le PDF du chapitre 7 a été créé le 24/09/2026.
- **URL** :
  - page : <https://www.education.gouv.fr/depp/panorama-statistique-des-personnels-de-l-enseignement-scolaire-2025-2026-504389> ;
  - PDF du chapitre 7 : <https://www.education.gouv.fr/sites/default/files/document/panoramachapitre-7-521089.pdf> ;
  - données du chapitre 7 : <https://www.education.gouv.fr/sites/default/files/document/chapitre-7-les-remunerations-520486.xlsx>.
- **Fichiers locaux** : `data/raw/couts_personnels/DEPP_Panorama_personnels_2025-2026_chapitre7_remunerations.pdf`, `…/DEPP_Panorama_personnels_2025-2026_chapitre7_donnees.xlsx`.
- **Utilisé** : onglet 7.3 (« Salaires bruts et nets mensuels moyens des personnels »), colonne G (salaire net moyen en EQTP). G19 : fonctionnaires et assimilés du 2nd degré, public, 3 450 €. G21 : enseignants contractuels et maîtres délégués, 2 350 €. Le rapport des deux donne l'indice 0,681 des contractuels.
- **Où** : script 04 ; rapport § 9 ; H-B5.
- **Consulté le** : 2026-10-04.

#### DEPP-12 · *Panorama statistique des personnels de l'enseignement scolaire 2024-2025* : [H] [C]
- **Titre exact** : *Panorama statistique des personnels de l'enseignement scolaire 2024-2025*.
- **Producteur** : DEPP.
- **Publication** : septembre 2025 (PDF créé le 22/09/2025).
- **URL** : <https://www.education.gouv.fr/sites/default/files/document/panorama-statistique-des-personnels-de-l-enseignement-scolaire-2024-2025-475342.pdf>
- **Fichier local** : `data/raw/etablissements/DEPP_Panorama_personnels_2024-2025.pdf`.
- **Utilisé** : figure 2.1, p. 32 (ETP d'enseignants au 30/11/2024 : 850 159). Comparé à la somme des ETP de l'open data (758 106), il donne environ 92 000 ETP non rattachés à un établissement (`data/raw/etablissements/NOTES.md`, § 4.2). Figures 2.14 et 2.16 : contrôle par corps.
- **Où** : H-B4 (« environ 92 000 ETP »).
- **Consulté le** : 2026-10-04.

### 1.4 Autres publications DEPP utilisées pour les contrôles et les extractions

| Titre exact (DEPP) | Publication | URL exacte | Fichier local (`data/raw/…`) | Utilisé pour | Consulté |
|---|---|---|---|---|---|
| *L'état de l'École 2025* (n° 35) | 14/11/2025, corrigé le 02/03/2026 | <https://www.education.gouv.fr/sites/default/files/document/l-tat-de-l-cole-2025-478952.pdf> (page : <https://www.education.gouv.fr/depp/l-etat-de-l-ecole-2025-468872>) | `depp_compte_education/depp_etat_de_l_ecole_2025.pdf` (copie identique dans `effectifs_nationaux/`) | p. 98 imprimée : allocations de stage (PFMP) exclues de la DIE [X] (H-B3, via la passerelle G5) ; fiches 9 et 10 | 2026-10-04 |
| *L'Éducation nationale en chiffres 2026* | 25/08/2026 | <https://www.education.gouv.fr/sites/default/files/document/enc-2026pdf-519886.pdf> (page : <https://www.education.gouv.fr/depp/l-education-nationale-en-chiffres-edition-2026-505326>) | `depp_compte_education/depp_education_nationale_en_chiffres_2026.pdf` (copie identique dans `effectifs_nationaux/`) | p. 3 : 10 350 € par élève des 1er et 2nd degrés en 2024p, tous financeurs [C] | 2026-10-04 |
| *Géographie de l'École 2026*, fiche 21 (données) | juin 2026 | <https://www.education.gouv.fr/sites/default/files/document/la-depense-d-education-par-eleve-ou-etudiant-prise-en-charge-par-les-ministeres-charges-de-l.xlsx> | `depp_compte_education/depp_geo_ecole2026_depense_par_eleve_MEN-MESRE_donnees.xlsx` | dépense du MEN par élève en 2023 [C] | 2026-10-04 |
| RERS 2026, fiche 10.01 (données) | 25/08/2026 | <https://rers.depp.education.fr/data/2026/10_BUD/01_DIE/dataExcel.fr.xlsx> | `depp_compte_education/depp_rers2026_10-01_DIE_donnees.xlsx` | DIE par niveau [C] | 2026-10-04 |
| RERS 2025, fiches 10.04 et 10.05 (données 2023p) | août 2025 | <https://rers.depp.education.fr/data/2025/10_BUD/04_PRODEDUC/dataExcel.fr.xlsx> ; <https://rers.depp.education.fr/data/2025/10_BUD/05_DEPEL/dataExcel.fr.xlsx> | `depp_compte_education/depp_rers2025_10-04_…xlsx`, `…_10-05_…xlsx` | comparaison avec l'édition 2026 [C] | 2026-10-04 |
| RERS 2025, chapitre 9 « Les personnels » | 29/07/2025 | <https://www.education.gouv.fr/sites/default/files/2025-07/rers2025-chapitre-9-441738.pdf> | `etablissements/DEPP_RERS2025_chapitre9_personnels.pdf` | fiche 9.01, p. 331 : ETP par mission, rentrée 2024 (localisation des ETP non rattachés, H-B4) [C] | 2026-10-04 |
| RERS 2026, chapitres 2, 4, 7, 9 et 11 | 25/08/2026 | <https://www.education.gouv.fr/sites/default/files/document/2-les-etablissementspdf-519279.pdf> ; <https://www.education.gouv.fr/sites/default/files/document/4-les-eleves-du-second-degrepdf-521305.pdf> ; <https://www.education.gouv.fr/sites/default/files/document/7-les-etudiantspdf-519348.pdf> ; <https://www.education.gouv.fr/sites/default/files/document/9-les-personnelspdf-519300.pdf> ; <https://www.education.gouv.fr/sites/default/files/document/11-la-france-d-outre-merpdf-519306.pdf> | `effectifs_nationaux/rers2026_ch02_…`, `…ch04_…`, `…ch07_…`, `…ch11_…` ; `etablissements/DEPP_RERS2026_chapitre9_personnels.pdf` | contrôle des effectifs (EREA, hors contrat, post-bac, outre-mer) et des ETP par mission [C] | 2026-10-04 |
| NI 24.41, 24.42, 23.50, 23.51 (effectifs des rentrées 2023 et 2024) | 2023-2024 | <https://www.education.gouv.fr/sites/default/files/document/depp-ni-2024-41-403569.pdf> ; <https://www.education.gouv.fr/sites/default/files/document/depp-ni-2024-42-403563.pdf> ; <https://www.education.gouv.fr/media/159297/download> ; <https://www.education.gouv.fr/media/159288/download> (données : voir `effectifs_nationaux/SOURCES.md`) | `effectifs_nationaux/depp_ni_2024-41_…`, `…2024-42_…`, `…2023-50_…`, `…2023-51_…` | contrôle des révisions [C] | 2026-10-04 |
| *L'état de l'École 2025*, données des fiches 1 à 4, 9 et 10 | 14/11/2025 | <https://www.education.gouv.fr/sites/default/files/document/la-scolarisation-dans-le-premier-degr--480608.xlsx> ; …/474610.xlsx ; …/474613.xlsx ; …/474616.xlsx ; …/474631.xlsx ; …/474634.xlsx (préfixe `https://www.education.gouv.fr/sites/default/files/document/`) | `effectifs_nationaux/depp_etat_ecole_2025_fiche0*.xlsx`, `depp_compte_education/depp_ede2025_fiche09_…`, `…fiche10_…` | contrôle [C] | 2026-10-04 |
| NI 24.45 « En 2023, 189,9 milliards d'euros consacrés à l'éducation, soit 6,7 % du PIB » | novembre 2024 | <https://archives-statistiques-depp.education.gouv.fr/default/digitalCollection/DigitalCollectionAttachmentDownloadHandler.ashx?parentDocumentId=55863&documentId=55864&skipWatermark=true&skipCopyright=true> | `budget_etat/depp_ni_2024-45_compte_education_2023.pdf` | définition de l'État financeur [X] (passerelle G5) | 2026-10-04 |
| Document de travail n° 2024-E08 « Le financement de l'éducation en 2023 » | septembre 2024 | <https://www.education.gouv.fr/sites/default/files/document/DT2024-E08-403287.pdf> | `budget_etat/depp_DT2024-E08_financement_education_2023.pdf` | périmètre de l'État [X] (passerelle G5) | 2026-10-04 |
| NI 19.07 « La dépense d'éducation des collectivités territoriales : 36,2 milliards d'euros en 2017 » (et données) | mars 2019 | <https://www.education.gouv.fr/sites/default/files/document/T%C3%A9l%C3%A9charger%20la%20version%20imprimable%20au%20format%20PDF-246936.pdf> ; <https://www.education.gouv.fr/sites/default/files/document/T%C3%A9l%C3%A9charger%20les%20donn%C3%A9es%20au%20format%20XLS-246939.xls> | `collectivites/DEPP_NI_19-07_…pdf`, `…_donnees.xls` | méthode « communes » de la DEPP [X] (G3, H-B8) | 2026-10-04 |

---

## 2. data.education.gouv.fr (open data par établissement)

- **Producteurs** : DEPP (« DEPP – Ministère chargé de l'éducation nationale ») pour les effectifs, les personnels, les moyens d'enseignement et l'IPS ; DNE pour l'annuaire ; DGESCO pour l'éducation prioritaire. Licence Ouverte v2.0 (Etalab).
- **Page d'un jeu** : `https://data.education.gouv.fr/explore/dataset/<identifiant>/information/`.
- **Exports** : préfixe `https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/`, suivi de l'identifiant et de la requête du tableau. Le 2026-10-04, chaque export lu par un script a été relancé : le fichier obtenu est identique octet pour octet au fichier local, sauf l'annuaire (même contenu, ordre des lignes différent).
- **Fichiers locaux** : `data/raw/etablissements/` ; métadonnées dans `data/raw/etablissements/_metadata/<identifiant>.json`.
- **Consultés le** : 2026-10-04.

| Identifiant · titre exact | Mise à jour du jeu | Requête d'export (après le préfixe) | Fichier(s) local(aux) | Ce qui est utilisé | Où |
|---|---|---|---|---|---|
| `fr-en-ecoles-effectifs-nb_classes` · « Effectifs d'élèves par école » | 27/08/2026 | `fr-en-ecoles-effectifs-nb_classes/exports/csv?delimiter=%3B&where=year(rentree_scolaire)%3D2024` (et `%3D2025`) | `effectifs_ecoles_1d_rentree2024.csv`, `…2025.csv` | élèves par niveau (préélémentaire, élémentaire, ULIS, UEEA), classes, secteur, académie, `rep`, `rep_plus` ; la colonne `code_commune_insee` contient en réalité le code postal | scripts 02, 03 ; H-E3, H-E4, H-B9, anomalie 3 |
| `fr-en-college-effectifs-niveau-sexe-lv` · « Effectifs d'élèves en collège » | 27/07/2026 | `…/exports/csv?delimiter=%3B&where=year(rentree_scolaire)%3D2024` (et 2025) | `effectifs_colleges_rentree2024.csv`, `…2025.csv` | `nombre_eleves_total` (Segpa et ULIS comprises), `nombre_d_eleves_total_segpa`, `rep`, `rep0` (= REP+) | scripts 02, 03 |
| `fr-en-lycee_gt-effectifs-niveau-sexe-lv` · « Effectifs d'élèves en lycée d'enseignement général et technologique » | 27/07/2026 | idem (2024 et 2025) | `effectifs_lycees_gt_rentree2024.csv`, `…2025.csv` | `nombre_d_eleves` | scripts 02, 03 |
| `fr-en-lycee_pro-effectifs-niveau-sexe-lv` · « Effectifs d'élèves en lycée professionnel » | 27/07/2026 | idem (2024 et 2025) | `effectifs_lycees_pro_rentree2024.csv`, `…2025.csv` | `nombre_d_eleves` | scripts 02, 03 |
| `fr-en-indicateurs_personnels_etablissements1d` · « Les personnels dans les établissements du premier degré » | 24/06/2026 | `…/exports/csv?delimiter=%3B&where=annee_de_la_rentree_scolaire%3D%222024%22` | `personnels_1d_rentree2024.csv` (2025 : contrôle) | `etp_d_enseignants_hommes_et_femmes` par école | script 03 ; H-B4 |
| `fr-en-indicateurs_personnels_etablissements2d` · « Les personnels dans les établissements du second degré » | 23/07/2026 (seule la rentrée 2024 est publiée) | idem, `%222024%22` | `personnels_2d_rentree2024.csv` | `etp_total`, `etp_enseignants_hommes_et_femmes`, `etp_de_personnels_de_vie_scolaire`, ETP par corps (agrégés, certifiés et PEPS, PLP, autres titulaires, non-titulaires), `nature_de_l_etablissement` | script 03 ; H-B1, H-B4, H-B5, H-B7 |
| `fr-en-moyens_enseignants_2d_public` · « Indicateurs d'encadrement H/E et E/S à la rentrée dans le secteur public » | 09/06/2026 | `…/exports/csv?delimiter=%3B&where=year(annee)%3D2024` | `moyens_enseignants_2d_public_rentree2024.csv` | `numerateur_h_e_nb_heures_enseignement_hebdo_devant_eleves`, `denominateur_h_e_somme_eleves_en_division`, par `uai` et `niveau` | scripts 03, 04, 07 ; H-B4, H-B6, H-B11, H-B18 |
| `fr-en-moyens_enseignants_2d_prive` · « Indicateurs d'encadrement H/E et E/S à la rentrée dans le secteur privé sous contrat » | 09/06/2026 | idem | `moyens_enseignants_2d_prive_rentree2024.csv` | idem | scripts 03, 04, 07 ; H-B18 |
| `fr-en-ips-ecoles-ap2022` · « Indices de position sociale des écoles (à partir de 2022) » (jeu qui n'est plus actualisé) | 07/08/2026 | `…/exports/csv?delimiter=%3B&where=rentree_scolaire%3D%222024-2025%22` | `ips_ecoles_2024-2025.csv` | `ips`, `code_insee_de_la_commune`. D'après les métadonnées, l'IPS n'est calculé que sur les élèves de CM2, pour les écoles ayant eu au moins 25 élèves de CM2 sur cinq ans | script 03 ; H-E4, H-B15 |
| `fr-en-ips-colleges-ap2023` · « Indices de position sociale des collèges (à partir de 2023) » | 01/09/2026 | idem, `%222024-2025%22` | `ips_colleges_2024-2025.csv` | `ips` | script 03 ; H-B15 |
| `fr-en-ips-lycees-ap2023` · « Indices de position sociale des lycées (à partir de 2023) » | 10/06/2026 | idem | `ips_lycees_2024-2025.csv` | `ips_etab` | script 03 ; H-B15 |
| `fr-en-ips-erea-ap2022` · « Indices de position sociale des EREA (à partir de 2022) » | 03/08/2026 | idem, `%222024-2025%22` | `ips_erea_2024-2025.csv` | `uai`, `ips` (fiche des EREA de la carte) | script 07 ; H-B18 |
| `fr-en-annuaire-education` · « Annuaire de l'éducation » (DNE) | quotidienne (03/10/2026) | `fr-en-annuaire-education/exports/csv?delimiter=%3B` (export complet) | `annuaire_education_extrait_2026-10-04.csv` | `identifiant_de_l_etablissement` → `code_commune` ; pour la carte des établissements : `latitude`, `longitude`, `precision_localisation`, `nom_etablissement`, `type_etablissement`, `nom_commune`, `ecole_maternelle`, `ecole_elementaire`, `type_contrat_prive` | scripts 03, 07 ; H-E4, H-B18 |

Jeux consultés pour contrôle [C] : `fr-en-etablissements-ep` (« Etablissements de l'éducation prioritaire », DGESCO, 02/02/2026) ; `fr-en-cites_scolaires` (« Liste des cités scolaires », 03/10/2026) ; `fr-en-mode-hebergement-eleves-etablissements-2d` (« Le mode d'hébergement des élèves dans les établissements du second degré », 05/08/2026) ; `fr-en-budget-missions` (DAF, « Le budget : missions interministérielles "Enseignement scolaire" et "Recherche et enseignement supérieur" », 29/01/2026, inutilisable après 2020). Leurs requêtes figurent dans `data/raw/etablissements/SOURCES.md`.

Extraits du même portail rangés dans `data/raw/collectivites/` [X] (couverture communale, G3) : `MEN_effectifs_par_ecole_rentrees2024-2025_extrait_API.csv`, `MEN_effectifs_par_ecole_rentrees2024-2025_libelles_communes_API.csv` et `MEN_annuaire_education_ecoles_UAI_commune_extrait_API.csv`. Leurs URL exactes, vérifiées octet pour octet, sont en annexe A.4.

---

## 3. Budget de l'État

`budget.gouv.fr` refuse les téléchargements automatisés (protection anti-robot). Les annexes budgétaires ont donc été prises sur le site de l'Assemblée nationale, qui publie les documents officiels déposés avec les projets de loi.

#### BUD-1 · RAP 2025, mission « Enseignement scolaire » : [X → S] [R] [H]
- **Titre exact** : *Rapport annuel de performances 2025*, mission interministérielle « Enseignement scolaire ». Annexe au projet de loi relatif aux résultats de la gestion et portant approbation des comptes de l'année 2025 (PLRG 2025, n° 2694).
- **Producteur** : Gouvernement : Direction du budget, ministère de l'Éducation nationale, ministère de l'Agriculture (P143).
- **Publication** : avril 2026 (PDF du 20/04/2026 ; projet de loi déposé le 22/04/2026).
- **URL** (copie officielle de l'Assemblée nationale) : <https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1109849/file/Enseignement_scolaire_EC.pdf>. Version budget.gouv.fr : non vérifiable (accès automatisé bloqué).
- **Fichiers locaux** : `data/raw/budget_etat/RAP2025_Enseignement_scolaire_EC.pdf` (copie identique : `data/raw/couts_personnels/RAP2025_mission_Enseignement_scolaire_AN.pdf`).
- **Utilisé** :
  - p. 22-24 : exécution 2024 et 2025 par programme et action (extraction du § 9, lue par les scripts 04 et 05) ;
  - p. 50 : ETPT des actions 01-03 du P140, soit 275 005,78 ;
  - p. 51, 105, 160, 221 et 280 : CAS Pensions, taux de 78,28 % (pensions civiles) et 0,32 % (ATI) ;
  - p. 116 : PFMP du P141, 208 000 000 € ;
  - p. 230 : PFMP du P139, 54 763 935 € ;
  - p. 156 et 168 : AED, 8 857,83 ETPT (tableau des emplois) et 8 731 ETPT (texte) ; subventions de 1 411 836 656 € et dépense de l'État de 1 413 417 331 € ;
  - P143 : 1 688,3 M€ exécutés.
- **Où** : scripts 04 et 05, via `rap2025_execution_par_action_2024_2025.csv`, `passerelle_G5_intrants_RAP_DPT_2024_2025.csv` et `TRANSCRIPTION_titre2_par_programme_CAS_Pensions.csv` ; rapport § 4, 9 ; hypothèses § 0, H-G6, H-B2, H-B3, H-B4, H-B7, H-C3, H-D1, anomalies 4 et 5.
- **Consulté le** : 2026-10-04.

#### BUD-2 · DPT « Outre-mer » 2026 : [X → S] [R] [H]
- **Titre exact** : *Document de politique transversale « Outre-mer »*, annexe au projet de loi de finances pour 2026.
- **Producteur** : Gouvernement (ministère chargé des outre-mer, Direction du budget).
- **Publication** : octobre 2025 (PDF du 22/10/2025).
- **URL** (copie de l'Assemblée nationale) : <https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1090079/file/4-DPT2026_OutreMer.pdf>
- **Fichier local** : `data/raw/budget_etat/DPT2026_Outre-mer_annexe_PLF2026.pdf`.
- **Utilisé** : annexe « Effort budgétaire et financier de l'État dans les outre-mer ». Synthèse p. 229-231 ; tableaux par territoire p. 232-277 : MIES par programme, exécution 2024. Les COM totalisent 1 160 639 707 € (p. 248-277), et les montants sont repris par programme dans la passerelle G5.
- **Où** : script 04 (via la passerelle G5) ; rapport § 9 ; H-G1, H-B2.
- **Consulté le** : 2026-10-04.

#### BUD-3 · Données du PLRG 2025 (data.economie.gouv.fr) : [X] [R] [H]
- **Titre exact** : « Projet de loi relatif aux résultats de la gestion et portant approbation des comptes de l'année (PLRG) 2025 », jeu de données.
- **Producteur** : DGFiP et Direction du budget.
- **Publication** : 2026.
- **URL** :
  - page du jeu : <https://data.economie.gouv.fr/explore/dataset/projet-de-loi-relatif-aux-resultats-de-la-gestion-et-portant-approbation-des-comptes-de-lannee-plrg-2025/> ;
  - pièces jointes : préfixe `https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/projet-de-loi-relatif-aux-resultats-de-la-gestion-et-portant-approbation-des-comptes-de-lannee-plrg-2025/attachments/`, suivi de `listdepfisc_plrn_2025csv`, `annexe1_etat_titre_cat_2025csv`, `annexe1_etat_cp_2025csv`, `annexe1_etat_ae_cp_2025csv`, `annexe1_etat_recettes_2025csv`, `annexe1_etat_fdc_adp_2025csv` ou `notices_par_fichierzip`.
- **Fichiers locaux** : `data/raw/budget_etat/PLRG2025_*.csv` et `PLRG2025_Notices_par_fichier.zip`.
- **Utilisé** : `PLRG2025_ListDepFisc-PLRN-2025.csv`, ligne 110215 « Réduction d'impôt pour frais de scolarité dans l'enseignement secondaire » : 221 M€ (2024 définitif), 224 M€ (2025 initial), 229 M€ (2025 actualisé). Recoupé par la NEB 2025, tableau 29, p. 69 (CDC-3). Les annexes 1 servent aux transferts par catégorie (extractions du § 9).
- **Où** : rapport § 8 (229 M€) ; H-G8.
- **Consulté le** : 2026-10-04.

#### BUD-4 · Taux de contribution au CAS « Pensions » (textes réglementaires) : [R] [H]
- **Décret n° 2025-61 du 22 janvier 2025 relevant le taux de la contribution employeur due au compte d'affectation spéciale « Pensions » au titre des fonctionnaires civils de l'Etat et des magistrats**, JORF n° 0019 du 23/01/2025 (Légifrance, DILA) : <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000051020776>. Utilisé : art. 1 et 2, taux porté de 74,28 % à 78,28 % au 1er janvier 2025. Fichier local : `data/raw/couts_personnels/Legifrance_decret_2025-61_du_22-01-2025.html`.
- **Décret n° 2012-1507 du 27 décembre 2012 portant fixation du taux de la contribution employeur due pour la couverture des charges de pension des fonctionnaires de l'Etat, des militaires et des magistrats ainsi que du taux de la contribution employeur versée au titre du financement des allocations temporaires d'invalidité des fonctionnaires de l'Etat et des magistrats** (version consolidée en vigueur au 01/01/2026) : <https://www.legifrance.gouv.fr/loda/id/JORFTEXT000026856494>. Utilisé : art. 3, ATI de 0,32 %. Fichier local : `data/raw/couts_personnels/Legifrance_decret_2012-1507_consolide_2026-10-04.html`.
- **Décret n° 2025-1341 du 26 décembre 2025** (taux porté de 78,28 % à 82,28 % au 1er janvier 2026), <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053175170>. Fichier local : `data/raw/couts_personnels/Legifrance_decret_2025-1341_du_26-12-2025.html`.
- **Où** : H-G6 (78,28 % + 0,32 %, 74,28 %, 82,28 %), H-C3 (78,6 %), rapport § 2 (lexique, 78,6 %), § 4 (78,6 %, écart public / privé) et § 8 (78,28 %, 78,6 %, 74,28 %, 82,28 %), script 05 (`TAUX_CAS`).
- **Consulté le** : 2026-10-04.

#### BUD-5 · « Jaune » Formation professionnelle, PLF 2026 (partie Dares) : [H] [X]
- **Titre exact** : *Annexe au projet de loi de finances pour 2026 : Formation professionnelle* (« jaune »).
- **Producteur** : Gouvernement (DGEFP, Dares, DGAFP, France compétences…).
- **Publication** : octobre 2025 (PDF créé le 21/10/2025).
- **URL** (copie de l'Assemblée nationale) : <https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1089989/file/7-Jaune2026_Formation_Professionnelle.pdf>
- **Fichier local** : `data/raw/depp_compte_education/jaune_PLF2026_formation_professionnelle_AN.pdf`.
- **Utilisé** :
  - partie 2 (Dares, dépense nationale par financeur final, 2024p), tableau 3, p. 35 (PDF) : 16,03 Md€ pour les apprentis, dont OPCO 8,71 Md€, État 6,33 Md€, régions 0,25 Md€ ;
  - tableaux 5 à 7, p. 39-43 ;
  - budget de France compétences, p. 65-66.
- **Où** : H-A3 (« Dares »), via `_derive_G4_part_publique_apprentissage_2nd_degre.csv`.
- **Consulté le** : 2026-10-04.

#### BUD-6 · RAP 2024, mission « Enseignement scolaire » : [X]
- **Titre exact** : *Rapport annuel de performances 2024*, mission « Enseignement scolaire » (annexe au PLRG 2024).
- **Producteur** : Gouvernement (Direction du budget, MEN, MAASA).
- **Publication** : avril 2025 (PDF du 15/04/2025).
- **URL** : <https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/906949/file/Enseignement_scolaire.pdf>
- **Fichiers locaux** : `data/raw/budget_etat/RAP2024_Enseignement_scolaire.pdf` (copie identique dans `couts_personnels/`).
- **Utilisé** : PFMP 2024 (p. 124, 234-235, 410), MEEF (p. 134, 182, 243), pour le calage 2024 de la passerelle G5 ; taux CAS 2024 (74,28 %).
- **Consulté le** : 2026-10-04.

**Autres documents budgétaires [C]** (prévisions, transferts hors mission, contrôle), tous consultés le 2026-10-04 :

| Titre exact | Producteur, date | URL exacte | Fichier local (`data/raw/…`) | Utilisé pour |
|---|---|---|---|---|
| *Rapport sur les pensions de retraite de la fonction publique*, annexe (jaune) au PLF 2026 | Direction du budget, DGAFP, SRE, CDC ; octobre 2025 | <https://www.assemblee-nationale.fr/dyn/contenu/visualisation/1090002/file/12-Jaune2026_Pensions.pdf> | `couts_personnels/Jaune_PLF2026_Rapport_pensions_retraite_fonction_publique_AN.pdf` | p. 13-14 : rôle d'équilibrage du taux du CAS ; p. 49 : assiette (H-G6, « taux d'équilibre ») |
| PAP 2027, compte d'affectation spéciale « Pensions » | Gouvernement ; 01/10/2026 | <https://www.assemblee-nationale.fr/dyn/contenu/visualisation/1128300/file/PAP%202027%20-%20Pensions.pdf> | `couts_personnels/PAP2027_CAS_Pensions_AN.pdf` | p. 17-19 : taux et assiette de l'ATI |
| PAP 2026 et PAP 2027, mission « Enseignement scolaire » | Gouvernement ; 13/10/2025 et 01/10/2026 | <https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1087978/file/PAP2026_BG_Enseignement_scolaire_EC.pdf> ; <https://www.assemblee-nationale.fr/dyn/contenu/visualisation/1128234/file/PAP%202027%20-%20Enseignement%20scolaire.pdf> | `budget_etat/PAP2026_…`, `budget_etat/PAP2027_…` (copies dans `couts_personnels/`) | prévisions 2026-2027, coûts moyens (transcriptions du § 9) |
| Projet de loi de finances pour 2027, n° 3210 | Gouvernement, Assemblée nationale ; 01/10/2026 | <https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf> | `budget_etat/PLF2027_projet_de_loi_AN_n3210.pdf` | état B, prélèvements sur recettes |
| Loi n° 2026-103 du 19 février 2026 de finances pour 2026 | Légifrance ; JO du 20/02/2026 | <https://www.legifrance.gouv.fr/loda/id/JORFTEXT000053508155/> | `budget_etat/LFI2026_loi_2026-103_du_19-02-2026_Legifrance.html` | état B |
| « Budget 2027 pour l'École », dossier de presse | MEN ; 01/10/2026 | <https://www.education.gouv.fr/sites/default/files/document/budget-2027-pour-l-cole-le-dossier-de-presse-521314.pdf> | `budget_etat/MEN_Budget2027_dossier_de_presse_PLF2027.pdf` | contexte |
| RAP 2025 des missions « Relations avec les collectivités territoriales », « Solidarité, insertion et égalité des chances », « Cohésion des territoires », « Outre-mer » | Gouvernement ; avril 2026 | <https://www.assemblee-nationale.fr/dyn/contenu/visualisation/1109928/file/Relations_collectivites_territoriales_RC.pdf> ; <https://www.assemblee-nationale.fr/dyn/contenu/visualisation/1109937/file/Solidarite_insertion_egalite_chances_SE.pdf> ; <https://www.assemblee-nationale.fr/dyn/contenu/visualisation/1109813/file/Cohesion_territoires_VA.pdf> ; <https://www.assemblee-nationale.fr/dyn/contenu/visualisation/1109900/file/Outre-mer_OA.pdf> | `budget_etat/RAP2025_*.pdf` | transferts de l'État hors mission (extraction `autres_depenses_etat_hors_mission.csv`) |
| Exécution du budget de l'État 2013 en AE et CP (PLR 2013) | DGFiP, Direction du budget ; data.economie.gouv.fr | <https://data.economie.gouv.fr/explore/dataset/execution-2013-du-budget-de-letat-en-cp-et-ae-/> | `budget_etat/PLR2013_execution_CP_mission_programme_action_titre.csv` | calage 2013 de la passerelle G5 |
| « Les dotations de soutien à l'investissement des collectivités territoriales en 2024 » | DGCL ; 01/10/2025 | voir annexe A.4 | `budget_etat/DGCL_bilan_dotations_investissement_2024.pdf` | subventions scolaires DETR/DSIL |
| Page « Les établissements publics nationaux ou organismes publics dotés de l'autonomie financière » | Service des retraites de l'État ; version du 04/10/2026 | <https://retraitesdeletat.gouv.fr/professionnels/le-versement-des-cotisations/les-etablissements-publics-nationaux-ou-organismes> | `couts_personnels/SRE_retraitesdeletat_taux_cotisations_EPN_2026-10-04.html` | assiette et taux du CAS |

---

## 4. Collectivités territoriales (DGFiP, DGCL, OFGL, collectivités)

#### COL-1 · DGFiP, balances comptables 2025, présentation croisée nature × fonction : [S] [X] [R] [H]
- **Titre exact** : « Balances comptables des collectivités et des établissements publics locaux avec la présentation croisée nature-fonction 2025 ».
- **Producteur** : DGFiP, sur data.economie.gouv.fr.
- **Publication** : jeu mis à jour le 13/07/2026 (balances définitives « DEF », 5 326 293 lignes).
- **URL** :
  - page du jeu : <https://data.economie.gouv.fr/explore/dataset/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/> ;
  - notice (pièce jointe, datée d'octobre 2018) : <https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/attachments/notice_balance_fonctionnelle_pdf> ;
  - exports agrégés : les 7 requêtes exactes sont en **annexe A.1**. Chacune a été relancée le 2026-10-04 et redonne le fichier local à l'octet près.
- **Fichiers locaux** (`data/raw/collectivites/`) :
  - `DGFiP_balances_nature-fonction_2025_communes_ecoles_fonct_par_commune_API.csv` (A.1-1), lu par le script 04 ;
  - `…_fonction2_et_81_agrege_API.csv` (A.1-3), source des extractions lues par les scripts 04 et 05 ;
  - `…_communes_ecoles_invest_par_commune_API.csv`, `…_communes_BP_toutes_fonctions_agrege_API.csv`, `…_communes_BP_total_toutes_fonctions_fonct_par_commune_API.csv`, `…_invest_par_commune_API.csv`, `…_GFP_ecoles_par_GFP_et_compte_API.csv` (G3) ;
  - `DGFiP_Notice_balance_fonctionnelle_2025.pdf`, `DGFiP_Structure_fichier_balance_fonction_2024.ods`.
- **Utilisé** :
  - dépense de fonctionnement « écoles » par commune (fonctions 20, 21x, 28x, 29 ; comptes 6 hors 66, 675, 676 et 68 ; opérations réelles = opérations nettes − opérations d'ordre), pour la clé communale (H-B9) ;
  - dépenses 2025 des départements, des régions et des CTU pour les collèges et les lycées, dont les dotations au privé (comptes 655112 et 655122), pour H-B10 ;
  - structure par nature des dépenses, pour H-D2.
- **Où** : script 04 ; scripts 04 et 05 via les extractions du § 9 ; rapport § 4, 9 ; hypothèses § 0, H-B8, H-B9, H-B10, H-D2.
- **Consulté le** : 2026-10-04.

#### COL-2 · DGCL, *Les collectivités locales en chiffres 2026* : [R] [X]
- **Titre exact** : *Les collectivités locales en chiffres 2026* ; en particulier le fichier « 4F – Ventilation fonctionnelle des dépenses, comptes de gestion 2025 » du chapitre 4 « Les finances des collectivités locales ».
- **Producteur** : DGCL, Département des études et des statistiques locales (DESL), ministère chargé des collectivités territoriales.
- **Publication** : édition 2026. Le chapitre 4 est indiqué comme mis à jour en septembre 2026 ; le fichier 4F porte la date Last-Modified du 24/06/2026.
- **URL** :
  - page : <https://www.collectivites-locales.gouv.fr/les-collectivites-locales-en-chiffres-2026> ;
  - 4F : <https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/DESL/2026/CLC/4F%20-%20Ventilation%20fonctionnelle%20CG25.xlsx> ;
  - autres fichiers (chapitres 3, 4, 4A, 6, 10) : même préfixe, voir `data/raw/collectivites/SOURCES.md` § 1.
- **Fichiers locaux** : `data/raw/collectivites/DGCL_CLC2026_4F_Ventilation_fonctionnelle_CG25.xlsx` et `DGCL_CLC2026_*` ; page : `DGCL_CLC2026_page_web.html`.
- **Utilisé** : onglets F1 à F6 (fonction « Enseignement, formation et apprentissage » et transports scolaires, 2024-2025 ; champ : communes de 3 500 habitants ou plus). Ces données servent de contrôle des agrégats DGFiP et entrent dans le tableau de passage G3. L'onglet F4, ligne 19 (apprentissage des régions, 251,2 M€) sert au contexte de H-A3.
- **Où** : rapport § 9 ; hypothèses § 0 (comptes par fonction des communes de 3 500 habitants ou plus) et H-B8 (via G3).
- **Consulté le** : 2026-10-04.

#### COL-3 · Région Centre-Val de Loire, dotations de fonctionnement aux lycées 2025 : [R]
- **Titre exact** : « Dotations de fonctionnement versées aux lycées de la Région Centre-Val de Loire en 2025 ».
- **Producteur** : Région Centre-Val de Loire (licence ODbL).
- **Publication** : 27/01/2026.
- **URL** :
  - export : <https://data.centrevaldeloire.fr/api/explore/v2.1/catalog/datasets/dotations-de-fonctionnement-versees-aux-lycees-de-la-region-centre-val-de-loire-en-2025/exports/csv?delimiter=%3B> ;
  - fiche : <https://www.data.gouv.fr/datasets/dotations-de-fonctionnement-versees-aux-lycees-de-la-region-centre-val-de-loire-en-2025>.
- **Fichiers locaux** : `data/raw/etablissements/RegionCVL_dotations_fonctionnement_lycees_2025.csv` ; `data/raw/collectivites/RegionCVL_dotations_fonctionnement_lycees_2025.csv` (export `?use_labels=true`).
- **Utilisé** : exemple de données publiques de dépense par établissement (98 lycées publics, 37,4 M€).
- **Où** : rapport § 4 (« Les rares exceptions… »).
- **Consulté le** : 2026-10-04.

**OFGL et autres sources sur les collectivités [X] [C]**, toutes consultées le 2026-10-04 :

| Titre exact | Producteur, date | URL exacte | Fichier local (`data/raw/collectivites/…`) | Utilisé pour |
|---|---|---|---|---|
| *Les finances des collectivités locales en 2026*, rapport complet | OFGL ; Last-Modified 25/08/2026 | <https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/2026/Rapport%20OFGL%202026%20complet%20V24ao%C3%BBt2026.pdf> | `OFGL_Rapport2026_complet_V24aout2026.pdf` | annexe 7A, p. 211 (caisses des écoles) ; annexe 8, tableau 6, p. 220 (redevances périscolaires) → G3 [X] |
| « Comptes des communes 2018-2025 » (extraction 2025 : population, EPCI, dépenses) | OFGL, data.ofgl.fr ; jeu modifié le 29/07/2026 | voir annexe A.4 (vérifiée octet pour octet) | `OFGL_base_communes_2025_BP_population_EPCI_depenses_API.csv` | extrapolation aux petites communes → G3 [X] |
| « Nomenclatures budgétaires » (M57, 2025) | OFGL, data.ofgl.fr ; 28/03/2024 | <https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/nomenclatures-budgetaires/exports/csv?delimiter=%3B&where=nomenclature%3D%22M57%22%20and%20year(annee)%3D2025&select=annee,nomenclature,numero_compte,libelle_compte,chemin> | `OFGL_nomenclature_M57_2025_libelles_comptes.csv` | libellés des comptes des extractions DGFiP [X] |
| « Comptes des départements 2012-2025 – présentation fonctionnelle » | OFGL ; 05/08/2026 | <https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/ofgl-base-departements-fonctionnelle/exports/csv?delimiter=%3B&where=startswith(fonction%2C%222%22)%20and%20exer%3E%3Ddate%272022%27> | `OFGL_departements_fonctionnelle_fonction2_2022-2025.csv` | contrôle des collèges [C] |
| Rapport OFGL 2026, annexe 2F « Ventilation fonctionnelle 2020-2025 » (identique au fichier 4F de la DGCL) | OFGL ; 06/07/2026 | <https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/pre%20rapport%202026/Annexe%202F%20-%20Ventilation%20fonctionnelle%202020-2025.xlsx> | `OFGL_Rapport2026_Annexe2F_Ventilation_fonctionnelle_2020-2025.xlsx` | contrôle [C] |
| *Cap sur…* n° 21 « Les investissements scolaires des collectivités locales » ; *Cap sur…* n° 10 « Les coûts locaux de l'éducation, enseignement et périscolaire » | OFGL ; octobre 2023 et novembre 2019 | <https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/Les%20chantiers%20de%20l'OFGL/OFGL_cap_sur_21_investissements_scolaires_collectivites_30-10-2023.pdf> ; <https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/Cap%20sur/ofgl_num10_cap_sur_cout_enseignement_nov19_0.pdf> | `OFGL_CapSur21_…pdf`, `OFGL_CapSur10_…pdf` | contexte [C] |
| *Dossier : bilan du mandat communal et intercommunal 2020-2025* | OFGL, DGCL ; juillet 2026 | <https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/rapport%202026/dossier%202026%20Bilan%20de%20mandat_VF%20juillet%202026.pdf> | `OFGL_dossier_2026_Bilan_mandat_communal_intercommunal_2020-2025_juillet2026.pdf` | p. 13 : recettes tarifaires du périscolaire [C] |
| Code officiel géographique au 1er janvier 2026 | Insee ; 2026 | voir INSEE-5 | `INSEE_COG2026_*` | appariement des écoles aux communes → G3 [X] |

---

## 5. INSEE

#### INSEE-1 · Comptes de la Nation 2024 : dépenses des APU par fonction (COFOG), tableaux 3.301 et 3.307 : [S] [R] [H]
- **Titres exacts** :
  - « 3.307 – Répartition par sous-secteur des dépenses consolidées des administrations publiques ventilées par fonction » ;
  - « 3.301 – Dépenses des administrations publiques (S13) ventilées par fonction ».
  - Les deux tableaux appartiennent à la publication « Dépenses des administrations publiques ventilées par fonction en 2024 – Les comptes de la Nation en 2024 » (comptes nationaux annuels, base 2020).
- **Producteur** : Insee.
- **Publication** : section parue le 27/03/2026 (fichiers créés le 28/11/2025). Les données 2024 sont provisoires ; les tableaux 2025 sont annoncés pour décembre 2026.
- **URL** :
  - page : <https://www.insee.fr/fr/statistiques/8574707?sommaire=8574832> ;
  - <https://www.insee.fr/fr/statistiques/fichier/8574707/T_3307.xlsx> ;
  - <https://www.insee.fr/fr/statistiques/fichier/8574707/T_3301.xlsx> ;
  - tableaux 3.302 à 3.306 : même préfixe, contrôle.
- **Fichiers locaux** : `data/raw/recoupements/insee_cofog2024_T_3307.xlsx`, `…_T_3301.xlsx` (et `T_3302` à `T_3306`) ; page : `insee_page_COFOG2024_comptes_nation_2024_8574707.html`.
- **Utilisé** : onglet `T_3307`, colonne T (2024), lignes S13 : T68 (09.1 = 42,176 Md€), T69 (09.2 = 63,779), T72 (09.5), T73 (09.6 = 20,023), T75 (09.8 = 0,575). Les valeurs sont identiques à `T_3301` (colonne AH).
- **Où** : script 05 (C1) ; rapport § 6, 9 ; hypothèses § 0, H-C1.
- **Consulté le** : 2026-10-04.

#### INSEE-2 · Fiche méthodologique n° 20, ventilation fonctionnelle en base 2020 : [H]
- **Titre exact** : « La ventilation fonctionnelle des dépenses des administrations publiques en base 2020 » (fiche méthodologique n° 20).
- **Producteur** : Insee. **Publication** : janvier 2025.
- **URL** : <https://www.insee.fr/fr/metadonnees/source/fichier/Note_base20_cofog.pdf>
- **Fichier local** : `data/raw/recoupements/insee_fiche_methodo20_cofog_base2020.pdf`.
- **Utilisé** : p. 3 : les OPCO sont classés en fonction 04.1 et le crédit d'impôt apprentissage en 09.3. p. 4 : ventilation des rémunérations de l'État à partir des RAP.
- **Où** : H-C1. **Consulté le** : 2026-10-04.

#### INSEE-3 · Liste des organismes divers d'administration centrale (ODAC), champ 2024 : [H] [X]
- **Titre exact** : « Liste des organismes divers d'administration centrale (ODAC) », comptes de la Nation 2025 (champ 2024).
- **Producteur** : Insee. **Publication** : mai 2026 (PDF créé le 18/05/2026).
- **URL** : <https://www.insee.fr/fr/statistiques/fichier/8988934/Liste_ODAC_SD2024.pdf>
- **Fichier local** : `data/raw/depp_compte_education/insee_liste_ODAC_SD2024_mai2026.pdf`.
- **Utilisé** : p. 4-5, « Fonction 4 : Affaires économiques » : France compétences et les 11 OPCO.
- **Où** : H-C1 ; NOTES (depp_compte_education) § 12.4. **Consulté le** : 2026-10-04.

#### INSEE-4 · Comptes de la Nation 2025 : page COFOG 2025 : [C]
- **Titre exact** : « Dépenses des administrations publiques ventilées par fonction en 2025 – Les comptes de la Nation en 2025 ».
- **Producteur** : Insee. **Publication** : 29/05/2026.
- **URL** : <https://www.insee.fr/fr/statistiques/8988847?sommaire=8988934>
- **Fichier local** : `data/raw/recoupements/insee_page_COFOG2025_comptes_nation_2025_8988847.html`.
- **Utilisé** : annonce de la publication des tableaux 3.301 à 3.307 pour 2025 en décembre 2026 (c'est pourquoi 2024 est la dernière année COFOG utilisée).
- **Consulté le** : 2026-10-04.

#### INSEE-5 · Code officiel géographique au 1er janvier 2026 : [X]
- **Titre exact** : « Code officiel géographique au 1er janvier 2026 ».
- **Producteur** : Insee. **Publication** : 2026.
- **URL** :
  - page : <https://www.insee.fr/fr/information/8740222> ;
  - fichiers : <https://www.insee.fr/fr/statistiques/fichier/8740222/v_commune_2026.csv> et <https://www.insee.fr/fr/statistiques/fichier/8740222/v_commune_depuis_1943.csv>.
- **Fichiers locaux** : `data/raw/collectivites/INSEE_COG2026_v_commune_2026.csv`, `…_v_commune_depuis_1943.csv`, `INSEE_COG2026_page_web.html`.
- **Utilisé** : rattachement des écoles fermées à leur commune (tableau de passage G3, H-B8).
- **Consulté le** : 2026-10-04.

**Autres publications Insee [C]**, consultées le 2026-10-04 (URL complètes et vérifiées dans `data/raw/recoupements/SOURCES.md` et `data/raw/couts_personnels/SOURCES.md`) :
- *Insee Première* n° 2093, « Usage de l'argent public : les dépenses publiques par fonction en 2024 » (05/02/2026), <https://www.insee.fr/fr/statistiques/fichier/8735252/IP2093.pdf> : cotisations employeurs comptées en rémunération dans chaque fonction ;
- liste des ODAL, champ 2024 (mai 2026), <https://www.insee.fr/fr/statistiques/fichier/8988934/Liste_ODAL_SD2024.pdf> : EPLE et caisses des écoles en APUL ;
- notes « Les principales révisions intervenues sur les comptes de la Nation » pour 2022-2024 (28/05/2025), <https://www.insee.fr/fr/statistiques/fichier/8574832/note_revisions_evol_2022_2024.pdf>, et pour 2023-2025 (03/06/2026), <https://www.insee.fr/fr/statistiques/fichier/8988934/Note_revisions_2023a2025.pdf> : statut provisoire des données 2024 ;
- billet de blog « Privatisations ou nationalisations, retraites des fonctionnaires, crédits d'impôts… » (24/10/2025), <https://blog.insee.fr/depenses-et-recettes-des-comptes-publics/> : convention des pensions ;
- *Insee Première* n° 2100, « Les salaires dans la fonction publique de l'État en 2024 » (06/05/2026), <https://www.insee.fr/fr/statistiques/fichier/8986474/ip2100.pdf> : contrôle des salaires.

---

## 6. Eurostat

Collecte UOE (Unesco-OCDE-Eurostat), données transmises par la DEPP à partir du compte de l'éducation. API publique d'Eurostat, France (`geo=FR`), années 2019 et suivantes. Producteur : Eurostat (Commission européenne). Consultation : 2026-10-04.

| Jeu (titre exact Eurostat) | Mise à jour | URL exacte (CSV lu) | Fichier local (`data/raw/depp_compte_education/`) | Ce qui est utilisé | Où |
|---|---|---|---|---|---|
| `educ_uoe_fini01` « Dépenses des établissement d'enseignement par niveau d'étude, orientation du programme, type d'établissement et catégorie des dépenses » (DOI <https://doi.org/10.2908/EDUC_UOE_FINI01>) | 15/09/2026 | <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fini01/A.MIO_EUR....FR?startPeriod=2019&format=SDMX-CSV> | `eurostat_educ_uoe_fini01_FR_MIO_EUR_2019-.csv` (et `.json` pour les libellés) | 2023, `sector` = TOT_SEC, CITE 02 + 1 (1er degré) et 2 + 3 (2nd degré) : catégories TOTAL, CUR_COMPT, CUR_COMPO, CUR_OTH, CAP, ASERV | script 01 (A7) ; rapport § 5 ; H-A6 |
| `educ_uoe_fine09` « Dépenses publiques au titre de l'éducation par élève/étudiant, calculs fondés sur des équivalents temps plein, par niveau d'étude et orientation du programme » (DOI <https://doi.org/10.2908/EDUC_UOE_FINE09>) | 15/09/2026 | <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fine09/A.EUR..FR?startPeriod=2019&format=SDMX-CSV> | `eurostat_educ_uoe_fine09_FR_EUR_2019-.csv` (et `.json`) | 2023 : 7 988 € (préélémentaire), 8 047 € (élémentaire), 9 446 € (collège), 11 561 € (lycée, apprentis compris) | script 05 (C2) ; rapport § 6 |
| `educ_uoe_fine10` « Élèves et étudiants par niveau d'étude et orientation du programme, corrigés des statistiques sur les dépenses d'éducation et alignés à l'année financière » (DOI <https://doi.org/10.2908/EDUC_UOE_FINE10>) | 11/09/2026 | <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fine10/A.NR....FR?startPeriod=2019&format=SDMX-CSV> | `eurostat_educ_uoe_fine10_FR_NR_2019-.csv` (et `.json`) | 2023, TOT_FTE, TOT_SEC : élèves en équivalent temps plein (pondération des moyennes) ; apprentis comptés pour 0,5 | script 05 (C2) ; H-C2 |
| Fiche de métadonnées ESMS « Pupils and students - enrolments (educ_uoe_enr) » (fiche commune à la collecte UOE, finance comprise) | 19/06/2026 | <https://ec.europa.eu/eurostat/cache/metadata/en/educ_uoe_enr_esms.htm> ; archive SDMX : <https://ec.europa.eu/eurostat/api/dissemination/files?file=metadata/educ_uoe_enr_esms.sdmx.zip> | `eurostat_esms_educ_uoe_enr_esms_en.htm`, `….sdmx.zip` | § 3.9, 5, 14.1, 15.1, 18.5, 18.6 : périodes de référence, comptabilité de caisse, alignement des effectifs sur l'exercice | H-C2 (conventions) [C] |

Autres jeux Eurostat [C] (calculs `_derive_G1_*`, contrôle ; mises à jour de septembre 2026, sauf `perp02` du 05/08/2026 et `enrp02` du 11/08/2026) :
- `educ_uoe_fine01`, <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fine01/A.MIO_EUR...FR?startPeriod=2019&format=SDMX-CSV> ;
- `educ_uoe_fine02`, <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fine02/A.MIO_EUR.....FR?startPeriod=2019&format=SDMX-CSV> ;
- `educ_uoe_fine03`, <https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_fine03?geo=FR&unit=MIO_EUR&sinceTimePeriod=2019&format=JSON&lang=fr> ;
- `educ_uoe_fini04`, <https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_fini04?geo=FR&unit=EUR&sinceTimePeriod=2019&format=JSON&lang=fr> ;
- `educ_uoe_perp02`, <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_perp02/A.NR.....FR?startPeriod=2019&format=SDMX-CSV> ;
- `educ_uoe_enrp02`, <https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_enrp02?geo=FR&isced11=ED02&sex=T&age=TOTAL&sinceTimePeriod=2019&format=JSON&lang=fr> ;
- les fichiers locaux sont dans `data/raw/depp_compte_education/eurostat_*`.

Enfin, `gov_10a_exp` (dépenses des APU par fonction, mise à jour du 16/09/2026, contrôle de la COFOG Insee) : <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/gov_10a_exp/A.MIO_EUR.S13+S1311+S1313.GF09+GF0901+GF0902+GF0903+GF0904+GF0905+GF0906+GF0907+GF0908.TE+D1+P2+P5+D62+D632+D7+D9+D3.FR?startPeriod=2019&format=SDMX-CSV> (`data/raw/recoupements/eurostat_gov_10a_exp_FR_COFOG09_2019-2024.csv`).

---

## 7. OCDE

#### OCDE-1 · Base *Education at a Glance* (OECD Data Explorer, SDMX) : dépense par élève ETP : [S] [R] [H]
- **Titre exact du flux** : « Expenditure on educational institutions per full-time equivalent student » (`OECD.EDU.IMEP,DSD_EAG_UOE_FIN@DF_UOE_INDIC_FIN_PERSTUD`, version 3.2). Base de *Regards sur l'éducation 2026*.
- **Producteur** : OCDE, à partir des données UOE transmises par la DEPP.
- **Publication** : dernière mise à jour du 01/07/2026 (données jusqu'à 2023).
- **URL** : requête exacte en **annexe A.3**.
- **Fichier local** : `data/raw/recoupements/oecd_sdmx_EAG_depense_par_eleve_FRA_OCDE_UE25_2019-2023.csv`.
- **Utilisé** :
  - filtres : EXP_SOURCE = S13 (ligne G5 du questionnaire UOE : dépense directe des administrations publiques), EXP_DESTINATION = INST_EDU, EXPENDITURE_TYPE = DIR_EXP, 2023 ;
  - France, moyenne OCDE et UE 25 ;
  - unités USD_PPP_ST (dollars PPA) et XDC_ST (euros) ;
  - niveaux CITE 02, 1, 2 et 3 : en France, 7 985 €, 7 847 €, 9 140 € et 11 067 €.
- **Où** : script 05 (C2) ; rapport § 6 (tableau des recoupements et comparaison internationale), § 9 ; hypothèses § 0, H-C2.
- **Consulté le** : 2026-10-04.

#### OCDE-2 · *Education at a Glance 2026: OECD Indicators* (éd. française : *Regards sur l'éducation 2026*) : [R] [C]
- **Titre exact** : *Education at a Glance 2026: OECD Indicators*.
- **Producteur** : OCDE (OECD Publishing, Paris).
- **Publication** : septembre 2026 (29/09/2026 d'après `data/raw/depp_compte_education/SOURCES.md`).
- **URL** :
  - DOI : <https://doi.org/10.1787/b4968bbc-en> ;
  - PDF : <https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/09/education-at-a-glance-2026_3bce4131/b4968bbc-en.pdf> ;
  - tableaux StatLink : <https://stat.link/ax7gjn> (C1), <https://stat.link/4y0jap> (C2), <https://stat.link/e0c4fw> (C3), <https://stat.link/83o9jl> (C4).
- **Fichiers locaux** : `data/raw/depp_compte_education/oecd_eag2026_education_at_a_glance_2026.pdf` et `oecd_eag2026_statlink_*.xlsx`.
- **Utilisé** : lignes France des tableaux C1 à C4 (contrôle ; tableau C1.2 : structure par nature identique à l'UOE).
- **Où** : rapport § 6 et 9 (« Regards sur l'éducation 2026 »). Les chiffres du rapport viennent cependant de la base SDMX (OCDE-1).
- **Consulté le** : 2026-10-04.

**Autres données et documents OCDE [C]**, consultés le 2026-10-04 :
- flux SDMX `DF_UOE_FIN_SOURCE_GV_PR_NDOM` (« Distribution of government, private and non-domestic expenditure on educational institutions », mise à jour du 01/07/2026) :
  - <https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_UOE_FIN@DF_UOE_FIN_SOURCE_GV_PR_NDOM,3.2/FRA+OECD..ISCED11_0+ISCED11_1+ISCED11_2+ISCED11_3+ISCED11_1T4+ISCED11_2_3.......?startPeriod=2021&dimensionAtObservation=AllDimensions&format=csvfilewithlabels>, fichier `recoupements/oecd_sdmx_EAG_sources_financement_FRA_OCDE_2021-2023.csv` ;
  - <https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_UOE_FIN@DF_UOE_FIN_SOURCE_GV_PR_NDOM,3.2/FRA..ISCED11_35SW+ISCED11_35+ISCED11_34+ISCED11_45SW+ISCED11_55SW+ISCED11_25+ISCED11_35_45.......?startPeriod=2019&dimensionAtObservation=AllDimensions&format=csvfilewithlabels>, fichier `depp_compte_education/oecd_sdmx_EAG_sources_financement_FRA_ISCED35_34_2019-2023.csv` (CITE 35 : part publique de 71,0 % en 2023, contexte de H-A3) ;
- flux `DF_UOE_FIN_ENR` (effectifs ajustés à l'année financière), <https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_UOE_FIN_ENR@DF_UOE_FIN_ENR,3.2/FRA......?startPeriod=2021&dimensionAtObservation=AllDimensions&format=csvfilewithlabels> ;
- structure SDMX (définition des lignes G5 et N5), <https://sdmx.oecd.org/public/rest/dataflow/OECD.EDU.IMEP/DSD_EAG_UOE_FIN@DF_UOE_INDIC_FIN_PERSTUD/3.2?references=all>, fichier `recoupements/oecd_sdmx_structure_DF_UOE_INDIC_FIN_PERSTUD_3.2.xml` ;
- Education GPS, profil France (EAG 2026), <https://gpseducation.oecd.org/CountryProfile?primaryCountry=FRA&treshold=10&topic=EO>, fichier `recoupements/oecd_education_gps_France_EAG2026.html` ;
- *Education at a Glance 2025: Sources, Methodologies and Technical Notes* (09/09/2025, DOI 10.1787/fcfaf2d1-en), <https://www.oecd.org/content/dam/oecd/en/publications/support-materials/2025/09/education-at-a-glance-2025-sources-methodologies-and-technical-notes_0050a1ae/Education%20at%20a%20Glance%20Sources%20Methodologies%20and%20Technical%20Notes.pdf>, et métadonnées UOE, <https://stat.link/o0puiv> ;
- *Regards sur l'éducation 2025 : France* (note pays, septembre 2025), <https://www.oecd.org/content/dam/oecd/fr/publications/reports/2025/09/education-at-a-glance-2025-country-notes_9749f4ff/france_0639c7fb/aca6dceb-fr.pdf>.

---

## 8. Cour des comptes et autres organismes publics

#### CDC-1 · Note thématique « Privilégier l'approche territoriale et l'autonomie dans la gestion des dépenses d'éducation » : [R] [H]
- **Titre exact** : « Privilégier l'approche territoriale et l'autonomie dans la gestion des dépenses d'éducation », *Notes thématiques*, contribution à la revue des dépenses publiques.
- **Producteur** : Cour des comptes. **Publication** : juillet 2023 (07/07/2023).
- **URL** : <https://www.ccomptes.fr/sites/default/files/2023-10/20230707-note-thematique-Gestion-depenses-education.pdf>
- **Fichier local** : `data/raw/recoupements/CdC_note_thematique_Gestion_depenses_education_juillet2023.pdf`.
- **Utilisé** : p. 8 : « Aucune information consolidée permettant de décrire le coût global d'un élève pour chaque niveau d'enseignement, en intégrant à la fois les dépenses de l'État et celles des collectivités territoriales, n'est publiée alors que, depuis 2017, la Cour des comptes recommande chaque année d'établir des indicateurs de coût par élève par programme, en distinguant secteur public et secteur privé ». Également p. 16 (tableau n° 2, dépense scolaire 2021) et p. 20.
- **Où** : rapport § 6 (« depuis 2017 ») ; anomalie 8 (« depuis 2017 » ici, « depuis 2018 » dans CDC-3). **Consulté le** : 2026-10-04.

#### CDC-2 · Rapport public annuel 2026, « Adapter la carte des collèges aux enjeux de la démographie et de la mixité sociale » : [R]
- **Titre exact** : *Rapport public annuel 2026*, première partie, chapitre 3 : « Adapter la carte des collèges aux enjeux de la démographie et de la mixité sociale ».
- **Producteur** : Cour des comptes. **Publication** : 25/03/2026.
- **URL** : <https://www.ccomptes.fr/sites/default/files/2026-03/20260325-RPA-2026-I-3-Adapter-la-carte-des-colleges.pdf> (page du rapport : <https://www.ccomptes.fr/fr/publications/le-rapport-public-annuel-2026>).
- **Fichier local** : `data/raw/recoupements/CdC_RPA2026_Adapter_la_carte_des_colleges_mars2026.pdf`.
- **Utilisé** : tableau n° 1, « Comparatif des charges de personnel par taille de collège pour l'État (2023) », p. 143 imprimée (p. 14 du PDF) : 8 900 € par collégien (moins de 200 élèves), 8 100 € (moins de 300 élèves), 6 700 € (500 à 600 élèves). Note 20 : surcoût d'environ 240 M€.
- **Où** : rapport § 4, 9. **Consulté le** : 2026-10-04.

#### CDC-3 · Note d'analyse de l'exécution budgétaire 2025, mission « Enseignement scolaire » : [X] [R] [H]
- **Titre exact** : « Analyse de l'exécution budgétaire 2025 – Mission interministérielle Enseignement scolaire ».
- **Producteur** : Cour des comptes. **Publication** : avril 2026 (PDF du 22/04/2026).
- **URL** : <https://www.ccomptes.fr/sites/default/files/2026-04/NEB-2026-Enseignement-scolaire.pdf>
- **Fichiers locaux** : `data/raw/budget_etat/CdC_NEB_execution2025_Enseignement_scolaire.pdf` (copie identique : `data/raw/couts_personnels/CourDesComptes_NEB2025_Enseignement_scolaire_avril2026.pdf`).
- **Utilisé** :
  - p. 6 : hausse 2025 « essentiellement portée par le CAS Pensions (+ 1,39 Md€) » ; masse salariale « active » + 226 M€ « à périmètre constant, soit 0,3 % » ; p. 52 : même chiffre, hors transfert des AESH et des AED ;
  - tableaux n° 17-19, p. 37-38 : titre 2 et CAS (tableau n° 18 : CAS Pensions 22,27 → 23,66 Md€ ; titre 2 hors CAS + 0,63 Md€, + 1,1 %) ;
  - p. 22, tableau n° 5 : imputation des crédits par action (119,4 % et 55,7 %) et citation sur l'imputation budgétaire ;
  - p. 54 : relèvement de 4 points du taux de contribution ;
  - p. 9 et 68 : recommandation n° 8 (dépense publique par élève) ; p. 62 : réponse du ministère (« complexe et peu fiable »), « depuis 2018 », « jusqu'en 2023 » ; p. 86 : suivi (ex-recommandation n° 7 de la NEB 2024, « non mise en œuvre »), « jusqu'en 2022 » ;
  - tableau n° 23, p. 43 : AED (8 731 ETPT en titre 2) ;
  - tableau n° 29, p. 69 : dépense fiscale 110215, 229 M€ en 2025 (recoupement de BUD-3).
- **Où** : rapport § 3, 4, 6, 9 ; hypothèses § 0, H-G6, H-B4, anomalies 4, 7 et 8 ; extractions du § 9. **Consulté le** : 2026-10-04.

#### CDC-4 · « Les lycées de la défense », observations définitives : [H]
- **Titre exact** : « Les lycées de la défense ». **Producteur** : Cour des comptes. **Publication** : 02/02/2026.
- **URL** : <https://www.ccomptes.fr/sites/default/files/2026-01/20260202-S2025-1868-Lycees-de-la-defense.pdf> (page : <https://www.ccomptes.fr/fr/publications/les-lycees-de-la-defense>).
- **Fichier local** : `data/raw/budget_etat/CdC_lycees_de_la_defense_2026.pdf`.
- **Utilisé** : tableau 19, p. 65 : coût complet 2024 de 142,5 M€ ; p. 65-68 : 4 390 élèves.
- **Où** : H-B3 (« lycées de la défense », hors approche B). **Consulté le** : 2026-10-04.

#### AUT-1 · Conseil d'analyse économique, *Focus* n° 121 : [R] [H]
- **Titre exact** : « Retraites des fonctionnaires d'État : pas de déficit caché mais un coût salarial surévalué », *Focus* du CAE n° 121.
- **Producteur** : Conseil d'analyse économique. Autrice : H. Paris ; « ce Focus est publié sous la responsabilité de l'autrice et n'engage qu'elle » (p. 1). **Publication** : septembre 2025.
- **URL** : <https://cae-eco.fr/static/pdf/Focus_121_pension_2509123.pdf> (communiqué : <https://cae-eco.fr/retraites-des-fonctionnaires-detat-pas-de-deficit-cache-mais-un-cout-salarial-surevalue-communique-de-presse>).
- **Fichier local** : `data/raw/recoupements/CAE_Focus121_retraites_fonctionnaires_Etat_sept2025.pdf`.
- **Utilisé** :
  - p. 1 : la contribution de l'État au CAS mêle « une cotisation similaire à celle des employeurs dans le régime général, le financement de dispositifs de solidarité […] et une subvention permettant d'équilibrer le régime » ; le CAE cherche à approcher « la notion classique d'effort contributif de l'État employeur » ;
  - p. 2-3 : le CAE retient le taux de 34,7 % évalué par l'IPP, et le compare à 78,3 % (taux des pensions civiles en 2025) et 126,07 % (militaires) ;
  - p. 6-7 : le CAE voit dans 34,7 % une « borne haute » et situe le « juste » taux entre 25,44 % et 34,7 %.
- **Où** : rapport § 8, 9 ; H-G6, H-C3 ; script 05 (taux codés l. 119-120 ; `TAUX_CAS` l. 113). **Consulté le** : 2026-10-04.

#### AUT-2 · Institut des politiques publiques, *Perspectives budgétaires*, chapitre 3 : [R] [H]
- **Titre exact** : « Retraites des fonctionnaires d'État : faut-il changer la convention comptable ? », *Perspectives budgétaires*, chapitre 3.
- **Producteur** : Institut des politiques publiques (IPP). Auteurs : P. Aubert, M. Pedrono, M. Tô, T. Tochev.
- **Publication** : juin 2025.
- **URL**, retrouvées et vérifiées le 2026-10-04 :
  - page : <https://www.ipp.eu/publication/retraites-des-fonctionnaires-detat-faut-il-changer-la-convention-comptable/> ;
  - PDF : <https://www.ipp.eu/wp-content/uploads/2026/04/chapitre_3_CAS_PENSION-_web.pdf>.
- **Fichier local** (archivé le 2026-10-04 après relecture) : `data/raw/recoupements/IPP_Perspectives_budgetaires_2025_chapitre3_CAS_pensions.pdf` (22 p.).
- **Pagination** : page imprimée = page du PDF + 52 (le pied de la p. 2 du PDF porte « 54 »).
- **Utilisé** :
  - « Résultats clés », p. 53 imprimée (p. 1 du PDF) : « En considérant un financement à part pour cette subvention, ainsi que pour certains droits propres à certaines professions spécifiques, le taux de cotisation d'équilibre des employeurs de fonctionnaires d'État serait de 34,7 % en 2020, soit bien en dessous des taux affichés de 74,28 % pour les civils » ;
  - p. 63 (p. 11 du PDF) : taux de 34,7 % rapporté à la masse des traitements des fonctionnaires d'État, « civils et militaires confondus », dans le compte corrigé ;
  - p. 67 (p. 15 du PDF, encadré 3) : « Nous faisons ici l'hypothèse que ce taux d'équilibre corrigé reste constant entre 2020 et 2023 ». Son maintien en 2025 est une hypothèse du dossier (H-C3).
- **Où** : rapport § 8, 9 ; H-G6, H-C3. **Consulté le** : 2026-10-04.

#### AUT-3 · France compétences, rapport sur l'usage des fonds de la formation professionnelle (RUF) 2025 : [H] [X]
- **Titre exact** : *Rapport sur l'usage des fonds de la formation professionnelle*, édition 2025 (fonds engagés en 2024) : fiche « L'apprentissage », rapport complet, annexes, panorama.
- **Producteur** : France compétences (établissement public de l'État). **Publication** : février 2026.
- **URL** : <https://www.francecompetences.fr/app/uploads/2026/02/RUF25_Apprentissage.pdf> ; <https://www.francecompetences.fr/app/uploads/2026/02/RUF25_VF.pdf> ; <https://www.francecompetences.fr/app/uploads/2026/02/RUF25_Annexes.pdf> ; <https://www.francecompetences.fr/app/uploads/2026/02/RUF25_Panorama.pdf>
- **Fichiers locaux** : `data/raw/depp_compte_education/francecompetences_RUF2025_*.pdf`.
- **Utilisé** :
  - fiche « L'apprentissage », p. 5-7 : 15 594 M€ engagés, origine des fonds, coûts pédagogiques des OPCO ;
  - rapport complet, PDF p. 19 et 21 : coût de revient par apprenti et par niveau (N3 : 7 590 € ; N4 : 8 640 €).
- **Où** : H-A3 (estimation de *s* = 17,5 %), via `_derive_G4_part_publique_apprentissage_2nd_degre.csv`. **Consulté le** : 2026-10-04.

#### AUT-4 · IGF-IGAS, « Revue des dépenses publiques d'apprentissage et de formation professionnelle » : [X]
- **Producteur** : Inspection générale des finances (n° 2023-M-112-04) et Inspection générale des affaires sociales (n° 2023-123R).
- **Publication** : mars 2024, mis en ligne en septembre 2024.
- **URL** : <https://igas.gouv.fr/sites/igas/files/2024-09/Rapport%20Igas%20-IGF%20Apprentissage-Formation%20(revue%20de%20d%C3%A9penses).pdf>
- **Fichier local** : `data/raw/depp_compte_education/igas_igf_2024-03_revue_depenses_publiques_apprentissage_formation_professionnelle.pdf`.
- **Utilisé** : annexe II, tableau 3, PDF p. 104 : NPEC moyens pondérés par niveau (N3 : 6 630 € ; N4 : 7 699 €).
- **Où** : H-A3, via G4. **Consulté le** : 2026-10-04.

#### AUT-5 · DGER, « Effectifs de l'enseignement agricole 2024-2025 » : [S] [R] [H]
- **Titre exact** : « Effectifs de l'enseignement agricole 2024-2025 » (onglet « Sommaire » du fichier).
- **Producteur** : ministère de l'Agriculture, Direction générale de l'enseignement et de la recherche (DGER), publié sur ChloroFil, site officiel de l'enseignement agricole (<https://chlorofil.fr/stats/effectifs>).
- **Publication** : mars 2025 (fichier modifié le 20/03/2025 selon ses métadonnées ; préfixe « 2503 » du nom de fichier).
- **URL** : <https://chlorofil.fr/fileadmin/user_upload/stats/effectifs/2503-effectifs-rs2024.xlsx>
- **Fichiers locaux** : `data/raw/budget_etat/DGER_effectifs_enseignement_agricole_rentree2024.xlsx` (copie identique, MD5 vérifié : `data/raw/effectifs_nationaux/dger_chlorofil_synthese_effectifs_EA_2024-2025.xlsx`).
- **Champ** : y compris la Nouvelle-Calédonie (436 élèves), la Polynésie française (815) et Wallis-et-Futuna (83), selon l'onglet « 1- Effectifs EAT » (soit environ 1 260 élèves du secondaire) ; effet négligeable sur H-B11 (moins de 0,1 point).
- **Utilisé** : onglet « 3- Voie sco par filières », cellules E29, E33 et E37 (public : 3 049 + 17 294 + 29 647 = 49 990 élèves du secondaire) et E48, E52 et E56 (privé : 29 016 + 6 678 + 54 314 = 90 008), avec contrôle des libellés de ligne (colonne B) et de colonne (« 2024 »). Onglet « 3bis- Voie sco par niveau » : contrôle de la passerelle G5.
- **Où** : script 04 (part « champ » des dépenses « lycées » des régions) ; rapport § 9 (« DGER ») ; H-B11. **Consulté le** : 2026-10-04.

#### CARTO-1 · data.gouv.fr (Etalab), « Contours administratifs », édition 2025 : [S] [R] [H]
- **Titre exact** : « Contours administratifs » (jeu de données), fichiers `departements-100m.geojson` et `regions-100m.geojson` de l'édition 2025.
- **Producteur** : data.gouv.fr (Etalab, DINUM). **Publication** : fichiers datés du 04/05/2026 par le serveur (en-tête Last-Modified). **Licence** : ODbL.
- **URL** : page <https://www.data.gouv.fr/datasets/contours-administratifs> ; fichiers <https://etalab-datasets.geo.data.gouv.fr/contours-administratifs/2025/geojson/departements-100m.geojson> et <https://etalab-datasets.geo.data.gouv.fr/contours-administratifs/2025/geojson/regions-100m.geojson>.
- **Fichiers locaux** : `data/raw/cartographie/etalab_contours_departements_2025_100m.geojson` et `…_regions_2025_100m.geojson`.
- **Utilisé** : contours des départements de métropole et des DROM, de Saint-Barthélemy et de Saint-Martin ; limites et noms des régions. Coordonnées arrondies au dix-millième de degré pour l'affichage (script 07).
- **Où** : script 07 ; carte des établissements ; rapport § 4 ; H-B18. **Consulté le** : 2026-10-04.

#### CARTO-2 · API Découpage administratif (geo.api.gouv.fr) : communes, arrondissements municipaux, communes déléguées : [S] [H]
- **Producteur** : DINUM (Etalab), API Découpage administratif. **Licence** : la page de l'API sur data.gouv.fr indique seulement que « toutes les données utilisées sont sous licences Open Data » ; selon le script de construction de l'API (<https://github.com/datagouv/api-geo>, `download-sources.sh` et `build/communes.js`), les centres et les mairies viennent du jeu « Contours administratifs » (CARTO-1, ODbL), sous licence duquel ils sont rediffusés ; les noms et les populations des communes viennent de l'Insee (paquet `@etalab/decoupage-administratif`).
- **URL** : <https://geo.api.gouv.fr/communes?fields=nom,code,centre,mairie,population,codeDepartement,codeRegion&format=json&geometry=centre> ; <https://geo.api.gouv.fr/communes?type=arrondissement-municipal&fields=nom,code,centre,mairie,population,codeDepartement&format=json&geometry=centre> ; <https://geo.api.gouv.fr/communes_associees_deleguees?fields=nom,code,type,chefLieu,codeDepartement,centre,mairie&format=json> (l'API ne donne pas de mairie pour les communes déléguées).
- **Fichiers locaux** : `data/raw/cartographie/api_geo_communes_2026-10-04.json` (34 969 communes), `…/api_geo_arrondissements_municipaux_2026-10-04.json` (45 arrondissements) et `…/api_geo_communes_associees_deleguees_2026-10-04.json` (2 576 communes associées ou déléguées).
- **Utilisé** : noms, populations et mairies des communes, pour les noms affichés sur la carte ; mairie de la commune des 892 établissements de la rentrée 2024 absents de l'annuaire actuel (centre de la commune pour 9 d'entre eux : 4 communes déléguées, dont l'API ne donne pas la mairie, et 5 arrondissements de Marseille dont la mairie de secteur est partagée) ; code commune des 566 écoles que ni l'annuaire ni le fichier IPS ne codent, retrouvé par le nom de leur commune (script 03, H-E4).
- **Où** : scripts 03 et 07 ; H-E4, H-B18. **Consulté le** : 2026-10-04.

#### CARTO-3 · IGN, Géoplateforme, fond « Plan IGN » : [H]
- **Producteur** : Institut national de l'information géographique et forestière (IGN). **Licence** : Licence Ouverte (Etalab), selon les conditions d'utilisation <https://cartes.gouv.fr/cgu/> (ancienne adresse : geoservices.ign.fr/cgu-licences).
- **Service** : WMTS <https://data.geopf.fr/wmts>, couche `GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2`.
- **Utilisé** : fond de carte facultatif, chargé à l'affichage, seulement quand la page est ouverte depuis le disque. Il n'entre dans aucun calcul et n'est pas archivé.
- **Où** : carte des établissements ; H-B18. **Consulté le** : 2026-10-04.

**Autres organismes publics [X] [C]**, tous consultés le 2026-10-04 :

| Titre exact | Producteur, date | URL exacte | Fichier local (`data/raw/…`) | Utilisé pour |
|---|---|---|---|---|
| « Allocation de rentrée scolaire (ARS) », fiche F1878 | service-public.gouv.fr (DILA) ; consultée le 04/10/2026 | <https://www.service-public.gouv.fr/particuliers/vosdroits/F1878> | non archivée (page web) | âge des enfants ouvrant droit à l'allocation (6 à 18 ans) : répartition des « autres APU » du 1er degré, H-B13 |
| « L'enseignement primaire », rapport public thématique | Cour des comptes ; 20/05/2025 | <https://www.ccomptes.fr/sites/default/files/2025-05/20250520-Enseignement-primaire.pdf> | `recoupements/CdC_RPT_Enseignement_primaire_mai2025.pdf` | p. 31-32 : méthode de la DEPP pour les petites communes (G3, H-B8) [X] |
| « Recentrer le soutien public à la formation professionnelle et à l'apprentissage », note thématique | Cour des comptes ; 07/07/2023 | <https://www.ccomptes.fr/system/files/2023-07/20230707-note-thematique-Soutien-public-formation-professionnelle-apprentissage.pdf> | `depp_compte_education/ccomptes_2023-07_note_thematique_…pdf` | p. 6 : France compétences parmi les financements publics (G4) [X] |
| « L'enseignement privé sous contrat », rapport public thématique | Cour des comptes ; 01/06/2023 | <https://www.ccomptes.fr/sites/default/files/2023-10/20230601-enseignement-prive-sous-contrat.pdf> | `recoupements/CdC_RPT_Enseignement_prive_sous_contrat_juin2023.pdf` | p. 22 (forfait communal, G3), p. 36 (enseignants du privé payés par l'État) [C] |
| « La construction, la rénovation et l'entretien des collèges », rapport public annuel 2023 | Cour des comptes ; 10/03/2023 | <https://www.ccomptes.fr/sites/default/files/2023-10/20230310-RPA-2023-construction-renovation-entretien-colleges.pdf> | `recoupements/CdC_RPA2023_construction_renovation_entretien_colleges.pdf` | contexte [C] |
| « L'éducation prioritaire », rapport d'évaluation de politique publique | Cour des comptes ; 17/10/2018 | <https://www.ccomptes.fr/system/files/2018-10/20181017-rapport-education-prioritaire.pdf> | `recoupements/CdC_Rapport_Education_prioritaire_oct2018.pdf` | contexte [C] |
| « Analyse de l'exécution budgétaire 2024 – Mission interministérielle Enseignement scolaire » | Cour des comptes ; avril 2025 | <https://www.ccomptes.fr/sites/default/files/2025-04/NEB-2024-Enseignement-scolaire.pdf> | `budget_etat/CdC_NEB_execution2024_Enseignement_scolaire.pdf` | contrôle 2024 [C] |
| « Modalités de financement des centres de formation des apprentis (CFA) » | IGF-IGAS ; juillet 2023 (mis en ligne en novembre 2024) | <https://igas.gouv.fr/sites/igas/files/2024-11/Rapport%20Igas-IGF%20Financement%20des%20CFA.pdf> | `depp_compte_education/igas_igf_2023-07_modalites_financement_CFA.pdf` | annexes II et III (G4) [X] |
| « Les premiers résultats de la campagne SOLTéA 2025 » | ministères chargés de l'éducation et de l'enseignement supérieur, Caisse des dépôts ; 29/05/2026, mis à jour le 24/09/2026 | <https://www.soltea.education.gouv.fr/espace-public/les-premiers-resultats-de-la-campagne-soltea-2025> | `depp_compte_education/pages_web/soltea_premiers_resultats_campagne_2025.html` | solde de la taxe d'apprentissage (G4) [C] |
| Arrêté du 28 mai 2026 fixant le montant et la répartition du fonds de soutien à l'apprentissage aux régions (NOR TRSD2614255A) | Légifrance ; JORF du 30/05/2026 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054151684> | `depp_compte_education/pages_web/legifrance_arrete_2026-05-28_…html` | contexte de H-A3 [C] |
| Effectifs de l'enseignement agricole 2025-2026 | ministère de l'Agriculture, DGER (ChloroFil) ; 01/04/2026 | <https://chlorofil.fr/fileadmin/user_upload/stats/effectifs/synth%C3%A8se-des-effectifs-2025-2026-ea-dger-dat.xlsx> | `budget_etat/DGER_synthese_effectifs_enseignement_agricole_2025-2026.xlsx` (copie dans `effectifs_nationaux/`) | élèves de l'enseignement agricole (passerelle G5, contrôle de H-E2) [X]. Le fichier de la rentrée 2024, lu par le script 04, a sa propre fiche (AUT-5) |
| *Portrait de l'enseignement agricole*, édition 2026 | ministère de l'Agriculture ; 13/04/2026 | <https://agriculture.gouv.fr/telecharger/154130> | `effectifs_nationaux/maasa_portrait_enseignement_agricole_2026.pdf` | contrôle [C] |
| Rapport d'information n° 2423 sur le financement public de l'enseignement privé sous contrat | Assemblée nationale ; 02/04/2024 | <https://www.assemblee-nationale.fr/dyn/16/rapports/cion-cedu/l16b2423_rapport-information.pdf> | `collectivites/AN_rapport_information_2423_financement_prive_sous_contrat_2024.pdf` | forfait communal (G3) [X] |
| « Niveau scolaire : éléments de diagnostic et propositions » | Haut-commissariat à la Stratégie et au Plan ; août 2026 | <https://www.strategie-plan.gouv.fr/files/files/Publications/2026/2026-08-31%20-%20Rapport%20Niveau%20scolaire/HCSP-2026-RAPPORT-Niveau-scolaire.pdf> | `recoupements/HCSP_rapport_Niveau_scolaire_aout2026.pdf` | p. 66-69 : convention des pensions [C] |
| Note d'analyse n° 61 « Élèves, professeurs et personnels des collèges publics sont-ils équitablement répartis ? » (et annexe) ; note d'analyse n° 76 « Écoles primaires : mieux adapter les moyens aux territoires » | France Stratégie ; 29/09/2017 et avril 2019 | <https://www.strategie-plan.gouv.fr/files/files/Publications/2017%20SP/2017-09-29%20-%20NA%2061%20-%20El%C3%A8ves%20professeurs/na-61-colleges-ok.pdf> ; <https://www.strategie-plan.gouv.fr/files/files/Publications/2017%20SP/annexe-note-analyse-61-colleges.pdf> ; <https://www.strategie-plan.gouv.fr/files/files/Publications/Rapport/fs-na-76-ecoles-primaires-avril-2019_0.pdf> | `recoupements/FranceStrategie_*` | études par établissement [C] |
| Rapports parlementaires sur le PLF 2026, mission « Enseignement scolaire » : Sénat, rapport général n° 139, tome III, annexe 13 ; Sénat, note de présentation de la commission des finances ; Sénat, avis n° 144, tome III, fasc. 1 ; AN, rapport n° 1996, annexe 23 ; AN, avis n° 2043, tome IV | Sénat, Assemblée nationale ; octobre-novembre 2025 | <https://www.senat.fr/rap/l25-139-313/l25-139-313_mono.html> ; <https://www.senat.fr/fileadmin/Commissions/Finances/2025-2026/PLF_2026/NP/Enseignement_scolaire_NP_PLF_2026.pdf> ; <https://www.senat.fr/rap/a25-144-31/a25-144-31_mono.html> ; <https://www.assemblee-nationale.fr/dyn/17/rapports/cion_fin/l17b1996-tiii-a23_rapport-fond.pdf> ; <https://www.assemblee-nationale.fr/dyn/17/rapports/cion-cedu/l17b2043-tiv_rapport-avis.pdf> | `recoupements/Senat_*`, `recoupements/AN_*` | aucun chiffre propre de dépense par élève [C] |

---

## 9. Extractions (transcriptions de sources officielles)

Ces fichiers ne sont pas des sources : ils ont été produits par les agents à partir des sources ci-dessus, sans calcul pour les transcriptions, avec un script pour les dérivés `_derive_*` et les `extractions/`. En cas de doute, la référence reste la source officielle.

### 9.1 Extractions lues directement par les scripts

| Fichier | Contenu | Source officielle et pages transcrites | Lu par |
|---|---|---|---|
| `data/raw/budget_etat/extractions/rap2025_execution_par_action_2024_2025.csv` | 55 actions : CP en LFI et consommés 2024-2025, titre 2 et hors titre 2 en 2025, ETPT 2025 | BUD-1 (RAP 2025) : p. 22-24 (récapitulation par programme et action) ; p. 44, 97-98, 152-153, 214-215, 270-271, 380-381 (éléments de synthèse, titre 2 et hors titre 2) ; tableaux « Répartition du plafond d'emplois par action » (p. 50 pour le P140) | script 04 (CP 2025 de 47 actions, soit 48 valeurs, l'action 04 du P230 étant lue en titre 2 et hors titre 2 ; voir `resultats/B3_intrants_extractions.csv`) ; script 05 (totaux par programme) |
| `data/raw/budget_etat/extractions/passerelle_G5_intrants_RAP_DPT_2024_2025.csv` | 32 intrants : PFMP, MEEF, stagiaires, MIES dans les COM par programme, P143 selon la RERS | BUD-1 p. 116, 230, 404 et 406 (PFMP 2025), p. 48, 53, 63-64, 101, 107, 125, 156, 162, 173, 217, 222, 238-239 (stagiaires, MEEF) ; BUD-6 p. 124, 134, 182, 234-235, 243, 410 ; BUD-2, tableaux par territoire p. 248-277 et p. 269, 273 ; DEPP-3, fiche 10.03, tableau 3 | script 04 : 7 valeurs (`com_p139_2024`, `com_p140_2024`, `com_p141_2024`, `com_p214_2024`, `com_p230_2024`, `pfmp_p141_2025`, `pfmp_p139_2025`) |
| `data/raw/couts_personnels/TRANSCRIPTION_titre2_par_programme_CAS_Pensions.csv` | titre 2 par catégorie et CAS Pensions, P140, P141, P230, P139, P214 : exécution 2024 et 2025, PLF 2026 et 2027 | BUD-1 p. 51, 105, 160, 220, 280 (ETPT p. 48, 101, 156, 217, 276) ; PAP 2026 p. 49, 102, 160, 212, 267 ; PAP 2027 p. 51, 101, 137, 190-191, 243 ; contrôle par CDC-3, tableau n° 17, p. 37 | script 05 (exécution 2025, `contributions_CAS_Pensions_total_EUR`) → C4, H-C3 ; exécution 2024 → H-G6 et rapport § 3 (effet du relèvement de 4 points, environ 94 € par élève) |
| `data/raw/collectivites/extractions/DGFiP_2025_enseignement_synthese_niveau_perimetre_BP.csv` | budgets principaux 2025 par niveau de collectivité et périmètre (écoles, collèges, lycées, transports, hors scolaire), en M€ | COL-1, export A.1-3, traité par `extractions/_script_extractions_collectivites.py` (opérations réelles ; codes 90x et 93x des budgets votés par fonction) | script 04 (5 valeurs : collèges, lycées, cas de Paris et de la Métropole de Lyon) → H-B10 |
| `data/raw/collectivites/extractions/DGFiP_2025_enseignement_postes_cles_budgets_principaux.csv` | postes clés par niveau : personnel, énergie, restauration, entretien, dotations aux EPLE, dotations au privé (655112, 655122), constructions… | COL-1, export A.1-3 ; libellés M57 de l'OFGL (§ 4) | script 04 (dotations au privé, H-B10 ; part des écoles dans le compte 6067, H-B8) ; script 05 (structure par nature, H-D2) |
| `data/raw/collectivites/extractions/DGFiP_2025_enseignement_niveau_sousfonction_nature.csv` | dépenses 2025 par niveau de collectivité × sous-fonction M57 × nature (M€) | COL-1, export A.1-3, traité par `extractions/_script_extractions_collectivites.py` (l. 223-225) | script 04 (sous-fonction 223 « Lycées privés » des régions : 578,6 M€) → H-B10 ; script 05 (retrait de cette sous-fonction de la structure des lycées) → H-D2 |
| `data/raw/budget_etat/DGER_effectifs_enseignement_agricole_rentree2024.xlsx` (fichier brut, pas une extraction) | élèves de l'enseignement agricole, rentrée 2024, public et privé | AUT-5 : onglet « 3- Voie sco par filières », cellules E29, E33, E37 (public) et E48, E52, E56 (privé) | script 04 (part agricole des dépenses « lycées » des régions) → H-B11 |

### 9.2 Extractions citées dans `hypotheses.md` (non lues par les scripts)

| Fichier | Contenu | Sources officielles et pages | Hypothèse |
|---|---|---|---|
| `data/raw/collectivites/extractions/G3_tableau_passage_DGFiP_DEPP_2025.csv`, avec `G3_quote_part_administration_generale_2025.csv`, `G3_couverture_extrapolation_communes_2025_horsCOM.csv`, `G3_extrapolation_par_classe_taille.csv`, `G3_eleves_par_strate_et_couverture.csv`, `G3_GFP_ecoles_par_GFP_part_non_couverte.csv`, `G3_appariement_ecoles_communes.csv` | passage de la dépense communale DGFiP 2025 au montant DEPP des écoles (étapes A0 à R5) ; quote-part d'administration générale (≈ 3,15 Md€) | COL-1 (les 7 exports de l'annexe A.1) ; COL-2 (4F) ; OFGL rapport 2026 (annexe 7A, p. 211 ; annexe 8, tableau 6, p. 220) et base communes 2025 ; DEPP-1 ; DEPP-2 ; DEPP-3 (10.04, tableau 2) ; DEPP-6 (règle d'imputation de l'administration générale) ; INSEE-5 ; § 2 (effectifs, annuaire, IPS des écoles) ; NI 19.07 ; Cour des comptes, « L'enseignement primaire » (mai 2025), p. 31-32 ; AN, rapport n° 2423. Script : `extractions/_script_G3_ecart_DGFiP_DEPP.py` | H-B8 |
| `data/raw/budget_etat/_derive_G5_passerelle_MIES_DEPP_2024_2025.csv` | passerelle de la MIES vers la part « État » du compte de l'éducation : table 2025, calages 2024 et 2013 | BUD-1, BUD-6, BUD-2, DEPP-6 (tableau 2i), *L'état de l'École 2025* p. 98, DEPP-3 (10.02, 10.03), PLR 2013, NI 24.45, DT 2024-E08. Script : `_derive_G5_passerelle_MIES_DEPP.py` ; `data/raw/budget_etat/NOTES.md` § 14 | H-B17 (≈ 2,6 Md€, dont ≈ 0,75 Md€ déjà retirés par B avec le post-bac) |
| `data/raw/depp_compte_education/_derive_G4_part_publique_apprentissage_2nd_degre.csv` | encadrement de la part publique *s* de l'apprentissage du 2nd degré (50 valeurs, avec source ou formule) | DEPP-2 (figure 4, C32:C36 ; figure 5) ; DEPP-1 (figures 4 et 5) ; DEPP-3 (10.04, tableau 2, lignes 10-11, 15, 20-21, 26-27 ; chap. 6) ; DEPP-4 (366606, ligne 19 ; 481445, ligne 22 ; 310608) ; AUT-3 ; BUD-5 (tableau 3, p. 35 ; p. 65-66) ; AUT-4 (tableau 3, p. 104) ; COL-2 (F4, ligne 19) ; INSEE-3. Script : `_derive_G4_apprentissage_2nd_degre.py` ; `NOTES.md` § 12 | H-A3 (*s* = 17,5 % [13,5 % ; 23 %]) |
| `data/raw/depp_compte_education/_derive_series_chrono_extraction_2021_2024.csv` et `_derive_series_chrono_calculs_2021_2025p.csv` | 295 valeurs des séries DEPP (fichier, onglet, cellule) et 191 calculs | DEPP-4 (5 fichiers), DEPP-3 (fiche 6.09). Script : `_derive_script_series_chrono.py` ; `NOTES.md` § 11 | H-A2, H-A3 |
| `data/raw/depp_compte_education/_derive_G1_*.csv` (5 fichiers) | structure UOE par nature et par niveau ; dépense publique par élève ETP ; rémunération par ETP d'enseignant | § 6 (fini01, fine01, fine02, fine03, fine09, fine10, fini04, perp02) ; OCDE-2 (tableau C1.2). Script : `_derive_G1_script_uoe_structure.py` ; `NOTES.md` § 13 | H-A6, H-C2 (contrôle de A7 et C2) |

### 9.3 Autres extractions (contrôle)

| Fichier(s) | Source officielle et emplacement |
|---|---|
| `data/raw/budget_etat/extractions/rap_execution_2024_2025_par_programme_et_titre.csv`, `rap2025_ETPT_par_programme_et_categorie.csv`, `rap2025_couts_moyens_entree_sortie_HCAS.csv` | BUD-1 : p. 20-26 ; tableaux « Emplois rémunérés par le programme » p. 47-48, 101, 156, 217, 276, 382 ; « Coûts entrée-sortie » p. 53, 107, 162, 222, 281-282, 386 |
| `data/raw/budget_etat/extractions/lfi2026_plf2027_par_action.csv`, `lfi2026_plf2027_par_programme_et_titre.csv` | PAP 2027, p. 22-26 ; LFI 2026 (état B) ; PLF 2027, tableau 2, p. 315-334 |
| `data/raw/budget_etat/extractions/plrg2025_execution_titre_categorie_MIES.csv`, `transferts_etat_education_2025.csv`, `autres_depenses_etat_hors_mission.csv`, `personnels_remuneres_hors_titre2_NEB2025.csv`, `indicateurs_officiels_par_eleve_documents_budgetaires.csv` | BUD-3 (annexe 1 « Etat_Titre_Cat », ListDepFisc, Recettes) ; BUD-1 (p. 109-117, 167-188, 230-239, 373, 390-404) ; CDC-3 (tableaux 23, 29) ; RAP 2025 des autres missions ; PAP 2027, P143, p. 303 |
| `data/raw/budget_etat/extractions/dpt2026_outremer_MIES_par_territoire_2024_2026.csv` | BUD-2 : synthèse p. 229-231 ; tableaux par territoire p. 232-277 (page PDF = page imprimée) |
| `data/raw/budget_etat/extractions/depp_rers2026_part_etat_compte_education_2024.csv` | DEPP-3, chap. 10 : fiches 10.02 (p. 411), 10.03 (p. 413), 10.04 (p. 414-415), 10.05 (p. 417), 10.06 (p. 419) |
| `data/raw/budget_etat/extractions/depp_dossier206_tableau2i_financement_initial_etat_par_niveau_2013_2014.csv` | DEPP-6 : tableau 2i, p. 152 et 168 imprimées (p. 154 et 170 du PDF) |
| `data/raw/budget_etat/extractions/plr2013_MIES_execution_CP_par_programme_action.csv`, `dger_effectifs_enseignement_agricole_voie_scolaire_par_niveau_2023_2025.csv` | PLR 2013 (data.economie.gouv.fr) ; DGER, onglet « 3bis- Voie sco par niveau » |
| `data/raw/couts_personnels/TRANSCRIPTION_couts_moyens_HCAS_et_ETPT_par_categorie.csv` | BUD-1 p. 53, 107, 162, 222, 281-282 ; RAP 2024 p. 55, 114, 171, 227, 287 ; PAP 2026 p. 52, 105, 163, 215, 270 ; PAP 2027 p. 54, 104, 140, 193, 245 |
| `data/raw/collectivites/extractions/DGCL_4F_enseignement_transport_2024_2025.csv`, `DGFiP_2025_enseignement_recettes_par_niveau_BP.csv`, `DGFiP_MEN_2025_communes_couverture_et_depense_par_eleve.csv`, `DEPP_collectivites_parts_montants_par_niveau.csv` | COL-2 (4F, cellules indiquées dans le fichier) ; COL-1 (exports A.1) ; § 2 (effectifs, annuaire) ; DEPP-1 et DEPP-3 (10.02, 10.04) |
| `data/raw/effectifs_nationaux/_derive_synthese_effectifs_nationaux_2023_2025.csv` | DEPP-7, DEPP-8, RERS 2026 (chap. 1, 3, 4, 6, 11), DGER (chaque ligne indique fichier et emplacement) |
| `data/raw/etablissements/_derive_ecoles_1d_rentree2024.csv`, `…_rentree2025.csv`, `_derive_etablissements_2d_rentree2024.csv` | § 2 (jointure par UAI), script `_exploration.py` |
| `data/raw/recoupements/_derive_insee_cofog09_2015-2024_long.csv` | INSEE-1 : toutes les lignes 09.x des tableaux T_3301 à T_3307, avec la cellule Excel |

Pour mémoire, `data/processed/base_ecoles_rentree2024.csv` et `base_2d_rentree2024.csv` sont produits par `scripts/03_base_etablissements.py` à partir des jeux du § 2.

---

## 10. Sources citées mais non archivées, introuvables ou à surveiller

| Point | Situation au 2026-10-04 | Conséquence |
|---|---|---|
| NI 26.35 (DEPP-9) | **Résolu le 2026-10-04** : archivée dans `data/raw/effectifs_nationaux/` et lue par le script 01. Avant correction : absente de `data/raw/` et des `SOURCES.md`. Retrouvée en ligne ; la figure 2 donne bien 392 035 (2024) et 391 937 (2025). Le commentaire du script renvoyait aussi à la « fiche 6.01 » de la RERS 2026, qui ne couvre que le 31/12/2024 (la valeur du 31/12/2025 est dans la fiche 6.09, tableau 2, p. 235) ; corrigé : il cite désormais la NI 26.35 | Fait : PDF et données archivés ; note citée dans H-A3 et au rapport § 9 |
| IPP, *Perspectives budgétaires* 2025, chapitre 3 (AUT-2) | **Résolu le 2026-10-04** : archivé dans `data/raw/recoupements/`. Avant correction : non archivé ; seul le *Focus* du CAE, qui le cite, est conservé. Retrouvé en ligne. Le taux de 34,7 % est un taux d'équilibre calculé pour l'année 2020 | Fait : archivé ; année de référence et nature du taux précisées (rapport § 8, H-C3) |
| DOI de la NI 26.42 (https://doi.org/10.48464/ni-26-42), cité dans `hypotheses.md` § 0 | Affiché sur la page officielle, mais pas encore enregistré : doi.org répond 404 (les DOI des NI 25.52, 25.58, 25.59, 26.35 et 26.36 fonctionnent) | Donner aussi l'URL de la page (DEPP-1) |
| `budget.gouv.fr` (RAP, PAP, guide de la justification au premier euro) | Accès automatisé bloqué (protection anti-robot) | Copies officielles de l'Assemblée nationale utilisées (mêmes documents) |
| Document méthodologique de la Dares sur la dépense nationale pour la formation professionnelle et l'apprentissage (jaune 2026) | Page anti-robot, non récupérée | Chiffres de la Dares repris du jaune « Formation professionnelle » (BUD-5) |
| Réponse ministérielle à la question écrite n° 06636 (Sénat, JO du 19/03/2026, p. 1424), <https://www.senat.fr/questions/base/2025/qSEQ251106636.html> | Lue en ligne (page accessible), non archivée | Contexte de H-A3 (le solde de la taxe d'apprentissage ne va pas aux CFA) |
| DPT « Outre-mer » 2027 (exécution 2025) ; COFOG 2025 de l'Insee ; jaune « Formation professionnelle » du PLF 2027 ; mise à jour de septembre 2026 des séries chronologiques DEPP ; *L'état de l'École 2026* | Non parus au 04/10/2026 (COFOG 2025 annoncée pour décembre 2026) | Années 2024 (DPT, COFOG) et 2024p (séries) utilisées, comme l'indiquent H-B2, H-C1 et H-A2 |
| Notes techniques OCDE *EAG 2026* ; fiche ESMS `educ_uoe_fin_esms` et rapport qualité France d'Eurostat | Notes OCDE 2026 non obtenues (page 403) ; pages Eurostat inexistantes (404) | Notes techniques *EAG 2025* et fiche ESMS `educ_uoe_enr_esms` utilisées |

---

## 11. Seine-Saint-Denis et Paris

Sources de l'analyse [analyse_seine_saint_denis_paris.md](analyse_seine_saint_denis_paris.md) et des hypothèses H-B19 à H-B23. Fichiers : `data/raw/recoupements/seine_saint_denis_paris/`, sous-dossiers `officiel/`, `etudes/` (ajouté le 2026-10-05) et `debat_public/` ; leur liste détaillée, avec tailles et empreintes, est dans le `SOURCES.md` de ce dossier. Repère supplémentaire : **[T]** = cité dans l'analyse. Toutes ces sources ont été consultées le 2026-10-04, sauf AUT-10 et les compléments de PAR-1 du 2026-10-05.

### 11.1 Compléments à des fiches existantes

- **DEPP-3 (RERS 2026)** : chapitre 2, fiche 2.06 « La taille des classes dans le second degré », p. 42 : 30,5 élèves par classe dans les formations générales et technologiques des lycées publics en 2025 (lecture du graphique). [T]
- **DEPP-5 (*Géographie de l'École* 2026, PDF et données de la fiche 22)** : fiche 21, texte p. 50 (Île-de-France : établissements plus grands, enseignants « plus jeunes […] aux rémunérations plus faibles ») ; méthodologie p. 106 (programmes retenus pour la fiche 21, montants « connus à un niveau infranational ») et p. 106-107 (départements sans dépenses de personnel en fonction « Éducation », retraités par la DEPP) ; fiche 22, onglets 22.1 à 22.3 (dépense par collégien, moyenne 2021-2023, public et privé : Paris 1 480 €, dont 1 230 € de fonctionnement et 250 € d'investissement ; Seine-Saint-Denis 2 190 €, 1 440 € et 750 € ; France 2 010 €, 1 210 € et 800 € ; lignes 87, 105 et 113) et onglet 22.4 (Île-de-France 2 380 € par lycéen, France 3 000 €). [T] [H]
- **Fiche 21 de la *Géographie de l'École* 2026 (données, `data/raw/depp_compte_education/depp_geo_ecole2026_depense_par_eleve_MEN-MESRE_donnees.xlsx`)** : onglet 21.1, C21 (Île-de-France, 4 600 €), C20 (Hauts-de-France, 4 860 €), C30 (France, 4 710 €) ; onglet 21.2, C20 (6 160 €), C19 (6 810 €), C29 (6 550 €) ; onglet 21.3, C20 (7 820 €), C19 (8 740 €), C29 (8 550 €) ; indices par région académique, DROM compris (validation de H-B19). [T] [H]
- **DEPP-10 (NI 26.36)** : données, figure 6 (indemnité de résidence moyenne de 20 € par mois pour les professeurs des écoles, traitement brut moyen 2 940 €) ; figure 9 (prime d'attractivité par échelon). [T] [H]
- **DEPP-11 (*Panorama* 2025-2026, chapitre 7)** : tableau 7.3 (salaire net en équivalent temps plein : contractuels et maîtres délégués enseignants, public et privé, 2 350 € ; fonctionnaires du 2nd degré public, 3 450 €) ; tableau 7.11 (salaires des fonctionnaires enseignants du public par âge : moins de 30 ans, 50 ans ou plus). [H]
- **BUD-1 (RAP 2025, mission « Enseignement scolaire »)** : p. 52 (P140), 106 (P141), 161 (P230), 221-222 (P139) et 281 (P214) : prime de fidélisation pour l'exercice en Seine-Saint-Denis, lignes « débasage de dépenses au profil atypique » (2024 : 82,0 ; 75,4 ; 30,1 ; 3,2 ; 0,7 M€) et « autres variations » (2025 : 47,8 ; 49,7 ; 17,6 ; 2,2 ; 0,1 M€) ; p. 53 : coûts d'entrée, global et de sortie des enseignants du 1er degré, hors CAS (38 363, 48 944 et 60 528 €) ; action 05 du P140 (« Remplacement », 2 170 M€ en 2025). [T] [H]
- **COL-1 (DGFiP, balances 2025, présentation croisée nature × fonction)** : extractions archivées dans `data/raw/recoupements/seine_saint_denis_paris/officiel/` : `DGFiP_2025_communes_fonction33_jeunesse_loisirs_par_commune_API.csv` (communes et Paris, budget principal, fonctions 33, 9033 et 9333, comptes 6 hors 66, 675, 676 et 68, sommes par commune) ; `DGFiP_2025_PARIS_fonction2_par_fonction_compte_API.csv` (Paris, fonctions 2, 902 et 932, par fonction et par compte, budgets 1 et 3) ; `DGFiP_2025_communes_75_92_93_94_personnel64_par_fonction_API.csv`, `DGFiP_2025_communes_personnel64_fonctions_ecoles_API.csv`, `DGFiP_2025_communes_personnel64_total_API.csv` (comptes 64) ; `DGFiP_2025_communes_92_93_94_ecoles_par_fonction_compte_API.csv` et `DGFiP_2025_communes_92_93_94_fonctionnement_par_fonction_API.csv`. Les variantes symétriques de la clé communale (H-B21) utilisent aussi les comptes 70 (recettes) et 6558-65748 (forfaits) des mêmes fonctions, pour toutes les communes (même API, requêtes analogues à l'annexe A.1). Utilisé : Paris 7 046 € de fonctionnement « écoles » par élève du public (personnel 5 070 €, caisses des écoles 1 304 €) ; communes du 93 2 552 € (personnel 1 523 €) ; fonction 33 : 273,0 M€ (93), 20,8 M€ (Paris) ; investissement « écoles » 249,0 M€ (93), 63,2 M€ (Paris) ; personnel en fonction 2 de Stains et des Lilas : 0 € ; fonction 81 du département de la Seine-Saint-Denis : 1,07 M€. [T] [H]
- **CDC-1 (note thématique de juillet 2023)** : p. 8 (aucun coût par élève consolidé, État et collectivités, n'est publié) ; p. 20 (soutien des communes de 250 € à 4 500 € par élève ; la Seine-Saint-Denis a construit 25 collèges et en a reconstruit 40 depuis 1986). [T]
- **INSEE-5 (COG 2026)** : Pierrefitte-sur-Seine (93059), commune déléguée de la commune nouvelle de Saint-Denis (93066) : la clé compte 39 communes en Seine-Saint-Denis. [H]

**Compléments pour le § 2.8 et la partie 4 de l'analyse (collèges, lycées et bâtiments ; H-B22, H-B23)** :

- **CDC-1 (note thématique de juillet 2023)** : p. 15 (« Le motif d'inquiétude le plus net concerne le bâti scolaire. Le décalage entre les besoins et les moyens de financement, mal quantifié à ce jour, laisse présager d'une dépense future n'ayant que peu de rapport avec la dépense actuelle »). [T]
- **CDC-7 (CRC Île-de-France, *Ville de Paris – L'école élémentaire*, IDR2025-64)** : p. 43 (parc des écoles construit « de 1880 à nos jours ») ; p. 49-50 (rénovation de toutes les écoles et crèches d'ici 2050, enveloppe de « 100 M€ votés pour initier les premiers travaux ») ; p. 44 (premier contrat de partenariat de performance énergétique, signé en 2011, pour 100 écoles) ; p. 52 (tableau des ETP d'agents de la Ville intervenant dans les écoles en 2023 : 7 853,6, dont 700 professeurs de la Ville, 1 910,1 ASEM, 1 730 agents d'entretien, 481,8 gardiens, 2 472,1 animateurs) ; p. 53 (répartition du temps de travail des agents d'entretien : 34,76 % scolaire, 52,14 % périscolaire, 13,10 % extrascolaire) ; p. 57 (tableau des dépenses d'équipement scolaires : 112 473 823 € en 2019, 89 553 885 € en 2023, source Ville de Paris, soit −20,4 % ; le texte écrit « 21 % ») ; p. 58 (écoliers du public : 122 759 en 2019, 106 180 en 2023). Pagination imprimée = page du PDF − 2. [T] [H]
- **PAR-1 (AN, rapport n° 1014)** : p. 48-49 (dédoublement des CP de REP+ à la rentrée 2017 : 47 % des classes du 93 à 12 élèves au plus, contre 63,3 % en France métropolitaine, les communes ne disposant « pas toujours des moyens ou des locaux nécessaires » ; à Aulnay-sous-Bois, une salle de 50 m² pour deux classes). [T]
- **PAR-2 (AN, rapport n° 1938)** : p. 90-91 (DSIL de 2 M€ par an pour l'immobilier scolaire du 93, plan « L'État plus fort ») ; p. 102 (co-enseignement au lieu du dédoublement : 17 % des CP, 19 % des CE1 et 35 % des grandes sections dans le 93, 14 % des classes en France). [T]
- **PAR-4 (AN, question orale n° 154)** : JO débats AN du 19/02/2025, p. 1379 : la ministre du Travail, au nom de la ministre de l'Éducation nationale : « La Seine-Saint-Denis, vous l'avez dit, est le département le plus jeune et le plus pauvre. Comme vous l'avez signalé, cela se voit dans l'état de certaines de ses écoles. » (sans chiffre). [T]
- **DEPP-5 (*Géographie de l'École* 2026, fiche 22)** : onglet 22.3 (investissement par collégien, public et privé, moyenne 2021-2023 : 750 € dans le 93, 250 € à Paris, 800 € en France ; lignes 105, 87 et 113, colonne C) ; onglets 22.5 et 22.6 (dépense des régions par lycéen, public et privé, moyenne 2021-2023 : Île-de-France 1 240 € de fonctionnement et 1 140 € d'investissement, ligne 16 ; France 1 850 € et 1 140 €, ligne 29 ; colonne C). [T]
- **DEPP-13 (*Géographie de l'École* 2026, données)** : ajouter la fiche 2 « La démographie des 0 à 25 ans », onglet 2.2, lignes 87, 105 et 113, colonne C (évolution des 0-17 ans de 2015 à 2025 : Paris −20,0 %, 93 −1,1 %, France −4,9 % ; estimations de population de l'Insee). URL : https://www.education.gouv.fr/sites/default/files/document/la-demographie-des-0-25-ans-518369.xlsx ; fichier local : `…/officiel/GeoEcole2026_la-demographie-des-0-25-ans-518369.xlsx`. [T]
- **COL-1 (DGFiP, balances 2025)** : extractions du projet `data/raw/collectivites/extractions/DGFiP_2025_enseignement_postes_cles_budgets_principaux.csv`, `…_niveau_sousfonction_nature.csv` et `…_synthese_niveau_perimetre_BP.csv` : part des bâtiments (investissement, énergie, entretien) dans la dépense publique par élève du public en 2025, France (10,4 à 12,5 % pour les écoles, 8,1 à 9,7 % pour les collèges, 7,5 à 9,8 % pour les lycées ; calcul de l'auteur, H-B22) ; `DGFiP_2025_PARIS_fonction2_par_fonction_compte_API.csv` et `DGFiP_2025_communes_92_93_94_ecoles_par_fonction_compte_API.csv` : bâtiments des écoles en 2025 (Paris 665 à 896 € par écolier du public selon que l'on compte le budget annexe ; communes du 93 1 604 €). [T] [H]
- **LEG-3 (textes cités, non archivés)** : ajouter le code de l'éducation, art. L. 239-2 (Observatoire national de la sécurité et de l'accessibilité des établissements d'enseignement), abrogé par l'article 10 de la loi n° 2020-1525 du 07/12/2020, en vigueur le 09/12/2020 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037286789 (téléchargement refusé, 403). [T]

### 11.2 Nouvelles fiches (sources officielles)

#### DEPP-13 · *Géographie de l'École* 2026, données par département et par académie (fiches 3, 5, 11, 17 à 20, 23 à 26) : [T] [H]
- **Titre exact** : *Géographie de l'École*, édition 2026, fichiers de données des fiches 3 « Le milieu social et le niveau de diplôme des parents », 5 « Les élèves boursiers dans le second degré », 11 « Les élèves de l'enseignement privé sous contrat », 17 « L'école inclusive », 18 « L'éducation prioritaire », 19 « Les conditions d'accueil dans le premier degré », 20 « Les conditions d'accueil dans le second degré », 23 « Les enseignants du premier degré », 24 « Les enseignants du second degré », 25 « La mobilité géographique des enseignants », 26 « Les personnels aux missions d'accompagnement et de prévention auprès des élèves ».
- **Producteur** : DEPP. **Publication** : juin 2026.
- **URL** (préfixe https://www.education.gouv.fr/sites/default/files/document/) : `le-milieu-social-et-le-niveau-de-diplome-des-parents-518372.xlsx` ; `ge2026-fiche-5sxlsx-518378.xlsx` ; `les-eleves-de-l-enseignement-prive-sous-contrat-518492.xlsx` ; `l-ecole-inclusive-518519.xlsx` ; `l-education-prioritaire-518522.xlsx` ; `les-conditions-d-accueil-dans-le-premier-degre-518525.xlsx` ; `les-conditions-d-accueil-dans-le-second-degre-518528.xlsx` ; `les-enseignants-du-premier-degre-518546.xlsx` ; `les-enseignants-du-second-degre-518549.xlsx` ; `la-mobilite-geographique-des-enseignants-518552.xlsx` ; `les-personnels-aux-missions-d-accompagnement-et-de-prevention-aupres-des-eleves-518555.xlsx`.
- **Fichiers locaux** : `…/seine_saint_denis_paris/officiel/GeoEcole2026_<nom>.xlsx` et `…/officiel/geo_<nom>.xlsx`.
- **Utilisé** (lignes 87 = Paris, 105 = Seine-Saint-Denis, 113 = France, colonne C, sauf mention) : 3.1 (indice de position sociale des collégiens, public et privé : 129,6 ; 92,8 ; 106,2) ; 5.2 (collégiens boursiers : 19,9 ; 41,4 ; 26,1 %) ; 18.1 (collégiens du public en éducation prioritaire : 22,3 ; 60,1 ; 21,8 %, colonne D) ; 19.2 (élèves par classe dans le 1er degré, rentrée 2025 : 21,1 ; 19,8 ; 21,3) ; 20.2 (élèves devant un professeur, voie générale et technologique, rentrée 2024 : 24,5 ; 23,1 ; 23,9 ; lignes 88, 106 et 114) ; 23.1 à 23.4 (enseignants du 1er degré, public et privé, rentrée 2024 : moins de 35 ans 24,3 ; 30,1 ; 21,2 % ; 50 ans ou plus 33,8 ; 22,1 ; 32,0 % ; non-titulaires 5,5 ; 10,0 ; 4,4 % ; remplaçants du public 6,5 ; 9,3 ; 8,7 %) ; 26.4 (AESH pour 1 000 élèves : Paris 14,8, ligne 12 ; Créteil 9,8, ligne 33 ; France 13,3, ligne 42).
- **Où** : [T] § 1.1, 2.1, 3.4 ; H-B19, H-B21.

#### DEPP-14 · *L'Éducation nationale en chiffres*, éditions 2023 et 2025 : [T]
- **Producteur** : DEPP. **Publication** : août 2023 ; juillet 2025.
- **URL** : 2023 : page officielle https://www.education.gouv.fr/depp/l-education-nationale-en-chiffres-edition-2023-378943 (accès automatisé refusé) ; copie du PDF sur le portail documentaire du Céreq : https://pmb.cereq.fr/doc_num.php?explnum_id=10267. 2025 : https://www.education.gouv.fr/sites/default/files/2025-08/l-ducation-nationale-en-chiffres-dition-2025-441804.pdf.
- **Fichiers locaux** : `…/seine_saint_denis_paris/officiel/DEPP_EN_chiffres_2023.pdf`, `…/DEPP_EN_chiffres_2025.pdf`. L'édition 2026 (10 350 € pour 2024) est déjà archivée (§ 1.4).
- **Utilisé** : 2023, rubrique « Le coût de l'éducation » (p. 3 du PDF) : 8 860 € par élève ou apprenti des 1er et 2nd degrés (dépense intérieure d'éducation 2021, tous financeurs) ; 2025 : 9 850 € (2023).
- **Où** : [T] § 1.2 ; H-B20 ; anomalie 13.

#### DEPP-15 · *Panorama statistique des personnels de l'enseignement scolaire 2025-2026*, chapitres 4, 6 et 11 (données) : [H]
- **Producteur** : DEPP. **Publication** : édition 2025-2026, chapitres mis en ligne au fil de l'eau.
- **URL** (préfixe https://www.education.gouv.fr/sites/default/files/document/) : `chapitre-4-les-missions-et-lieux-d-exercices-520480.xlsx` ; `chapitre-6-la-carriere-des-personnels-fonctionnaires-520483.xlsx` ; `chapitre-11-les-departs-volontaires-des-enseignants-du-secteur-public-520492.xlsx`.
- **Fichiers locaux** : `…/seine_saint_denis_paris/officiel/chapitre-4-…xlsx`, `…chapitre-6-…xlsx`, `…chapitre-11-…xlsx`.
- **Utilisé** : chapitre 6, figure 6.8 (indice moyen des professeurs des écoles selon l'ancienneté) et données 6.1 (pyramide des anciennetés) ; chapitre 4, figures 4.21 et 4.23 (contractuels et âge moyen en éducation prioritaire) ; chapitre 11, figure 11.6 (départs volontaires par académie).
- **Où** : H-B21.

#### PAR-1 · Assemblée nationale, rapport d'information n° 1014 (2018) : [T]
- **Titre exact** : Rapport d'information déposé par le Comité d'évaluation et de contrôle des politiques publiques sur l'évaluation de l'action de l'État dans l'exercice de ses missions régaliennes en Seine-Saint-Denis (rapporteurs : F. Cornut-Gentille et R. Kokouendo).
- **Producteur** : Assemblée nationale (XVe législature). **Publication** : 31/05/2018.
- **URL** : https://www.assemblee-nationale.fr/dyn/15/rapports/cec/l15b1014_rapport-information.pdf
- **Fichier local** : `…/seine_saint_denis_paris/officiel/AN_l15b1014_rapport_SSD_2018.pdf`.
- **Utilisé** : p. 14 (taux d'efficacité de la suppléance du 1er degré en 2015-2016 : 51,26 % dans le 93 contre 78,41 % en France) ; p. 40 (encadré citant un sociologue auditionné) ; p. 42 (enseignants de moins de 30 ans en 2016-2017 : 26,1 % contre 9,5 % en France métropolitaine ; 50 ans et plus : 18,3 % contre 30,0 % ; tableau « Proportion des néo-titulaires affectés dans le second degré à la rentrée scolaire 2016 », source citée : ministère de l'Éducation nationale : France métropolitaine 12 919 néo-titulaires, dont 2 723 en établissements « difficiles » (REP, REP+ ou QPV), soit 21,1 % ; académie de Créteil 2 635, 1 139, 43,2 % ; Seine-Saint-Denis 1 175, 757, 64,4 % ; part du 93 dans le total, 9,1 %, et de l'académie, 20,4 % : calcul de l'auteur ; ajouté le 2026-10-05) ; p. 49, note 1 (existence d'un rapport d'observations provisoires non publié de la Cour des comptes, à propos d'un autre chiffre). Aucune dépense par élève (recherche dans le texte intégral).
- **Où** : [T] § 1.3.

#### PAR-2 · Assemblée nationale, rapport d'information n° 1938 (2023) : [T] [H]
- **Titre exact** : Rapport d'information sur la mise en œuvre des conclusions du rapport d'information n° 1014 (rapporteurs : C. Decodts et S. Peu).
- **Producteur** : Assemblée nationale, Comité d'évaluation et de contrôle des politiques publiques (XVIe législature). **Publication** : 30/11/2023.
- **URL** : https://www.assemblee-nationale.fr/dyn/16/rapports/cec/l16b1938_rapport-information.pdf
- **Fichier local** : `…/seine_saint_denis_paris/officiel/AN_l16b1938_rapport_suivi_SSD_2023.pdf`.
- **Utilisé** : p. 103-104 (cités éducatives) ; p. 122-123 (952 contractuels dans les écoles publiques en 2023-2024, 577 en 2021-2022 ; 13 % de contractuels dans le 2nd degré) ; p. 123 (postes vacants : 87 ETP sur 1 140 dans la brigade, 72 sur 671 « hors la classe » ; 2nd degré : 20 vacants et 87 non rejoints) ; p. 124 (taux d'encadrement « légèrement supérieur à la moyenne nationale » ; P/E de 6,56 en 2023 et série en note 1) ; p. 129-130 (absences du 1er degré en 2022-2023 : 10,6 % ; 48 628 jours d'absence non remplacés pour 186 344 élèves, soit 0,26 jour d'absence non remplacée par élève, données ORSEM) ; p. 151-156 (primes REP+ et prime de fidélisation, versements de 20, 40 et 40 %).
- **Où** : [T] § 1.1, 1.3, 3.2, 3.5, 3.6 ; H-B21 ; anomalies 10 à 12.

#### PAR-3 · Assemblée nationale, réponses ministérielles aux questions écrites n° 10116, 51, 17285 et 9179 : [T] [H]
- **Titres et dates** : n° 10116 (G. Gouffier Valente), « Taux d'encadrement dans le premier degré par département », réponse au JO AN du 07/11/2023, p. 9959 ; n° 51 (A. Corbière), « Situation d'urgence dans l'école publique en Seine-Saint-Denis », réponse au JO AN du 24/01/2023, p. 644 ; n° 17285 (C. Autain), réponse au JO AN du 22/09/2020, p. 6477 ; n° 9179 (P. Anato), « Conditions éducatives en Seine-Saint-Denis », réponse au JO AN du 25/12/2018, p. 12130.
- **URL** : https://www.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE10116.pdf ; https://www.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE51.pdf ; https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE17285.pdf ; https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE9179.pdf
- **Fichiers locaux** : `…/seine_saint_denis_paris/officiel/QANR5L16QE10116.pdf`, `…QANR5L16QE51.pdf`, `…QANR5L15QE17285.pdf`, `…QANR5L15QE9179.pdf`.
- **Utilisé** : n° 10116, tableau par département (P/E 2020, 2021, 2022 : Seine-Saint-Denis 6,25 ; 6,43 ; 6,50 ; Paris 6,04 ; 6,35 ; 6,59 ; France métropolitaine 5,68 ; 5,79 ; 5,87 ; métropole et DROM 5,74 ; 5,84 ; 5,93) ; n° 51 (P/E 2016 et 2021) ; n° 17285 (P/E 2019) ; n° 9179 (académie de Créteil en 2017 : 28,5 élèves par division en lycée contre 30,1).
- **Où** : [T] § 1.1, 2.2 ; anomalie 10.

#### PAR-4 · Assemblée nationale, débats : question orale n° 154 (2025) et 1re séance du 16/06/2026 : [T]
- **Titres et dates** : question orale sans débat n° 154 (T. Portes), réponse en séance, JO débats AN du 19/02/2025, p. 1379 ; compte rendu intégral de la 1re séance du mardi 16 juin 2026, question orale n° 773, « Enseignement en Seine-Saint-Denis », p. 6021-6022.
- **URL** : https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QOSD154.pdf ; https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/premiere-seance-du-mardi-16-juin-2026.pdf
- **Fichiers locaux** : `…/seine_saint_denis_paris/officiel/QANR5L17QOSD154.pdf`, `…/AN_CRI_2026-06-16_1re_seance.pdf`.
- **Utilisé** : reprise du chiffre syndical en séance (2025 ; la ministre du Travail répondait au nom de la ministre de l'Éducation nationale) ; 19,7 élèves par classe dans le 93 contre 21 en moyenne (2026).
- **Où** : [T] § 1.1, 1.2.

#### PAR-5 · Sénat, réponses ministérielles aux questions écrites n° 01297 et n° 03308 : [T] [H]
- **Titres et dates** : n° 01297 (F. Gay), réponse au JO Sénat du 10/07/2025, p. 4006 ; n° 03308 (N. Havet), « Pour un régime de droit commun en matière de décharge d'enseignement des directeurs d'école », réponse au JO Sénat du 25/12/2025, p. 6303.
- **URL** : https://www.senat.fr/questions/base/2024/qSEQ241001297.html ; https://www.senat.fr/questions/base/2025/qSEQ250203308.html
- **Fichiers locaux** : `…/seine_saint_denis_paris/officiel/Senat_QE_01297_Gay_reponse_2025-07-10.html`, `…/Senat_QE_03308.html`.
- **Utilisé** : n° 01297 : P/E national prévu de 6,13 pour la rentrée 2025 ; brigade de 850 enseignants (+120). N° 03308 : coût des décharges des directeurs parisiens de « 24 millions d'euros annuels », supporté par l'État seul depuis 2019.
- **Où** : [T] § 1.1, 2.2 ; anomalie 12.

#### PAR-6 · Sénat, rapport d'information n° 730 (2024-2025), « Remplacement des enseignants » : [T]
- **Producteur** : Sénat, commission des finances (rapporteur : O. Paccaud). **Publication** : 11/06/2025.
- **URL** : https://www.senat.fr/rap/r24-730/r24-7301.pdf
- **Fichier local** : `…/seine_saint_denis_paris/officiel/Senat_r24-730_Paccaud_remplacement_enseignants_2025.pdf`.
- **Utilisé** : p. 7 et 31 (efficacité du remplacement en 2023-2024 : 78 % en France dans le 1er degré, moins de 75 % à Créteil, Paris et Versailles ; p. 33 : remplacement des absences courtes du 2nd degré faible à Paris, en Seine-Saint-Denis et dans les Hauts-de-Seine).
- **Où** : [T] § 3.5.

#### CDC-5 · Cour des comptes, référé S2024-1239 « Les décharges irrégulières de service des directeurs d'écoles parisiennes » : [T]
- **Producteur** : Cour des comptes. **Publication** : référé du 16/09/2024, rendu public le 25/11/2024.
- **URL** : https://www.ccomptes.fr/sites/default/files/2024-11/20241125-S2024-1239-Decharges-irregulieres-de-service-directeurs-ecoles-parisiennes.pdf
- **Fichier local** : `…/seine_saint_denis_paris/officiel/CdC_refere_S2024-1239_decharges_directeurs_Paris.pdf`.
- **Utilisé** : p. 2 (régime parisien « sans fondement juridique ») ; p. 3 (coût cumulé non compensé, recommandation d'y mettre fin).
- **Où** : [T] § 2.2.

#### CDC-6 · Cour des comptes, référé n° 64421 « Égalité des chances et répartition des moyens dans l'enseignement scolaire » : [T]
- **Producteur** : Cour des comptes. **Publication** : référé du 11/07/2012, rendu public le 03/10/2012 (PDF scanné).
- **URL** : https://www.ccomptes.fr/sites/default/files/EzPublish/refere_egalite_des_chances_64421.pdf
- **Fichier local** : `…/seine_saint_denis_paris/officiel/CdC_refere_2012-07-11_egalite_chances_64421.pdf`.
- **Utilisé** : p. 4-5 (les dotations des académies de Versailles et de Créteil « figurent systématiquement dans le bas du classement ») ; aucun chiffre de dépense par élève.
- **Où** : [T] § 1.3.

#### CDC-7 · Chambre régionale des comptes d'Île-de-France, « Ville de Paris – L'école élémentaire » (IDR2025-64) : [T] [H]
- **Producteur** : chambre régionale des comptes Île-de-France. **Publication** : 20/11/2025 (rapport d'observations définitives).
- **URL** : https://www.ccomptes.fr/sites/default/files/2025-11/IDR2025-64.pdf
- **Fichier local** : `…/seine_saint_denis_paris/officiel/CRC_IDF_VilleParis_ecole_elementaire_2025_IDR2025-64.pdf`.
- **Utilisé** : p. 5 et 36-37 (593 directeurs sur 626 totalement déchargés ; « plus de 348 » ETP) ; p. 42-43 et 52 (700 professeurs de la Ville de Paris, 44 M€) ; p. 53-54 (personnel extrascolaire : 53,1 M€ en 2023) ; p. 55 (forfait des écoles privées : 35 M€ ; caisses des écoles : 92 M€) ; p. 4 et 57-58 (coût net de fonctionnement : 5 434 € par élève en 2023 ; 106 180 élèves en 2023 contre 122 759 en 2019).
- **Où** : [T] § 2.2, 3.1 ; H-B9, H-B21.

#### CDC-8 · Chambre régionale des comptes d'Île-de-France, « Ville de Paris – L'exercice des compétences scolaire et périscolaire, exercices 2013 et suivants » (IDR2018-20) : [C]
- **Publication** : 08/06/2018. **URL** : https://www.ccomptes.fr/sites/default/files/2018-06/IDR2018-20.pdf
- **Fichier local** : `…/seine_saint_denis_paris/officiel/CRC_IDF_2018_Ville_de_Paris_competences_scolaire_periscolaire_IDR2018-20.pdf`.
- **Utilisé** : contexte (coût net de 3 762 € par élève en 2016 ; 769 professeurs de la Ville).

#### CDC-9 · Cour des comptes, « L'éducation prioritaire », rapport d'évaluation de politique publique : [T] [H]
- **Publication** : 17/10/2018. **URL** : https://www.ccomptes.fr/system/files/2018-10/20181017-rapport-education-prioritaire.pdf
- **Fichier local** (déjà archivé, § 8) : `data/raw/recoupements/CdC_Rapport_Education_prioritaire_oct2018.pdf`.
- **Utilisé** : p. 33, tableau n° 2 (masse salariale de l'État par élève en 2016 : écoles 3 615 € en éducation prioritaire contre 3 215 € ailleurs ; écoles et collèges réunis, sans les moyens propres de l'éducation prioritaire, 3 826 € contre 4 002 € : « Ceci s'explique par la composition plus jeune des équipes enseignantes ») ; p. 80-81 (remplacement par un contractuel sans effet compensateur significatif).
- **Où** : [T] § 1.1, 3.5 ; H-B21.

#### AUT-6 · France Stratégie, notes d'analyse n° 61 (2017) et n° 76 (2019) : [T]
- Fichiers déjà archivés dans `data/raw/recoupements/` (§ 8). **Utilisé** : note n° 61, p. 3 (le nombre de postes par élève explique 90 % des écarts de masse salariale par élève entre collèges hors DOM ; l'ancienneté et la composition du corps enseignant, une « part résiduelle »). **Où** : [T] § 3.2.

#### LEG-1 · Régime indemnitaire de l'éducation prioritaire : [T] [H]
- **Textes** : décret n° 2015-1087 du 28/08/2015 portant régime indemnitaire spécifique en faveur des personnels exerçant dans les écoles ou établissements relevant des programmes « Réseau d'éducation prioritaire renforcé » et « Réseau d'éducation prioritaire » ; arrêté du 08/12/2022 modifiant l'arrêté du 28/08/2015 fixant les taux annuels (NOR MENH2230834A) ; circulaire du 30/06/2021 « Revalorisation du régime indemnitaire spécifique en faveur des personnels exerçant dans les écoles ou établissements relevant du programme Réseau d'éducation prioritaire renforcé (REP+) … » (NOR MENE2120129C, BO n° 26 du 01/07/2021).
- **Producteurs** : Légifrance (SGG, DILA) ; ministère de l'Éducation nationale (BO).
- **URL** : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000031113279 ; https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046711303 ; https://www.education.gouv.fr/bo/21/Hebdo26/MENE2120129C.htm
- **Fichiers locaux** : `…/seine_saint_denis_paris/officiel/decret_2015-1087.html`, `…/arrete_2022-12-08_REP.html`, `…/BO_MENE2120129C.htm`.
- **Utilisé** : arrêté du 08/12/2022, art. 1 (part fixe REP+ de 5 114 €, montant de l'arrêté du 28/08/2015 modifié) ; circulaire de 2021 (part modulable REP+ de 234, 421 ou 702 € bruts) ; décret n° 2015-1087, notice (REP : 1 734 €).
- **Où** : [T] § 3.2 ; H-B21.

#### LEG-2 · Prime de fidélisation territoriale : [T] [H]
- **Textes** : arrêté du 24/10/2020 pris en application de l'article 3 du décret n° 2020-1299 du 24/10/2020 portant création d'une prime de fidélisation territoriale dans la fonction publique de l'État, version consolidée en vigueur depuis le 01/01/2024 (modifié par l'arrêté du 20/12/2023, NOR TFPF2331307A).
- **URL** : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000042460953
- **Fichier local** : `…/seine_saint_denis_paris/officiel/arrete_PFT_consolide.html`.
- **Utilisé** : article 1 (montant : 12 000 € depuis le 01/01/2024). Versements en trois fois : rapport AN n° 1938, p. 151-156 (PAR-2) ; dépense annuelle : RAP 2025 (BUD-1).
- **Où** : [T] § 3.2 ; H-B21.

#### LEG-3 · Textes cités, non archivés : [T] [H]
- Loi n° 2017-257 du 28/02/2017 relative au statut de Paris et à l'aménagement métropolitain (création de la Ville de Paris au 01/01/2019, à la place de la commune et du département) : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034103927/
- Décret n° 85-1148 du 24/10/1985 (indemnité de résidence, art. 9 : taux de 3 %, 1 % et 0 % selon la zone) et circulaire du 12/03/2001 (communes de zone 1).
- **Où** : [T] § 2.3, 3.2 ; H-B9, H-B21.

#### CNAF-1 · CNAF, allocation de rentrée scolaire par département : [T] [H]
- **Titre exact** : « ARS - Répartition des allocataires selon type d'ARS [Département] » (jeu `ars_s_type_dep`).
- **Producteur** : Caisse nationale des allocations familiales (data.caf.fr). **Publication** : mise à jour du 28/09/2026.
- **URL** : https://data.caf.fr/explore/dataset/ars_s_type_dep/
- **Fichier local** : `…/seine_saint_denis_paris/officiel/caf_ars_7593.json` (extraction : Paris, Hauts-de-Seine, Seine-Saint-Denis, Val-de-Marne, 2024 et 2025).
- **Utilisé** : année 2025, taux plein et différentiel additionnés (`indmtt_ars`) : Paris 37,30 M€, Seine-Saint-Denis 84,76 M€ ; total national 2 134,9 M€ (même jeu, somme des départements).
- **Où** : [T] § 3.4 ; H-B21.

#### LOC-1 · Direction des services départementaux de l'éducation nationale de la Seine-Saint-Denis, « Chiffres clés » : [T]
- **Publication** : constat de la rentrée 2023, article mis à jour le 10/09/2024.
- **URL** : https://www.dsden93.ac-creteil.fr/spip/spip.php?article6886
- **Fichier local** : `…/seine_saint_denis_paris/officiel/DSDEN93_chiffres_cles_article6886.html`.
- **Utilisé** : 355 085 élèves à la rentrée 2023, public et privé sous contrat (post-bac des lycées compris), dont 325 456 dans le public.
- **Où** : [T] § 1.2.

#### LOC-2 · Préfecture de la Seine-Saint-Denis, « Le plan État plus fort en Seine-Saint-Denis » : [C]
- **Publication** : page mise à jour le 13/05/2026. **URL** : https://www.seine-saint-denis.gouv.fr/Actions-de-l-Etat/Plan-L-Etat-plus-fort-en-Seine-Saint-Denis/Le-plan-Etat-plus-fort-en-Seine-Saint-Denis
- **Fichier local** : `…/seine_saint_denis_paris/officiel/plan_Etat_plus_fort_SSD.html`. **Utilisé** : contexte (prime de fidélisation, prérecrutement, immobilier scolaire).

#### CDC-10 · Chambre régionale des comptes d'Île-de-France, « Département de la Seine-Saint-Denis, cahier n° 3 : la construction, la rénovation et l'entretien des collèges » (IDR2023-57) : [T] [H]
- **Producteur** : chambre régionale des comptes Île-de-France. **Publication** : délibéré le 17/01/2023, publié le 15/12/2023 (rapport d'observations définitives, exercices 2015 et suivants).
- **URL** : https://www.ccomptes.fr/sites/default/files/2023-12/IDR2023-57.pdf
- **Fichier local** : `…/seine_saint_denis_paris/officiel/CRC_IDF_IDR2023-57_Dep93_cahier3_colleges_2023.pdf`.
- **Utilisé** : p. 5 (synthèse : « Quelques points noirs bâtimentaires sont identifiés et inclus dans un programme de rénovation ») ; p. 12 (72 collèges sur 130, soit 55 %, « font l'objet d'une attention particulière » : 2 protégés par le plan local d'urbanisme, 2 à structure métallique, 67 en zone de plan de prévention des risques ; collège Pierre-Sémard à Bobigny « dans un état particulièrement dégradé ») ; p. 13-15 (transfert de 1985-1986 : selon les procès-verbaux transmis, incomplets, 66 ou 67 équipements, 23 ans d'âge moyen, 735 élèves en moyenne, qualifiés le plus souvent de « mauvais » et « médiocres », parc « globalement ancien, mal entretenu », sans documentation ; aucun collège neuf avant 1990) ; p. 15 (depuis 1986 : 25 collèges créés, 40 reconstruits, 34 rénovations lourdes) ; p. 18 (18 collèges en PPP) ; p. 19 (objectifs des plans précédents atteints, « mis à part quelques retards ») ; p. 20 (choix architecturaux des années 1990 « sans souci des coûts de fonctionnement ou d'entretien ») ; p. 23 (intertitre : la double tutelle « complexifie et dégrade le suivi de l'entretien » ; texte : selon le Département, elle rend plus complexe le suivi de l'entretien, avec une « forte rotation des gestionnaires d'établissements, du fait de la faible attractivité de la fonction et du territoire ») ; p. 29-30 (ventilation insuffisante de certains locaux).
- **Où** : [T] § 4.2, 4.3, 4.4 ; H-B23.

#### CDC-11 · Chambre régionale des comptes d'Île-de-France, « Département de la Seine-Saint-Denis, cahier n° 1 : organique » (IDR2023-24) : [T] [H]
- **Producteur** : chambre régionale des comptes Île-de-France. **Publication** : délibéré le 01/03/2023, publié en décembre 2023 (exercices 2015 et suivants).
- **URL** : https://www.ccomptes.fr/sites/default/files/2023-12/IDR2023-24.pdf
- **Fichier local** : `…/officiel/CRC_IDF_IDR2023-24_Dep93_cahier1_organique_2023.pdf`.
- **Utilisé** : p. 45 (dette liée aux PPP : 221 M€ fin 2021, « exclusivement » pour des collèges).
- **Où** : [T] § 4.2 ; H-B23.

#### CDC-12 · Chambre régionale des comptes d'Île-de-France, « Département de la Seine-Saint-Denis, exercices 2010 et suivants » : [T] [H]
- **Producteur** : chambre régionale des comptes Île-de-France. **Publication** : délibéré le 26/05/2015, publié le 30/06/2015 (rapport d'observations définitives et sa réponse ; chapitre 7, « La construction et la rénovation de 21 collèges »). Pagination imprimée = page du PDF − 1.
- **URL** : https://www.ccomptes.fr/sites/default/files/EzPublish/Rapport-d-observation-d--finitives-et-sa-r--ponse_1.pdf (page : https://www.ccomptes.fr/fr/publications/departement-de-la-seine-saint-denis-seine-saint-denis-6).
- **Fichier local** : `…/officiel/CRC_IDF_2015_Dep93_ROD_exercices2010_et_suivants.pdf`.
- **Utilisé** : p. 8 et 87-88 (rappel du rapport « exercices 2004 et suivants », délibéré le 17/11/2010 : « l'important retard » d'investissement pour les collèges ; besoin de plus de 70 M€ par an pendant dix ans, 14 M€ de plus que la dépense annuelle depuis 2004) ; p. 87-89 (plan exceptionnel d'investissement 2010-2015 ; trois contrats de partenariat, 12 collèges livrés à la rentrée 2014) ; p. 20 (« soit plus de 300 M€ » à intégrer à la dette fin 2014) ; p. 114-116 (participations du Département de 39,5, 36,9 et 38,2 M€ HT ; montants nets à financer par les partenaires de 69,6, 65,6 et 67,9 M€ HT) (anomalie 15).
- **Où** : [T] § 4.4 ; H-B23, anomalie 15.

#### CDC-13 · Chambre régionale des comptes d'Île-de-France, « Région Île-de-France – Politique régionale pour la construction, la rénovation et l'entretien des lycées » (IDR2021-39) : [T] [H]
- **Producteur** : chambre régionale des comptes Île-de-France. **Publication** : délibéré le 10/05/2021, publié en novembre 2021 (exercices 2016 et suivants).
- **URL** : https://www.ccomptes.fr/system/files/2021-11/IDR2021-39.pdf
- **Fichier local** : `…/officiel/CRC_IDF_IDR2021-39_Region_IDF_lycees.pdf`.
- **Utilisé** : p. 6 (« Certes, les contraintes liées à l'état des bâtiments sont importantes à Paris » ; lycées Lavoisier, Rabelais et Fauré fermés ou déplacés « en raison de leur vétusté ou des risques pour la sécurité des élèves ») ; p. 19 (datations parfois inexactes dans les données de la Région) ; p. 20-23 (places vacantes, taux de remplissage et places manquantes par département, d'après les données de la Région : constat de la rentrée 2017 et prévisions pour 2018-2020 ; constat 2017 : lycées remplis à 88 % dans le 93 et à 86 % à Paris, 924 et 933 places manquantes, 6 761 et 9 093 places vacantes ; prévisions 2020 : 90 % et 85 %, 1 360 et 760 places manquantes ; tableaux lus avec pdfplumber) ; p. 28-29 (diagnostic de 2017 des 2 500 bâtiments : 38 % à risque en sécurité incendie, 35 % de couvertures et menuiseries extérieures très dégradées, 190 lycées, soit 41 %, à rénover globalement ; fiches par établissement non communiquées à la chambre) ; p. 52 (lycée Rabelais « particulièrement délabré »).
- **Où** : [T] § 4.3, 4.4 ; H-B22, anomalie 18.

#### CDC-14 · Chambre régionale des comptes d'Île-de-France, « Commune de Saint-Denis (Seine-Saint-Denis) » (IDR2024-40) : [T]
- **Producteur** : chambre régionale des comptes Île-de-France. **Publication** : délibéré le 06/02/2024, publié le 09/10/2024 (exercices 2016 et suivants).
- **URL** : https://www.ccomptes.fr/sites/default/files/2024-10/IDR2024-40.pdf
- **Fichier local** : `…/officiel/CRC_IDF_IDR2024-40_Commune_Saint-Denis.pdf`.
- **Utilisé** : p. 22-23 (opérations lancées en début de mandat, « principalement consacrées à la rénovation des bâtiments municipaux, et en premier lieu des écoles », reportées ; capacité de financement d'environ 37 M€ de dépenses d'équipement par an, contre 45 M€ annoncés en 2024 et 50 M€ ensuite).
- **Où** : [T] § 4.4.

#### CDC-15 · Cour des comptes, *Rapport public annuel 2023*, « La construction, la rénovation et l'entretien des collèges : mieux articuler les actions de l'Éducation nationale et des départements » : [T]
- **Producteur** : Cour des comptes. **Publication** : 10/03/2023.
- **URL** : https://www.ccomptes.fr/sites/default/files/2023-10/20230310-RPA-2023-construction-renovation-entretien-colleges.pdf
- **Fichier local** (déjà archivé, § 8) : `data/raw/recoupements/CdC_RPA2023_construction_renovation_entretien_colleges.pdf`.
- **Utilisé** : p. 342-343, tableau n° 1 (DDEC forfaitisée à compter de 2008, « fixe depuis 2009 » : elle a couvert 9,28 % de l'investissement « collèges » du 93 en 2015-2019, 15,61 % en moyenne nationale) ; p. 348 (« Les différences observées entre départements s'expliquent principalement par l'état du patrimoine existant et la dynamique démographique ») ; p. 351 et note 213 (rappel de 1995 : la suppression de tout service technique au 01/01/1990 « ne permettait plus au ministère de disposer d'une vision cohérente du patrimoine scolaire et donc de suivre son état physique »).
- **Où** : [T] § 4.3, 4.4.

#### CDC-16 · Cour des comptes, « L'enseignement primaire », rapport public thématique : [T]
- **Producteur** : Cour des comptes. **Publication** : 20/05/2025.
- **URL** : https://www.ccomptes.fr/sites/default/files/2025-05/20250520-Enseignement-primaire.pdf
- **Fichier local** (déjà archivé, § 8) : `data/raw/recoupements/CdC_RPT_Enseignement_primaire_mai2025.pdf`.
- **Utilisé** : p. 88 et 92 (« toutes ces démarches se heurtent à une absence de consolidation des données qui empêche d'avoir une quantification précise des besoins et des financements requis » pour la rénovation des écoles).
- **Où** : [T] § 4.3.

#### PAR-7 · Sénat, rapport d'information n° 800 (2022-2023), « Le bâti scolaire à l'épreuve de la transition écologique » : [T]
- **Producteur** : Sénat, mission d'information (président J.-M. Mizzon, rapporteure N. Havet). **Publication** : 28/06/2023.
- **URL** : https://www.senat.fr/rap/r22-800/r22-8001.pdf ; « L'essentiel » : https://www.senat.fr/fileadmin/Structures_temporaires/missions_d_information_communes/MI_bati_scolaire/cEssentiel_BatiScolaire_.pdf
- **Fichiers locaux** : `…/officiel/Senat_r22-800_bati_scolaire_transition_ecologique_2023.pdf`, `…/officiel/Senat_r22-800_essentiel.pdf`.
- **Utilisé** : p. 154-155 (« l'absence d'état des lieux du parc scolaire » ; « Les associations d'élus ne disposent pas d'information sur l'état des lieux des écoles, collèges et lycées »).
- **Où** : [T] § 4.3.

#### PAR-8 · Assemblée nationale, rapport d'information n° 1974 sur l'adaptation de l'école aux enjeux climatiques : [T]
- **Producteur** : Assemblée nationale, commission des affaires culturelles et de l'éducation (rapporteures G. Melchior, F. Pasquini). **Publication** : 06/12/2023.
- **URL** : https://www.assemblee-nationale.fr/dyn/16/rapports/cion-cedu/l16b1974_rapport-information.pdf
- **Fichier local** : `…/officiel/AN_l16b1974_rapport_adaptation_ecole_climat_2023.pdf`.
- **Utilisé** : p. 15 (« le lycée d'Aulnay-sous-Bois a été privé de chauffage et d'électricité à l'hiver 2022 », exemple tiré de l'actualité ; pas de chiffres consolidés du ministère sur l'état du bâti) ; p. 42 (« impossibilité de disposer d'un état des lieux complet du bâti scolaire en France »).
- **Où** : [T] § 4.3.

#### PAR-9 · Assemblée nationale, réponses ministérielles aux questions écrites n° 9350, 14292, 2613, 4744 et 16397 : [T]
- **Titres et dates** : n° 9350 (N. Abomangoli), « État vétuste des lycées en Île-de-France », réponse au JO AN du 31/10/2023, p. 9722 ; n° 14292 (M. Bouloux), « Observatoire de la sécurité et de l'accessibilité des établissements scolaires », JO AN du 19/03/2024, p. 2200 ; n° 2613 (R. Pilato), « Scandale de l'amiante dans les établissements scolaires », JO AN du 22/07/2025, p. 6657 ; n° 4744 (C. Guetté), « Urgence du désamiantage en France », JO AN du 28/10/2025, p. 8772 ; n° 16397 (P. Vannier), « Inadaptation du bâti scolaire aux épisodes de canicule », JO AN du 29/09/2026, p. 9094.
- **URL** : https://www.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE9350.pdf ; https://www.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE14292.pdf ; https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE2613.pdf ; https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE4744.pdf ; https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE16397.pdf
- **Fichiers locaux** : `…/officiel/QANR5L16QE9350.pdf`, `…/QANR5L16QE14292.pdf`, `…/QANR5L17QE2613.pdf`, `…/QANR5L17QE4744.pdf`, `…/QANR5L17QE16397.pdf`.
- **Utilisé** : n° 9350 (réponse : intervention avec la Région au « lycée Voillaume (93) en décembre 2022 » ; diagnostics techniques de tous les lycées établis en 2017 ; la question est une déclaration de la députée) ; n° 14292 (question : suppression de l'observatoire par la loi n° 2020-1525, selon le député ; réponse : enquête amiante et recherche d'un « état des lieux objectivé ») ; n° 2613 (enquête amiante lancée en avril 2024, résultats « restitués … prochainement ») et n° 4744 (résultats présentés en mars 2025 au comité social d'administration ministériel et aux associations d'élus) ; aucune publication trouvée au 04/10/2026 ; n° 16397 (plan du 28/05/2026 : diagnostic de l'exposition des sites scolaires aux vagues de chaleur dans chaque académie, non publié).
- **Où** : [T] § 4.3.

#### PAR-10 · Assemblée nationale, avis n° 2043, tome IV, projet de loi de finances pour 2026, « Enseignement scolaire » : [T]
- **Producteur** : Assemblée nationale, commission des affaires culturelles et de l'éducation (rapporteur B. Sorre). **Publication** : 29/10/2025.
- **URL** : https://www.assemblee-nationale.fr/dyn/17/rapports/cion-cedu/l17b2043-tiv_rapport-avis.pdf
- **Fichier local** (déjà archivé, § 8) : `data/raw/recoupements/AN_avis_2043_tIV_PLF2026_Enseignement_scolaire.pdf`.
- **Utilisé** : p. 35-36 (co-enseignement pouvant « atteindre jusqu'à un quart des classes dédoublées » dans le Val-d'Oise, l'Essonne ou la Seine-Saint-Denis, « où le bâti scolaire est particulièrement insuffisant » ; communes « peu incitées à investir durablement dans le bâti scolaire »).
- **Où** : [T] § 4.3.

#### DEPP-16 · DEPP, enquête « Bâtiments scolaires et conditions d'accueil des élèves et des personnels » : fiche d'enquête et avis du CNIS : [T]
- **Producteurs** : CNIS (fiche d'enquête, avis d'opportunité) ; Comité du label de la statistique publique (avis de conformité n° 2026_4491_DG75-L002) ; enquête conduite par la DEPP.
- **Publication** : avis d'opportunité du 10/10/2025 ; avis de conformité du 19/02/2026 ; fiche d'enquête et liste des Notes d'Information consultées le 04/10/2026.
- **URL** : https://www.cnis.fr/enquetes/batiments-scolaires-et-les-conditions-daccueil-des-eleves-et-des-personnels/ ; https://www.cnis.fr/app/uploads/2025/11/ao-2025-depp-bati-scolaire-et-conditions-daccueil-des-eleves-et-personnels.pdf ; https://www.cnis.fr/app/uploads/2026/01/ac-2026-depp-batiments-scolaires-ponctuelle.pdf ; https://www.education.gouv.fr/depp/les-notes-d-information-de-la-depp (ancienne adresse, redirigée : https://www.education.gouv.fr/les-notes-d-information-de-la-depp-89612)
- **Fichiers locaux** : `…/officiel/CNIS_fiche_enquete_batiments_scolaires.html`, `…/CNIS_avis_opportunite_2025_DEPP_bati_scolaire.pdf`, `…/CNIS_comite_label_2026_DEPP_batiments_scolaires.pdf`, `…/DEPP_liste_notes_information_2026-10-04.html`.
- **Utilisé** : fiche (« A ce jour, il n'existe aucun système d'information permettant de disposer de données administratives fiables et harmonisées entre les différentes collectivités territoriales » ; « la publication de résultats n'est réalisée que pour l'échelle nationale ») ; avis d'opportunité (enquête issue de la fusion et de l'extension de deux enquêtes annuelles, MicroTIC 1D et Immobilier – Cadre de vie ; collecte en 2026 auprès d'environ 3 500 écoles et établissements ; point de vue des directeurs et chefs d'établissement, pas de description technique du bâti ; données accessibles aux chercheurs) ; liste des Notes d'Information (aucune sur ce sujet au 15/09/2026).
- **Où** : [T] § 4.3.

#### DEPP-17 · data.education.gouv.fr : séries d'effectifs 2009-2025 et annuaires (Paris, Seine-Saint-Denis, Île-de-France, France) : [T] [H]
- **Producteurs** : DEPP ; ministère de l'Éducation nationale (annuaires). Licence Ouverte (Etalab).
- **Jeux** : `fr-en-ecoles-effectifs-nb_classes` (mis à jour le 27/08/2026) ; `fr-en-college-effectifs-niveau-sexe-lv` (27/07/2026) ; `fr-en-lycee_gt-effectifs-niveau-sexe-lv` et `fr-en-lycee_pro-effectifs-niveau-sexe-lv` (27/07/2026) ; `fr-en-effectifs-second-degre` (jeu « obsolète », 2015-2016 à 2019-2020) ; `fr-en-mode-hebergement-eleves-etablissements-2d` (05/08/2026) ; `fr-en-cites_scolaires` (04/10/2026) ; `fr-en-annuaire-education` ; `fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre` (04/10/2026).
- **URL** : page d'un jeu : https://data.education.gouv.fr/explore/dataset/<identifiant>/ ; requêtes exactes dans le tableau d'archivage et dans `_urls_requetes_ecoles_2021-2025.txt`.
- **Fichiers locaux** : `…/officiel/DEPP_opendata_effectifs/` (voir le tableau d'archivage).
- **Utilisé** : élèves des écoles publiques de la rentrée N−1 (dénominateur des écoles, H-B22) ; écoles, classes et élèves des écoles publiques 2015-2024 (93 : classes +18,9 %, élèves −2,5 % ; Paris : −4,3 % et −22,0 %) ; collégiens du public 2015-2025 (93 +9,7 %, Paris −12,6 %, raccord en 2019 entre deux jeux) ; lycéens pré-bac du public 2019-2025 (93 +10,1 %, Paris −3,8 %) ; collégiens du public dans un établissement de 700 élèves ou plus à la rentrée 2025 (93 31,1 %, Paris 10,2 %) ; élèves accueillis par les lycées (pré-bac, post-bac, collégiens des cités mixtes, rentrée 2025) ; date d'ouverture administrative des établissements (01/05/1965 pour 64,8 % des écoles publiques parisiennes) et identifiants RNB.
- **Où** : [T] § 2.8, 4.2, 4.3, 4.4 ; H-B22, anomalie 17.

#### DEPP-18 · DEPP, projections d'effectifs d'élèves dans les premier et second degrés à l'horizon 2035 : [T]
- **Titres** : *Note d'Information* n° 26.09, « Projections d'effectifs scolaires à horizon 2035 » ; document de travail n° 2026-E08 (M. Barhoumi, N. Miconnet, P. Serre) ; « Projections des effectifs d'élèves 2025-2035 », académies de Paris et de Créteil ; données associées au document de travail.
- **Producteur** : DEPP. **Publication** : avril 2026.
- **URL** : https://www.education.gouv.fr/depp/projections-d-effectifs-d-eleves-dans-les-premier-et-second-degres-horizon-2035-504275 ; fichiers (préfixe https://www.education.gouv.fr/sites/default/files/document/) : `education-nationale-depp-ni-2026-09-pdf-508061.pdf`, `projections-d-effectifs-d-l-ves-dans-les-premier-et-second-degr-s-horizon-2035-515387.pdf`, `projections-des-effectifs-d-l-ves-2025-2035---acad-mie-de-paris-515360.xlsx`, `projections-des-effectifs-d-l-ves-2025-2035---acad-mie-de-cr-teil-xlsx-515312.xlsx`, `donn-es-associ-es-au-document-de-travail-n-2026-e08-515384.xlsx`.
- **Fichiers locaux** : `…/officiel/DEPP_NI_26-09_projections_effectifs_2035.pdf`, `…/DEPP_DT2026-E08_projections_effectifs_2035_515387.pdf`, `…/DEPP_projections_2025-2035_academie_Paris_515360.xlsx`, `…/DEPP_projections_2025-2035_academie_Creteil_515312.xlsx`, `…/DEPP_DT2026-E08_donnees_associees_515384.xlsx`, `…/DEPP_page_projections_2035_504275.html`.
- **Utilisé** : onglets 075_2D et 093_2D, colonnes B (2025) et L (2035), scénario intermédiaire : élèves du second degré public −20,9 % à Paris, −5,8 % dans le 93 (maximum en 2029) ; voie générale et technologique du 93 : maximum en 2030. Ce sont des projections, pas des prévisions certaines.
- **Où** : [T] § 4.4.

#### COL-4 · DGFiP, balances comptables, présentation croisée nature × fonction, exercices 2012 à 2025 : extractions « écoles », « collèges » et partenariats public-privé : [T] [H]
- **Titre exact** : « Balances comptables des collectivités et des établissements publics locaux avec la présentation croisée nature-fonction » (un jeu par exercice ; 2025 : voir COL-1).
- **Producteur** : DGFiP, sur data.economie.gouv.fr. **Publication** : jeux de 2021 publié le 22/12/2022 ; de 2022 mis à jour le 07/12/2023 ; de 2023 le 06/12/2024 ; de 2024 le 09/12/2025 ; de 2025 le 13/07/2026 ; dates de publication des jeux 2012-2020 non relevées.
- **URL** : page d'un jeu : https://data.economie.gouv.fr/explore/dataset/<identifiant>/ (identifiants dans `DGFiP_identifiants_jeux_2012-2025.json`) ; requêtes exactes : `_urls_requetes_ecoles_2021-2025.txt`, `_urls_extraction_colleges_2012_2024.json`, `_urls_extraction_colleges_2025.json`.
- **Fichiers locaux** : `…/officiel/DGFiP_balances_2012-2025/` (74 extractions ; 85 fichiers avec les requêtes et les métadonnées).
- **Utilisé** : *écoles* (communes de Paris, des Hauts-de-Seine, de la Seine-Saint-Denis et du Val-de-Marne ; toutes les communes à comptabilité fonctionnelle ; 2021-2025) : investissement, bâti, dépenses courantes liées aux bâtiments, personnel, subventions d'investissement reçues, part des écoles dans l'équipement, comptes 1675 et 235 (marchés de partenariat) ; *collèges* (fonction 221 ; départements, Paris, Métropole de Lyon, CTU ; 2012-2025) : équipement, subventions d'équipement, capital (1675) et intérêts (6618) des PPP, énergie ; *Ville de Paris* : capital remboursé du contrat de partenariat de 2011 (écoles).
- **Où** : [T] § 2.8, 4.2, 4.5 ; H-B22, H-B23, anomalie 15.

#### COL-5 · OFGL, « Comptes des départements 2012-2025 – présentation fonctionnelle » et méthodologie des agrégats : [T] [H]
- **Producteur** : Observatoire des finances et de la gestion publique locales (data.ofgl.fr). **Publication** : jeu modifié le 05/08/2026 ; « Méthodologie OFGL : formules des agrégats financiers » modifié le 14/08/2026 ; « … définitions des agrégats financiers » du 24/03/2020.
- **URL** : https://data.ofgl.fr/explore/dataset/ofgl-base-departements-fonctionnelle (export : voir le tableau « OFGL » du § 4) ; https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/methodologie-ofgl-formules-des-agregats-financiers/exports/csv?delimiter=%3B&where=type_collectivite%3D%22D%C3%A9partements%22%20and%20annee%3E%3Ddate%272022%27 ; https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/methodologie-ofgl-definitions-agregats-financiers/exports/csv?delimiter=%3B
- **Fichiers locaux** : `data/raw/collectivites/OFGL_departements_fonctionnelle_fonction2_2022-2025.csv` (déjà archivé, § 4) ; `…/officiel/OFGL_methodologie_formules_agregats_departements_2022-2025.csv`, `…/OFGL_methodologie_definitions_agregats.csv` et leurs métadonnées ; `…/officiel/OFGL_catalogue_2026-10-04.json`.
- **Utilisé** : agrégat « dépenses d'équipement » de la fonction 221 (M57 : D20 + D21 + D23 − D204 − D2324 − C236 − C237 − C238), 2022-2025 : Seine-Saint-Denis 321,7 M€, soit 1 020 € par collégien du public et par an ; Paris 57,8 M€, 273 € ; départements, Paris et Métropole de Lyon 9 730 M€, 928 € ; 939 € sans Mayotte, dont l'OFGL ne donne pas de fonction 221 (calcul de l'auteur) ; catalogue : aucun jeu des comptes communaux par fonction.
- **Où** : [T] § 4.2 ; H-B22.

#### COL-6 · OFGL, *Cap sur…* n° 21, « Les investissements scolaires des collectivités locales » : [T] [H]
- **Producteur** : OFGL. **Publication** : octobre 2023 (pied de page : novembre 2023).
- **URL** : https://www.collectivites-locales.gouv.fr/files/files/Etudes-et-statistiques/OFGL/Les%20chantiers%20de%20l'OFGL/OFGL_cap_sur_21_investissements_scolaires_collectivites_30-10-2023.pdf
- **Fichier local** (déjà archivé, § 4) : `data/raw/collectivites/OFGL_CapSur21_investissements_scolaires_2023.pdf`.
- **Utilisé** : p. 3 et 9 (indicateur d'âge fondé sur la date d'ouverture de l'annuaire ; « l'âge d'un bâtiment ne révèle pas son état ») ; p. 5-6 (plus haut niveau d'investissement scolaire des communes en 2019, avant les élections municipales de 2020).
- **Où** : [T] § 4.2, 4.3 ; anomalie 17.

#### LOC-3 · Ville de Paris, comptes administratifs 2023, 2024 et 2025, rapports financiers : [T] [H]
- **Producteur** : Ville de Paris. **Publication** : 03/07/2024 (CA 2023) ; 30/06/2025 (CA 2024) ; 01/07/2026 (CA 2025).
- **URL** : https://cdn.paris.fr/paris/2024/07/03/rapport-ca-2023-consolide-vf-pour-intro-pxNk.pdf ; https://cdn.paris.fr/paris/2025/06/30/ca-2024-rapport-financier-rFhS.pdf ; https://cdn.paris.fr/paris/2026/07/01/ca-2025-rapport-financier_-gk9Q.pdf (page : https://www.paris.fr/pages/comptes-administratifs-de-la-ville-retrouvez-toutes-les-infos-27793).
- **Fichiers locaux** : `…/officiel/VilleParis_CA2023_rapport_financier.pdf`, `…/VilleParis_CA2024_rapport_financier.pdf`, `…/VilleParis_CA2025_rapport_financier.pdf`, `…/VilleParis_page_comptes_administratifs.html`.
- **Utilisé** : postes scolaires imputés hors des fonctions « écoles » (budget participatif d'arrondissement « affaires scolaires » et budget participatif des écoles, accessibilité des bâtiments scolaires, contrats de performance énergétique des écoles et collèges, école de la ZAC Saint-Vincent-de-Paul) : 15,4, 35,0 et 36,5 M€ en 2023, 2024 et 2025 (CA 2023, p. 77, 105 et 129 ; CA 2024, p. 29, 70, 95 et 118, dont 6,0 M€ en 2024 pour l'école de l'équipement Pinard, ZAC Saint-Vincent-de-Paul, p. 29 ; CA 2025, p. 33, 68, 88 et 105) ; premier degré : « nouvelles écoles et opérations de rénovation » (14,9 M€ en 2023, 4,5 M€ en 2025) et « entretien et équipement des écoles » (45,5, 42,8 et 46,7 M€) (CA 2023, p. 51 ; CA 2024, p. 47 ; CA 2025, p. 47-48) ; contrat de partenariat de performance énergétique des écoles : encours de 14,6 M€ fin 2025 (CA 2025, p. 23) et intérêts de 0,8 M€ (p. 27) ; contrat signé en 2011 pour 100 écoles selon la CRC (CDC-7, p. 44). Montants lus sur les pages des PDF, l'extraction de texte étant défectueuse.
- **Où** : [T] § 4.2 ; H-B22, H-B23.

#### LOC-4 · Ville de Paris, rapport d'orientations budgétaires 2026, communication 2021 DCPA 20, projet de délibération 2026 DASCO 12 et page sur la rénovation des écoles : [T]
- **Producteur** : Ville de Paris. **Publication** : rapport d'orientations budgétaires 2026 (novembre 2025, mis en ligne le 21/01/2026) ; 2021 DCPA 20 (novembre 2021) ; 2026 DASCO 12 (avis du conseil départemental de l'éducation nationale du 29/01/2026) ; page « Les écoles et crèches parisiennes vont être entièrement rénovées » (mise à jour du 10/09/2026).
- **URL** : https://cdn.paris.fr/paris/2026/01/21/rapport-d-orientations-budgetaires-2026-jBjO.pdf ; https://cdn.paris.fr/paris/2021/11/09/c33f2ff383b43d5d6ac30130ff4e315c.pdf ; https://a06-v7.apps.paris.fr/a06/jsp/site/plugins/odjcp/DoDownload.jsp?id_entite=66098&id_type_entite=6 ; https://www.paris.fr/pages/paris-lance-la-renovation-complete-de-ses-ecoles-et-creches-26971
- **Fichiers locaux** : `…/officiel/VilleParis_ROB_2026_nov2025.pdf`, `…/VilleParis_2021_DCPA_20.pdf`, `…/VilleParis_2026_DASCO_12_sectorisation_colleges.pdf`, `…/VilleParis_page_renovation_complete_ecoles_creches.html`.
- **Utilisé** : rapport d'orientations budgétaires 2026, p. 20 (contrats de performance énergétique « notamment sur neuf collèges ») ; 2021 DCPA 20 (collèges Lucie-Faure, Chappe, Utrillo et Courteline restructurés ou reconstruits, livrés en 2019-2021) ; 2026 DASCO 12 (collège Aimé-Césaire, 18e : « ne compte plus que deux divisions de 6e à la rentrée 2025 ») ; page de la Ville : contexte (déclaration de la collectivité).
- **Où** : [T] § 4.3, 4.4.

#### LOC-5 · Département de la Seine-Saint-Denis, plan « Éco-collège » 2021-2030 et communiqué du 04/02/2022 : [T]
- **Producteur** : Département de la Seine-Saint-Denis. **Publication** : « Éco-collège 2021-2030 : le plan d'investissement pour la résilience écologique des collèges », portail webcollege, 18/11/2020 (mis à jour le 27/01/2021) ; communiqué de presse du 04/02/2022.
- **URL** : https://www.webcollege.seinesaintdenis.fr/actualites/eco-college-2021-2030-le-plan-d-investissement-pour-la-resilience-ecologique-des-colleges--4885.htm ; https://seinesaintdenis.fr/l-essentiel-du-departement/espace-presse/article/colleges-en-seine-saint-denis-le-departement-accelere-son-plan-de-renovation-d
- **Fichiers locaux** : `…/officiel/Dep93_webcollege_eco-college_2021-2030.html`, `…/officiel/Dep93_CP_2022-02-04_plan_renovation_colleges.html`.
- **Utilisé** (déclarations de la collectivité) : 8 collèges neufs et 7 000 places annoncés pour 2021-2030 ; en 2022, 5 collèges choisis pour une rénovation thermique « pour le niveau de vétusté de l'enveloppe de leurs bâtiments ».
- **Où** : [T] § 4.3, 4.4.

#### LOC-6 · Région Île-de-France, délibérations sur les lycées : CR 2017-059, CR 2021-012 et CR 2025-030 : [T] [H]
- **Producteur** : Région Île-de-France (conseil régional). **Publication** : 10/03/2017 (plan d'urgence pour les lycées) ; 04/02/2021 (revoyure du plan d'urgence) ; 24/09/2025 (financement du fonctionnement des lycées pour 2026).
- **URL** : https://www.iledefrance.fr/actes/deliberations/CR2017-059RAP.pdf (et `CR2017-059DEL.pdf`) ; https://www.iledefrance.fr/actes/deliberations/CR2021-012RAP.pdf (et `CR2021-012DEL.pdf`) ; https://www.iledefrance.fr/actes/deliberations/CR2025-030RAP.pdf (et `CR2025-030DEL.pdf`).
- **Fichiers locaux** : `…/officiel/RegionIDF_CR2017-059RAP.pdf`, `…DEL.pdf` ; `…/RegionIDF_CR2021-012RAP.pdf`, `…DEL.pdf` ; `…/RegionIDF_CR2025-030RAP.pdf`, `…DEL.pdf`.
- **Utilisé** : CR 2017-059, annexes 1 à 5, p. 81-93 (4 150 places nouvelles dans le 93 sur 21 600, aucune à Paris ; rénovations globales : 5 dans le 93, 7 à Paris ; opérations « toit-façade » : 12 et 3 ; lycée Saint-Exupéry de Créteil : opérations « demi-pension » et « rénovation simple ») ; CR 2021-012, p. 6 et annexe 2, p. 40-41 (30 lycées « très vétustes » en 2016, dont 10 à Paris et 1 dans le 93 ; « A fin 2021, tous ces lycées auront fait l'objet d'un traitement ») et annexe 1 (rénovation simple du lycée Saint-Exupéry livrée en 2019) ; CR 2025-030, p. 3-4 et annexe 1 à la délibération, p. 18-21 (barèmes de la DGFL 2026 ; 382 M€ de salaires des agents des lycées en 2026) et annexe 1 au rapport, p. 7-13 (dotation de fonctionnement consolidée 2016 et 2026 par établissement ; 210 067 860 € publiés en 2026).
- **Où** : [T] § 2.8, 4.2, 4.3, 4.6 ; H-B22.

#### LOC-7 · Région Île-de-France, données ouvertes sur les lycées : [T] [H]
- **Producteur** : Région Île-de-France (data.iledefrance.fr).
- **Jeux** : « Données budgétaires des lycées – opérations directes votées » (décisions du 21/01/2021 au 17/11/2023 ; mis à jour le 20/03/2024) ; « Opérations de construction et de rénovation dans les lycées franciliens » (26/01/2018) ; « Plan d'urgence lycées 2019 » (26/09/2019) ; « Lycées – données générales » (08/09/2026).
- **URL** : https://data.iledefrance.fr/explore/dataset/donnees-budgetaires-lycees-operations-directes/ ; https://data.iledefrance.fr/explore/dataset/operations-de-construction-et-de-renovation-dans-les-lycees-francilens/ ; https://data.iledefrance.fr/explore/dataset/travaux-lycees-2019/ ; https://data.iledefrance.fr/explore/dataset/lycees-donnees-generales/
- **Fichiers locaux** : `…/officiel/RegionIDF_opendata_lycees_operations_directes_2021-2023.csv`, `…/RegionIDF_opendata_operations_construction_renovation_lycees.csv`, `…/RegionIDF_opendata_travaux_lycees_2019.csv`, `…/RegionIDF_opendata_lycees_donnees_generales.csv` et leurs métadonnées.
- **Utilisé** (calcul de l'auteur) : opérations directes votées en 2021-2023, part rattachable à un département (1 294,9 M€ sur 2 847,9 M€, soit 45 %) : 733 € par élève accueilli et par an dans le 93, 514 € à Paris, 956 € en Île-de-France ; 829 €, 926 € et 1 158 € par lycéen pré-bac ; trois opérations font 77 % du montant du 93 (Cugnot 42,15 M€, Paul-Éluard 40 M€, Henri-Sellier 22,75 M€) ; autorisations de programme des plans d'investissement 1995-2018 : 14 258 €, 7 792 € et 11 955 € par élève accueilli en 2015 ; plan d'urgence 2019 : toitures et verrière du lycée Saint-Exupéry (4,37 M€, octobre 2019) ; année de construction des lycées publics (médiane 1895 à Paris, 1971 dans le 93 ; années renseignées pour 70 lycées sur 92 et 59 sur 68).
- **Où** : [T] § 4.2, 4.3, 4.6 ; H-B22.

#### LOC-8 · Région Île-de-France, communication sur les lycées (2024-2026) : [T]
- **Producteur** : Région Île-de-France. **Publication** : « La Région Île-de-France investit 1 milliard d'euros par an dans ses lycées publics » (28/03/2024) ; « Rentrée des lycées 2026 : les travaux à Paris (75) » et « … en Seine-Saint-Denis (93) » (31/08/2026) ; dossier de presse « Rentrée scolaire 2026-2027 » (07/09/2026).
- **URL** : https://www.iledefrance.fr/toutes-les-actualites/la-region-ile-de-france-investit-1-milliard-deuros-par-dans-ses-lycees-publics ; https://www.iledefrance.fr/morienter-etudier-me-former/lyceen/rentree-des-lycees-2025-en-ile-de-france/rentree-des-lycees-2026-les-travaux-paris-75 ; https://www.iledefrance.fr/morienter-etudier-me-former/lyceen/rentree-des-lycees-2025-en-ile-de-france/rentree-des-lycees-2026-les-travaux-en-seine-saint-denis-93 ; https://www.iledefrance.fr/sites/default/files/2026-09/ridf-dp-lycees-2026-2027_v35.pdf
- **Fichiers locaux** : `…/officiel/RegionIDF_page_1milliard_lycees_2024-03-28.html`, `…/RegionIDF_page_travaux_lycees_2026_75.html`, `…/RegionIDF_page_travaux_lycees_2026_93.html`, `…/RegionIDF_dossier_presse_rentree_lycees_2026-2027.pdf`.
- **Utilisé** (déclarations de la collectivité, non vérifiables) : dossier de presse, p. 35 (lycées ayant eu plus de 1 M€ de travaux depuis 2016 : 72 sur 93 à Paris, 51 sur 66 dans le 93, soit 77 % ; 362 sur 468 en Île-de-France) ; page du 28/03/2024 (« Plus de 200 lycées publics étaient vétustes en 2016 » ; pour la Seine-Saint-Denis, « Le nombre de lycées vétustes a été divisé par 7 »).
- **Où** : [T] § 4.3.

#### LOC-9 · Villes de Bobigny et de Pantin : [T]
- **Producteurs** : Ville de Bobigny (direction des finances et des achats) ; Ville de Pantin. **Publication** : « Budget de la Ville – CA 2024 – Mémoire de présentation » (2025, fichier daté du 11/04/2025) ; « L'éducation, une priorité » (30/08/2024) ; « Inauguration de la nouvelle école Diderot » (23/08/2024).
- **URL** : https://www.bobigny.fr/fileadmin/images/PDF/vie_municipale_et_citoyenne/vie_municipale/budget/2025/Budget_de_la_Ville_-_CA_2024_-_M%C3%A9moire_de_pr%C3%A9sentation.pdf ; https://www.pantin.fr/la-ville/aller-plus-loin/leducation-une-priorite-5874 ; https://www.pantin.fr/la-ville/en-ce-moment/inauguration-de-la-nouvelle-ecole-diderot-5863
- **Fichiers locaux** : `…/officiel/Bobigny_CA2024_memoire_presentation.pdf`, `…/Pantin_education_une_priorite_2024-08-30.html`, `…/Pantin_inauguration_ecole_Diderot_2024-08-23.html`.
- **Utilisé** : Bobigny, p. 3, 17, 18 et 20 (reconstruction du pôle maternel Anne-Sylvestre / Robespierre : 19,05 M€, 39 % des 48,6 M€ d'équipement de la ville en 2024 ; acomptes de l'ANRU (11,08 M€), de la Région (1,6 M€) et de la Métropole (0,4 M€) ; avec la dotation politique de la ville de l'État, financement proche de 80 % du montant hors taxes) ; Pantin (déclarations de la commune : écoles neuves ; « d'importants travaux » pour « renforcer et stabiliser les bâtiments anciens » des écoles Langevin et Méhul).
- **Où** : [T] § 4.2.

#### AUT-7 · Banque des Territoires, « ÉduRénov – 1er baromètre de la rénovation des écoles » : [T]
- **Producteur** : Banque des Territoires (Caisse des dépôts). **Publication** : octobre 2025.
- **URL** : https://www.banquedesterritoires.fr/sites/default/files/2025-10/Barom%C3%A8tre%20compress%C3%A9%20.pdf
- **Fichier local** : `…/officiel/BdT_EduRenov_barometre_2025.pdf`.
- **Utilisé** : p. 9 (54 % des collectivités interrogées « n'ont qu'une vision partielle de l'état de leur patrimoine scolaire » ; enquête déclarative). Le chiffre de « 10 à 20 % » de bâtiments très dégradés (p. 6 et 15) vient de l'Alliance écologique et sociale, collectif syndical et associatif : non utilisé.
- **Où** : [T] § 4.3.

#### AUT-8 · CSTB, Base de données nationale des bâtiments (BDNB), API ouverte : [T] [H]
- **Producteur** : Centre scientifique et technique du bâtiment (CSTB). **Version** : schéma `api_open_202602a_1`, interrogé le 04/10/2026.
- **URL** : https://api.bdnb.io/v1/bdnb/donnees/batiment_construction ; https://api.bdnb.io/v1/bdnb/donnees/batiment_groupe_complet
- **Fichiers locaux** : `…/officiel/CSTB_BDNB_batiment_construction_RNB_75_93.csv`, `…/officiel/CSTB_BDNB_batiment_groupe_complet_75_93.csv` (réponses de l'API ; liaison avec les établissements par l'identifiant RNB de l'annuaire, DEPP-17).
- **Utilisé** (calcul de l'auteur, indication fragile) : année de construction du bâtiment principal (plus grande emprise) des établissements publics ; médianes : écoles 1927 à Paris et 1971 dans le 93, collèges 1920 et 1994 ; couverture de 46 à 74 % selon le type ; 243 bâtiments parisiens datés de 2020 à 2024 traités comme inconnus.
- **Où** : [T] § 4.4 ; H-B22, anomalie 16.

#### AUT-9 · ADEME, « Inventaire des bâtiments publics des collectivités et de l'État » : [T]
- **Producteur** : ADEME (data.ademe.fr). **Publication** : version du 10/04/2026.
- **URL** : https://data.ademe.fr/data-fair/api/v1/datasets/pxktz0scmweig6lhun2ni-6i
- **Fichiers locaux** : `…/officiel/ADEME_inventaire_batiments_publics_metadonnees_2026-04.json`, `…/ADEME_inventaire_batiments_publics_agregat_usage.json`, `…/ADEME_inventaire_batiments_publics_agregat_detenteur.json`.
- **Utilisé** : les biens des collectivités sont anonymisés (« Bien detenu par un organisme public autre que l'Etat » : 296 681 lignes sur 321 074), sans commune ni département ; on ne peut pas isoler les bâtiments scolaires d'un département.
- **Où** : [T] § 4.3.

#### AUT-10 · Institut des politiques publiques, billet de blog n° 43, « Paris et ses départements limitrophes : quelles inégalités dans les conditions d'enseignement ? » : [T]
- **Producteur** : Institut des politiques publiques (IPP). Auteur : Y. Souidi. **Publication** : 16/10/2025. **Consultation** : 2026-10-05.
- **Nature** : étude d'un institut de recherche, pas une statistique officielle. Les chiffres sont des « traitements de l'IPP » des données ouvertes de la DEPP, dont les erreurs éventuelles sont « de la seule responsabilité de l'auteur ». **Champ : écoles et collèges publics de Paris, des Hauts-de-Seine, de la Seine-Saint-Denis et du Val-de-Marne. Les lycées ne sont pas étudiés.**
- **URL** :
  - billet : <https://blog.ipp.eu/2025/10/16/paris-et-ses-departements-limitrophes-quelles-inegalites-dans-les-conditions-denseignement/> ;
  - page de la publication : <https://www.ipp.eu/publication/paris-et-ses-departements-limitrophes-quelles-inegalites-dans-les-conditions-denseignement/>.
- **Fichiers locaux** : `…/seine_saint_denis_paris/etudes/IPP_blog43_Souidi_2025-10-16.html`, `…/etudes/IPP_blog43_figure6_age_colleges.jpeg`, `…/etudes/IPP_blog43_figure7_anciennete_colleges.jpeg`, `…/etudes/IPP_blog43_figure8_statuts_colleges.jpeg`.
- **Utilisé**, après recalcul à partir de la source officielle (DEPP, données ouvertes « Les personnels dans les établissements du second degré », rentrée 2024, § 2 ; script `…/seine_saint_denis_paris/calculs_enseignants_2026-10-05/statuts_colleges_publics_2024.py`, calcul de l'auteur). Les chiffres sont en % des ETP d'enseignants des collèges publics, dans l'ordre Paris, 93 et France :
  - figure 8 : agrégés 16 %, 7 %, 6 % (recalcul : 16,5, 7,5, 6,5 %) ; certifiés 73 %, 79 %, 80 % (73,1, 78,7, 80,4 %) ; contractuels 8 %, 10 %, 7 % (non-titulaires : 8,0, 9,6, 7,2 %) ;
  - figure 6 et texte : moins de 35 ans 16 %, 50 %, 20 % ; 50 ans ou plus 43 %, 15 %, 36 % (recalcul : 16,3, 49,7, 20,1 % ; 43,0, 14,9, 36,1 %, déjà utilisés en H-B21, effet 3) ;
  - figure 7 et texte : en poste depuis plus de 8 ans dans le même collège, 39 %, 29 % et « près de la moitié » (recalcul, 8 ans ou plus : 39,0, 29,0, 46,6 %).
  
  L'écart d'arrondi sur les agrégés (7 % et 6 % publiés pour 7,5 % et 6,5 % recalculés) n'est pas expliqué. On retient les valeurs recalculées.
- **Non utilisé** :
  - taux de remplacement par département (1er degré) et par académie (2nd degré : Paris 97 %, Créteil 93 %, Versailles 94 %) : l'étude définit ces taux, mais ne précise pas le fichier dont ils viennent ;
  - vie scolaire (1,6 ETP pour 100 collégiens dans le 93, 1,3 à Paris, 1,4 en France), taille des classes et concours de professeurs des écoles : non recalculés.
- **Où** : [T] § 1.3 et 2.3 (part des agrégés dans l'effet des corps).

### 11.3 Débat public (non officiel, cité comme tel)

Ces documents ne sont pas des sources de données. Ils sont archivés pour montrer ce qui a été dit, par qui et quand. Dossier : `data/raw/recoupements/seine_saint_denis_paris/debat_public/`.

| Code | Titre | Auteur ou média, date | URL | Fichier local | Utilisé pour |
|---|---|---|---|---|---|
| DEB-1 | Message X d'Édouard Geffray (texte complet) et vidéo jointe (extrait de BFMTV, direct vers 21 h 13, bandeau « Blocus des lycées ») | ministre de l'Éducation nationale, 28/09/2026, 23 h 50 (heure de Paris) | https://x.com/EdouardGeffray/status/2104690255639060716 | `tweet_geffray_2026-09-28_texte_complet.txt` ; `transcription_whisper_small_geffray_BFMTV_2026-09-28.txt` (transcription automatique, à relire à l'écoute) ; `geffray_BFMTV_2026-09-28_image_21h13.png` ; la vidéo n'est pas archivée | « +13 % », 28,6 contre 30,5 (§ 1.1) |
| DEB-2 | « En réponse à la mobilisation des lycéens, Edouard Geffray annonce un plan d'action pour accélérer les remplacements des professeurs » | franceinfo, 02/10/2026 | https://www.franceinfo.fr/societe/education/blocage-des-lycees/edouard-geffray-annonce-un-plan-d-action-pour-accelerer-les-remplacements-des-professeurs_8220190.html | `franceinfo_2026-10-02_plan_remplacements.html` | contexte (§ 1.1) ; sur le « bâti scolaire », pas de décision possible « pour la rentrée 2027 » (§ 4.6) |
| DEB-3 | « « Nos établissements manquent de tout » : l'école de Seine-Saint-Denis au point de bascule » | Café pédagogique, 12/03/2026 | https://www.cafepedagogique.net/2026/03/12/nos-etablissements-manquent-de-tout-lecole-de-seine-saint-denis-au-point-de-bascule/ | `cafepedagogique_2026-03-12_point_de_bascule.html` | 6 200 € contre 8 840 € (§ 1.2) |
| DEB-4 | « Intersyndicale 93 : « l'Etat investit 30% de moins pour nos élèves qu'ailleurs » » | Café pédagogique, 13/03/2026 | https://www.cafepedagogique.net/2026/03/13/intersyndicale-93-letat-investi-30-de-moins-pour-nos-eleves-quailleurs/ | `cafepedagogique_2026-03-13_intersyndicale_30pc.html` | « rabais de 30 % » (§ 1.2) |
| DEB-5 | « Plan d'urgence 93 - pétition intersyndicale - Réparons notre école » | SUD éducation 93, 02/10/2024 | https://www.sudeducation93.org/petition-reparons-notre-ecole-exigeons-un-plan-durgence-pour-leducation-dans-le-93/ | `SUD93_petition_2024-10-02.html` | « 6 200 € contre 8 800 € » (§ 1.2) |
| DEB-6 | « Un plan d'urgence pour le 93 : l'intersyndicale ne lâche rien, le ministère non plus » | Café pédagogique, 05/06/2026 | https://www.cafepedagogique.net/2026/06/05/un-plan-durgence-pour-le-93-lintersyndicale-ne-lache-rien-tout-comme-le-ministere/ | `cafepedagogique_2026-06-05_plan_urgence.html` | 846 M€ (§ 1.2) |
| DEB-7 | « VRAI OU FAUX. L'Etat investit-il 2 000 euros de moins par élève en Seine-Saint-Denis par rapport au reste de la France ? » | franceinfo, 09/05/2024 | https://www.franceinfo.fr/vrai-ou-fake/vrai-ou-faux-l-etat-investit-il-2-000-euros-de-moins-par-eleve-en-seine-saint-denis-par-rapport-au-reste-de-la-france_6522941.html | `franceinfo_2024-05-09_vrai_faux_2000_euros_SSD.html` | origine des 6 263 € ; comparaison du maire à « autour de 8 600 euros » (§ 1.2) |
| DEB-8 | « L'égalité des chances à l'école, le vœu pieux de l'Education nationale » ; « Plus de dépenses pour un écolier parisien qu'en Seine-Saint-Denis ? » | franceinfo, 13/04/2012 et 13/02/2015 | https://www.franceinfo.fr/france/l-egalite-des-chances-a-l-ecole-le-voeu-pieux-de-l-education-nationale_83339.html ; https://www.franceinfo.fr/replay-radio/le-vrai-du-faux/plus-de-depenses-pour-un-ecolier-parisien-qu-en-seine-saint-denis_1772283.html | `franceinfo_2012-04-13_egalite_chances_47pc.html`, `franceinfo_2015-02-13_vrai_du_faux_Paris_SSD.html` | chiffres de 2010 d'un rapport provisoire non publié de la Cour des comptes (§ 1.3) |
| DEB-9 | « Rentrée 2025 en Val-de-Marne et Seine-Saint-Denis : moins d'élèves en primaire, plus au lycée » | Citoyens.com, 04/02/2025 | https://citoyens.com/2025/rentree-2025-en-val-de-marne-et-seine-saint-denis-moins-deleves-en-primaire-plus-au-lycee,04-02-2025.html | `citoyens_2025-02-04_rentree2025_93_94.html` | P/E prévu de 6,70 dans le 93 selon la directrice académique (§ 1.1) |
| DEB-10 | « Où en est le plan collèges d'1 milliard d'euros en Seine-Saint-Denis ? » | Citoyens.com, 19/02/2025 | https://citoyens.com/2025/ou-en-est-le-plan-colleges-d1-milliard-deuros-en-seine-saint-denis,19-02-2025.html | `citoyens_2025-02-19_plan_colleges_1Md_SSD.html` | incident rapporté (plafond effondré dans une classe d'un collège d'Épinay-sur-Seine, octobre 2024) ; bilan du plan collèges attribué au président du Département, non retrouvé dans un document officiel (§ 4.3) |
| DEB-11 | « Revendications locales, vidéos virales, soutien de LFI… Comment le blocage de quelques lycées s'est transformé en un mouvement d'ampleur » | franceinfo (L. Rivière), 01/10/2026 | https://www.franceinfo.fr/societe/education/blocage-des-lycees/la-mobilisation-a-pris-une-ampleur-inattendue-comment-le-mouvement-de-blocage-des-lycees-s-est-propage-en-france_8216054.html | `franceinfo_2026-10-01_mouvement_blocage_lycees.html` | Créteil (lycée Saint-Exupéry), « épicentre » du mouvement après de premiers blocus en Bretagne, dans le Nord et le Calvados ; « une grosse dizaine » de lycées bloqués le 25/09 selon le rectorat ; revendications de l'Union syndicale lycéenne (§ 4.6) |
| DEB-12 | « La mobilisation lycéenne se propage en Île-de-France » | Café pédagogique (D. Gani, citant l'AFP), 28/09/2026 | https://www.cafepedagogique.net/2026/09/28/la-mobilisation-lyceenne-se-propage-en-ile-de-france/ | `cafepedagogique_2026-09-28_mobilisation_lyceenne_IDF.html` | revendications « encore très variables selon les établissements », selon le rectorat de Créteil (§ 4.6) |
| DEB-13 | « Colère lycéenne : Édouard Geffray propose un plan d'action, un appel à la mobilisation est lancé pour mardi » | Orange Actualités (P. Rouvière Flamand, 6Médias avec L'Express, d'après franceinfo), 03/10/2026 | https://actu.orange.fr/france/colere-lyceenne-edouard-geffray-propose-un-plan-d-action-un-appel-a-la-mobilisation-est-lance-pour-mardi-magic-CNT000002si2Co.html | `orange_6medias_2026-10-03_Geffray_plan_action.html` | plan pour accélérer les remplacements ; sur le « bâti scolaire », pas de décision possible « pour la rentrée 2027 » (§ 4.6) |

### 11.4 Non archivé, introuvable ou à vérifier

| Point | Situation au 2026-10-04 | Conséquence |
|---|---|---|
| Note du préfet de la Seine-Saint-Denis (2,3 Md€ de dépense d'éducation de l'État en 2023), citée par franceinfo le 09/05/2024 | Non publiée | Non utilisée comme donnée (H-B20) |
| Calcul du « +13 % » du ministre (28/09/2026) | Introuvable (ministère, DEPP, Assemblée, Sénat, rectorat de Créteil, DSDEN 93) | Non vérifiable ; comparé à B (analyse, § 2.6) |
| Académie de Créteil : chiffres clés et bilan social | Accès automatisé intermittent (protection anti-robot) | P/E prévu de 6,70 pour le 93 connu seulement par la presse (DEB-9) ; à récupérer à la main |
| Arrêté du 28/08/2015 fixant les taux annuels (version consolidée) et décret n° 2020-1299 (prime de fidélisation) | Non archivés : le premier téléchargement correspondait à un autre texte, la page du second ne contenait pas le texte | Montants pris dans l'arrêté du 08/12/2022, la circulaire de 2021 et l'arrêté consolidé du 24/10/2020 (LEG-1, LEG-2) |
| Décret n° 85-1148 et circulaire du 12/03/2001 (indemnité de résidence) | Non archivés | Hypothèse de H-B21 (zone 1 à 3 %) |
| Vidéo jointe au message du ministre (extrait de BFMTV) | Non archivée (droits de la chaîne) ; lien, transcription et image archivés | Citation orale à confirmer à l'écoute |
| Élèves par division au lycée, par département | Non publié en données ouvertes | Le 28,6 du ministre n'est pas vérifiable |
| Rémunération moyenne des enseignants par académie ou département | Non publiée au niveau national | Effet de l'âge estimé indirectement (H-B21) |
| Compte administratif 2025 de la Ville de Paris (présentation fonctionnelle) | Non consulté | Périmètre de la fonction 2 de Paris à vérifier (H-B9) |
| Contributions des collectivités franciliennes à Île-de-France Mobilités pour le transport scolaire | Non recherchées | Effet de H-B14 pour Paris et le 93 non chiffré |
| Indicateur officiel de l'état du bâti scolaire par département ou par établissement | Inexistant (DEPP-16, CDC-15, CDC-16, PAR-7, PAR-8) | État des bâtiments de Paris et du 93 non comparable |
| Résultats de l'enquête de la DEPP « Bâtiments scolaires et conditions d'accueil » (collecte 2026) | Non publiés ; seule une publication nationale est prévue | Pas d'indicateur départemental publié ; données ouvertes aux chercheurs selon l'avis d'opportunité |
| Fiches par lycée du diagnostic régional de 2017 (190 lycées à rénover, 41 %) | Non publiées ; la CRC ne les a pas obtenues (CDC-13, p. 29) | Seule la liste des 30 lycées « très vétustes » de 2016 est publiée (LOC-6) |
| Enquête nationale du ministère sur l'amiante (avril 2024) | Présentée en mars 2025, non publiée (PAR-9) | — |
| Diagnostic de l'exposition des sites scolaires aux vagues de chaleur, par académie (plan du 28/05/2026) | Non publié (PAR-9) | À surveiller |
| Code de l'éducation, art. L. 239-2 (version abrogée) | Consulté sur Légifrance, téléchargement refusé (403) | Suppression mentionnée aussi dans le texte de la question n° 14292 (déclaration du député), pas dans la réponse du ministère (PAR-9) ; la section réglementaire D. 239-25 à D. 239-33 reste affichée « en vigueur » sur Légifrance |
| Documents récents du Département de la Seine-Saint-Denis : budget primitif 2026, compte administratif 2025, bilan à mi-parcours du plan « Éco-collège » (février 2025), Atlas du patrimoine, outils d'évaluation de l'entretien des collèges cités par la CRC | Pages en erreur 404 ou protégées ; non archivés | Bilan du plan connu seulement par la presse (DEB-10) ; état d'entretien des collèges non publié |
| Bilan officiel de l'état des collèges parisiens (CRC, inspection générale, Ville de Paris) | Aucun document trouvé | Pas de comparaison possible des collèges des deux départements |
| Diagnostic des écoles des 39 communes du 93 ; dépenses scolaires qu'elles rangent hors des fonctions « écoles » | Non trouvés (il faudrait lire leurs comptes administratifs) | Correction « Paris au plus » faite d'un seul côté (H-B22) |
| Investissement « écoles » de Paris en 2024 cité au § 3.1 et en H-B21 (64 M€) | 62,4 M€ sur le périmètre des fonctions 20, 21x, 28x et 29 ; 63,7 M€ avec la sous-fonction 258, origine probable des 64 M€ | Écrit « 62 à 64 M€ selon le périmètre » (analyse, § 3.1 ; H-B21 ; H-B22) |
| Paiements de la Région par lycée ou par département ; salaires des agents régionaux par lycée (382 M€ en 2026) | Non publiés ; open data des montants votés arrêté au 17/11/2023 | Lycées comparés en montants votés et en dotations, pas en paiements |
| Communiqués du ministère, du rectorat de Créteil et de la Région sur le blocus des lycées | education.gouv.fr et ac-creteil.fr inaccessibles (protection anti-robot) | Déclarations connues par la presse (DEB-2, DEB-11 à DEB-13) |

---

## Annexe A. URL exactes des requêtes d'API

### A.1 DGFiP, balances nature × fonction 2025 (COL-1)

Chaque requête a été relancée le 2026-10-04 : le fichier obtenu est identique, octet pour octet, au fichier local de `data/raw/collectivites/`. Ces URL exactes ne figuraient pas dans `data/raw/collectivites/SOURCES.md`, qui ne donnait que les paramètres.

A.1-1 · `DGFiP_balances_nature-fonction_2025_communes_ecoles_fonct_par_commune_API.csv` (lu par le script 04) :
```
https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/exports/csv?select=categ%2Cndept%2Cinsee%2Csiren%2Csum%28obnetdeb%29+as+obnetdeb%2Csum%28obnetcre%29+as+obnetcre%2Csum%28oobdeb%29+as+oobdeb%2Csum%28oobcre%29+as+oobcre%2Ccount%28%2A%29+as+nb_lignes&where=%28categ%3D%22Commune%22+or+categ%3D%22PARIS%22%29+and+cbudg%3D%221%22+and+%28startswith%28fonction%2C%2220%22%29+or+startswith%28fonction%2C%2221%22%29+or+startswith%28fonction%2C%2228%22%29+or+startswith%28fonction%2C%2229%22%29+or+startswith%28fonction%2C%229020%22%29+or+startswith%28fonction%2C%229021%22%29+or+startswith%28fonction%2C%229028%22%29+or+startswith%28fonction%2C%229029%22%29+or+startswith%28fonction%2C%229320%22%29+or+startswith%28fonction%2C%229321%22%29+or+startswith%28fonction%2C%229328%22%29+or+startswith%28fonction%2C%229329%22%29%29+and+startswith%28compte%2C%226%22%29+and+not+startswith%28compte%2C%2266%22%29+and+not+startswith%28compte%2C%22675%22%29+and+not+startswith%28compte%2C%22676%22%29+and+not+startswith%28compte%2C%2268%22%29&group_by=categ%2Cndept%2Cinsee%2Csiren&delimiter=%3B
```

A.1-2 · `DGFiP_balances_nature-fonction_2025_communes_ecoles_invest_par_commune_API.csv` :
```
https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/exports/csv?select=categ%2Cndept%2Cinsee%2Csiren%2Csum%28obnetdeb%29+as+obnetdeb%2Csum%28obnetcre%29+as+obnetcre%2Csum%28oobdeb%29+as+oobdeb%2Csum%28oobcre%29+as+oobcre%2Ccount%28%2A%29+as+nb_lignes&where=%28categ%3D%22Commune%22+or+categ%3D%22PARIS%22%29+and+cbudg%3D%221%22+and+%28startswith%28fonction%2C%2220%22%29+or+startswith%28fonction%2C%2221%22%29+or+startswith%28fonction%2C%2228%22%29+or+startswith%28fonction%2C%2229%22%29+or+startswith%28fonction%2C%229020%22%29+or+startswith%28fonction%2C%229021%22%29+or+startswith%28fonction%2C%229028%22%29+or+startswith%28fonction%2C%229029%22%29+or+startswith%28fonction%2C%229320%22%29+or+startswith%28fonction%2C%229321%22%29+or+startswith%28fonction%2C%229328%22%29+or+startswith%28fonction%2C%229329%22%29%29+and+%28startswith%28compte%2C%2220%22%29+or+startswith%28compte%2C%2221%22%29+or+startswith%28compte%2C%2223%22%29%29&group_by=categ%2Cndept%2Cinsee%2Csiren&delimiter=%3B
```

A.1-3 · `DGFiP_balances_nature-fonction_2025_fonction2_et_81_agrege_API.csv` (source des extractions lues par les scripts 04 et 05) :
```
https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/exports/csv?select=categ%2Cctype%2Ccstyp%2Ccacti%2Ccbudg%2Cnomen%2Cfonction%2Ccompte%2Csum%28obnetdeb%29+as+obnetdeb%2Csum%28obnetcre%29+as+obnetcre%2Csum%28oobdeb%29+as+oobdeb%2Csum%28oobcre%29+as+oobcre%2Ccount%28%2A%29+as+nb_lignes&where=%28startswith%28fonction%2C%222%22%29+or+startswith%28fonction%2C%22902%22%29+or+startswith%28fonction%2C%22932%22%29+or+startswith%28fonction%2C%2281%22%29+or+startswith%28fonction%2C%229081%22%29+or+startswith%28fonction%2C%229381%22%29%29&group_by=categ%2Cctype%2Ccstyp%2Ccacti%2Ccbudg%2Cnomen%2Cfonction%2Ccompte&delimiter=%3B
```

A.1-4 · `DGFiP_balances_nature-fonction_2025_communes_BP_toutes_fonctions_agrege_API.csv` (G3) :
```
https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/exports/csv?select=categ%2Cfonction%2Ccompte%2Csum%28obnetdeb%29+as+obnetdeb%2Csum%28obnetcre%29+as+obnetcre%2Csum%28oobdeb%29+as+oobdeb%2Csum%28oobcre%29+as+oobcre%2Ccount%28%2A%29+as+nb_lignes&where=%28categ%3D%22Commune%22+or+categ%3D%22PARIS%22%29+and+cbudg%3D%221%22+and+%28startswith%28compte%2C%226%22%29+or+startswith%28compte%2C%2220%22%29+or+startswith%28compte%2C%2221%22%29+or+startswith%28compte%2C%2223%22%29%29&group_by=categ%2Cfonction%2Ccompte&delimiter=%3B
```

A.1-5 · `DGFiP_balances_nature-fonction_2025_communes_BP_total_toutes_fonctions_fonct_par_commune_API.csv` (G3) :
```
https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/exports/csv?select=categ%2Cndept%2Cinsee%2Csiren%2Csum%28obnetdeb%29+as+obnetdeb%2Csum%28obnetcre%29+as+obnetcre%2Csum%28oobdeb%29+as+oobdeb%2Csum%28oobcre%29+as+oobcre%2Ccount%28%2A%29+as+nb_lignes&where=%28categ%3D%22Commune%22+or+categ%3D%22PARIS%22%29+and+cbudg%3D%221%22+and+startswith%28compte%2C%226%22%29+and+not+startswith%28compte%2C%2266%22%29+and+not+startswith%28compte%2C%22675%22%29+and+not+startswith%28compte%2C%22676%22%29+and+not+startswith%28compte%2C%2268%22%29&group_by=categ%2Cndept%2Cinsee%2Csiren&delimiter=%3B
```

A.1-6 · `DGFiP_balances_nature-fonction_2025_communes_BP_total_toutes_fonctions_invest_par_commune_API.csv` (G3) :
```
https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/exports/csv?select=categ%2Cndept%2Cinsee%2Csiren%2Csum%28obnetdeb%29+as+obnetdeb%2Csum%28obnetcre%29+as+obnetcre%2Csum%28oobdeb%29+as+oobdeb%2Csum%28oobcre%29+as+oobcre%2Ccount%28%2A%29+as+nb_lignes&where=%28categ%3D%22Commune%22+or+categ%3D%22PARIS%22%29+and+cbudg%3D%221%22+and+%28startswith%28compte%2C%2220%22%29+or+startswith%28compte%2C%2221%22%29+or+startswith%28compte%2C%2223%22%29%29+and+not+startswith%28compte%2C%22204%22%29&group_by=categ%2Cndept%2Cinsee%2Csiren&delimiter=%3B
```

A.1-7 · `DGFiP_balances_nature-fonction_2025_GFP_ecoles_par_GFP_et_compte_API.csv` (G3) :
```
https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2025/exports/csv?select=categ%2Cndept%2Cinsee%2Csiren%2Clbudg%2Ccompte%2Csum%28obnetdeb%29+as+obnetdeb%2Csum%28obnetcre%29+as+obnetcre%2Csum%28oobdeb%29+as+oobdeb%2Csum%28oobcre%29+as+oobcre%2Ccount%28%2A%29+as+nb_lignes&where=%28categ%3D%22GFP%22+or+categ%3D%22ML%22+or+categ%3D%22EPT%22%29+and+cbudg%3D%221%22+and+%28startswith%28fonction%2C%2220%22%29+or+startswith%28fonction%2C%2221%22%29+or+startswith%28fonction%2C%2228%22%29+or+startswith%28fonction%2C%2229%22%29+or+startswith%28fonction%2C%229020%22%29+or+startswith%28fonction%2C%229021%22%29+or+startswith%28fonction%2C%229028%22%29+or+startswith%28fonction%2C%229029%22%29+or+startswith%28fonction%2C%229320%22%29+or+startswith%28fonction%2C%229321%22%29+or+startswith%28fonction%2C%229328%22%29+or+startswith%28fonction%2C%229329%22%29%29+and+%28startswith%28compte%2C%226%22%29+or+startswith%28compte%2C%2220%22%29+or+startswith%28compte%2C%2221%22%29+or+startswith%28compte%2C%2223%22%29%29&group_by=categ%2Cndept%2Cinsee%2Csiren%2Clbudg%2Ccompte&delimiter=%3B
```

### A.2 data.education.gouv.fr (§ 2)

Préfixe : `https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/`. Exemples complets (les autres requêtes suivent le tableau du § 2) :
```
https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ecoles-effectifs-nb_classes/exports/csv?delimiter=%3B&where=year(rentree_scolaire)%3D2024
https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-indicateurs_personnels_etablissements2d/exports/csv?delimiter=%3B&where=annee_de_la_rentree_scolaire%3D%222024%22
https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-moyens_enseignants_2d_public/exports/csv?delimiter=%3B&where=year(annee)%3D2024
https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ips-ecoles-ap2022/exports/csv?delimiter=%3B&where=rentree_scolaire%3D%222024-2025%22
https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-annuaire-education/exports/csv?delimiter=%3B
```

### A.3 OCDE, flux SDMX de la dépense par élève (OCDE-1)

```
https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_UOE_FIN@DF_UOE_INDIC_FIN_PERSTUD,3.2/FRA+OECD+EU25.FIN_PERSTUD.ISCED11_0+ISCED11_02+ISCED11_1+ISCED11_2+ISCED11_3+ISCED11_34+ISCED11_35+ISCED11_2_3+ISCED11_1T4._T+S13+S1D_NON_EDU.INST_EDU+INST_EDU_PUB+INST_EDU_PRIV.DIR_EXP+CORE+ASERV.V.USD_PPP_ST+XDC_ST.?startPeriod=2019&dimensionAtObservation=AllDimensions&format=csvfilewithlabels
```
Les valeurs retéléchargées le 2026-10-04 sont identiques au fichier local. Seule la langue des colonnes de libellés dépend de la langue demandée par le navigateur.

### A.4 Autres exports et fichiers utilisés par les extractions (G3, contrôle)

Toutes ces URL ont été vérifiées le 2026-10-04 : le fichier obtenu est identique au fichier local de `data/raw/collectivites/` ou de `data/raw/budget_etat/`.

`MEN_effectifs_par_ecole_rentrees2024-2025_extrait_API.csv` :
```
https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ecoles-effectifs-nb_classes/exports/csv?select=rentree_scolaire%2Cnumero_ecole%2Csecteur%2Ccode_departement%2Cnombre_total_eleves%2Cnombre_eleves_preelementaire_hors_ulis%2Cnombre_total_classes&where=year%28rentree_scolaire%29%3E%3D2024&delimiter=%3B
```
`MEN_effectifs_par_ecole_rentrees2024-2025_libelles_communes_API.csv` :
```
https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-ecoles-effectifs-nb_classes/exports/csv?select=rentree_scolaire%2Cnumero_ecole%2Csecteur%2Ccode_departement%2Ccode_commune_insee%2Ccommune%2Cdenomination_principale%2Cpatronyme%2Cnombre_total_eleves&where=year%28rentree_scolaire%29%3E%3D2024&delimiter=%3B
```
`MEN_annuaire_education_ecoles_UAI_commune_extrait_API.csv` :
```
https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-annuaire-education/exports/csv?select=identifiant_de_l_etablissement%2Ctype_etablissement%2Cstatut_public_prive%2Ccode_commune%2Cnom_commune%2Ccode_departement%2Cetat%2Crpi_concentre%2Crpi_disperse&where=type_etablissement%3D%22Ecole%22&delimiter=%3B
```
`OFGL_base_communes_2025_BP_population_EPCI_depenses_API.csv` (OFGL, « Comptes des communes 2018-2025 ») :
```
https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/ofgl-base-communes/exports/csv?select=exer%2Ccateg%2Ccom_code%2Ccom_name%2Cinsee%2Csiren%2Cdep_code%2Cptot%2Ctranche_population%2Crural%2Cepci_code%2Cepci_name%2Cagregat%2Cmontant&where=year%28exer%29%3D2025+and+type_de_budget%3D%22Budget+principal%22+and+agregat+in+%28%22D%C3%A9penses+totales+hors+remb%22%2C%22D%C3%A9penses+de+fonctionnement%22%2C%22D%C3%A9penses+d%27investissement+hors+remb%22%2C%22Charges+financi%C3%A8res%22%2C%22Frais+de+personnel%22%29&delimiter=%3B
```
`DGCL_bilan_dotations_investissement_2024.pdf` (DGCL, « Les dotations de soutien à l'investissement des collectivités territoriales en 2024 ») :
```
https://www.collectivites-locales.gouv.fr/files/files/2.%20G%C3%A9rer%20les%20finances%20publiques%20locales/2.%20L'ex%C3%A9cution%20des%20recettes%20et%20des%20d%C3%A9penses/4.%20R%C3%A9gies%20d'avances%20et%20de%20recettes/Recette%20locales/Dotations/Bilans%20annuels%20des%20dotations/Bilans+dotations+d'investissement+2024.pdf
```

---

### A.5 Requêtes du dossier « collèges, lycées et bâtiments » (COL-4, COL-5, DEPP-17, LOC-7, AUT-8)

Les requêtes exactes sont archivées avec les extractions, dans `data/raw/recoupements/seine_saint_denis_paris/officiel/` :
- DGFiP, balances 2012-2025 : `DGFiP_balances_2012-2025/_urls_requetes_ecoles_2021-2025.txt` (écoles, et effectifs de la DEPP), `_urls_extraction_colleges_2012_2024.json` et `_urls_extraction_colleges_2025.json` (collèges) ; identifiants des jeux annuels : `DGFiP_identifiants_jeux_2012-2025.json` ;
- OFGL : export de COL-5 (voir § 4) et requêtes de méthodologie données dans la fiche COL-5 ;
- data.education.gouv.fr, Région Île-de-France (data.iledefrance.fr) et CSTB (api.bdnb.io) : URL de chaque export dans le `SOURCES.md` du dossier (colonne URL).

## Annexe B. Vérification des liens (2026-10-04)

- **Méthode** : chaque URL des `SOURCES.md` de `data/raw/` et de ce fichier a été appelée le 2026-10-04, avec des en-têtes de navigateur. Pour les fichiers, le contenu téléchargé a été comparé au fichier local (empreinte MD5). Les scripts de vérification ont été exécutés hors du dossier du projet.
- **Résultat** :
  - tous les fichiers lus par les scripts répondent (HTTP 200) et sont identiques aux fichiers locaux ;
  - exception : l'annuaire de l'éducation, mis à jour chaque jour, dont le contenu est identique mais l'ordre des lignes différent ;
  - exception : le flux OCDE de l'annexe A.3, dont seule la langue des libellés change ;
  - les autres fichiers archivés sont identiques, sauf les PDF de plus de 30 Mo (*Géographie de l'École 2026*, *L'état de l'École 2025*), pour lesquels seule la réponse HTTP 200 a été contrôlée.
- **Pages d'accueil** (education.gouv.fr, Légifrance, oecd.org, Education GPS) : elles refusent les requêtes automatisées sans en-têtes de navigateur (403), mais répondent normalement (200) avec un navigateur.
- **Liens en erreur** :
  - DOI de la NI 26.42 (404, non encore enregistré) ;
  - fiches Eurostat `educ_uoe_fin_esms` et rapport qualité France (404, documentés comme inexistants) ;
  - page des notes techniques *EAG 2026* de l'OCDE (403) ;
  - budget.gouv.fr (bloqué).
- **Ajout du 2026-10-05** : les URL de AUT-10 répondent (HTTP 200) ; le billet et ses figures 6 à 8 ont été archivés le jour même.
- **Documents retrouvés pendant la compilation** : NI 26.35 (DEPP-9) et chapitre 3 des *Perspectives budgétaires* 2025 de l'IPP (AUT-2). Leur contenu a été vérifié, puis ils ont été archivés dans `data/raw/` le 2026-10-04.
