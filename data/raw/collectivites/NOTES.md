# NOTES — Dépenses des collectivités territoriales (CT) pour l'enseignement scolaire

Consulté le 2026-10-04. Les sources détaillées sont dans `SOURCES.md` ; les calculs dans `extractions/` (script reproductible).

**Abréviations**
- BP : budget principal ; BA : budget annexe ; GFP : groupement à fiscalité propre ; CTU : collectivité territoriale unique (Corse, Guyane, Martinique) ; ML : Métropole de Lyon.
- F : fonctionnement ; I : investissement (hors remboursements de dette).
- DIE : dépense intérieure d'éducation ; p : provisoire.
- M€ et Md€ : euros courants.

Statut des **comptes 2025** des collectivités : ce sont des comptes de gestion, issus des balances DGFiP « DEF » (définitives) mises en ligne le 13/07/2026. La ventilation par fonction en comptabilité nationale (COFOG) pour 2025 ne paraîtra qu'en décembre 2026.

---

## 0. L'essentiel

1. **Référence DEPP** (NI 26.42, 2025p, financement initial) :
   - les CT financent **38,41 % de la DIE du 1er degré** et **19,63 % de celle du 2nd degré** ;
   - en montants (calcul : part × DIE), cela fait **23 046 M€** et **14 477 M€**, soit **37 522 M€** pour le scolaire ;
   - par élève (calcul : part × dépense moyenne) : **3 626 €** pour un écolier, **2 312 €** pour un élève du 2nd degré.
   - Toutes activités et tous niveaux : CT = **45 539 M€** (22,86 % de la DIE), dont communes 13,13 %, départements 3,58 %, régions 6,15 %.
2. **Comptes des collectivités 2025** (DGCL, CLC 2026, fichier 4F, BP, fonction « Enseignement, formation et apprentissage ») :

   | Niveau | Montant 2025 | Ce que couvre la ligne | Transports scolaires (fonction 81) |
   |---|---|---|---|
   | Communes ≥ 3 500 hab. | **14 407 M€** | essentiellement les écoles | 61 M€ |
   | GFP | **1 317 M€** | | 209 M€ |
   | Départements | **6 522 M€** | dont 2nd degré 5 531 M€ | 262 M€ |
   | Régions et CTU | **11 889 M€** | dont 2nd degré 6 874 M€, mais aussi formation professionnelle, apprentissage, formations sanitaires et sociales | 1 621 M€ |

   **Les communes de moins de 3 500 habitants n'ont pas de ventilation fonctionnelle.** Elles représentent 26,3 Md€ de dépenses totales et environ 30 % des élèves du public.
3. **Extrapolation aux petites communes** (méthode OFGL, recalculée pour 2025) :
   - 69,9 % des élèves du public sont scolarisés dans les 3 336 communes à comptabilité fonctionnelle ;
   - ces communes dépensent **3 752 € par élève du public** (2 821 € en F, 931 € en I) ;
   - dépense « écoles » des communes non couvertes : **4,9 à 6,1 Md€**, soit environ **20,2 Md€** pour l'ensemble des communes (estimation centrale, calcul dérivé).
4. **Décomposition 2025** (DGFiP, calcul) :

   | Périmètre | Total | Personnel | Restauration / achats | Énergie | Investissement |
   |---|---|---|---|---|---|
   | Écoles (communes couvertes) | 14 145 M€ | 6 746 | restauration (sous-fonction 281) 3 384 | 543 | 3 519, dont constructions et rénovations 3 039 |
   | Collèges (départements) | 6 257 M€ | 1 914 | — | 174 | 2 448 |
   | Lycées (régions + CTU) | 7 338 M€ | 2 578 | — | 162 | 2 802 |

   Dotations de fonctionnement aux EPLE publics : 573 M€ pour les collèges, 871 M€ pour les lycées.
5. **Par élève**, collectivités de rattachement :
   - DEPP (Géographie de l'École 2026, moyenne 2021-2023, euros 2023) : **2 010 € par collégien** et **3 000 € par lycéen** ;
   - mon calcul 2025 : 1 852 € par collégien (départements seuls) et 3 259 € par lycéen.
6. **Doubles comptes et part non publique** (point 4) :
   - les recettes « familles » portées par les CT s'élèvent à **≈ 1,67 Md€ en 2025** (7067, 7066, 74881) ; elles ne sont pas de la dépense publique ;
   - subventions d'investissement fléchées de l'État reçues en fonction enseignement : **DDEC 290 M€** (dont 275 M€ par les départements) et **DRES 635 M€**, plus environ 0,52 Md€ d'autres aides de l'État (subventions diverses 0,40 ; DETR, DSIL et DSID 0,12) ;
   - subventions d'investissement entre collectivités : ≈ 0,31 Md€ ;
   - les **1,41 Md€ de subventions de l'État aux EPLE pour les AED** n'apparaissent pas dans les budgets des CT (pas de double compte avec la DGCL) ; en comptabilité nationale, les EPLE sont toutefois des APUL.
7. **Écart DGFiP / DEPP pour les écoles** (ajout G3, voir le § 8, qui remplace le § 3 pour la couverture) :
   - couverture hors COM, écoles fermées appariées : **70,61 %** des élèves du public ;
   - reconstitution comptable 2025 nette des familles : **18,6 Md€** ;
   - DEPP 2025 (CT → écoles publiques + privées, 2024p porté en 2025) : **22,3 Md€** ;
   - l'écart (3,7 Md€, soit 593 € par écolier) s'explique surtout par la **quote-part d'administration générale** que la DEPP ajoute aux communes (≈ 2,9-3,6 Md€). L'extrapolation aux petites communes n'est pas en cause : le bloc DEPP est même plus bas ;
   - après une reconstitution « à la DEPP » (21,8 Md€), le résidu n'est plus que de 0,5 Md€.

---

## 1. Dépenses d'enseignement par niveau de collectivité (DGCL, CLC 2026, 4F « Ventilation fonctionnelle CG25 »)

Fichier : `DGCL_CLC2026_4F_Ventilation_fonctionnelle_CG25.xlsx`. Extraction complète avec les cellules : `extractions/DGCL_4F_enseignement_transport_2024_2025.csv`.
Champ : budgets principaux, opérations réelles, comptes de gestion (données DGFiP) ; F hors charges financières, I hors remboursements.

| Ligne (M€) | 2025 F | 2025 I | **2025 total** | 2024 total | Emplacement (2025 ; 2024) |
|---|---|---|---|---|---|
| **Communes ≥ 3 500 hab. (Paris inclus)** – Enseignement, formation et apprentissage | 10 832,3 | 3 575,0 | **14 407,4** | 14 109,2 | F1 Comm B16:D16 ; P16:R16 |
| dont services communs | 1 475,2 | 321,4 | 1 796,7 | 1 731,8 | l. 17 |
| dont 1er degré | 5 499,2 | 2 867,1 | 8 366,3 | 8 249,6 | l. 18 |
| dont 2nd degré | 86,4 | 25,9 | 112,3 | 113,8 | l. 19 |
| dont supérieur, professionnel, continu | 153,5 | 23,4 | 176,9 | 188,4 | l. 20 |
| dont hébergement et restauration scolaires | 3 064,0 | 297,7 | 3 361,7 | 3 260,9 | l. 21 |
| dont autres services annexes | 554,0 | 39,6 | 593,6 | 564,7 | l. 22 |
| Communes ≥ 3 500 – Transports scolaires | 59,2 | 1,9 | 61,1 | 64,2 | l. 54 |
| **Communes < 3 500 hab. (hors champ, toutes fonctions)** | 17 050,4 (charges fin. comprises) | 9 266,7 | 26 317,1 | 25 573,0 | F1 Comm l. 67 |
| **GFP** (au moins une commune ≥ 3 500 hab. ; ML incluse) – Enseignement | 856,6 | 460,6 | **1 317,2** | 1 302,9 | F2 GFP l. 16 |
| dont 1er degré / 2nd degré / supérieur et pro. / restauration / services communs / annexes | | | 335,5 / 127,1 / 352,6 / 278,8 / 146,5 / 76,7 | | F2 l. 17-22 |
| GFP – Transports scolaires | 207,9 | 1,3 | 209,2 | 211,8 | F2 l. 54 |
| **Départements** – Enseignement | 3 912,0 | 2 610,4 | **6 522,4** | 6 663,3 | F3 Dept l. 13 |
| dont services communs | 577,8 | 8,0 | 585,8 | 635,9 | l. 14 |
| dont 1er degré | 2,0 | 89,8 | 91,8 | 83,4 | l. 15 |
| dont **2nd degré (collèges)** | 3 118,1 | 2 412,5 | **5 530,6** | 5 600,8 | l. 16 |
| dont supérieur, professionnel / autres services annexes | | | 171,4 / 142,9 | 195,6 / 147,6 | l. 17-18 |
| Départements – Transports scolaires | 262,0 | 0,0 | 262,0 | 274,7 | F3 l. 53 |
| **Régions et CTU** – Enseignement | 8 538,3 | 3 350,5 | **11 888,8** | 12 187,1 | F4 Reg+CTU l. 12 |
| dont services communs / 1er degré | | | 83,6 / 1,6 | 89,6 / 3,4 | l. 13-14 |
| dont **2nd degré (lycées)** | 4 338,5 | 2 535,8 | **6 874,3** | 6 899,9 | l. 15 |
| dont supérieur, professionnel et continu | 3 953,4 | 503,2 | 4 456,6 | 4 696,9 | l. 16 |
| … dont supérieur / formation professionnelle / apprentissage / sanitaire et social | | | 348,3 / 2 339,6 / 251,2 / 1 517,5 | | l. 17-20 |
| dont autres services annexes (cités scolaires comprises, voir § 2) | | | 472,7 | 497,3 | l. 21 |
| Régions et CTU – Transports scolaires | 1 619,2 | 1,5 | 1 620,7 | 1 643,0 | F4 l. 42 |
| **Ensemble (F5)** – Enseignement | 24 022,5 | 9 786,7 | **33 809,2** | 34 234,1 | F5 Ens l. 11 |
| dont 1er degré / 2nd degré | | | 8 653,9 / 12 674,3 | 8 652,7 / 12 820,5 | l. 13-14 |
| Ensemble – Transports scolaires | 2 155,6 | 3,2 | **2 158,8** | 2 188,9 | F5 l. 37 |
| Budgets annexes (code activité 03 ou 23) – Enseignement | 122,3 | 12,9 | 135,2 | 130,8 | F6 l. 8 |
| **Syndicats** (codes activité 03, 23 ; non consolidés) – Enseignement | 455,3 | 75,2 | **530,5** | 512,0 | F6 l. 30 |

Données de contexte (F1 Série) :
- en 2025, les communes ≥ 3 500 hab. comptent 48,1 M d'habitants et 3 303 budgets (N5, N6) ;
- les communes < 3 500 hab. comptent 21,2 M d'habitants et 31 572 budgets (N72, N73).

La dépense d'enseignement des collectivités recule de 1,2 % en 2025 (présentation 4A, p. 2).

**Anomalies du fichier 4F à signaler** :
- (a) F5 n'est pas la somme de F1 à F4. Somme des quatre tableaux pour l'enseignement : 34 135,8 M€, contre 33 809,2 M€ dans F5 (écart −326,6 M€). L'écart n'est pas une simple consolidation : −141 M€ au 1er degré et +30 M€ au 2nd degré en série. Il est **préférable d'utiliser F1 à F4**.
- (b) Dans F5, la ligne « Autres services annexes » englobe la restauration scolaire. Sa colonne 2024 (M16 = 912,8) l'omet, contrairement à la série (« F5 Série », M25 = 4 168,3). L'« évolution » affichée (+278 %) est donc fausse.
- (c) Toujours dans F5, les lignes 48-49 (charges financières, hors champ) ont des colonnes 2024 incohérentes.

## 2. Décomposition par nature et par sous-fonction (DGFiP 2025, calcul)

Source : export agrégé de la balance DGFiP « nature-fonction » 2025 (`DGFiP_balances_nature-fonction_2025_fonction2_et_81_agrege_API.csv`).

**Méthode**
- Opérations réelles = OBNETDEB − OOBDEB (et de même au crédit).
- Fonctionnement = débit net de la classe 6, hors 66, 675, 676 et 68.
- Investissement = débit des comptes 20, 21 et 23, moins le crédit des comptes 236 à 238, plus 204, 13, 26, 27, 45x et 481.
- Budgets votés par fonction : codes 90x (investissement) et 93x (fonctionnement) suivis du code fonctionnel.

**Validation** contre la DGCL :
- départements, fonctionnement : 3 912,2 contre 3 912,0 ;
- régions + CTU, fonctionnement : 8 538,3 contre 8 538,3 ;
- 2nd degré des départements, investissement : 2 409,6 contre 2 412,5 ;
- OFGL, fonction 221 « Collèges » 2025 : 5 744,1 M€, contre ≈ 5 741 M€ dans ma décomposition (départements + ML + Paris).

**Couverture** : la fonction 2 des communes ne couvre presque que les communes ≥ 3 500 hab. Côté fonctionnement : 10 885 M€ contre 10 832 M€ pour la DGCL (+0,5 %).

Périmètres retenus (hypothèse H1) et totaux des budgets principaux 2025 (`extractions/DGFiP_2025_enseignement_synthese_niveau_perimetre_BP.csv`) :

| Périmètre (M€) | F | I | Total |
|---|---|---|---|
| Écoles – communes couvertes (fonctions 20, 21x, 28x, 29) | 10 626,1 | 3 519,3 | **14 145,4** |
| Écoles – GFP | 771,7 | 220,8 | 992,5 |
| Collèges – départements (20, 22x, 24, 28x, 29) | 3 808,4 | 2 448,1 | **6 256,5** |
| Collèges – CTU / ML / Paris (cas particuliers) | | | 92,2 / 128,2 / 154,4 |
| Lycées – régions et CTU (20, 222, 223, 24, 28x, 29) | 4 536,1 | 2 801,7 | **7 337,8** |
| Transports scolaires (fonction 81) – communes / GFP / départements / régions / syndicats | | | 70,5 / 221,0 / 262,0 / 1 620,7 / 178,6 |
| Hors scolaire – régions et CTU (supérieur, formation professionnelle, apprentissage, sanitaire et social) | 3 953,5 | 503,2 | 4 456,7 |

**Postes clés** (M€, BP 2025, `extractions/DGFiP_2025_enseignement_postes_cles_budgets_principaux.csv` ; libellés M57 officiels de l'OFGL) :

| Poste | Écoles (communes) | Collèges (départements) | Lycées (régions + CTU) |
|---|---|---|---|
| Personnel (621, 631, 633, 64) : ATSEM, agents d'entretien et de restauration, ATTEE | **6 745,8** | **1 914,1** | **2 577,5** |
| Alimentation, prestations, contrats (60623, 6042, 611) | 1 448,6 | 59,6 | 36,2 |
| Énergie et fluides (6061x, 60621-22) | 543,1 | 174,2 | 161,7 |
| Entretien, maintenance, nettoyage (6152x, 6156, 6283) | 298,0 | 159,3 | 63,9 |
| Fournitures scolaires (6067) | 140,6 | 1,6 | 11,4 |
| Autres achats (60-62) | 484,9 | 156,2 | 131,1 |
| Dotations de fonctionnement aux EPLE publics (655111 / 655121) | — | **572,6** | **871,4** |
| Dotations aux établissements privés sous contrat (655112 / 655122) | — | 399,2 | 450,1 |
| Dotations non subdivisées (65511 / 65512) | — | 83,2 | — |
| Subventions aux caisses des écoles (657364) | 292,3 | — | — |
| Autres contributions obligatoires (6558 : forfait des écoles privées, frais de scolarité intercommunaux) | 350,1 | 7,3 | 0,0 |
| Autres subventions et participations (65x) | 286,4 | 189,4 | 199,7 |
| Autres charges de fonctionnement | 36,0 | 91,6 | 33,1 |
| **Constructions, rénovations, grosses réparations** (231x, 2131x/21312 bâtiments scolaires, 2135x, 217x, 2317 biens mis à disposition, 236-238 avances) | **3 039,0** | **2 010,4** | **1 992,6** |
| Équipement : informatique, mobilier, matériel (218x, 215x) | 267,7 | 242,7 | 407,2 |
| Études, logiciels (20 hors 204) | 106,4 | 85,1 | 111,6 |
| Subventions d'équipement versées (204) | 4,8 | 84,4 | 237,6 |
| Autres investissements | 101,3 | 25,6 | 52,6 |
| **Total** | **14 145,4** | **6 256,5** | **7 337,8** |

**Écoles, par sous-fonction** (communes, BP 2025, M€ ; entre parenthèses, € par élève du public des communes couvertes, 3 765 723 élèves en année civile 2025) :
- 20 services communs : 1 798,1 (477 €) ;
- 211 écoles maternelles : 2 625,0 (697 €) ;
- 212 écoles primaires : 2 782,3 (739 €) ;
- 213 classes regroupées : 2 998,9 (796 €) ;
- **281 hébergement et restauration** : 3 384,1, dont F 3 083,9 et I 300,2 (899 €) ;
- 282 sport scolaire : 58,3 (15 €) ;
- 283 médecine scolaire : 13,4 (4 €) ;
- 284 classes de découverte : 91,7 (24 €) ;
- 288 autres services annexes : 390,1 (104 €).

Total : 14 145,3 M€, soit **3 756 € par élève**.

**Restauration scolaire (281), BP 2025** :
- communes : 3 384,1 M€ ; GFP : 325,8 ; départements : 59,7 ; régions : 77,4 ; syndicats : 30,2 ;
- dans les collèges et lycées, l'essentiel de la restauration est géré par les EPLE (service annexe d'hébergement, financé par les familles et les dotations) et n'apparaît pas ici.

**Ce qui n'est pas décomposable** :
- construction neuve et rénovation sont confondues dans le compte 2313 ;
- le coût des ATSEM n'est pas isolé : il est inclus dans le personnel des écoles maternelles (211) ;
- l'accueil **périscolaire** (accueils de loisirs) relève surtout de la fonction 4 (jeunesse) et non de la fonction 2. Il n'est donc pas compté ici, sauf garderie et étude éventuellement imputées en 288 ou 211-213.

## 3. Communes sans comptabilité fonctionnelle : couverture et extrapolation (calcul, 2025)

Fichiers : `extractions/DGFiP_MEN_2025_communes_couverture_et_depense_par_eleve.csv` (script, partie C).

**Effectifs.** Élèves des écoles publiques (open data MEN, appariés à la commune Insee via l'annuaire) :
- rentrée 2024 : 5 462 329 ; rentrée 2025 : 5 365 524 ;
- non appariés : 57 174 en 2024 et 23 507 en 2025 (écoles fermées depuis) ;
- année civile 2025 (2/3 R2024 + 1/3 R2025) : 5 384 109.

**Couverture.** Communes dont la dépense de fonction 20, 21, 28 ou 29 est positive en 2025 :
- **3 336 communes sur 20 729** ayant une école publique ;
- elles scolarisent **3 765 723 élèves, soit 69,94 %**.
- L'OFGL estimait environ 62 % en 2022 (Cap sur n° 21, p. 5).

**Dépense moyenne** des communes couvertes :
- **3 752 € par élève du public** (F 2 821 €, I 931 €) ;
- médiane communale : 2 983 € (F 2 399 €).

**Courbe en U** selon le nombre d'élèves du public de la commune (€ par élève, total) :

| Élèves du public | < 100 | 100-199 | 200-299 | 300-499 | 500-999 | 1 000-1 999 | 2 000-4 999 | ≥ 5 000 |
|---|---|---|---|---|---|---|---|---|
| € par élève | 6 088 (17 communes) | 4 970 | 3 475 | **3 014** | 3 341 | 3 452 | 3 701 | 4 370 (105 communes, 1,13 M d'élèves) |

**Non couverts.** **1 618 386 élèves dans 17 393 communes**, dont 1,46 M dans des communes de moins de 300 élèves du public.

**Extrapolation (hypothèse H2)** de la dépense « écoles » des communes non couvertes :
- bas : 3 014 €/élève → **4 878 M€** ;
- central, méthode OFGL (moyenne couverte) : 3 752 € → **6 072 M€**, soit un total communes de **20 208 M€** (facteur 1/0,6994 = 1,43) ;
- haut : 3 797 €, moyenne des petites communes couvertes de moins de 300 élèves → **6 145 M€**.

Attention aux recouvrements : une partie de la dépense des élèves « non couverts » est portée par les GFP (992,5 M€ d'écoles) et les syndicats scolaires (SIVOS ; 530,5 M€ d'enseignement en F6). **Ne pas additionner l'extrapolation et la totalité GFP + syndicats** sans le signaler (hypothèse H3).

**Recoupement indicatif avec la DEPP (2025)** :
- somme « scolaire » des CT à partir des comptes, hors syndicats et budgets annexes :
  - écoles : 15 231 M€ + petites communes 4 878 à 6 145 M€ ;
  - collèges : 6 631 M€ ;
  - lycées : 7 338 M€ ;
  - transports scolaires : 2 353 M€ ;
  - total : **36,4 à 37,7 Md€** (brut, participations des familles comprises) ;
- DEPP 2025p, CT, 1er + 2nd degrés, financement initial : **37,5 Md€**.

Les concepts diffèrent : la DEPP retire la part des cantines payée par les familles, ajoute une quote-part de l'administration générale des communes, inclut l'apprentissage au 2nd degré, etc. La proximité est un ordre de grandeur, pas une validation.

## 4. Part et montant des CT dans la DIE du 1er et du 2nd degré (DEPP)

`extractions/DEPP_collectivites_parts_montants_par_niveau.csv` (cellules exactes).

**NI 26.42 (septembre 2026)** : 2025p ; 2024 définitif.
- **Part des CT en financement initial, 2025p** (Figure 4, B33 et C33) :
  - 1er degré : **38,41 %** de 59 999 M€ de DIE (Figure 5 B32), soit **23 046 M€** (calcul) ;
  - 2nd degré, apprentissage compris : **19,63 %** de 73 754 M€ (B33), soit **14 477 M€** (calcul).
  - Supérieur : 7,32 % ; tous niveaux : 22,86 %.
- **Par élève** (calcul = part × dépense moyenne, Figure 6) :
  - 9 440 € × 38,41 % = **3 626 €** par écolier ;
  - 11 780 € × 19,63 % = **2 312 €** par élève du 2nd degré.
  - Ces montants ne sont **pas publiés** par la DEPP.
- **2024p** (NI 25.52, rapporté par `depp_compte_education/NOTES.md` § 3c) : CT 38,33 % au 1er degré et 20,12 % au 2nd degré.
- **DIE totale financée par les CT**, en financement initial (Figure 3bis) : **45 539 M€ en 2025p** (F6) et 45 328 M€ en 2024 définitif (E6).
  - Répartition en 2025p (Figure 2, C7:C9) : communes 13,13 %, départements 3,58 %, régions 6,15 % de la DIE ;
  - soit environ **26 158 / 7 135 / 12 246 M€** (calcul, part × DIE totale de F10).
  - Texte de la NI (p. 2) : « les communes financent […] 57 % ; les départements en financent 16 % et les régions, qui ont des compétences élargies, 27 % ».
- **Financement final 2025p** (Figure 2bis, F6:F9) : CT 22,66 % (communes 13,24 ; départements 3,50 ; régions 5,91). L'écart avec le financement initial est faible (bourses).
- **Évolution 2025** (NI 26.42, p. 3) : dépenses d'éducation des CT +0,5 % (−0,6 % en euros constants) :
  - personnel +2,2 % (hausse du taux de cotisation vieillesse CNRACL) ;
  - fonctionnement −1,7 % (énergie, dotations aux établissements) ;
  - investissement +1,5 % : communes +5,1 % (plan « Rénovation des écoles », Fonds vert), départements −3,7 %, régions −0,2 %.

**RERS 2026, fiche 10.02, tableau 4** (2024p, financement **final**, M€, colonne F) :

| Activité | 1er degré | 2nd degré | Supérieur | Extrascolaire | Hébergement-restauration (tous niveaux) | Transports scolaires | Fournitures et livres | Administration générale | Médecine scolaire | Orientation | **Total CT** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Montant | **16 684,1** | **12 120,0** | 2 926,0 | 4 605,7 | **5 929,2** | **2 484,8** | 185,8 | 121,8 | 17,7 | 16,1 | **45 091,2** |

**RERS 2026, fiche 10.04, tableau 2** (2024p, financement final des producteurs, colonne E) :
- écoles publiques **20 608,1 M€** (40,56 % de leur financement, Graphique 3 C6) ;
- collèges et lycées publics **12 715,3 M€** (22,03 %, C7) ;
- écoles privées sous contrat 1 141,8 M€ (25,87 %, J6) ;
- collèges et lycées privés sous contrat 1 031,5 M€ (9,59 %, J7) ;
- centres de formation artistique (conservatoires) 1 935,8 M€ ;
- total producteurs 42 420,7 M€.

**Géographie de l'École 2026, fiche 22** (xlsx : 22.1-22.3 C113 ; 22.4-22.6 C29) :
- **départements et CTU : 2 010 € par collégien et par an** (F 1 210 € y compris personnel, I 800 €) ; extrêmes : Loire 1 450 €, Lozère 3 530 € ;
- **régions et CTU : 3 000 € par lycéen** (F 1 850 €, I 1 140 €) ; extrêmes : Île-de-France 2 380 €, Guyane 5 830 € ;
- champ : moyenne annuelle 2021-2023, euros constants 2023, public + privé sous contrat, MEN, hors apprentissage, hors Mayotte ;
- dépenses retenues : uniquement celles destinées aux collégiens (départements) ou aux lycéens (régions) (PDF p. 108) ;
- départements et régions ont consacré **14,5 Md€** aux établissements du 2nd degré en 2023 (PDF p. 54, dossier voisin) ;
- **aucun indicateur équivalent n'est publié pour les communes.**

**Mes calculs 2025**, à comparer (BP DGFiP ; dénominateurs public + privé sous contrat, MEN, année civile 2025 issus de NI 25.59 via `effectifs_nationaux/NOTES.md`) :
- **collégiens** (3 377 864) : 6 256,5 M€ → **1 852 €** (F 1 127, I 725) ; 1 963 € si l'on ajoute CTU, ML et Paris (+374,8 M€) ;
- **lycéens GT + pro** (2 251 702) : 7 337,8 M€ → **3 259 €** (F 2 015, I 1 244). Valeur légèrement surestimée : lycées agricoles et post-bac financés mais hors dénominateur.

**OFGL (éditions antérieures, utiles pour la structure des coûts)** :
- **Cap sur n° 21 (2023, données 2022)** :
  - investissements scolaires des CT : 8,4 Md€ (écoles 3,6, y compris l'estimation des communes hors champ ; collèges 2,5 ; lycées 2,3) ;
  - par élève du public : **646 € (écolier), 916 € (collégien), 1 317 € (lycéen)** ; dont constructions 509 / 734 / 939 € et matériel 19 / 118 / 301 € (p. 3, 5, 8) ;
  - les subventions reçues couvrent 17 % de l'investissement scolaire des communes et des départements et 33 % de celui des régions ; l'État en fournit 50 % / 89 % / 93 % (p. 3, 10).
- **Cap sur n° 10 (2019, données 2018)** :
  - coût communal **médian** de fonctionnement par élève du primaire public : **950 €** (maternelle 1 508 €, élémentaire 575 €) ; moyenne 1 051 € ;
  - échantillon : 2 126 communes, 43 % des élèves ;
  - le personnel représente environ 3/4 du coût (82 % en maternelle à cause des ATSEM) ; investissement médian 176 € (p. 5, 8-12) ;
  - ces données sont anciennes et portent sur la seule sous-fonction 21, d'où un niveau plus bas que mes 3 752 €, qui incluent restauration et services communs.

## 5. Transferts de l'État au titre de l'éducation et doubles comptes (point 4)

**Prélèvements sur recettes (PSR) de l'État** (DGCL chapitre 6, onglet 6.1 l. 12-14 ; exécution onglet 6.2 l. 12-14) :

| PSR | LFI 2026 | Exécution 2024 |
|---|---|---|
| DDEC (départements) | **326 M€** | 326 M€ |
| DRES (régions) | **661 M€** | 661 M€ |
| DGCES (Corse) | 3 M€ | 3 M€ |

- Exécution 2025 (PLRG 2025, dans `budget_etat/NOTES.md` § 6) : DRES 661 186 704 €, DDEC 326 316 128 €, DGCES 2 685 550 €, logement des instituteurs (DSI) 2 611 157 €.
- La DSI vaut 3,9 M€ en LFI 2026 (6.1 version_web F10).
- Ces dotations sont **figées depuis 2008**. Ce sont des PSR, **hors mission « Enseignement scolaire »**.

**Autres flux de l'État**
- Subventions de fonctionnement et d'équipement des « autres ministères » aux CT : 4 391 M€ en LFI 2026, tous domaines (6.1 version_web F71). **Non ventilées par ministère dans la DGCL** : le Jaune « Transferts financiers de l'État aux CT » n'a pas été récupéré.
- DGD : 1 675,7 M€ en LFI 2026 (l. 50). Elle comprend la DGD « instruction obligatoire à 3 ans », 48,48 M€ au PLF 2027 (PAP RCT p. 36-37, dossier `budget_etat`).
- Fiscalité transférée de l'acte II (TICPE régions 3 553 M€, TICPE et TSCA départements, LFI 2026, l. 80-83) : elle compense globalement les transferts de 2004, **dont les TOS/ATTEE des collèges et lycées**. La part propre à l'éducation n'est pas isolée.

**Dans les comptes des CT** (recettes réelles, fonction 2 scolaire, BP 2025 ; `extractions/DGFiP_2025_enseignement_recettes_par_niveau_BP.csv`) :

| Niveau | Recettes de fonctionnement (familles et autres) | Subventions d'investissement reçues |
|---|---|---|
| Communes | 1 843,8 M€, dont **7067 « redevances des services périscolaires et d'enseignement » 1 193,2** ; 7066 : 60,8 ; CAF : 26,7 | 688,9 M€ : État 240,5 (1321 + 1311), DSIL 36,2, DETR 22,0, départements 115,7, GFP 76,3, régions 63,6, FEDER 19,6 |
| Départements | 265,2 M€, dont **74881 « participation des familles à la restauration et à l'hébergement » 136,8** | 412,8 M€ : **DDEC 274,9**, DSID 44,2, État 39,7 |
| Régions et CTU | 252,7 M€, dont **74881 : 145,7** ; FSE : 13,5 | 793,2 M€ : **DRES 634,9**, État 109,3, FEDER 23,5 |
| GFP | 221,5 M€, dont 7067 : 103,2 | 49,9 M€ |

**Mission « Enseignement scolaire », titre 6, catégorie 63 « Transferts aux collectivités territoriales »** (exécution 2025, PLRG 2025) :
- par programme : P230 1 523,3 M€ ; P141 90,8 ; P143 53,4 ; P140 30,6 ; P214 14,4 ; P139 0,1 ; total ≈ 1 712,7 M€ ;
- **l'essentiel va aux EPLE, pas aux budgets des CT** : RAP 2025 p. 168, P230 action 01 « Subventions versées au titre des personnels d'assistance éducative : 1 411 836 656 € […] subventions versées aux EPLE qui rémunèrent ces personnels » ;
- aux communes : service minimum d'accueil 6,4 M€ (P140, p. 60), subventions de santé scolaire aux villes à régime autonome 2,7 M€ (P230, p. 171), internats ruraux.

**Ce que fait la DEPP** (Dossier 206, p. 18) :
- les transferts sont comptés « deux fois : en positif pour le financeur qui les verse et en négatif pour celui qui les reçoit » ;
- la DRES et la DDEC « sont financées depuis 2007 par des taxes affectées et ne sont plus considérées comme des transferts » : la dépense est attribuée aux départements et aux régions ;
- la DGD n'est jamais traitée comme un transfert (ressource globale non affectée) ;
- le financeur « Communes » comprend groupements, syndicats et caisses des écoles (p. 20) ;
- les cantines sont comptées nettes de la part payée par les familles, et une quote-part de l'administration générale des communes est ajoutée (p. 36).

**Comptabilité nationale** (DGCL chapitre 3, onglet « 3.5 », 2024, Md€) :
- Enseignement : APUC 106,1 (B15) + APUL **46,0** (C15) = 152,1 ; or l'**ensemble APU consolidé = 148,6** (E15). L'écart de 3,5 Md€ (calcul) correspond aux flux entre administrations neutralisés (note b l. 19).
- Les APUL incluent les EPLE (ODAL, « hors masse salariale des enseignants », chapitre 3 PDF p. 2), ainsi que les CT, syndicats, caisses des écoles, etc.
- Part de l'enseignement dans les dépenses des APUL : 13,95 % (C33).

**Méthode recommandée pour une somme de budgets publics (C2)**, hypothèses H4 à H6 :
1. Compter chaque euro **une seule fois, chez le dernier payeur public**. Côté CT : dépense brute de la fonction enseignement (F + I) des communes, GFP, syndicats, départements et régions, plus le transport scolaire.
2. Côté État : si l'on prend la mission « Enseignement scolaire » (titres 2 à 6), il ne faut **rien retrancher pour les AED** (versés aux EPLE, absents des budgets des CT). Il faut retrancher les quelques transferts de la catégorie 63 reçus par les budgets des CT (quelques dizaines de M€).
3. **Si l'on ajoute à l'État** les PSR (DDEC, DRES, DGCES, DSI ≈ 0,99 Md€), la DSIL, la DETR ou le Fonds vert : retrancher le même montant des CT. Montants reçus en fonction 2 scolaire : DDEC 290,0 M€ (dont départements 274,9) ; DRES 634,9 M€ ; DETR, DSIL et DSID 119,1 M€ ; subventions diverses de l'État 1321 et 1311 401,3 M€. Sinon, laisser ces sommes aux CT, comme le fait la DEPP.
4. **Retirer la part payée par les familles** portée par les CT (7067, 7066, 74881 = **1 671,6 M€** en 2025, BP) : ce n'est pas de la dépense publique. Répartition : communes 1 258,2 ; régions 145,7 ; départements 140,3 ; GFP 111,5 ; syndicats 13,8 ; EPL 2,0. Ce montant n'inclut pas les familles des petites communes non couvertes.
5. **Flux entre collectivités** : subventions d'investissement reçues d'autres CT en fonction 2 scolaire = 311,1 M€, dont 272,8 M€ reçus par les communes (départements 115,7 ; GFP 76,3 ; régions 63,6…). S'y ajoutent les contributions entre communes (6558, 74748, 74741). Ces flux sont à retirer une fois si l'on additionne les niveaux. Il n'existe pas de consolidation par fonction publiée (la consolidation DGCL 4.12 n'est pas fonctionnelle).
6. Ne pas ajouter les dépenses propres des **EPLE** (comptes financiers) aux dotations des CT et aux subventions de l'État : ce sont les mêmes fonds. Pour la COFOG, utiliser le **total APU consolidé**.

## 6. Données officielles par établissement côté collectivités (point 5)

- **Région Centre-Val de Loire** : dotations de fonctionnement versées à chaque lycée public, par type de dotation et code UAI, série annuelle 2017-2025 (data.gouv.fr / data.centrevaldeloire.fr, ODbL). Fichier 2025 téléchargé :
  - 98 lycées (dont agricoles et EREA), **37,43 M€** ;
  - par type : DGF 34,54 M€, travaux du propriétaire 1,61, compléments de DGF 0,62, transports EPS 0,40, charges particulières 0,14, transports des élèves 0,12 ;
  - moyenne 381 907 € par lycée, médiane 346 554 € (de 52 984 € à 1 291 287 €).
  - Ces montants ne couvrent **que les dotations versées aux EPLE**. Le personnel ATTEE, l'investissement et l'entretien réalisés directement par la région sont absents : au niveau national, 871 M€ de dotations aux lycées publics contre 7 338 M€ de dépenses « lycées ».
- **Département de la Gironde** : « Montant des dotations des collèges publics » (2015-2017, data.gouv.fr). Exemple ancien. Les jeux départementaux récents par collège sont rares (souvent de simples annuaires sans montant, comme dans les Pyrénées-Atlantiques).
- **Comptes financiers des EPLE** :
  - pas d'open data national (application COFI / Op@le, DAF-DEPP) ;
  - l'académie de Normandie a publié des agrégats par catégorie (2018) et la **masse salariale de l'État par établissement** (coût employeur, 2016-2020).
- **Communes** : aucune donnée publique de dépense par école. Les balances DGFiP sont par collectivité ; le calcul par élève de la commune est possible (fichier de couverture du § 3), pas par école.
- **SNEE (plan de relance 2021-2022)** : subvention de l'État par collectivité et liste des écoles bénéficiaires. Il illustre un transfert de l'État aux CT.

## 7. Conventions, limites et points d'attention

- **Champ** des tableaux DGCL : BP en opérations réelles (BA et syndicats à part). Communes ≥ 3 500 hab. seulement. Départements hors Paris, ML, Corse, Guyane, Martinique (comptés ailleurs). Régions avec les CTU, hors Mayotte (population).
- **Investissement** compté en flux de l'année, sans amortissement, comme dans la DEPP. Il est volatil : la DEPP lisse sur 3 ans dans Géographie de l'École.
- Les dépenses d'enseignement des régions comprennent **4,46 Md€ hors scolaire** (formation professionnelle, sanitaire et social, apprentissage, supérieur). Il faut les exclure pour un coût par élève.
- Dans la DGFiP, les « services communs » (20) et les « cités scolaires » (24) sont rattachés entièrement au niveau scolaire de la collectivité (hypothèse H1). Les départements y portent 585,8 M€, dont une large part de personnel des collèges (OFGL : 646 M€ de frais de personnel en fonction 20 en 2025).
- Les caisses des écoles, budgets distincts, sont peu visibles dans la balance fonctionnelle (EPL, code activité 03 : 38,9 M€). Seules les subventions des communes (292,3 M€) sont comptées.
- **Euros courants partout.** DEPP 2025p provisoire (révision en septembre 2027). DGCL 2025 = comptes de gestion. Géographie de l'École = euros constants 2023 (moyenne 2021-2023).
- Années : comptes CT par année civile. Dénominateurs à pondérer 2/3 R(N-1) + 1/3 R(N), convention DEPP.

---

## 8. Tâche G3 (ajout du 2026-10-04) : écart entre la dépense communale reconstituée (DGFiP 2025) et le compte DEPP

Script : `extractions/_script_G3_ecart_DGFiP_DEPP.py` ; sorties `extractions/G3_*.csv`. Il ne lit que des fichiers bruts. Pour la couverture, ce calcul **remplace le § 3** (COM exclues, écoles fermées appariées). Le fichier `DGFiP_MEN_2025_communes_couverture_et_depense_par_eleve.csv` est conservé pour mémoire.

### 8.1 Ce que la DEPP publie sur sa méthode « communes »

- **Dossier DEPP n° 206** (avril 2016 ; `depp_compte_education/`, n° de page du PDF, page imprimée = PDF − 2) :
  - le financeur « Communes » regroupe communes, groupements et syndicats de communes, communautés urbaines et caisses des écoles (PDF p. 20) ;
  - source : « Comptes des communes, groupements de communes, syndicats et caisses des écoles (DGFiP) » (tableau 9, PDF p. 33) ;
  - les comptes des écoles publiques sont « reconstitués à partir de l'étude des comptes administratifs des communes », complétés par le budget de l'État, l'ASP et la dépense des familles issue d'une enquête DEPP (PDF p. 21) ;
  - les écoles privées sous contrat sont reconstituées « à partir du budget de l'État, des comptes des communes et des droits de scolarité » (PDF p. 25) ;
  - les dépenses de garderie et d'étude, ainsi que celles des rythmes scolaires, sont comprises dans l'activité « enseignement » (PDF p. 17) ;
  - les conservatoires et « une partie de l'administration des collectivités locales » sont réintégrés en fonction 2 (note 16, PDF p. 32) ;
  - **quote-part d'administration générale** (PDF p. 36) : rapport entre les dépenses d'éducation identifiées et les dépenses totales des communes, appliqué à leur administration générale, puis réparti par niveau sur l'activité « enseignement ». Effet du changement de méthode en 2012 : **+0,6 Md€** ;
  - **cantines nettes des familles** (même page) : **−1,5 Md€** en 2012.
  - Le dossier ne dit rien du traitement des communes sans comptabilité fonctionnelle, ni de l'estimation du forfait des écoles privées.
- **NI 19.07** (mars 2019 ; xls, onglet « Définitions et méthodologie », zone de texte) :
  - comptes définitifs des CT tirés de leurs comptes, « ventilés par nature et fonction » ;
  - **compte provisoire « estimé à partir des évolutions des budgets primitifs ou d'indices de prix »** ;
  - en financeur final, une subvention de l'État à une construction scolaire est attribuée à la CT maître d'ouvrage.
- **NI 24.45** (novembre 2024) : le PDF ne contient pas d'encadré méthodologique (« voir définitions et méthodologie en ligne »). La page web n'est plus en ligne : education.gouv.fr renvoie 404 et le DOI 10.48464/ni-24-45 mène à HAL, protégé par captcha. La NI 26.42 (texte méthodologique du xlsx, déjà local) dit seulement que « la mesure […] des communes a été revue » en 2012-2013.
- **Source primaire décisive : Cour des comptes, *L'enseignement primaire*, RPT de mai 2025, p. 31-32** (`recoupements/`) :
  - les communes de moins de 3 500 habitants et les groupements sans commune de 3 500 habitants ou plus « scolarisent 31 % des élèves de l'enseignement public et représenteraient plus d'un cinquième de la dépense d'éducation des communes (4,2 Md€) » ;
  - « les services de l'État les traitent comme un bloc homogène, et considèrent que leur ventilation budgétaire est similaire à celle observée dans les communes comptant entre 3 500 et 10 000 habitants » ;
  - « Ce *ratio* a été établi en 2010 et […] n'a jamais été révisé depuis ».
  - L'année des 4,2 Md€ n'est pas précisée (vraisemblablement 2022 : la même section donne 19 Md€ de CT pour le 1er degré en 2022, p. 29).

### 8.2 Forfait communal des écoles privées sous contrat

- **Aucune estimation nationale officielle autre que celle de la DEPP** :
  - CT vers écoles privées sous contrat : **1 141,8 M€ en 2024p** (RERS 2026, 10.04, T2 E19) ;
  - CT vers privé du 1er et du 2nd degré : 1,9 Md€ en 2022 (DEPP, cité par le rapport AN n° 2423, p. 7 et 43).
- Le rapport **AN n° 2423** (2 avril 2024) :
  - constate « l'absence de données consolidées » (p. 43) ;
  - demande, par sa **proposition n° 7** (p. 45), que les référentiels comptables des CT distinguent les dépenses vers le privé : **la M57 ne permet pas d'isoler le forfait communal** ;
  - cite la **circulaire n° 2012-025** (p. 25), qui inclut dans le coût d'un élève du public « la quote-part des services généraux de l'administration communale ».
- **Cour des comptes 2023** (privé sous contrat, p. 22) : loi Goblet, « les écoles primaires ne peuvent recevoir aucune aide de la part des communes […] en dehors du forfait communal ». Les 1 141,8 M€ de la DEPP correspondent donc en pratique au forfait communal.
- **DGFiP 2025** (communes couvertes, fonctions écoles) :
  - 6558 « autres contributions obligatoires » : **350,1 M€**, qui mêle forfait et frais de scolarité intercommunaux ;
  - 65748 « autres personnes de droit privé » : **155,1 M€** ;
  - soit **505,2 M€ au plus**, déjà inclus dans la base.
- Il reste ainsi jusqu'à ≈ 0,6 Md€ que la DGFiP ne permet pas d'identifier.
- Aucun montant DGCL ni OFGL n'a été trouvé.

### 8.3 OFGL 2026 : aucune estimation scolaire incluant les petites communes

- **Rapport complet** (V 24 août 2026, 289 p.) : il reproduit les tableaux DGCL 4F (communes ≥ 3 500 hab. seulement). Il apporte deux données utiles :
  - **annexe 7A (p. 211), caisses des écoles 2025** : 772 établissements, dépenses totales 631 M€ (dont fonctionnement 616, personnel 371). Elles sont financées par 434 M€ de dotations et participations reçues et 148 M€ de ventes ;
  - **annexe 8, tableau 6 (p. 220), redevances « périscolaire » 2025** : communes **2 161 M€** (BP + BA, Paris inclus), syndicats 149, GFP 202, ensemble 2 530 (+1,2 %).
- **Dossier « bilan du mandat 2020-2025 »** (juillet 2026, 28 p.) : il ne traite que des recettes tarifaires du périscolaire (p. 13 : −30,7 % en 2020, +35,3 % en 2021, puis ≈ +0,6 %/an en euros constants de 2020 à 2025). Il ne donne aucune estimation de la dépense scolaire du bloc communal.

### 8.4 Couverture recalculée (2025, hors COM, écoles fermées appariées)

**Écoles fermées.** Les 823 UAI absentes de l'annuaire actuel (≈ 46 000 élèves en année civile) ont été appariées. L'annuaire ne contient que les établissements ouverts : `etat` = OUVERT (68 563) ou « A FERMER » (1), ce qui explique le recours à trois autres sources.

| Méthode d'appariement | UAI | Élèves (année civile 2025) |
|---|---|---|
| Annuaire actuel | 42 418 | 5 384 109 (COM comprises) |
| IPS écoles 2024-2025 (UAI → code Insee) | 256 | 15 403 |
| Libellé de commune + département, appris sur les écoles ouvertes | 481 | 28 950 |
| COG 2026 de l'Insee (communes déléguées → commune parente) | 87 | 1 599 |
| Non appariés | 0 | 0 |

**Contrôle des appariements.** Libellés concordants à 95-98 %. Les écarts correspondent tous à des arrondissements PLM, des communes nouvelles ou des COM.

**Effectifs hors COM** (année civile 2025) :
- public : **5 379 623** (décompte national DEPP de `effectifs_nationaux` : 5 379 642) ;
- privé sous contrat : 846 510 (DEPP : 846 517) ;
- les COM retirées comptent 50 702 élèves (R2024) et 49 909 (R2025).

**Couverture** :
- **3 336 communes couvertes sur 20 848** ;
- **3 798 310 élèves, soit 70,61 %** (Cour des comptes : 31 % non couverts ; OFGL 2023 : 38 %) ;
- non couverts : **1 581 313 élèves**, dont 36 983 dans des communes de la balance fonctionnelle sans dépense « écoles ».

Les élèves non couverts vivent presque tous dans des communes de moins de 3 500 habitants : 163 951 (< 500 hab.), 373 398, 532 902 et 454 116 (2 000-3 499 hab.), contre 46 552 au-delà (`G3_eleves_par_strate_et_couverture.csv`).

**Dépense « écoles » des communes couvertes** : 14 133,8 M€ (fichiers par commune) et 14 145,4 M€ (synthèse), soit **3 720 € par élève du public**.

### 8.5 Extrapolation aux communes non couvertes (M€ 2025, écoles)

| Méthode | € par élève non couvert | Montant |
|---|---|---|
| M1 coût moyen des communes couvertes (OFGL) | 3 720 | **5 882,5** |
| M2 8 classes d'élèves du public | 4 146 | 6 556,6 |
| M3 3 classes regroupées | 3 618 | 5 720,7 |
| M4 coût des communes couvertes de 3 500-9 999 hab. | 3 057 | 4 834,3 |
| M5 « à la DEPP », ratio 2025 : écoles / dépense totale des communes couvertes de 3 500-9 999 hab. (15,48 %) × 25 842,5 M€ (31 440 communes non couvertes, OFGL) | 2 530 | 4 001,1 |
| **M5bis : 4,2 Md€ DEPP (Cour) portés en 2025** avec la dépense des communes < 3 500 hab. (DGCL F1 Série l. 228 : 22 627,3 en 2022 ; 24 071,8 en 2023 ; 26 317,1 en 2025) | 3 089 ou 2 904 | **4 884,9** (base 2022) ou 4 591,8 (base 2023) |
| Pour mémoire : facteur OFGL 1/0,62 (couverture 2022) | — | 8 662,7 |

- **La piste « extrapolation sous-estimée » ne tient pas.**
  - Une fois les COM exclues et les écoles fermées réintégrées, la pondération par taille ne donne que 6,56 Md€, et non 7,8.
  - Surtout, le bloc « petites communes » de la DEPP (≈ 4,6-4,9 Md€) est **inférieur** à M1 d'environ 1,0 Md€.
- Les classes de moins de 200 élèves couverts reposent sur 15 et 161 communes atypiques, de 3 500 habitants ou plus avec peu d'élèves du public : M2 est fragile.

**Recouvrement avec les GFP** :
- la dépense « écoles » des GFP, de la ML et des EPT s'élève à 980,5 M€ ;
- **485,2 M€** sont imputables aux élèves des communes non couvertes, au prorata des élèves de chaque EPCI (EPCI tiré de la base OFGL) ;
- 495,4 M€ concernent les élèves des communes couvertes.
- Les syndicats à code d'activité scolaire dépensent 530,5 M€ (DGCL F6) et servent surtout les petites communes.

### 8.6 Quote-part d'administration générale (règle du Dossier 206 appliquée aux comptes 2025)

**Données de base** (communes à comptabilité fonctionnelle, BP 2025) :
- dépense totale toutes fonctions : 87 447,0 M€, dont fonction 2 : 14 444,7 M€, d'où un **ratio de 16,52 %** ;
- administration générale « indéterminée » (fonctions 0, 02, 020, 021 personnel non ventilé, 028) : 19 495,6 M€ en F, 22 548,6 M€ en F + I ;
- fonction 020 seule : 17 802,1 M€ en F.

**Quote-part qui en résulte** :

| Variante | Quote-part | Dont « écoles » (97,8 % de la fonction 2) |
|---|---|---|
| Basse (020, F) | 2 940,6 M€ | 2 877,3 M€ |
| **Centrale (A00, F)** | **3 220,3 M€** | **3 151,0 M€** |
| Haute (A00, F + I) | 3 724,6 M€ | 3 644,5 M€ |

**Si la DEPP l'applique aussi au bloc des petites communes** : +0,9 à +1,3 Md€.

**Limite** : le passage à la M57 en 2024 gonfle l'administration générale.
- Selon DGCL F1 Série, communes de 3 500 hab. et plus, en F :
  - les opérations non ventilables passent de 2 554 M€ en 2023 à 802 M€ en 2024 ;
  - l'administration générale passe de 16 673 M€ à 19 336 M€.
- Une quote-part fondée sur l'administration générale augmente donc mécaniquement.

### 8.7 Tableau de passage DGFiP → DEPP (2025, M€ courants ; `G3_tableau_passage_DGFiP_DEPP_2025.csv`)

| Étape | M€ |
|---|---|
| A0 Communes couvertes, périmètre « écoles » (BP, F + I) | 14 145,4 |
| A1 + communes non couvertes (M1) | 5 882,5 |
| A2 + GFP, part des élèves des communes couvertes | 495,4 |
| A3 syndicats, réputés compris dans M1 (pour mémoire 530,5) | 0,0 |
| A4 + budgets annexes à code d'activité 03/23 | 135,2 |
| A5 + caisses des écoles hors subventions et familles (631 − 434 − 148) | 49,0 |
| A6 − familles des communes couvertes (7067, 7066, 74881) | −1 257,7 |
| A7 − familles des GFP et des syndicats | −125,6 |
| A8 − familles des communes non couvertes (même montant par élève) | −523,6 |
| A9 − fournitures scolaires (6067), extrapolation comprise | −199,1 |
| **TOTAL A, reconstitution comptable** (sans administration générale) | **18 601,5** (2 988 € par écolier public + privé) |
| B1 remplacer M1 par le bloc DEPP M5bis (base 2022) | −997,6 |
| B2 + GFP imputables aux non couverts | +485,2 |
| B3 + syndicats | +530,5 |
| B4 + quote-part d'administration générale, centrale, part « écoles » | +3 151,0 |
| **TOTAL B, reconstitution « à la DEPP »** | **21 770,6** (3 497 €) ; fourchette 20 613,1 à 23 523,7 |
| D1 DEPP, CT → écoles publiques (20 608,1) + privées (1 141,8), financement final 2024p | 21 749,9 |
| **D2 DEPP porté en 2025** (+2,505 % : financement initial des communes, NI 26.42 Fig. 2 × Fig. 3bis) | **22 294,8** (3 581 €) |
| Pour mémoire : DEPP, CT, financement initial du 1er degré 2025p (transports et fournitures compris) | 23 045,5 |
| **Écart D2 − A** | **3 693,3**, soit 593 € par écolier (687 € par élève du public) |
| **Écart D2 − B** | **524,2**, soit 84 € par écolier ; la fourchette de B encadre D2 |

**Contrôle sur les familles.** La déduction totale (A6 + A7 + A8 = 1 906,9 M€) coïncide avec le financement des écoles publiques par les ménages selon la DEPP (1 905,7 M€ en 2024p, RERS 10.04 T2 G9).

**Ventilation de l'écart de 3,7 Md€** :
1. **quote-part d'administration générale de la DEPP : +2,9 à +3,6 Md€.** C'est le facteur principal, documenté mais non publié en montant ;
2. ajout séparé des GFP (part non couverte) et des syndicats : +1,0 Md€ ;
3. bloc DEPP des petites communes inférieur à M1 : −1,0 Md€ (−1,3 si la base est 2023 ; −1,9 avec M5) ;
4. résidu ≈ +0,5 Md€. Pistes :
   - forfait privé non identifiable en M57 (≤ 0,6) ;
   - quote-part appliquée aussi aux petites communes (+0,9 à +1,3) ;
   - périscolaire hors fonction 2 ;
   - restauration en budgets annexes hors codes 03/23 ;
   - part des conservatoires dans le ratio ;
   - passage de 2024p à 2025 et révision de 2024 (2024 définitif : CT −0,16 % par rapport à 2024p).
5. Les caisses des écoles pèsent peu (+0,05 Md€).

**Conséquence pour l'approche B** (hypothèse à documenter) :
- soit le coût comptable **sans frais généraux** : ≈ 18,6 Md€, soit ≈ 2 990 € par écolier pour les communes ;
- soit le concept DEPP, **avec quote-part d'administration générale** : ≈ 21,8-22,3 Md€, soit ≈ 3 500-3 580 € par écolier.
- La circulaire 2012-025 inclut cette quote-part dans le coût d'un élève du public.
