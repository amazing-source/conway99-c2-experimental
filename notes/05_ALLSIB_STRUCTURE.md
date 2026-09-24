# Structure de la configuration « allsib » à m = 7 (toutes les paires de blocs sœurs) — analyse à la main

Statut : DÉRIVÉ (conséquences du lemme S1) ; allsib est UNSAT pour CaDiCaL (20 s ; 3,9 s / 623 conflits avec le lemme S1 explicite) — non certifié.
But : isoler le mécanisme de la contradiction (preuve humaine souhaitée).

## 1. Une racine = un voisin par paire complémentaire
Pour toute racine β (support {k,l}), ses 10 voisins s=0 sont **exactement une racine sur chacune des 10 paires du K₅ complémentaire** (lemme S1(4)
appliqué aux 10 paires sœurs disjointes de {k,l}). Ses 5 droites extérieures forment une **quasi-1-factorisation de K₅** (la droite de direction j
utilise un couplage parfait des 4 blocs restants). C'est la « rigidité m = 7 » : 2(m−2) = C(m−2,2).

## 2. Connexion D₄ sur le graphe de Kneser KG(7,2)
Pour deux paires disjointes p, q : f_pq : P_p → P_q (α ↦ son unique voisin dans P_q) est une bijection σ-équivariante qui préserve la relation
« sœurs » : un élément du groupe diédral D₄ du carré des sœurs (4-cycle α – s₁ – −α – s₂). f_qp = f_pq⁻¹.
Pour un triple T = {p,q,r} de paires deux à deux disjointes (6 blocs, bloc manquant k) : holonomie H_T = f_rp ∘ f_qr ∘ f_pq ∈ D₄ (sur P_p).
α est sur une droite supportée par T ⇔ H_T(α) = α. Fix(H_T) est réunion de σ-paires : |Fix| = φ(T) ∈ {0, 2, 4}
(identité : 4 ; réflexion diagonale : 2 ; sinon 0) et φ(T) = nombre de droites extérieures supportées par T.

## 3. Comptage : 2-recouvrements du quadrangle GQ(2,2)
Pour (p, k) fixé (k ∉ p), les 3 triples contenant p et évitant k ont (φ) = (4,0,0) ou (2,2,0) : chaque σ-paire de P_p choisit une direction.
Pour k fixé, ψ = φ/2 est une fonction sur les 15 couplages parfaits (synthèmes) de K₆ = [7]∖{k}, à valeurs {0,1,2}, telle que chaque duade est
couverte exactement 2 fois : un **2-recouvrement des points de GQ(2,2) par ses droites** (ex. : deux fois un spread ; somme de deux spreads (ils
partagent toujours exactement un synthème) ; complémentaire d'un spread). Σ_T φ(T) = 7 × 20 = 140 = nombre de droites extérieures ✓.

## 4. Ce qui reste à trouver
La contradiction (confirmée par SAT) doit venir des conditions μ entre racines non adjacentes (non encore exploitées ici) combinées à ces holonomies.
Piste : écrire les conditions μ pour β et une racine de P_p non adjacente en termes de f (fait pour deux paires : intersections 1/2/0 selon
α = f(β), −f(β), sœurs) et chercher une incompatibilité de parité dans D₄ sur les 105 triples.
