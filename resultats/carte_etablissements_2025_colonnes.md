# Colonnes de `carte_etablissements_2025.csv`

Une ligne par établissement de l'approche B (script `scripts/07_carte_etablissements.py`). Séparateur « ; », décimale « . », encodage UTF-8 avec BOM ; case vide = valeur inconnue ou sans objet. Hypothèses : H-B18 (hypotheses.md).

| Colonne | Contenu |
|---|---|
| `uai` | Identifiant national de l'établissement (UAI). |
| `nom` | Nom de l'annuaire de l'éducation (typographie harmonisée) ; pour les établissements absents de l'annuaire actuel, nom de la base reconstitué à partir des capitales (sans accents). |
| `commune` | Commune de l'annuaire ; à défaut, commune de l'API Découpage administratif. |
| `code_commune` | Code Insee de la commune ou de l'arrondissement municipal : annuaire ; à défaut fichier IPS (écoles) ou fichiers des collèges et des lycées généraux et technologiques (second degré) ; à défaut nom de la commune dans le département (écoles fermées depuis, H-E4). |
| `code_departement` | Département (977 et 978 pour les écoles de Saint-Barthélemy et de Saint-Martin). |
| `region` | Région académique. |
| `type` | Type d'établissement : écoles d'après les élèves par niveau, à défaut l'annuaire puis le nom (voir type_source) ; second degré d'après la nature officielle (H-B16). |
| `type_source` | Écoles : source du type (effectifs, annuaire, nom ou inconnu). |
| `secteur` | Public ou privé sous contrat. |
| `latitude` | Latitude WGS84 (5 décimales). |
| `longitude` | Longitude WGS84 (5 décimales). |
| `position` | Origine de la position : adresse de l'annuaire, commune seulement, incertaine, ou, pour un établissement absent de l'annuaire actuel, mairie de la commune (centre si l'API ne donne pas de mairie propre). |
| `eleves_rentree2024` | Élèves de la rentrée 2024 (apprentis et étudiants exclus). |
| `dont_maternelle_ou_college` | Écoles : élèves de préélémentaire hors ULIS ; 2nd degré : élèves du collège (Segpa comprise). Vide si non publié. |
| `dont_elementaire_ou_voie_gt` | Écoles : élèves d'élémentaire hors ULIS ; 2nd degré : voie générale et technologique. Vide si non publié. |
| `dont_ulis_ecole_ou_voie_pro` | Écoles : élèves d'ULIS et d'UEEA ; 2nd degré : voie professionnelle. Vide si non publié. |
| `classes_ecole` | Écoles : nombre de classes. |
| `etudiants_sts_cpge_non_comptes` | Lycées : étudiants de STS et de CPGE (hors champ ; part de leurs heures et personnels retirée). |
| `effectif_sts_cpge_masque` | 1 si l'effectif post-bac est en partie ou en totalité masqué (« ns ») dans la source. |
| `etp_enseignants_tous_niveaux` | Équivalents temps plein d'enseignants (post-bac compris) ; vide si non publié. |
| `heures_enseignement_par_eleve_HE` | Heures d'enseignement hebdomadaires devant élèves par élève (niveaux du secondaire). |
| `couverture_HE_%` | Part des élèves présents dans le fichier H/E (peut dépasser 100 : fichiers différents). |
| `indice_cout_corps_enseignants` | Coût relatif des corps d'enseignants (1 = moyenne des titulaires du 2nd degré) ; vide si aucun ETP n'est publié (1 dans le calcul). |
| `ips` | Indice de position sociale (rentrée 2024). |
| `ips_statut` | publié, non publié (NS : effectif trop faible) ou absent. |
| `education_prioritaire` | REP ou REP+. |
| `depense_publique_par_eleve_€` | Dépense publique estimée par élève en 2025 (arrondie à l'euro). |
| `dont_enseignants_€` | État : enseignants. |
| `dont_vie_scolaire_direction_encadrement_€` | État : vie scolaire et direction (public), encadrement pédagogique (écoles publiques), forfait d'externat (privé du 2nd degré). |
| `dont_autres_credits_etat_€` | État : remplacement, formation, AESH, santé, actions éducatives, bourses, administration centrale et académique (et internats publics), répartis par élève. |
| `dont_commune_€` | Commune (écoles) : financement des écoles par les collectivités (compte de l'éducation). |
| `dont_departement_€` | Département : collégiens. |
| `dont_region_€` | Région : lycéens. |
| `dont_transports_scolaires_€` | Transports scolaires (même montant par élève). |
| `dont_caf_autres_apu_€` | Autres administrations publiques, surtout l'allocation de rentrée scolaire (élèves de 6 ans et plus). |
| `cle_commune` | Clé de répartition de la ligne commune (dépense par élève de la commune d'après ses comptes 2025, plafonnée ou relevée aux 99e et 1er centiles ; moyenne des communes ; forfait national du privé) ; les montants sont recalés sur le total du compte de l'éducation. |
| `cle_departement` | Clé de la ligne département (dépense par collégien du département, moyenne nationale, montant national du privé), recalée sur les comptes 2025 des départements. |
| `cle_region` | Clé de la ligne région (dépense par lycéen de la région, valeur de la Guadeloupe pour Saint-Martin et Saint-Barthélemy, moyenne nationale, montant national du privé), recalée sur les comptes 2025 des régions. |
| `moyenne_meme_type_et_secteur_€` | Moyenne de la dépense par élève du groupe (même type, même secteur), pondérée par les élèves. |
| `comparaison` | Vide si l'établissement est comparé à son groupe ; sinon, la raison pour laquelle il ne l'est pas. |
| `ecart_a_la_moyenne_%` | Écart de la dépense par élève à la moyenne du groupe (établissements comparés seulement). |
| `etablissements_comparables` | Établissements comparés dans le groupe. |
| `dont_moins_chers` | Parmi eux, ceux dont la dépense par élève (arrondie) est strictement plus faible. |
| `part_moins_chers_%` | dont_moins_chers / etablissements_comparables × 100. |
