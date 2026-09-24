# Résultats négatifs (gardés : chaque échec doit produire de l'information)

## N01 — Comptage des triangles signés de Γ₁ (2026-09-23) — RÉFUTÉ comme obstruction
Idée : tr(S_out³) = −420 ⇒ Σ_{triangles T de Γ₁} signe(T) = −70 ; les 140 triangles extérieurs de H se projettent en triangles de signe +1 ;
avec #tri(Γ₁) = 126 + 4n_sib + 2n_one j'ai d'abord cru obtenir 2n_sib + n_one ≥ 42, donc « allsib forcé ».
**Erreur trouvée :** un triangle extérieur de H peut contenir une arête D (exactement 2n_one + 4n_dis d'entre eux, au plus une arête D chacun) ; il se
projette alors sur un triangle du multigraphe Q utilisant une arête double, pas sur un triangle de Γ₁. Recompte exact :
#(+1) = 70 − n_one − 2n_dis, #(−1) = 140 − n_one − 2n_dis, somme = −70 **identiquement**.
Leçon : l'identité signée de degré 3 est une conséquence du modèle (comme toutes les identités de trace) ; elle ne voit pas n_sib.
Pourquoi cela paraissait presque vrai : on oublie facilement que D contribue des arêtes s=0 (types one/dis), donc des triangles extérieurs « mixtes ».

## N02 — Théorème 5.14 de van Eijl (caractères modulaires) avec G = ⟨t⟩ — sans contenu
p = 7 ne divise pas |G| = 2 : les caractères modulaires sont ordinaires ; φ(E₃) = 27(1+ε), φ(E₋₄) = 22(1+ε) ⇒ rang₇(A−3I) ∈ {δ + a + b : a,b ≤ 22} :
seulement R = R₊ + ρ ≤ 45. Rien de nouveau.

## N03 — Algèbre de Terwilliger T(x) + involution — sans contenu
t commute avec T(x). Composantes isotypiques : primaire (dim 3, mult 1), extrémité 1 « symétrique » (dim 2, mult 6), « antisymétrique » (dim 2, mult 7),
extrémité 2 (dim 1) valeurs propres 3 (mult 40) et −4 (mult 30). Traces de t : 3, +12, −14, τ₃, τ₋₄ ; tr t = 1 et χ₃(t) = 0 ⇒ τ₃ = τ₋₄ = 0,
ce qui redonne exactement Spec(Q_out), Spec(S_out) (20+20, 15+15). Le module mince n'ajoute rien.

## N04 — Borne de Hadamard sur ρ = rang₇(S−3I) — triviale
det L₋ = 7^{22−ρ} ≤ 4⁷(5/2)¹⁵ ⇒ ρ ≥ 10 ; det L₊ = 7^{27−ρ} ≤ 3⁷(10/3)²⁰ ⇒ ρ ≥ 11. Mais ρ = 7 + rang₇(S_out − 3I + 2G) et un seul mineur 4×4
non nul donne déjà ρ ≥ 11 : aucune information.

## N06 — Harmoniques des racines (I-05) — RÉFUTÉ sur le contrôle
Dans BvLS (m=11) les sous-espaces « quadratiques hors diagonale » (55), « fonctions de paires » (44), X symétrique / antisymétrique (côté impair)
**ne sont pas** invariants par Q_out / S_out (défauts d'invariance 0,21 à 0,80, `logs/harmonics_bvls.log`). Seuls les sous-espaces connus
(constantes, quadratiques diagonales ↔ −2, linéaires ↔ ker S_out) le sont. Pas de condition linéaire cachée de ce type.

## N07 — Quotient de deux paires sœurs disjointes (entrelacement de Haemers) — pas de contradiction
Partition à 10 cellules, un seul paramètre ε = #arêtes parmi les 12 racines des blocs restants : entrelacement ⇔ ε ≤ 12 ; égalité ⇔ partition
équitable (spectre {14, 3⁶, (−4)³}). Même borne par l'identité du second moment Σ_w n_C(w)² = 12|C| + 2|C|² − 2e(C). (`logs/quotient_2K2.log`)

## N08 — Orthogonalité des vecteurs propres relevés des partitions équitables π_p — pas de contradiction
Pour toute famille de paires sœurs (y compris les 21), les vecteurs propres relevés (fonctions de blocs) pour des valeurs propres distinctes sont
orthogonaux ; l'espace engendré (allsib) : 21 dim pour 3, 7 pour −4 — compatible. (`logs/equitable_orth.log`)
Leçon : la contradiction « beaucoup de paires sœurs » est **combinatoire/intégrale**, pas spectrale au niveau des fonctions de blocs.

## N05 — Identité trace–rang d'Ishida sur le carré symétrique — redonne le théorème F₂
Sur Sym²(Z⁹⁹), l'idempotent (E₃⊗E₃)^{sym} est 2-entier ; restreint aux 49 paires fixes {u, tu} il vaut Q mod 2 ; tr(t | Sym² V₃) = 27 ⇒ rang_F2 = 27 :
c'est le théorème F₂ connu. (Méthode d'Ishida épuisée pour p = 2, comme le notait la phase 2.)

## N09 — Comparaison des spécialisations de Z₂[C₂] (transfert du mécanisme C3) — vide pour une involution
Tout est dans `notes/09_TRANSFERT_C3.md`.
- Pourquoi l'idée était prometteuse : elle a tué C3 en ~1 jour.
- Ce qui se passe : F_θ = E_θZ₂⁹⁹ est libre sur Z₂[C₂] et pair. Le recollement des deux spécialisations est une anti-isométrie des formes Z/4
  (invariants de Brown opposés), soit d₊d₋ ≡ (−1)²⁷ (mod 4). Avec d₊ = 7^{ρ₊}·11 et d₋ = 7^{ρ₋}, cela donne seulement ρ₊ + ρ₋ pair.
- Pourquoi c'est structurellement vide : Milgram pour chaque morceau, plus Milgram pour le tout, impliquent le recollement ; les caractères de C₂
  sont rationnels. La contradiction C3 utilisait (i) un caractère non rationnel (forme hermitienne sur Z[ω]) et (ii) 7 ≡ 1 (mod 3). À p = 2,
  7 ≡ −1 (mod 4) est visible, et les 7-rangs inconnus absorbent le 11 venant de 𝟏.
- Autres recollements 2-adiques (module de permutation, côtés ±) : automatiquement satisfaits.
- Leçon : aucune obstruction « de genre » ne tuera C2 ; il faut des vecteurs précis (combinatoire) ou des invariants de classe.
- Sous-produit gardé : rang₇(A − 3I) impair, D₇(N₃) de type moins (indépendant de σ).

## N10 — Fréquences des sous-graphes d'ordre 7 (Reimbayev, arXiv 2608.19410) : aucune borne nouvelle sur n₃
Les 208 fréquences sont linéaires en deux paramètres libres (n₃, z₁₁). J'ai reconstruit 207 formules sur 208 depuis le PDF (fractions
éclatées) et résolu le programme linéaire « toutes les fréquences ≥ 0 » (`scripts/reimbayev7_lp.py`).
Pour (99,14,1,2) : n₃ ∈ [0, 4158] seulement, la borne déjà connue ; contraintes serrées 2n₃ ≤ z₁₁ ≤ 4n₃. Contrôles : Paley(9) donne
n₃ = 0 (correct) ; BvLS donne [0, 26 730].
Leçon : la positivité des comptages locaux jusqu'à l'ordre 7 ne force pas de grille (il faudrait n₃ < 2079, note 08).

## N11 — Étage S seul et relaxation A (S + D + sommes par bloc) : UNKNOWN après 7 h (nuit du 23 au 24/09)
Modèle validé sur le vrai BvLS (m = 11). CP-SAT : 12 fils × 40 min, 3 fils × 20 min (symétrie cyclique d'ordre 7 imposée), puis 4 et 2 fils
× 7 h. kissat : 2 graines × 7 h (≈ 155 M de conflits chacune). BreakID : 0 générateur (les encodages de cardinalité cassent la symétrie
syntaxique).
Leçon : l'étage S n'est pas le « maillon faible » facile. Une attaque par le calcul exigerait de casser les symétries à la main (W(B₇),
d'ordre 322 560 effectif) et de découper en cubes, soit des jours de calcul. C'est le régime du dépôt C3 « calcul », qui n'a pas conclu.
