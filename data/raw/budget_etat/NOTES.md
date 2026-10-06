# Composante « État » de l'agrégat public : budget de l'État pour l'enseignement scolaire

Synthèse des données brutes de ce dossier (consultation : 2026-10-04).

**Rôle dans le projet.** L'étudiant veut la **dépense publique** par élève : État + collectivités + autres administrations publiques. Les chiffres de ce dossier ne sont donc **pas un résultat final**. Ils servent à trois choses :
1. recouper la part de l'État dans le compte de l'éducation de la DEPP (approche A) ;
2. alimenter la somme des budgets publics, sans double compte (approche C2) ;
3. répartir par élève les dépenses de l'État qui ne sont pas rattachées à un établissement (approche B) : remplacement, encadrement, AESH, vie scolaire, bourses, soutien, etc.

Conventions de lecture :
- montants en **euros courants** ;
- crédits de paiement (CP) sauf mention contraire ;
- « exécution » = crédits consommés, fonds de concours (FdC) et attributions de produits (AdP) compris.

Les sources (URL, dates) sont dans `SOURCES.md`. Les tableaux transcrits sont dans `extractions/` (CSV séparés par `;`, UTF-8).

## 1. Périmètre de la mission « Enseignement scolaire » (MIES)

**Programmes.** La MIES compte 6 programmes :

| Programme | Contenu | Ministère |
|---|---|---|
| **140** | 1er degré public | MEN |
| **141** | 2nd degré public | MEN |
| **230** | Vie de l'élève | MEN |
| **139** | Privé sous contrat, 1er et 2nd degrés | MEN |
| **214** | Soutien | MEN |
| **143** | Enseignement technique agricole | Agriculture (MAASA) |

En PLF 2027, le P214 est renommé « Conduite et soutien des politiques de l'enseignement, de la recherche, de la jeunesse, de la vie associative et des sports ».

**Champ géographique : France + COM.** Le budget couvre la métropole, les DROM et les collectivités d'outre-mer (COM). La DEPP (RERS fiche 10.03) qualifie ce champ de « France + COM ».
- Le compte de l'éducation et les effectifs DEPP portent sur le champ « France », c'est-à-dire la métropole et les DROM. Le dossier DEPP n° 206 (2016, p.7 imprimée) indique que le territoire est « la France métropolitaine et les départements d'outre-mer ».
- Il faut donc **retirer les dépenses faites dans les COM** pour comparer au compte de l'éducation (voir § 8).

**Dépenses hors scolaire 1er et 2nd degrés incluses dans la MIES** (exécution 2025) :
- post-bac en lycée : P141 action 05, 1 405,8 M€ ; P139 action 06, 212,5 M€ ;
- apprentissage : P141 action 04, 3,0 M€ ;
- formation continue des adultes et VAE : P141 action 09, 92,5 M€ ;
- sport, jeunesse et vie associative : P214 action 11, 188,9 M€ ;
- BTSA dans le P143 (montant non isolable).

**Une partie des dépenses de l'État est hors MIES** (voir § 7). La Cour des comptes (NEB 2025, p.5) parle de « la quasi-totalité des moyens consacrés à l'enseignement scolaire par l'État ».

## 2. Chiffres clés : exécution 2025 et 2024 (RAP 2025)

**Sources.** RAP 2025 de la mission (annexe au PLRG 2025, avril 2026) :
- p.20-21 : crédits et ETPT par programme ;
- p.22-24 : crédits par action ;
- p.25-26 : crédits par titre ;
- CAS Pensions : tableaux « Présentation des crédits par catégorie et contributions employeurs », p.51 (P140), 105 (P141), 160 (P230), 220 (P139), 280 (P214), 384 (P143).

**Contrôles.**
- La colonne 2024 du RAP 2025 est identique au RAP 2024.
- Les fichiers DGFiP du PLRG 2025 confirment les montants au centime : CP consommés = 87 745 903 451,38 €. Vérifié à nouveau le 2026-10-04.
- Tous les montants du CSV sont re-vérifiés dans le texte du RAP (p.20-21, 25-26, tableaux CAS).

Fichier : `extractions/rap_execution_2024_2025_par_programme_et_titre.csv`.

### Exécution 2025 (CP consommés, €)

| Prog. | Total CP | Titre 2 | dont CAS Pensions | T2 hors CAS | Titre 3 | Titre 5 | Titre 6 | Titre 7 | **Total hors CAS** | ETPT réalisés |
|---|---|---|---|---|---|---|---|---|---|---|
| 140 | 27 358 507 822 | 27 277 406 728 | 9 653 767 996 | 17 623 638 732 | 39 736 298 | 0 | 41 078 256 | 286 540 | 17 704 739 826 | 339 740,90 |
| 141 | 38 974 173 358 | 38 601 565 523 | 12 512 490 496 | 26 089 075 028 | 61 266 962 | 0 | 311 340 873 | 0 | 26 461 682 862 | 450 028,58 |
| 230 | 7 948 971 523 | 5 419 402 059 | 636 803 805 | 4 782 598 254 | 59 110 897 | 6 600 | 2 470 451 966 | 0 | 7 312 167 718 | 122 022,95 |
| 139 | 8 812 182 661 | 7 921 531 370 | 50 580 300 | 7 870 951 070 | 4 650 259 | 0 | 886 001 032 | 0 | 8 761 602 361 | 130 515,54 |
| 214 | 2 963 770 647 | 2 145 427 174 | 563 445 304 | 1 581 981 870 | 645 242 355 | 141 443 407 | 31 657 711 | 0 | 2 400 325 343 | 27 453,28 |
| 143 | 1 688 297 441 | 1 116 701 955 | 243 556 059 | 873 145 896 | 13 887 889 | 124 032 | 556 969 350 | 614 216 | 1 444 741 382 | 15 622,60 |
| **Mission** | **87 745 903 451** | **82 482 034 810** | **23 660 643 960** | **58 821 390 850** | 823 894 659 | 141 574 039 | 4 297 499 188 | 900 756 | **64 085 259 491** | **1 085 384** |

AE consommées en 2025 : 87 690 179 159 €. Hors titre 2 : 5 263 868 642 €.

### Exécution 2024 (CP consommés, €)

| Prog. | Total CP | Titre 2 | dont CAS Pensions | Titre 3 | Titre 5 | Titre 6 | Titre 7 | **Total hors CAS** | ETPT réalisés |
|---|---|---|---|---|---|---|---|---|---|
| 140 | 26 685 544 935 | 26 590 427 344 | 9 051 766 970 | 52 529 210 | 99 000 | 41 539 850 | 949 532 | 17 633 777 965 | 340 746,41 |
| 141 | 38 247 288 123 | 37 788 687 429 | 11 811 604 041 | 60 753 177 | 0 | 397 847 516 | 0 | 26 435 684 082 | 449 767,87 |
| 230 | 7 933 873 880 | 4 873 261 933 | 597 211 559 | 72 909 199 | 0 | 2 987 702 749 | 0 | 7 336 662 321 | 105 871,67 |
| 139 | 8 939 358 667 | 8 043 871 112 | 47 993 443 | 3 917 847 | 0 | 891 492 117 | 77 591 | 8 891 365 224 | 130 727,54 |
| 214 | 2 909 792 898 | 2 073 420 720 | 525 587 049 | 640 490 706 | 169 446 648 | 26 427 224 | 7 600 | 2 384 205 849 | 27 017,38 |
| 143 | 1 681 618 831 | 1 091 364 894 | 233 691 128 | 11 536 099 | 0 | 577 884 960 | 832 878 | 1 447 927 703 | 15 428,00 |
| **Mission** | **86 397 477 334** | **80 461 033 432** | **22 267 854 190** | 842 136 238 | 169 545 648 | 4 922 894 415 | 1 867 601 | **64 129 623 144** | **1 069 559** |

**Recoupements avec la Cour des comptes** (NEB 2025) :
- titre 2 hors CAS : 58 821,4 M€ en 2025 et 58 193,2 M€ en 2024 (tableaux 17 et 19, p.37-38) ;
- exécution hors CAS : 64,09 Md€ en 2025 et 64,13 Md€ en 2024 (tableau 28, p.53) ;
- CAS : 23,66 Md€, soit 27 % de la dépense 2025 (p.53).

## 3. Ventilation par action (exécution 2025, CP)

**Fichier complet** : `extractions/rap2025_execution_par_action_2024_2025.csv`. Il contient 2024, 2025, la LFI 2025, les AE, la répartition titre 2 / hors titre 2 et les ETPT par action. Sources : RAP 2025 p.22-24 ; répartition T2/HT2 dans les tableaux « Éléments de synthèse », p.44, 97-98, 152-153, 214-215, 270-271, 380-381. Les sommes des actions sont égales aux totaux des programmes.

**P140 (1er degré public)** :
- 01 préélémentaire : 6 689 890 986 ;
- 02 élémentaire : 14 167 029 206 ;
- 03 besoins éducatifs particuliers : 2 103 756 753 ;
- 04 formation des enseignants : 368 838 633 ;
- 05 remplacement : 2 170 138 668 ;
- 06 pilotage : 1 694 156 079 ;
- 07 situations diverses : 164 697 497.

**P141 (2nd degré public)** :
- 01 collège : 14 069 267 692 ;
- 02 lycée général et technologique : 10 346 483 589 ;
- 03 lycée professionnel : 4 479 736 994 ;
- 04 apprentissage : 2 958 122 ;
- 05 post-bac : 1 405 849 445 ;
- 06 besoins éducatifs particuliers : 1 121 558 374 ;
- 07 insertion : 52 662 857 ;
- 08 orientation : 305 178 293 ;
- 09 formation continue des adultes : 92 495 094 ;
- 10 formation des enseignants : 261 905 183 ;
- 11 remplacement : 2 207 471 301 ;
- 12 pilotage : 4 416 259 922 ;
- 13 situations diverses : 212 346 492.

**P230 (Vie de l'élève)** :
- 01 vie scolaire : 2 906 927 101 (dont 1 468 031 251 hors titre 2, surtout les AED en CDD) ;
- 02 santé scolaire : 700 428 827 ;
- 03 inclusion (AESH) : 3 008 233 612 ;
- 04 action sociale : 1 057 916 721 ;
- 05 internat et établissements à la charge de l'État : 88 066 228 ;
- 06 actions éducatives complémentaires : 187 226 525 ;
- 07 scolarisation à 3 ans : 172 509.

**P139 (privé sous contrat)** :
- 01 préélémentaire : 502 760 370 ;
- 02 élémentaire : 1 525 349 788 ;
- 03 collège : 2 522 028 323 ;
- 04 lycée général et technologique : 1 849 177 915 ;
- 05 lycée professionnel : 816 440 704 ;
- 06 post-bac : 212 533 674 ;
- 07 dispositifs spécifiques : 216 665 720 ;
- 08 action sociale : 80 352 684 ;
- 09 fonctionnement des établissements : 717 137 886 ;
- 10 formation : 87 004 027 ;
- 11 remplacement : 214 427 577 ;
- 12 soutien : 68 303 993.

**P214 (soutien)** :
- 01 pilotage : 639 730 944 ;
- 02 évaluation : 125 912 884 ;
- 03 communication : 19 309 522 ;
- 04 juridique : 32 226 718 ;
- 05 international : 13 158 861 ;
- 06 ressources humaines : 802 274 024 ;
- 07 opérateurs : 137 272 082 ;
- 08 logistique, systèmes d'information et immobilier : 826 711 648 ;
- 09 examens : 174 946 854 ;
- 10 transports scolaires : 3 281 902 ;
- **11 sport, jeunesse et vie associative : 188 945 208 (hors scolaire)**.

**P143 (enseignement agricole)** :
- 01 établissements publics : 902 928 745 ;
- 02 établissements privés : 648 259 927 ;
- 03 aide sociale et santé : 80 160 334 ;
- 04 territoires : 4 477 885 ;
- 05 moyens communs : 52 470 551.

**Usage pour l'approche B.** Les dépenses de l'État non rattachables directement à un établissement sont à répartir par élève avec une clé à documenter dans les hypothèses, par exemple les élèves du niveau et du secteur. Ce sont :
- **1er degré public** : remplacement (P140-05), pilotage (P140-06), formation (P140-04), besoins éducatifs particuliers (P140-03) ;
- **2nd degré public** : P141-06, 08, 10, 11 et 12 ;
- **public, P230** : vie scolaire (01), santé (02), AESH (03), action sociale (04), actions éducatives (06) ;
- **privé sous contrat** : P139-07 à 12 ;
- **soutien** : tout le P214, sauf l'action 11.

**Prudence sur la ventilation par niveau.** La Cour (NEB 2025, p.21-22) rappelle que l'imputation du personnel par action « repose sur le statut et l'affectation principale des agents ». Exemple : l'action lycée GT du P141 est exécutée à 119 % de la LFI. La ventilation collège / lycée est donc approximative.

## 4. Emplois et coûts moyens

**ETPT réalisés en 2025** (RAP p.20-21) :
- 140 : 339 740,90 ;
- 141 : 450 028,58 ;
- 230 : 122 022,95 ;
- 139 : 130 515,54 ;
- 214 : 27 453,28 ;
- 143 : 15 622,60 ;
- mission : 1 085 384 (2024 : 1 069 559).

**Par catégorie** : `extractions/rap2025_ETPT_par_programme_et_categorie.csv`. Exemples 2025 :
- enseignants du 1er degré public : 325 271 ETPT ;
- enseignants du 2nd degré public : 371 166,72 ETPT ;
- privé : 41 318,54 (1er degré) et 87 157,67 (2nd degré) ;
- AESH : 86 410,18 ;
- AED sous plafond : 8 857,83.

**Personnels payés hors titre 2 (absents des ETPT de l'État)** (NEB 2025, tableau 23, p.43) :
- AED en CDD : 41 292 ETPT, 1 347,5 M€ ;
- AED « prépro » : 2 155 ETPT, 64,3 M€ ;
- ils sont payés via des subventions aux EPLE ;
- au MAASA : 1 135 ETPT d'AED et des AESH en CDD.

Voir `extractions/personnels_remuneres_hors_titre2_NEB2025.csv`.

**Coûts moyens chargés hors CAS** (coût global, RAP 2025 tableaux « Coûts entrée-sortie ») :
- enseignant du 1er degré public : 48 944 € ;
- enseignant du 2nd degré public : 52 248 € ;
- privé : 52 651 € (1er degré) et 54 227 € (2nd degré) ;
- AESH : 34 985 € ;
- AED : 32 747 € ;
- enseignant de l'enseignement agricole : 56 810 €.

Voir `extractions/rap2025_couts_moyens_entree_sortie_HCAS.csv`.

Ces coûts **excluent le CAS Pensions**, alors que le compte de l'éducation l'inclut (§ 8). Pour l'approche B, il faut donc les majorer, par exemple avec le rapport titre 2 / ETPT.

**Ratios calculés T2 / ETPT 2025** (calcul, non officiel) :

| Programme | Avec CAS | Hors CAS |
|---|---|---|
| P140 | 80 289 € | 51 874 € |
| P141 | 85 776 € | 57 972 € |
| P139 | 60 694 € | 60 307 € |

## 5. LFI 2026 et PLF 2027 (prévisions)

**LFI 2026** (loi n° 2026-103, état B) :
- mission : **CP 89 621 003 132 €** ;
- par programme : 140 = 27 912 141 280 ; 141 = 40 001 618 399 ; 230 = 8 060 719 293 ; 139 = 8 870 628 702 ; 214 = 3 045 962 854 ; 143 = 1 729 932 604 ;
- titre 2 : 84 456 715 562 €, dont CAS 25 159 470 963 € (somme des 6 tableaux du PAP 2027, re-vérifiée), soit **hors CAS 64 461 532 169 €** ;
- plafond d'emplois : 1 101 108 ETPT.

**PLF 2027** (déposé le 1/10/2026) :
- mission : **CP 90 859 899 196 €** ;
- par programme : 140 = 28 524 973 930 ; 141 = 40 283 677 823 ; 230 = 8 252 517 134 ; 139 = 8 939 648 669 ; 214 = 3 087 222 108 ; 143 = 1 771 859 532 ;
- titre 2 : 85 757 917 681 €, dont CAS 25 327 753 504 €, soit **hors CAS 65 532 145 692 €** ;
- 1 108 904 ETPT.

Détail : `extractions/lfi2026_plf2027_par_programme_et_titre.csv` et `..._par_action.csv`.

Pour un coût observé, utiliser l'exécution (RAP). Le RAP 2026 paraîtra au printemps 2027.

## 6. Transferts de l'État au titre de l'éducation : éviter les doubles comptes

Fichier : **`extractions/transferts_etat_education_2025.csv`**. Il contient 54 lignes, avec pour chacune le montant, la source, la présence ou non dans la MIES et le **traitement recommandé dans l'agrégat public**.

### 6.1 Transferts inclus dans la MIES (exécution 2025, titre 6, fichier DGFiP du PLRG)

Total du titre 6 : 4 297 499 188 €.

| Catégorie | Montant (€) | Principaux postes (RAP 2025) |
|---|---|---|
| 61 Ménages | 1 207 372 733 | **Bourses** : 766,26 M€ (P230 ; p.175) + 76,77 M€ (P139 ; p.233) + 40,40 M€ (P143 ; p.396).<br>**Allocations de stage des lycéens professionnels** : 208,0 M€ (P141) + 54,76 M€ (P139) + 28,98 M€ (P143).<br>**Fonds sociaux** : 23,96 M€ (P230) + 3,58 M€ (P139). |
| 62 Entreprises | 73 933 514 | Part collective du pass Culture : 71,87 M€. |
| 63 Collectivités territoriales, **y compris les EPLE** | 1 712 724 959 | **AED en CDD payés via les EPLE** : 1 411,84 M€ (P230 ; p.168) + 36,64 M€ (P143).<br>Crédits pédagogiques aux EPLE : 85,53 M€ (p.110).<br>FSDAP : 20,27 M€ ; petits déjeuners : 18,05 M€ ; FIP : 20,0 M€ ; service minimum d'accueil : 6,45 M€ ; internats : 12,87 M€ ; Polynésie : 11,42 M€. |
| 64 Autres collectivités | 1 303 467 982 | **Forfait d'externat, part personnels** (privé) : 697,46 M€ (p.235).<br>**Enseignement agricole privé** : 392,85 M€ (p.393-394).<br>Associations : 62,69 M€ ; formation continue du privé : 33,34 M€. |
| Titre 3, catégorie 32 : subventions pour charges de service public | 145 456 445 | Opérateurs CNED, Canopé, ONISEP, FEi, Céreq : 135,9 M€ (NEB tableau 30). |

Somme des bourses : 883,4 M€ (calcul).

### 6.2 Transferts hors MIES, à ne pas ajouter si les dépenses des collectivités sont comptées

Ces versements financent des dépenses que les collectivités enregistrent elles-mêmes.

| Poste | Montant | Année | Source |
|---|---|---|---|
| DDEC (prélèvement sur recettes) | 326 316 128 € | 2025 | PLRG, état des recettes |
| DRES | 661 186 704 € | 2025 | idem |
| DGCES | 2 685 550 € | 2025 | idem |
| Logement des instituteurs | 2 611 157 € | 2025 | idem |
| DGD instruction obligatoire à 3 ans (P119) | 48,4 M€ | 2025 | RAP RCT p.30 et 36 ; PLF 2027 : 48,48 M€ |
| Cantine à 1 € (P304) | 78 157 138 € | 2025 | RAP Solidarité p.68-70 |
| Plan « Marseille en grand » écoles (P119) | 40,1 M€ | 2025 | RAP RCT p.34 |
| Dotations scolaires en DROM (P123 : Mayotte 3,19 M€ ; Guyane 10,85 et 29,32 M€) | 43,36 M€ | 2025 | RAP Outre-mer p.129-130 |
| DETR, DPV, DSIL, DSID pour des projets « scolaire et jeunesse » (subventions accordées, périmètre plus large) | 517 M€ | 2024 | DGCL, bilan 2024, tableau 10 p.12 |

Le transfert de compétences de 2004 (agents techniques des collèges et lycées) est compensé par des fractions d'impôts transférés (TICPE, TSCA). Ce n'est **pas** une dépense budgétaire de l'État : rien à neutraliser.

### 6.3 Règles de traitement (à reporter dans `hypotheses.md`)

1. **Ménages (bourses, allocations, fonds sociaux ; ARS côté CNAF)**. Ce sont des dépenses publiques, à compter **une fois** chez le payeur.
   - La DEPP les attribue à l'État en **financement initial** et aux ménages en **financement final** (dossier DEPP n° 206, p.16 imprimée).
   - La part publique en financement final les **exclut** ; la part publique en financement initial les **inclut**.
   - Pour un « coût pour la puissance publique », le financement **initial** est donc le concept cohérent.
2. **État vers collectivités** (DDEC, DRES, DGD, FSDAP, petits déjeuners, service minimum d'accueil, cantine à 1 €, plan Marseille, DETR…). Il faut compter ces montants **soit** chez l'État, **soit** chez la collectivité qui dépense, jamais les deux. Les dépenses brutes des collectivités (comptes de gestion, fonctions « enseignement ») incluent déjà ce qu'elles financent avec ces dotations.
3. **État vers EPLE** : AED, crédits pédagogiques, fonds sociaux. En comptabilité nationale, les EPLE font partie des administrations publiques locales. Si l'on additionne les comptes financiers des EPLE, il faut retirer ces subventions (environ 1,58 Md€ en 2025, calcul : AED 1 411,8 + 36,6 ; crédits pédagogiques 85,5 ; fonds sociaux 24,0 ; contrats aidés 15,3 ; autres 5,7 M€).
4. **État vers privé sous contrat** (forfait d'externat, subventions au privé agricole) : dépense publique comptée chez l'État. Les maîtres du privé sont payés directement en titre 2 (7,92 Md€ en 2025). Ce n'est pas un transfert.
5. **Flux internes à l'État** (CAS Pensions, subventions aux opérateurs, petits déjeuners financés par le P304 et exécutés sur le P230) : rien à neutraliser, mais il ne faut **pas** ajouter le P304 ni les comptes des opérateurs en plus.
6. **FSDAP**. La Cour ajoute 33,6 M€ (campagne 2024-2025) à la dépense de la mission (NEB p.77), mais 20,27 M€ ont été versés en 2025 depuis le P230. Ajouter 33,6 M€ ferait un double compte partiel.

## 7. Autres dépenses de l'État pour l'enseignement scolaire hors mission

Fichier : `extractions/autres_depenses_etat_hors_mission.csv` (28 lignes).

**Dépenses de l'État proprement dites :**
- **Lycées de la défense** (ministère des Armées, P178 et P212) : coût complet **142,5 M€ en 2024** pour 4 390 élèves, dont 1 473 en CPGE, CPES et BTS. Coût moyen : **32 400 €/élève**. Source : Cour des comptes, *Les lycées de la défense*, 02/02/2026, tableau 19 p.65 et p.68. La DEPP les classe en « autres ministères ».
- **Politique de la ville** (P147), pilier « éducation » : **161,7 M€ en 2025**, dont programme de réussite éducative 63,2 M€ et cités éducatives 80,1 M€ (RAP Cohésion des territoires p.237-238). C'est surtout du périscolaire ou de l'extrascolaire ; leur inclusion dans un coût par élève est discutable.
- **Outre-mer** (P123) : DGCEC de Nouvelle-Calédonie 11,16 M€ et fonds de reconstruction. Ce sont des COM, donc hors champ « France ».

**Le compte de l'éducation chiffre les « autres ministères »** (financement final 2024, activités d'enseignement, RERS 2026 fiche 10.02) :
- 161 M€ pour le 1er degré ;
- 1 582 M€ pour le 2nd degré ;
- ces montants comprennent l'Agriculture (P143, déjà dans la MIES) et le reste du monde ;
- on ne peut pas isoler la part réellement hors MIES.

**Dépenses fiscales** (ce ne sont pas des dépenses publiques en comptabilité nationale) :
- réduction d'impôt pour frais de scolarité (n° 110215) : 229 M€ en 2025 (actualisé), 221 M€ en 2024 (définitif) ;
- dépenses rattachées à titre subsidiaire : 1 021 M€ (NEB tableau 29, p.69 ; PLRG).

**Hors budget :**
- plan de relance : 14,4 M€ ;
- fonds de concours : déjà dans l'exécution (38,47 M€ selon le PLRG).

**Pas de chiffrage officiel trouvé** pour :
- les lycées professionnels maritimes (ministère de la Mer) ;
- l'éducation artistique et culturelle (P361) ;
- le sport scolaire (P219) ;
- la part « écoles » du Fonds vert (P380).

## 8. Recoupement avec le compte de l'éducation (DEPP)

### Conventions de la DEPP utiles au recoupement

- **Le CAS Pensions est inclus.**
  - Dossier DEPP n° 206 : les masses salariales comprennent « les charges de retraite gérées dans le compte d'affectation spéciale au titre des pensions » (p.18 imprimée). Les contributions « correspondent au principe des cotisations imputées en Comptabilité nationale » (p.25 imprimée).
  - Note d'information 26.42 (sept. 2026), p.1 : les dépenses de personnel de l'État « comprennent la totalité des charges sociales dues par l'employeur dont les versements au compte d'affectation spéciale « pensions » ».
  - Il faut donc comparer avec la MIES **CAS compris**.
- **Champ « France »** (métropole + DROM) : les COM sont exclues.
- **Les post-bac de lycée** (STS, CPGE) relèvent du « supérieur » pour la DEPP.
- **Les bourses** passent aux ménages en financement final.

### Dépenses de la MIES dans les COM

Source : DPT « Outre-mer » annexé au PLF 2026, annexe « Effort budgétaire et financier de l'État dans les outre-mer », p.229-277. Fichier : `extractions/dpt2026_outremer_MIES_par_territoire_2024_2026.csv`. Chaque territoire et la synthèse sont vérifiés à ±2 € près.

**Exécution 2024 (CP) :**
- COM : **1 160 639 707 €** (Nouvelle-Calédonie 445,0 M€ ; Polynésie 639,3 M€ ; Wallis-et-Futuna 57,4 M€ ; Saint-Pierre-et-Miquelon 19,0 M€ ; Saint-Martin, Saint-Barthélemy et TAAF : 0) ;
- soit **1,34 % de la MIES 2024** ;
- DROM : 5 334 183 158 € ;
- MIES 2024 hors COM (calcul) : **85 236 837 627 €** ;
- COM par programme (CP 2024) : P139 242,3 M€ ; P140 191,3 M€ ; P141 550,2 M€ ; P143 22,1 M€ ; P214 49,7 M€ ; P230 105,1 M€.

**Montants prévus pour les COM :** LFI 2025 : 1 103,5 M€ ; PLF 2026 : 1 117,2 M€.

**Saint-Martin et Saint-Barthélemy.** Le DPT leur attribue 0 €. Leurs écoles relèvent de l'académie de Guadeloupe ; leurs dépenses sont vraisemblablement comptées avec la Guadeloupe (non vérifié). À rapprocher du traitement de ces deux COM dans les effectifs DEPP.

L'exécution 2025 par territoire paraîtra dans le DPT annexé au PLF 2027, qui n'était pas publié au 04/10/2026.

### Ce que publie la DEPP pour l'État

**Compte provisoire 2024** (RERS 2026, fiches 10.02 et 10.04) :
- État en financement final, activités d'enseignement : **30 382 M€** (1er degré) et **43 541 M€** (2nd degré) ;
- parts de l'État dans la dépense intérieure d'éducation : 55,2 % en financement initial, 53,1 % en financement final ;
- financement des producteurs : écoles publiques, État 28 284 M€ sur 50 807 M€ ; collèges et lycées publics, État 42 052 M€ sur 57 705 M€.

Fichier : `extractions/depp_rers2026_part_etat_compte_education_2024.csv` (215 lignes).

**Attention : ces chiffres 2024 de la RERS (juillet 2026) sont provisoires.** La NI 26.42 (septembre 2026) publie le compte **définitif 2024** :
- dépense intérieure d'éducation : 196,76 Md€, au lieu de 197,10 Md€ (onglet « Figure 1bis ») ;
- État en financement initial : 108 698,5 M€ courants (onglet « Figure 3bis ») ;
- elle ne republie pas la ventilation par financeur et par activité.

Pour 2024, préférer donc la NI 26.42 quand le chiffre y figure.

**Compte provisoire 2025** (NI 26.42, fichier dans `../depp_compte_education/`, données figure 4, financement initial) :
- part de l'État : **55,10 %** de 59 999 M€ (1er degré) et **67,26 %** de 73 754 M€ (2nd degré) ;
- soit environ **82 668 M€** pour l'État, 1er et 2nd degrés (calcul) ;
- part publique totale (État + collectivités + autres administrations publiques) : 94,9 % (1er degré) et 88,9 % (2nd degré) (calcul).

### Passerelle indicative pour 2025 (calcul non officiel)

| Étape | Montant |
|---|---|
| MIES 2025 | 87 745,9 M€ |
| − COM (hypothèse : montant exécuté 2024) | − 1 160,6 M€ |
| − post-bac | − 1 618,4 M€ |
| − P214 action 11 | − 188,9 M€ |
| − formation continue des adultes | − 92,5 M€ |
| − apprentissage | − 3,0 M€ |
| **= MIES ramenée au champ de la DEPP** | **≈ 84 682 M€** |
| État selon la DEPP (1er + 2nd degrés) | ≈ 82 668 M€ |
| **Écart** | **≈ 2,0 Md€ (2,4 %)** |

Pistes non vérifiées pour expliquer l'écart :
- formation des enseignants classée en formation continue ou en supérieur (P140-04 + P141-10 + P139-10 = 717,7 M€) ;
- BTSA du P143 ;
- calendrier comptable.

La DEPP ne publie pas sa passerelle détaillée. La RERS 2026 affiche aussi un P143 exécuté 2025 de 1 731 M€, contre 1 688,3 M€ dans le RAP : écart de 43 M€.

**Mise à jour du 2026-10-04 (tâche G5).** Cette passerelle indicative est remplacée par celle du **§ 14**. Celle-ci est complète, documentée et chiffrée par script, avec un résidu d'environ 0 en variante centrale. Deux corrections ressortent :
- l'apprentissage (P141-04) ne doit pas être retiré, car le 2nd degré DEPP l'inclut ;
- la DEPP impute au supérieur bien plus que les seules actions post-bac.

## 9. Indicateurs officiels « par élève » des documents budgétaires

Fichier : `extractions/indicateurs_officiels_par_eleve_documents_budgetaires.csv`.

- **P143, indicateur 2.1** : dépense de l'État par élève ou étudiant de l'enseignement agricole :
  - 9 375 € en 2024 et 9 336 € en 2025 ;
  - cibles : 9 850 € en 2026 et 10 000 € en 2027 ;
  - convention : année civile = 2/3 de l'année scolaire N-1/N + 1/3 de N/N+1 (RAP p.373 ; PAP 2027 p.303).
- **Forfait d'externat, part personnels** : 556 €/élève en 2024-2025 (RAP p.235).
- **Crédits pédagogiques du 2nd degré public** : 18,2 €/élève en 2025 (RAP p.109).
- **Établissements à la charge de l'État** : 232,95 €/élève (RAP p.178).
- **Lycées de la défense** : 32 400 €/élève en 2024, coût complet (Cour des comptes).
- **Recommandation n° 8 de la Cour** (NEB 2025) : publier la dépense publique par élève dans le PLF. Le PAP 2027 ne le fait pas.

## 10. Jeu data.education.gouv.fr « fr-en-budget-missions »

Export : `data_education_fr-en-budget-missions_export.csv` (612 lignes ; métadonnées du 29/01/2026).

- **Inutilisable pour 2024-2026** : il s'arrête à la LFI 2020 et à l'exécution 2019.
- Anomalies relevées :
  - P140 et P141 sont inversés en LFI 2018 et en exécution 2017 ;
  - le total LFI 2013 est aberrant.

## 11. Conventions et hypothèses à reporter dans `hypotheses.md`

1. **Année.** Exécution **2025** (dernier exercice clos ; compte DEPP 2025 provisoire, NI 26.42). Exécution 2024 pour le compte définitif ou la RERS. Euros courants.
2. **Concepts budgétaires.** Exécution (RAP) plutôt que LFI. CP plutôt qu'AE. FdC et AdP inclus.
3. **CAS Pensions inclus dans la variante principale** (cohérence avec la DEPP et la comptabilité nationale), avec une variante hors CAS.
   - Montants : 87,75 Md€ avec, 64,09 Md€ sans.
   - Le CAS est une contribution d'équilibre : 78,28 % + 0,32 % (ATI) du traitement indiciaire en 2025 (RAP P140 p.51).
   - Le privé sous contrat et les contractuels n'y cotisent pas.
4. **Champ « France ».** Retirer les COM (1,16 Md€ en 2024 selon le DPT). Pour 2025, hypothèse : reprendre le montant exécuté 2024 (ou celui de la LFI 2025, 1,10 Md€).
5. **Champ « élèves ».** Exclure :
   - le post-bac en lycée (1 618,4 M€) ;
   - la formation continue des adultes (92,5 M€) ;
   - l'apprentissage (3,0 M€) ;
   - P214 action 11 (188,9 M€) ;
   - le BTSA (non isolable : hypothèse au prorata des effectifs du P143 si besoin).
6. **Agrégat public = financement initial public** (État + collectivités + autres administrations publiques), avec les transferts vers les ménages comptés une fois (bourses ; ARS pour la CNAF, 2,21 Md€ en 2025). Les transferts entre administrations sont neutralisés (§ 6.3).
7. **Dénominateur.** Élèves du public et du privé sous contrat, France. Le privé hors contrat n'est pas financé par l'État. Enseignement agricole inclus si le P143 est inclus. Pondération calendaire 2/3 – 1/3 (convention du P143).
8. **P214 (soutien)** réparti au prorata des élèves, faute de clé officielle.
9. **Dépenses hors mission** : lycées de la défense (0,14 Md€) en variante « État toutes missions ». Les dépenses fiscales sont exclues : ce ne sont pas des dépenses en comptabilité nationale.

## 12. Limites

- Le budget de l'État ne couvre ni les collectivités (bâtiments, entretien, agents techniques, ATSEM, cantines, transports) ni les familles. Voir les axes « collectivités » et « compte de l'éducation ».
- Les AED en CDD (et une partie des AESH du MAASA) sont payés en titre 6 : ils sont dans les montants, pas dans les ETPT.
- La ventilation des dépenses de personnel par action est approximative.
- La part des COM pour 2025 n'est pas encore publiée (DPT 2027 à paraître).
- La NEB 2025 (p.77) reprend pour les FdC (41,3 et 41,1 M€) et le plan de relance (14,4 M€) des montants identiques à ceux de la NEB 2024.
- budget.gouv.fr bloque les téléchargements automatisés. Les RAP, PAP et DPT viennent du site de l'Assemblée nationale (mêmes annexes officielles).
- Le bilan DGCL des dotations d'investissement 2025 n'est pas publié. Le chiffre 2024 (517 M€) est un montant engagé, sur un périmètre « scolaire et jeunesse ».

## 13. Contrôles de cohérence effectués

Tous les contrôles ont été faits le 2026-10-04 et sont vérifiés à ±3 € près (arrondis de publication) :
- somme des titres = total par programme ;
- somme des programmes = mission ;
- somme des actions = programme ;
- CAS de la LFI 2026 et du PLF 2027 = somme des 6 tableaux du PAP 2027 ;
- exécution du RAP = fichiers DGFiP du PLRG ;
- titre 6 par catégorie du PLRG = titre 6 du RAP (4 297 499 188 €) ;
- DPT : COM + DROM + non réparti = synthèse outre-mer ;
- RERS : sommes de lignes des tableaux 10.02 et 10.04 vérifiées, cellules relues sur l'image de la p.5.

Scripts de transcription (pypdf, pdfplumber) conservés hors du dossier.

## 14. Passerelle entre la MIES et la part État du compte de l'éducation (tâche G5, 2026-10-04)

**Objet.** Expliquer l'écart d'environ 2,0 Md€ entre deux montants 2025 :
- la MIES 2025 ramenée au champ DEPP, soit environ 84,7 Md€ (§ 8) ;
- la part État du compte DEPP en financement initial, 1er + 2nd degrés, soit 82,67 Md€.

**Fichiers.**
- Script reproductible : `_derive_G5_passerelle_MIES_DEPP.py`. Il lit seulement des fichiers locaux.
- Résultat : `_derive_G5_passerelle_MIES_DEPP_2024_2025.csv` (48 lignes, emplacement de chaque chiffre).
- Intrants transcrits dans `extractions/` :
  - `passerelle_G5_intrants_RAP_DPT_2024_2025.csv` (RAP 2024-2025 et DPT) ;
  - `depp_dossier206_tableau2i_financement_initial_etat_par_niveau_2013_2014.csv` ;
  - `plr2013_MIES_execution_CP_par_programme_action.csv` ;
  - `dger_effectifs_enseignement_agricole_voie_scolaire_par_niveau_2023_2025.csv`.

Montants en M€ courants, CP exécutés, CAS Pensions compris.

### 14.1 Classement des postes dans le compte : ce que documente la DEPP

**Aucune passerelle chiffrée publiée.** Aucune publication DEPP ne chiffre le passage du budget au compte. Ont été consultés :
- la NI 24.45 ;
- le document de travail 2024-E08 ;
- le dossier 206 ;
- la NI 26.42 ;
- L'état de l'École 2025.

Seules les règles de classement sont publiées :

| Poste | Classement dans le compte | Source |
|---|---|---|
| Dépenses dans les COM | hors champ (« France » = métropole + DROM) | dossier 206 p.7 ; NI 26.42 (champ France) |
| Post-bac en lycée (STS, CPGE) | supérieur (technique court ; long) | dossier 206 p.13-14 imprimées |
| Formation continue des adultes (GRETA, VAE) | extrascolaire, formation professionnelle continue (FPC) | dossier 206 p.14 |
| **Formation continue des personnels d'éducation** | les rémunérations des personnels d'éducation en formation **sont comptées** ; la FPC « interne aux administrations » relève de l'**extrascolaire** | dossier 206 p.8, 10 et 14 imprimées ; xlsx NI 26.42, onglet « Définitions et méthodologie » ; L'état de l'École 2025 p.97 |
| **Stagiaires** (formation initiale) | rémunération « intégrée dans les dépenses d'enseignement » ; **niveau non précisé** (la phrase figure dans le paragraphe sur le supérieur long) | dossier 206 p.14 et 25-26 imprimées |
| **Allocations PFMP** | **exclues de la DIE** : « Elles excluent de même l'indemnité de gratification des PFMP mise en place à la rentrée 2023 » | L'état de l'École 2025, « Méthodologie et définitions », p.98 imprimée (= p.100 du PDF) |
| Bourses | État en financement initial ; ménages en financement final | dossier 206 p.16 ; NI 26.42 |
| Crédits transversaux (remplacement, etc.) | **répartis entre niveaux par des clés**, « au prorata des postes de personnel enseignant par niveau » | dossier 206 p.32 imprimée (= p.34 du PDF) |
| P214 (administration) | activité « administration générale », répartie entre niveaux ; la partie « Recherche » de l'administration centrale est comptée en supérieur ; aucune clé publiée | dossier 206 p.15 et 18 |
| DRES, DDEC, DGD | ne sont plus des transferts depuis 2007 ; la DGD n'est jamais décrite | dossier 206 p.16 |

**Les stagiaires restent vraisemblablement dans le scolaire (inférence).** À la rentrée 2013, les stagiaires passent à mi-temps devant élèves. Si la DEPP les avait reclassés, la ligne « Enseignement scolaire » du compte aurait dû bondir vers le supérieur long ou la FPC. Elle ne bouge presque pas entre 2013 et 2014 :
- supérieur long : 971,0 → 990,9 ;
- FPC : 281,8 → 296,6.

On en déduit que la rémunération des stagiaires reste imputée aux 1er et 2nd degrés.

**P214.** Le RAP 2025 ne donne **aucune ventilation analytique** du P214 vers d'autres programmes ou missions. Une phrase d'introduction générique (p.3) annonce une « analyse des coûts », mais la section n'existe pas.

**NI 24.45** (compte 2023, novembre 2024, 4 p.) :
- le PDF renvoie aux « définitions et méthodologie en ligne » ;
- ce texte est celui de l'onglet « Définitions et méthodologie » du xlsx de la NI 26.42, qui porte d'ailleurs la mention « Réf. : NI 24.45 ».

**Document de travail 2024-E08** (septembre 2024) :
- p.8 : il exclut « les rémunérations des étudiants fonctionnaires, apprentis et des stagiaires de la formation continue (hors personnel d'éducation) » ;
- p.9 : pour le scolaire, le financement de l'État « est principalement assuré par la MIES ».

### 14.2 Contrôle global, tous niveaux : la DEPP reprend la quasi-totalité des crédits MEN-MESR

| | 2024 | 2025 |
|---|---|---|
| MIES-MEN + P150 + P231, hors COM (COM 2024), hors PFMP | 101 465,4 | 103 095,0 |
| DEPP, « dont MEN-MESR » en financement initial (NI 26.42, Figure 3bis : 2024 définitif en E5 ; 2025p en F5) | 101 607,9 | 103 194,6 |
| Écart DEPP − budget | +142,5 (+0,14 %) | +99,6 (+0,10 %) |

Sources des montants :
- P150 et P231 : RERS 2026, fiche 10.03, tableau 3 ;
- COM de la MIRES en 2024 : 81,5 M€ (Polynésie et Nouvelle-Calédonie, DPT 2026 p.269 et 273).

**Conclusion.** L'écart de 2 Md€ au niveau 1er + 2nd degrés ne vient **pas d'exclusions**. Il vient du **classement par niveau** des crédits MEN.

### 14.3 Seule ventilation officielle complète de la ligne « Enseignement scolaire » par niveau (dossier 206)

**Compte 2013 définitif** (tableau 2i, p.152 imprimée) :
- ligne « Enseignement scolaire » (programmes MEN de la MIES) : 61 189,0 M€ ;
- budget MEN 2013 (PLR 2013) : 62 107,7 M€, soit un écart de 918,7 M€, de l'ordre des COM ;
- dont **supérieur 3 007,4** :
  - STS : 1 959,5 ;
  - supérieur long, dont CPGE : 971,0 ;
  - formations post-secondaires : 68,9 ;
  - apprentissage : 8,1 ;
- dont **extrascolaire 332,4** (FPC : 281,8) ;
- soit **5,46 % hors 1er et 2nd degrés**.

**Comparaison avec les actions post-bac.** Les actions post-bac du budget 2013 ne totalisent que 1 223,2 M€ (P141-05 : 1 077,6 ; P139-06 : 145,6). La DEPP impute donc au supérieur **2,46 fois** ces actions : elle y ajoute, par clés, une part des actions transversales et des enseignants imputés aux actions « lycée ».

**Compte 2014 provisoire** (p.168) : 62 708,8 M€, dont supérieur 3 068,5 et extrascolaire 348,5 (5,45 %).

### 14.4 Calage sur 2024 (données DEPP 2024p)

**Part MEN-MESR du compte, 1er + 2nd degrés : 78 795,6 M€.**
- Calcul : parts « dont MENESR » de 54,8 % et 63,9 %, multipliées par la DIE de chaque niveau (58 523,0 et 73 122,1).
- Sources : séries chronologiques 366603, cellules U17 ; NI 25.52, Figure 5.
- Arrondi des parts : ± 66 M€.

**Crédits MEN classés hors 1er et 2nd degrés.**
- Crédits MEN de la MIES hors COM : 83 577,3 M€.
- Montant classé hors 1er/2nd degrés ou exclu : **4 781,7 M€ (5,72 %)**.
- Dont postes identifiables : 2 250,8 M€.
  - post-bac : 1 570,3 ;
  - formation continue des adultes : 92,7 ;
  - PFMP MEN : 392,9 ;
  - P214-11 : 181,0 ;
  - MEEF : 13,8.
- Dont **imputations par clés non identifiables : 2 530,9 M€, soit 3,03 % des crédits MEN** (3,33 % en 2013).

**Financements hors MIES.**
- État en 1er + 2nd degrés : 81 282,3 M€.
- Part MEN-MESR : 78 795,6 M€.
- Différence (autres ministères, agriculture comprise, et reste du monde) : 2 486,7 M€.
- Dont P143 en 2nd degré : 1 451,2 M€ (hors COM, PFMP et BTSA ; supérieur court au prorata, 10,18 %).
- Il reste **1 035,4 M€ pour les autres ministères hors agriculture et le reste du monde**, contre 780,0 en 2013.
- Cette hausse est cohérente avec de nouveaux financements de l'État pour les écoles hors MIES (cités éducatives, cantine à 1 €, plan Marseille, DSIL scolaires, voir § 6.2 et § 7). C'est une inférence : le classement de ces transferts par la DEPP n'est pas documenté.

### 14.5 Table de passage 2025

| Étape | M€ | Classement DEPP | Statut |
|---|---|---|---|
| **Référence : DEPP, État, financement initial, 1er + 2nd degrés 2025p** (55,0983 % × 59 999,2 + 67,2638 % × 73 753,7 ; NI 26.42, Figures 4 et 5) | **82 668,1** | | publié |
| MIES 2025 (RAP) | 87 745,9 | | officiel |
| − COM (montant exécuté 2024, faute de chiffre 2025) | −1 160,6 | hors champ | hypothèse sur le montant |
| − post-bac (P141-05 : 1 405,8 ; P139-06 : 212,5) | −1 618,4 | supérieur | documenté |
| − formation continue des adultes (P141-09) | −92,5 | extrascolaire | documenté |
| − PFMP (P141 : 208,0, p.116 ; P139 : 54,76, p.230 ; P143 : 28,98, p.404) | −291,7 | exclues | documenté |
| − P214 action 11 | −188,9 | hors DIE ou extrascolaire | supposé |
| − gratifications MEEF (P140 : 5,96 ; P141 : 7,13 ; P139 : 0,51 ; P230 : 0,57) | −14,2 | supérieur ou exclues | supposé |
| − BTSA, BTS et CPGE du P143 (9,84 % de P143 hors COM et hors PFMP) | −161,1 | supérieur court | prorata des effectifs |
| **= après postes identifiables dans le RAP** | **84 218,4** | écart restant **+1 550,3** | |
| − crédits MEN imputés par clés hors 1er/2nd degrés (3,028 % × 84 919,1) | −2 571,5 | supérieur et extrascolaire | principe documenté ; montant calé sur 2024 |
| + autres ministères hors agriculture et reste du monde | +1 035,4 | État | montant 2024, supposé stable |
| **= estimation budgétaire de la part État DEPP** | **82 682,3** | | |
| **Résidu (estimation − DEPP)** | **+14,2 (0,02 %)** | | sous 0,5 Md€ |

L'apprentissage (P141-04, 3,0 M€) n'est **plus retiré** : le 2nd degré DEPP l'inclut.

**Sensibilité du résidu.**

| Variante | Résidu (M€) |
|---|---|
| BTSA au prorata pondéré par secteur (12,14 % ; coûts par élève public et privé approchés par les actions 01 et 02 du P143) | +8,4 |
| BTSA selon la structure DEPP 2013 (17,92 %) | +7,1 |
| COM 2025 = LFI 2025 (1 103,5) | +71,4 |
| **Calage complet sur la structure DEPP 2013** (5,46 % hors 1er/2nd ; P143 en 2nd degré : 79,43 % ; autres ministères et reste du monde : 780,0) | **−752,0** |
| Ancienne passerelle (§ 8) | +2 014,4 |

### 14.6 Conclusions

1. **L'écart résiduel tombe sous 0,5 Md€** (+0,01 Md€), mais seulement grâce à deux postes qu'on ne lit pas dans le budget. Ils sont calés sur les parts DEPP 2024 :
   - environ **2,6 Md€** de crédits MEN que la DEPP impute par clés au supérieur et à l'extrascolaire, en plus des actions explicitement post-bac ;
   - environ **1,0 Md€** de financements de l'État hors MIES, en sens inverse.

   Le résultat 2025 vérifie donc surtout la **stabilité de la structure entre 2024 et 2025**. Ce n'est pas une validation indépendante. Avec la seule ventilation officielle complète, qui date de 2013, le résidu serait de −0,75 Md€ : cette structure est périmée.

2. **Formation des enseignants : la piste n'explique qu'une petite part.** Les actions de formation (P140-04 + P141-10 + P139-10) totalisent **717,7 M€ en 2025** (titre 2 : 640,8 ; hors titre 2 : 76,9) et 737,9 M€ en 2024.
   - Seule la **formation continue des personnels** passe en extrascolaire. Son montant n'est pas isolable. Borne basse : 63,3 M€ de hors titre 2 hors MEEF. Ordre de grandeur d'après 2013 : environ 0,2 à 0,35 Md€.
   - Les **stagiaires** restent vraisemblablement en 1er/2nd degrés (inférence, § 14.1). Ils représentent 21 344,81 ETPT en 2025 :

     | Programme | ETPT | Coût hors CAS | Total (M€) |
     |---|---|---|---|
     | P140 | 9 774,00 | 31 232 € | 305,3 |
     | P141 | 8 987,43 | 31 231 € | 280,7 |
     | P230 | 544,05 | 30 718 € | 16,7 |
     | P139 | 2 039,33 | 33 249 € | 67,8 |
     | **Total** | | | **670,5** |

     Avec le CAS, on estime environ 981 M€ (ratio CAS / titre 2 hors CAS de chaque programme ; ratio du P141 pour le P230).
   - Les stagiaires à temps plein sont imputés aux actions d'enseignement, ce qui explique la sous-exécution de l'action 04 (RAP p.44).
3. **PFMP** : exclues de la DIE (documenté). 291,7 M€ en 2025 ; **436,8 M€ en 2024** (P141 : 321,0, RAP 2024 p.124 ; P139 : 71,9, p.235 ; P143 : 43,9, p.410).
4. **P143 et BTSA.** Effectifs DGER en voie scolaire (BTSA + BTS + CPGE sur le total) :
   - rentrée 2023 : 15 836 / 153 449 ;
   - rentrée 2024 : 15 365 / 155 363 ;
   - rentrée 2025 : 15 345 / 157 386.

   Part du supérieur court en année civile (pondération 2/3 – 1/3) : **10,18 % en 2024** et **9,84 % en 2025**.

   Le RAP (indicateur 2.1, p.373) ne publie **pas** les effectifs : il donne seulement le coût, 9 336 €/élève en 2025, avec la convention 2/3 – 1/3.

   L'écart RERS/RAP sur le P143 (1 731,1 contre 1 688,3 M€) reste **inexpliqué** : il ne correspond ni à la LFI (1 712,2), ni aux CP ouverts (≈ 1 702,6), ni aux AE (1 687,3).
5. **Comptabilité nationale (inférence).** L'écart de 2,6 Md€ entre l'État en COFOG 09.1 + 09.2 et les programmes P140, P141, P139 et P143 s'explique pour partie par les mêmes postes :
   - COM de ces 4 programmes : 1,01 Md€ ;
   - PFMP : 0,44 Md€ ;
   - BTSA : 0,16 Md€ ;
   - formation continue des adultes : 0,09 Md€.

   Le reste s'explique par le classement de l'INSEE : en 2024, l'État a **3,80 Md€ en 09.5** « non défini par niveau » et 2,02 Md€ en 09.8 (T_3303, `../recoupements/`). La passerelle INSEE n'est pas publiée.

### 14.7 Conséquences pour les calculs (à reporter dans `hypotheses.md`)

- **Approche A** : utiliser directement la part État DEPP. La passerelle n'est pas nécessaire.
- **Approche C2** (somme des budgets) : retirer seulement les actions post-bac **sous-estime** ce que la DEPP classe hors scolaire, d'environ 2,5 Md€.
  - Variante cohérente avec la DEPP : retirer des crédits MEN hors COM les postes identifiables, plus 3,03 % au titre des imputations par clés (calage 2024).
  - Autre formulation : appliquer directement le taux observé en 2024, soit 5,72 % hors 1er/2nd degrés ou exclus.
- **Champ État** : ajouter environ 1,0 Md€ d'autres ministères et de reste du monde pour retrouver la part « État » de la DEPP. Ce montant est un résidu calé sur 2024, non ventilé.
- **PFMP** : à exclure du coût par élève si l'on suit la DEPP. Elles sont à inclure si l'on vise toute dépense publique liée à la scolarité : c'est une convention à choisir.
- **Limite** : les parts « dont MENESR » par niveau ne sont publiées qu'arrondies à 0,1 point et seulement jusqu'en 2024p. La NI 26.42 ne les donne pas pour 2025.
