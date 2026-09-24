# Carte de l'état C2 (reconstruite le 2026-09-23 à partir des dépôts en lecture seule)

Sources lues : `conway99-involution` (README, LAB_INSTRUCTIONS, notes/*, report/dossier_chercheurs_fr.tex, results/*, code/z2/**)
et `conway99-lab-archive` (phase 2, sorties des probes, transcription). Aucune autre branche Conway 99 consultée
(dossiers `c3_suivi`, `other-branches-inventory/tau6*`, clone du dépôt public : non ouverts).

Étiquettes : ÉTABLI (source primaire ou preuve relue) · DÉRIVÉ (conséquence démontrée dans le dépôt) · CALCULÉ (sortie de calcul archivée) ·
REDONDANT (conséquence d'autre chose, sans contenu propre) · TESTÉ SANS SUCCÈS · SUGGÉRÉ (jamais fait).

## Niveau 0 — littérature (ÉTABLI)
- |Aut Γ| ∈ {1,2,3} (Makhnev–Minakova 2004 ; Behbahani 2009 / Behbahani–Lam 2011 ; Crnković–Maksimović 2020 ; Cesarz–Woldar 2025).
- Involution t : Fix(t) = {x} ; a₁(t) = 14 (M–M ; Ishida 2606.29183 le retrouve).

## Niveau 1 — rigidité (ÉTABLI/DÉRIVÉ, preuves élémentaires relues deux fois)
- Réduction enracinée : N(x) = 7K₂ (blocs Bᵢ), 84 extérieurs = étiquettes {(i,s),(j,e)} ; seule inconnue : H (12-régulier sur 84).
- t = σ (retournement de tous les blocs) [lemme de Makhnev] ; u ≁ σu pour u extérieur ; χ₃(t) = χ₋₄(t) = 0.
- D(u) = N(u) ∩ N(σu) est une σ-orbite ; D = couplage parfait sur les 42 orbites extérieures [propre au dépôt].

## Niveau 2 — modèle exact (DÉRIVÉ, validé : m=2 SAT+relèvement, m=3 UNSAT, contrôle fort BvLS m=11, CNF m=11 validée)
- Bits (a_UV, b_UV) ; (R) Σ(a+b)=12 ; (D) un seul (1,1) ; (I) comptes par sommet intérieur ; (P) λ/μ entre orbites. ⇔ A²+A−12I=2J.
- Q = a+b, S = a−b : modèle = Stage Q ∧ Stage S ∧ supp S = {Q=1}.
  Stage Q : Q_out ∈ {0,1,2}, un 2 (D) et dix 1 par ligne, sommes par bloc (2/4), Q_out²+Q_out = 12I+4J−Sh.
  Stage S : Cᵀ S_out = 0, S_out² + S_out = 12I − G (G = CCᵀ).

## Niveau 3 — invariants (tous DÉRIVÉS ; tous REDONDANTS avec le modèle, utiles seulement comme filtres)
- Spec(S) = {3²⁷,(−4)²²} ; Spec(S_out) = {0⁷,3²⁰,(−4)¹⁵} ; Spec(Q_out) = {12,(−2)⁶,3²⁰,(−4)¹⁵} ; partie E₂/ker = contraintes de blocs (aucune info).
- Spec(H) pour TOUT Conway-99 enraciné : {12,(−2)⁶,0⁷,3⁴⁰,(−4)³⁰} (l'involution n'ajoute rien au niveau spectral de H).
- F₂ : rang(Γ̄+Sh) = 20, Γ̄²+Γ̄ = Sh ; K = Γ̄² idempotent rang 20 ; code LCD [42,20] ⊂ (col N_b)^⊥. (Γ̄ = Q mod 2.)
- F₃ : rang_F3(S) = 22 ; rang(S_out+G) = 15 ; M = I+Q−Ĵ mod 3 idempotent de rang 27.
- Z₂, Z₃ : formes de Smith de S−θI triviales. L₃, L₋₄ libres sur Z₂[C₂] (Broué) ⇔ rang_F2 S = 27.
- Z₇ : (S−3I)² = −7(S−3I) ; 7 ≤ rang_F7(S−3I) ≤ 22. **Seul contenu p-adique non épuisé (question q:7 du dossier, jamais faite).**
- s=1/s=0 : chaque extérieur a 2 arêtes s=1 (une par élément de son étiquette) ; M_c couplage parfait sur les 12 étiquettes ∋ c ;
  les arêtes s=0 forment 140 triangles (espace linéaire partiel 84 points, 5 droites/point) ; 11 types de cycle pour M_c ; 35 560 triangles candidats.
- #triangles(Γ₁) = 126 + 4 n_sib + 2 n_one (identité de cohérence) ; (Γ²+Γ+Sh)/2 ≡ ΓD+DΓ+D (mod 2).
- c₄ = 2079 constant (vide) ; les C₄ induits σ-invariants = les 21 cycles u v σu σv avec D(u) = {v,σv}.
- Découpage sib/one/dis exhaustif ; lignes de U₀ (Stage Q) 3 436 / 36 175 / 321 878 ; cubes 13 (9 distincts) / 149 / 1 164.
  Lignes du modèle complet (phase 2, non vérifié) : 22 176 (sib), 155 904 (one).

## Niveau 4 — calculs (CALCULÉ ; aucun ne tranche)
- Modèle complet CNF : 7 × 8 h UNKNOWN (kissat/cadical). CP-SAT UNKNOWN. Stage Q 2 h ×3 UNKNOWN (kissat, CP-SAT). Cubes sib 20 min UNKNOWN.
- Relaxation signée seule (sans CᵀS_out=0) : UNKNOWN. DFS ligne à ligne : arrêt au plafond de nœuds. Recuit : plateau ≈ 1550.
- Phase 2 (non certifié) : « allsib » (les 7 M_c internes aux blocs ⇔ toutes les arêtes D de type sœur) → UNSAT en 33 s (pysat, sans preuve DRAT).
- Contrôles positifs : m = 2 (srg(9,4,1,2)) et **m = 11 (Berlekamp–van Lint–Seidel, srg(243,22,1,2), involution x ↦ −x)** : table exacte disponible
  (`data/bvls_table_m11.json`). **Toute obstruction proposée doit échouer sur m = 2 et m = 11.**

## Niveau 5 — suggéré, jamais fait (SUGGÉRÉ)
- q:gen générateur ordonné (entrelacement + nauty) ; q:orbit énumération des Q_out ; q:cas exclure sib à la main ;
  q:code MacWilliams sur le code LCD ; q:7 contenu 7-adique ; q:ishida version « forme quadratique » ; q:parite parités d'ordre 7.

## Graphe des dépendances (ce qui implique quoi)
```
littérature ──> Fix(t)={x} ──> t=σ, u≁σu ──> D couplage ──> modèle exact (R,D,I,P) ⇔ srg
                                                     │
                     ┌───────────────────────────────┴──────────────────────────┐
                 Stage Q (Q_out)                                          Stage S (S_out, C)
   spectre Q_out, F2 (rang 20), mod 3 (M)                 spectre S, F2 (rang 27 ⇔ Broué), F3 (22), Z7 (ouvert)
                     └──────── tous REDONDANTS : conséquences de A²+A−12I=2J restreinte aux orbites ────────┘
```
Point clé : **tout ce qui est au niveau 3 est une conséquence du niveau 2** ; aucune information indépendante n'a encore été trouvée.
Une vraie avancée doit soit (a) extraire une conséquence *non linéaire / arithmétique / globale* que les solveurs ne voient pas,
soit (b) changer d'objet.
