"""Graphiques du rapport (PNG, dans resultats/figures/).

Palette catégorielle de référence (ordre fixe validé, cf. compétence dataviz) ; texte en encre neutre ;
grille fine et discrète ; écart blanc de 2 px entre segments empilés ; étiquettes de valeur sélectives.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from commun import BRUT, RESULTATS  # noqa: E402

FIG = RESULTATS / "figures"
FIG.mkdir(exist_ok=True)
SURFACE, ENCRE, ENCRE_2, GRILLE = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e1"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "text.color": ENCRE, "axes.labelcolor": ENCRE_2,
                     "xtick.color": ENCRE_2, "ytick.color": ENCRE_2, "axes.edgecolor": GRILLE,
                     "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE})


def eur(x: float) -> str:
    return f"{x:,.0f}".replace(",", " ") + " €"


def habiller(ax, axe="x"):
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRILLE)
    ax.grid(axis=axe, color=GRILLE, linewidth=0.8, linestyle="-")
    ax.set_axisbelow(True)
    ax.tick_params(length=0)
    fmt = matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", " "))
    (ax.xaxis if axe == "x" else ax.yaxis).set_major_formatter(fmt)


def titre(fig, t, sous_titre, source):
    fig.text(0.01, 0.97, t, fontsize=13, fontweight="bold", va="top")
    fig.text(0.01, 0.915, sous_titre, fontsize=9.5, color=ENCRE_2, va="top")
    fig.text(0.01, 0.015, source, fontsize=7.5, color=ENCRE_2, va="bottom")


etab = pd.read_csv(RESULTATS / "B1_depense_publique_par_etablissement_2025.csv", sep=";", low_memory=False)
dec = pd.read_csv(RESULTATS / "D1_decomposition_par_poste.csv", sep=";")
c3 = pd.read_csv(RESULTATS / "C3_comparaison_A_B.csv", sep=";").set_index("niveau")
b2 = pd.read_csv(RESULTATS / "B2_agregats_et_distribution.csv", sep=";")

# ------------------------------------------------------------------ Figure 1 : décomposition par poste
GROUPES = {
    "Enseignants (salaires, pensions, remplacement, formation)": [
        "Enseignants affectés dans les établissements (salaires et pensions)",
        "Remplacement et formation des enseignants"],
    "Autres personnels (vie scolaire, AESH, direction, ATSEM, agents)": [
        "Vie scolaire (CPE, assistants d'éducation)", "Direction, administration et encadrement pédagogique",
        "AESH, santé et service social scolaires, orientation",
        "Personnels des collectivités (ATSEM, agents d'entretien et de restauration)"],
    "Bâtiments et équipement (construction, réparations, entretien, énergie)": [
        "Bâtiments : construction, rénovation, grosses réparations, équipement",
        "Entretien, énergie et fluides des bâtiments"],
    "Activités et fonctionnement (cantine, transports, forfaits du privé…)": [
        "Dotations et autres frais de fonctionnement (fournitures, caisses des écoles…)",
        "Restauration scolaire et activités (achats, prestations)", "Transports scolaires",
        "Actions éducatives complémentaires", "Forfait communal / départemental / régional versé au privé",
        "Forfait d'externat versé par l'État au privé, internats"],
    "Aides aux familles et administration centrale": [
        "Bourses et fonds sociaux", "Allocation de rentrée scolaire et autres (CAF…)",
        "Administration centrale et académique, examens"],
}
d = dec[dec["secteur"].eq("public + privé")]
valeurs = {deg: [round(d[(d["degre"] == deg) & d["poste"].isin(postes)]["euros_par_eleve_non_arrondi"].sum())
                  for postes in GROUPES.values()]
           for deg in ("1er degré", "2nd degré")}
fig, ax = plt.subplots(figsize=(10, 4.6))
fig.subplots_adjust(left=0.13, right=0.97, top=0.80, bottom=0.36)
for i, (deg, vals) in enumerate(valeurs.items()):
    gauche = 0
    for j, v in enumerate(vals):
        ax.barh(i, v, left=gauche, height=0.42, color=SERIES[j], edgecolor=SURFACE, linewidth=1.6)
        if v > 900:  # étiquette seulement si elle tient dans le segment
            ax.text(gauche + v / 2, i, eur(v), ha="center", va="center", fontsize=8.5,
                    color="white" if j in (0, 1, 5) else ENCRE)
        gauche += v
    total = float(b2.loc[(b2["groupe"] == "Degré") & (b2["modalite"] == deg), "depense_publique_par_eleve_€"].iloc[0])
    ax.text(gauche + 120, i, eur(total), va="center", fontsize=10, fontweight="bold")
ax.set_yticks([0, 1], list(valeurs))
ax.invert_yaxis()
ax.set_xlim(0, 13200)
habiller(ax)
ax.legend([plt.Rectangle((0, 0), 1, 1, color=SERIES[j]) for j in range(len(GROUPES))], list(GROUPES),
          loc="upper left", bbox_to_anchor=(-0.12, -0.16), ncol=2, frameon=False, fontsize=8.5)
titre(fig, "Où va la dépense publique pour un élève ? (2025, en € par élève et par an)",
      "Reconstitution établissement par établissement (approche B), public et privé sous contrat, hors apprentis.\n"
      f"Référence A hors apprentis : {eur(c3.loc['1er degré', 'A_hors_apprentis_€'])} et "
      f"{eur(c3.loc['2nd degré', 'A_hors_apprentis_€'])} (A apprentis compris, 2nd degré : "
      f"{eur(c3.loc['2nd degré', 'A_convention_DEPP_€'])})",
      "Sources : RAP 2025 (mission Enseignement scolaire), DGFiP 2025, DEPP (compte de l'éducation), "
      "data.education.gouv.fr — calculs : scripts/04 et 05")
fig.savefig(FIG / "fig1_decomposition.png", dpi=170)
plt.close(fig)

# ------------------------------------------------------------------ Figure 2 : dispersion entre établissements
def quantiles(df):
    x = df.sort_values("depense_publique_par_eleve")
    w = x["eleves"].cumsum() / x["eleves"].sum()
    return [float(x.loc[w >= q, "depense_publique_par_eleve"].iloc[0]) for q in (0.1, 0.5, 0.9)]


LIGNES = [("Écoles publiques", "1er degré", None, "public"), ("Écoles privées sous contrat", "1er degré", None, "prive_sc"),
          ("Collèges publics", None, "collège", "public"), ("Collèges privés sous contrat", None, "collège", "prive_sc"),
          ("Lycées généraux et techno. publics", None, "lycée général et technologique", "public"),
          ("Lycées polyvalents publics", None, "lycée polyvalent", "public"),
          ("Lycées professionnels publics", None, "lycée professionnel", "public"),
          ("Lycées privés sous contrat (tous types)", None, "LYCEES", "prive_sc")]
fig, ax = plt.subplots(figsize=(10, 5.2))
fig.subplots_adjust(left=0.29, right=0.95, top=0.82, bottom=0.15)
for i, (lib, deg, typ, sect) in enumerate(LIGNES):
    LYC = ["lycée général et technologique", "lycée polyvalent", "lycée professionnel"]
    filtre_type = etab["type"].isin(LYC) if typ == "LYCEES" else etab["type"].eq(typ)
    m = etab["secteur"].eq(sect) & (etab["degre"].eq(deg) if deg else filtre_type)
    p10, p50, p90 = quantiles(etab[m])
    ax.plot([p10, p90], [i, i], color=SERIES[0], linewidth=6, solid_capstyle="round", alpha=0.35)
    ax.plot(p50, i, "o", color=SERIES[0], markersize=8, markeredgecolor=SURFACE, markeredgewidth=2)
    ax.text(p90 + 250, i, eur(p50), va="center", fontsize=9)
ax.set_yticks(range(len(LIGNES)), [l[0] for l in LIGNES])
ax.invert_yaxis()
ax.set_xlim(0, 23500)
habiller(ax)
titre(fig, "La dépense publique par élève dépend surtout du niveau et du secteur (2025)",
      "Point : médiane ; trait : de 10 % à 90 % des élèves (chaque élève porte la dépense de son établissement). "
      "Valeur affichée : médiane",
      "Source : approche B (scripts/04) — budgets 2025 répartis par établissement, élèves à la rentrée 2024")
fig.savefig(FIG / "fig2_dispersion_etablissements.png", dpi=170)
plt.close(fig)

# ------------------------------------------------------------------ Figure 3 : gradient social (IPS)
b2 = pd.read_csv(RESULTATS / "B2_agregats_et_distribution.csv", sep=";")
fig, ax = plt.subplots(figsize=(10, 4.6))
fig.subplots_adjust(left=0.08, right=0.97, top=0.80, bottom=0.22)
quint = ["Q1 (plus défavorisés)", "Q2", "Q3", "Q4", "Q5 (plus favorisés)"]
largeur = 0.36
for k, (grp, lib) in enumerate((("écoles publiques × quintile d'IPS", "Écoles publiques"),
                                ("collèges publics × quintile d'IPS", "Collèges publics"))):
    v = [float(b2.loc[(b2["groupe"] == grp) & (b2["modalite"] == q), "depense_publique_par_eleve_€"].iloc[0])
         for q in quint]
    x = np.arange(5) + (k - 0.5) * largeur
    ax.bar(x, v, width=largeur * 0.92, color=SERIES[k], edgecolor=SURFACE, linewidth=1.6, label=lib)
    for xi, vi in ((x[0], v[0]), (x[-1], v[-1])):
        ax.text(xi, vi + 120, eur(vi), ha="center", fontsize=8.5)
ax.set_xticks(range(5), quint)
ax.set_ylim(0, 14500)
habiller(ax, axe="y")
ax.legend(frameon=False, loc="upper center", ncol=2, fontsize=9)
titre(fig, "Plus de dépense publique par élève dans les écoles et collèges les plus défavorisés",
      "Dépense publique par élève en 2025 selon le quintile d'indice de position sociale (IPS) de l'établissement",
      "Sources : approche B (scripts/04) ; IPS 2024-2025 (DEPP). Quintiles = 5 groupes de même nombre d'établissements ; "
      "écoles : IPS publié seulement pour 60 % des écoles publiques")
fig.savefig(FIG / "fig3_gradient_social_IPS.png", dpi=170)
plt.close(fig)

# ------------------------------------------------------------------ Figure 4 : série longue 1980-2025
s = pd.read_csv(RESULTATS / "A5_serie_longue_euros_constants.csv", sep=";")
s["an"] = s["annee"].astype(str).str[:4].astype(int)
fig, ax = plt.subplots(figsize=(10, 4.6))
fig.subplots_adjust(left=0.08, right=0.88, top=0.80, bottom=0.14)
for k, (col, lib) in enumerate((("1er_degre_€2025", "1er degré"), ("2nd_degre_€2025", "2nd degré"))):
    ax.plot(s["an"], s[col], color=SERIES[k], linewidth=2, solid_capstyle="round", label=lib)
    ax.plot(s["an"].iloc[-1], s[col].iloc[-1], "o", color=SERIES[k], markersize=8, markeredgecolor=SURFACE,
            markeredgewidth=2)
    ax.text(s["an"].iloc[-1] + 0.8, s[col].iloc[-1], f"{lib}\n{eur(s[col].iloc[-1])}", va="center", fontsize=9)
    ax.text(s["an"].iloc[0] - 0.8, s[col].iloc[0], eur(s[col].iloc[0]), ha="right", va="center", fontsize=8.5,
            color=ENCRE_2)
ax.set_ylim(0, 13500)
ax.set_xlim(1973, 2031)
habiller(ax, axe="y")
ax.legend(frameon=False, loc="lower right", fontsize=9)
titre(fig, "La dépense par élève a plus que doublé depuis 1980 dans le 1er degré",
      "Dépense moyenne par élève, tous financeurs (y c. familles et entreprises), en euros constants 2025 ; "
      "apprentis compris pour le 2nd degré",
      "Source : DEPP, Note d'Information n° 26.42 (sept. 2026), figure 7 — 2025 : données provisoires")
fig.savefig(FIG / "fig4_serie_longue.png", dpi=170)
plt.close(fig)
print("Figures écrites dans", FIG)
