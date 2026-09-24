# Les grilles 3×3 d'un srg(99,14,1,2) sont des codes parfaits (ensembles intrigants de valeur propre 3)

(Résultat général : ne dépend pas de l'involution. Étiquette : DÉRIVÉ, preuve complète ci-dessous ; cohérence spectrale vérifiée par calcul exact.)

**Antériorité (vérifiée le 2026-09-23).** G1 est une application immédiate du lemme de Wilbrink–Brouwer sur les sous-graphes induits d'un srg
(cité et utilisé par Lou–Murin, *On the strongly regular graph of parameters (99,14,1,2)*, MIT PRIMES 2014, texte local
`downloads/lou_murin_primes_2014.txt`) : pour la grille (N = 9, M = 18, tous les degrés 4) le membre de gauche vaut
(99−9) − (126−36) + 18 + 2(36−18) − 9·6 = 0, d'où x₀ = x_{≥3} = 0. Lou–Murin démontrent (Th. 2.1) que « grille moins une arête ⇒ grille induite » ;
ils **n'excluent pas** les grilles et n'énoncent pas G1 sous cette forme (code parfait / ensemble intrigant). Ce qui semble propre à ce laboratoire :
l'énoncé « k ∈ {4,14} », la lecture comme ensemble intrigant et ses conséquences (partition à 18 cellules, identité sur g, Gram des grilles), et
le lien avec C2 (grilles par x ⇔ paires sœurs, lemme S1).

## Théorème G1
Soit Γ un srg(n,k,1,2) et Λ ⊂ Γ un sous-graphe isomorphe à K₃×K₃ (grille : 9 sommets, 6 droites). Alors tout sommet z ∉ Λ a **au plus un**
voisin dans Λ. Donc |Λ ∪ N(Λ)| = 9 + 9(k−4), et **Λ ∪ N(Λ) = V(Γ) ⇔ k² − 18k + 56 = 0 ⇔ k ∈ {4, 14}**.
Pour Conway-99 (k = 14) : chaque sommet hors d'une grille a exactement un voisin dans la grille.
Pour BvLS (k = 22) : 9 + 162 = 171 < 243, simple empilement (cohérent avec le lemme S1, densité 1/2).

*Preuve.* Si z ∉ Λ est adjacent à deux points colinéaires de Λ (même ligne ou colonne), z est un voisin commun de deux sommets adjacents ; λ = 1 et le
troisième point de leur droite est déjà ce voisin commun, dans Λ : contradiction. Si z est adjacent à deux points non colinéaires y, y' de Λ, leurs deux
voisins communs (μ = 2) sont les deux autres coins du carré de Λ contenant y, y' : contradiction. Chaque sommet de Λ a k−4 voisins hors de Λ, tous
distincts. ∎

## Corollaires (k = 14)
1. A χ_Λ = 3χ_Λ + 1, donc **χ_Λ − (1/11)𝟏 ∈ V₃** : Λ est un ensemble intrigant (type « positif ») du quadrangle partiel PQ(2,6,2).
2. Partition équitable à 18 cellules : les 9 sommets de Λ et les 9 ensembles F_y = N(y) ∖ Λ (10 sommets chacun). Pour z ∈ F_y :
   1 voisin dans F_y, 1 dans F_{y'} (y' colinéaire à y), 2 dans F_{y'} (y' non colinéaire), 1 dans Λ. Quotient de spectre {14, 3⁹, (−4)⁸} (calcul exact
   par blocs K₃×K₃ : paires (a,f) = (4,13) → {14,3} ; (1,−2) et (−2,1) → {3,−4}).
3. Pour deux grilles : ⟨χ_Λ − 𝟏/11, χ_Λ' − 𝟏/11⟩ = |Λ∩Λ'| − 9/11 ; la matrice de Gram de toutes les grilles est semi-définie positive de rang ≤ 54.
   Ex. : au plus 11 grilles deux à deux disjointes.
4. Tout ensemble intrigant T de type −4 (χ_T − |T|/99 ∈ V₋₄) rencontre chaque grille en exactement |T|/11 points.
5. Soit g(y) = nombre de grilles contenant y, N = nombre total de grilles. Alors g − (N/11)𝟏 ∈ V₃, i.e. **Σ_{z∼y} g(z) − 3g(y) = N pour tout y**.

## Lien avec C2 (DÉRIVÉ)
- Grilles contenant x ⇔ grilles σ-invariantes ⇔ paires de blocs sœurs (arêtes D de type sib). n_sib = g(x) ; N ≡ n_sib (mod 2).
- Identité en x : N = n_sib + 2 Σᵢ g'(eᵢ) où g'(eᵢ) = grilles par eᵢ ne passant pas par x.
- Une grille Λ ne contenant pas x donne un vecteur w = χ_Λ − χ_{σΛ} ∈ V₃ anti-invariant, i.e. (dans la base des orbites) un **vecteur propre de S à
  coefficients 0, ±1 et de support ≤ 9** pour la valeur propre 3 : un vecteur court du réseau N₊ = Z⁴⁹ ∩ V₃(S) (det 7^ρ). Pont entre I-01 et I-03.
- Le lemme S1 (`03_…`) est le cas particulier « grille par x » vu depuis x.

## Questions ouvertes (à attaquer)
- Q-G1 : borner N (ou n_sib) par un argument de Gram / d'intersection. Les grilles par x seules ont un Gram défini positif (21 max : valeurs propres
  350, 154, 44 en unités 1/11) : pas de contradiction.
- Q-G2 : existe-t-il un ensemble intrigant naturel de type −4 dans C2 ? (Taille divisible par 11 dès qu'une grille existe.)
- Q-G3 : expliquer pourquoi plusieurs grilles par x « disjointes » (paires sœurs disjointes) sont vite contradictoires (données E1–E5).
