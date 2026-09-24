# 16 — Relaxations de moments du modèle C2 : degré 2, puis triangles de degré 3 (24/09/2026)

Plan relayé (« à prendre avec des pincettes »). Construire une relaxation SoS/Lasserre de degré 2 sur les arêtes « libres »,
symétrisée, avec les contraintes multipliées. Si elle est réalisable, comprendre pourquoi et monter d'un cran de façon ciblée.

Scripts :
- `scripts/sos2_orbits.py` : tailles par Burnside ;
- `scripts/sos2_relax.py` : degré 2 ;
- `scripts/sos3_triangles.py` : ajoute les triangles de degré 3 ;
- `scripts/sos_all.sh` : campagne complète.

Journaux : `logs/sos2_orbits.txt` et `logs/sos_relax_summary.txt`.

Solveurs : cvxpy 1.9.3 + Clarabel 0.11.1 (point intérieur), installés dans `.venv`. Un seul fil, priorité minimale, environ 20 s par
résolution à m = 7.

## 0. Résumé

- **Correction de la prémisse.** Les inconnues ne sont pas 210 variables mais **1722** variables binaires (à t près). 210 est le nombre
  de *vraies* arêtes de type II à t près. Détail au §1.
- **CALCULÉ.** Symétrisée par W(B₇), la relaxation de degré 2 compte 4 moments d'ordre 1 et 142 moments d'ordre 2 distincts. La
  contrainte PSD se ramène à une matrice 243 × 243 (représentation régulière de l'algèbre commutante, de dimension 234 + 9).
- **CALCULÉ (livrable 3).** À m = 7, la relaxation de degré 2 est **réalisable** : les équations laissent un espace affine de
  dimension 35, et y_sœur ∈ [0, 1] tout entier.
  - Raison structurelle : au degré 2, l'équation du srg entre deux racines ne voit que Σ_w Q_uw Q_wv + Q_uv. **λ et μ y sont
    fusionnés.**
  - Étalonnage : le degré 2 réfute m = 3, mais pas m = 4, 5, 6, alors que ces graphes n'existent pas. Il est aveugle à l'intégralité
    des multiplicités.
- **CALCULÉ.** Premier cran ciblé : les moments de triangles de degré 3 (λ séparé de μ, Sherali-Adams de niveau 2 sur les
  triangles).
  - Il réfute m = 3 et **m = 4**.
  - Mais m = 5, 6 et **7 restent réalisables**, et y_sœur ∈ [0, 1] encore.
  - En particulier, **« allsib » passe**, alors que kissat le réfute en 18 s avec une preuve DRAT vérifiée.
- **Réponse à la question directrice.** Au degré 2, aucune information de second ordre au-delà des marges n'a de pouvoir. La première
  couche informative est la séparation λ/μ (degré 3, triangles), et elle ne suffit ni pour m = 7 ni même pour allsib.

## 1. Les variables exactes (correction)

Les inconnues sont les orbites sous t des paires de racines {u, w}, avec w ≠ u et w ≠ −u. Ce sont les variables a/b du modèle
d'orbites (`orbit_sat.py`).

| Type de paire | Variables à t près | Arêtes vraies à t près |
|---|---|---|
| partagent une demi-étiquette (couplages locaux M_h ; dont 42 paires sœurs) | 462 | 42 |
| partagent un bloc, sans étiquette commune | 420 | environ 42, selon les arcs sœurs |
| supports disjoints | 840 | environ 168, selon les arcs sœurs |
| **total** | **1722** | **252** (dont 210 de type II) |

Une racine a 12 voisines racines :
- 2 par ses deux droites intérieures (type I) ;
- 10 de type II. Génériquement, 2 partagent un bloc et 8 ont un support disjoint.

## 2. Symétrisation (DÉRIVÉ) et tailles (CALCULÉ)

Si une solution Q existe, ses images par les réétiquetages de la carte, g ∈ W(B₇) = 2⁷⋊S₇ (qui contient t = −1), sont aussi des
solutions. La loi uniforme sur ces images est une vraie distribution. Ses moments sont W(B₇)-invariants et satisfont **toutes** les
contraintes, y compris les contraintes multipliées. On peut donc imposer l'invariance sans rien supposer sur la solution elle-même.

Tailles, par Burnside sur les 110 classes de conjugaison de W(B₇) :

| Objet | Nombre |
|---|---|
| orbites de variables | 4 : paires sœurs, étiquette partagée, bloc partagé, supports disjoints |
| orbites de paires ordonnées de variables (dimension de l'algèbre commutante, Σ m_λ²) | 234 |
| orbites de paires non ordonnées (moments d'ordre 2 distincts) | 142 |

**Réduction PSD.** Soient B_k les matrices d'orbites et p_kj^i les constantes de structure. La matrice des moments X = Σ x_k B_k
(taille 1723) est PSD si et seulement si Σ x_k L_k ⪰ 0, avec L_k[i,j] = p_kj^i √(n_i/n_j), taille 243 (de Klerk–Pasechnik–Schrijver).
Les p_kj^i se lisent sur un représentant par orbite, sans aucun produit de matrices.

## 3. Relaxation de degré 2

**Variables.** y_e = E[x_e] et Y_ef = E[x_e x_f], par orbites.

**Contraintes.**
- x_e² = x_e.
- (R) Σ_w Q_uw = 12.
- (I) #{w ∋ c, w ~ u} ∈ {1, 2}.
- Chaque (R) et chaque (I) **multiplié par chacune des 1722 variables** (E[x_f L] = c_L E[x_f]).
- (P) Σ_w Q_uw Q_wv + Q_uv = 2 − |u ∩ v|, qui inclut la contrainte D (cas v = −u).
- Sherali-Adams de niveau 1 : 0 ≤ Y_ef ≤ y_e, y_f et Y_ef ≥ y_e + y_f − 1.
- PSD.

Au total : 372 équations distinctes, de rang 208 sur 243 moments.

| m | Graphe | Degré 2 |
|---|---|---|
| 2 | Paley(9) existe | réalisable, y_sœur = 1 forcé (grille) ✓ |
| 3 | n'existe pas | **irréalisable** ✓ |
| 4, 5, 6 | n'existent pas (intégralité) | réalisable : aveugle |
| **7** | ? | **réalisable** : résidus ≤ 3·10⁻¹¹, λ_min(PSD) ≥ −2·10⁻⁹, espace affine de dimension 35, y_sœur ∈ [0, 1] |

(m = 11, BvLS, n'est pas testé : 12 000 variables, l'énumération des orbites de paires est hors de portée ici. Mais le contrôle positif
m = 2 et le contrôle négatif m = 3 fonctionnent.)

**Pourquoi c'est automatiquement cohérent (DÉRIVÉ + CALCULÉ).**
- Au degré 2, la seule contrainte quadratique est (P), qui ne voit que la *somme* Σ_w Q_uw Q_wv + Q_uv.
- Rien ne distingue « u ~ v avec exactement 1 − |u ∩ v| voisins communs racines » de « u ≁ v avec 2 − |u ∩ v| ». Le distinguer
  exige de multiplier (P) par x_uv, ce qui est de degré 3.
- Les contraintes multipliées ne portent que sur (R) et (I), qui sont linéaires.
- Les moments de paires d'arêtes disjointes ne sont donc liés que par des sommes en étoile et par la PSD. Il reste 35 degrés de
  liberté, assez pour satisfaire la PSD.

## 4. Premier cran ciblé : triangles de degré 3

**Ajout.**
- z_T = E[x_uv x_uw x_vw] pour chaque triangle de racines, à t près.
- (P_adj) : E[x_uv Σ_w x_uw x_wv] = (1 − |u ∩ v|) E[x_uv]. Une arête a exactement 1 − |u ∩ v| triangles de racines ; la partie μ s'en
  déduit.
- Sherali-Adams de niveau 2 sur chaque triplet : les 8 probabilités d'atomes sont ≥ 0.

À m = 7 : 45 920 triangles de racines à t près, en **16 orbites**, et 4 équations (P_adj) distinctes.

| m | Degré 2 + triangles |
|---|---|
| 2 | réalisable ✓ |
| 3 | **irréalisable** |
| 4 | **irréalisable** (le degré 2 ne le voyait pas) |
| 5 | réalisable : violation ≤ 2·10⁻⁸, y_sœur ≈ 0 |
| 6 | réalisable |
| **7** | **réalisable** : violation maximale 3·10⁻⁸, PSD comprise ; y_sœur ∈ [0, 1] |

**Étalonnage décisif.** y_sœur = 1 est le cas allsib : les 42 arcs sœurs sont présents et les 7 blocs sont tous sœurs deux à deux.
Kissat le réfute en 18 s (preuve DRAT vérifiée, note 06). La relaxation « degré 2 + triangles » le laisse passer. La réfutation
d'allsib utilise donc une information d'ordre plus élevé que les triangles.

## 5. Les autres axes du plan

- **B (trois points, Terwilliger raffiné).**
  - Les triplets (x, u, v) : les comptes de voisins communs sont de degré 2 en Q, donc déjà contenus dans le §3.
  - Les triplets de racines : c'est exactement le §4 pour les triangles.
  - Il ne reste que des moments de triplets non triangulaires, de degré 3 en général.
- **C (Gram des vecteurs de défaut des carrés D).** Pour une structure D fixée, les r_i sont linéaires en Q. ||Σ r_i||² ≥ 0 est donc
  une conséquence de la PSD de degré 2. Comme le degré 2 est réalisable même à y_sœur = 1 (allsib, structure D entièrement fixée),
  l'axe C ne peut pas réfuter allsib. Il est trop faible.
- **D (monter de façon ciblée).** Fait pour les triangles (§4). Crans suivants, par coût croissant :
  1. multiplier (P) par les x_f des arêtes voisines (triplets en chemin) ;
  2. Sherali-Adams de niveau 3 sur les configurations locales ;
  3. Lasserre de niveau 2 localisé : matrice des moments indexée par {1, x_e, x_e x_f avec e, f partageant une racine}.

  Il faut alors compter les orbites de quadruplets. Taille et temps de résolution : c'est ici que le matériel devient limitant.

## 6. Suite proposée

1. **Étalonner sur allsib** : trouver le plus petit cran de relaxation qui le réfute. La preuve DRAT et le noyau UNSAT (745 contraintes)
   existent déjà ; leur analyse dirait quel « degré » la réfutation utilise vraiment. Un cran qui ne tue pas allsib ne tuera pas C2.
2. **Si le matériel le permet** : Lasserre de niveau 2 localisé, symétrisé, d'abord sur allsib puis sur le modèle général.
3. **Garder** : l'outil de symétrisation (orbites, représentation régulière). Il est réutilisable tel quel pour tout cran supérieur.
