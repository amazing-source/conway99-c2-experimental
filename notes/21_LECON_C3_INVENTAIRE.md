# 21 — D'où vient l'étincelle C3, et l'inventaire C2 fait à sa manière (24/09/2026, soir)

**Origine : NON INDÉPENDANTE.** À la demande explicite de l'utilisateur (« check c3 now »), lecture seule de
`external_c3/conway99-c3-experimental` (JOURNAL, IDEES, notes/P1_recollement.md). Rien n'y a été modifié.

## 1. L'étincelle C3, telle que leur journal la raconte (ÉTABLI dans C3 ; preuve formalisée en Lean)

1. **D'abord un inventaire.** Le registre des idées commence par deux listes.
   - Ce qui était épuisé : τ = 6 par la trace, certificats de Farkas, 46 classes de phases, énumérations, étage quotient par SAT
     (sans solution), modèle complet (indécis).
   - Ce qui n'avait **jamais servi** : discriminants, réseaux propres, droites du quadrangle partiel, rangs modulaires autres que la
     trace, arithmétique de ℤ[ω] au-delà de la définition de M.
2. **Une question : « quel invariant après le rang ? »**
   - La preuve de τ = 6 ne lit que la trace du module libre E₃ℤ₃⁹⁹ ≅ ℤ₃[C₃]¹⁸. L'invariant suivant d'un module hermitien libre est son
     discriminant, une unité de ℤ₃[C₃].
   - Ses deux spécialisations (caractère trivial → Q ; caractère ω → M d'Eisenstein) sont donc congrues modulo 1 − ω.
3. **Le calcul.**
   - Côté Q : d₁ = 7ᵃ·11ᵇ avec b impair, parce que le 11 vient de ⟨𝟏,𝟏⟩ = 33, qui n'existe que du côté trivial. D'où d₁ ≡ 2 (mod 3).
   - Côté M : d_ω = 7ʲ ≡ 1 (mod 3).
   - Version élémentaire : la même forme (Q + I) mod 3, de rang 18, aurait pour discriminant 2 d'un côté et 1 de l'autre.
4. **La discipline.**
   - Chaque piste est notée en potentiel (1–5) et en coût de réfutation (minutes → jours). D1 valait 5 en potentiel et 1 en coût.
   - Avant d'y croire, ils l'ont attaquée : graphes réels T(6)…T(18), environ 1 660 réseaux aléatoires, balayage des paramètres de
     srg jusqu'à v = 1300. Le critère n'exclut que 7 jeux, tous d'existence inconnue.
   - Ensuite seulement : une preuve élémentaire, puis la formalisation Lean. **Aucun solveur dans la preuve finale.**

Ce qu'il y a de « génial » : une question systématique (monter d'un cran dans les invariants) et le bon bagage (les spécialisations
d'une unité d'anneau de groupe sont congrues modulo le premier ramifié). La part de chance est arithmétique : 7 ≡ 1 (mod 3) rend
invisibles les puissances de 7 inconnues, alors que 11 ≡ 2 (mod 3) reste visible.

## 2. Transfert à C2 : déjà fait (notes 09–10), et fermé au niveau des genres

- Pour p = 2, la comparaison simple des discriminants est **vide**. Les formes tordues par l'opérateur (invariants de Brown) donnent
  seulement des **parités** : rang₇(S − 3I), rang₇(S_out − 3I), rang₇(Q_out − 3I) et ρ₊ sont pairs.
- Il n'y a pas de contradiction : 7 ≡ −1 (mod 4) est visible modulo 4, et les 7-rangs inconnus absorbent tout défaut. C'est l'inverse
  de la chance de C3.
- Les caractères de C₂ sont rationnels : pas de forme hermitienne sur ℤ[ω], pas d'invariant modulo les normes.
- **Verdict de la note 09** (HEURISTIQUE solide ; la note 09 le range à tort sous un titre DÉRIVÉ, revue du 24/09) : aucune
  obstruction de type genre ne tue C2. Il faut des **vecteurs précis** (e_x, les 99
  projections, les grilles), donc de la combinatoire, ou des invariants de classe.
- Une prise reste ouverte (note 10 §4) : un calcul **indépendant** qui forcerait l'imparité d'un des 7-rangs ci-dessus tuerait C2.

## 3. L'inventaire C2, à la manière de C3

**Épuisé.**
- Spectres, p-rangs (F₂ : 20 et 27 ; F₃ : 22), formes de Smith en 2 et 3, oddité et Brown (notes 09–10).
- Burnside, Tate, idempotent F₂ (note 20, idées 1–4).
- Modèle complet, étage Q seul, étage S seul (7 h de CP-SAT, 158 M conflits kissat) : UNKNOWN.
- Système χ et système signé : lemme des étoiles (ingrédients DRAT, recollement à la main), 10 survivants.
- Moments et SOS (note 16), types locaux R2 (note 15).
- Problème local de l'étoile libre (note 20) : formulation compacte ; tous les solveurs calent.

**« Jamais utilisé » — liste CORRIGÉE à la revue du 24/09 (soir) : cinq des sept pistes étaient déjà dans le labo.**

| # | piste | P | C | remarque |
|---|---|---|---|---|
| J1 | ~~Grilles = codes parfaits~~ **ERREUR : déjà utilisé.** C'est G1 (note 04, l. 13–22, k ∈ {4, 14}, soit m ∈ {2, 7} et non « seulement m = 7 »), ingrédient explicite du lemme des étoiles (note 19) | 1 | – | doublon |
| J2 | Les 7-rangs pairs (note 10), croisés avec des sous-réseaux explicites (grilles par x, droites, e_x) | 3 | 3 | **doublon** : IDEES I-03 + note 10 §4 |
| J3 | Représentation euclidienne (les 99 projections) sur des configurations imposées par Σ | 2 | 3 | **en partie déjà tenté** (note 04 l. 42–43, N07, note 01 psd_gen), sans contradiction |
| J4 | Graphes signés à deux valeurs propres (étage S seul) : littérature, bornes | 3 | 2 | **doublon** : IDEES I-11 |
| J5 | Invariant « suivant » de la formulation compacte : signes et pfaffiens des couplages μ, τ, ρ, au-delà des comptes (ii) et (iii) | 2 | 2 | l'analogue combinatoire du « après le rang » |
| J6 | MacWilliams sur le code LCD [42,20] | 2 | 1 | **doublon** : IDEES I-12, note 00 |
| J7 | Séries thêta des réseaux propres ± (invariants de classe) | 2 | 4 | **doublon** : IDEES I-27, note 09 l. 80 |

~~Choix : J1 d'abord…~~ Seule J5 est réellement neuve. L'inventaire complet, pistes tentées comprises, est dans la note 22.
