# Synthèse — laboratoire expérimental C2 (session du 2026-09-23)

Rien ici ne tranche l'existence d'un Conway-99 avec involution. Étiquettes : ÉTABLI (preuve ou calcul certifié) · DÉRIVÉ · OBSERVÉ · CONJECTURE ·
HEURISTIQUE · RÉFUTÉ. Tout le détail : `JOURNAL.md`, `IDEES.md`, `NEGATIVE_RESULTS.md`, `notes/`.

## 1. Nouvelles représentations (DÉRIVÉ)
- **Z⁷ / D₇ / boule de Hamming F₃⁷** : les 99 sommets = vecteurs de norme ≤ 2 de Z⁷ = boule B₂(0) ⊂ F₃⁷ ; extérieurs = racines de D₇ ; σ = −1 ;
  groupe W(B₇). Les deux cas existants de la famille (m = 2 et m = 11, BvLS) sont des graphes de cosets de codes ternaires **parfaits** ; m = 7 ne
  peut pas l'être (99 n'est pas une puissance de 3 ; 3 n'est pas valeur propre de H(7,3)). (`notes/02_Z7_HAMMING.md`)
- **Réseaux entiers de l'involution** : Gram 3I−S (rang 22) et S+4I (rang 27), trames serrées de constante 7, déterminants 7^{22−ρ}, 7^{27−ρ}
  avec ρ = rang₇(S−3I). (`notes/external_bridges/B04…`)

## 2. Un mécanisme propre à k = 14 (DÉRIVÉ, général — hors involution)
- **Théorème G1** : dans un srg(99,14,1,2), toute grille 3×3 est un **code parfait** (tout sommet extérieur a exactement un voisin dans la grille) ;
  dans la famille srg(n,k,1,2) cela n'arrive que pour k ∈ {4,14}. Conséquences : ensemble intrigant de valeur propre 3, partition équitable à 18
  cellules, Gram des grilles PSD de rang ≤ 54, identité Σ_{z∼y} g(z) − 3g(y) = N_grilles. Application immédiate du lemme de Wilbrink–Brouwer
  (cité par Lou–Murin 2014, qui prouvent « grille moins une arête ⇒ grille » mais n'excluent pas les grilles). (`notes/04_…`)
- **Lemme S1** (vue depuis x) : une paire de blocs « sœur » (⇔ grille par x ⇔ arête D de type sib) partitionne exactement les 40 racines
  complémentaires en 4 classes (2(m−2) = C(m−2,2) ⇔ m = 7) ; à m = 11 c'est un empilement de densité 1/2 (vérifié sur BvLS). (`notes/03_…`)
- **Prismes et n₃** : Σ c = 6·#prismes, donc c̄ = 4 − 2n₃/2079 (via Reimbayev). **n₃ < 2079 ⇒ Γ contient une grille** ; en C2, n₃/3 ≡ n_one (mod 2). Corrigé le 24/09 : l'ancien « n₃ ≡ 0 (mod 6) » était faux,
  voir la note 20.
  (`notes/08_…`)
- **Parité du 7-rang** (indépendant de σ) : N₃ = Z⁹⁹ ∩ V₃ est pair, 2-unimodulaire, de déterminant 7^ρ·11. Il en découle que **rang₇(A − 3I) = 1 + ρ
  est impair** et que D₇(N₃) est un F₇-espace quadratique **de type moins** (formule de l'oddité). Prédictions vérifiées sur 4 graphes réels.
  Antériorité non trouvée (argument classique). (`notes/09_…`)
- **Parités propres à C2** (invariants de Brown des formes b(y, f(A,P)y), cadre validé sans erreur sur 3 graphes réels) :
  rang₇(S − 3I), rang₇(S_out − 3I), rang₇(Q_out − 3I) et ρ₊ sont **pairs**. Ce sont les restes « modulo 4 » de la contradiction C3 :
  7 ≡ −1 (mod 4) absorbe tout. **Le système de genres de C2 est cohérent** : toutes les structures sont rationnelles, donc pas
  d'invariant hermitien, et la norme spinorielle est triviale. (`notes/10_…`)

## 3. Théorème certifié par ordinateur (ÉTABLI, preuves DRAT vérifiées par drat-trim)
Le graphe Σ des grilles passant par x (paires sœurs) ne contient aucune des configurations suivantes (liste en cours d'extension) :
allsib (K₇), K2+K2+P3, K3+K2+K2, K2+P5, K2+araignée, P4+P3, K1,3+P3, K3+K3, C₆, K2+K3 pendant, K₁,₁,₄, S7b, S7c et 7 graphes à 6–8 arêtes
issus de la boucle (20 preuves VERIFIED). Chaîne de confiance et empreintes : `notes/06_THEOREME_GRILLES_PAR_X.md`, `data/cert_results.txt`,
`data/cnf/MANIFEST.txt`.
**Conséquence (ÉTABLI) : Σ ∈ 53 graphes possibles, au plus 7 grilles par x.** On tombe à 50 en ajoutant K₄, S6, S7a, S8 (UNSAT solveur, sans
DRAT). La boucle a été arrêtée volontairement (changement de régime demandé par l'utilisateur).

## 4. Résultats négatifs utiles (RÉFUTÉ / sans contenu)
Triangles signés (identité toujours vraie) ; théorème de van Eijl pour G = ⟨t⟩ ; Terwilliger + involution ; harmoniques des racines (réfuté sur BvLS) ;
quotient de 2 paires sœurs (seulement ε ≤ 12) ; orthogonalité des partitions équitables ; Ishida sur Sym² ; H-COVER. (`NEGATIVE_RESULTS.md`)
**N09 — transfert du mécanisme C3** (comparaison des spécialisations de Z₂[C₂]) : vide pour une involution. Les caractères de C₂ sont
rationnels, donc le recollement équivaut à la formule de Milgram du réseau total. L'analogue exact de la contradiction C3 donne seulement
ρ₊ + ρ₋ pair, parce que 7 ≡ −1 (mod 4), alors que 7 ≡ 1 (mod 3) en C3. Leçon : **aucune obstruction de genre ne tuera C2**.

## 5. Observations (OBSERVÉ / HEURISTIQUE)
- Paramètres de Krein entiers pour m = 2, 11 (existants), dénominateur 49 pour m = 7, 56, 497 (ouverts) ; les cas ouverts sont exactement 7 | d.
- Configurations à ≤ 3 grilles par x, « une seule grille exactement », motifs « tout one » / « tout dis » : indécis à 10–15 min (non concluant).

## 6. Suite proposée
0. (Après N09) Les obstructions arithmétiques « de genre » sont épuisées pour C2. Ce qui reste : des vecteurs précis (grilles, e_x, les 99
   projections), des invariants de classe (série thêta du réseau pair √77·N₃*, niveau 77), ou un comptage qui force des grilles (n₃ < 2079).
1. (Arrêtée) Boucle de réduction de Σ : 53 graphes survivants certifiés ; reprise possible si l'on veut l'énoncé final « Σ ∈ {liste} ».
2. Preuve humaine : noyau UNSAT minimisé (339 → ~177 contraintes pour K2+K2+P3, en cours) ; connexion D₄ (`notes/05_ALLSIB_STRUCTURE.md`).
3. Découper le cas sib par le type exact de Σ (≤ 57 sous-cas) avec kissat + DRAT.
4. Chercher un analogue de G1 pour les carrés D de type one/dis (le vrai cœur du problème : cas one et dis).

## Salve « reset » du 24/09 : t comme réflexion ponctuelle (notes 11 à 14)
- **Mouvement** : t n'est plus une symétrie par laquelle on quotiente, c'est la réflexion ponctuelle σ_x d'une famille (σ_v) définie en
  tout sommet. C2 = « Hall en un seul point ».
- **Mécanisme externe exact** : Hall 1960 et Bondarenko–Radchenko 2013 (réflexions automorphes ⇒ affine sur F₃ ⇒ 3^m). L'étape de
  propagation échoue pour une raison de dimension : 14 sur 44, soit un résidu de dimension 30. Le lemme manquant (P) est formulé
  (note 14, §3).
- **DÉRIVÉ** :
  - théorème R1 sur les grilles hors de x (note 11) ;
  - « translation partout » ⇒ allsib, donc impossible ;
  - défauts de Hall en x, H1 à H5 : σ_v(x) = σ_x(v) seulement sur les 4n_sib ≤ 28 coins sib ; au plus 28 droites D-fermantes sur 42 ;
    multiplicité des milieux ;
  - Lefschetz sur X_Γ ;
  - aucune coclique de Delsarte t-invariante.
- **Réfuté ou vide** :
  - Krein gradué à deux points (N12) ;
  - existence de grille via les fréquences d'ordre 7 (N10) ;
  - Ishida sur quatre modules (N14) ;
  - Hamming local, Makhnev 1988, Cameron, intersections triples (N15).
- **Ouvert** : conjecture R2 (vraie dans BvLS, où tout est sœur, donc indice faible) ; J_x ; SDP du résidu.

## Note 15 (24/09) : R2 et types locaux
- **DÉRIVÉ** :
  - formule des multiplicités ;
  - R2 complète ⇒ quatre blocs distincts et motif rigide des coins, donc R2 complète est fausse avec une droite sœur ;
  - R2 complète en w ⇒ σ_w ∉ Aut.
- **OBSERVÉ (exact)** :
  - 1194 types locaux autour d'une grille hors de x ;
  - aucun élément d'ordre 3 forcé ;
  - 112 types à symétrie locale, aucune propageable en C2 (Aut = ⟨t⟩ par |Aut| ≤ 3, sans besoin de C3) ;
  - le recollement de deux grilles par une droite n'élimine aucun φ.
- **Réserve** : tout ce qui passe par les grilles laisse intact le cœur sans grille.

## Note 16 (24/09) : relaxations de moments
- **Prémisse corrigée** : 1722 variables binaires à t près (dont 210 vraies arêtes de type II).
- **CALCULÉ** :
  - le degré 2 symétrisé (243 moments d'orbite) est réalisable à m = 7, et aveugle même à m = 4, 5, 6 ;
  - l'ajout des triangles de degré 3 réfute m = 3 et m = 4, mais laisse passer m = 7 et même allsib (certifié impossible).
- **Conséquence** : la contradiction, si elle existe, est d'un ordre supérieur. Le prochain cran (Lasserre 2 localisé) demande du
  matériel.

## Note 17 (24/09) : allsib, preuve humaine
**DÉRIVÉ** : allsib est impossible. La preuve passe par la cohomologie du complexe des couplages M₇ :
- λ et μ entre paires disjointes ⇒ cocycle Z₂ ;
- H¹(M₇ ; Z₂) = 0 ⇒ cobord ;
- μ entre paires qui se coupent ⇒ équirépartition 3/3, impossible pour un cobord.

C'est la première preuve humaine d'un cas certifié, et un patron local → global réutilisable.

## Note 18 (25/09) : système χ, atomes, g07 fermé
- **ÉTABLI (DRAT)** : g07_ca15a23af4 (K₁,₆ + une arête) est impossible, par l'étage Q. C'était le dernier cas indécis de la boucle Σ.
- **Système χ** (dérivé de l'étage Q) : il classe les 1044 graphes Σ en 988 impossibles et 56 possibles, à travers 11 atomes minimaux
  certifiés par DRAT.
- Il reste **39 graphes Σ possibles**, dont le graphe vide (au plus 7 arêtes).
- **Preuves humaines** : allsib (cohomologie de M₇) ; K₃ + K₂ (lemme du triangle).

## Note 19 (24/09) : lignes, signes, lemme des étoiles
- **Système χ signé.** Le système χ, c'est exactement l'étage Q sur les lignes sœurs ; ce qui lui manque, ce sont les **signes**. Le
  modèle complet restreint aux lignes sœurs tue les 8 configurations χ-SAT certifiées ailleurs, et S6 (DRAT VERIFIED).
- **LEMME DES ÉTOILES (DÉRIVÉ, preuve humaine courte, ingrédients vérifiés par SAT).** Trois paires sœurs ne partagent jamais un bloc :
  Σ est de degré ≤ 2.
  - La preuve est une parité : 6 identités μ = 2 (Fait A) et 3 identités μ = 2 (Fait B) donnent (−1)³ = +1.
  - Elle est propre à k = 14, par G1.
  - Ses 18 ingrédients (6 Faits A, 12 Faits B éclatés) sont certifiés par DRAT.
- **Au plus 4 grilles par x (n_sib ≤ 4) et au plus 2 par droite de x.** La borne précédente était 7.
- **Modèle complet sur les petits survivants** : C₄ et P₄+K₂ sont exclus (DRAT, 495 s et 252 s). **Σ survivants : 39 → 10.**
- Avant ce dernier point, Σ survivants : 39 → 12, tous de degré ≤ 2 : ∅, K₂, P₃, 2K₂, K₃, P₄, P₃+K₂, 3K₂, C₄, P₅, P₄+K₂, 2P₃. Pour chacun, l'information
  des lignes sœurs, signes compris, est épuisée : il faut des lignes non sœurs, comme pour le cœur sans grille.
- **Cœur sans grille** : aucune obstruction locale visible jusqu'à 22 lignes. Le mécanisme de parité ne s'étend pas localement aux
  carrés D de type one.
- **Parité des orbites « − » (DÉRIVÉ, contrôlée sur BvLS).** Toute ligne a un nombre pair de voisins Q = 1 parmi les orbites
  ±(eᵢ − eⱼ). L'étage Q ne voit pas cette contrainte : il a une symétrie parasite (Z₂)²¹, et l'échange d'une paire la viole. Ce
  sont 42 XOR à ajouter à l'étage Q.
