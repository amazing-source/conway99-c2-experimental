# 11 — L'involution comme RÉFLEXION PONCTUELLE : ce qu'elle induit sur les grilles (salve « reset », 24/09)

**Mouvement conceptuel.** Jusqu'ici, t servait de symétrie par laquelle on quotientait (orbites, Q/S, réseaux ±). Ici, on renverse le
point de vue : t est la **réflexion ponctuelle en x** d'une géométrie localement de Hamming sur F₃. Dans F₃^m, la réflexion en p est
v ↦ −v − p, c'est-à-dire « le troisième point de la droite (p, v) ». Dans les systèmes triples de Hall, les réflexions engendrent les
translations et la structure affine.
La question devient : **que force t sur les sous-structures parfaites (les grilles), et cette action est-elle elle-même une réflexion
(renormalisation) ?** Rien de tel dans l'historique : les grilles n'y servaient qu'au comptage et aux contraintes SAT.

## Théorème R1 (DÉRIVÉ, preuve complète)
Soit Γ un srg(99,14,1,2) et t une involution de point fixe unique x (cas C2).
1. Une grille contient x ⟺ elle est t-invariante. Ce sont les grilles Λ_ij des paires sœurs.
2. Si x ∉ Λ, alors **Λ ∩ tΛ = ∅**.
3. Λ contient exactement un sommet w de N(x). Les arêtes entre Λ et tΛ forment un **couplage parfait π**, avec π(w) = tw.
4. **φ := t∘π est une involution de Λ dont w est l'unique point fixe** (quatre transpositions).
5. Pour u ∈ Λ∖{w} : D(u) ∩ Λ ≠ ∅ ⟺ φ(u) ~ u, et alors D(u) = {φ(u), tφ(u)}.
6. **(Partition des étiquettes)** Soit w = εeᵢ. Les 12 demi-étiquettes des blocs ≠ i apparaissent chacune **exactement une fois** parmi
   les racines de Λ : une dans chacune des 4 racines voisines de w, qui contiennent w (ce sont deux droites de M_w), et deux dans chacun
   des 4 coins, qui ne contiennent pas ±eᵢ.

*Preuve.*
- **(1)** Si x ∈ Λ, les deux droites de Λ passant par x sont t-invariantes ; une grille est déterminée par deux droites sécantes (les coins
  sont les voisins communs μ), donc tΛ = Λ. Réciproquement, si tΛ = Λ, t agit sur 9 points et a donc un point fixe, qui ne peut être que x.
- **(2)** Deux grilles distinctes se coupent en 0, 1 ou 3 points :
  - deux points communs adjacents entraînent la droite commune ;
  - deux points communs non adjacents entraînent leurs deux voisins communs, donc un carré μ, donc 8 points, donc l'égalité des grilles.
  
  Or Λ ∩ tΛ est t-stable sans point fixe (x ∉ Λ), donc de cardinal pair, donc vide.
- **(3)** Par G1, x a exactement un voisin dans Λ, forcément dans N(x) ; et tout sommet hors de Λ en a exactement un dans Λ. Comme
  tΛ ∩ Λ = ∅, chaque u ∈ Λ a exactement un voisin π(u) dans tΛ. Enfin w ~ tw (deux compagnons de droite de x).
- **(4)** u ~ π(u) donne tu ~ tπ(u), avec tπ(u) = φ(u) ∈ Λ et tu ∈ tΛ, donc π(φ(u)) = tu et φ(φ(u)) = u. De plus φ(u) = u ⟺ u ~ tu
  ⟺ u ∈ N(x) ⟺ u = w.
- **(5)** Si φ(u) ~ u, alors φ(u) est voisin de u et de tu, donc φ(u) ∈ D(u). Réciproquement, si v ∈ D(u) ∩ Λ, alors v ~ tu ∈ tΛ, donc
  π(v) = tu et φ(v) = u.
- **(6)** Chaque sommet intérieur h ≠ w a exactement un voisin dans Λ (G1). Pour une demi-étiquette h d'un bloc ≠ i, ce voisin est une
  racine de Λ contenant h. Un coin contenant w serait voisin de w, ce qui est exclu dans la grille. Un coin contenant −w = tw serait
  π⁻¹(tw) = w. Le décompte donne 4 + 8 = 12. ∎

**Contrôle réel (BvLS, m = 11, t = −1)** : 990 grilles évitant x et touchant N(x). Dans les 990 cas : Λ ∩ tΛ = ∅, π est un couplage
parfait, et φ est une involution de point fixe unique (`scripts/bvls_grid_phi.py`).

## Conjecture R2 (renormalisation) — φ est la réflexion ponctuelle de Λ en w
Dans les coordonnées F₃² de Λ centrées en w : φ(i,j) = (−i,−j). Donc φ(α) = β et φ(γ) = δ sur les deux droites de w, et φ échange les
coins opposés.
- **Vraie dans BvLS : 990/990.** C'est une conséquence de la structure de coset : π y est la translation par w, et t∘translation est la
  réflexion en w.
- **Conséquences si R2 est vraie en C2** :
  - D(w+a) = orbite de w+b et D(w+c) = orbite de w+d, où {a,b} et {c,d} sont les deux paires de M_w qui portent Λ. Toute grille hors de
    x **ferme deux droites de M_w en paires D**, de type sib si b = −a, sinon de type one.
  - Si les droites de Λ en w = eᵢ sont sœurs (directions j, k), alors {i,j} et {i,k} sont des paires sœurs, et **les grilles Λ_ij, Λ_ik
    passant par x existent** : une grille hors de x engendre deux grilles par x. C'est l'analogue de la translation de coset, et un lien
    direct avec le théorème certifié sur Σ (au plus 7 arêtes) [périmé : au plus 4 arêtes et deg ≤ 2 depuis la note 19 ; voir aussi 15.3 (revue du 24/09, soir)].
  - π(coin) = −(coin opposé) : la paire (Λ, tΛ) est rigide.
- **Test** (`scripts/grid_offx_phi.py`, modèle C2 exact, grille imposée, un seul fil) : on demande si « NON φ(α) = β » est UNSAT.
  Résultat ci-dessous.

## Pourquoi c'est un mouvement nouveau
Le nombre de grilles, n₃ et les prismes relevaient d'une statistique. Ici, l'involution **se reproduit à plus petite échelle** : sur
chaque paire de grilles, elle induit une involution à point fixe unique, comme t sur Γ. Si cette auto-similarité est rigide (R2), elle
propage la structure de Hamming de x vers ses voisins. Une chaîne de telles propagations est exactement ce qu'il faudrait pour forcer
une structure de coset, qui est impossible à 99 sommets.
