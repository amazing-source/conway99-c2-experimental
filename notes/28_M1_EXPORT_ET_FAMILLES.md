# 28 — Mélanges M1 : lemme de scission, lemme d'export, et trois familles tuées (26/09/2026)

Session principale C2. Tout est à la main (aucun calcul machine). **Statut : DÉRIVÉ, à relire.**

Cadre M1 (note 26) :
- Σ = ∅ et pas de carré disjoint ;
- les paires tordues forment un seul cycle T de longueur n ;
- toutes les autres paires sont ancrées, orientées vers leur ancre.

Rappels de la note 26 :
- les blocs de T ont d ≤ 2 ;
- un bloc hors de T a d ∈ {0, 2, 3, 6} ;
- un « C-bloc » est un bloc hors de T de degré 3, et il y en a au plus deux ;
- A désigne un bloc de degré 6 (a ∈ {0,1}) ;
- familles possibles : a = 0 donne (c, n) ∈ {(0,7), (1,6), (2,5)}, avec tous les blocs de T de degré 2 ; a = 1 donne c ≤ 2 et
  n ≤ 6 − c.

## 1. Lemme de scission (SL), général en Σ = ∅ avec des carrés « un bloc »
Un **troisième bloc** est un bloc k qui porte au moins une étiquette libre. Autrement dit, c'est le troisième bloc du carré d'au
moins une orbite, et c'est le cas de tout bloc de degré < 6.

**Lemme 28.1.** En tout troisième bloc k, G_k est de type (6), (4,2) ou (3,3).
- Un cycle D fermé en k (mono-pivot, toutes ses paires ancrées en k et appariées par k) est une composante de G_k. Il y en a au
  plus un, et sa longueur est au plus 3.
- En type (3,3), pour toute orbite X de troisième bloc k (de pivot i et de bras partenaire j) : j est dans la composante qui ne
  contient pas i, et les deux racines supplémentaires w, w′ de x aussi.

*Preuve.* C'est le raffinement A de « structures » (note 26 §6) : par l'équilibre composante par composante, une composante qui ne
contient pas i a b ≤ [j ∈ C] + 2 ≤ 3, et b ≥ 2 en Σ = ∅. Un cycle fermé ne contient jamais i. En effet D(X) ⊂ {i, k} est appariée
par i, donc la paire {i, k} a une étiquette libre en k. ∎

**Conséquence.** Hors de T (t_k = 0), toutes les paires ancrées en k sont sur des cycles fermés, donc d_k ≤ 3. On retrouve la queue.

## 2. Lemme d'export des C-blocs
**Lemme 28.2.** Soit k un C-bloc : hors de T, d_k = 3, triangle fermé sur In(k), et G_k = (3,3) avec les composantes In(k) et
Out(k). Alors, **pour tout o ∈ Out(k), les voisins D, au pivot o, de la paire {o, k} sont des paires {o, j} avec j ∈ In(k).**
*Preuve.* Les deux orbites de {o, k} sont appariées par o (paire ancrée en o). Leurs partenaires X ⊂ {o, j} ont pour troisième bloc
k, avec i = o ∈ Out(k). Par 28.1 (3,3), on a j ∈ In(k). ∎

**Règle de tête** (26.3) : entre deux bras d'un même carré, un arc ancré a une queue de degré ≤ 2. Un C-bloc est donc toujours la
tête de ses arcs vers les autres éléments d'un In.

## 3. Trois familles de M1 sont impossibles
**Théorème 28.3.** Les familles (a, c) = (0, 1), (0, 2) et (1, 2) de M1 sont impossibles.

**(a = 0, c = 1)**, donc n = 6 et tous les blocs de T de degré 2.
- Soit C le C-bloc, In(C) = {p, q, r} et Out(C) = {s, u, v} ; les six sont dans T.
- Pour o ∈ Out(C), on a In(o) = {C, j′(o)}.
- 28.2 impose que les voisins D de {o, C} en o soient des paires {o, j} avec j ∈ {p, q, r}. On passe en revue les structures
  possibles en o :
  - structure liée sur In(o) : j′(o) ∈ {p, q, r} ;
  - chemin Tw – {o,C} – {o,j′} – Tw′ (ou l'ordre inverse) : j′(o) ∈ {p, q, r}, et le Tw adjacent aussi ;
  - chemin Tw – {o,C} – Tw′ : impossible, car {o, j′} resterait seule, ce qui ferait une boucle.
- Donc s, u et v reçoivent chacun leur second arc depuis {p, q, r}.
- Comptage dans T : les 9 paires ancrées donnent Σ des degrés internes = 9 = 3·1 (s, u, v) + 3·2 (p, q, r). Donc aucune paire de
  {s, u, v} n'est ancrée : elles sont toutes tordues.
- {s, u, v} serait alors un triangle de T, alors que T est un 6-cycle. Contradiction.

**(a = 0, c = 2)**, donc n = 5.
- On pose C₁ → C₂. Par la règle de tête, les deux autres éléments p, q de In(C₂) pointent vers C₁. Donc In(C₁) = {p, q, r}.
- T = {p, q, r, s, u}, Out(C₁) = {C₂, s, u} et Out(C₂) = {r, s, u}.
- On a In(s) = {C₁, C₂}, car d_s = 2. Par 28.2 appliqué à C₁, les deux voisins D de {s, C₁} doivent être des {s, j} avec
  j ∈ {p, q, r}.
- Or ni {s, C₂} ni une paire ancrée ne conviennent : il faudrait le chemin Tw – {s,C₁} – Tw′, et {s, C₂} serait alors seule, ce qui
  ferait une boucle. Contradiction.

**(a = 1, c = 2).**
- Même début : C₁ → C₂, In(C₂) = {C₁, p, q}, In(C₁) = {p, q, r}. Les « autres » sont {p, q, r, s}.
- Donc In(s) ⊇ {C₁, C₂}, puis In(s) = {C₁, C₂} puisque d_s ≤ 2.
- Si s ∉ T : la structure liée {s,C₁} – {s,C₂} contredit 28.2, car C₂ ∉ In(C₁).
- Si s ∈ T : même contradiction que ci-dessus. ∎

## 4. Ce qui reste dans M1
- **(a = 1, c = 1)**, n ∈ {3, 4, 5}. 28.2 impose que s, u ∈ Out(C) ∖ {A} reçoivent un arc de In(C), ou, si d = 1 et s ∈ T,
  que leurs deux voisins sur T soient dans In(C).
  - Pour n = 3, le cas « le bloc de degré 1 est s » meurt : s → u donnerait j′(u) = s ∉ In(C).
  - Il reste un squelette survivant à ce niveau : T = {p, s, u} avec d_p = 1, In(s) = {C, j_s} et In(u) = {C, j_u}, j_s, j_u ∈ {q, r}.
  - Il faut l'équilibre croisé ou le budget.
- **(a = 1, c = 0)**, n ∈ {3, …, 6} : non traité.
- **(a = 0, c = 0)** = H (T hamiltonien, tous les degrés égaux à 2). Il contient H-β, qui est dans le cœur. Le circulant α est mort
  (27.2).

**Bilan M1** : sur les six familles (a, c), trois sont tuées à la main, et le circulant de H aussi. Restent (1,1), (1,0) et H hors
circulant.

## 5. Lemme d'exclusion par paire liée (général), et la famille (a = 1, c = 1) à n = 3
**Lemme 28.4 (exclusion liée).** Supposons réunies les trois conditions suivantes :
- (i) en un bloc c, il y a une structure liée fermée sur {i, k}, c'est-à-dire une composante L_c = {i, k} ;
- (ii) il existe un carré de pivot i et de bras j, k, qui donne l'orbite (i, j, k) avec j ∉ {i, k} ;
- (iii) G_k = (4,2), avec L_k la paire liée en k, M_k les 4 autres blocs formant une seule composante, et j ∉ L_k.

Alors c'est une contradiction.

*Preuve.* Soit x dans l'orbite (i, j, k).
- **En c.** L_c = {i, k} et j ∉ L_c. On a φ_x({c, i}) = 0 par F1, car c ≠ k. Par l'équilibre (27.1), φ_x({c, k}) = 2 − 1 = 1.
- **En k.** i ∈ M_k, car {i, k} a une étiquette libre en k. j ∈ M_k par (iii). La composante M_k est donc serrée : les racines de x
  dans M_k sont exactement v et σv, d'où φ_x({k, r}) = 0 pour tout r ∈ M_k ∖ {i}.
- Or i → c et k → c (car i, k ∈ In(c)), donc c ∈ Out(k) ⊂ M_k. Donc φ_x({k, c}) = 0. Contradiction. ∎

(iii) vaut automatiquement en un bloc hors de T de degré 2, ainsi qu'en un bloc α de T de degré 2 (structure liée plus chaîne
directe).

**Famille (a = 1, c = 1), n = 3.** Notations : In(C) = {p, q, r}, Out(C) = {A, s, u}.
- Par 28.2 et les comptages (§4), T = {p, s, u}, d_p = 1, et j_s, j_u ∈ {q, r}.
- À symétrie près (s ↔ u, q ↔ r), il reste trois squelettes :
  - **S1** : q→s, q→u, s→r, u→r, r→p, p→q, r→q ;
  - **S2** : q→s, r→u, s→r, u→q, p→q, q→r, r→p ;
  - **S3** : q→s, r→u, s→r, u→q, p→r, r→q, q→p.
- **S2 est impossible.** Le carré {s,C} – {s,q} existe en s, que s soit α (structure liée) ou β (chemin p – C – q – u) : il donne
  l'orbite (s, C, q). On a L_r = {s, q}, et G_q = (4,2) avec L_q = {u, p} ∌ C. 28.4 s'applique.
- **S3 est impossible.** L'orbite (u, C, r) existe en u, que u soit α ou β. On a L_q = {u, r}, et G_r = (4,2) avec L_r = {s, p} ∌ C.
  28.4 s'applique.
- **S1 : α en s et en u à la fois est impossible.** L'orbite (s, p, u) du carré de chaîne en s, avec L_r = {s, u}, contredit 28.4 en u,
  car p ∉ L_u = {C, q}.
  - Restent (α_s, β_u), (β_s, α_u) et (β_s, β_u).
  - Pour l'orbite (s, p, u) dans (α_s, β_u), le profil complet d'équilibre, sur les 5 blocs et avec F1, est **réalisable** (solution
    explicite trouvée à la main). Un profil isolé ne suffit donc pas. Il faudra les interactions entre orbites : le budget, ou
    l'ordre des cycles libres.

**Bilan provisoire de (1,1).** À n = 3, seul S1 avec au moins un bloc β survit. n = 4 et n = 5 sont à traiter. Pour n = 4, le cas
« z de degré 0 » donne un squelette avec T = q – r – s – u et les diagonales s → q, u → r, où il faut examiner les choix α/β.

## 6. Famille H (T hamiltonien, tous les degrés égaux à 2) : ce que 28.4 tue
Petit test machine, **quelques secondes** (`scripts/h_linked_exclusion.py`, `logs/h_linked_exclusion.log`). Il n'applique que le
lemme 28.4, démontré ci-dessus.
- Il y a 60 orientations eulériennes de K₇ − C₇.
- En chaque bloc on a trois choix : α, ou β avec l'un des deux ordres du chemin. Soit 131 220 squelettes.

**Contrôles.**
- Le circulant m → m+2, m+3 tout-α est tué, comme au 27.2.
- Tous les squelettes tout-β survivent (7 680 = 60 × 2⁷). C'est attendu : G_c est connexe partout, c'est le cœur.

**Résultat.**
- 28.4 tue 60 678 squelettes sur 131 220.
- Il en reste 70 542. Par nombre de blocs α : 0 → 7 680, 1 → 26 880, 2 → 25 312, 3 → 8 904, 4 → 1 610, 5 → 140, 6 → 14, 7 → 2.
- **Les deux survivants tout-α** sont les circulants m → m+2, m → m−3 (In(c) = {c−2, c+3}) et son miroir.
  - Pour l'orbite de chaîne (0, 6, 1), j'ai écrit à la main le profil d'équilibre complet sur les 5 blocs, avec F1 et les sommes
    proches et lointaines.
  - Ce système est réalisable. Solution : n = (0,1,1,0,0) ; φ(14) = φ(15) = φ(23) = φ(24) = φ(25) = φ(34) = φ(35) = φ(45) = 1 ;
    φ(12) = φ(13) = 0.
  - Un profil isolé ne tue donc pas ce squelette.

**Leçon.** 28.4 est un filtre réel, mais faible sur H. La suite demande des arguments qui couplent plusieurs orbites (le budget des
doubles, l'ordre des cycles libres), comme « structures » en tout-tordu. Le circulant (+2, −3) tout-α, très symétrique (Z₇), est la
cible naturelle suivante, analogue du Paley du carnet.

## 7. Lemme de la paire propre liée (28.5), et le circulant (+2, −3) est mort
**Lemme 28.5 (général en Σ = ∅, carrés « un bloc »).** Supposons qu'un bloc c porte une structure liée fermée sur {a, b}, et que la
paire {a, b} soit ancrée en b (a → b). Alors f_a ≥ 8, où f_a = 2·out_a + t_a est le nombre d'orbites libres en a.
*Preuve.*
- Les deux orbites sœurs x₁, x₂ de {a, b} sont libres en a (appariées par b) et évitent c.
- En c, leur paire est contenue dans L_c. Par l'équilibre, elles n'ont aucune racine dans les carrés liés de c, donc φ_x({c, a}) = 0.
- Leurs voisins sur le graphe libre en a ne sont donc ni des orbites de {a, c} (paire ancrée en c, libre en a), ni leur sœur.
- Il reste R, formé des f_a − 4 autres orbites libres. Si |R| ≤ 2, les deux sœurs ont le même ensemble R de voisins : elles ont
  deux voisins communs, et un 4-cycle se ferme, contre 19.1. ∎

**En H** (f = 2·2 + 2 = 6 partout) : **un bloc α ne peut pas avoir ses deux prédécesseurs reliés par une corde.** Ses prédécesseurs
sont donc consécutifs sur T.
- **Le circulant (+2, −3) tout-α en meurt.** On a In(4) = {2, 0}, avec la corde 0 → 2 et Out(0) = {2, 4}.
- Vérifié aussi à la main par le profil de l'orbite de {0, 2} : l'équilibre en 4 donne n₄ = 0, puis n₁ = n₆ = 1 pour les deux
  sœurs.
- Son miroir meurt aussi. **Aucune configuration tout-α de H ne survit.**

**Recomptage** (`scripts/h_linked_exclusion2.py`, `logs/h_linked_exclusion2.log`, quelques secondes).
- 28.4 et 28.5 laissent **30 346** squelettes de H sur 131 220.
- Par nombre de blocs α : 0 → 7 680, 1 → 14 336, 2 → 7 168, 3 → 1 148, 4 → 14. **Au plus 4 blocs α.**
- Chaque bloc α a ses prédécesseurs consécutifs sur T.

**Dans M1 hors de H**, 28.5 ne tue pas S1. Pour la paire liée {p, r} en q (r → p), on a f_r = 8. Pour {C, q} en s et en u, on a
f_q = 8.

**Où en est M1.**
- (0,1), (0,2) et (1,2) sont morts.
- (1,1) à n = 3 : seul S1 avec au moins un β survit. n = 4 et n = 5 restent.
- (1,0) : non traité.
- H : il reste les squelettes à au plus 4 blocs α, plus le tout-β, qui est le cœur.
