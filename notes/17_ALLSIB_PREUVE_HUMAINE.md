# 17 — Allsib est impossible : preuve humaine par la cohomologie du complexe des couplages M₇ (24/09/2026)

Hypothèse de travail posée par l'utilisateur : C2 n'existe pas. On cherche pourquoi les cas rigides meurent, puis comment généraliser.

**Statut : DÉRIVÉ** (preuve complète ci-dessous, à faire relire). Première preuve humaine d'un cas que le labo ne connaissait que par
kissat avec preuve DRAT (note 06).

Contrôles machine :
- `scripts/allsib_connection.py`, `logs/allsib_connection.txt` : le modèle réduit est UNSAT. **LM + H3 suffisent** ; H4 n'est pas
  nécessaire ; LM seul et H3 + H4 s'arrêtent en TIMEOUT à 300 s.
- H¹(M₇ ; Z₂) = 0 est calculé : rang δ₀ = 20, rang δ₁ = 85.

## Énoncé

**Théorème 17.1.** Il n'existe pas de srg(99,14,1,2) muni d'une involution t de point fixe unique x tel que les 21 paires de droites
par x engendrent toutes une grille 3×3 (cas « allsib », Σ = K₇).

## Notations

- Carte en x : sommets intérieurs ±eᵢ (i = 1..7) ; racines ±eᵢ ± eⱼ, avec t = −1.
- Pour une paire de blocs p = {i<j}, P_p = {(a,b) : a, b = ±1} désigne les 4 racines a·eᵢ + b·eⱼ.
  - Deux racines de P_p sont **sœurs** si elles diffèrent d'un signe, **opposées** sinon (t-conjuguées).
  - Les deux t-orbites de P_p sont U_p⁺ = {produit ab = +1} et U_p⁻ = {ab = −1}.
- M₇ est le complexe des couplages de K₇ :
  - sommets : les 21 paires ;
  - arêtes : les paires disjointes (graphe de Kneser KG(7,2), 105 arêtes) ;
  - triangles : les triplets de paires deux à deux disjointes (105).

## Preuve

**Étape 1 : structure (lemme S1, note 03, DÉRIVÉ ; allsib = toutes les paires sont sœurs).**
- (a) Toute racine α ∈ P_p a exactement 12 voisines racines : ses 2 sœurs, et une racine dans chacun des 10 P_q, q disjointe de p.
  Deux racines sur des paires distinctes qui se coupent ne sont donc jamais adjacentes (sauf les sœurs, qui ont le même support).
- (b) Pour p, q disjointes, l'adjacence entre P_p et P_q est une bijection f_pq. Elle est t-équivariante (f_pq(−α) = −f_pq(α)) :
  - par S1(4), chaque racine évitant p a exactement un voisin dans P_p, et symétriquement ;
  - t est un automorphisme.

  Elle envoie donc U_p^± sur les deux t-orbites de P_q. Elle préserve aussi les sœurs, parce que l'autre t-orbite de P_q est formée
  des deux sœurs.

**Étape 2 : les conditions λ, μ entre paires disjointes donnent un cocycle.**
- Soient α ∈ P_p, β ∈ P_q, avec p et q disjointes. Leurs voisins communs sont :
  - les racines γ ∈ P_r, pour r disjointe de p ∪ q (3 paires) ;
  - les sœurs s de α telles que f_pq(s) = β ;
  - les sœurs s′ de β telles que f_pq(α) = s′.

  Il n'y a pas de voisin commun intérieur (étiquettes disjointes).
- Pour un triangle T = {p, q, r}, notons H_T = f_rp ∘ f_qr ∘ f_pq : P_p → P_p. Les conditions λ = 1 et μ = 2, pour β = f_pq(α),
  β = −f_pq(α) et β sœur de f_pq(α), donnent pour les trois triangles contenant {p, q} :
  - H_T(α) = α pour exactement un T ;
  - H_T(α) = −α pour exactement deux T ;
  - H_T(α) n'est jamais une sœur de α.
- Donc, pour **tout** triangle T, H_T fixe chaque t-orbite de P_p.
- Notons χ(f) ∈ Z₂ le fait qu'une bijection t-équivariante échange ou non les orbites « produit +1 / −1 ». χ est additif pour la
  composition. La cochaîne c(p,q) := χ(f_pq) vérifie donc c(p,q) + c(q,r) + c(r,p) = 0 sur chaque triangle : **c est un 1-cocycle
  de M₇ à valeurs dans Z₂.**

**Étape 3 : topologie.**
- H¹(M₇ ; Z₂) = 0 (calcul exact : rang δ₀ = 20 et rang δ₁ = 85, donc dim ker δ₁ = 20 = dim im δ₀). C'est cohérent avec
  H₁(M₇ ; Z) = Z/3 (Bouc).
- Donc c = δb pour une fonction b : {paires} → Z₂, c'est-à-dire c(p,q) = b(p) + b(q).

**Étape 4 : les conditions μ entre paires qui se coupent donnent une équirépartition impossible.**
- Soient i, et j ≠ k tous deux différents de i. Soient α ∈ P_ij et β ∈ P_ik ; elles ne sont pas adjacentes (étape 1a).
- Leurs voisins communs sont :
  - un voisin intérieur si α et β ont le même signe sur le bloc i ;
  - sinon aucun voisin intérieur, et les racines γ ∈ P_r, pour r parmi les 6 paires disjointes de {i, j, k}.
- Condition μ : #{r : f_{ij,r}(α) = f_{ik,r}(β)} = 2 − [αᵢ = βᵢ]. Posons g_r = f_{ik,r}⁻¹ ∘ f_{ij,r} : P_ij → P_ik. Pour α fixé, le
  multi-ensemble {g_r(α)} (6 éléments) atteint :
  - une fois chacun des deux β tels que βᵢ = αᵢ ;
  - deux fois chacun des deux β tels que βᵢ = −αᵢ.
- Chaque t-orbite de P_ik contient un β de chaque sorte. Donc exactement 3 des g_r(α) tombent dans chaque t-orbite, c'est-à-dire

  #{r : c(ij,r) + c(ik,r) = 1} = 3, puisque χ(g_r) = c(ij,r) + c(ik,r).
- Or, avec c = δb, on a c(ij,r) + c(ik,r) = b(ij) + b(ik), qui ne dépend pas de r. Le compte vaut donc 0 ou 6, jamais 3.
  **Contradiction.** ∎

## Ce que la preuve utilise, et ce qu'elle n'utilise pas

- **Utilise :**
  - λ = 1 et μ = 2 ;
  - l'involution t (orbites, t-équivariance) ;
  - le lemme S1, propre à m = 7 (partition exacte, 2(m−2) = C(m−2,2)) ;
  - H¹(M₇ ; Z₂) = 0.
- **N'utilise pas :**
  - l'équilibre des signes H4 (les conditions (I) hors des blocs de la racine) ;
  - la finesse des signes : tout se passe au niveau des **orbites** (étage Q).

  Reformulation à l'étage Q : la somme des deux équations (P), prise entre les orbites de P_ij et de P_ik, donne directement
  #{W : χ_ij(W) = ε, χ_ik(W) = ε′} = 3 pour chacune des 4 classes (ε, ε′). Ici W parcourt les 12 orbites des 6 paires disjointes de
  {i,j,k}.

## Portée : pourquoi ce mécanisme est le bon patron « local → global »

Le passage manquant (note 14 et « où je coince ») est exactement celui-ci :

| Niveau | Rôle | Ce qui le réalise ici |
|---|---|---|
| **Local** | une rigidité donne une donnée de recollement | les grilles-codes parfaits donnent des bijections f_pq, de caractère c ∈ Z₂ |
| **Local** | les conditions λ/μ disent que la donnée est plate | c est un cocycle |
| **Global** | la topologie du complexe de recollement l'intègre | H¹(M₇ ; Z₂) = 0, donc c est un cobord |
| **Local** | un autre comptage exige une donnée non intégrable | l'équirépartition 3/3 est incompatible avec un cobord |

**Ce qui ne se généralise pas tel quel.** Les bijections f_pq n'existent que pour les paires sœurs, c'est-à-dire les grilles par x.
Avec moins de grilles :
- le complexe de recollement est un sous-complexe de M₇ ;
- l'équirépartition de l'étape 4 porte sur des orbites de paires non sœurs, où χ_p est défini par S1(4) mais n'est plus une bijection.

## Suite (hypothèse : C2 n'existe pas)

1. **Rejouer le mécanisme** sur les autres configurations certifiées (K2+K2+P3, K3+K3, C₆…) : sous-complexe des paires sœurs, cocycle,
   cohomologie, équirépartition. Objectif : une preuve humaine pour chacune, puis pour tout Σ contenant deux paires sœurs disjointes et
   une paire qui coupe les deux.
2. **Cas pauvres en grilles.** Définir la même donnée χ_p à partir des carrés D de type one et dis, avec leurs défauts 2 et 8
   (note 07). On obtiendrait un « cocycle à défauts ». Chercher le complexe de recollement et son H¹, et une équirépartition exacte
   corrigée des défauts.
3. **Cœur sans grille (Σ = ∅).** Seuls les carrés D existent. C'est l'objectif final du point 2.
