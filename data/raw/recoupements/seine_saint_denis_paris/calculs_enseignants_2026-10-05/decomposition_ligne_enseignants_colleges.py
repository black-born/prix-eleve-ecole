# Décomposition de la ligne « enseignants » de B (part de l'État) dans les collèges publics : heures par élève × indice des corps.
# Dans B, les crédits du P141 (actions 01, 02, 03, 05, 06) sont répartis au prorata des heures d'enseignement × indice de coût
# des corps de l'établissement (H-B4, H-B5 ; scripts/04_approche_B_par_etablissement.py). Donc, pour chaque collège :
#   etat_enseignants = k × heures × indice, d'où  heures × k = etat_enseignants / indice.
# Par territoire : ligne par élève E = (Σ etat / Σ élèves) = [k × heures par élève] × [indice moyen pondéré par les heures].
# Décomposition de l'écart entre deux territoires par la méthode du point milieu (exacte pour un produit de deux facteurs).
# Source : resultats/B1_depense_publique_par_etablissement_2025.csv. Chemin relatif à la racine du projet.
import pandas as pd

b = pd.read_csv('resultats/B1_depense_publique_par_etablissement_2025.csv', sep=None, engine='python', encoding='utf-8-sig')
c = b[b['type'].eq('collège') & b['secteur'].eq('public') & b['eleves'].gt(0)].copy()
c['hk'] = c['etat_enseignants'] / c['indice_cout_enseignant']
c['etp_x_indice'] = c['etp_enseignants'] * c['indice_cout_enseignant']

def agreger(d):
    el, etat, hk = d['eleves'].sum(), d['etat_enseignants'].sum(), d['hk'].sum()
    return {'colleges': len(d), 'eleves': int(el), 'ligne_enseignants_par_eleve': etat / el,
            'facteur_heures_par_eleve': hk / el, 'indice_corps_pondere_heures': etat / hk,
            'indice_corps_pondere_etp': d['etp_x_indice'].sum() / d['etp_enseignants'].sum()}

dep = c['code_departement'].astype(str).str.zfill(2)
t = {'Paris': agreger(c[dep == '75']), 'Seine-Saint-Denis': agreger(c[dep == '93']), 'France': agreger(c)}
out = pd.DataFrame(t).T
fr = t['France']
out['heures_par_eleve_vs_France_%'] = 100 * (out['facteur_heures_par_eleve'] / fr['facteur_heures_par_eleve'] - 1)
out['indice_vs_France_%'] = 100 * (out['indice_corps_pondere_heures'] / fr['indice_corps_pondere_heures'] - 1)
print(out.round(4).to_string())

def decomposer(a, b_):
    A, B = t[a], t[b_]
    dE = B['ligne_enseignants_par_eleve'] - A['ligne_enseignants_par_eleve']
    dH = (B['facteur_heures_par_eleve'] - A['facteur_heures_par_eleve']) * (A['indice_corps_pondere_heures'] + B['indice_corps_pondere_heures']) / 2
    dI = (B['indice_corps_pondere_heures'] - A['indice_corps_pondere_heures']) * (A['facteur_heures_par_eleve'] + B['facteur_heures_par_eleve']) / 2
    return {'de': a, 'vers': b_, 'ecart_total': dE, 'effet_heures_par_eleve': dH, 'effet_corps': dI}

dec = pd.DataFrame([decomposer('Paris', 'Seine-Saint-Denis'), decomposer('France', 'Seine-Saint-Denis'),
                    decomposer('France', 'Paris')])
print(dec.round(1).to_string(index=False))
dossier = 'data/raw/recoupements/seine_saint_denis_paris/calculs_enseignants_2026-10-05/'
out.round(4).to_csv(dossier + 'decomposition_ligne_enseignants_colleges_territoires.csv', sep=';')
dec.round(1).to_csv(dossier + 'decomposition_ligne_enseignants_colleges_ecarts.csv', sep=';', index=False)

# Part de chaque corps dans l'écart d'indice Paris − Seine-Saint-Denis, en pondération par les ETP (données ouvertes DEPP,
# rentrée 2024 ; la pondération par les heures donne presque le même indice, voir ci-dessus). Avec les indices de H-B5
# arrondis : indice = indice des certifiés + Σ part du corps × (indice du corps − indice des certifiés).
INDICE = {'etp_d_enseignants_agreges': 1.233, 'etp_d_enseignants_certifies_peps': 0.947, 'etp_d_enseignants_plp': 1.024,
          'etp_d_enseignants_titulaires_d_un_autre_corps': 0.861, 'etp_d_enseignants_non_titulaires': 0.681}
p = pd.read_csv('data/raw/etablissements/personnels_2d_rentree2024.csv', sep=';', encoding='utf-8-sig', dtype={'code_departement': str})
p = p[(p.secteur == 'Public') & (p.nature_de_l_etablissement == 'Collège')]
parts = {d: p[p.code_departement == d][list(INDICE)].sum() / p[p.code_departement == d][list(INDICE)].sum().sum() for d in ('75', '93')}
ref = INDICE['etp_d_enseignants_certifies_peps']
contrib = {k: (parts['75'][k] - parts['93'][k]) * (v - ref) for k, v in INDICE.items() if v != ref}
total = sum(contrib.values())
for k, v in contrib.items():
    print(f"{k:50s} écart de part {100*(parts['75'][k]-parts['93'][k]):+5.1f} pts  contribution {v:+.4f}  ({100*v/total:.0f} %)")
print(f"total {total:+.4f} ; effet corps Paris -> 93 dans B : {dec.iloc[0]['effet_corps']:.1f} EUR, dont agreges environ {dec.iloc[0]['effet_corps']*contrib['etp_d_enseignants_agreges']/total:.0f} EUR")
