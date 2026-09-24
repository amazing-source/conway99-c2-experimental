# Représentation Z⁷ / D₇ / boule de Hamming F₃⁷ (nouvelle pour C2)

## Énoncé (DÉRIVÉ ; vérifié sur les contrôles m = 2, 11)
Pour srg(n, 2m, 1, 2) (n = 2m²+1) enraciné en x avec N(x) = mK₂ (blocs Bᵢ = {(i,0),(i,1)}) :
- (i,s) ↦ (−1)^s eᵢ ∈ Z^m ; étiquette {(i,s),(j,t)} ↦ (−1)^s eᵢ + (−1)^t eⱼ (racine de D_m) ; x ↦ 0.
  Les n sommets = les vecteurs de norme ≤ 2 de Z^m = la boule de Hamming B₂(0) ⊂ F₃^m (coordonnées dans {0,±1}) : 1 + 2m + 2m(m−1) = 2m²+1.
- Adjacences forcées (x–intérieur, intérieur–intérieur, intérieur–extérieur) = « différer d'un vecteur unité modulo 3 » (eᵢ et −eᵢ diffèrent de
  2eᵢ ≡ −eᵢ). Inconnue : les arêtes entre racines.
- Groupe des relabellisations = W(B_m) = 2^m ⋊ S_m ; l'involution C2 est σ = −1 (centrale). Orbites extérieures = 42 paires ±α = racines positives.
- Matrices du dépôt : C = coordonnées des racines représentantes ; G = CCᵀ = Gram des racines ; Sh = Gram des supports ; CᵀC = 12I₇ (D₇ est une
  trame serrée). (I) ⇔ pour chaque racine α, les voisins (racines) couvrent chaque ±e_l exactement 1 fois (l ∈ supp α) ou 2 fois (sinon) ; en
  particulier Σ_{β∼α} β = 0.
- Lignes (triangles, 231 = 7 + 84 + 140) : 7 lignes de x {x, ±eᵢ} ; 84 lignes s=1 {c, c+a, c+b} (c intérieur, {c+a, c+b} ∈ M_c) ; 140 lignes
  extérieures. Défaut δ(ℓ) = somme des 3 points dans F₃⁷ (0 ⇔ ligne affine ; une ligne s=1 est affine ⇔ ses deux racines sont sœurs).

## Cas existants = graphes de cosets de codes ternaires parfaits
- m = 11 : BvLS = graphe de cosets du Golay [11,6,5]₃ ; représentants de cosets = B₂(0) ; δ(ℓ) ∈ Golay pour toute ligne.
- m = 2 : Paley(9) = H(2,3) (code nul).
- m = 7 : 99 n'est pas une puissance de 3 ⇒ pas de code parfait ; de plus 3 ∉ {14 − 3w} = valeurs propres de H(7,3) ⇒ Conway-99 n'est pas un
  quotient équitable de H(7,3) (Lloyd).

## Grilles
Deux droites de x (blocs i, j) engendrent une grille 3×3 ⇔ les 4 racines ±eᵢ±eⱼ forment le 4-cycle des arêtes sœurs ⇔ (en C2) la paire {i,j} est
une arête D de type sœur. BvLS et Paley(9) : toutes les paires (« allsib »). À m = 7, voir le lemme S1 (`03_LEMME_S1_paires_soeurs.md`).
