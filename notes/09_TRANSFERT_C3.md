# 09 — Transfert du mécanisme C3 (comparaison des spécialisations) à C2

**Origine : NON INDÉPENDANTE.** L'idée vient de la lecture, demandée par l'utilisateur, du dépôt `conway99-c3-experimental`
(preuve Lean de « pas d'automorphisme d'ordre 3 »), comparé au dépôt `conway99-c3` (approche par calcul). Clones dans `external_c3/`.

**Verdict.** Pour une involution, le mécanisme est **vide** (RÉFUTÉ comme obstruction, raison structurelle au §2). Il laisse un
sous-produit **indépendant de σ** (§3, DÉRIVÉ) : pour tout srg(99,14,1,2), rang₇(A − 3I) est impair.

## 0. Le mécanisme C3, en une ligne (ÉTABLI dans C3, formalisé en Lean)
E₃Z₃⁹⁹ est un Z₃[C₃]-module libre muni d'une forme unimodulaire. Ses deux spécialisations (caractère trivial → Z₃ ; caractère ω → Z₃[ω],
hermitienne) coïncident modulo (1−ω) : elles ont donc le même discriminant dans F₃*/F₃*².
Or d₁ = 7^a·11 ≡ 2, parce que le 11 vient de ⟨𝟏,𝟏⟩ = 33 et ne vit que du côté invariant. De l'autre côté, d_ω = 7^j ≡ 1.
Contradiction, parce que **7 ≡ 1 (mod 3)** rend les puissances de 7 invisibles et que **11 ≡ −1 (mod 3)** n'est pas un carré.

## 1. Le cadre 2-adique pour C2 (DÉRIVÉ)
- E₁₄ = J/99, E₃ = (A−14I)(A+4I)/(−77) et E₋₄ = (27I − 9A + J)/63 sont tous 2-entiers. Donc Z₂⁹⁹ = Z₂𝟏 ⊥ F₃ ⊥ F₋₄ orthogonalement,
  chaque morceau étant unimodulaire.
- N_θ = Z⁹⁹ ∩ V_θ est **pair** (tout vecteur entier ⊥ 𝟏 a une norme paire) et 2-unimodulaire. On a det N₃ = 7^ρ·11 et det N₋₄ = 7^ρ·9.
- Z₂⁹⁹ ≅ Z₂ ⊕ Z₂[C₂]⁴⁹ comme module de permutation. Krull–Schmidt donne alors **F₃ ≅ Z₂[C₂]²⁷ et F₋₄ ≅ Z₂[C₂]²²**, qui sont libres.
- Pour un module libre, F^σ = (1+σ)F. Donc (N_θ^±, b/2) est unimodulaire en 2. On le vérifie sur les contrôles (P3 ci-dessous).
- F_θ = {(u,u′) ∈ P₊×P₋ : φ(ū) = ū′}, avec b = (h₊ ⊥ h₋)/2. Comme F_θ est **pair**, φ est une anti-isométrie des formes à valeurs dans Z/4
  (h(u,u) mod 4). Pour les invariants de Brown, cela donne β(h₊) + β(h₋) ≡ 0 (mod 8).
- Traduit en déterminants (rang 27, impair) : d₊·d₋ ≡ (−1)²⁷ (mod 4), avec d₊ = 7^{ρ₊}·11 (le 11 vient de 𝟏, qui est invariant) et d₋ = 7^{ρ₋}.
  **C'est l'analogue exact de la contradiction C3, et il donne seulement ρ₊ + ρ₋ pair.**
  La raison : 7 ≡ −1 (mod 4) est visible modulo 4 (alors que 7 ≡ 1 mod 3), si bien que les 7-rangs inconnus absorbent le 11.

## 2. Pourquoi c'est vide pour une involution (DÉRIVÉ)
- La formule de Milgram, appliquée séparément à L^± = (N_θ^±, b), fixe β± en fonction des données aux premiers impairs.
  Le recollement β₊ + β₋ ≡ 0 équivaut alors à la formule de Milgram pour N_θ **tout entier**, qui ne fait pas intervenir σ.
- Raison générale (HEURISTIQUE solide) : les caractères de C₂ sont rationnels. Les deux spécialisations sont des Z-réseaux ; les formules de
  produit de chaque morceau et du tout impliquent le recollement. En C3, la spécialisation ω est hermitienne sur Z[ω] et porte un invariant
  supplémentaire (d_ω modulo les normes), que les genres de Z-réseaux ne voient pas. C'est là que la contradiction C3 trouve sa prise.
- Autres recollements vérifiés, et tous automatiquement satisfaits :
  - côté invariant : (Z₂⁹⁹)^σ ≅ ⟨1⟩ ⊥ ⟨2⟩⁴⁹ ⊇ ⟨99⟩ ⊥ M₃⁺(2) ⊥ M₋₄⁺(2), qui donne oddité(M₃⁺) + oddité(M₋₄⁺) ≡ 3 (mod 8). Cela découle de
    l'anti-isométrie 7-adique D₇(L₃⁺) ≅ −D₇(L₋₄⁺) ;
  - côté anti-invariant : M₃⁻ ⊥ M₋₄⁻ ≅ Z₂⁴⁹.
- **Conclusion.** Le couple (Z⁹⁹, σ) avec les données C2 (27+27, 22+22) est cohérent au niveau des genres équivariants dès que la condition du §3
  est remplie. Aucune obstruction de type « genre » ne peut tuer C2 : il faut des vecteurs précis (e_x, les 99 projections, les grilles),
  donc de la combinatoire, ou des invariants de classe (séries thêta).
- Rappel (ÉTABLI) : |Aut Γ| ∈ {1,2,3} dans la littérature (carte 00). Si la preuve C3 est validée, il ne reste que {1,2}.

## 3. Sous-produit indépendant de σ (DÉRIVÉ ; antériorité non trouvée)
**Proposition.** Pour tout srg(99,14,1,2), soit ρ = dim_{F₇} D₇(N₃).
1. rang₇(A − 3I) = rang₇(A + 4I) = 1 + ρ.
2. **ρ est pair.** Donc rang₇(A − 3I) est **impair**.
3. La forme discriminante D₇(N₃), espace quadratique sur F₇ de dimension ρ, est **de type moins** (non hyperbolique).
   Autrement dit : ρ ≡ 0 (mod 4) ⇒ discriminant non carré ; ρ ≡ 2 (mod 4) ⇒ discriminant carré.
4. Forme concrète : D₇(N₃) est le quotient non dégénéré de F₇⁹⁹ muni de la forme 2A + I − J (0 sur la diagonale, +1 sur les arêtes, −1 sur les
   non-arêtes), de rang ρ.

**Preuve.**
- (1) Réduction de Smith sur Z₇𝟏 ⊥ U, avec U = Z₇⁹⁹ ∩ 𝟏^⊥ unimodulaire en 7 (car 99 est premier à 7). Sur U, A − 3I = −7E₋₄, d'image 7N₋₄*.
  Le rang modulo 7 vaut dim D₇(N₋₄) = dim D₇(N₃).
- (2) N₃ est un réseau pair, 2-unimodulaire, de rang 54 = 2·27. Tout réseau pair unimodulaire sur Z₂ de rang 2m est une somme de H et de E,
  donc de déterminant ≡ (−1)^m (mod 4). Or det N₃ = 7^ρ·11 ≡ (−1)^{ρ+1} (mod 4), d'où ρ pair.
  - Le 11 : D₁₁(N₃) ≅ −D₁₁(Z𝟏) = −⟨99⟩ = Z/11, d'unité −9.
  - Pas de 3 : E₃ est 3-entier.
- (3) Formule de l'oddité pour N₃ : 54 + (6ρ + 4k₇) + (10 + 4) ≡ 0 (mod 8), puisque (−9/11) = −1. On obtient k₇ ≡ ρ/2 + 1.
  Or (−1/7) = −1, donc l'espace est hyperbolique ssi disc = (−1)^{ρ/2}. C'est exactement ce qui est exclu.
- (4) Les classes c_v = [11E₃e_v] engendrent D₇(N₃), et 7·b(c_u,c_v) = 847·E₃[u,v] ≡ 0 / 1 / −1 (mod 7).

**Contrôles** (`scripts/milgram_check.py`, `logs/milgram_check.txt`, graphes réels) :
- P1 (N_θ pair), P2 (det ≡ (−1)^{f/2} mod 4) et P4 (formule de l'oddité via ma décomposition de Jordan p-adique) : ✓ sur Paley(9), T(7),
  L₂(7) et Paley(49). Paley(49) a les mêmes valeurs propres 3 et −4 que le graphe 99.
- P3 ((N_θ^±, b/2) à déterminant impair) : ✓ pour les trois involutions à un seul point fixe. Échoue, comme attendu, pour T(7), θ = −2
  (involution à 3 points fixes : l'hypothèse n'est pas remplie).
- P5 (rang_p = 1 + dim D_p) : ✓ sur T(7) à p = 5.
- **Vraie prédiction testée sur T(7)** (l'analogue exact : 𝟏 donne Z/7 d'un seul côté, et r − s = 5). La formule prédit ρ₅ + k₅ impair.
  On observe ρ₅ = 6 et k₅ = 1 (discriminant non carré, type moins) : ✓.

**Antériorité.** La thèse de van Eijl (1991) ne contient que la parité des 2-rangs (lemme 3.9). La note N02 du labo borne rang₇ ≤ 45.
Je n'ai pas trouvé la parité de rang₇ pour (99,14,1,2), mais c'est un argument classique (Stickelberger / oddité) : à vérifier avant d'en faire état.

Notation C2 (N02) : R = R₊ + ρ_S, où ρ_S = rang₇(S − 3I). Donc **R₊ + ρ_S est impair**.

## 4. Ce que ça enseigne
- La prise de C3 tenait à trois ingrédients : un caractère **non rationnel** (hermitien), un vecteur asymétrique (𝟏, d'où le 11) et une
  coïncidence arithmétique (7 ≡ 1 et 11 ≡ −1 mod 3). Pour C2, le premier ingrédient manque, par construction.
- Pour tuer C2, il faut dépasser le genre :
  1. la classe du réseau. Par exemple, le réseau pair √77·N₃*, de rang 54 et de niveau 77, contient 198 vecteurs de norme 42 : série thêta
     dans M₂₇(Γ₀(77), χ), à la Bannai–Munemasa–Venkov. SPÉCULATION, lourd.
  2. l'exploitation du **type moins** : tout sous-espace de D₇(N₃) totalement isotrope forcé par la combinatoire est de dimension ≤ ρ/2 − 1.
     Les indicatrices de grilles tombent dans le radical (11E₃g = 11g − 𝟏 ∈ N₃) et ne donnent donc rien.
