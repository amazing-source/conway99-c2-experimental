# 15 — R2, types locaux autour d'une grille, et recollement de deux grilles (24/09/2026)

Programme demandé (après la note 14) :
1. une preuve humaine de R2 ;
2. les réflexions locales ρᵢ = t∘ι_{eᵢ} et leur propagation ;
3. l'exploitation du théorème annoncé du dépôt C3 ;
4. une boucle courte de monodromie.

Puis, sur suggestion relayée (« à prendre avec des pincettes ») : classer les φ survivants et chercher dans le groupe ⟨φ, τ, ν⟩ ;
tester le recollement de deux grilles.

Scripts :
- `scripts/r2_label_constraints.py` ;
- `scripts/r2_types.py` ;
- `scripts/r2_two_grids.py` ;
- `scripts/r2_local_sat.py`.

Journaux :
- `logs/r2_label_constraints*.txt` ;
- `logs/r2_types.txt` ;
- `logs/r2_two_grids.txt` ;
- `logs/r2_local_sat.log`.

Tous les calculs sont exacts, sauf le test SAT local : énumérations de quelques secondes, un seul fil, priorité minimale.

## 0. Résumé

- **DÉRIVÉ.** Formule des multiplicités (§1) : le nombre de témoins extérieurs de chaque paire (u, tv) est fixé par φ.
- **DÉRIVÉ.** La réflexion ponctuelle complète (R2 au sens de la note 11) force a, b, c, d dans quatre blocs distincts, avec un motif
  rigide des coins (§2). **R2 complète est donc fausse dès qu'une droite de Λ en w est sœur ou qu'une paire sœur croise les deux
  droites.**
- **OBSERVÉ (énumération exacte).** R2 « sur les droites » ne découle pas des contraintes locales **retenues** (filtres C3, C4, C8
  seulement ; la vraie relaxation SAT locale a fait TIMEOUT, §5 — « pas de preuve locale » n'est donc pas établi, revue du 24/09, soir).
  - Il reste 1194 types locaux, à symétrie près, et 263 formes de φ (§3).
  - Deux tests SAT locaux s'arrêtent en TIMEOUT (240 s) : inconclusifs.
- **Mal posé tel quel.** Le triplet (φ, τ, ω) et le groupe H = ⟨φ, τ, ν⟩ (§4) :
  - cyc(φ) = 2⁴ toujours ;
  - τ n'est forcé que sur les échanges P–P ;
  - φ n'agit sur les 12 demi-étiquettes que si φ(P) = P, ce qui arrive dans 56 types sur 1194.
- **OBSERVÉ.** Dans ces 56 types, un élément d'ordre 3 apparaît pour certains choix, jamais pour tous. Rien ne force l'ordre 3.
- **DÉRIVÉ.** 112 types ont une symétrie locale non triviale g. Aucune ne peut se propager en automorphisme en C2, car Aut(Γ) = ⟨t⟩
  (§5). Chercher g, c'est encore le lemme de propagation (P) de la note 14.
- **DÉRIVÉ.** Le théorème C3 n'est pas nécessaire pour cette cible : en C2, Aut(Γ) = ⟨t⟩ découle déjà de |Aut Γ| ≤ 3
  (littérature, carte 00). De plus, le README du dépôt C3 (daté du 23/09) indique que sa conclusion n'est pas encore acquise (§5).
- **DÉRIVÉ.** Incompatibilité (§6) : R2 complète en w entraîne σ_w ∉ Aut. Les étapes 1 et 2 du programme tirent en sens contraires
  à m = 7.
- **OBSERVÉ.** Le recollement de deux grilles partageant une droite en w (sans étiquettes, §7) :
  - élimine 54 % des paires (φ, φ′) quand la droite partagée n'est pas D-fermante ;
  - n'élimine **aucun** φ d'une grille seule.

  Le saut local → global espéré n'apparaît pas à ce niveau.

## 1. Multiplicités (DÉRIVÉ)

Cadre (notes 11 et 13) :
- Λ est une grille évitant x, w = e₁ ;
- α = [e₁,a], β = [e₁,b], γ = [e₁,c], δ = [e₁,d], avec {a,b}, {c,d} ∈ M₁ ;
- les coins z_pq portent les 8 demi-étiquettes restantes R8 (R1(6)) ;
- φ = t∘π.

**Proposition 15.1.** Pour u ≠ v dans Λ∖{w}, le nombre de voisins communs de u et de tv hors de Λ ∪ tΛ vaut

  m(u,v) = 2 − [u ~ φ(v)] − [φ(u) ~ v] − [φ(u) = v].

*Preuve.* Dans Λ, le seul voisin de tv est φ(v). Dans tΛ, le seul voisin de u est π(u) = tφ(u). Le total vaut λ = 1 si u ~ tv,
c'est-à-dire si φ(u) = v, et μ = 2 sinon. ∎

**Corollaire 15.2 (blocs).** Pour chaque bloc k ≠ 1, m(λ(e_k), λ(−e_k)) ≥ 1, car le sommet intérieur e_k est un voisin commun
extérieur de λ(e_k) et de tλ(−e_k).

**Remarque.** La matrice 12I − M − M², avec M = G − F (G la grille, F la matrice de φ), est le laplacien du multigraphe des arêtes
{c_Λ(y), c_Λ(ty)}. Il est automatiquement à poids positifs : aucune contrainte spectrale sur φ n'en sort (entrelacement vide).

## 2. R2 complète force quatre blocs distincts (DÉRIVÉ)

**Théorème 15.3.** Supposons que φ est la réflexion ponctuelle de Λ en w. Alors :
- a, b, c, d sont dans quatre blocs distincts ;
- chaque coin porte exactement une des étiquettes −a, −b, −c, −d. Plus précisément, −a est dans la ligne de α, −b dans celle de β,
  −c dans la colonne de γ et −d dans celle de δ. Deux motifs tournants sont possibles :
  - (z_ac ∋ −a, z_ad ∋ −d, z_bd ∋ −b, z_bc ∋ −c) ;
  - (z_ac ∋ −c, z_ad ∋ −a, z_bd ∋ −d, z_bc ∋ −b) ;
- les deux blocs restants occupent chacun une diagonale.

*Preuve.*
- Sous φ = σ_w :
  - m(z, z′) = 0 pour deux coins sœurs, et m = 1 pour deux coins opposés ;
  - m(α, z) = 0 pour z dans la ligne de β, et 2 pour z dans la ligne de α (idem pour β, γ, δ).
- Par 15.2 :
  - un bloc entièrement dans R8 occupe deux coins opposés ;
  - une étiquette −p ∈ R8 (p ∈ {a,b,c,d}) se trouve dans la ligne ou la colonne de [e₁,p].
- Si un coin z = [h,g] avait −h et −g dans R8, ces deux étiquettes seraient dans σ_w(z). On aurait alors σ_w(z) = [−h,−g] = tz,
  donc Λ ∩ tΛ ≠ ∅, ce qui contredit R1(2).
- Chacun des 4 coins contient donc une étiquette dont l'opposée est dans {a,b,c,d}. Ces étiquettes sont parmi −a, −b, −c, −d, et
  chacune n'apparaît qu'une fois. Il faut les quatre : il n'y a pas de sœurs dans {a,b,c,d}, et chaque coin en porte exactement
  une. ∎

**Contrôle.** Dans l'énumération (§3), la réflexion ne survit que dans le type T3.

**Conséquence.** Dans le cas « droites sœurs » de la note 11 :
- R2 sur une droite sœur équivaut toujours à {1,k} ∈ Σ ;
- mais R2 **complète** y est impossible.

## 3. Énumération exacte et types locaux (OBSERVÉ)

**Filtres.**
- (C3) : blocs (15.2).
- (C4) : aucun coin n'est t d'un autre.
- (C8) : lemme S1 vu depuis w (valable dans toute carte).
  - Les 40 w-racines évitant les blocs {α,β} et {γ,δ} se partagent en N₀(z) de façon équitable (1 / 1 / 1 / 2).
  - Une w-racine qui touche un seul bloc a 6 voisins évitants, répartis 1 / 1 / 2 / 2.
  - Les sommets connus sont : h ∈ H ; tu (évitant de classe φ(u) si φ(u) est un coin).

  (C8) n'élimine **rien** de plus que (C3) et (C4).

**Symétries locales.** W(B₆), qui agit sur les étiquettes des blocs 2 à 7, et D₄, les symétries de la grille fixant w. Le groupe
résiduel est d'ordre 3072 (T1), 192 (T2), 64 (T3), 96 (T4a) ou 1536 (T4b).

| Type de {a,b,c,d} | orbites de dispositions | types locaux (disposition, φ) | formes de φ | réflexion | types « droites R2 » |
|---|---|---|---|---|---|
| T1 : deux droites sœurs | 2 | 16 | 13 | 0 | 1 |
| T2 : une droite sœur | 11 | 185 | 71 | 0 | 4 |
| T3 : quatre blocs | 33 | 676 | 92 | 1 | 10 |
| T4a : c = −a | 15 | 297 | 70 | 0 | 4 |
| T4b : c = −a, d = −b | 2 | 20 | 17 | 0 | 1 |
| **Total** | 63 | **1194** | 263 | 1 | 20 |

**Réponse à « combien de types locaux réellement différents ? »** 1194. Ils ne se réduisent pas à 2–5 types structurels : les
contraintes locales sont trop faibles.

**Types « droites R2 » (φ(α) = β et φ(γ) = δ).** Les coins y sont échangés par lignes, par colonnes, ou par la réflexion (T3
seulement). Les carrés D internes sont :

| Type | Carrés D internes |
|---|---|
| T1 | one, one, sib, sib : les arcs de retour {1,2} et {1,3} sont dans Σ |
| T3, réflexion | one, one |
| T3, autres | one / dis |

**Tests SAT locaux.** Relaxation : conditions srg touchant S = {x} ∪ N(x) ∪ Λ ∪ tΛ, grille imposée, NON(α ~ tβ). T3 et T1 :
TIMEOUT à 240 s. Inconclusifs.

## 4. Le triplet (φ, τ, ω) et le groupe H = ⟨φ, τ, ν⟩

- **φ.** C'est une involution sans point fixe des 8 sommets de Λ∖{w} : cyc(φ) = 2⁴ toujours, sans information.
- **τ.** C'est l'involution canonique autour de w, définie par [e₁,h] ~ t[e₁,τ(h)]. La configuration locale ne la fixe que sur les
  échanges P–P (φ([e₁,p]) = [e₁,q] ⟺ τ(p) = q), soit 0 à 2 paires. Pour un échange P–K, on sait seulement τ(p) ∈ R8. Ailleurs, τ
  est libre.
- **ω = τν.** Il en est de même : ω(−p) = τ(p) sur les paires forcées. La relation νων = ω⁻¹ est automatique (τ est une involution).
- **φ sur les étiquettes.** φ n'agit sur les 12 demi-étiquettes que si φ(P) = P. Un sommet [e₁,p] porte e₁ et une étiquette, un
  coin en porte deux. Même dans ce cas, il y a 2 choix par échange de coins.
- **Ombre Φ (56 types sur 1194).** Pour **chacun** des 56 types, certains choix donnent ord(Φν) divisible par 3 et d'autres non.
  Ordres observés : 2, 3, 4, 6. **Aucun type ne force un élément d'ordre 3.**
- **Réflexion (T3).** Le choix canonique respecte la structure « −p / diagonale » des coins :
  Φ = (a b)(c d)(−a −b)(−c −d)(e_m −e_m)(e_n −e_n). Il commute à ν, et ⟨Φ, ν⟩ est le groupe de Klein : **pas d'ordre 3.**

Conclusion : H n'est pas un invariant du type local. La seule quantité canonique mesurable est **l'écart entre φ et τ sur les
échanges P–P**, c'est-à-dire les droites D-fermantes et les arcs, que le tableau du §3 recense.

## 5. Symétries candidates g, C3 et Aut(Γ) (DÉRIVÉ)

**Candidats.** 112 types locaux ont un stabilisateur non trivial dans W(B₆) × D₄ : 8 en T1, 28 en T2, 66 en T3, 2 en T4a, 8 en T4b.
Ce sont exactement les permutations g des demi-étiquettes qui :
- préservent les paires de négation ;
- préservent les données locales ;
- sont différentes de 1.

Le prolongement candidat est v_{a,b} ↦ v_{g(a),g(b)}.

**Pourquoi aucun ne peut se propager.**
- Un tel g fixe x et w. S'il était un automorphisme, il serait dans Aut(Γ)_x ∩ Aut(Γ)_w.
- Or, en C2, Aut(Γ) = ⟨t⟩ :
  - |Aut Γ| ∈ {1,2,3} (Makhnev–Minakova, Behbahani–Lam, Crnković–Maksimović, Cesarz–Woldar ; carte 00) ;
  - t est d'ordre 2.
- Comme t déplace w, on aurait g = 1.
- Donc la question « v_ab ~ v_cd ⟺ v_{g(a)g(b)} ~ v_{g(c)g(d)} pour tous a, b, c, d ? » a nécessairement la réponse « non » en C2.
  La forcer serait une contradiction : c'est de nouveau le lemme (P) de la note 14.

**Sur C3.**
- En C2, tout automorphisme autre que 1 et t est déjà exclu par |Aut Γ| ≤ 3. Le théorème « g³ = 1 ⇒ g = 1 » n'ajoute rien pour cette
  cible.
- Le README de `amazing-source/conway99-c3` (état au 23/09/2026) dit : « Rien n'est encore décidé : la conclusion “pas
  d'automorphisme d'ordre 3” n'est acquise que si tout le calcul restant finit UNSAT et si les démonstrations sont relues ». Il
  demande aussi aux sessions de la branche involution de ne pas consulter le dépôt.
- Seul ce README a été lu, pour connaître l'énoncé exact. Rien d'autre n'a été consulté.

## 6. R2 et « ρ_w automorphisme » sont incompatibles à m = 7 (DÉRIVÉ)

- Si σ_w ∈ Aut, il envoie la droite {tw, tα, tβ} sur {x, M₁τ(a), M₁τ(b)}, qui doit être une droite par x.
- Sous R2 sur ℓ₁ (τ(a) = b), cette image est {x, a, b}, ce qui force b = −a : la droite est sœur.
- Or R2 complète interdit les droites sœurs (15.3).
- **Donc, si φ est la réflexion pour une grille en w, σ_w n'est pas un automorphisme.**

Cela n'apporte rien de neuf sur C2, puisque σ_w ∉ Aut y est déjà connu. En revanche, cela montre que le chemin « R2 ⇒ propagation ⇒
ρ_w automorphe » ne peut pas passer par R2 complète.

**Conditions locales nécessaires pour σ_{e₁} ∈ Aut.** Elles correspondent à la préservation de l'étoile de la droite {x, e₁, −e₁},
avec κ = νM₁ :
- (B) ω commute avec κ ;
- (A) ω²κ³ = 1.

Elles ne suffisent pas : il faut aussi l'équivariance des racines lointaines. Un repère de 39 sommets contrôlés, de rang au plus 39,
est trop petit pour la rigidité de type Bondarenko–Radchenko : il faudrait au moins 54 sommets pour engendrer V₃.

## 7. Recollement de deux grilles partageant une droite en w (OBSERVÉ, sans étiquettes)

**Cadre.**
- Λ et Λ′ passent par w et se coupent exactement en ℓ₁ = {w, α, β}.
- Il n'y a aucune arête entre Λ∖ℓ₁ et Λ′∖ℓ₁ : par G1, leur voisin est dans ℓ₁.
- Couplages : π (Λ–tΛ), π′ (Λ′–tΛ′), et ψ (Λ′–tΛ), supposé parfait (Λ′ ∩ tΛ = ∅). [Portée, revue du 24/09, soir : les intersections Λ′ ∩ tΛ en 1 ou 3 points, permises par R1(2),
  ne sont pas testées.]
- Valeurs forcées de ψ : ψ = π sur ℓ₁, ψ⁻¹(tα) = φ′(α), ψ⁻¹(tβ) = φ′(β), et φ(α) = β ⟺ φ′(α) = β.
- Sur 30 sommets, le graphe induit est alors entièrement déterminé par (φ, φ′, ψ). On teste λ et μ sur toutes les paires.

**Résultats.**
- Paires (φ, φ′) compatibles avec la droite partagée : 8325. Au moins un ψ convient pour 3977 d'entre elles.
- Si ℓ₁ est D-fermante : 225 paires sur 225 conviennent.
- Sinon : 3752 sur 8100.
- **Les 105 φ de Λ gardent un partenaire.** La réflexion en a 15.

Le recollement élague des paires, mais ne tue aucun type d'une grille seule. Étape suivante possible : la version étiquetée, où les
sommets intérieurs deviennent des témoins et où les étiquettes des coins de Λ′ entrent en jeu. Elle est plus coûteuse (quelques
centaines de milliers de configurations par type), à faire seulement si l'on garde la voie des grilles.

## 8. Portée et suite

- **Portée.** Autour d'une ou de deux grilles, la structure locale est souple : 1194 types, aucun ordre 3 forcé, aucune symétrie
  propageable, recollement non contradictoire.
- **Réserve stratégique.** Tout ce qui passe par les grilles laisse intact le cœur sans grille (n₃ ≥ 2079 possible, note 08). Même
  une élimination complète des configurations à grilles ne tuerait pas C2.
- **Ce qui reste mesurable et canonique** : l'écart entre φ et τ, c'est-à-dire les droites D-fermantes et les arcs. Il est relié au
  programme Δ par une traduction explicite :

  > droite D-fermante en eᵢ ⟺ arête « one » (ou boucle sib) de Δ entre deux paires de blocs contenant i.

  R2 complète exige deux arêtes « one » disjointes de Δ en i, sur quatre blocs distincts (15.3).
