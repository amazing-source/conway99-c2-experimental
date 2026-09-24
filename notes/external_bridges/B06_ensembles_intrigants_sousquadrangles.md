# B06 — Ensembles intrigants, sous-quadrangles « serrés », grilles

**Sources.** J. Bamberg, F. De Clerck, N. Durante, *Intriguing sets of partial quadrangles* (arXiv 0812.2871 ; texte local
`downloads/bamberg_declerck_durante_intriguing_PQ.txt`, lu) ; Bamberg–Law–Penttila (tight sets et m-ovoïdes des GQ, Combinatorica) ;
Payne–Thas (sous-quadrangles d'ordre (s,t') de GQ(s,t) : si t = s t', chaque point extérieur est colinéaire à un ovoïde du sous-quadrangle).
Attention : le résumé automatique de l'article prétendait qu'il traite PQ(2,6,2) ; **faux** (vérifié par recherche dans le texte).

**Problème d'origine.** Structure des hémisystèmes / sous-structures des GQ ; ensembles intrigants d'un quadrangle partiel.

**Mécanisme.** Un ensemble I est intrigant si χ_I − c𝟏 est un vecteur propre ; deux types (valeur propre positive / négative) ; un intrigant positif et un
intrigant négatif se rencontrent en |I||J|/n points (orthogonalité d'espaces propres). Les sous-structures « serrées » (cas d'égalité d'une inégalité
de comptage) sont intrigantes.

**Analogue Conway-99 (DÉRIVÉ, `notes/04_GRILLES_ENSEMBLES_INTRIGANTS.md`).** Toute grille 3×3 est un **code parfait** (chaque point extérieur a exactement
un voisin dans la grille) — cas d'égalité, exactement pour k = 14 dans la famille srg(n,k,1,2) — donc un intrigant positif (valeur propre 3).
Intrigants négatifs possibles (valeur propre −4) : A χ_T = a χ_T + (a+4)(𝟏−χ_T) ⇒ |T| = 11(a+4)/2, a pair :
|T| ∈ {22 (coclique de Hoffman), 33 (a = 2 : par ex. 11 droites disjointes, chaque point extérieur adjacent à 6 d'entre elles), 44, 55, 66, 77}.
Chaque grille rencontre un tel T en |T|/11 ∈ {2,…,7} points. Les « m-ovoïdes » au sens des GQ (valeur propre −(t+1) = −7) n'existent pas (−7 n'est pas
valeur propre) ; en particulier Conway-99 n'a pas d'ovoïde (33 points rencontrant chaque droite une fois).

**Test rapide.** Cohérence spectrale de la partition à 18 cellules d'une grille : OK (calcul exact). En C2 : grilles par x ⇔ paires sœurs.

**Verdict.** Pont RÉUSSI (a produit un théorème général G1). Reste à trouver une obstruction : combiner grilles (forcées ? rares ?) et intrigants
négatifs, ou exploiter le Gram des grilles.
