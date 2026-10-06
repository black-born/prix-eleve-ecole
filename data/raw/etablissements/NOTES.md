# NOTES — Axe B : données officielles par établissement (approche « bottom-up »)

Synthèse rédigée le 2026-10-04. Les sources et les URL exactes sont dans `SOURCES.md`.

Tous les chiffres ci-dessous sont recalculés par `_exploration.py`. Leur sortie complète est `_exploration_output.txt` ; les numéros de section (§) y renvoient.

## 1. Ce qui existe, et pour quelles rentrées

| Besoin de l'approche B | Jeu open data (DEPP) | Rentrées disponibles au 2026-10-04 | Retenu |
|---|---|---|---|
| ETP d'enseignants par école | `fr-en-indicateurs_personnels_etablissements1d` | 2024, 2025 | **2025** (et 2024) |
| ETP par établissement du 2nd degré (corps, vie scolaire, total) | `fr-en-indicateurs_personnels_etablissements2d` | **2024 seulement** | **2024** |
| Élèves par école | `fr-en-ecoles-effectifs-nb_classes` | 2009 à 2025 | 2025 (et 2024) |
| Élèves par établissement du 2nd degré | collège, lycée GT, LP et **hébergement** (une ligne par UAI) | 2019/2020 à 2025 | **2024** (et 2023, 2025 pour information) |
| Heures d'enseignement par établissement et niveau (H/E) | `fr-en-moyens_enseignants_2d_public` / `_prive` | 2023 à 2025 | 2024 |
| Caractéristiques | annuaire, cités scolaires, IPS (écoles 2024-2025 au plus tard ; collèges, lycées et EREA jusqu'en 2025-2026), REP/REP+ | — | — |

**Champ, producteur et licence de ces jeux**

Tous sont publiés sous Licence Ouverte v2.0 (Etalab).

| Jeux | Producteur | Champ public / privé | Territoire et observation |
|---|---|---|---|
| Personnels 1d et 2d | DEPP, bureau des études statistiques sur les personnels ; panel des personnels issu de BSA | Public et privé sous contrat | Observation au 30/11 |
| Effectifs (écoles, collèges, lycées GT, LP, hébergement) | DEPP, bureau des études statistiques sur les élèves ; constat de rentrée du 1er degré et SI Scolarité | Établissements publics et privés sous contrat sous tutelle du MEN | France, COM et Nouvelle-Calédonie. Secret statistique sous 5 élèves |
| H/E | DEPP, bases-relais | Deux jeux séparés : public, et privé sous contrat | — |
| IPS | DEPP, bureau des études sur les établissements | Public et privé sous contrat | — |
| Annuaire | DNE (données ONISEP et RAMSESE) | Établissements ouverts, publics et privés | Mise à jour quotidienne |
| Cités scolaires | MEN | Public et privé | Mise à jour quotidienne |
| Liste EP | DGESCO | — | — |

**Dernière rentrée commune aux fichiers de personnels et d'effectifs :**
- **1er degré : rentrée 2025.** Personnels observés au 30/11/2025, effectifs au 15/09/2025. La rentrée précédente, 2024, est aussi exportée.
- **2nd degré : rentrée 2024.** Personnels observés au 30/11/2024, effectifs au 01/10/2024. Le fichier des personnels du 2nd degré n'a jamais publié 2023 (le jeu a été créé en juillet 2025) ni encore 2025. Ses métadonnées annoncent pourtant une « date d'observation 30/11/2025 », ce qui est incohérent avec les données. Les effectifs 2023 et 2025 sont conservés, mais ne peuvent pas être appariés à des ETP.

## 2. Conventions retenues (à reporter dans le fichier d'hypothèses)

1. **Périmètre « France » de la DEPP.** Il comprend :
   - la métropole ;
   - les DROM : 971, 972, 973, 974 et 976 (Mayotte comprise) ;
   - Saint-Barthélemy (977) et Saint-Martin (978), rattachés à l'académie de Guadeloupe.

   Sont exclus Saint-Pierre-et-Miquelon (975), Wallis-et-Futuna (986), la Polynésie française (987) et la Nouvelle-Calédonie (988, codée 983 dans le fichier des personnels du 1er degré). Ce périmètre **redonne exactement les totaux nationaux d'élèves** (§ 4.1, voir § 4 ci-dessous).
2. **Clé d'appariement : l'UAI.** Selon le fichier, elle s'appelle `identifiant_de_l_etablissement`, `numero_ecole`, `numero_college`, `numero_lycee` ou `uai`. Aucun doublon de clé n'existe dans les fichiers de personnels, d'effectifs, d'IPS ou de cités. L'annuaire contient 77 UAI en double (une seule ligne est gardée) et la liste EP une seule (0572690P).
3. **Élèves du 2nd degré par UAI : jeu « hébergement ».** Il est égal, UAI par UAI, à la somme des fichiers collège, lycée GT et LP (99,91 % d'égalité exacte, écart maximal de 14 élèves dû au secret statistique, § 3.2). Un UAI présent dans plusieurs fichiers n'est donc **pas un doublon** :
   - lycées polyvalents : LGT + LP (526 UAI) ;
   - LP avec 3e prépa-métiers : collège + LP (837 UAI, LP et EREA) ;
   - établissements collège + LGT + LP (460 UAI) ;
   - cités scolaires à UAI unique : collège + LGT (27).

   Il faut sommer les fichiers par UAI ou prendre directement le jeu hébergement. Totaux France 2024 des fichiers de niveau : collège 3 386 798 (dont SEGPA 83 006 et ULIS 52 140), lycée GT 1 598 768, LP 650 073, EREA 9 299 (jeu hébergement).
4. **Post-bac (STS, CPGE) dans les lycées.** On compte 290 544 étudiants en 2024 (public 230 765, privé 59 779), hors du champ « élève ». Leur part des ETP d'enseignants est estimée UAI par UAI : c'est la part des heures STS + CPGE dans les heures totales du jeu H/E (part utilisée pour 10 682 UAI). À défaut, on prend la part des élèves du supérieur (9 UAI), sinon 0 (6 UAI). Résultat : **29 411,1 ETP imputés au post-bac (6,66 % des ETP des établissements du 2nd degré)**, soit 23 372,9 dans le public et 6 038,2 dans le privé. Cela suppose que les ETP sont proportionnels aux heures d'enseignement (hypothèse).
5. **ETP masqués (« ss »).** Dans les établissements de moins de 5 ETP, tous les ETP enseignants du fichier 2d sont masqués (44 lignes). On les impute par `etp_total`, borne haute : au plus 123,46 ETP, dont 2 Maisons d'éducation de la Légion d'honneur non appariées. Dans le fichier 1d, seules les caractéristiques fines sont masquées ; le total des ETP est toujours renseigné.
6. **Classement des enseignants.** Les fichiers rattachent les enseignants au **degré de l'établissement**. Le Panorama et le RERS les classent par **corps**. Les « titulaires d'un autre corps » des établissements du 2nd degré (9 408 ETP dans le public, 1 058 dans le privé) sont pour l'essentiel des professeurs des écoles enseignant en SEGPA, ULIS ou EREA. Le RERS 2025 (fiche 9.02) compte 9 534 personnes du corps du 1er degré et 159 d'autres corps dans la mission « enseignement du 2nd degré public » (§ 4.3).
7. **Ce que contiennent les fichiers de personnels (métadonnées).**
   - Champ : enseignants **affectés** dans les écoles et établissements publics et privés sous contrat. Les enseignants des établissements hospitaliers et médico-sociaux sont exclus.
   - 2nd degré public : on dispose aussi de l'ETP de vie scolaire (non défini dans les métadonnées ; vraisemblablement CPE et assistants d'éducation) et de `etp_total`, qui couvre tous les personnels rémunérés par le MEN sauf les AESH. Les AESH sont exclus car mutualisés entre établissements.
   - Privé : seuls les enseignants sont renseignés, la vie scolaire est marquée « nc ».
   - Public, ETP « autres » (`etp_total` − enseignants − vie scolaire) : 71 835,5 ETP (direction, administration, santé-social…).
8. **Cités scolaires** (806 cités, 1 742 UAI ; 1 370 UAI du 2nd degré appariées en font partie). Les rapports élèves/ETP par UAI des cités ont la même dispersion qu'hors cité (§ 3.6) : **pas de distorsion visible** de l'affectation des enseignants. Agréger les UAI d'une cité reste prudent pour répartir les dépenses communes.
9. **Trois lycées agricoles publics** (0350700W, 0340128E, 0763004C) ont 75,3 ETP de l'Éducation nationale sous leur UAI, alors que leurs 1 011 élèves sont rattachés à l'UAI d'une « section » (0352867B, 0341915X, 0763079J). Un appariement manuel est possible (hypothèse).

## 3. Chiffres clés calculés (France, open data DEPP)

### 3.1 Premier degré, rentrée 2025 (§ 2.1)

**Écoles et élèves**
- Écoles des effectifs : public 42 396, privé 4 583, soit 46 979.
- Élèves : public 5 315 615, privé 839 284, soit **6 154 899**.

**Appariement par UAI avec les personnels**
- 46 970 écoles appariées : 99,98 % des écoles, 99,99 % des élèves et 99,93 % des ETP.
- 37 UAI ne figurent que dans les personnels (233,5 ETP) : surtout l'école européenne 0573745L (60 ETP) et les écoles françaises d'Andorre (UAI 130xxxx, dép. 66).
- 9 écoles ne figurent que dans les effectifs (354 élèves).

**ETP d'enseignants des écoles, France**
- Public 277 148,2 ; privé 37 181,3 ; total 314 329,5.
- Dans les écoles appariées : public 276 931,3 et privé 37 164,7.

**Élèves par ETP (écoles appariées)**

| Type d'école | Public |
|---|---:|
| Toutes écoles | **19,19** |
| Maternelles | 19,85 |
| Élémentaires | 18,65 |
| Primaires | 19,42 |

Dans le privé, on compte **22,58** élèves par ETP. On compte 1,08 ETP par classe dans le public et 1,07 dans le privé.

Rentrée 2024 (§ 2.2) : 6 261 750 élèves ; 316 529,4 ETP (public 279 172,7, privé 37 356,7) ; 19,40 élèves par ETP dans le public et 22,76 dans le privé.

### 3.2 Second degré, rentrée 2024 (§ 3.1 à 3.5)

**Établissements**
- Fichier des personnels : 10 697 UAI (public 7 803, privé 2 894).
- Effectifs, France : 10 703 UAI.
- Appariées : 10 692 UAI, soit 99,95 % des UAI des personnels et 99,90 % des UAI d'effectifs ; elles couvrent 99,97 % des élèves et 99,98 % des ETP.

**Élèves (France)** : 5 635 688 au total, dont public 4 444 244 et privé 1 191 444. Dans les UAI appariées : 5 633 720.

**ETP d'enseignants, avec imputation des « ss »**

| Corps | Public | Privé |
|---|---:|---:|
| Agrégés | 50 997,2 | 4 205,6 |
| Certifiés et PEPS | 216 723,0 | 56 606,3 |
| PLP | 47 148,1 | 9 761,6 |
| Autres titulaires | 9 408,3 | 1 058,3 |
| Non titulaires | 31 355,8 | 14 188,8 |
| **Total** | **355 638,1** | **85 938,3** |

Ensemble : 441 576,4 ETP.

**Autres personnels**
- Public : ETP de vie scolaire 59 807,1 et ETP total 487 280,6.
- Privé : ETP total 86 409,9.

**ETP hors post-bac (UAI appariées)** : public 332 187,8, privé 79 900,1, ensemble 412 087,9.

**Élèves par ETP enseignant hors post-bac** : public **13,37**, privé **14,91**, ensemble **13,67** (soit 7,31 ETP pour 100 élèves). Par type, dans le public :

| Type d'établissement (public) | Élèves par ETP |
|---|---:|
| Collège | 14,85 |
| LGT | 13,90 |
| Lycée général | 13,52 |
| Lycée polyvalent | 11,61 |
| LP | 8,80 |
| EREA | 4,67 |

Dans le privé : collège 17,28, LGT 14,17, lycée polyvalent 11,30, LP 9,23.

**SEGPA et ULIS (collèges publics)**
- 1 360 collèges ont une SEGPA (76 234 élèves) ; on compte 47 299 élèves en ULIS collège.
- Les collèges avec SEGPA ont 4,25 ETP « autres titulaires » en moyenne, contre 0,66 sans SEGPA ; 13,77 élèves par ETP, contre 15,37 sans SEGPA.

**EREA** : 77 établissements, 9 299 élèves, 1 973,2 ETP, soit 4,71 élèves par ETP. **Aucun effectif national d'élèves d'EREA n'est publié par la DEPP** ; ce total est obtenu par sommation des établissements.

## 4. Couverture par rapport aux chiffres nationaux de la DEPP (§ 4)

### 4.1 Élèves : couverture complète

| | Somme des établissements | Total DEPP | Couverture |
|---|---:|---:|---:|
| 1er degré 2025 | 6 154 899 | 6 154 916 (NI 25.58) | 100,000 % |
| 1er degré 2024 | 6 261 750 | 6 261 780 | 100,000 % |
| 2nd degré 2024 | 5 635 688 | 5 635 691 (NI 25.59) | 100,000 % |
| 2nd degré 2025 | 5 620 979 | 5 620 979 | 100 % exact |

Les écarts résiduels, au plus 30 élèves, viennent du secret statistique sur les effectifs inférieurs à 5.

### 4.2 ETP d'enseignants : 89,2 % sont rattachés à un établissement

Comparaison avec le Panorama 2024-2025 (figure 2.1, p. 32, au 30/11/2024) et le Panorama 2025-2026 (xlsx, onglet 2.1, au 30/11/2025).

| | ETP des établissements | ETP DEPP (Panorama) | Couverture |
|---|---:|---:|---:|
| **Total 2024 (1er + 2nd degré, public + privé)** | **758 105,8** | **850 159** | **89,2 %** (92 053 ETP non rattachés) |
| 1er degré public 2024 | 279 172,7 | 342 930 | 81,4 % |
| 1er degré public 2025 | 277 148,2 | 342 449 | 80,9 % |
| 1er degré privé 2024 | 37 356,7 | 42 344 | 88,2 % |
| 1er degré privé 2025 | 37 181,3 | 42 231 | 88,0 % |
| 2nd degré public 2024 | 355 638,1 | 377 629 | 94,2 % |
| 2nd degré privé 2024 | 85 938,3 | 87 256 | 98,5 % |

Corrigé du classement par corps (les « autres titulaires » des établissements du 2nd degré sont rebasculés vers le 1er degré), le 1er degré public passe à 84,2 % et le 2nd degré public à 91,7 %.

**Couverture par corps, 2nd degré 2024** (figures 2.14 et 2.16 du Panorama 2024-2025)

| Corps | Public | Privé |
|---|---:|---:|
| Agrégés et chaires supérieures | 93,4 % | 126,5 % (écart de nomenclature non expliqué) |
| Certifiés et PEPS | 94,3 % | 99,5 % |
| PLP | 92,3 % | 97,2 % |
| Non titulaires | **74,8 %** | 86,4 % |

Les non-titulaires sont les moins bien couverts : ce sont souvent des remplaçants non rattachés.

### 4.3 Où sont les ETP non rattachés ?

D'après la fiche 9.01 du RERS (ETP « consacrés à la mission »).

**Rentrée 2024 (RERS 2025, p. 331)**

| Mission | ETP de la mission | ETP des établissements | Part couverte |
|---|---:|---:|---:|
| Enseignement 2nd degré public | 378 570 | 355 638 | 93,9 % |
| Enseignement 2nd degré privé | 88 716 | 85 938 | 96,9 % |
| Enseignement 1er degré public | 307 791 | 279 173 | 90,7 % |
| Enseignement 1er degré privé | 39 874 (39 873 publié) | 37 357 | 93,7 % |

Détail des missions du 2nd degré :
- public : classes attitrées 343 702, remplacement 20 965, documentation 8 707, besoins spécifiques 5 196 ;
- privé : remplacement 2 791 ETP.

L'écart de 22 932 ETP dans le 2nd degré public correspond à peu près au remplacement (TZR).

Dans le 1er degré public :
- les ETP des écoles représentent 108,8 % des ETP « en classe » (préélémentaire 83 769 + élémentaire 172 715) et 102,9 % de « classes + direction du 1er degré » (direction : 14 869, public et privé confondus) ;
- les écoles comptent donc vraisemblablement le directeur et une partie des besoins spécifiques (ULIS) ;
- le remplacement (32 038) et l'essentiel des RASED (besoins spécifiques, 19 269) sont hors fichier.

**Rentrée 2025 (RERS 2026, p. 341)**
- Enseignement 1er degré public : 306 692 ETP en sommant les lignes ; les écoles en couvrent 90,4 %.
- **Anomalie de la source** : le sous-total publié est **278 146**, alors que la somme des lignes vaut 306 692. Le total « secteur public » publié (684 936) correspond bien à la somme des lignes. Même anomalie dans le privé : **37 595** publié contre 39 756 en sommant les lignes.

**Conséquence pour l'approche B.** Environ 11 % des ETP d'enseignants (92 000 ETP en 2024) ne sont rattachés à aucun établissement : remplacement, RASED, conseillers pédagogiques, enseignants en établissements médico-sociaux ou hospitaliers, agents sans affectation. Il faut les répartir par élève, ou proportionnellement aux ETP rattachés : c'est une hypothèse à documenter. Sinon, l'approche B sous-estime le coût en personnel enseignant.

## 5. Dépenses par établissement en open data officiel : NON au niveau national

- **Budgets et comptes financiers des EPLE** (logiciel Op@le) : aucune publication en open data, ni sur data.education.gouv.fr (306 jeux examinés) ni sur data.gouv.fr. Les comptes remontent aux rectorats et aux collectivités de rattachement, selon des circulaires académiques, sans diffusion publique.
- **Dotation horaire globale (DHG)** : non publiée telle quelle. Le **meilleur substitut officiel** est le numérateur H du jeu H/E : les heures hebdomadaires d'enseignement devant élèves financées par le MEN, par UAI et par niveau. Il couvre tout le 2nd degré public (7 801 UAI en 2024) et privé (2 890 UAI), pour les rentrées 2023 à 2025.

  En 2024, dans le public, on compte 6 373 112 h par semaine, dont 6,18 % en STS et CPGE. Le nombre d'élèves E, hors post-bac, vaut 4 441 977 dans le public, contre 4 444 244 au niveau national.
- **Dotations des collectivités par établissement** : seulement quelques jeux locaux, partiels et hétérogènes.
  - Région **Centre-Val de Loire** : dotations de fonctionnement aux lycées publics, de 2017 à 2025. Pour 2025, 98 lycées et 37 426 870 €, dont DGF 34 544 007 € (fichier téléchargé). 90 de ces UAI se retrouvent dans le jeu hébergement 2025 (68 745 élèves du second degré et 7 513 du post-bac).
  - Région **Île-de-France** : subventions votées aux lycées de 2021 à 2023, environ 213 à 222 M€ par an. Ce sont des montants votés et non exécutés, sans mise à jour depuis mars 2024.
  - **Gironde** : dotations des collèges de 2015 à 2017.
  - Ces jeux ne couvrent ni les personnels territoriaux (agents des EPLE, ATSEM), ni l'investissement (sauf les « opérations directes » de l'Île-de-France), ni les écoles.
- **Écoles** : aucune donnée par école. La dépense communale n'existe que par commune et par fonction (balances DGFiP, OFGL : axe « collectivités »).
- **AESH, ATSEM, agents territoriaux des EPLE** : aucun effectif par établissement en open data.

## 6. Distribution (pondérée par les élèves) et caractéristiques (§ 5)

**Élèves par ETP enseignant, déciles P10 / médiane / P90, pondérés par les élèves**

| Champ | P10 | Médiane | P90 |
|---|---:|---:|---:|
| Écoles publiques 2025 | 15,17 | 20,27 | 23,57 |
| Collèges publics 2024 | 12,55 | 15,35 | 17,25 |
| LGT publics | 12,40 | 14,13 | 15,58 |
| Lycées polyvalents publics | 9,58 | 11,98 | 14,15 |
| LP publics | 7,37 | 9,03 | 10,66 |

**Éducation prioritaire : élèves par ETP**

| | REP+ | REP | Hors EP |
|---|---:|---:|---:|
| Écoles publiques 2025 | 15,43 | 15,64 | 20,44 |
| Collèges publics 2024 | 11,89 | 13,61 | 15,47 |

Dans les collèges, H/E vaut 1,434 en REP+ et 1,176 hors EP. On compte 54,8 élèves par ETP de vie scolaire en REP+, contre 81,8 hors EP.

**IPS 2024-2025, quintiles d'établissements**

| | Q1 (plus défavorisés) | Q5 (plus favorisés) |
|---|---:|---:|
| Collèges publics (élèves par ETP) | 13,07 | 16,45 |
| Écoles publiques avec CM2 (25 758 écoles) | 16,34 | 21,53 |

Les moyens enseignants par élève sont donc plus élevés dans les établissements défavorisés. Cela compte pour la distribution du coût par élève de l'approche B.

## 7. Limites et points d'attention

- 2nd degré : une seule rentrée de personnels (2024). Une estimation pour 2025 devrait appliquer les ratios 2024 aux effectifs 2025 (hypothèse).
- Les ETP sont observés au 30/11, alors que les coûts du RAP et du PAP sont en ETPT sur l'année civile. Une règle de passage est nécessaire.
- Les métadonnées sont en partie incohérentes :
  - le fichier personnels 2d annonce une observation au 30/11/2025 alors qu'il ne contient que 2024 ;
  - le fichier H/E du privé annonce « 2023-2024 » alors qu'il contient 2025.
- Les valeurs du Panorama 2024-2025 et du RERS (fiches 9.01 et 9.02) sont recopiées des PDF, faute de tableur publié. Le script les contrôle automatiquement avec pypdf : 109 valeurs sur 109 sont retrouvées aux pages citées.
- L'IPS des écoles n'est plus actualisé (dernier millésime 2024-2025) et exclut les maternelles (25 758 écoles publiques appariées sur 42 802).
- L'annuaire est un instantané au 03/10/2026 : les établissements fermés depuis 2024 n'y figurent pas (0,3 % des UAI du 2nd degré manquent).
