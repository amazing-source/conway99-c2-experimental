# B02 — p-rangs, nombres de Frame, algèbres d'adjacence modulaires

**Sources.** C.A. van Eijl, *On the p-rank of the adjacency matrices of strongly regular graphs* (mémoire, Eindhoven 1991 ; base de Brouwer–van Eijl,
J. Algebraic Combin. 1 (1992)) — texte local `downloads/vaneijl_thesis.txt` ; arXiv 2512.06541 (nombres de Frame, radicaux de Jacobson des schémas
de géométries partielles).

**Problème d'origine.** Calcul des p-rangs de A + τI ; détection des p non semi-simples.

**Mécanisme.** Rang déterminé par les paramètres sauf si p | (r−s) ; bornes : induced subgraphs (minorants), rang ≤ min(f,g)+1 (majorant) ;
Théorème 5.14 (van Eijl) : si G ≤ Aut Γ, les multiplicités des caractères modulaires dans les espaces propres bornent le p-rang.

**Analogue C2 (DÉRIVÉ).** p = 7 = r − s. Sur Z₍₇₎, 2 est inversible donc Z₍₇₎⁹⁹ = (invariant) ⊕ (anti-invariant) et
rang₇(A − 3I) = R₊ + ρ (+1 pour J) avec R₊ = rang₇(Q̂ − 3I), ρ = rang₇(S − 3I) ; R₊, ρ ≤ 22.
Le théorème 5.14 avec G = ⟨t⟩ (p ∤ |G|) donne exactement cela et rien de plus (VÉRIFIÉ à la main : φ(E₃) = 27·1 + 27·ε, φ(E₋₄) = 22·1 + 22·ε).

**Test.** Contrôle m = 11 (p = 3, d = 9) : rang₃(S − 4I) = 35, SNF 3-adique de 4I−S : 1³⁵ 3¹⁰ 9¹⁰ (CALCULÉ, `logs/z7_check_controls.log`).

**Verdict.** Aucun contenu nouveau pour un groupe d'ordre 2 (RÉFUTÉ comme source d'obstruction directe). Reste : l'invariant ρ lui-même (voir B05).
