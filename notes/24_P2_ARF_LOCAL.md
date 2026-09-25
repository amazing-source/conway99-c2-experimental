# 24 — Le niveau p = 2 est vide, invariant d'Arf compris (25/09/2026, session principale C2, régime sans solveur)

**Place dans le labo.** Cette note **confirme N09 et les notes 09–10 (23/09)** : la transposition de C3 est vide pour une
involution, et les méthodes de genre sont épuisées. Je l'avais refaite au §23 du carnet principal sans savoir que ce labo existait.
Apports propres, modestes :
- le critère « det ≡ 1 + f/v (mod 4) » est une tautologie (il équivaut à f pair) ;
- une formule **locale** de l'invariant d'Arf, Arf(Λ_θ ⊗ Z₂) = w̃·w̃/2, contrôlée dans 50 cas sur 50 ;
- pour Λ₋₄, cet Arf redonne σ_S ≡ 1 (mod 8), qui est déjà combinatoire.

Scripts : `scripts/e1_arf_local.py` et `scripts/e1b_unit_parts.py`.

**Hypothèses communes.** Γ est un srg(v,k,λ,μ) avec v impair et des valeurs propres entières r, s telles que r − s soit impair ;
alors E_θ est 2-entier pour θ ∈ {r, s}. On note f = dim E_θ et Λ_θ = Z^v ∩ E_θ. σ est un automorphisme d'ordre 2 dont le seul
point fixe est x. On note R = Z₂[C₂].

## 1. DÉRIVÉ : Λ_θ ⊗ Z₂ est unimodulaire pair, donc det Λ_θ ≡ (−1)^{f/2} (mod 4) (sans σ)
- *Unimodulaire* : E_θ est 2-entier, donc Λ_θ ⊗ Z₂ = E_θ Z₂^v est un facteur direct orthogonal de Z₂^v.
- *Pair* : w = E_θ 1 est caractéristique (x·w = x·1 ≡ x·x mod 2), et w = 0 puisque θ ≠ k.
- Un Z₂-réseau unimodulaire pair est une somme de plans H (dét −1) et d'au plus un plan anisotrope (dét 3). Son déterminant est
  donc (−1)^{f/2} (Arf 0) ou 5·(−1)^{f/2} (Arf 1) modulo 8.

Pour Conway 99 : det Λ₃ = 7^α·11 et det Λ₋₄ = 9·7^α. Le point 1 redonne « α pair », c'est-à-dire le Théorème A. Les
invariants d'Arf globaux valent 1 pour Λ₃ (3 ≡ 5·(−1)) et 0 pour Λ₋₄.

## 2. DÉRIVÉ : le critère du §23 est une tautologie
Avec σ, le module Λ_θ ⊗ Z₂ est R-libre (Krull–Schmidt : Z₂j absorbe le facteur trivial Z₂e_x). Donc f est pair et
tr(σ | E_θ) = 0, ce qui s'écrit a(σ) = k (OBSERVÉ 25 fois sur 25). Le critère du §23 dit det_impair ≡ 1 + f/v (mod 4). Or,
f étant pair et v impair, 1 + f/v ≡ 1 + f ≡ (−1)^{f/2} (mod 4). C'est exactement le point 1 : **ce critère n'exclut jamais
rien.**

## 3. DÉRIVÉ + OBSERVÉ : formule locale de l'invariant d'Arf
Soit V = Λ_θ/2Λ_θ, avec q(y) = y·y/2 mod 2 et b(y, z) = y·z mod 2.
- L = (1 + σ)V est un lagrangien pour b, car (1+σ)y·(1+σ)z = 2(y·z + y·σz).
- Sur L, q((1+σ)y) = y·y + y·σy ≡ y·σy ≡ y_x (mod 2).
- Si w̃ vérifie (1 + σ)w̃ = E_θ e_x, alors b(w̃, (1+σ)y) = y_x : w̃ représente q restreinte à L.
- Lemme d'algèbre linéaire (base symplectique adaptée à L) : si c représente q|_L, alors Arf(q) = q(c).

D'où **Arf(Λ_θ ⊗ Z₂) = w̃·w̃/2 (mod 2)**, avec w̃ = E_θ w̃₀ et w̃₀ = (E_xx/2)e_x + Σ_{u∈Rep} E_ux e_u. Rep contient un
représentant par σ-orbite ; le résultat ne dépend pas de ce choix.

*Observé :* valeur globale (tirée de det mod 8) = valeur locale dans les **50 cas sur 50**, dont 17 où l'invariant d'Arf vaut 1 (et 33 où il vaut 0).
Les graphes : Paley(q²), q = 3, 5, 7, 11, 13 ; les graphes de réseaux L_m(n), n = 5, 7, 11, 13 ; BvLS.

## 4. DÉRIVÉ : pour Conway 99, l'invariant d'Arf ne dit rien de neuf
Notations : e₁ = arêtes entre représentants intérieurs et extérieurs, e₂ = arêtes entre représentants extérieurs.
Dans les deux cas, 1ᵀw̃₀ = 0.
- θ = 3 : q(w̃) = (3675 + 4e₂ − 18e₁)/41503 ≡ 1 (mod 2) quels que soient e₁ et e₂. Cela vaut automatiquement l'Arf global 1.
- θ = −4 : q(w̃) = (1813 − e₂ + 8e₁)/27783 ≡ 1 + e₂. L'Arf global 0 impose donc **e₂ impair**.
  - e₂ mod 2 ne dépend pas des représentants : changer celui de U fait varier e₂ de Σ_W S_UW, somme de 10 termes ±1.
  - Comme a = (Q + S)/2, Σ_{U<W} Q_UW = 42·12/2 = 252 et tr S_out = 0, on obtient e₂ = 126 + σ(S_out)/4.
    Donc e₂ est impair ⟺ σ(S_out) ≡ 4 (mod 8) ⟺ σ_S ≡ 1 (mod 8) (convention du §0, où ΣC = 42).
  - C'est exactement l'identité du §4 du carnet principal, redémontrée combinatoirement (n₋ pair).

**Bilan.** Rang, discriminant, puis invariant d'Arf : à p = 2, tout est soit tautologique, soit déjà combinatoire. Cela
concorde avec le no-go de « structures » : il faudrait une relation sans terme J congrue modulo un premier impair.

## 5. OBSERVÉ (piste D2) : les parties unités séparées
u₊ = partie impaire de det Λ⁺ et u₋ = partie impaire de det Λ⁻, lues modulo 8. On a trois paires de graphes non isomorphes de
mêmes paramètres : Paley(25) et L₃(5), Paley(49) et L₄(7), Paley(121) et L₆(11). Dans chaque paire, les deux graphes donnent
les mêmes (u₊, u₋). Cela va dans le sens d'une conjecture : les données 2-adiques hermitiennes seraient fonction des seuls
paramètres. Si elle se démontre, c'est un no-go 2-adique définitif pour C2.
