# Contrôle des chiffres de l'IPP (blog n° 43, Y. Souidi, 16/10/2025, figures 6 à 8) à partir de la source officielle :
# DEPP, open data « Les personnels dans les établissements du second degré », rentrée 2024 (data/raw/etablissements/personnels_2d_rentree2024.csv).
# Champ : collèges publics (nature « Collège », hors collèges spécialisés et climatiques). Parts en % des ETP d'enseignants.
# Chemin relatif à la racine du projet.
import pandas as pd

df = pd.read_csv('data/raw/etablissements/personnels_2d_rentree2024.csv', sep=';', encoding='utf-8-sig', dtype={'code_departement': str})
c = df[(df.secteur == 'Public') & (df.nature_de_l_etablissement == 'Collège')]
cols = {
    'agreges': 'etp_d_enseignants_agreges',
    'certifies_peps': 'etp_d_enseignants_certifies_peps',
    'plp_et_autres_titulaires': ['etp_d_enseignants_plp', 'etp_d_enseignants_titulaires_d_un_autre_corps'],
    'non_titulaires': 'etp_d_enseignants_non_titulaires',
    'moins_de_35_ans': 'etp_d_enseignants_de_moins_de_35_ans',
    '50_ans_ou_plus': 'etp_d_enseignants_de_50_ans_ou_plus',
    'anciennete_8_ans_ou_plus': 'etp_d_enseignants_ayant_une_anciennete_dans_l_etablissement_de_8_ans_ou_plus',
}
rows = []
for nom, d in [('Paris', c[c.code_departement == '75']), ('Hauts-de-Seine', c[c.code_departement == '92']),
               ('Seine-Saint-Denis', c[c.code_departement == '93']), ('Val-de-Marne', c[c.code_departement == '94']),
               ('France', c)]:
    t = d['etp_enseignants_hommes_et_femmes'].sum()
    r = {'territoire': nom, 'colleges': len(d), 'etp_enseignants': round(t, 1)}
    for k, v in cols.items():
        r[k] = round(100 * d[v].sum().sum() / t if isinstance(v, list) else 100 * d[v].sum() / t, 1)
    rows.append(r)
out = pd.DataFrame(rows)
out.to_csv('data/raw/recoupements/seine_saint_denis_paris/calculs_enseignants_2026-10-05/statuts_colleges_publics_2024.csv', index=False, sep=';')
print(out.to_string(index=False))
