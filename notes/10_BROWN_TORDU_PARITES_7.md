# 10 — Invariants de Brown tordus par l'opérateur : parités des 7-rangs en C2 (DÉRIVÉ, cadre validé sur 3 graphes réels)

Correction de N09 : le mécanisme C3 n'est pas « vide » pour C2. La comparaison des spécialisations avec la forme standard seule est vide.
En revanche, **les formes tordues par l'opérateur**, b_f(y,y′) = b(y, f(A,P)y′), portent de l'information. Elle est globale (formule de
l'oddité / Milgram), et un solveur ne la voit pas.

## 1. Le lemme des blocs de rang 1 (DÉRIVÉ, vérifié par calcul)
F = E_θZ₂⁹⁹ est un Z₂[C₂]-module libre muni d'une forme symétrique unimodulaire H (carte 09). On le décompose en blocs orthogonaux :
des blocs de rang 1 ⟨ρ⟩ (ρ inversible) et des blocs pairs de rang 2 (argument standard sur un anneau local).
Pour a, a′ impairs, on pose B_{a,a′} = (a·h₊ ⊥ a′·h₋)/2 = αb + βb_σ, avec α = (a+a′)/2 et β = (a−a′)/2.
- bloc ⟨ρ⟩ : β(B_{a,a′}) ≡ a·ρ(1) + a′·ρ(−1) (mod 8), par un calcul 2×2 direct ;
- bloc pair : β = 0, par une somme de Gauss (seul u ≡ 0 contribue).

**Donc β(F; a, a′) ≡ a·t₊ + a′·t₋ (mod 8)**, où t± est l'oddité de M^±_θ = (N_θ^±, b/2).

## 2. Deux calculs du même invariant
Pour f = f₀(A) + f₁(A)P, avec f_e de degré ≤ 2, f ≡ I ou f ≡ P (mod 2) hors diagonale :
- **(comb)** β(q_f) se lit sur la seule diagonale de f, qui ne dépend que de d(u, σu) ∈ {0, 1, 2}.
  Type I : Σ_u β(f_uu). Type P : β(f_xx) + 4·#{orbites avec f_vv ≡ 2 mod 4}.
- **(eig)** β(q_f) = β(⟨n·f(k,+)⟩) + Σ_{θ,ε} f(θ,ε)·t^ε_θ (mod 8).

**Validation** (`scripts/brown_twist.py`, `logs/brown_twist.txt`) : pour les t calculés directement sur les réseaux, 0 désaccord sur les
32 768 formes admissibles, sur Paley(9), L₂(7) et Paley(49) (involution à un point fixe dans les trois cas).

## 3. Conséquences pour C2 (DÉRIVÉ)
Les t^ε_θ sont donnés par la formule de l'oddité (primes 7, 11 via 𝟏, et 3 via Z/9 de 𝟏) en fonction des inconnues ρ± = dim D₇(N₃^±) et des
symboles de Legendre k±.
1. **Système complet sur Z⁹⁹** (32 768 formes) : cohérent ssi **ρ₊ ≡ ρ₋ (mod 2)**. Les k± disparaissent.
2. **Sous-réseau anti-invariant** (Z⁴⁹ avec b/2 et S), forme W = 2S + I : sa forme Z/4 est Σ(2S_ii + 1)y_i, avec 7 fois −1 (orbites intérieures)
   et 42 fois +1, donc β = 35. Or (Z₂⁴⁹, W) = M₃⁻(7) ⊥ M₋₄⁻(−7), d'où β(M₃⁻) ≡ 3 (mod 4).
   Avec la formule de l'oddité : **ρ_S := rang₇(S − 3I) est pair.**
3. **Sous-réseau invariant ⊥ 𝟏** (Gram I + 2J, forme W/2 = I + 2Q + 2J − 4(…)) : β = −35. On en tire t(M₃⁺) ≡ 1 (mod 4), donc **ρ₊ pair**.
4. **Décomposition locale, côté S** : S = [[−I₇, Cᵀ],[C, S_out]] et CᵀC = 12I. On a M₃⁻ ⊇ Z⁷(21) ⊥ M_out, avec M_out = Z⁴² ∩ ker(S_out − 3I)
   (primitifs, complémentaires). Or D₃(M_out) ≅ −(Z/3)⁷ et t(M₃⁻) = 147 + t(M_out).
   Il en résulte : **dim D₇(M_out) impair, donc rang₇(S_out − 3I) = 7 + dim D₇(M_out) est pair.**
5. **Décomposition locale, côté Q** :
   - V₋₂(Q_out) = vect{b_i − b_j} (indicatrices de blocs) est **explicite**. Q_out b_i = 4·𝟏 − 2b_i.
   - Le réseau K = Z⁴² ∩ vect(b_i) = ⟨b_i⟩ + Z𝟏 a pour déterminant 2⁷·3·5⁶. Donc D₅(K₃) ≅ (Z/5)⁶ (type non carré) et D₃(K₃) = Z/3 sont
     **connus**, où K₃ = Z⁴² ∩ V₃(Q_out).
   - Le complément de K₃ dans M₃⁺ est J₇ = {(−6Σλ, (5I−2J)λ, Bλ)}, de Gram 7(5I + 4J), de déterminant 3·5⁶·7⁷·11 et d'oddité 1.
   - Conclusion : **dim D₇(K₃) impair et rang₇(Q_out − 3I) pair**, cohérent avec ρ₊ pair (indice : 7 + ρ_Q − ρ₊ pair).
   - Le 5 est un premier nouveau dans le paysage, mais son symbole de Legendre est connu : aucune liberté, aucune contradiction.

**Bilan des parités (C2) :** rang₇(S − 3I), rang₇(S_out − 3I), rang₇(Q_out − 3I) et ρ₊ sont **pairs**. rang₇(A − 3I) = 1 + ρ₊ + ρ_S est
impair (indépendant de σ, carte 09).

## 4. Portée (HEURISTIQUE solide)
- Toutes ces parités sont des théorèmes sur **toute** solution entière de l'étage S (resp. Q), pas seulement sur un graphe complet.
  Ils ne peuvent donc pas servir de filtre à une énumération ; ils ne tueraient C2 que combinés à un calcul **indépendant** d'un 7-rang.
- Pourquoi aucune contradiction n'apparaît : à p = 2, les seuls premiers inconnus sont des 7 (7 ≡ −1 mod 4), dont les puissances absorbent
  tout défaut modulo 4. En C3, 7 ≡ 1 (mod 3) les rendait invisibles. Les données connues (11 via 𝟏, 5 et 3 via les blocs, 3 via le
  Z⁷(21) intérieur) sont toujours recollées de façon cohérente. **Le système de genres de C2 est cohérent** : aucune obstruction arithmétique
  de ce type n'existe.
- Test en cours : l'étage S seul par CP-SAT (`scripts/stage_s_alone.py`). Une solution permettrait de vérifier « rang₇(S − 3I) pair » sur un
  objet réel. Un UNSAT tuerait C2.

## 5. Pourquoi il n'y a pas de « recollement hermitien » en C2 (HEURISTIQUE solide)
- Le mécanisme C3 exige une spécialisation **non rationnelle** (caractère ω, forme hermitienne sur Z[ω]) : son discriminant, pris modulo
  les normes, est un invariant que les genres de Z-réseaux ne voient pas.
- En C2, tout est rationnel :
  - A, σ, AP et les polynômes en A et P ont des valeurs propres rationnelles ;
  - l'algèbre de Terwilliger T(x) a ses modules définis sur Q ;
  - H, Q_out et S_out aussi.
- Le recollement « à p = 7 » de Z₇[A] sur U = 𝟏^⊥ (spécialisations 3 et −4, égales modulo 7) est exactement l'anti-isométrie
  D₇(N₃) ≅ −D₇(N₋₄) : l'involution de l'anneau est triviale, donc pas d'invariant supplémentaire.
- **Conclusion** : les méthodes de genre donnent des parités (§3), jamais de contradiction. Il reste les méthodes de classe (B07 :
  défavorable, repères minces) et la combinatoire, ou le calcul : étage S seul, en cours.
