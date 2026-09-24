# 12 — Théorèmes rêvés (salve « reset », 24/09/2026)

Principe : partir de la contradiction désirée, écrire l'énoncé qui la produirait, chercher un mécanisme, puis tenter de le réfuter à
moindre coût.

Format de chaque entrée :
- **E** : l'énoncé.
- **Pourquoi** : comment il tue ou comprime C2.
- **Hyp.** : les hypothèses utilisées.
- **Non trivial** : pourquoi ce n'est pas une conséquence immédiate du modèle.
- **Test** : la réfutation la moins coûteuse.
- **Statut**, quand il y en a un.

Notations : C2 = (Γ, t), t involution de point fixe unique x ; Σ = graphe des paires sœurs ; n₃ = paramètre libre de Reimbayev ;
grilles = K₃×K₃ induits.

## A. Grilles et renormalisation (mouvement « réflexion », note 11)
1. **R2 (renormalisation)**
   - E : pour toute grille Λ ∌ x, φ = t∘π est la réflexion ponctuelle de Λ en w.
   - Pourquoi : rigidifie toutes les paires de grilles ; ferme deux droites de M_w en paires D ; relie les grilles hors de x à Σ.
   - Hyp. : C2 et G1.
   - Non trivial : a priori, 105 involutions possibles à point fixe unique.
   - Test : SAT court (en cours).
   - Statut : vraie dans BvLS (990/990).
2. **Pas de grille hors de x**
   - E : en C2, toute grille contient x.
   - Pourquoi : N = n_sib ≤ 7, donc n₃ ≥ 2016 (via c̄) ; la géométrie des grilles devient entièrement locale en x.
   - Test : SAT court, mode « exist ».
3. **Triangle de translation**
   - E : si Λ ∌ x passe par eᵢ avec des droites sœurs de directions j, k, alors {i,j}, {i,k}, {j,k} ∈ Σ.
   - Pourquoi : combiné avec « K₃ + … » certifiés interdits dans Σ, cela bornerait fortement les grilles hors de x.
   - Test : via R2, puis SAT en imposant la grille.
4. **Réseau de grilles (spread)**
   - E : tout Conway-99 admet une partition en 11 grilles.
   - Pourquoi : le quotient serait 3I + J, chaque grille induirait une 1-factorisation de K₁₀ indexée par ses 9 points, et l'ansatz est
     un petit problème fini.
   - Non trivial : la cohérence spectrale est parfaite (Gram 9I − 9J/11) ; seule la combinatoire peut trancher.
   - Test : SAT de l'ansatz (≈ 4 500 variables).
5. **Existence d'une grille**
   - E : n₃ < 2079.
   - Pourquoi : élimine le cas « sans grille », le cœur dur.
   - Test : programme linéaire des fréquences d'ordre 7.
   - Statut : **réfuté comme conséquence des fréquences** (N10).
6. **Grilles régulières**
   - E : g(y) est constant.
   - Pourquoi : g ∈ vect(𝟏) ; en C2, N = 11·n_sib et chaque sommet est dans n_sib grilles, ce qui contredirait le point 2 si n_sib ≥ 1.
   - Test : l'identité Σ_{z∼y} g(z) − 3g(y) = N est cohérente, il faut un argument de plus.

## B. Hamming local ⇒ global
7. **Rigidité de Hamming**
   - E : n₃ = 0 pour tout srg(1+2m², 2m, 1, 2).
   - Pourquoi : si tous les coins se ferment, le 2-complexe triangles + carrés μ (localement isomorphe à celui de H(7,3) : même lien K₁₄,
     note 13) se relève en H(7,3), donc 99 divise 3⁷ : absurde (Makhnev).
   - Non trivial : **équivalent au problème**. Cela sert de boussole, pas de test.
8. **Courbure concentrée**
   - E : la « courbure » κ(y) = Σ_{coins en y}(4 − c) est ≥ 28 en x (prouvé : au plus 7 paires sœurs), et sa moyenne vaut 2n₃/99.
   - Rêve : κ est sous-harmonique (Σ_{z∼y} κ(z) ≤ 14κ(y) + c), ce qui forcerait n₃ > 4158 : absurde.
   - Test : impossible en l'absence de graphe ; il faut chercher une identité locale sur κ.
9. **Monodromie**
   - E : le transport des directions par les coins fermés définit un système local partiel sur X_Γ ; sa monodromie autour des carrés D
     non sœurs est forcée (t = −1).
   - Rêve : cette monodromie contredit la trivialité locale autour de x.
   - Test : calculer la monodromie dans BvLS (triviale) et chercher une contrainte en C2.
10. **Réflexions locales**
    - E : ρᵢ = t∘ι_{eᵢ} (ι = négation de carte) est d'ordre 3 sur les 36 points I ∪ R⁺ ∪ R⁻ (κωκωκ = id, note 13).
    - Pourquoi : cela forcerait une translation locale, puis une structure de coset.
    - Test : SAT court sur la structure au bloc 1.

## C. Objets dérivés qui devraient être impossibles
11. **Code ternaire des droites**
    - E : l'espace engendré sur F₃ par les 231 droites a une dimension fixée par la forme de Smith 3-adique de NNᵀ = A + 7I, et
      l'énumérateur de son dual, contraint par les grilles (mots de poids 6 dans ker N), a un coefficient négatif.
    - Test : calculer sur Paley(9) et BvLS, puis la formule générale.
12. **Réseau des syzygies de droites**
    - E : K_L = ker N ∩ Z²³¹ (rang 132, pair, t-stable) a trop de vecteurs de norme 6 (les grilles) pour son déterminant.
    - Test : déterminant via NNᵀ, puis borne de Hermite ou d'Odlyzko.
13. **Deux-graphe des triangles de S**
    - E : le deux-graphe des signes des triangles du graphe signé S est régulier, ce qui donnerait des droites équiangulaires, puis une
      parité à la Neumann absurde.
    - Test : régularité sur BvLS (m = 11).
14. **Égalité d'inertie**
    - E : α(|S|) = 22, égalité dans la borne d'inertie ; le 22-ensemble est alors un « code » du graphe orbital, et une contradiction
      viendrait des blocs.
    - Test : α(|S|) sur BvLS.
15. **Cocliques de Delsarte**
    - E : Conway-99 contient une 22-coclique (égalité de Hoffman).
    - Pourquoi : en C2, **aucune n'est t-invariante (prouvé : x aurait 4 voisins formant 2 arêtes-blocs)**, donc elles vont par paires ;
      la contradiction viendrait de leurs intersections.
    - Test : aucun direct.
16. **Graphe des carrés D**
    - E : les 21 carrés D, reliés par les arêtes S, forment un multigraphe régulier dont le spectre est forcé.
    - Test : spectre de Q_out restreint aux blocs 4×4.

## D. Structures sur les 7 blocs
17. **Classe forcée de Δ**
    - E : le multigraphe 2-régulier Δ des paires D sur les 21 paires de blocs est une union de 7 triangles (plan de Fano).
    - Pourquoi : une vérification finie tuerait ou isolerait le cas.
    - Test : SAT avec Δ imposé (quelques motifs).
18. **Engendrement par les couplages**
    - E : les 7 couplages locaux M_{eᵢ} (involutions sur 12 demi-étiquettes), avec la négation ν, engendrent un groupe contenant une
      translation d'ordre 3 ; une contradiction viendrait avec C3 (si la preuve est validée).
    - Test : tirages aléatoires de solutions de la relaxation.
19. **Types de carrés forcés**
    - E : n_sib + n_one + n_dis = 21 avec n_dis = 0.
    - Pourquoi : les carrés dis ont un défaut 8 ; « pas de dis » réduirait fortement le problème.
    - Test : SAT « au moins un carré dis ».

## E. Positivité et algèbre
20. **Krein gradué à deux points**
    - E : un ⟨E_i^a ∘ E_j^b, E_k^c⟩ < 0 pour la paire (Γ, t).
    - Statut : **réfuté** (`scripts/graded_krein.py`) : tous ≥ 0, même pour des involutions hypothétiques. Aucun pouvoir discriminant.
21. **Positivité à trois points (Schrijver)**
    - E : la relaxation du moment de degré 2 du modèle C2, symétrisée par W(B₇), est infaisable.
    - Test : symétrisation, puis SDP de taille modérée (quelques centaines de variables).
    - Statut : non fait (charge machine).
22. **Algèbre de Norton graduée**
    - E : la forme cubique F(w) = Σ w(z)³ s'annule sur V_θ⁻ (**prouvé** : t impose F(−w) = F(w)).
    - Rêve : l'application quadratique V_θ⁻ → V_θ⁺, w ↦ E_θ(w∘w), a un rang incompatible avec 27 ou 22.
    - Test : identités de trace.
23. **Complexe triangles + carrés**
    - E : H₁(X_Γ; F₃) est forcé par la forme de Smith de A mod 3, et la formule de Lefschetz tr(t|H₂) − tr(t|H₁) = 21 (**prouvée**) le
      contredit.
    - Test : H₁ sur Paley(9) et BvLS (attendu : 0 et F₃⁶).
24. **Unicité, donc symétrie**
    - E : la structure en x (Σ, les M_{eᵢ}, D) détermine Γ de façon unique, et l'objet unique hérite d'une symétrie d'ordre 3 de ses
      données : absurde.
    - Test : aucun.

**Les plus éloignés du programme Δ** : 1–4 (renormalisation), 7–10 (Hamming local, réflexions), 11–12 (codes et syzygies de droites),
21–23 (positivité, Norton, topologie).
