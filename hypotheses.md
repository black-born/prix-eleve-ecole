# Hypothèses du calcul du coût moyen d'un élève pour la puissance publique

Ce document recense **toutes les hypothèses introduites** dans le calcul, avec leur justification et, quand c'est possible, leur effet chiffré. Il accompagne le rapport ([rapport.md](rapport.md)) ; les sources sont détaillées dans [sources.md](sources.md). Les numéros H-… sont repris dans les commentaires des scripts ([scripts/](scripts/)).

La section 0 rappelle d'abord les **conventions des sources officielles**. Ce ne sont pas nos hypothèses, mais il faut les connaître pour lire les chiffres.

- [0. Conventions des sources officielles (rappel)](#0-conventions-des-sources-officielles-rappel)
- [G. Cadrage général](#g-cadrage-général)
- [E. Effectifs d'élèves](#e-effectifs-délèves)
- [A. Approche A : compte de l'éducation (DEPP)](#a-approche-a--compte-de-léducation-depp)
- [B. Approche B : établissement par établissement](#b-approche-b--établissement-par-établissement)
- [C. Recoupements et sensibilités](#c-recoupements-et-sensibilités)
- [D. Décomposition par poste de dépense](#d-décomposition-par-poste-de-dépense)
- [Anomalies relevées dans les sources](#anomalies-relevées-dans-les-sources)
- [Récapitulatif des effets chiffrés](#récapitulatif-des-effets-chiffrés)

---

## 0. Conventions des sources officielles (rappel)

**Compte de l'éducation (DEPP)**, source de l'approche A : DEPP, *Note d'Information* n° 26.42, septembre 2026, page https://www.education.gouv.fr/depp/en-2025-1992-milliards-d-euros-consacres-l-education-soit-67-du-pib-506005. Le DOI 10.48464/ni-26-42 est affiché, mais pas encore actif. La méthode est décrite dans le Dossier DEPP n° 206.

- **Dépense intérieure d'éducation (DIE)**. C'est tout ce que dépensent pour l'éducation en France l'État, les collectivités, les autres administrations publiques, les entreprises et les ménages. Elle couvre l'enseignement, la restauration et l'hébergement, les transports scolaires, la médecine scolaire, l'orientation, l'administration, ainsi que les fournitures et livres demandés aux familles. Le fonctionnement et l'investissement de l'année sont comptés.
- **Dépense moyenne par élève de l'année civile N**. C'est la DIE du niveau divisée par l'effectif de l'année civile, égal à 2/3 de la rentrée N-1 + 1/3 de la rentrée N.
- **Champ « France »**. Métropole + DROM, Mayotte comprise ; les collectivités d'outre-mer (COM) sont exclues. Le compte couvre le public et le privé (sous contrat et hors contrat), l'enseignement agricole et les autres ministères.
- **Le 2nd degré** comprend les apprentis en CFA de niveau secondaire et l'enseignement spécial (EREA, Segpa, établissements de santé). Les STS et les CPGE des lycées sont classées dans le supérieur.
- **Apprentissage.** Le financement de l'apprentissage via les OPCO est compté comme dépense des « entreprises » : la note 2 de la figure 4 de la NI 26.42 (p. 2) précise « dont financement de l'apprentissage via les OPCO », et le texte (p. 3) indique que les OPCO sont « assimilés à des acteurs privés dans le compte de l'éducation ». L'Insee classe pourtant ces organismes parmi les administrations publiques.
- **Pensions.** Les dépenses de personnel de l'État comprennent les contributions employeur au CAS Pensions, c'est-à-dire le taux d'équilibre du régime des fonctionnaires.
- **Financement initial / final.** En financement initial, chaque dépense est attribuée au premier payeur, avant transferts : les bourses vont à l'État, l'allocation de rentrée scolaire aux CAF. En financement final, elle est attribuée après transferts, à celui qui dépense effectivement : bourses et allocation de rentrée vont alors aux ménages.
- **Statut des données.** 2025 est **provisoire** ; 2024 est définitif depuis septembre 2026.

**Budget de l'État (RAP 2025).** Ce sont les crédits de paiement exécutés en 2025, par programme et par action. La mission « Enseignement scolaire » couvre la France et les COM. Le titre 2 (dépenses de personnel) comprend les contributions au CAS Pensions. Selon la Cour des comptes, « l'imputation budgétaire repose ainsi sur le statut et l'affectation principale des agents, et non sur la réalité de leur service effectif » (NEB 2025, p. 22).

**Comptes des collectivités (DGFiP, balances 2025).** Ce sont les opérations réelles des budgets principaux, en présentation par fonction (nomenclature M57). Seules les communes de 3 500 habitants ou plus sont tenues de présenter leurs comptes par fonction.

**Comptabilité nationale (INSEE, COFOG).** Ce sont les dépenses consolidées des administrations publiques par fonction : les flux entre administrations ne sont comptés qu'une fois.

**Collecte internationale UOE (Eurostat, OCDE).** Elle repose sur les données transmises par la DEPP. Les élèves y sont comptés en équivalent temps plein, les années sont alignées sur l'exercice financier et les apprentis comptent pour moitié.

---

## G. Cadrage général

**H-G1. Territoire : la France au sens de la DEPP.** On retient la métropole et les DROM, Mayotte comprise. Les COM présentes dans certaines données sont exclues : Nouvelle-Calédonie, Polynésie française, Wallis-et-Futuna, Saint-Pierre-et-Miquelon. Saint-Martin et Saint-Barthélemy, rattachés à l'académie de Guadeloupe, restent inclus, comme dans les totaux de la DEPP.
*Effet* : environ 120 000 élèves et 1,13 Md€ de crédits de l'État retirés des enveloppes de B (1,16 Md€ pour toute la mission, programme 143 compris) (H-E3, H-B2).

**H-G2. Champ des élèves, selon l'approche.** Dans tous les cas, « élève » désigne l'enseignement scolaire : 1er degré (maternelle, élémentaire, ULIS) et 2nd degré (collège, y compris Segpa et ULIS, lycée général et technologique, lycée professionnel, EREA). Les étudiants de STS et de CPGE sont exclus, même au lycée, ainsi que la formation continue. Le champ précis dépend de l'approche :

| Approche | Champ | Effectif 2025 |
|---|---|---|
| **A** (référence DEPP) | public, privé sous contrat et hors contrat, Éducation nationale et enseignement agricole, établissements de santé, apprentis du secondaire | 12,62 millions (année civile 2025) |
| **A'** (hors apprentis) | même champ, sans les apprentis | 12,22 millions |
| **B** (par établissement) | écoles et établissements de l'Éducation nationale, publics et privés sous contrat | 11,90 millions (rentrée 2024) |

**H-G3. « Coût pour la puissance publique » = agrégat des administrations publiques.** On additionne l'État (tous ministères), les collectivités territoriales et les autres administrations publiques (surtout les CAF). Les ménages et les entreprises sont exclus. C'est la demande explicite de l'étudiant : « le budget du public, un agrégat », et non l'État seul.
- Dans la DEPP, la ligne « État » comprend le « reste du monde », c'est-à-dire surtout les fonds européens : 428,9 M€ tous niveaux en 2024, en financement final (RERS 2026, fiche 10.02, tableau 4, note 2). Nous la gardons telle quelle : effet inférieur à 0,3 %.
- Apprentissage : on suit la convention DEPP (financements des OPCO = entreprises). Variante en H-A8.
- La rémunération des apprentis et les aides à l'embauche sont hors champ.

**H-G4. Année de référence : 2025, en euros courants.** Les données 2025 du compte de l'éducation sont **provisoires** (publiées le 29/09/2026). L'année 2024 et les données 2023 (UOE, OCDE) servent de comparaison.
*Ordre de grandeur des révisions* : la DEPP a révisé 2024 de −0,3 Md€ sur 197 Md€ pour la dépense intérieure d'éducation totale, dont +0,14 Md€ (+0,1 %) pour l'enseignement scolaire du 1er et du 2nd degré (NI 26.42, figure 1bis).

**H-G5. « Coût » = dépense de l'année, sans amortissement.** Les investissements (constructions, rénovations) sont comptés l'année où ils sont payés. C'est la convention de la DEPP et des budgets publics. Le poste « bâtiments » varie donc d'une année à l'autre.

**H-G6. Retraites des fonctionnaires : on retient le taux de cotisation de l'État (CAS Pensions).** Pour les fonctionnaires civils, il vaut 78,28 % du traitement indiciaire en 2025, plus 0,32 % au titre de l'allocation temporaire d'invalidité (ATI), soit 78,6 % ; il était de 74,28 % (74,6 % avec l'ATI) jusqu'en 2024 et passe à 82,28 % en 2026. C'est un taux « d'équilibre », fixé pour équilibrer chaque année le CAS : il finance les pensions actuellement versées, alors que le régime compte de plus en plus de retraités par fonctionnaire actif. Selon un *Focus* du CAE (H. Paris, 2025, publié sous la seule responsabilité de son autrice), il mêle une cotisation d'employeur, le financement de dispositifs de solidarité et une subvention d'équilibre (*Focus* n° 121, p. 1).
- **Effet sur l'évolution 2024-2025.** Selon la Cour des comptes, la hausse 2025 des crédits de la mission « Enseignement scolaire » est « essentiellement portée par le CAS Pensions (+ 1,39 Md€) » (NEB 2025, p. 6 ; tableau n° 18, p. 37). Cette hausse « s'explique notamment par le relèvement de 4 points du taux de contribution » (p. 54). Le titre 2 hors CAS n'augmente que de 0,3 % à périmètre constant, c'est-à-dire hors transfert des AESH et des AED sur le titre 2 (+1,1 % à périmètre courant).
  - Rapportée aux 12,62 M d'élèves de A, la hausse du CAS représente environ 110 € par élève, soit environ la moitié de la hausse de la dépense publique par élève (+217 €).
  - L'effet du seul relèvement du taux est d'environ 94 € par élève : contributions 2024 des programmes du ministère (22,03 Md€) × 4 / 74,6, soit 1,18 Md€ (couts_personnels/TRANSCRIPTION_titre2_par_programme_CAS_Pensions.csv).
  - Ces montants portent sur toute la mission, y compris des crédits hors du champ de A (post-bac, COM) : ce sont des ordres de grandeur. C'est une hausse comptable, pas une hausse des moyens.
- **Sensibilité (H-C3)** avec un taux de cotisation corrigé, plus proche de l'« effort contributif » de l'État employeur (notion reprise de ce *Focus*), pour le champ de A :
  - 34,7 % (taux d'équilibre corrigé de l'Institut des politiques publiques, 2020 ; « borne haute » selon le *Focus* du CAE) : environ **−990 € par élève** ;
  - 25,44 % (borne basse proposée dans ce *Focus*) : environ **−1 200 € par élève**.

**H-G7. Moyenne pondérée.** Le coût moyen d'un élève est le total des dépenses divisé par le total des élèves. Ce n'est **pas** la moyenne des coûts par élève de chaque établissement, qui donnerait trop de poids aux petits établissements. Dans les distributions par établissement (déciles), chaque élève porte la dépense de son établissement.

**H-G8. Dépenses fiscales non comptées.** Les réductions d'impôt ne sont pas des dépenses publiques en comptabilité nationale. La réduction d'impôt pour frais de scolarité des enfants au collège et au lycée représente 229 M€ en 2025, soit environ 18 € par élève (PLRG 2025, ligne 110215).

---

## E. Effectifs d'élèves

**H-E1. Effectifs de l'année civile.** Pour 2025, la DEPP pondère 2/3 de la rentrée 2024 + 1/3 de la rentrée 2025, et l'approche A suit cette convention. L'approche B rapporte les budgets 2025 aux élèves de la **rentrée 2024**, dernière année où les personnels du 2nd degré sont publiés par établissement.
*Effet* : les effectifs baissent d'environ 1 % par an ; l'effectif de l'année civile 2025 (11 856 946) est inférieur de 0,34 % à celui de la rentrée 2024 (11 897 471). B sous-estime donc la dépense par élève d'environ **0,3 %** (environ 35 €). L'effet n'est pas le même partout : là où les effectifs augmentent, B surestime au contraire la dépense par élève (Seine-Saint-Denis : environ +0,2 % au collège et +0,9 % au lycée ; Paris : environ −0,8 % au collège ; analyse, § 3.6).

**H-E2. Dénominateur de l'approche A.** On utilise les effectifs implicites de la DEPP, égaux à la DIE divisée par la dépense moyenne publiée : 6,36 M au 1er degré et 6,26 M au 2nd degré, soit 12,62 M en 2025.
- Ils dépassent de 0,76 M les effectifs de l'Éducation nationale (11,86 M). L'écart s'explique pour 0,68 M par le privé hors contrat (environ 85 000 élèves, très peu financés sur fonds publics), l'enseignement agricole (environ 140 000), les établissements de santé (environ 67 000) et les apprentis du secondaire (environ 392 000), en année civile 2025 (data/raw/effectifs_nationaux/NOTES.md). Un résidu d'environ 77 000 élèves (0,6 % du dénominateur de A) n'est pas expliqué : la DEPP ne publie pas le détail de ses effectifs.
- La dépense moyenne publiée étant arrondie à 10 €, l'erreur sur ces effectifs est inférieure à 0,05 %.

**H-E3. Données par établissement hors COM.** Les fichiers de data.education.gouv.fr comprennent les COM. Une fois celles-ci retirées, la somme des élèves des établissements retrouve le total national DEPP à 0,1 % près au plus pour chaque type d'établissement et chaque secteur (tableau E2 ; écart maximal : +0,104 % pour les lycées généraux et technologiques publics à la rentrée 2024).

**H-E4. Code commune.** Dans le jeu « Effectifs d'élèves par école », la colonne « code_commune_insee » contient en réalité le **code postal** ; dans le jeu « Effectifs d'élèves en lycée professionnel », la colonne « code_commune » aussi. Le vrai code Insee est repris de l'annuaire de l'éducation (par UAI) ; à défaut, du fichier IPS pour les écoles, des fichiers des collèges et des lycées généraux et technologiques pour le second degré (jamais du fichier des lycées professionnels). Tous les collèges et lycées ayant des élèves ont ainsi un code ; il ne sert à aucun montant du second degré. Pour 566 écoles ayant des élèves (37 568 élèves, souvent fermées depuis), dont 562 publiques (37 288 élèves), aucun de ces fichiers ne donne le code : il est retrouvé par le nom de la commune dans le département, dans les listes de l'API Découpage administratif (H-B18) : commune actuelle de même nom (560), commune déléguée ou associée, rattachée à sa commune actuelle (4), chef-lieu d'une commune nouvelle dont les communes déléguées forment l'ancien nom (1), seule commune actuelle dont le nom contient l'ancien (1). Toutes les écoles ont ainsi un code : les écoles publiques reçoivent la clé de leur commune (H-B9) ; la clé ne s'applique pas au privé.

**H-E5. Privé sous contrat du 1er degré.** Comme dans les notes DEPP, il inclut quelques classes hors contrat des écoles sous contrat. Effet inférieur à 0,1 % sur les moyennes. Il est plus net pour les écoles concernées : selon l'annuaire de l'éducation (colonne `type_contrat_prive`, situation de 2026), 137 écoles privées de la base (30 262 élèves) ne sont sous contrat que pour une partie de leurs classes (131), ou ne le sont plus (6 écoles « hors contrat », 627 élèves) ; leurs élèves hors contrat font baisser leur dépense publique par élève. La carte en signale 136 pour ce motif et ne les compare pas aux autres écoles privées ; la 137e (0331957Y, 19 élèves) n'est pas comparée non plus, faute d'enseignant publié (H-B12, H-B18). Pour les collèges et lycées privés dans ce cas, rien n'indique que leurs effectifs comprennent des élèves hors contrat (leurs heures H/E couvrent tous leurs élèves) : ils ne sont pas signalés.

---

## A. Approche A : compte de l'éducation (DEPP)

**H-A1. Dépense publique par élève = dépense moyenne × part publique.** Pour chaque degré, on multiplie la dépense moyenne par élève (tous financeurs, NI 26.42) par la part des financeurs publics (État + collectivités + autres administrations publiques) en **financement initial**, publiée par degré (figure 4).
- Hypothèse : la part publique est la même pour tous les élèves d'un degré.
- La DEPP publie les deux termes, mais **pas leur produit** : 9 710 € est un calcul de l'auteur à partir des chiffres officiels.

**H-A2. Financement initial plutôt que final.** En financement initial, les bourses (État) et l'allocation de rentrée scolaire (CAF) comptent comme dépense publique : c'est de l'argent public consacré aux élèves.
*Variante* : en financement final (données 2024 provisoires des séries DEPP), on obtient **9 231 €** au lieu de 9 493 € (−2,8 %).

**H-A3. Variante « hors apprentis » (élèves sous statut scolaire).** Trois paramètres :
- **Dépense d'apprentissage du 2nd degré.** En 2024p, elle représente 1,9 % de la DIE totale (séries DEPP 366606, cellule U19, part arrondie à 0,1 point ; DIE 2024p : série 508145, cellule AU10), soit 3,74 Md€. On la porte en 2025 au rythme de la DIE du 2nd degré, ce qui donne 3,78 Md€.
- **Apprentis de niveaux 3 et 4** (enquête SIFA, DEPP, NI 26.35, figure 2) : 392 035 au 31/12/2024 et 391 937 au 31/12/2025, pondérés 2/3-1/3, soit 392 000.
- **Part publique de l'apprentissage du 2nd degré : *s* = 17,5 %.** Aucune source ne la publie. C'est une estimation centrale fondée sur France compétences, la Dares et la DEPP (data/raw/depp_compte_education/NOTES.md, § 12), avec une fourchette de 13,5 à 23 %.

*Résultat* : **9 968 €** (fourchette 9 951 à 9 980 €) ; 11 057 € dans le 2nd degré. Le paramètre *s* change le résultat de moins de 20 €.

**H-A4. Les « autres administrations publiques » sont incluses.** Elles représentent 2,32 Md€ en 2025, dont l'allocation de rentrée scolaire (ARS) des CAF (2 207,8 M€ en 2025 ; RERS 2026, fiche 10.06, p. 419), qui est un transfert aux familles et non une dépense des établissements.
*Variante sans les autres administrations publiques* : **9 526 €** (−184 €).

**H-A5. Sous-niveaux.** La DEPP ne publie la part publique que par degré.
- Maternelle et élémentaire : on applique la part du 1er degré (94,93 %).
- Collège, lycée général et technologique, lycée professionnel : ce sont des formations sous statut scolaire. On applique donc la part publique du 2nd degré **hors apprentissage** (92,73 % en 2025, mêmes paramètres que H-A3).

En réalité, les familles et les entreprises paient un peu plus en lycée qu'au collège. Ces valeurs couvrent aussi le privé hors contrat et l'agricole : elles ne sont pas comparables aux valeurs par type d'établissement de l'approche B.

**H-A6. Décomposition par nature (tableau A7).** On applique à la dépense publique 2025 la structure 2023 des dépenses des établissements de la collecte UOE (Eurostat, fichier fini01) : enseignants, autres personnels, autres dépenses courantes, investissement.
- Secteur TOT_SEC (public et privé) ; 1er degré = CITE 02 + 1 ; 2nd degré = CITE 2 + 3 (CITE 4 exclue). Les « services annexes » sont un « dont », non additif.
- Hypothèses : la structure de la dépense publique est celle de la dépense totale, et elle n'a pas changé entre 2023 et 2025.

**H-A7. Lecture des cellules.** La moyenne par degré 2025 est lue dans la figure 7 de la NI 26.42 : la figure 6 porte un libellé erroné (voir les anomalies). La moyenne « 1er + 2nd degrés » 2025 n'est pas publiée. Notre méthode de calcul redonne la valeur publiée pour 2024 : 10 352 € calculés pour 10 350 € publiés (dépense totale, tous financeurs).

**H-A8. Convention de l'apprentissage (OPCO).** Si l'on comptait comme publique toute la part « entreprises » du 2nd degré, qui contient surtout le financement de l'apprentissage via les OPCO, la référence apprentis compris passerait de 9 710 à **9 981 €** (1er degré inchangé). C'est une borne haute, car cette part contient aussi d'autres financements d'entreprises. La variante hors apprentis (9 968 €) ne dépend pas de cette convention.

---

## B. Approche B : établissement par établissement

L'idée est de rattacher chaque euro public à un établissement, puis de diviser par ses élèves. Aucune source ne publie les dépenses par établissement : on part des budgets officiels de 2025 et on les **répartit** avec les clés les plus fines disponibles en open data. Toutes les clés sont listées dans `resultats/B0_enveloppes_reparties.csv`, les indicateurs de méthode dans `B4_indicateurs_methode.csv`.

Au total, 53,8 % de la dépense de B est répartie avec des données propres à chaque établissement : ETP et heures d'enseignement, ETP de vie scolaire et d'autres personnels. Les enveloppes de ces postes réparties par élève (P140 a06 et P139 a07, 1,9 Md€) ne sont pas comptées dans ce pourcentage. 22,1 % de B reprend directement des montants du compte de l'éducation (collectivités pour les écoles, fournitures scolaires des écoles comprises, transports, autres administrations publiques).

**H-B1. Calendrier.** Les établissements, leurs élèves et leurs personnels sont ceux de la rentrée 2024 (année scolaire 2024-2025). Les budgets sont ceux de 2025 : RAP 2025 pour l'État, balances DGFiP 2025 pour les départements et les régions.

**H-B2. Retrait de l'outre-mer hors champ (COM).** Les crédits de la mission dépensés dans les COM sont de 1 160,6 M€ en exécution 2024, dont 22,1 M€ au programme 143 (DPT Outre-mer 2026 ; 2025 non publié). Pour chaque programme, on applique à chaque action retenue le rapport entre ses dépenses dans les COM en 2024 et ses crédits exécutés en 2025. Au total, 1 129,6 M€ sont retirés des enveloppes de B (P140 : 191,3 ; P141 : 545,9 ; P139 : 240,8 ; P230 : 105,1 ; P214 : 46,6 ; valeurs arrondies).

**H-B3. Crédits exclus.**
- *Comme dans la DEPP* (hors du 1er et du 2nd degré, ou hors de la dépense d'éducation) :
  - programme 141, action 09 (formation continue des adultes) ;
  - programme 214, action 11 (sport, jeunesse, vie associative), que la DEPP classe vraisemblablement dans l'extrascolaire ou hors de la dépense d'éducation ;
  - allocations de stage des lycéens professionnels (PFMP : 208,0 M€ au P141, 54,8 M€ au P139).
- *Propres au champ de B* (la DEPP les compte dans le 2nd degré, donc dans A) :
  - programme 141, action 04 (apprentissage), car B ne compte pas les apprentis ;
  - programme 143 (enseignement agricole), dont les élèves ne sont pas dans les fichiers de l'Éducation nationale.

Le post-bac est retiré par les heures (H-B4). Les dépenses d'autres ministères (lycées de la défense, etc.) ne sont pas dans B.

**H-B4. Crédits d'enseignement de l'État.**
- **1er degré.** Actions 01-03 du P140 (public, RASED compris) et 01-02 du P139 (privé), au prorata des ETP d'enseignants de l'école. *Contrôle* : les actions 01-03 du P140 correspondent à 275 006 ETPT, pour 278 953 ETP dans les écoles publiques ayant des élèves. Le coût par ETP est le même partout : ni l'âge, ni l'ancienneté, ni le statut (contractuels), ni les primes (REP, REP+, prime de fidélisation territoriale de la Seine-Saint-Denis), ni l'indemnité de résidence, ni les majorations de traitement outre-mer ne sont pris en compte. La ligne « enseignants » d'une école est donc proportionnelle à ses ETP (effets estimés pour Paris et la Seine-Saint-Denis : H-B21 ; outre-mer : H-B19).
- **2nd degré : actions mutualisées.** Les actions 01 (collège), 02 (lycée GT), 03 (lycée professionnel), 05 (post-bac) et 06 (besoins éducatifs particuliers) du P141, ainsi que les actions 03 à 06 du P139, sont **mutualisées**. Elles sont réparties au prorata des heures hebdomadaires d'enseignement **de tous niveaux** de l'établissement (indicateur H/E), pondérées par l'indice de coût des corps (H-B5), sur l'ensemble des établissements du secteur, y compris les établissements post-bac seuls.
- **2nd degré : retrait du post-bac.** On garde les heures du secondaire : Collège ; Lycée général et technologique ; Prépa seconde ; Lycée professionnel ; Segpa ; EREA. La part des heures de STS et de CPGE sort du champ : 2 370,2 M€ au total, public et privé.
- **Pourquoi mutualiser.** L'imputation des crédits par action suit l'affectation principale des agents. La Cour des comptes la juge peu fiable par niveau : en 2025, la masse salariale de l'action « lycée GT » est exécutée à 119,4 % de la loi de finances, celle de l'action « post-bac » à 55,7 % (NEB 2025, p. 22, tableau). Les heures, elles, mesurent le service réellement fait.
- **Conséquence.** En lycée professionnel, les enseignants assurent 2,14 heures d'enseignement hebdomadaires par élève (indicateur H/E : heures-professeur rapportées aux élèves), contre 1,26 en voie générale et technologique (public, rentrée 2024, total des heures / total des élèves). Ce n'est pas le nombre d'heures de cours suivies par un élève : l'écart vient surtout des ateliers en petits groupes. B attribue donc au lycée professionnel un coût plus élevé que les moyennes par niveau de la DEPP.
- **Dispositifs spécifiques du privé.** L'action 07 du P139 (ULIS, Segpa, UPE2A… des deux degrés) est répartie par élève entre tous les élèves du privé.
- **Enseignants non rattachés à un établissement.** Ils sont financés en partie par des actions réparties par élève (remplacement, formation). On compte environ 92 000 ETP de différence avec le total des enseignants recensés par la DEPP (Panorama, 30/11/2024), et environ 56 800 avec les seuls ETP consacrés à l'enseignement (RERS 2025, fiche 9.01, surtout le remplacement).

**H-B5. Indice de coût relatif des corps (2nd degré).** On utilise le salaire net moyen 2024 de chaque corps, rapporté à celui de l'ensemble des fonctionnaires du 2nd degré (3 310 € ; DEPP, NI 26.36, figures 1 et 6) :

| Corps | Indice |
|---|---|
| Agrégés (y compris chaires supérieures, 4 080 €) | 1,233 |
| Certifiés et PEPS (moyenne pondérée par les effectifs) | 0,947 |
| PLP | 1,024 |
| Autres titulaires (valorisés comme des professeurs des écoles) | 0,861 |
| Contractuels | 0,681 |

Pour les contractuels, l'indice est leur salaire en équivalent temps plein rapporté à celui des fonctionnaires du 2nd degré public (2 350 € / 3 450 € ; Panorama 2025-2026, tableau 7.3).

*Hypothèses et limites* :
- le coût employeur est supposé proportionnel au salaire net, ce qui ignore la cotisation retraite plus faible des contractuels : dans la convention du CAS Pensions (H-G6), un contractuel coûte plutôt 0,5 à 0,6 fois un titulaire, et l'indice de 0,681 surévalue les établissements qui en emploient beaucoup ;
- les salaires des titulaires sont des moyennes par personne, temps partiel compris ;
- l'indice est calculé sur tous les enseignants de l'établissement, y compris ceux de CPGE, ce qui relève un peu le coût des heures du secondaire dans les lycées à CPGE ;
- **aucun ajustement selon l'ancienneté** n'est fait (les enseignants sont plus jeunes, donc moins payés, en REP et REP+ : écarts surestimés de ce côté ; titulaires des collèges publics : environ −6 à −11 % du coût d'un ETP en Seine-Saint-Denis, +1,5 à +2,5 % à Paris ; lycées : −7,6 % et +3 %, H-B21) ;
- **ni les primes de l'éducation prioritaire, ni la pondération de 1,1 des heures en REP+** ne sont imputées aux établissements concernés (écarts sous-estimés de ce côté), **ni la prime de fidélisation territoriale de la Seine-Saint-Denis** (environ 117 M€ en 2025 pour les programmes de l'Éducation nationale, RAP 2025), **ni l'indemnité de résidence** (H-B21).

**H-B6. Établissements sans heures H/E** (15 établissements ayant des élèves, 1 359 élèves). Pour chaque niveau (collège, voie générale et technologique, voie professionnelle), on leur attribue le nombre d'élèves × le H/E moyen du niveau et du secteur (rentrée 2024, total des heures / total des élèves).
- *Heures publiées pour une partie des élèves seulement* : dans 26 autres établissements, moins de 90 % des élèves figurent dans le fichier H/E, en général parce qu'un niveau y est masqué (« ns », effectif faible). Les heures des 1 114 élèves manquants sont estimées avec le H/E moyen des établissements du même type et du même secteur dont la couverture est complète, soit 1 661 heures hebdomadaires en tout.

**H-B7. Crédits répartis par élève** dans la population concernée.

| Crédits | Population |
|---|---|
| P140 a04, a05, a07 (formation, remplacement, situations diverses) | écoles publiques |
| P140 a06 (inspection, conseillers pédagogiques) | écoles publiques |
| P141 a07-08 (insertion, orientation) ; a10, a11, a13 (formation, remplacement, situations diverses) | collèges et lycées publics |
| P230 a02 (santé scolaire) | élèves du public |
| P230 a03, a07 (AESH, scolarisation à 3 ans) ; a06 (actions éducatives) ; P214 a01-10 (soutien) | tous les élèves |
| P230 a04, titre 2 (assistants de service social) | élèves du 2nd degré public |
| P230 a04, hors titre 2 (bourses, primes, fonds sociaux de l'**enseignement public**) | élèves du 2nd degré public |
| P230 a05 (internats, établissements à la charge de l'État) | élèves du 2nd degré public |
| P139 a07 (dispositifs spécifiques) | tous les élèves du privé |
| P139 a08 (actions sociales du privé : bourses, fonds sociaux) ; a09 (forfait d'externat, part État) | collèges et lycées privés |
| P139 a10-12 (formation, remplacement, soutien du privé) | tous les élèves du privé |
| Collectivités → écoles privées sous contrat (forfait communal) | élèves des écoles privées |

Deux enveloppes sont réparties selon des données par établissement, pour les seuls collèges et lycées publics :
- vie scolaire (P230 a01) : ETP de vie scolaire ;
- direction et administration (P141 a12) : ETP « autres personnels », c'est-à-dire ETP total − ETP d'enseignants − ETP de vie scolaire de l'établissement, avec un plancher à 0 (script 03).

Ces personnels servent aussi les étudiants de STS et de CPGE des lycées. Pour ces deux enveloppes, on ne retient donc que la part des élèves du secondaire : ETP × élèves / (élèves + étudiants). La part des étudiants, et celle des établissements post-bac seuls, sort du champ (356,8 M€), comme pour les heures d'enseignement (H-B4).

*Limite* : en réalité, les AESH et les bourses se concentrent sur certains élèves et certains établissements. Sensibilités selon les besoins (allocation de rentrée selon les montants des CAF par département, bourses selon le taux de boursiers, AESH selon l'académie, remplaçants selon leur part) : H-B21.

**H-B8. Collectivités → écoles, fournitures scolaires et transports : montants du compte de l'éducation.** On prend le financement des écoles publiques (20 608 M€) et privées (1 142 M€) par les collectivités, et celui des transports scolaires (2 485 M€). Ce sont des montants 2024p en **financement final** (RERS 2026, fiche 10.04, tableau 2, cellules E9 et E19 ; fiche 10.02, tableau 4, cellule F17). On les porte en 2025 avec l'évolution du financement initial des collectivités, 1er et 2nd degrés réunis : +1,02 % entre la NI 25.52 et la NI 26.42.
- *Fournitures et livres scolaires.* La fiche 10.04 finance les producteurs : elle exclut les fournitures et livres scolaires payés par les collectivités (185,8 M€ en 2024p ; fiche 10.02, tableau 4, cellule F18), que la DEPP compte dans la DIE, donc dans A. On les ajoute, portés en 2025 de la même façon, pour la part des écoles dans les achats de fournitures scolaires des collectivités (compte 6067, DGFiP 2025 : 91,1 %). Cela fait 171,0 M€, répartis entre écoles publiques avec la clé communale (H-B9). Le reste (départements, régions) figure déjà dans les comptes des collèges et lycées (H-B10). La part des écoles est calculée avec les seules communes qui présentent leurs comptes par fonction : c'est une borne basse. Avec l'extrapolation du tableau G3 (199,1 M€ pour les écoles), elle serait d'environ 93,5 %, soit environ 4 M€ de plus (moins de 1 € par écolier du public).
- *Variante* : avec l'évolution propre au 1er degré (+2,75 %) pour les écoles, B augmenterait d'environ 60 € par écolier.
- *Justification* : les comptes communaux par fonction ne couvrent que 70 % des écoliers du public. Une reconstitution par les comptes (18,6 Md€ nets des familles) s'écarte du compte DEPP surtout parce que la DEPP impute aux écoles une quote-part de l'administration générale des mairies (environ 3,15 Md€). Voir data/raw/collectivites/extractions/G3_tableau_passage_DGFiP_DEPP_2025.csv.

**H-B9. Répartition entre écoles publiques : clé communale.** Chaque école reçoit une part proportionnelle à ses élèves × la dépense de fonctionnement « écoles » par élève du public de sa commune en 2025 (balances DGFiP, fonctions 20, 21x, 28x et 29).
- **Couverture** : 3 337 communes publient des comptes par fonction et ont des écoles publiques (70,6 % des élèves du public). 3 163 sont retenues (67,8 % des élèves) : au moins 50 élèves du public et au moins 500 € par élève. En dessous, les écoles sont vraisemblablement gérées par un groupement (SIVOS, EPCI).
- **Écrêtage** aux 1er et 99e centiles pondérés par les élèves : 610 € et 7 041 €. Paris est la première commune au-dessus du plafond : clé brute 7 045,60 €, ramenée à 7 040,91 € (−0,07 %).
- Les communes sous les seuils et les petites communes sans comptes par fonction reçoivent la moyenne des communes retenues : 2 883 € par élève. Les écoles fermées depuis la rentrée 2024 reçoivent la clé de leur commune actuelle (H-E4).
- **Recalage** : la clé ne fixe que la part de chaque école ; les montants sont recalés sur le total à répartir (H-B8), qui comprend aussi l'investissement et une quote-part de l'administration générale des mairies. Une école à la moyenne reçoit ainsi 3 878 € par élève, environ 1,35 fois les 2 883 € de la clé. Les montants d'une fiche de la carte ne sont donc pas les dépenses inscrites dans les comptes de la commune.
- La dépense communale comprend aussi le forfait versé aux écoles privées et les frais de scolarité versés à d'autres communes (comptes 6558 et 65748), rapportés aux seuls élèves du public. La clé est donc un peu gonflée là où le privé est important.
- L'investissement n'entre pas dans la clé, car il varie trop d'une année à l'autre.
- Hypothèse : tous les élèves d'une commune « coûtent » autant à la commune. On compare des communes, pas des écoles.
- *Investissement* : le montant DEPP réparti comprend l'investissement, mais la clé ne compte que le fonctionnement ; l'investissement est donc réparti comme le fonctionnement. En 2025, les communes du 93 investissent 1 357 € par écolier du public dans leurs écoles, Paris 610 €, l'ensemble des communes à comptes fonctionnels environ 920 € (H-B21). En moyenne 2023-2025 : 1 223 € dans le 93, 624 € à Paris, 837 € pour les communes à comptes fonctionnels (H-B22).
- *Périmètre des fonctions et des recettes* : Paris range dans la fonction 2, d'après la chambre régionale des comptes, une partie du périscolaire et de l'extrascolaire ; les communes du 93 rangent ces activités en fonction 33 « jeunesse et loisirs » (environ 273 M€ en 2025, contre 21 M€ pour Paris). Toutes les communes y inscrivent aussi les forfaits versés aux écoles privées (comptes 6558 et 65748). En sens inverse, la clé compte la dépense avant les recettes des familles (cantine), que les communes du 93 encaissent (10,8 % de la clé) mais pas la Ville de Paris (1,5 %), dont les caisses des écoles les reçoivent. Paris exerce aussi les compétences d'un département (loi n° 2017-257) : ses « services communs » (fonction 201, 78 M€) peuvent servir les collèges (H-B21).
- *Personnel non ventilé* : certaines communes n'imputent pas leur personnel à la fonction 2 (Stains et Les Lilas : 0 € ; 509 communes, 7,8 % des élèves du public, en imputent moins de 5 % ; 820 communes, 13,4 %, moins de 10 %). Leurs écoles reçoivent une clé trop basse.
- *Communes nouvelles* : Saint-Denis et Pierrefitte-sur-Seine forment la commune nouvelle 93066 (COG 2026 : 93059 commune déléguée) ; la clé compte 39 communes en Seine-Saint-Denis ; seule Stains est relevée au plancher (566 € → 610 €).

**H-B10. Collèges et lycées : comptes 2025 des départements et des régions.**
- **Collèges** (6 631 M€ : départements, CTU, Paris, Métropole de Lyon). Les dotations versées aux collèges privés (432 M€) sont réparties par collégien du privé, sans clé territoriale ; le reste va aux collèges publics.
- **Lycées** (7 338 M€, régions). La sous-fonction « 223 Lycées privés » (578,6 M€) va aux lycées privés, répartie par lycéen du privé, sans clé territoriale ; le reste va aux lycées publics.
- **Répartition territoriale** entre établissements publics : élèves × dépense par collégien du département ou par lycéen de la région (DEPP, *Géographie de l'École* 2026, moyenne 2021-2023, public + privé). On suppose les écarts entre territoires stables. Absents de ces fiches, les collèges de Mayotte, de Saint-Martin et de Saint-Barthélemy prennent la moyenne nationale (2 010 € par collégien), et les lycées de Mayotte la moyenne nationale par lycéen (3 000 €). Ceux de Saint-Martin et de Saint-Barthélemy prennent la valeur de la région académique de Guadeloupe. Le script vérifie qu'aucun autre territoire de la base ne manque dans ces fiches.
- *Limite* : la clé est une dépense par collégien (ou par lycéen) du public et du privé ; appliquée aux seuls établissements publics, elle sous-estime les départements où le privé pèse lourd, dont le financement passe surtout par un forfait. Paris (37 % de collégiens dans le privé) : environ +250 € par collégien du public ; Seine-Saint-Denis (13 %) : environ −154 € (H-B21).

**H-B11. Les dépenses « lycées » des régions servent aussi le post-bac et l'enseignement agricole.** On ne garde que la part des lycéens de l'Éducation nationale : lycéens / (lycéens + étudiants de STS et CPGE d'après l'indicateur H/E + élèves agricoles du secondaire de la rentrée 2024). Les étudiants post-bac sont comptés dans tous les établissements du secteur, y compris les établissements post-bac seuls (H-B12). Les élèves agricoles sont 49 990 dans le public et 90 008 dans le privé (DGER, « Effectifs de l'enseignement agricole 2024-2025 », onglet « 3- Voie sco par filières »). Ce fichier comprend la Nouvelle-Calédonie, la Polynésie française et Wallis-et-Futuna (environ 1 300 élèves, dont environ 1 260 du secondaire) : effet négligeable, moins de 0,1 point sur la part retenue. On obtient 86,5 % dans le public et 75,7 % dans le privé.
*Hypothèse* : une région dépense autant par élève, quel que soit le type d'élève.

**H-B12. Établissements sans élèves du secondaire.** Les établissements post-bac seuls et les écoles fermées ou fusionnées ne reçoivent aucune dépense. Les heures et les étudiants des établissements post-bac seuls restent toutefois dans les dénominateurs de la clé d'enseignement (H-B4) et de la part « champ » des régions (H-B11). Les établissements ayant des élèves mais aucun ETP enseignant exploitable reçoivent un indice de coût égal à 1. Les établissements dont aucun personnel n'est publié reçoivent 0 € des enveloppes réparties au prorata de ces personnels : 12 écoles sans ETP d'enseignant (338 élèves ; 0 € d'enseignants dans le public, seulement les crédits répartis par élève dans le privé) et 35 collèges et lycées publics sans personnel de vie scolaire ou sans personnel de direction : 13 n'ont ni l'un ni l'autre (2 139 élèves), 4 n'ont pas de vie scolaire (927 élèves) et 18 pas de direction (4 080 élèves). Ce sont souvent des annexes, des sections de lycées agricoles ou des micro-lycées dont les personnels sont rattachés à un autre UAI (data/raw/etablissements/NOTES.md, § 9). Les montants vont aux autres établissements ; la dépense de ces 47 établissements est sous-estimée, et la carte ne les compare pas à leur groupe (H-B18).

**H-B13. Autres administrations publiques.** On prend le montant DEPP 2025p de chaque degré (part « autres APU » × dépense moyenne × élèves) : 134 € par écolier en moyenne, 234 € par élève du 2nd degré. Au 2nd degré, il est réparti par élève. Au 1er degré, il est réparti sur les seuls élèves de 6 ans et plus (élémentaire, ULIS et UEEA : 3 995 051 élèves sur 6 261 750), soit 211 € chacun et rien en maternelle : l'essentiel du montant est l'allocation de rentrée scolaire (H-A4), versée pour les enfants de 6 à 18 ans (service-public.gouv.fr, fiche F1878). Pour les 326 écoles dont les effectifs par niveau ne sont pas publiés, on s'appuie sur leur type (H-B18) : aucun élève compté dans une maternelle, tous dans une élémentaire, et 63,7 % dans une primaire (part des élèves de 6 ans et plus dans les écoles primaires dont les niveaux sont publiés).

**H-B14. Transports scolaires répartis à parts égales entre tous les élèves.** En réalité, ils servent surtout les collégiens, les lycéens et les élèves ruraux. À Paris et en Seine-Saint-Denis, les comptes 2025 ne montrent presque pas de transports scolaires (fonction 81 : 0 € pour Paris, 1,07 M€ pour le département de la Seine-Saint-Denis) ; en Île-de-France, ce transport est organisé par Île-de-France Mobilités. B surestime vraisemblablement la dépense des deux, sans qu'on puisse le chiffrer (hypothèse).

**H-B15. Comparaisons sociales.** Les écarts sont mesurés à type d'établissement constant (écoles publiques, collèges publics, lycées publics). Les quintiles d'IPS sont des **quintiles d'établissements** (même nombre d'établissements par groupe, sans pondération par les élèves), calculés sur les IPS numériques de chaque groupe ; les IPS « NS » sont exclus.
- **Groupes** : les « lycées publics » réunissent les lycées généraux et technologiques, polyvalents et professionnels publics ; les EREA et la cité scolaire n'y sont pas. La variante « écoles publiques hors Paris » recalcule les quintiles sans les écoles de Paris.
- **Taille des collèges publics** : moins de 200 élèves, 200 à 399, 400 à 499, 500 à 599, 600 à 799, 800 et plus.
- **IPS des écoles** : il est calculé sur les élèves de CM2 et publié seulement pour les écoles ayant eu au moins 25 élèves de CM2 sur cinq ans (métadonnées DEPP). Les maternelles et les petites écoles sont exclues : l'analyse porte sur 25 762 écoles publiques sur 42 805, soit 3,97 M d'élèves sur 5,41 M.
- **Cités scolaires** : on retient l'IPS du collège.
- L'éducation prioritaire n'existe qu'à l'école et au collège.

**H-B16. Type d'établissement.** C'est la nature officielle du fichier des personnels du 2nd degré, avec des regroupements :
- collège spécialisé et collège climatique → collège ;
- lycées d'enseignement général, technologique et climatique → lycée général et technologique ;
- EREA et LEA ensemble ;
- école secondaire spécialisée → autre.

À défaut (11 établissements), le type est déduit des élèves. Tous les élèves d'un établissement sont comptés dans son type : beaucoup de lycées professionnels et polyvalents accueillent aussi des collégiens (3e prépa-métiers).

**H-B17. Rapprochement avec A.** B répartit 121,4 Md€, contre 121,9 Md€ pour A hors apprentis : les totaux sont presque égaux (−0,4 %). L'écart par élève (+2,4 %) vient surtout du dénominateur : 11,90 M d'élèves dans B, contre 12,22 M dans A hors apprentis (H-G2). Les deux totaux ne se correspondent pas ligne à ligne :
- Selon notre passerelle budgétaire (data/raw/budget_etat/NOTES.md, § 14, estimation calée sur 2024), la DEPP classe dans le supérieur ou l'extrascolaire environ 2,6 Md€ de crédits de l'Éducation nationale, en plus des actions explicitement post-bac (P141 a05 et P139 a06 : 1,62 Md€). Ces crédits comprendraient une part des actions transversales et des enseignants imputés aux actions « lycée » (inférence tirée de la ventilation 2013 du dossier 206 de la DEPP). B retire le post-bac par les heures (2,37 Md€, H-B4), soit environ 0,75 Md€ de plus que ces deux actions, et retire aussi la part post-bac de la vie scolaire et de la direction (0,36 Md€, H-B7). B garde donc environ 1,5 Md€ que la DEPP ne compte pas dans le 1er et le 2nd degré.
- A comprend l'enseignement agricole et les autres ministères.

**H-B18. Carte des établissements** (`resultats/carte_etablissements.html`, script 07 ; colonnes du CSV décrites dans `resultats/carte_etablissements_2025_colonnes.md`). Elle reprend les résultats de B pour les 58 068 établissements, publics et privés sous contrat (11 897 389 élèves) : 47 405 écoles et 10 663 collèges, lycées et EREA. L'enseignement supérieur n'y figure pas : B ne l'estime pas.
- *Types* : une école est « maternelle » si elle n'a que des élèves de préélémentaire, « élémentaire » si elle n'en a aucun, « primaire » si elle a les deux (élèves de la rentrée 2024). Pour les 326 écoles dont les effectifs par niveau ne sont pas publiés, le type vient de l'annuaire (classes maternelles, classes élémentaires : 308 écoles), sinon du nom (18). Collèges, lycées et EREA : type de H-B16 (les 4 lycées d'enseignement adapté, LEA, sont comptés avec les EREA). Les 3 autres établissements du second degré (une cité scolaire, deux écoles secondaires spécialisées) forment un type « autre » ; la pastille « EREA et autres » les affiche avec les EREA.
- *Département* : celui de B1, sauf pour les 17 écoles de Saint-Martin et de Saint-Barthélemy, codées 971 (Guadeloupe) dans le fichier des effectifs des écoles : leur département est tiré de leur code commune (978, 977), comme pour leurs collèges et lycées. Le filtre de région garde la région académique (Guadeloupe).
- *Position* : latitude et longitude de l'annuaire de l'éducation (instantané du 03/10/2026). Pour 1 926 établissements, l'annuaire ne donne que la commune, et pour 1 une position incertaine. Quand un UAI a plusieurs lignes (sites), on garde celle dont la commune est celle de la base (ou en contient le nom, ou l'inverse) et dont le nom n'indique ni une annexe ni un site post-bac ; à égalité, celle dont le type (école, collège, lycée, EREA) concorde, puis celle dont le nom a le plus de mots en commun avec celui de la base.
- *Établissements absents de l'annuaire actuel* (fermés ou fusionnés depuis la rentrée 2024 ; 892 établissements, 65 242 élèves) : ils sont placés à la mairie de leur commune (API Découpage administratif ; 883 établissements), ou à son centre (9) : commune déléguée, dont l'API ne donne pas la mairie (4), ou arrondissement de Marseille dont la mairie de secteur est partagée avec un autre arrondissement (5). La commune est retrouvée par son code (325 établissements) ou, à défaut, par son nom dans le département : commune actuelle (560), commune déléguée ou associée (4), seule commune actuelle dont le nom contient l'ancien (2 : Ciel → Verdun-Ciel, Éragny → Éragny-sur-Oise), chef-lieu dont les communes déléguées forment ensemble l'ancien nom (1 : Castelnau Montratier-Sainte Alauzie → Castelnau-Montratier). Leur nom est celui de la base, écrit en capitales sans accents et remis en minuscules : les accents ne peuvent pas être rétablis.
- *Établissements au même point de la carte* (5 333) : légèrement décalés à l'affichage pour rester cliquables ; la fiche de chacun renvoie aux autres.
- *Noms* : ceux de l'annuaire, avec une typographie harmonisée (« Ecole primaire Publique » et « E.P.PU » → « École primaire publique » ; noms et mots écrits en capitales remis en minuscules, sauf sigles, sigles à points et chiffres romains ; « E.E.A.PU » → « École élémentaire d'application publique », « E.P.S.PR » → « École primaire spécialisée privée »).
- *Décomposition* : enseignants (État) ; vie scolaire et direction (État ; encadrement pédagogique pour les écoles publiques ; forfait d'externat pour le privé du second degré) ; autres crédits de l'État répartis par élève ; collectivités (commune, département, région, transports) ; CAF et autres administrations publiques (H-B13). Chaque montant est arrondi à l'euro, en conservant le total (méthode du plus fort reste). La fiche dit selon quoi chaque montant des collectivités est réparti (colonnes `cle_commune`, `cle_departement` et `cle_region` de B1) : comptes 2025 de la commune (20 958 écoles publiques), plafonnés ou relevés aux 99e et 1er centiles (658 et 222 écoles), ou moyenne des communes faute de comptes utilisables (20 967 écoles, 32,2 % des écoliers du public, H-B9) ; dépense par collégien du département et par lycéen de la région ; moyenne nationale pour les territoires absents de la *Géographie de l'École* : part du département de 27 établissements (collèges de Mayotte, de Saint-Martin et de Saint-Barthélemy, et un lycée professionnel de Saint-Martin qui accueille des collégiens), part de la région de 16 établissements de Mayotte ; valeur de la Guadeloupe pour la part de la région de 3 établissements de Saint-Martin et de Saint-Barthélemy (H-B10) ; montants nationaux par élève dans le privé ; transports, même montant pour tous les élèves (H-B14). Ces clés ne fixent que la part de chaque établissement : les montants sont recalés sur le total à répartir (H-B9, H-B10) et ne sont pas les dépenses inscrites dans les comptes de la collectivité. La fiche écrit donc « réparti selon… ».
- *Écoles* : la dépense de la commune est la même pour tous les élèves des écoles publiques de la commune (H-B9). Les ATSEM, propres aux classes maternelles, sont donc réparties sur tous les écoliers : la carte sous-estime vraisemblablement la dépense communale des écoles maternelles et surestime celle des écoles élémentaires.
- *Ce que mesurent les écarts* (part de la variance de la dépense par élève, pondérée par les élèves, à l'intérieur de chaque groupe) : entre écoles publiques, la ligne « commune » explique environ 74 % des écarts, les enseignants le reste ; entre collèges publics, les enseignants 54 %, la vie scolaire et la direction 33 %, le département 13 % ; entre lycées généraux et technologiques publics, la vie scolaire et la direction 37 %, la région 32 %, les enseignants 31 % ; dans le privé, les enseignants expliquent tout.
- *Groupe, écart et rang* : le groupe réunit les établissements du même type et du même secteur ; sa moyenne, pondérée par les élèves, porte sur tous ses établissements (comme B2). L'écart rapporte la dépense par élève de l'établissement à cette moyenne. Le rang est la part des établissements comparés du groupe dont la dépense par élève, arrondie à l'euro, est strictement plus faible (colonnes `etablissements_comparables` et `dont_moins_chers` du CSV) ; la fiche l'arrondit vers le bas et le borne (« moins de 1 % », « plus de 99 % », « la plus faible », « la plus élevée »). Sous 50 élèves (8 896 établissements), la page signale une estimation fragile.
- *Établissements non classés* (affichés, mais sans écart ni rang ; 186 établissements, 37 998 élèves) : écoles sans ETP d'enseignant publié (12) et collèges et lycées publics dont tout ou partie des personnels de vie scolaire et de direction n'est pas publié (35 : 13 sans l'un ni l'autre, 4 sans vie scolaire, 18 sans direction), dont la dépense est sous-estimée (H-B12) ; écoles privées sous contrat pour une partie de leurs classes, ou hors contrat, selon l'annuaire (136, H-E5) ; établissements des groupes de moins de 10 établissements (3 : l'EREA privé et les deux écoles secondaires spécialisées, privées). Pour un groupe de moins de 10 établissements, la fiche ne cite pas de moyenne.
- *Histogramme de la fiche* : axe limité aux 1er et 99e centiles du groupe quand il compte au moins 50 établissements comparés ; les valeurs extrêmes vont dans les barres du bord.
- *Heures d'enseignement par élève (H/E)* : heures hebdomadaires assurées devant les élèves, rapportées aux élèves en division, pour les seuls niveaux du secondaire.
- *Symboles*, choix de présentation : le rayon d'un point croît avec la racine carrée de ses élèves (1,6 + 0,075 × √élèves pixels, multiplié par un facteur qui augmente avec le zoom ; la clé de la page montre 100, 500 et 2 000 élèves). Le public est un disque plein ; le privé sous contrat, un anneau, dès que le rayon atteint 2,6 pixels.
- *IPS de la fiche* : IPS 2024-2025 de la DEPP. Écoles : calculé sur les élèves de CM2, publié pour les écoles ayant eu au moins 25 élèves de CM2 sur cinq ans (H-B15) ; EREA : fichier propre aux EREA (`ips_erea_2024-2025.csv`) ; cité scolaire : IPS du collège.
- *Classes de couleur des établissements*, choix de présentation : moins de 8 000 €, puis tranches de 3 000 € jusqu'à 17 000 € et plus ; pour l'écart, moins de −20 %, −20 à −10 %, −10 à −3 %, −3 à +3 %, +3 à +10 %, +10 à +20 %, +20 % et plus ; en mode écart, les établissements non classés sont des cercles neutres à contour pointillé.
- *Affichage*, au choix du lecteur : un bouton au-dessus de la carte choisit « Moyennes par département » (à l'ouverture) ou « Chaque établissement ». La carte ne change pas d'affichage d'elle-même au zoom ; rechercher ou choisir un établissement passe à « Chaque établissement ».
- *Vue par département*, choix de présentation : chaque département prend la couleur de ses établissements affichés. Soit leur dépense par élève (dépense totale / élèves), en cinq classes fixes autour de la moyenne des établissements affichés (−10, −3, +3 et +10 %) ; soit l'écart « à structure égale » : dépense des établissements affichés du département / dépense qu'ils auraient au coût moyen national de leur type et de leur secteur, − 1, avec les classes de l'écart des établissements. Les établissements des groupes de moins de 10 établissements en France (H-B18, non classés) ne comptent pas dans cet écart, et la fiche ne leur donne pas de moyenne nationale. Un clic sur un département ou une collectivité (Saint-Martin, Saint-Barthélemy) ouvre sa fiche : moyenne et écart à structure égale, décomposition moyenne par élève, tableau par type et secteur (moyenne du département, moyenne nationale, écart), part des élèves du privé et du second degré, et deux boutons (« Voir ses établissements », « Zoomer sur le département » ou « … sur la collectivité »). Les valeurs de chaque département figurent aussi dans un tableau sous la carte, dont chaque ligne ouvre la fiche.
- *Fond de carte* : contours administratifs 2025 (Etalab, généralisation à 100 m), coordonnées arrondies au dix-millième de degré ; positions des mairies et des centres des communes : API Découpage administratif, qui les tire du même jeu (ODbL) ; noms et populations des communes : Insee, par la même API. Ouverte depuis le disque, la page propose aussi le fond « Plan IGN » (Géoplateforme de l'IGN) ; la version publiée en ligne ne peut pas charger d'images externes.

### Comparaisons territoriales (Paris et Seine-Saint-Denis)

Ces cinq hypothèses (H-B19 à H-B23) servent l'analyse [analyse_seine_saint_denis_paris.md](analyse_seine_saint_denis_paris.md). Elles ne changent pas B.

**H-B19. Comparer des départements avec B.** Une moyenne départementale de B additionne trois sortes de montants :
- *des moyens observés par établissement*, comptés au coût moyen national : ETP d'enseignants (écoles), heures d'enseignement pondérées par l'indice des corps (collèges, lycées), ETP de vie scolaire et de direction (H-B4, H-B5, H-B7). L'âge, l'ancienneté et le statut des enseignants (sauf, en partie, les contractuels du 2nd degré), les primes d'éducation prioritaire, la prime de fidélisation territoriale de la Seine-Saint-Denis, l'indemnité de résidence et les majorations de traitement outre-mer ne sont pas pris en compte. La ligne « enseignants » d'une école est donc proportionnelle à ses ETP ;
- *des montants répartis par une clé territoriale* : commune (H-B9), département et région (H-B10) ;
- *des montants répartis à parts égales par élève* : remplacement, formation, AESH, bourses, allocation de rentrée, transports (H-B7, H-B13, H-B14).

Les ETP sont ceux des enseignants affectés dans l'établissement au 30 novembre (panel des personnels de la DEPP ; métadonnées des jeux « Les personnels dans les établissements du premier degré » et « … du second degré »). Un poste vacant n'est pas compté ; un enseignant absent l'est, qu'il soit remplacé ou non. B ne mesure donc ni les postes vacants, ni les absences non remplacées, ni l'expérience des enseignants.

*À structure égale* : dépense des établissements du département / dépense qu'ils auraient au coût moyen national de leur type et de leur secteur − 1 (méthode de la carte, H-B18). Cette correction neutralise la part du privé et le poids de chaque niveau ; elle ne neutralise ni l'éducation prioritaire, ni la taille des établissements, ni le milieu social. Les contributions par composante sont calculées avec les moyennes nationales de chaque composante, par type et secteur.

*Validation* : rapportée à la moyenne nationale, la part de l'État de B dépasse celle de la DEPP (*Géographie de l'École* 2026, fiche 21 : dépense du MEN par élève en 2023, public et privé, par région) de 2,8 points au 1er degré (B : 100,5 ; DEPP : 97,7), 3,4 points au collège (97,4 ; 94,0) et 3,4 points au lycée (94,9 ; 91,5) pour l'Île-de-France. L'écart est faible pour les Hauts-de-France (B : 102,3, 103,6, 102,9 ; DEPP : 103,2, 104,0, 102,2). Interprétation : B ne voit pas les rémunérations plus faibles d'enseignants plus jeunes (texte de la fiche 21, p. 50). Dans les DROM, B est au contraire inférieur à la DEPP de 10 à 45 points, faute d'imputer les majorations de traitement des fonctionnaires outre-mer : la carte y sous-estime la part de l'État. Aucune série officielle n'existe par département.

**H-B20. Comparer B aux chiffres du débat public.** On ne compare que des grandeurs de même périmètre :
1. même financeur : l'État seul, ou l'ensemble des administrations publiques ; jamais l'État seul d'un côté et tous les financeurs (familles et entreprises comprises) de l'autre ;
2. mêmes élèves : public seul, ou public et privé sous contrat ; avec ou sans post-bac ;
3. même année et mêmes conventions (pensions au taux du CAS, H-G6). Les comparaisons qui mêlent public et privé dépendent de cette convention : le CAS Pensions fait 35 % du titre 2 du programme 140 (public), 0,6 % de celui du programme 139 (privé).

Référence nationale « État seul » pour 2023 : environ **5 950 € par élève** du 1er et du 2nd degré, public et privé sous contrat. C'est la moyenne des montants de la fiche 21 (4 710 € par écolier, 6 550 € par collégien, 8 550 € par lycéen), pondérée par les élèves de la rentrée 2023 du tableau E1 (6 339 913 écoliers, 3 404 820 collégiens, 2 251 866 lycéens), soit 5 953 € ; calcul de l'auteur. Pour le public seul, environ 6 380 € (5 953 € × 1,072, rapport entre la part de l'État par élève du public et par élève de l'ensemble dans B : 7 354 / 6 863). La fiche 21 ne cite pas le programme 140 dans sa liste de programmes (anomalie 9) ; on suppose qu'il est compris.

Les chiffres non publiés (note du préfet de la Seine-Saint-Denis sur 2023 ; calcul du « +13 % » du ministre) ne sont pas utilisés comme données. Les déclarations, les chiffres syndicaux et les articles de presse sont cités comme éléments du débat.

**H-B21. Effets non modélisés, chiffrés pour Paris et la Seine-Saint-Denis (sensibilités, non intégrées à B).** Ordres de grandeur en euros par élève du public, en 2025, par rapport à B. Calculs de l'auteur ; les effets sont additionnés sans être croisés (les effets 1 à 3 se recouvrent en partie).

| Effet | Données et hypothèses | Paris | Seine-Saint-Denis |
|---|---|---|---|
| 1. Âge et ancienneté, écoles publiques | Moins de 35 ans : 24,3 % (Paris), 30,1 % (93), 21,2 % (France) ; 50 ans ou plus : 33,8 %, 22,1 %, 32,0 % (*Géographie de l'École* 2026, fiche 23, onglets 23.1 et 23.2 ; champ : public et privé sous contrat). Salaires par âge (*Panorama* 2025-2026, tableau 7.11 : seules les tranches « moins de 30 ans » et « 50 ans ou plus » sont publiées), indice moyen par ancienneté (figure 6.8), prime d'attractivité par échelon (NI 26.36, figure 9). Hypothèses : les moins de 35 ans sont payés entre le salaire des moins de 30 ans et la moyenne ; les pensions sont proportionnelles au traitement. | ≈ 0 (−0,1 à +0,3 % du coût d'un ETP) | −2,2 à −3,6 % : −100 à −165 € |
| 2. Contractuels, écoles publiques | Non-titulaires : 5,5 %, 10,0 %, 4,4 % (fiche 23, onglet 23.3 ; public et privé : à Paris, où 26 % des écoliers sont dans le privé, la part du seul public peut différer). Coût d'un contractuel : 0,5 à 0,6 fois celui d'un titulaire dans la convention de B, qui compte la cotisation des fonctionnaires au CAS Pensions (35 % du titre 2 du programme 140) ; le rapport des seuls salaires nets est d'environ 0,68 (*Panorama*, tableau 7.3 : contractuels et maîtres délégués enseignants, public et privé, 2 350 € ; fonctionnaires du 2nd degré public, 3 450 €). | −0,5 % : −23 à −28 € | −2,5 % : −110 à −130 € |
| 3. Âge et ancienneté, collèges et lycées publics | Collèges, tous ETP (non-titulaires compris) : moins de 35 ans 16,3 %, 49,7 %, 20,1 % ; 50 ans ou plus 43,0 %, 14,9 %, 36,1 %. B tenant déjà compte des contractuels du 2nd degré par l'indice des corps (H-B5), l'effet est un majorant. Lycées, titulaires seuls : moins de 35 ans 2,9 %, 25,6 %, 8,3 % ; 50 ans ou plus 62,2 %, 33,0 %, 53,5 % (open data « personnels des établissements du second degré », rentrée 2024). Même méthode que l'effet 1 (certifiés). | collèges +1,4 à +2,7 % : +80 à +150 € ; lycées +3,0 % : +110 à +225 € | collèges −5,6 à −10,7 % : −340 à −640 € (majorant) ; lycées −7,6 % : −300 à −570 € |
| 4. Indemnités REP et REP+ | 5 114 € par an (REP+, part fixe : arrêté du 28/08/2015 modifié, montant rappelé par l'arrêté du 08/12/2022) plus une part modulable de 234, 421 ou 702 € bruts (circulaire du 30/06/2021), supposée attribuée à 25 %, 50 % et 25 % des personnels (à vérifier) ; 1 734 € (REP, décret n° 2015-1087). Part des ETP en REP+ / REP (B1) : écoles 4,4 / 33,8 % (Paris), 24,7 / 38,7 % (93), 10,2 / 15,3 % (France) ; collèges 3,6 / 22,7 %, 24,0 / 40,3 %, 9,1 / 15,6 %. | écoles ≈ 0 ; collèges +16 € | écoles +65 à +80 € ; collèges +85 à +135 € |
| 5. Pondération de 1,1 des heures en REP+ (collèges) | Part des heures en REP+ : 23,0 % (93), 8,6 % (France). | −5 € | +85 à +107 € |
| 6. Prime de fidélisation territoriale | 12 000 € depuis le 01/01/2024. Montants lus dans le RAP 2025, lignes « autres variations » (2025) et « débasage » (2024) : P140 47,8 et 82,0 M€ ; P141 49,7 et 75,4 M€ ; P230 17,6 et 30,1 M€ ; P139 2,2 et 3,2 M€ ; P214 0,1 et 0,7 M€. Hypothèse : ces lignes donnent les montants versés chaque année. Imputation aux seuls élèves du public du 93 (P230 non compté). | −9 € (écoles), −11 € (2nd degré) | +252 € par écolier ; +358 € par élève du 2nd degré (2025) ; environ +430 € par écolier en 2024 |
| 7. Indemnité de résidence | 3 % du traitement en zone 1 (Paris et toutes les communes du 93 ; décret n° 85-1148, art. 9 ; circulaire du 12/03/2001), contre 0,68 % en moyenne (NI 26.36, figure 6 : 20 € par mois pour un traitement brut moyen de 2 940 €) ; environ +937 € par ETP (+1,2 %). | +57 € (écoles), +71 € (2nd degré) | +56 € (écoles), +73 € (2nd degré) |
| 8. Clé départementale par collégien du public | (dépense par collégien × collégiens du public et du privé − 594 € × collégiens du privé) / collégiens du public (fiche 22, onglet 22.1 ; forfait du privé : B0) : 2 006 € au lieu de 1 480 € (Paris), 2 428 € au lieu de 2 190 € (93), puis recalage sur le total. | +250 € | −154 € |
| 9. Allocation de rentrée selon les CAF | Montants 2025 (taux plein et différentiel) : 37,30 M€ (Paris), 84,76 M€ (93), 2 134,9 M€ (France) (CNAF, data.caf.fr, jeu ars_s_type_dep). | −37 € (écoliers de 6 ans et plus), −68 € (2nd degré) | +47 €, +84 € |
| 10. Bourses selon le taux de boursiers | Collégiens boursiers : 19,9 %, 41,4 %, 26,1 % (fiche 5, onglet 5.2) ; B : environ 180 € par élève du 2nd degré public. | −25 à −45 € | +60 à +105 € |
| 11. AESH selon l'académie | 14,8 (Paris), 9,8 (Créteil, appliqué au 93), 13,3 (France) pour 1 000 élèves du public (fiche 26, onglet 26.4) ; B : environ 250 € par élève. | +28 € | −66 € |
| 12. Remplaçants du 1er degré | 6,5 %, 9,3 %, 8,7 % des enseignants du public (fiche 23, onglet 23.4) ; rapportés aux élèves, environ ±17 % ; B : environ 400 € par écolier du public (P140, action 05 « Remplacement », 2 170 M€ en 2025). | −66 € | +66 € |
| 13. Postes vacants du 93 | 87 ETP vacants dans la brigade de remplacement et 72 « hors la classe » en 2023 (rapport AN n° 1938, p. 123) ; crédits répartis par élève dans B. **Non additionné** : les remplaçants de l'effet 12 sont des enseignants en poste, sans les postes vacants. | — | (−35 à −65 €) |
| 14. Clé communale | Variantes ci-dessous (DGFiP 2025 ; CRC Île-de-France, IDR2025-64). | −2 461 à +942 € | +93 à +1 013 € |
| 15. Partenariats public-privé des collèges du 93 (H-B23) | Capital (compte 1675) et intérêts (compte 6618) de la fonction 221, 2022-2025, DGFiP. **Non additionné.** | — | collèges : +207 € (capital), vraisemblablement +79 € (intérêts) |

Variantes de la clé communale (ligne « commune » des écoles publiques), appliquées à toutes les communes ; le total national ne change pas (3 878 € par écolier du public) :

| Variante | Paris | 93 |
|---|---|---|
| B : fonctionnement 2025 (fonctions 20, 21x, 28x, 29 ; comptes 6 hors 66, 675, 676, 68) | 9 473 € | 3 435 € |
| Sans les forfaits versés aux écoles privées et les frais de scolarité (comptes 6558 et 65748 : 505 M€, 4,8 % de la clé ; Paris 37,0 M€, 93 5,8 M€) | 9 416 € | 3 552 € |
| Nette des recettes des familles (comptes 70 des mêmes fonctions : 1 358 M€, 12,8 % de la clé ; Paris 10,7 M€, 1,5 % ; 93 50,4 M€, 10,8 %) | 10 230 € | 3 528 € |
| Nette des recettes, sans les forfaits | 10 415 € | 3 651 € |
| Fonctionnement + investissement 2025 de chaque commune (comptes 20, 21 et 23 des mêmes fonctions) | 7 778 € | 4 040 € |
| Nette des recettes, + investissement de chaque commune | 8 528 € | 4 272 € |
| Nette, sans forfaits, + investissement de chaque commune | 8 487 € | 4 202 € |
| Nette, sans le personnel extrascolaire de Paris (53,1 M€ en 2023, CRC, p. 53-54 ; hypothèse : il figure dans la fonction 2), + investissement | 7 918 € | 4 219 € |
| Nette, élargie à la fonction 33 « jeunesse et loisirs » (borne haute pour le 93 : elle contient aussi des dépenses sans lien avec l'école) | 8 046 € | 4 448 € |
| Nette, sans forfaits, fonction 33, part d'investissement (24,8 % du total) répartie à parts égales par élève (borne basse pour Paris) | 7 012 € | 4 307 € |

Les variantes qui comptent l'investissement de chaque commune sont jugées les plus défendables : l'investissement des communes du 93 dans leurs écoles est élevé en 2024 comme en 2025 (242 et 249 M€, contre, pour Paris, 62 à 64 M€ selon le périmètre et 63 M€ ; en moyenne 2023-2025, 1 223 € par écolier du public contre 624 €, H-B22). Bilan des effets 1 à 14, sans croisement : voir le § 3.7 de l'analyse ; l'effet 15 n'y est pas additionné.

**H-B22. Dépense de bâtiments : indicateurs de la comparaison Paris / Seine-Saint-Denis (non intégrés à B).** On compare des flux de dépense pour les bâtiments, par élève du public, sur plusieurs années, à partir des comptes de chaque collectivité. Ces indicateurs servent l'analyse (§ 2.8 et § 4) ; ils ne changent pas B. Calculs de l'auteur.
- *Écoles (communes)* : balances DGFiP 2021-2025, tous budgets (budgets d'arrondissement de Paris compris), fonctions « écoles » : 20, 21x, 28x et 29, codes 90x et 93x compris ; en M14, 25x sauf 252 ; fonction 2 non ventilée. **Investissement** : débit réel (OBNETDEB − OOBDEB) des comptes 20 (y compris 204), 21 et 23. **Bâti** : constructions et rénovations (2313, 2314, 2131x, 2135x, 2138, 214x, 2173-2174, 2181, 2317, 235), avances sur travaux (236 à 238), terrains et aménagements (211, 212, 2171-2172, 2311, 2312). **Dépenses courantes liées aux bâtiments, hors personnel** : débit net (débit − crédit réels) des comptes 6152, 61521, 61522x, 6156, 6283, 60631, 6061x, 60621, 6132, 614 et 616. **Personnel** : comptes 621, 631, 633 et 64. **Subventions d'investissement reçues** : crédit réel net des comptes 13 (hors 139), enregistré l'année où la subvention est titrée, pas celle de la dépense ; origine lue dans le compte, l'ANRU étant comptée avec l'État (1321). Dénominateur : élèves des écoles publiques de la rentrée N−1 (DEPP, appariés à la commune par l'annuaire ; pour la rentrée 2024, les mêmes que B1 à Paris et en petite couronne). Moyenne pluriannuelle = somme des montants / somme des élèves. Saint-Denis et Pierrefitte-sur-Seine sont regroupées sur toute la période (39 entités). « France » : communes à comptabilité fonctionnelle (environ 3 300 communes, environ 70 % des élèves du public). Paris « au plus » : on ajoute les investissements scolaires que la Ville range hors des fonctions « écoles » dans ses comptes administratifs (budget participatif, accessibilité, contrats de performance énergétique, écoles de zones d'aménagement : 15,4, 35,0 et 36,5 M€ en 2023, 2024 et 2025, dont 6,0 M€ en 2024 pour l'école de l'équipement Pinard, ZAC Saint-Vincent-de-Paul) ; c'est une borne haute, qui compte aussi des collèges. Avec ces définitions, le 93 est à 1 363 € en 2025 (débit réel), contre 1 357 € au § 3.1 de l'analyse et en H-B21 (net des crédits). Investissement « écoles » de Paris en 2024 : 62,4 M€ sur ce périmètre, 63,7 M€ en ajoutant la sous-fonction 258 (origine probable des 64 M€ cités en H-B21).
- *Collèges (départements)* : fonction 221, budgets principaux. **Équipement** : agrégat OFGL « dépenses d'équipement » (M57 : D20 + D21 + D23 − D204 − D2324 − C236 − C237 − C238). **Investissement dans le bâti** : équipement + subventions d'équipement versées + capital des partenariats public-privé remboursé (débit réel du compte 1675 en fonction 221, DGFiP ; H-B23). Dénominateur : collégiens du public de l'année civile N = 2/3 de la rentrée N−1 + 1/3 de la rentrée N (convention de la DEPP ; rentrées 2015-2018 raccordées à 2019 par le rapport des deux jeux de la DEPP). **Dotation de l'État pour l'équipement des collèges (DDEC) par collégien** : cumul 2015-2019 du tableau n° 1 de la Cour des comptes (RPA 2023, p. 343 : 40,1 M€ pour le 93, 1 401,6 M€ pour la France) / 5 / collégiens du public moyens des rentrées 2015-2019 (DEPP) : environ 108 € dans le 93 et 106 € en France. Paris : Département de Paris jusqu'en 2018, Ville de Paris ensuite ; « au plus » : avec la fonction 24 (cités scolaires), qui sert aussi des lycées. « France » : départements, Paris et Métropole de Lyon (OFGL, sans les collectivités territoriales uniques), **sans Mayotte**, dont l'OFGL ne donne pas de fonction 221 : 939 € d'équipement par collégien du public et par an en 2022-2025 (928 € si l'on garde Mayotte au dénominateur) ; 979 € avec les subventions d'équipement ; environ 990 € avec le capital des PPP (DGFiP, collectivités territoriales uniques comprises).
- *Lycées (Région Île-de-France)* : **dotation de fonctionnement consolidée 2026** par établissement (CR 2025-030, annexe 1 au rapport : DGFL, internat, contrôles et contrats d'entretien obligatoires, énergie, équipements de protection individuelle ; montants votés, l'énergie étant estimée au budget 2026 ; sans les salaires des agents ni l'investissement ; 206,2 M€ pour les 461 établissements dont les effectifs sont connus, sur 210,1 M€ publiés) ; **opérations directes et subventions votées en 2021-2023** (open data de la Région : autorisations affectées, revalorisations et désaffectations comprises ; ce ne sont pas des paiements ; département lu dans l'UAI ou, à défaut, dans le libellé ; 45 % du montant des opérations directes est rattachable) ; **autorisations de programme des plans d'investissement**, années 1995-2018. Dénominateurs : élèves accueillis (lycéens pré-bac, étudiants de BTS et de classes préparatoires, collégiens des collèges appariés aux cités mixtes régionales, que la Région dote en entier) ou lycéens pré-bac (comme B) ; élèves de la rentrée 2025 pour la dotation 2026, moyenne des rentrées 2021 à 2023 pour les opérations votées en 2021-2023 (B, lui, divise par les élèves de la rentrée 2024). Moyenne 2021-2023 : somme / élèves moyens / 3. Le numérateur couvre tous les élèves accueillis : la comparaison par lycéen pré-bac avantage donc Paris, où 44 % des élèves accueillis ne sont pas des lycéens pré-bac (11 % dans le 93) ; l'écart entre Paris et le 93 change de signe selon le dénominateur.
- *Part des bâtiments dans la dépense par élève (France, 2025)* : investissement, énergie (6061x, 60621-60622) et entretien (6152x, 6156, 6283) des collectivités, budgets principaux (balances DGFiP 2025), rapportés aux élèves du public concernés (pour les écoles, ceux des communes à comptes par fonction), puis au total de B. Variante « étroite » : constructions et rénovations seulement ; « large » : tout l'investissement ; majorant : avec toutes les dotations de fonctionnement versées aux collèges et aux lycées (12,0 % et 12,8 %). Pour les lycées, sans la sous-fonction 223 « lycées privés » et × 0,8649 (part du champ, H-B11). Variante M2 : structure de H-D2 appliquée aux lignes de B. 2025 est vraisemblablement une année haute pour les écoles (dernière année pleine du mandat municipal).
- *Limites* : flux annuels en euros courants, sans amortissement (H-G5) ; montants irréguliers d'une année à l'autre, d'où les moyennes pluriannuelles. Les collectivités ne rangent pas toutes leurs dépenses aux mêmes fonctions : Paris range des investissements scolaires hors des fonctions « écoles » (voir plus haut ; pour le 93, non recherché). En 2025, 12 communes du 93 (51 163 élèves, 28 % des écoliers du public) imputent moins de 10 % de leur personnel aux écoles : le personnel « écoles » du 93 (1 462 €) est un minimum, les 27 autres communes étant vers 1 790 €. Dix communes du 93 (61 098 élèves) imputent moins de 10 % de leur énergie aux écoles, et Paris n'y impute pas l'eau en 2023-2024 : les dépenses courantes « bâti » (287 € des deux côtés) sont deux minimums. Bondy et Aulnay-sous-Bois imputent peu de leur équipement aux écoles (Bondy : 6 à 9 % en 2021-2025 ; Aulnay-sous-Bois : 8 à 9 % en 2024-2025 ; 30,4 % pour l'ensemble des communes du 93 en 2023-2025) : leur faible investissement « écoles » peut tenir en partie à ce choix. Le personnel d'entretien n'est pas isolable dans les comptes ; la régie ou la sous-traitance changent les comptes (Paris : 1 730 ETP d'agents d'entretien dans les écoles en 2023, dont plus de la moitié du temps sur le périscolaire, CRC, IDR2025-64, p. 52-53). Pour les départements, le fonctionnement n'est pas comparable (énergie payée par le département dans le 93, par les collèges à Paris ; personnel rangé hors de la fonction 221 dans certains départements, et en partie dans la fonction 201 à Paris). **Aucun de ces indicateurs ne mesure l'état des bâtiments.** L'âge non plus : l'année de construction de la BDNB (CSTB, issue des fichiers fonciers) n'est connue que pour 46 à 74 % des établissements publics de Paris et du 93, et fausse pour une partie des bâtiments de la Ville de Paris (anomalie 16) ; la date d'ouverture de l'annuaire est administrative (anomalie 17) ; l'année de construction des lycées de la Région manque pour 14 % d'entre eux (24 % à Paris) et est parfois inexacte (CRC, IDR2021-39, p. 19).

**H-B23. Partenariats public-privé (PPP) des collèges de la Seine-Saint-Denis : absents de B (sensibilité, non intégrée).**
- Le Département rembourse chaque année le capital de ses contrats de partenariat (18 collèges en PPP, selon la chambre régionale des comptes) : 16,11 ; 16,03 ; 16,36 et 16,69 M€ de 2022 à 2025 (débit réel du compte 1675 en fonction 221, DGFiP), soit environ 207 € par collégien du public et par an. Les intérêts (compte 6618, fonction 221) font environ 6,2 M€ par an, soit environ 79 €. Encours au 31/12/2025 : 173,9 M€ (calcul de l'auteur : encours au 1er janvier + dette inscrite − capital remboursé).
- Ni le total national réparti par B (investissement sans les comptes 16, fonctionnement sans le compte 66 : `data/raw/collectivites/NOTES.md`, § 2), ni, vraisemblablement, la clé de la fiche 22 de la DEPP ne comptent ces montants : sans les PPP, notre calcul donne 730 € d'investissement par collégien du public et du privé en 2021-2023 (euros courants), proche des 750 € publiés par la DEPP (euros constants 2023) ; avec eux, 903 €.
- *Effet* : la ligne « département » des collèges publics du 93 est sous-estimée d'environ 207 € par élève (capital), et vraisemblablement d'environ 79 € (intérêts). En moyenne nationale, le capital des PPP fait environ 11 € par collégien du public (2022-2025) : le recalage sur le total national changerait peu cet ordre de grandeur. Aucun remboursement de PPP n'apparaît dans les comptes des collèges de Paris (fonction 221). La dette de PPP de la Ville (2,41, 2,33 et 2,22 M€ de capital remboursé en 2023, 2024 et 2025, chapitre 923) correspond au contrat de partenariat de performance énergétique des écoles (encours de 14,6 M€ fin 2025, compte administratif 2025, p. 23 ; signé en 2011 pour 100 écoles selon la CRC, IDR2025-64, p. 44), soit environ 20 à 23 € par écolier du public.
- *Convention* : compter le capital remboursé suit la présentation du Département lui-même : ses montants de 2016-2020, publiés par la chambre régionale des comptes, correspondent presque exactement à l'équipement de la fonction 221 plus ce capital. Une convention « patrimoniale » compterait plutôt la dette inscrite à la livraison des collèges (317,8 M€ de 2014 à 2022), soit 1 474,8 M€ d'investissement pour le 93 sur 2012-2025, au lieu de 1 301,0 M€. Lire les inscriptions de 2016 à 2022 comme des livraisons des nouveaux contrats est une déduction.
- Cette sensibilité n'est pas additionnée aux fourchettes de H-B21 ni du § 3.7 de l'analyse.

---

## C. Recoupements et sensibilités

**H-C1. COFOG (INSEE, 2024).** On calcule une fourchette :
- borne basse : fonctions 09.1 (préélémentaire et primaire) + 09.2 (secondaire) ;
- borne haute : on ajoute 09.6 (services annexes : cantines, internats et transports en dépenses brutes, mais aussi services du supérieur comme les CROUS et les bourses étudiantes) et 09.8.

La fonction 09.5 (enseignement non défini par niveau, 8,6 Md€) n'est pas répartie. L'allocation de rentrée scolaire relève de la protection sociale (fonction 10) et non de la fonction 09. On rapporte la fourchette aux effectifs DEPP (comparables à A) et, pour mémoire, aux seuls élèves de l'Éducation nationale.

**H-C2. UOE et OCDE (2023).** Les valeurs par niveau sont publiées. Les agrégats « 1er degré », « 2nd degré » et « ensemble » (8 026, 10 342 et 9 141 €) sont **des moyennes calculées ici**, pondérées par les élèves en équivalent temps plein. Ces sources servent de comparaison d'ordre de grandeur.

**H-C3. Sensibilité aux pensions.**
- Base de calcul : les contributions au CAS Pensions 2025 de chaque programme (RAP 2025), comptées pour la part des crédits du programme réellement répartis dans B, soit 22,3 Md€.
- On applique à la place de 78,6 % un taux de cotisation corrigé :
  - 34,7 % : taux d'équilibre des employeurs de fonctionnaires d'État (civils et militaires) calculé par l'IPP pour 2020, si l'État finançait à part la subvention implicite liée au déséquilibre démographique non compensé et les droits propres à certaines professions (IPP, p. 53 et 63). L'IPP le suppose constant entre 2020 et 2023 (encadré 3, p. 67) ; son maintien en 2025 est une hypothèse du dossier. Le *Focus* du CAE (H. Paris, publié sous la seule responsabilité de son autrice) y voit une approximation de l'effort contributif de l'État employeur et une « borne haute » (*Focus* n° 121, p. 7) ;
  - 25,44 % : borne basse proposée dans ce *Focus* (même page) ; le « juste » taux « pourrait » se situer entre les deux.
- Baisse : 12,4 à 15,1 Md€, soit −1 050 à −1 270 € par élève de B et −990 à −1 200 € par élève de A.
- Les pensions de l'enseignement agricole et des autres ministères ne sont pas comptées : c'est un minimum.

**H-C4. Comparaison A / B : voir H-B17.**

---

## D. Décomposition par poste de dépense

**H-D1. Postes de l'État (tableau D1).** Ce sont les actions budgétaires regroupées :

| Poste | Actions |
|---|---|
| Enseignants affectés | crédits d'enseignement, H-B4 |
| Remplacement et formation | P140 a04, a05, a07 ; P141 a10, a11, a13 ; P139 a10-12 |
| Direction, administration et encadrement pédagogique | P141 a12 ; P140 a06 |
| Vie scolaire | P230 a01 |
| AESH, santé et service social, orientation | P230 a02, a03, a07, a04 (titre 2) ; P141 a07-08 |
| Actions éducatives | P230 a06 |
| Bourses et fonds sociaux | P230 a04 (hors titre 2) ; P139 a08 |
| Forfait d'externat et internats | P139 a09 ; P230 a05 |
| Administration centrale et académique | P214 a01-10 |

Les postes de personnel incluent les pensions, au taux du CAS (H-G6).

**H-D2. Postes des collectivités.** Les montants des collectivités pour les écoles, les collèges et les lycées publics sont ventilés selon la **structure nationale 2025 des balances DGFiP** de chaque niveau :
- personnel ;
- investissement (construction, rénovation, grosses réparations, équipement) ;
- entretien et énergie ;
- restauration (achats, prestations) ;
- autres dépenses de fonctionnement (dotations aux établissements, fournitures, caisses des écoles).

Hypothèses : cette structure vaut pour chaque établissement, et pour le montant DEPP des écoles, qui comprend la quote-part d'administration générale et est net des participations des familles. Ce montant DEPP ne contient pas les fournitures scolaires : on le ventile donc avec la structure hors compte 6067, et les fournitures ajoutées en H-B8 sont classées dans les « autres dépenses de fonctionnement ». Pour les lycées, la structure exclut toute la sous-fonction 223 « Lycées privés », comme le montant réparti entre lycées publics (H-B10). Pour le privé, toute la dépense des collectivités est classée « forfait » (fonctionnement).

**H-D3. Les quatre catégories de départ (tableau D2).**

| Catégorie | Postes regroupés |
|---|---|
| 1. « profs » | enseignants affectés + remplacement et formation |
| 2. « réparations » (bâtiments et équipement) | investissement des collectivités (construction, rénovation, grosses réparations, équipement) + entretien et énergie |
| 3. « activités » et fonctionnement | restauration, transports, actions éducatives, autres dépenses de fonctionnement, forfaits versés au privé (collectivités et État), internats |
| 4. « autres » | vie scolaire, direction et encadrement, AESH, santé et service social, orientation, personnels des collectivités (ATSEM, agents), bourses et fonds sociaux, allocation de rentrée scolaire, administration centrale |

Ces regroupements sont des choix de présentation.

---

## Anomalies relevées dans les sources

Elles sont signalées pour la transparence ; aucune ne change le résultat.

1. **NI 26.42, onglet « Figure 6 »** : la cellule D33 porte le libellé « Supérieur » en face de la moyenne du 2nd degré (11 780 €). Nous lisons la figure 7, correctement libellée.
2. **RERS 2026, fiche 10.04** : la structure par nature diffère entre le PDF (rémunérations 72,0 %, enseignants 48,4 %, investissement 8,5 %) et l'Excel (70,4 %, 47,4 %, 8,4 %). Nous retenons la structure UOE par niveau (H-A6).
3. **data.education.gouv.fr, « Effectifs d'élèves par école »** : la colonne « code_commune_insee » contient des codes postaux (H-E4).
4. **RAP 2025** : deux valeurs coexistent pour les assistants d'éducation du titre 2 (8 731 ou 8 857,83 ETPT) et pour la subvention aux EPLE (1 411,8 ou 1 413,4 M€). Sans effet : nous répartissons les montants des actions.
5. **RERS 2026, fiche 10.03** : 1 731 M€ pour le programme 143 en 2025, contre 1 688 M€ exécutés selon le RAP. Écart non expliqué ; le programme 143 est hors du champ de B.
6. **DOI de la NI 26.42** : affiché, mais pas encore actif au 04/10/2026. L'URL de la page est donnée en section 0.
7. **Cour des comptes, NEB 2025** : la dépense par élève figurait dans les documents budgétaires « jusqu'en 2023 » (p. 62) ou « jusqu'en 2022 » (p. 86), selon la page.
8. **Cour des comptes, date de la recommandation** sur la dépense par élève : « depuis 2018 » selon la NEB 2025 (p. 62), « depuis 2017 » selon la note thématique de juillet 2023 (p. 8). Le rapport (§ 6) cite les deux.
9. **Géographie de l'École 2026, méthodologie (p. 106)** : la liste des programmes de la fiche 21 (139, 141, 214, 230, 150 et 231) ne cite pas le programme 140 (1er degré public), sans doute par erreur.
10. **P/E de la Seine-Saint-Denis** : 6,43 à la rentrée 2021 dans les réponses aux questions écrites n° 51 et n° 10116, 6,32 dans le rapport AN n° 1938 (p. 124, note 1) ; 6,15 à la rentrée 2019 dans la réponse à la question n° 17285, 6,07 dans le rapport n° 1938. Les définitions (constat ou prévision, postes ou ETP) ne sont pas précisées.
11. **Rapport AN n° 1938, p. 123** : dans le tableau des postes vacants, la dernière colonne est datée « 2022-2023 », comme la précédente ; il s'agit vraisemblablement de 2023-2024.
12. **Brigade de remplacement du 1er degré de la Seine-Saint-Denis** : 1 140 ETP selon la DSDEN (rapport n° 1938, p. 123), « 850 enseignants » renforcés de 120 selon la réponse du ministère au Sénat (JO Sénat du 10/07/2025, p. 4006). Périmètres à préciser.
13. **Chiffre syndical de 8 840 €** : il ne figure dans aucune publication de la DEPP consultée ; *L'Éducation nationale en chiffres 2023* donne 8 860 € (dépense intérieure d'éducation par élève ou apprenti en 2021, tous financeurs).
14. **Date de la déclaration du ministre** : le message X et l'entretien sur BFMTV datent du 28/09/2026 au soir (et non du 29/09, date des premiers relais).
15. **Dette des partenariats public-privé des collèges du 93** : en 2015, la chambre régionale des comptes écrivait que le Département devait intégrer à sa dette, fin 2014, « plus de 300 M€ » au titre des investissements des partenaires privés (CRC 2015, p. 20) ; les balances DGFiP montrent 239,7 M€ inscrits en 2014 au compte 1675. Piste (déduction, à vérifier) : les 239,7 M€ correspondent à peu près aux montants nets financés par les partenaires (203,1 M€ HT, p. 114-116), TVA comprise ; les « plus de 300 M€ » compteraient aussi les participations du Département (114,6 M€ HT).
16. **BDNB (CSTB)** : 243 des 723 bâtiments principaux d'établissements parisiens dont l'année est connue sont datés de 2020 ou après (180 de 2023, 50 de 2024), presque tous propriété de la Ville de Paris (exemple : école Tanger, 19e, datée de 2023 dans les fichiers fonciers et de 1948 dans son diagnostic de performance énergétique). Ces dates sont traitées comme inconnues (H-B22).
17. **Annuaire de l'éducation, date d'ouverture** : le 01/05/1965, date de création de la base, est la date d'ouverture de 64,8 % des écoles publiques parisiennes et de 82,7 % des lycées publics parisiens. Ce champ, sur lequel l'OFGL fonde son indicateur d'âge des établissements (*Cap sur…* n° 21), ne date pas les bâtiments.
18. **Places des lycées (CRC Île-de-France, IDR2021-39, p. 20-23)** : les valeurs de 2018 à 2020 sont des prévisions de la Région « à partir du constat de rentrée 2017 », dont la chambre n'a pas obtenu d'actualisation ; seul 2017 est un constat (remplissage 88 % dans le 93 et 86 % à Paris ; places manquantes 924 et 933). Le tableau des taux de remplissage est illisible en extraction texte (pdftotext) ; il a été lu avec pdfplumber.

---

## Récapitulatif des effets chiffrés

| Hypothèse ou variante | Dépense publique par élève (1er + 2nd degrés), 2025 | Écart à la référence |
|---|---|---|
| **Référence A** (DEPP 2025p, financement initial, apprentis compris) | **9 710 €** | — |
| Hors apprentis (H-A3), *s* = 17,5 % [13,5 % ; 23 %] | 9 968 € [9 951 ; 9 980] | +2,7 % |
| Part « entreprises » du 2nd degré (surtout OPCO) comptée comme publique (H-A8, borne haute) | 9 981 € | +2,8 % |
| Sans les autres administrations publiques, dont l'ARS (H-A4) | 9 526 € | −1,9 % |
| Financement final (H-A2), 2024p | 9 231 € (contre 9 493 € en initial 2024p) | −2,8 % |
| Retraites avec un taux de cotisation corrigé de 34,7 % ou 25,44 % (H-G6, H-C3) | environ 8 500 à 8 700 € | −990 à −1 200 € |
| **Approche B** (par établissement, hors apprentis, H-B1 à H-B17) | **10 203 €** | +2,4 % par rapport à A hors apprentis |
| Élèves de la rentrée 2024 au lieu de l'année civile 2025 dans B (H-E1) | environ −0,3 % sur B (environ −35 €) | — |
| Comparaisons territoriales, Paris et Seine-Saint-Denis : salaires réels, primes, clés communale et départementale (H-B21) | écoles publiques : écart Paris − 93 de +6 144 € dans B, environ +2 500 à +6 700 € après corrections (+3 500 à +4 250 € si l'investissement suit chaque commune) ; collèges publics : 93 − Paris de +1 061 € dans B, +200 à +1 050 € après corrections, sans les remboursements des partenariats public-privé du Département de la Seine-Saint-Denis (environ +207 € par collégien du public, H-B23) | — |
