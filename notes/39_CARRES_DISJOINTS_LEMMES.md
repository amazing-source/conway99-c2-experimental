# 39 — Carrés disjoints : premiers lemmes structurels, à la main (26/09/2026)

Cadre : Σ = ∅. L'orbite U de la paire P = {i,j} a pour représentant u = (i,α)(j,β). Son partenaire D est l'orbite W d'une paire
**disjointe** R = {k,l}, avec w = (k,γ)(l,δ), u ~ w et u ~ σw. Le carré est Q = (u, w, σu, σw), et c'est un 4-cycle **induit**, car
u ≁ σu et w ≁ σw.

## Lemme 39.1 (sommets d'apex)
On note c₁ le troisième point de la droite (u,w) et c₂ celui de la droite (w,σu). Les apex de Q sont c₁, c₂, σc₁, σc₂.
- (a) Les quatre apex sont des **racines**. Aucun ne contient l'un des sommets intérieurs (i,α), (j,β), (k,γ), (l,δ) de u ou de w.
- (b) **Quasi-perfection.** Tout sommet y ∉ Q a au plus un voisin dans Q, sauf les 4 apex, qui en ont exactement 2.
- (c) 40 sommets ont exactement 1 voisin dans Q, et 51 n'en ont aucun.

*Preuve.*
- (a) Un sommet intérieur voisin de u et de w serait un sommet intérieur commun, or les blocs sont disjoints. x n'est voisin d'aucune
  racine. Supposons que c₁ contienne (i,α). Alors c₁ ~ (i,α) et c₁ ~ u, donc c₁ = m_i(u), et {u, (i,α), c₁} est une droite. Mais
  {u, w, c₁} en est une autre, donc u et c₁, qui sont adjacents, auraient deux voisins communs, w et (i,α), contre λ = 1. On raisonne de
  même pour (j,β), (k,γ), (l,δ), et pour c₂ (droite (w,σu), sommets intérieurs de w et de σu).
- (b) Si y a deux voisins non adjacents dans Q, par exemple u et σu, alors y ∈ N(u) ∩ N(σu) = {w, σw}, donc y ∈ Q. Si ce sont deux
  voisins adjacents, par exemple u et w, y est l'unique voisin commun c₁. Trois voisins dans Q en contiendraient deux non adjacents.
- (c) Σ_{y∉Q} |N(y) ∩ Q| = 4·(14 − 2) = 48. Les apex en prennent 8, et les 91 autres sommets hors de Q en prennent 40. ∎

## Lemme 39.2 (les apex vus depuis x)
Un apex c est une racine. Tous ses voisins intérieurs sont hors des 4 sommets intérieurs de u et de w (39.1(a)). Donc :
- soit c est dans une paire disjointe de P ∪ R ;
- soit c contient (i,−α), (j,−β), (k,−γ) ou (l,−δ). Dans ce cas, c est le π correspondant : c = π_i(u), π_j(u), π_k(w) ou π_l(w).
  En effet, par μ, c est l'unique voisin de u (ou de w) contenant ce sommet opposé.

En particulier, un apex qui rencontre le bloc i est π_i(u) : **l'arête R_i de U vers l'orbite de π_i(u) est alors une arête d'apex.**
C'est une première liaison entre le graphe libre (19.1) et la géométrie du carré disjoint.

## Comptes de droites (rappel, carnet §14 et notes 23–29)
- Chaque carré D contient exactement 2 orbites de droites portant une arête D. Un carré « un bloc » donne 1 droite intérieure et
  1 droite de racines. Un carré disjoint donne 2 droites de racines.
- Il y a 112 orbites de droites hors de x (42 intérieures, 70 de racines), dont 42 portent une arête D. Les traces (tr S³, tr S⁴) sont
  indépendantes des types : **aucune obstruction linéaire**, comme attendu.

## Suite (à la main)
Chercher une contrainte de parité ou de comptage qui relie n_dis, le nombre de carrés disjoints, aux cycles libres (19.1 avec boucles
possibles quand n_s = 1). Ce sont ces liaisons qui détermineront la taille de l'énumération des squelettes « avec carrés disjoints ».

## Lemme 39.3 (boucle ⇒ doublement disjointe)
Si n_s(P) = 1, **les deux orbites de P sont de type dis**.

*Preuve.* Soit ρ = (i,α)(j,−β) la racine sœur voisine de u. Si U était « un bloc » via i, on aurait m_i(u) = v, un sommet du carré D.
Or m_i(u) est l'unique voisin de u contenant (i,α), c'est-à-dire ρ. Donc D(U) serait l'orbite sœur (carré sib), contre Σ = ∅. Le cas
« via j » est symétrique, avec π_j(u) = ρ. La sœur U′ se traite de même, par la boucle σρ ~ σu. ∎

Hexagone des coins (note 23 §1.1) : u – ρ – z′ – σu – σρ – z – u. Le sommet de lien z (second voisin commun de u et σρ) ne contient
**aucun** sommet intérieur des blocs i et j : c'est un voisin lointain commun de u et de σρ. (En raisonnant sur les droites par
(j,β) et (i,−α), on exclut que z contienne (j,β), (i,−α), (i,α) ou (j,−β).)

## Lemme 39.4 (équilibre en un bloc sans paire « à moitié »)
En un bloc k, les étiquettes X_k se partagent en deux parties :
- M_k : les orbites appariées via k ;
- F_k : les orbites libres en k (ancrées ailleurs, tordues ou mixtes via l'autre bloc, ou de type dis).

μ_k = τ_k sur M_k, qui est donc stable. Si **aucune paire en k n'a exactement une orbite appariée via k** (pas de paire tordue ni mixte
« via k »), σ préserve M_k. Alors M_k et F_k sont des réunions de composantes de G_k. Sur F_k, les composantes sont les blocs des
composantes connexes du graphe libre R_k (sœurs identifiées).

## Configurations « AD » (paires ancrées et paires doublement disjointes seulement)
Aucun bloc n'y a de paire à moitié, donc 39.4 s'applique partout. On note out_k, d_k (ancrées en k) et dis_k (paires dd en k), avec
d_k + out_k + dis_k = 6. Le nombre d'orbites libres en k vaut f_k = 2(out_k + dis_k).
- **Queue** (24.1 appliqué à un carré de pivot i, bras j et k) : la composante de i dans G_k est contenue dans F_k et compte ≥ 3
  blocs. Donc **d_k ≤ 3 dès que out_k ≥ 1**, avec la version 24.2 : d_k ≤ 3 − [k → j].
- **d_k ≠ 1** (boucle D, c'est-à-dire sib). **d_k ≠ 5** : f_k = 2, soit deux sœurs seules, impossible par 19.1, même avec une boucle,
  puisqu'il faudrait π_k ailleurs.
- **d_k = 4** entraîne out_k = 0 et dis_k = 2, et les deux paires dd en k **ont une boucle** (n_s = 1). En effet, avec f_k = 4, un 4-cycle
  formé de deux paires de sœurs à n_s = 0 donnerait deux voisins communs.
- Un bloc A (d = 6) force out ≥ 1, donc d ≤ 3, pour tous les autres blocs.
- Carré dis (X ⊂ {i,j}, partenaire W ⊂ {k,l}) : dans G_k, la composante de l (dans F_k) compte ≥ 2 + [i ∈] + [j ∈] blocs, puisque x y
  voit w, σw et ses intérieurs.
- n_dd = 0 redonne les configurations ancrées, mortes par 24.3.

**Statut** : lemmes PROUVÉS. Ils ne suffisent pas encore à tuer les AD à la main. Ils bornent leur énumération par les degrés, comme
la queue l'a fait pour les ancrées. Suite : combiner avec les cycles libres à boucles et le partenariat disjoint entre paires dd.
