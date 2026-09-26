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
