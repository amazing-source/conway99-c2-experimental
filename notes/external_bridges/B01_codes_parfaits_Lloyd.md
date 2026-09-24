# B01 — Codes parfaits, théorème de Lloyd, graphes de cosets

**Source.** Berlekamp–van Lint–Seidel (1973) : srg(243,22,1,2) = graphe de cosets du code de Golay ternaire [11,6,5] (parfait) ; les 243 cosets
ont pour représentants uniques 0, les 22 vecteurs de poids 1, les 220 vecteurs de poids 2 (van Eijl, thèse 1991, §6.7 et annexe A4 ; Brouwer).
Lloyd (1957) et généralisations (Delsarte ; codes complètement réguliers, partitions équitables : arXiv 2411.09698, 2605.17376, 1903.08824) :
si un graphe Γ est quotient (par une partition équitable / un revêtement) d'un graphe Ω, les valeurs propres du quotient sont des valeurs propres de Ω.

**Problème d'origine.** Existence de codes parfaits dans H(n,q).

**Mécanisme.** (i) Un code parfait e-correcteur fait de H(n,q) un revêtement du graphe de cosets ; (ii) les valeurs propres du graphe de cosets sont
des valeurs de Krawtchouk K₁(w) = (q−1)n − q w ; (iii) la fonction indicatrice de la boule a une transformée de Fourier (polynôme de Lloyd) dont les
zéros doivent être entiers.

**Objet C2 analogue (DÉRIVÉ, vérifié sur les contrôles).** Pour srg(2m²+1, 2m, 1, 2) enraciné en x, les sommets s'identifient canoniquement
à la boule de Hamming B₂(0) ⊂ F₃^m (|B₂| = 1 + 2m + 4C(m,2) = 2m²+1) ; les adjacences forcées sont « différer d'un vecteur unité ».
m = 2 : code parfait trivial ; m = 11 : Golay ; **m = 7 : 99 n'est pas une puissance de 3, donc Conway-99 n'est pas un graphe de cosets**.
Valeurs propres de H(7,3) : 14 − 3w ∈ {14, 11, 8, 5, 2, −1, −4, −7} ; **3 n'en est pas une** (c'est le « Lloyd » de Conway-99 : il n'est quotient
équitable d'aucun H(7,3)).
Nouveaux objets : « lignes » (231 triangles) ; « défaut » δ(ℓ) = somme des trois points de la ligne dans F₃⁷ (0 pour une ligne affine) ;
« grilles » 3×3 ; **grilles passant par x ⇔ arêtes D de type sœur** (en C2).

**Test rapide.** Sur les contrôles : BvLS et Paley(9) sont « allsib » (toutes les arêtes D sœurs, toutes les arêtes s=1 sœurs) — CALCULÉ
(`logs/z7_check_controls.log`). Phase 2 : allsib à m = 7 → UNSAT en 33 s (non certifié à l'époque ; depuis, allsib est exclu par DRAT et par le lemme des étoiles (revue du 24/09, soir)).

**Verdict.** PROMETTEUR comme langage (explique pourquoi « allsib » est la configuration des cas existants). Question ouverte : quelle fraction de la
structure « de Hamming » (grilles, directions, défauts nuls) une solution à m = 7 peut-elle avoir ? → idée I-GRILLES.
