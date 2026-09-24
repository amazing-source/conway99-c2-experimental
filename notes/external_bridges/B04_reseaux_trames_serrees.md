# B04 — Réseaux entiers, trames serrées entières, réseaux unimodulaires impairs

**Sources.** Conway–Sloane (SPLAG ch. 16–19 ; « The unimodular lattices of dimension up to 23 ») ; résumé (recherche web) : *il n'existe aucun réseau
unimodulaire impair de minimum ≥ 3 en dimension ≤ 22* ; O₂₃ (réseau de Leech court) unique en dim 23. Sustik–Tropp–Dhillon–Heath (ETF : intégralité
des valeurs propres de la matrice de signature ⇒ conditions arithmétiques sur (d,N)).

**Mécanisme.** Une matrice de Gram entière G avec G² = cG est une trame serrée ; le réseau engendré a un déterminant contrôlé ; la classification des
réseaux (genre, symboles p-adiques, formules d'« oddity », minimum) contraint l'existence.

**Objet C2 (DÉRIVÉ, nouveau pour C2).** Comme J s'annule sur la partie anti-invariante, l'involution fournit deux **réseaux entiers** :
- L₋ : Gram 3I − S (rang 22) engendré par 42 vecteurs de norme 3 (extérieurs) et 7 vecteurs orthogonaux de norme 4 (intérieurs), produits scalaires ∈ {0,±1} ;
  (3I−S)² = 7(3I−S) : **trame serrée de constante 7** ; det L₋ = 7^{22−ρ}, 7L₋^# ⊂ L₋.
- L₊ : Gram S + 4I (rang 27), 42 vecteurs de norme 4, 7 de norme 3 ; det L₊ = 7^{27−ρ}.
- Partenaires N± = Z⁴⁹ ∩ V± (det 7^ρ), recollés en Z⁴⁹ par (Z/7)^ρ. ρ = rang₇(S−3I).
- Dans les coordonnées où les vecteurs intérieurs sont 2eᵢ (L₋), la projection d'un vecteur extérieur sur R⁷ est −α_U/2 (demi-racine de D₇) :
  le réseau projeté est ½D₇.
Borne de Hadamard (DÉRIVÉ) : ρ ≥ 11 — mais triviale en pratique (équivaut à un mineur 4×4 non nul de S_out − 3I + 2G mod 7).

**Test rapide.** Contrôle m = 11 : réseaux analogues gouvernés par le premier 3 (constructions de type A sur des codes ternaires projectifs issus du dual
du Golay) — cohérent avec B03. Si ρ = 22 alors L₋ serait unimodulaire impair de dim 22, donc (Conway–Sloane) contiendrait des vecteurs de norme 1 ou 2 :
pas une contradiction en soi.

**Verdict.** Objet nouveau et exact, mais aucune contrainte trouvée pour l'instant. À garder : calcul du minimum et des vecteurs courts de L± sur des
solutions partielles / relaxations ; question « quelles valeurs de ρ sont possibles ? » (I-7ADIQUE).
