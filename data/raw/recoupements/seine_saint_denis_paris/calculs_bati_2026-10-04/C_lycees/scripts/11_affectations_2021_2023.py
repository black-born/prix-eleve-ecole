# -*- coding: utf-8 -*-
"""Affectations votées par la Région Île-de-France en faveur des lycées, 2021-2023 (open data data.iledefrance.fr) :
- « Données budgétaires des lycées - subventions votées » (subventions aux EPLE, avec UAI) ;
- « Données budgétaires des lycées - opérations directes votées » (travaux et achats en maîtrise d'ouvrage régionale ;
  UAI renseigné pour une partie seulement : le département est alors lu dans le libellé du dossier, puis dans le nom de
  la commune ; à défaut, l'opération est « non attribuable » : accords-cadres, énergie, numérique, etc.).
Montant voté = montant affecté (autorisations de programme ou d'engagement), pas un paiement.
Rapporté aux élèves accueillis (second degré + post-bac + collégiens des cités mixtes régionales), moyenne des rentrées
2021, 2022 et 2023 (DEPP, jeu « mode d'hébergement »).
Sorties : resultats/affectations_2021_2023_par_departement.csv, resultats/operations_directes_attribution.csv
"""
import re
import sys
import unicodedata
import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 40)
pd.set_option('display.max_rows', 200)
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
IDF = ['75', '77', '78', '91', '92', '93', '94', '95']


def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode().upper()
    return re.sub(r'[^A-Z0-9]+', ' ', s).strip()


# ---------- référentiel des lycées publics (Région) : UAI -> département, commune
g = pd.read_csv(W + 'raw/IDF_opendata_lycees-donnees-generales.csv', sep=';', encoding='utf-8-sig', dtype=str)
communes = {}
for _, r in g.iterrows():
    communes[norm(r['libelle'])] = r['dep']
# variantes fréquentes dans les libellés
extra = {'EPINAY SUR SEINE': '93', 'ST DENIS': '93', 'SAINT DENIS': '93', 'ST OUEN': '93', 'LIVRY GARGAN': '93', 'NEUILLY SUR MARNE': '93',
         'AULNAY SOUS BOIS': '93', 'NOISY LE GRAND': '93', 'VITRY SUR SEINE': '94', 'VILLENEUVE LE ROI': '94', 'CACHAN': '94',
         'VINCENNES': '94', 'CHAMPIGNY': '94', 'COURBEVOIE': '92', 'SCEAUX': '92', 'BAGNEUX': '92', 'PUTEAUX': '92', 'SEVRES': '92',
         'CHATENAY MALABRY': '92', 'POISSY': '78', 'SARTROUVILLE': '78', 'VERSAILLES': '78', 'MANTES LA VILLE': '78',
         'CARRIERES SUR SEINE': '78', 'NANGIS': '77', 'FONTAINEBLEAU': '77', 'MEAUX': '77', 'VILLEPARISIS': '77', 'MONTEVRAIN': '77',
         'DAMMARIE LES LYS': '77', 'COULOMMIERS': '77', 'AVON': '77', 'DRAVEIL': '91', 'CERNY': '91', 'COURCOURONNES': '91',
         'RIS ORANGIS': '91', 'MORSANG SUR ORGE': '91', 'SAVIGNY': '91', 'BRUNOY': '91', 'ARGENTEUIL': '95', 'BEZONS': '95',
         'GONESSE': '95', 'VILLIERS LE BEL': '95', 'ENGHIEN LES BAINS': '95', 'TAVERNY': '95'}
communes.update(extra)
communes.pop('PARIS', None)
COMMUNE_KEYS = sorted(communes, key=len, reverse=True)


def dep_from_label(lbl):
    s = norm(lbl)
    m = re.match(r'^(?:PPI|PPR|PPI PPR|PPR PPI|MGP)?(?: ?\d{4})?\s*(75|77|78|91|92|93|94|95)(?:0\d\d)?\b', s)
    if m:
        return m.group(1), 'numero'
    m = re.search(r'\b(75|77|78|91|92|93|94|95)(0\d\d)\b', s)  # code postal parisien 75012...
    if m:
        return m.group(1), 'code postal'
    if re.match(r'^99\b', s):
        return 'regional', 'numero 99'
    m = re.search(r'\b(75|77|78|91|92|93|94|95)\b', s)
    if m and not re.search(r'\b(ACCORDS?|AC|MAC|CONV|P2P3PFI|PFI)\b', s):
        return m.group(1), 'numero interne'
    if re.search(r'\bPARIS\b', s) and not re.search(r'EST PARISIEN|PARIS LA DEFENSE|PARIS SACLAY', s):
        return '75', 'PARIS'
    for k in COMMUNE_KEYS:
        if len(k) >= 5 and re.search(r'\b' + re.escape(k) + r'\b', s):
            return communes[k], 'commune'
    return None, None


# ---------- effectifs accueillis (moyenne des rentrées 2021-2023)
h = pd.read_csv(W + 'raw/DEPP_fr-en-mode-hebergement-eleves-etablissements-2d_IDF_2020-2025.csv', sep=';', dtype={'uai': str, 'code_departement': str})
h['rentree'] = h['rentree'].astype(int)
S2, SUP = 'nombre_d_eleves_dans_une_formation_du_second_degre', 'nombre_d_eleves_dans_une_formation_du_superieur'
dc = pd.read_csv(W + 'resultats/dotation_consolidee_par_lycee_avec_eleves.csv', sep=';', dtype={'uai': str, 'dep': str})
c = pd.read_csv(W + 'raw/DEPP_fr-en-cites_scolaires_IDF.csv', sep=';', dtype=str)
coll = {}
for cs, gg in c.groupby('code_cite_scolaire'):
    lyc = gg[~gg['libelle_nature'].str.contains('COLLEGE', na=False)]['uai'].tolist()
    col = gg[gg['libelle_nature'].str.contains('COLLEGE', na=False)]['uai'].tolist()
    for u in lyc:
        coll.setdefault(u, []).extend(col)
lyc_uais = sum((u.split('+') for u in dc['uai']), [])
cmr_uais = sum((u.split('+') for u in dc.loc[dc['section'] == 'CMR', 'uai']), [])
col_uais = sum((coll.get(u, []) for u in cmr_uais), [])
hh = h[h['rentree'].isin([2021, 2022, 2023])]
lyc_e = hh[hh['uai'].isin(lyc_uais)].copy()
lyc_e['n'] = lyc_e[S2] + lyc_e[SUP]
col_e = hh[hh['uai'].isin(col_uais)].copy()
col_e['n'] = col_e[S2]
e = pd.concat([lyc_e, col_e])
e['dep'] = e['uai'].str[1:3]
eleves_dep = e.groupby('dep')['n'].sum() / 3
prebac_dep = lyc_e.assign(dep=lyc_e['uai'].str[1:3]).groupby('dep')[S2].sum() / 3
lycpost_dep = lyc_e.assign(dep=lyc_e['uai'].str[1:3]).groupby('dep')['n'].sum() / 3
print('élèves accueillis (moy. 2021-2023) :', eleves_dep.round(0).to_dict())

# ---------- subventions votées
s = pd.read_csv(W + 'raw/IDF_opendata_subventions-votees-pour-les-lycees.csv', sep=';', encoding='utf-8-sig', dtype=str)
s['m'] = pd.to_numeric(s['montant_vote'], errors='coerce')
print(s.groupby('type_de_decision')['m'].agg(['sum', 'count', 'min', 'max']))
s = s[s['type_de_tiers'] == 'Lycées et collèges publics'].copy()
s['dep'] = s['code_uai_ex_rne'].str[1:3]
CAT = {'Dotation globale de fonctionnement': 'DGF (fonctionnement)',
       'Maintenance, contrôles et entretien des EPLE': 'maintenance, contrôles, entretien (fonctionnement)',
       'Travaux de maintenance': 'travaux de maintenance (investissement)',
       'Equipements pédagogiques dans les EPLE': 'équipements pédagogiques (investissement)',
       'Aide régionale à la demi-pension des élèves pré et post Bac': 'aides aux familles (demi-pension, équipement)',
       "Aide régionale à l'équipement pour les élèves pré et post bac": 'aides aux familles (demi-pension, équipement)'}
s['cat'] = s['procedure_du_dossier'].map(CAT).fillna('autres subventions')
ts = s.pivot_table(index='dep', columns='cat', values='m', aggfunc='sum').fillna(0)
print(ts.round(0))

# ---------- opérations directes
o = pd.read_csv(W + 'raw/IDF_opendata_donnees-budgetaires-lycees-operations-directes.csv', sep=';', encoding='utf-8-sig', dtype=str)
o['m'] = pd.to_numeric(o['montant_vote'], errors='coerce')
print(o.groupby('type_de_decision')['m'].agg(['sum', 'count', 'min', 'max']))
rows_split = []
for _, r in o.iterrows():
    u = r['code_uai_ex_rne']
    if isinstance(u, str) and u[1:3] in IDF:
        rows_split.append({**r.to_dict(), 'dep_attribue': u[1:3], 'source_attribution': 'UAI', 'part': 1.0})
        continue
    lbl = norm(r['dossier'])
    # libellé citant plusieurs départements (ex. « 4 ETABLISSTS / PREVERT 95, DE NERVAL 95, CLAUDEL 94, LANGEVIN 91 ») :
    # montant partagé à parts égales entre les établissements cités
    multi = re.findall(r'\b(75|77|78|91|92|93|94|95)\b', lbl)
    if len(set(multi)) > 1 and not re.match(r'^(PPI|PPR|MGP)', lbl):
        for d_ in multi:
            rows_split.append({**r.to_dict(), 'dep_attribue': d_, 'source_attribution': 'plusieurs départements', 'part': 1 / len(multi)})
        continue
    d1, s1 = dep_from_label(r['dossier'])
    if d1 is None:
        d1, s1 = dep_from_label(r['objet_de_l_operation'])
    rows_split.append({**r.to_dict(), 'dep_attribue': d1 if d1 else 'non attribuable', 'source_attribution': s1 if s1 else '', 'part': 1.0})
o = pd.DataFrame(rows_split)
o['m'] = o['m'] * o['part']
o.to_csv(W + 'resultats/operations_directes_attribution.csv', sep=';', index=False, encoding='utf-8-sig')
print(o.groupby('source_attribution')['m'].agg(['sum', 'count']))
print(o.groupby('dep_attribue')['m'].agg(['sum', 'count']))
# contrôle visuel des attributions par libellé
print(o[o['source_attribution'].isin(['commune', 'numero interne', 'PARIS'])][['dossier', 'dep_attribue', 'source_attribution', 'm']].sort_values('m', ascending=False).head(60).to_string())
print(o[o['dep_attribue'] == 'non attribuable'].sort_values('m', ascending=False)[['dossier', 'm']].head(40).to_string())

# ---------- synthèse par département
od = o.groupby('dep_attribue')['m'].sum()
rows = []
for dep in IDF:
    n = eleves_dep.get(dep, np.nan)
    sub = ts.loc[dep] if dep in ts.index else pd.Series(dtype=float)
    inv_sub = sub.get('travaux de maintenance (investissement)', 0) + sub.get('équipements pédagogiques (investissement)', 0)
    rows.append({'dep': dep, 'eleves_accueillis_moy_2021_2023': n, 'lyceens_prebac_moy_2021_2023': prebac_dep.get(dep, np.nan),
                 'operations_directes_attribuees_MEUR': od.get(dep, 0) / 1e6,
                 'EUR_par_eleve_par_an_operations_directes': od.get(dep, 0) / n / 3,
                 'EUR_par_lyceen_postbac_inclus_par_an_operations_directes': od.get(dep, 0) / lycpost_dep.get(dep) / 3,
                 'EUR_par_lyceen_prebac_par_an_operations_directes': od.get(dep, 0) / prebac_dep.get(dep) / 3,
                 'subventions_investissement_MEUR': inv_sub / 1e6,
                 'EUR_par_eleve_par_an_subv_invest': inv_sub / n / 3,
                 'DGF_et_entretien_MEUR': (sub.get('DGF (fonctionnement)', 0) + sub.get('maintenance, contrôles, entretien (fonctionnement)', 0)) / 1e6,
                 'EUR_par_eleve_par_an_DGF_entretien': (sub.get('DGF (fonctionnement)', 0) + sub.get('maintenance, contrôles, entretien (fonctionnement)', 0)) / n / 3,
                 'aides_familles_EUR_par_eleve_par_an': sub.get('aides aux familles (demi-pension, équipement)', 0) / n / 3})
t = pd.DataFrame(rows)
tot_n = eleves_dep[IDF].sum()
t.loc[len(t)] = {'dep': 'IDF (attribuable)', 'eleves_accueillis_moy_2021_2023': tot_n, 'lyceens_prebac_moy_2021_2023': prebac_dep[IDF].sum(),
                 'operations_directes_attribuees_MEUR': od[IDF].sum() / 1e6, 'EUR_par_eleve_par_an_operations_directes': od[IDF].sum() / tot_n / 3,
                 'EUR_par_lyceen_postbac_inclus_par_an_operations_directes': od[IDF].sum() / lycpost_dep[IDF].sum() / 3,
                 'EUR_par_lyceen_prebac_par_an_operations_directes': od[IDF].sum() / prebac_dep[IDF].sum() / 3,
                 'subventions_investissement_MEUR': t['subventions_investissement_MEUR'].sum(), 'EUR_par_eleve_par_an_subv_invest': t['subventions_investissement_MEUR'].sum() * 1e6 / tot_n / 3,
                 'DGF_et_entretien_MEUR': t['DGF_et_entretien_MEUR'].sum(), 'EUR_par_eleve_par_an_DGF_entretien': t['DGF_et_entretien_MEUR'].sum() * 1e6 / tot_n / 3,
                 'aides_familles_EUR_par_eleve_par_an': np.nan}
print(t.round(1).to_string())
print('opérations directes non attribuables : %.1f M€ ; numéro 99 (régional) : %.1f M€ ; total : %.1f M€' % (
    od.get('non attribuable', 0) / 1e6, od.get('regional', 0) / 1e6, o['m'].sum() / 1e6))
t.to_csv(W + 'resultats/affectations_2021_2023_par_departement.csv', sep=';', index=False, encoding='utf-8-sig')
