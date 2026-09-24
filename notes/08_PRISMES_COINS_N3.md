# Prismes, arêtes de coin et le paramètre libre n₃ (DÉRIVÉ — pari « grilles forcées »)

Source : R. Reimbayev, *The subgraphs of order six of the family of srg with λ=1, μ=2*, arXiv 2508.03377v2 (texte local
`downloads/reimbayev_order6.txt`). Il paramètre les 62 sous-graphes d'ordre 6 par un paramètre libre n₃ ; en particulier
n₁ = nk(k−2)/12 − n₃/3 où N₁ = **prisme** K₃×K₂ (carré avec triangles sur deux côtés opposés et troisièmes points adjacents) et N₃ = même
configuration sans l'arête entre les troisièmes points. Pour (99,14) : **P := n₁ = 1386 − n₃/3**.

## Identité des coins (DÉRIVÉ ici)
Pour un sommet y et deux droites ℓ₁, ℓ₂ par y, soit c(y;ℓ₁,ℓ₂) ∈ {0,…,4} le nombre d'arêtes entre les 4 « coins » (voisins communs hors de y des
points de ℓ₁∖y et ℓ₂∖y) formant le 4-cycle de la grille potentielle. Alors **Σ_{(y,ℓ₁,ℓ₂)} c = 6P** : chaque arête de coin p–p' en (y;ℓ₁,ℓ₂)
détermine le prisme formé de ℓ₁ et de la droite {b,p,p'} (b ∈ ℓ₂) reliées par y–b, a–p, a'–p' ; réciproquement chaque prisme donne exactement
une arête de coin en chacun de ses 6 sommets.
Il y a 99·21 = 2079 triplets (y;ℓ₁,ℓ₂), d'où la **moyenne c̄ = 6P/2079 = 4 − 2n₃/2079**.

## Conséquences
1. c ≠ 3 (Lou–Murin 2014, Th. 2.1 : « grille moins une arête ⇒ grille »). Donc si c̄ > 2, un triplet a c = 4 : **une grille existe**.
   **n₃ < 2079 ⇒ Γ contient une grille** (et alors, par G1, un code parfait à 9 points).
2. n₃ = 0 ⇔ c ≡ 4 ⇔ toutes les paires de droites engendrent des grilles (structure de Hamming, impossible à 99 sommets).
   La borne n₃ ≤ 4158 (connue) est exactement « P ≥ 0 » (c ≡ 0).
3. Sans grille : c ∈ {0,1,2} partout, donc n₃ ≥ 2079.
4. **C2** : aucun prisme n'est σ-invariant (vérifié : un prisme σ-invariant forcerait u ∼ σu pour un extérieur, ou deux droites σ-invariantes
   disjointes, or seules les 7 droites de x sont σ-invariantes) ⇒ P pair ⇒ **n₃ ≡ 0 (mod 6)**.
   Prismes passant par x ↔ transitions sœurs : #prismes(x) = S_sis = 4n_sib + 2n_half (arêtes sœurs de H), à comparer à la moyenne
   6P/99 = 84 − 2n₃/99 par sommet.
5. En x, c ∈ {0,2,4} (σ) : c̄(x) = (2n_half + 4n_sib)/21.

## Pistes
- Borner n₃ en C2 (ou en général) par un autre comptage ⇒ grilles forcées ⇒ combiner avec la rareté certifiée des grilles par x.
- Relier n₃ à des quantités C2 (types de M_c, D) par un comptage σ-équivariant des prismes.
