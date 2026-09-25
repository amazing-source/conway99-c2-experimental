# 26 — Lemme de la queue hors ancrage : configurations « ancrées sauf une chaîne tordue » (25/09/2026, soir)

Session principale C2, régime sans solveur. Aucune énumération : tout est fait à la main.

**Statut.** DÉRIVÉ, à relire. **Résultat partiel** : fortes contraintes de degrés, mais **pas de fermeture**. Un survivant
modèle est identifié au §4.

## 0. Cadre (M1)
- Σ = ∅, et tous les carrés D sont de type « un bloc » (pas de carré disjoint). Donc n_s = 0 partout (carnet §7 : n_s = 1 ⟹ carré
  disjoint).
- Chaque paire est :
  - soit **ancrée** : ses deux orbites sont appariées par le même bloc. On l'oriente vers l'ancre ;
  - soit **tordue** : une orbite par chaque bloc (carnet §14).
- En chaque bloc, le nombre de paires tordues est pair (carnet §14, parité par bloc). Les paires tordues forment donc un
  sous-graphe pair de K₇.
- **Hypothèse M1** : ce sous-graphe est un **seul cycle** T = t₀t₁…t_{n−1}, avec 3 ≤ n ≤ 7.

**Notations.** d_k = nombre de paires ancrées en k (degré entrant) ; t_k = nombre de paires tordues en k (0 ou 2) ;
out_k = 6 − d_k − t_k.

**Graphe D en un bloc k** (les arêtes D « via k »). Ses sommets sont les paires {k, m} qui ont au moins une orbite appariée par k. Une
paire ancrée en k y a le degré 2, une paire tordue le degré 1. C'est donc une réunion de cycles sur les paires ancrées en k (de
longueur ≥ 2, sans boucle puisque Σ = ∅), plus, si k ∈ T, un **chemin** qui va d'une paire tordue à l'autre en passant par des
paires ancrées en k.

**Orbites libres en k** (carnet 19.1). Ce sont les orbites passant par k qui ne sont pas appariées par k. Sous R_k, elles forment des
cycles pairs de longueur ≥ 4 :
- sans arête entre sœurs ;
- deux sœurs ont au plus un voisin commun, donc un 4-cycle libre ne contient jamais deux sœurs.

Il y a 2·out_k + t_k orbites libres.

## 1. Les blocs de T
**Lemme 26.1.** Si t ∈ T, alors out_t ≥ 2, donc d_t ≤ 2.
*Preuve.* Il y a 2·out_t + 2 orbites libres. Si out_t = 0, il en reste 2 : c'est une digone, exclue. Si out_t = 1, il en reste 4,
dont deux sœurs (la paire sortante) sur un même 4-cycle : exclu. ∎

## 2. Les blocs hors de T : la queue vaut encore
**Lemme 26.2.** Si k ∉ T, alors d_k ∈ {0, 2, 3, 6}.
*Preuve.* Toutes les paires en k sont ancrées.
- d_k = 1 est exclu : il faudrait une boucle dans le graphe D.
- 2·out_k ∈ {2, 4} est exclu par 19.1 (digone, ou K₂,₂).
- Enfin, un bloc qui a un arc sortant est un bras, donc d ≤ 3 par 26.3. ∎

**Lemme 26.3 (queue).** Soit un carré de pivot i et de bras j, m, avec m ∉ T. Alors **d_m ≤ 3 − [m → j]**, où [m → j] = 1 si la
paire jm est ancrée en j.
*Preuve.* C'est 25.2 appliqué en m.
- En m, toutes les paires sont ancrées. Une orbite appariée par m l'est à une orbite, elle aussi appariée par m, d'une paire {m, m′}.
  Cette paire n'est pas tordue (m ∉ T), elle est donc ancrée en m. X_In(m) est donc stable par σ, μ_m, τ_m, et X_Out(m) est une
  réunion de composantes de taille 2(6 − d_m).
- La paire {i, m} a une orbite appariée par i, et n'est pas tordue : elle est ancrée en i, donc i ∈ Out(m).
- L'équilibre en ℓ_m donne alors, pour x dans l'orbite de {i, j} : 6 − d_m ≥ 1 + 2 + [j ∈ Out(m)]. ∎

Les blocs de T ont d ≤ 2 de toute façon (26.1). Donc, **pour tout arc ancré entre deux bras d'un même carré, la queue a d ≤ 2.**

## 3. Conséquences sur les degrés
On appelle **C-bloc** un bloc hors de T de degré 3, et **A** un éventuel bloc de degré 6 (au plus un ; il est hors de T et n'a aucun
arc sortant). Tous les autres blocs ont d ≤ 2.

**Proposition 26.4.** Il y a au plus deux C-blocs.
*Preuve.*
- En un C-bloc c, le graphe D est un triangle sur In(c) : les trois paires de bras portent des carrés. Deux C-blocs de In(c)
  seraient reliés par un arc ancré (ils sont hors de T) de queue de degré 3. Donc |In(c) ∩ C| ≤ 1.
- S'il y avait 3 C-blocs, ils formeraient un cycle, et In(C_j) = {C_{j−1}, p_j, q_j}.
- C_{j−1} doit être la tête de ses arcs vers p_j et q_j : ces arcs sont ancrés, puisque les C-blocs sont hors de T. Donc
  p_j, q_j ∈ In(C_{j−1}), et les trois C-blocs ont le même couple {p, q}.
- Tout autre bloc r ∉ {A, p, q} reçoit alors des arcs des trois C-blocs, d'où d_r ≥ 3, alors que d_r ≤ 2.
- Un tel r existe, puisqu'il faudrait sinon 7 = 3 + 2 + [A]. ∎

**Bilan des sommes.** Σ_k d_k = nombre de paires ancrées = 21 − n. Avec a = [A existe] et c = nombre de C-blocs :
- Σd ≤ 6a + 3c + 2(7 − a − c) = 14 + 4a + c ;
- T ne contient que des blocs de degré ≤ 2, donc n ≤ 7 − a − c.

Cas possibles :
- **a = 0** :
  - c = 0 et n = 7 : tout est de degré 2 ;
  - c = 1 et n = 6 ;
  - c = 2 et n = 5.
  Dans les trois cas, les blocs non C sont exactement T, de degré 2.
- **a = 1** : c = 0 avec 3 ≤ n ≤ 6 ; c = 1 avec 3 ≤ n ≤ 5 ; c = 2 avec 3 ≤ n ≤ 4.

Par un C-bloc, A impose aussi : dans le graphe D en A, les deux voisins de la paire {A, c} doivent pointer vers c.

## 4. Limite : un survivant modèle
**Observation 26.5 (non réfuté par la queue).** Prenons n = 7 (T hamiltonien), a = c = 0, et tous les degrés égaux à 2. Les
14 paires ancrées forment K₇ − C₇, 4-régulier, orienté de façon eulérienne (2 entrants, 2 sortants en chaque bloc).
- En chaque bloc t, il y a 6 orbites libres, sur un seul 6-cycle (4 + 2 est impossible).
- Si le chemin D en t est direct (la chaîne tordue passe par t sans passer par une paire ancrée), les deux paires ancrées en t
  forment une structure liée. Les composantes en t sont alors {a, b} (2 blocs) et M = Tw(t) ∪ Out(t) (4 blocs).
- Toutes les inégalités 24.1 et 26.3 tiennent, parfois avec égalité. Par exemple, pour le carré de chaîne de pivot t_m, on obtient
  en t_{m+1} : |M| = 4 ≥ 3 + 1.
- **Le mécanisme de la queue ne ferme donc pas les chaînes tordues.** La chaîne tordue hamiltonienne est le cas modèle de ce
  régime, comme Fano l'était des triangles.

## 5. Suite possible
- Attaquer la chaîne tordue hamiltonienne avec les outils qui ont tué Fano (Théorème F du carnet : budget μ 16.1, lemme du coin,
  règle des zéros) et Paley (saturation du budget des zéros).
- Combiner avec l'équilibre en des droites qui ne passent pas par x.
- Les cas a = 1 de §3 sont plus contraints. Il faudrait les examiner un par un à la main, sans énumération par machine.
- Les carrés disjoints restent hors de portée de la queue.

## 6. Raffinement de « structures » (25/09, revérifié ici) : l'équilibre composante par composante
Soit un carré « un bloc » de pivot i, avec X ⊂ ij, D(X) ⊂ ik, et x ∈ X. Pour **chaque** composante C de G_k, l'équilibre donne :

  [i ∈ C] + [j ∈ C] + #(racines de x dans C) = b_C, où b_C est le nombre de blocs de C.

x a exactement 4 racines en star(k) : v, σv, et deux autres w, w′.
- En Σ = ∅, toute composante vérifie b ≥ 2 (b = 1 demanderait une frère ou un cycle libre de longueur 2).
- Une composante qui ne contient pas i a au plus 3 blocs, et comp(i) en a au moins 3.
- **G_k est donc de type (6), (4,2) ou (3,3)**, avec une répartition forcée :
  - (3,3) : j, w et w′ sont dans l'autre composante ;
  - (4,2) avec j ∈ comp(i) : w et w′ sont dans la 2-composante ;
  - (4,2) avec j dans la 2-composante : exactement une de w, w′ y est.
- Une 2-composante est une structure liée de charnière k. Une composante sans digone a au moins 3 blocs.

*Dans M1.*
- Hors de T, c'est cohérent avec 26.2 : d = 2 donne (4,2) ; d = 3 donne (3,3), avec j ∈ In(k) et w, w′ à étiquettes dans X_In(k) ;
  d = 0 donne (6) ou (3,3).
- Sur T, les types (6), (4,2) et (3,3) sont tous réalisables.
- Le raffinement impose donc seulement **la place des racines w, w′**. Ce sont de nouvelles contraintes locales, qui n'ont pas
  encore été exploitées sur le survivant hamiltonien.

**Partage du travail (25/09).**
- « structures » prend le tout-tordu pur (D = décomposition de K₇ en cycles, hors Fano). Là, G_k est connexe partout et 24.1 est vide.
- C2 garde les mélanges presque ancrés, dont le survivant hamiltonien du §4.
