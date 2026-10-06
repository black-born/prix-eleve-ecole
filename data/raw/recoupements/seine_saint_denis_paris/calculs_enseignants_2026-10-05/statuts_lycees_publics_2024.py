# Profil des enseignants des lycées publics (généraux et technologiques, polyvalents, professionnels), rentrée 2024.
# Source officielle : DEPP, open data « Les personnels dans les établissements du second degré » (data/raw/etablissements/personnels_2d_rentree2024.csv).
# Champ : les lycées publics de B (resultats/B1_depense_publique_par_etablissement_2025.csv, types « lycée … », hors EREA).
# Parts en % des ETP d'enseignants. Chemin relatif à la racine du projet.
import pandas as pd

df = pd.read_csv('data/raw/etablissements/personnels_2d_rentree2024.csv', sep=';', encoding='utf-8-sig', dtype={'code_departement': str})
b1 = pd.read_csv('resultats/B1_depense_publique_par_etablissement_2025.csv', sep=None, engine='python', encoding='utf-8-sig')
uai = set(b1[b1['type'].str.startswith('lycée') & b1['secteur'].eq('public')]['uai'])
l = df[(df.secteur == 'Public') & df.identifiant_de_l_etablissement.isin(uai)]
cols = {'agreges': 'etp_d_enseignants_agreges', 'non_titulaires': 'etp_d_enseignants_non_titulaires',
        'moins_de_35_ans': 'etp_d_enseignants_de_moins_de_35_ans', '50_ans_ou_plus': 'etp_d_enseignants_de_50_ans_ou_plus',
        'anciennete_8_ans_ou_plus': 'etp_d_enseignants_ayant_une_anciennete_dans_l_etablissement_de_8_ans_ou_plus'}
rows = []
for nom, d in [('Paris', l[l.code_departement == '75']), ('Seine-Saint-Denis', l[l.code_departement == '93']), ('France', l)]:
    t = d['etp_enseignants_hommes_et_femmes'].sum()
    rows.append({'territoire': nom, 'lycees': len(d), 'etp_enseignants': round(t, 1),
                 **{k: round(100 * d[v].sum() / t, 1) for k, v in cols.items()}})
out = pd.DataFrame(rows)
out.to_csv('data/raw/recoupements/seine_saint_denis_paris/calculs_enseignants_2026-10-05/statuts_lycees_publics_2024.csv', index=False, sep=';')
print(out.to_string(index=False))
