# NOTES — Axe C : recoupements de l'agrégat public (dépense publique par élève)

**Cible** : dépense publique moyenne par élève (maternelle, élémentaire, collège, lycée). C'est l'agrégat État (tous ministères) + collectivités + autres administrations publiques, **et non l'État seul**.
**Consultation** : 2026-10-04. Montants en euros courants. Md€ = milliards d'euros.
Le détail des fichiers et des URL figure dans `SOURCES.md`. Le fichier `_derive_insee_cofog09_2015-2024_long.csv` reprend toutes les valeurs COFOG 09.x avec leur cellule Excel.

---

## 0. Reprise de l'exécution interrompue
- Fichiers déjà présents et **valides**, donc conservés : `insee_cofog2024_T_3301.xlsx` à `T_3307.xlsx` (xlsx corrects, créés le 2025-11-28), ainsi que `insee_IP2093_*.pdf` et `*.xlsx`.
- Fichiers `_tmp_` **supprimés** :
  - `_tmp_eag2026.pdf` et `_tmp_eag2026_fr.html` : pages Cloudflare « Just a moment », pas des PDF ;
  - `_tmp_insee_*.html` : pages retéléchargées sous un nom explicite ;
  - `_tmp_oecd_dataflows.xml` et `_tmp_oecd_dsd_fin.xml` : remplacés par `oecd_sdmx_structure_*.xml`.
- Aucun gros fichier OCDE ne restait. Les requêtes SDMX de cette exécution sont filtrées sur FRA, OCDE et UE25 et sur un seul indicateur (≤ 1,9 Mo).

---

## 1. (C1) INSEE, comptabilité nationale, COFOG fonction 09 « Enseignement »

### 1.1 Édition et statut
- **Dernière édition disponible** : campagne « Comptes de la Nation 2024 », tableaux 3.301 à 3.307 (section parue le 27/03/2026). Les **données 2024 sont provisoires**.
- La page « Comptes de la Nation 2025 » du 29/05/2026 indique que les tableaux 3.301 à 3.307 (2025 provisoire, 2024 semi-définitif) **seront publiés en décembre 2026**. Ils ne sont donc pas disponibles au 04/10/2026.
- L'IP 2093 annonce une première révision des données 2024 à l'automne 2026 et une version définitive à l'automne 2027.
- **Contrôle croisé Eurostat** (`gov_10a_exp`, mise à jour du 16/09/2026) : les valeurs sont identiques (09.1 = 42 176,4 M€ ; 09.2 = 63 778,9 M€ en 2024). Eurostat marque 2023 et 2024 comme provisoires (`p`) ; 2022 et les années antérieures sont définitives.

### 1.2 Chiffres clés 2024 : APU **consolidées**, France entière, en Md€
Source : `insee_cofog2024_T_3307.xlsx`, onglet `T_3307`, lignes S13, colonne T. Les valeurs sont identiques à `T_3301` (OTE, colonne AH).

| Sous-fonction | 2024 | cellule | 2023 (col. S) |
|---|---|---|---|
| 09 Enseignement (total) | **148,640** | T67 | 141,555 |
| 09.1 Préélémentaire et primaire | **42,176** | T68 | 39,317 |
| 09.2 Secondaire | **63,779** | T69 | 61,316 |
| 09.3 Postsecondaire non supérieur | 1,156 | T70 | 1,066 |
| 09.4 Supérieur | 12,308 | T71 | 13,222 |
| 09.5 Non défini par niveau | 8,622 | T72 | 8,402 |
| 09.6 Services annexes à l'enseignement | **20,023** | T73 | 17,647 |
| 09.7 R-D en enseignement | 0,000 | T74 | 0,011 |
| 09.8 Enseignement n.c.a. | 0,575 | T75 | 0,575 |
| Total des dépenses APU (toutes fonctions) | 1 671,794 | T6 | 1 607,393 |

**Répartition par sous-secteur, en dépenses consolidées** (T_3307, 2024, Md€) :

| | 09.1 | 09.2 | 09.6 | 09.8 |
|---|---|---|---|---|
| État (S13111) | 27,836 (T228) | 44,940 (T229) | 12,194 (T233) | 0,575 (T235) |
| ODAC (S13112) | – | 0,000 (T309) | 0,756 (T313) | – |
| APUL (S1313) | 14,340 (T388) | 18,839 (T389) | 7,073 (T393) | – |
| ASSO (S1314) | – | – | – | – |

**Par nature** (T_3301, APU, 2024, Md€ ; cellules en colonne AH) :

| | Total | Rémunérations D1 | Conso. intermédiaires P2 | Investissement P5L | Autres transferts D7 | Prestations en espèces D62 | Autres |
|---|---|---|---|---|---|---|---|
| 09.1 | 42,176 | 34,256 (AH149) | 2,511 (AH230) | 4,171 (AH878) | 0,709 (AH716) | 0,016 | 0,514 (OED 0,390 ; D9 0,069 ; D3 0,030 ; D632 0,025) |
| 09.2 | 63,779 | 49,762 (AH150) | 5,670 (AH231) | 4,557 (AH879) | 1,558 (AH717) | 1,406 (AH555) | 0,826 (OED 0,596 ; D9 0,214 ; D3 0,014 ; D632 0,002) |
| 09.6 | 20,023 | 9,789 (AH154) | 2,886 (AH235) | 1,012 (AH883) | 1,293 (AH721) | 2,696 (AH559) | 2,347 (D632 1,463 ; D3 0,502 ; D9 0,246 ; OED 0,132 ; D4 0,004) |

Pour 09.1, la somme des composantes (42,177) diffère de 0,001 du total à cause des arrondis de l'INSEE. Légende : OED = autres impôts et ajustements ; D9 = transferts en capital ; D3 = subventions ; D632 = transferts sociaux en nature achetés ; D4 = revenus de la propriété.

### 1.3 Ce que contient (ou non) la COFOG : conventions documentées
1. **Consolidation.** Les lignes S13 (T_3301 et T_3307) excluent les flux internes aux APU. Les transferts État → collectivités ne sont donc pas comptés deux fois.
   - Les transferts sont affectés à la fonction qu'ils financent. Les dotations générales (DGF…) sont classées en 01 « Services généraux » (page INSEE 8988847, « Pour comprendre »). Elles sont donc hors fonction 09.
   - Dans 09.1 et 09.2, les transferts entre sous-secteurs sont faibles en 2024 :
     - État 09.1 : 27,945 non consolidé (T_3303) contre 27,836 consolidé ;
     - État 09.2 : 45,017 contre 44,940 ;
     - APUL 09.2 : 18,871 (T_3305) contre 18,839.
2. **Pensions.** Les cotisations employeurs des fonctionnaires sont comptées en **rémunération (D1) dans chaque fonction** (IP 2093, p.2). Pour l'État, il s'agit de cotisations **imputées**, calées sur le CAS Pensions (pensions de retraite seulement, hors invalidité et hors ex-PTT), selon le blog Insee du 24/10/2025. Les pensions versées relèvent de 10.2 et sont hors 09. Voir le § 7 : cette convention gonfle le coût salarial.
3. **Privé sous contrat.** Les enseignants ont l'État pour employeur (Cour des comptes 2023, p.36). Leur rémunération est donc dans la D1 de l'État, en 09.1 et 09.2. Les forfaits d'externat et communaux sont des transferts aux établissements privés (ISBLSM, hors APU). Les frais de scolarité payés par les familles sont hors COFOG. **Le dénominateur doit donc inclure les élèves du privé sous contrat.**
4. **EPLE et caisses des écoles = ODAL, donc dans les APUL.** La liste INSEE de mai 2026 compte 7 967 EPLE et 1 113 caisses des écoles. Les dépenses des collèges et lycées publics (personnels recrutés par les EPLE, restauration, internat) sont donc en APUL. La COFOG mesure des **dépenses brutes d'unités publiques**, y compris celles financées par les familles (cantine, internat). Ce n'est pas un financement public net.
5. **Apprentissage et formation continue.** Le crédit d'impôt apprentissage est en 09.3 ; les OPCO sont en 04.1 (fiche méthodologique 20, p.3). Les APUL ont 4,275 Md€ en 09.5 (prestations D62 1,315 ; D632 0,923 ; subventions D3 0,694). Ce profil évoque la formation professionnelle des régions. C'est une **inférence**, à exclure du « scolaire ».
6. **Passage des programmes budgétaires à la COFOG : non publié.** L'INSEE ventile les rémunérations de l'État à partir des RAP de chaque programme (fiche méthodologique 20, p.4). Ordres de grandeur (inférences, à ne pas présenter comme une correspondance officielle) :
   - État 09.1 + 09.2, non consolidé (T_3303) = **72,962 Md€**. L'exécution 2024 de P140 + P141 + P139 + P143 vaut **75,554 Md€** (`../budget_etat/NOTES.md`, RAP 2025).
   - État 09.6, non consolidé = 14,499 Md€ (consolidé 12,194). L'exécution 2024 de P230 « Vie de l'élève » vaut 7,934 Md€. Le 09.6 contient donc aussi d'autres dépenses, **probablement la vie étudiante** (bourses sur critères sociaux, CROUS). Pour ordre de grandeur, P231 « Vie étudiante » = 3,206 Md€ en 2025 (PLRG 2025). Le 09.6 mêle donc scolaire et supérieur.
   - La D1 de l'État en 09.6 passe de 5,413 Md€ (2023) à 7,140 Md€ (2024). Ce saut est cohérent avec la bascule en titre 2 des AESH et AED, auparavant payés par subventions aux EPLE : la D7 de l'État en 09.6 passe de 4,220 à 3,296 Md€. Cette lecture est une **inférence de l'agent**, non documentée par l'INSEE.
   - Le **post-bac en lycée** (CPGE, STS) est probablement compté en 09.2 : l'État n'a que 0,633 Md€ consolidé en 09.4. Ordre de grandeur : P141 action 05 ≈ 1,4 Md€ (`../budget_etat/NOTES.md`). C'est une inférence.
7. 09.1 couvre la **maternelle et l'élémentaire** ; 09.2 couvre le collège et le lycée (GT, pro, et l'enseignement agricole du P143 selon toute vraisemblance).

### 1.4 Ratios indicatifs
Ces ratios sont **calculés par l'agent, non officiels**, à refaire par script avec des hypothèses documentées.

Dénominateur : élèves MEN, public + privé sous contrat, France entière avec Mayotte, **année civile 2024 = 2/3 de la rentrée 2023 + 1/3 de la rentrée 2024**, soit **11 963 556** (1er degré 6 313 869 ; 2nd degré 5 649 688). Source : `../effectifs_nationaux/_derive_synthese_effectifs_nationaux_2023_2025.csv`.

| Variante | Montant | Résultat |
|---|---|---|
| Borne basse : 09.1 + 09.2 | 105,955 Md€ | **≈ 8 857 € par élève** |
| Borne haute : 09.1 + 09.2 + 09.6 + 09.8 | 126,553 Md€ | **≈ 10 578 € par élève** |

La borne haute est surévaluée : elle contient la vie étudiante et les dépenses financées par les familles (cantine, internat).

Par niveau :
- 09.1 / élèves du 1er degré ≈ 6 680 € ;
- 09.2 / élèves du 2nd degré MEN ≈ 11 289 €. Ce ratio est surévalué : le numérateur inclut probablement le post-bac et l'agriculture, alors que le dénominateur ne compte ni les élèves de l'enseignement agricole ni les étudiants post-bac.

---

## 2. OCDE, Regards sur l'éducation (EAG)

### 2.1 EAG 2026
EAG 2026 a été lancé le 29/09/2026. L'année de référence financière est **2023**. Source : base OCDE (SDMX, mise à jour du 2026-07-01) et Education GPS.

Définitions :
- Dépense **au titre des établissements d'enseignement** : enseignement et services auxiliaires fournis par les établissements (cantine, internat, transport).
- Par élève en **équivalent temps plein**, avec des effectifs ajustés à l'année financière.
- « Administrations publiques » = ligne **G5** du questionnaire UOE : dépense *directe* de toutes les APU consolidées envers les établissements, donc **après** transferts aux ménages et au privé.
- « Total » = ligne **N5**, toutes sources.
- Hors dépenses des ménages en dehors des établissements (fournitures, etc.).
- CITE 3 inclut l'**apprentissage**, d'où un financement privé important en voie professionnelle.

**France 2023, dépense par élève ETP (DIR_EXP, tous établissements, prix courants)** :

| CITE | Public (G5), € | Public (G5), USD PPA | Moyenne OCDE public, USD PPA | Toutes sources, € | Toutes sources, USD PPA | Moyenne OCDE toutes sources, USD PPA |
|---|---|---|---|---|---|---|
| 02 Préélémentaire | **7 985** | 11 768 | 11 992 | 8 495 | 12 519 | 13 599 |
| 1 Élémentaire | **7 847** | 11 565 | 12 821 | 8 353 | 12 310 | 13 552 |
| 2 Collège | **9 140** | 13 471 | 14 241 | 9 973 | 14 699 | 15 244 |
| 3 Lycée (dont apprentis) | **11 067** | 16 311 | 13 077 | 13 250 | 19 527 | 15 208 |
| 34 Lycée général | 11 314 | 16 674 | 12 279 | 12 332 | 18 175 | 13 225 |
| 35 Lycée professionnel | 10 611 | 15 638 | 13 901 | 14 950 | 22 033 | 16 104 |
| 1-4 Élémentaire à post-sec. non sup. | 9 093 | 13 400 | 13 158 | 10 132 | 14 932 | 14 356 |

Source : `oecd_sdmx_EAG_depense_par_eleve_*.csv`. Les montants de l'UE25 sont dans le même fichier.

- **Part publique 2023** (G5/N5) en France : 94,0 % (CITE 0), 93,95 % (CITE 1), 91,65 % (CITE 2), 83,53 % (CITE 3), **89,74 % (CITE 1-4)**. Pour l'OCDE : 86,65 / 93,38 / 91,99 / 87,75 / **90,58 %**. Source : `oecd_sdmx_EAG_sources_financement_*.csv`.
- **Montants publics 2023 en France (G5)** : CITE 0 = 18 604,2 M€ ; CITE 1 = 32 917,1 M€ ; CITE 2 = 31 911,0 M€ ; CITE 3 = 28 417,5 M€.
- **Effectifs ETP 2023** : 2 329 903 / 4 194 830 / 3 491 280 / 2 567 681. Les CITE 0 à 3 totalisent 111 849,8 M€ pour 12 583 694 ETP, soit **≈ 8 889 € par ETP** (calcul de l'agent). Cet ordre de grandeur est proche de la borne basse COFOG.
- **Education GPS (EAG 2026)** :
  - 12 310 USD par élève de l'élémentaire (OCDE 13 552) ;
  - 18 175 USD au lycée général, 22 033 USD au lycée professionnel ;
  - dépense publique avant transferts, du primaire au supérieur : 4,5 % du PIB (OCDE 4 %), privée 0,8 % (OCDE 0,6 %) ;
  - éducation = 8,1 % des dépenses publiques totales (OCDE 9,8 %).

### 2.2 EAG 2025 (référence 2022)
Note pays France en français, p.7-9 :
- toutes sources : **11 135 USD** à l'élémentaire contre 12 730 pour l'OCDE (-13 %) ; **13 622** au collège contre 14 315 (-5 %) ; **18 127** au lycée contre 14 562 (+24 %) ;
- **dépense publique de 12 321 USD** par élève de l'élémentaire au post-secondaire non supérieur ;
- **92 %** de financement public avant transferts, contre **90,1 %** pour l'OCDE.

Les valeurs 2022 ont été **révisées** dans la base 2026 (PPA et données) : l'élémentaire 2022 vaut 11 326 USD (toutes sources) et 10 623 USD (public). Pour 2022, utiliser la base actuelle plutôt que la note 2025.

**Écarts avec la DEPP** (compte de l'éducation) : périmètre « établissements » contre DIE (la DIE inclut les achats des ménages hors établissements), apprentissage inclus en CITE 3, ETP, et rattachement du post-bac au supérieur.

---

## 3. Cour des comptes
- **NEB 2025 « Enseignement scolaire »** (avril 2026, fichier dans `../budget_etat/`) : la recommandation n° 8, **reconduite et non mise en œuvre**, demande d'« indiquer dès le PLF 2027 … la dépense publique par élève aux différents niveaux de formation » en distinguant public, privé sous contrat et agricole (p.9, p.62). Le ministère juge le calcul « complexe et peu fiable » ; selon la Cour, il figurait pourtant dans les documents budgétaires jusqu'en 2022-2023 (p.62 et 86). **Le PAP 2027 ne le réintroduit pas** (vérification textuelle).
- **Note thématique de juillet 2023** :
  - « Aucune information consolidée permettant de décrire le coût global d'un élève pour chaque niveau d'enseignement, en intégrant à la fois les dépenses de l'État et celles des collectivités territoriales, n'est publiée » (p.8).
  - **Tableau n° 2 (p.16)**, dépense scolaire 2021 (source DEPP ; France métropolitaine + DROM ; public et privé sous contrat, hors supérieur, apprentissage et formation continue) : **total 102,2 Md€ = État 71,1 + collectivités 31,1**. Détail :
    - écoles 41,3 (27,9 + 13,4) ;
    - 2nd degré 51,8 (41,1 + 10,7), dont collèges 27,2 et lycées 24,6 ;
    - hébergement-restauration 5,9 ; transport scolaire 2,2 ; fournitures 0,2 ; médecine scolaire 0,7.
  - **Chiffres clés (p.6)** : « dépense totale 109 Md€ » = État 78,5 + collectivités 31,1. ⚠ Ce total **mélange l'État 2022** (dépense scolaire 78,5 Md€ en 2022, p.11) et **les collectivités 2021**.
  - Concours des collectivités : de 4 500 € par élève et par an (communes à forte fiscalité) à 250 € (petites communes), p.20.
- **Enseignement primaire (mai 2025)**, p.12 :
  - dépense pour l'école primaire de **52 Md€ en 2022** : État 20,1 + pensions 8,9 + collectivités 19 + ménages et acteurs privés ≈ 3 + autres administrations 1 ;
  - 2023 provisoire, en note 4 : 55,1 Md€ (21,9 + 8,8 + 20,6 + 0,8 + 2,9) ;
  - investissement des collectivités dans les établissements publics : 8,4 Md€ en 2022, dont 3,6 Md€ pour les écoles ;
  - p.44 : de 250 à 4 500 € par élève selon les communes.
- **Privé sous contrat (juin 2023)** :
  - P139 exécuté à 8,05 Md€ en 2022 (p.34) ;
  - part de l'État dans le financement : 55 % (1er degré privé) et 68 % (2nd degré privé), contre 59 % et 74 % dans le public ; familles 22 % et 23 % (p.10) ;
  - pas de coût par élève dans les documents budgétaires (p.78) ;
  - forfait d'externat moyen de 537 € en 2020-2021 (p.123 et 140).
- **RPA 2026, « Adapter la carte des collèges »** (25/03/2026), **tableau n° 1, p.143** : **coût salarial de l'État par collégien en 2023** :

  | Taille du collège | Coût par collégien |
  |---|---|
  | moins de 200 élèves | **8 900 €** |
  | moins de 300 élèves | **8 100 €** |
  | 500 à 600 élèves | **6 700 €** |

  - Selon la note 20, le surcoût est d'environ 240 M€ sur près de 17 Md€ de charges et cotisations.
  - Selon la CRC Grand Est, le fonctionnement par élève des collèges de moins de 300 élèves est **50 % plus élevé** pour les départements.
  - Le montant de 647 € de forfait départemental (2024) provient d'une réponse de la FNOGEC : **source non officielle**.
- **Éducation prioritaire (2018)**, tableau n° 2, p.33 : masse salariale de l'État par élève en 2016, en euros.

  | | REP+ | REP | Hors EP |
  |---|---|---|---|
  | Écoles | 3 789 | 3 510 | 3 215 |
  | Collèges | 7 780 | 6 636 | 5 807 |
  | Ensemble | 4 878 | 4 566 | 4 002 |

  Le surcoût est de 1 137 € par élève en REP+ et 693 € en REP. Méthode : masse salariale de l'année N divisée par les élèves de la rentrée N. Données anciennes.
- **RPA 2023, collèges** (p.12-14) :
  - les départements ont consacré 4,9 Md€ aux collèges en 2021 ;
  - **1 720 € par collégien** en 2019 (DEPP, Géographie de l'école 2021), plus de 2 400 € dans 5 départements et moins de 1 400 € dans 15 ;
  - équipement : 684 € par collégien public en moyenne (123 € dans les Ardennes, 1 284 € dans le Val-de-Marne) ;
  - construction : 21 900 € HT par collégien en maîtrise d'ouvrage publique, 24 465 € HT en PPP.

## 4. Rapports parlementaires PLF 2026 : constat négatif
Le rapport général du Sénat n° 139 (annexe 13), la note de présentation de la commission des finances, l'avis n° 144 du Sénat et le rapport AN n° 1996 (annexe 23) **ne produisent aucun chiffre propre** de dépense publique agrégée par élève.

L'avis AN n° 2043, tome IV, reprend la DEPP et l'OCDE (p.35) : la DIE par élève du 1er degré a augmenté de 9 % entre 2017 et 2022 ; en 2021, elle restait inférieure de 11 % à la moyenne de l'OCDE.

Les rapports sur le PLF 2027 ne sont pas encore publiés.

## 5. Communication officielle du ministère
- **DEPP, « L'éducation nationale en chiffres 2026 »** (juillet 2026, fichier dans `../depp_compte_education/`), p.3 : **10 350 € par élève ou apprenti des 1er et 2d degrés** (DIE 2024, **tous financeurs**, ménages et entreprises compris). Détail : 9 080 € pour le 1er degré, 11 660 € pour le 2nd degré, 10 450 € au collège, 13 020 € en lycée GT, 14 700 € en lycée professionnel. Ce n'est **pas** la part publique ; à rapprocher de l'axe A.
- La page education.gouv.fr « Le budget et les finances… », rubrique « coût d'une scolarité », est **obsolète** (données 2019).
- PAP 2027, P143, indicateur 2.1 : **dépense de l'État seul** par élève de l'enseignement agricole technique (public + privé, 4e au BTSA) : 9 375 € (2024) et 9 336 € (2025). Convention d'effectifs : 2/3 de l'année N-1/N et 1/3 de N/N+1. C'est l'État seul, donc hors cible, mais la convention d'effectifs est réutilisable.

## 6. Études par établissement ou selon les caractéristiques des établissements

| Étude | Statut | Contenu | Année des données |
|---|---|---|---|
| Cour des comptes, RPA 2026 (collèges) | officielle, récente | coût salarial **État seul** par collégien selon la taille | 2023 |
| Cour des comptes, Éducation prioritaire | officielle, ancienne | masse salariale **État** par élève (REP+/REP/hors EP) | 2016 |
| France Stratégie, NA 61 | officielle (organisme public d'études), ancienne | masse salariale **nette**, hors cotisations employeurs, par élève et par collège public : 10 % des collèges sous 2 500 €, 10 % au-dessus de 3 700 € ; 50 moins dotés 2 100 €, 50 mieux dotés 6 000 € ; 9,9 postes et 3 000 € pour 100 élèves défavorisés contre 9,1 postes et 2 800 € pour les très favorisés ; total 23 Md€ pour les collèges publics | 2015 |
| France Stratégie, NA 76 | officielle, ancienne | moyens (enseignants pour 100 élèves) des écoles selon le niveau de vie du quartier ; **pas d'euros par élève** | 2013-2016 |
| Cour des comptes, Enseignement primaire et note 2023 | officielle | dispersion des dépenses des communes : 250 à 4 500 € par élève | non précisée (renvoi à la Cour 2018) |
| HCSP (ex-France Stratégie), rapport « Niveau scolaire » | officielle, août 2026 | reprend la DEPP ; discute la convention des pensions | 2021-2024 |

**Aucune étude officielle récente** ne fournit un coût public complet (État + collectivités) **par établissement**. L'approche B de l'étudiant reste à construire avec les données open data (axe « etablissements »).

## 7. Convention des pensions : hypothèse majeure, effet d'environ 10 %
- La comptabilité nationale et les budgets incluent, pour les fonctionnaires d'État, une contribution employeur au CAS Pensions **calée pour équilibrer les pensions versées** (blog Insee du 24/10/2025). Selon le CAE (Focus n° 121, sept. 2025), elle vaut **78,3 %** du traitement indiciaire brut pour les pensions civiles en 2025 (74,3 % de 2014 à 2024) et 126,07 % pour les militaires.
- Le CAE et l'IPP proposent de retenir un taux « contributif » de **34,7 %** (IPP), voire **25,44 %** (borne basse du CAE). Le CAE chiffre la correction à -28,9 Md€ de dépenses publiques en 2023, dont **-0,5 point de PIB pour l'éducation**.
- HCSP (août 2026, p.69) : avec la convention IPP, la dépense d'éducation passerait de 5,4 % à 5,0 % du PIB en 2021. La dépense par élève du primaire tomberait de **10 554 à 9 649 USD PPA**, contre 11 902 pour l'OCDE.
- La méthode actuelle reste **conforme aux normes internationales**. L'INSEE étudie une autre convention pour la prochaine base.
- **À traiter comme une hypothèse explicite** avec une variante de sensibilité.

## 8. Limites et points d'attention pour le calcul
- La COFOG 2024 est provisoire (révision prévue en décembre 2026). OCDE : 2023. DEPP : 2024 et 2025. **Les années diffèrent selon les sources.**
- La COFOG ne distingue pas le public du privé sous contrat. Elle ne sépare pas non plus le scolaire du supérieur dans 09.6, ni le post-bac en lycée.
- La COFOG compte des dépenses **brutes** d'unités publiques, y compris celles financées par les familles (cantine, internat des EPLE et des caisses des écoles). L'OCDE et la DEPP raisonnent en financement.
- L'agrégat public de l'OCDE (G5) est mesuré **après transferts**. Celui de la note EAG 2025 (92 %) est mesuré **avant transferts**.
