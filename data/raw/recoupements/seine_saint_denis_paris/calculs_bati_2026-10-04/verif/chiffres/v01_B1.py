# Verification independante des chiffres B1 cites dans reponse.md / section_analyse.md
import sys, pandas as pd, numpy as np
sys.stdout.reconfigure(encoding='utf-8')
B1 = r"C:/Users/chret/Documents/EtatEcole/resultats/B1_depense_publique_par_etablissement_2025.csv"
df = pd.read_csv(B1, sep=';', encoding='utf-8-sig', dtype={'code_departement': str, 'uai': str, 'code_commune_norm': str})
print(df.shape)
print(df['type'].value_counts())
print(df['secteur'].value_counts())
pub = df[df.secteur == 'public'].copy()
lines = ['etat_enseignants','etat_remplacement_formation','etat_vie_scolaire','etat_pilotage_admin','etat_inclusion_sante_social','etat_activites_educatives','etat_aides_familles','etat_forfait_prive_internats','etat_soutien_administration','ct_ecoles','ct_colleges','ct_lycees','ct_transports','etat','collectivites','depense_publique']
# check etat = sum of etat_*
etat_parts = [c for c in lines if c.startswith('etat_')]
chk = (pub[etat_parts].sum(axis=1) - pub['etat']).abs().max()
print('max |sum etat_* - etat| =', chk)
# check depense_publique = etat + collectivites + apu?
pub['apu_tot'] = pub['apu_par_eleve'] * pub['eleves']
chk2 = (pub['etat'] + pub['collectivites'] + pub['apu_tot'] - pub['depense_publique']).abs().max()
print('max |etat+collectivites+apu*eleves - depense_publique| =', chk2)
chk3 = (pub[['ct_ecoles','ct_colleges','ct_lycees','ct_transports']].sum(axis=1) - pub['collectivites']).abs().max()
print('max |ct_* - collectivites| =', chk3)
chk4 = (pub['depense_publique']/pub['eleves'] - pub['depense_publique_par_eleve']).abs().max()
print('max |dp/eleves - dp_par_eleve| =', chk4)

groups = {
 'ecoles': pub['type'] == 'école',
 'colleges': pub['type'] == 'collège',
 'lycees': pub['type'].isin(['lycée général et technologique','lycée polyvalent','lycée professionnel']),
 'lycees_GT': pub['type'] == 'lycée général et technologique',
}
terr = {'Paris': pub.code_departement == '75', '93': pub.code_departement == '93', 'France': pd.Series(True, index=pub.index)}
rows = []
for g, gm in groups.items():
    for t, tm in terr.items():
        s = pub[gm & tm]
        n = s.eleves.sum()
        r = {'groupe': g, 'terr': t, 'nb': len(s), 'eleves': n}
        for c in lines + ['apu_tot']:
            r[c] = s[c].sum() / n
        rows.append(r)
res = pd.DataFrame(rows)
pd.set_option('display.width', 250); pd.set_option('display.max_columns', 40)
print(res[['groupe','terr','nb','eleves','depense_publique','etat','etat_enseignants','ct_ecoles','ct_colleges','ct_lycees','ct_transports','apu_tot']].round(2))
# parts collectivite hors transports
for _, r in res.iterrows():
    part = (r.ct_ecoles + r.ct_colleges + r.ct_lycees) / r.depense_publique
    part_t = (r.ct_ecoles + r.ct_colleges + r.ct_lycees + r.ct_transports) / r.depense_publique
    ens = r.etat_enseignants / r.depense_publique
    ensrf = (r.etat_enseignants + r.etat_remplacement_formation) / r.depense_publique
    print(f"{r.groupe:10s} {r.terr:7s} part coll hors transp {100*part:.2f} % ; avec transp {100*part_t:.2f} % ; enseignants {100*ens:.2f} % ; ens+rempl {100*ensrf:.2f} % ; etat {100*r.etat/r.depense_publique:.2f} %")
# ecarts ecoles
e = res.set_index(['groupe','terr'])
print('ecart ecoles total Paris-93 =', e.loc[('ecoles','Paris'),'depense_publique'] - e.loc[('ecoles','93'),'depense_publique'])
print('ecart ecoles commune Paris-93 =', e.loc[('ecoles','Paris'),'ct_ecoles'] - e.loc[('ecoles','93'),'ct_ecoles'])
print('ecart colleges 93-Paris =', e.loc[('colleges','93'),'depense_publique'] - e.loc[('colleges','Paris'),'depense_publique'])
print('region line only share lycees Paris/93:', e.loc[('lycees','Paris'),'ct_lycees']/e.loc[('lycees','Paris'),'depense_publique'], e.loc[('lycees','93'),'ct_lycees']/e.loc[('lycees','93'),'depense_publique'])
# taille
for g in ['colleges','lycees_GT','ecoles','lycees']:
    for t in ['Paris','93','France']:
        r = e.loc[(g,t)]
        print(f'taille {g} {t}: {r.eleves:.0f}/{r.nb:.0f} = {r.eleves/r.nb:.1f}')
