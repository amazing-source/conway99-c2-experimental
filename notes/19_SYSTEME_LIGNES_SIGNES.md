# 19 — Systèmes de lignes, système χ signé, et cœur sans grille (24/09/2026)

Suite de la note 18. Les deux chantiers ouverts sont traités par ordre d'importance :
- **(a)** le cœur sans grille (Σ = ∅) ;
- **(b)** les 39 graphes Σ survivants (`data/survivors39.txt`).

Consigne : chercher la manière la plus instructive, pas la plus rapide.

**Choix de méthode.** Un « système χ à défauts » pour les paires D de types one et dis n'est pas une bonne abstraction. Pour une paire D
de type one, de pivot i, les 30 orbites qui évitent i se répartissent ainsi (DÉRIVÉ de (Q1)–(Q4)) :
- 1 orbite commune ;
- 9 orbites voisines de U seulement ;
- 9 orbites voisines de D(U) seulement ;
- 11 orbites voisines d'aucune des deux.

Ces domaines ne sont fixés par aucune structure de blocs, contrairement au cas sœur, où l'on a une partition 10 + 10 de O_p. Les
paramétrer reviendrait à réécrire l'étage Q sous un autre nom.

On étudie donc directement les **systèmes de lignes** : les contraintes exactes du modèle qui ne portent que sur les lignes d'un
ensemble S d'orbites. On cherche ce qu'elles voient, et à partir de quelle taille.

Scripts :
- `scripts/row_system.py` : RS(S), étage Q.
- `scripts/row_system_full.py` : RSF(S), modèle complet.
- `scripts/rs_experiments.py`, `scripts/schi_system.py`, `scripts/schi_onehot.py`, `scripts/schi_cms.py`, `scripts/schi_soundness.py`,
  `scripts/schi_classify.py`, `scripts/schi_mus.py`, `scripts/make_rsf_cnf.py`, `scripts/list_survivors.py`, `scripts/survivor_max.py`.

## 1. RS(S) : l'étage Q restreint aux lignes de S (CALCULÉ)

**Définition.** RS(S) est l'ensemble des contraintes de `vendor/stage_q.constraints(7)` dont toutes les variables Q[U,W] vérifient
U ∈ S ou W ∈ S. L'encodage du dépôt est repris tel quel, puis filtré par support. Concrètement, RS(S) contient :
- pour chaque U ∈ S : la somme de ligne, l'unique 2 et les 7 sommes par bloc ;
- pour U ≠ U′ dans S : les équations de Gram.

C'est une **relaxation** de l'étage Q. Avec Σ imposée sur les paires portant une orbite de S (`sigma`) :

> RS(S) UNSAT ⇒ étage Q UNSAT ⇒ configuration impossible.

**Validation (`python scripts/rs_experiments.py validate`) :**
- m = 2 : RS(toutes les orbites) est SAT.
- m = 3 : RS(toutes les orbites) est UNSAT, comme `stage_q --validate`.
- m = 7 : RS(toutes les orbites) sélectionne 2100 contraintes sur 2100.

**RS(orbites sœurs) ≡ système χ (`logs/rs_chi.txt`).**
- Les 11 atomes sont UNSAT (1 à 6 s).
- Les 12 graphes χ-SAT maximaux sont SAT (0,2 à 1,9 s).

Par monotonie, les deux systèmes ont donc le même verdict sur les 1044 graphes. Le système χ (note 18) capture **toute** l'information
de l'étage Q contenue dans les lignes sœurs. Pour aller plus loin, il faut des lignes non sœurs, ou des signes.

## 2. RSF(S) : le modèle complet restreint aux lignes de S (CALCULÉ)

`row_system_full.build` recopie `vendor/orbit_sat.build` instruction par instruction : même ordre d'appels, mêmes identifiants. Il y
ajoute un filtre de support : une contrainte (R), (D), (I) ou (P) n'est gardée que si toutes ses variables a[U,V], b[U,V] ont U ∈ S
ou V ∈ S.

**Validation octet pour octet.** RSF(toutes les orbites) avec les paires de K2K2P3 reproduit `data/cnf/K2K2P3.cnf` :
- vars = 666183, clauses = 1510454 ;
- sha256 = 7ab7737d…, identique à celle du MANIFEST.

RSF(S) est donc exactement un sous-ensemble des contraintes du modèle complet certifié.

## 3. Résultat principal : il manque les signes, pas des lignes (CALCULÉ)

On prend RSF(orbites sœurs), c'est-à-dire le modèle complet sur les **seules lignes sœurs**, signes a/b compris
(`logs/rsf_sister.txt`) :

| Configuration (χ-SAT) | Certifiée dans le modèle complet ? | RSF(lignes sœurs) |
|---|---|---|
| K2K2P3 = 12 34 56 67 | oui (DRAT) | **UNSAT** 2,6 s |
| K2P5 = 12 34 45 56 67 | oui | **UNSAT** 3,8 s |
| K2spider = 12 34 45 47 56 | oui | **UNSAT** 4,2 s |
| P4P3 = 12 23 37 45 56 | oui | **UNSAT** 3,9 s |
| g06_03276f8462 = 12 24 25 47 56 67 | oui | **UNSAT** 104 s |
| g06_0fa0ea004a = 23 34 36 47 56 67 | oui | **UNSAT** 127 s |
| g06_177a07b777 = 23 25 36 47 56 67 | oui | **UNSAT** 18,5 s |
| S7c = 23 26 34 35 47 56 67 | oui | **UNSAT** 25,8 s |
| **S6 = 12 26 27 47 56 67** | **non** (survivant maximal) | **UNSAT** 141,6 s |
| K4 = 12 13 14 23 24 34 | non | TIMEOUT 300 s |

Les huit configurations χ-SAT tuées par le modèle complet le sont déjà par les lignes sœurs seules, **dès qu'on garde les signes**.
Le système χ perd une information décisive en ne gardant que l'orbite du voisin de grille, et non le voisin lui-même.

## 4. Le système χ signé (DÉRIVÉ)

**Données.** Pour une paire sœur p = {i<j} :
- la grille G_p = {±r_p, ±r′_p}, avec r_p = rep U_p⁺ = {(i,0),(j,0)} et r′_p = rep U_p⁻ = {(i,0),(j,1)} ;
- par G1 (note 04), toute racine w évitant p a exactement un voisin c_p(w) ∈ G_p, et c_p(−w) = −c_p(w) (note 03, S1(4)) ;
- au niveau des orbites : c_p(rep W) = σ_p(W) · rep U_p^{χ_p(W)}, avec χ_p ∈ Z₂ (note 18) et un **signe** σ_p(W) = ±1 ;
- σ = +1 si a[U_p^χ, W] = 1, et σ = −1 si b[U_p^χ, W] = 1.

Notation : s_ℓ(r) désigne le signe en ℓ de la racine r.

Les contraintes suivantes sont dérivées des équations (I) et (P) de `orbit_sat`, restreintes aux lignes sœurs.

**(sbloc)** Pour p, ε et ℓ ∉ p : parmi les 4 orbites W ⊂ O_p qui rencontrent ℓ et ont χ_p(W) = ε, exactement 2 vérifient
π_ℓ(W) := σ_p(W)·s_ℓ(rep W) = +1.
*Source :* (I) pour U_p^ε et c = (ℓ,±). La racine rep U_p^ε a exactement 2 voisins racines contenant (ℓ,0) et 2 contenant (ℓ,1).
Ce sont tous des voisins non de grille, et π_ℓ(W) est le signe en ℓ de celle des deux racines de W qui est envoyée sur +rep U_p^ε.

**(sbij)** Pour p, q disjointes : c_p(rep U_q^f) = z·rep U_p^e ⟺ c_q(rep U_p^e) = z·rep U_q^f.
*Source :* l'adjacence est symétrique. L'adjacence entre G_p et G_q est donc une bijection β_pq, t-équivariante, qui envoie sœurs sur
sœurs (note 03) : une « connexion D₄ ».

**(sdisj)** Pour p, q disjointes, et pour les 6 orbites W sur les 3 blocs restants, on pose ρ(W) = σ_q(W)·σ_p(W)·σ_q(U_p^{χ_p(W)}).
Alors ρ(W) = +1 exactement quand c_q(rep W) = β_pq(c_p(rep W)). Contrainte : pour chaque ε, **exactement une** des 3 orbites W
avec χ_p(W) = ε vérifie ρ(W) = +1.
*Source :* (P) pour (u, v) ∈ G_p × G_q. Le nombre de voisins racines communs vaut 2 − [u ~ v]. On compte :
- le terme de grille de p, qui vaut [orb c_p(v) ≠ orb u] ;
- le terme de grille de q ;
- les racines w des paires restantes telles que c_p(w) = u et c_q(w) = v.

On obtient :
- n(u, β(u)) = 1 ;
- n(u, −β(u)) = 2 ;
- n = 0 si v est dans l'autre orbite de q.

C'est le décompte « 4 alignées, 8 anti-alignées » de la note 03, qui n'avait pas été intégré au système χ.

**Holonomie.** Si r ⊂ C est elle-même une paire sœur, ρ(U_r^±) vaut +1 exactement quand l'holonomie β_rq β_pr β_qp… de la connexion
autour du triangle de paires disjointes fixe rep U_r^±. La partie non signée (cocycle) force cette holonomie dans le groupe de Klein
{id, t, s₁, s₂} ⊂ D₄. (sdisj) relie ainsi les holonomies des triangles voisins.

**(sint)** Pour p = {i,j} et q = {i,k} : pour chaque couple (e,f), parmi les 3 orbites W (hors de {i,j,k}) telles que
(χ_p, χ_q)(W) = (e,f), **exactement une** vérifie s_i(c_p(rep W)) = s_i(c_q(rep W)).
*Source :* (P) donne #{w : c_p(w) = u, c_q(w) = v} = 2 − |u ∩ v| = 2 − [s_i(u) = s_i(v)], puisque u ≁ v et qu'il n'y a pas de voisin
commun de grille.

**Conséquences de parité (DÉRIVÉ).** Toute cardinalité « exactement k » implique une équation XOR de parité k. Certaines ne dépendent
pas de χ :
- (L1) Σ_{W ∈ O_p, W ∋ ℓ} Z_p(W) ≡ #{m ∉ p ∪ {ℓ} : m < ℓ}, où Z = [σ = −1] ;
- (L2) Σ_{W ∈ O_p∩O_q} (Z_p + Z_q)(W) ≡ 0, pour p et q sécantes ;
- (L3) Σ_{W ∈ C} (Z_p + Z_q)(W) + Z_q(U_p⁰) + Z_q(U_p¹) ≡ 0, pour p et q disjointes.

**Correction.** Une première version de cette note affirmait, sans l'avoir calculé, que ces équations étaient compatibles pour K₁,₃.
C'était **faux**. Elles sont incohérentes pour K₁,₃, et c'est le lemme des étoiles (§6 bis). Pour les graphes de degré ≤ 2, elles
sont cohérentes (`logs/parity_classify.txt`).

**Contrôles (CALCULÉ).**
- **Correction par transfert de modèles** (`scripts/schi_soundness.py`). Sur 8 configurations où RSF(lignes sœurs) est SAT (67 ; 23 34 ;
  17 56 ; 13 15 35 ; 17 56 67 ; 23 34 67 ; 15 24 67 ; 23 25 36 56), qui instancient toutes les familles, on a :
  - S1 vérifié ;
  - le (χ, σ) lu dans le modèle RSF, imposé à schi, donne SAT dans 8 cas sur 8.
- **Accord sur les verdicts UNSAT.** schi_system donne UNSAT sur les 9 configurations du §3, en 1,1 à 52 s, soit 3 à 60 fois plus vite
  que RSF.
- **Deuxième encodage** (`schi_onehot.py`, « un parmi quatre », sans XOR) : verdicts identiques (K2K2P3 UNSAT, S6 UNSAT, P3+K2 SAT,
  C4 SAT).

## 5. Classification sous le système signé (CALCULÉ : `logs/schi_classify.txt`, `logs/schi_deg2.txt`)

On a passé les 56 graphes χ-SAT au système signé, par ordre croissant du nombre d'arêtes :
- limite 600 s ;
- 120 s pour ceux qui contiennent K₁,₃ ; ils échouent tous par TIMEOUT, puis tombent tous au §6 bis.

| Graphe (degré ≤ 2) | Survivant ? | Système signé |
|---|---|---|
| ∅, 67, 23 34, 17 56, 13 15 35 (K₃), 17 56 67 (P₄), 23 34 67, 15 24 67 (3K₂), 23 25 36 56 (C₄), 12 23 34 45 (P₅), 17 24 56 67 (P₄+K₂), 14 15 36 37 (2P₃) | oui | **SAT** (0,0–0,5 s) |
| **12 15 23 34 45 (C₅)** | oui (maximal) | **UNSAT** 2,6 s |
| **12 17 45 56 67 (P₆)** | oui (maximal) | **UNSAT** 19,5 s (un parmi quatre) |
| **25 34 36 47 67 (C₄+K₂)** | oui (maximal) | **UNSAT** 9,1 s (un parmi quatre) |
| 17 23 34 56 (contient K2K2P3) | non | UNSAT 2,7 s (contrôle cohérent) |

Les trois survivants de degré ≤ 2 tués ici sont **certifiés par DRAT** sur RSF (§8).

**Contrôle direct dans RSF.** Pour les 11 survivants non vides, RSF(lignes sœurs) est **SAT** :
- 7 cas dans `logs/rsf_classify.txt` : 67, 23 34, 17 56, 17 56 67, 23 34 67, 15 24 67, 23 25 36 56 ;
- P₅, P₄+K₂, 2P₃ et K₃ en 0,0–4,3 s (nouvelle passe). L'information des lignes sœurs, signes compris, est donc bien épuisée pour
eux. Ce constat ne dépend pas de l'équivalence entre schi et RSF.

## 6. Les étoiles : pourquoi elles résistent, et la contrainte (aug)

K₁,₃ (12 16 17) résiste à tous les solveurs essayés :

| Solveur / encodage | Limite | Verdict |
|---|---|---|
| cadical, schi | 600 s | TIMEOUT |
| cadical, RSF | 300 s | TIMEOUT |
| CryptoMiniSat + parités | 600 s | TIMEOUT |
| CryptoMiniSat + parités + (aug) | 600 s | TIMEOUT |
| kissat (Docker) | 1200 s | UNKNOWN |
| cadical, un parmi quatre | 240 s | TIMEOUT |

L'instance est pourtant minuscule : 120 variables primaires (60 χ et 60 σ), 3204 variables, 7596 clauses.

**(aug) (DÉRIVÉ).** Pour une orbite W quelconque et un bloc ℓ ∉ W, (I) pour la ligne de W donne exactement 2 voisins racines de rep W
contenant (ℓ,0), et 2 contenant (ℓ,1). Parmi eux figurent les voisins de grille c_p(rep W), pour p sœur avec ℓ ∈ p et p ∩ W = ∅.
Donc **au plus 2 voisins de grille de chaque signe en ℓ**. C'est non trivial dès que g = #{p} ≥ 3 : dans une étoile K₁,₃ de centre c,
les 3 signes en c des voisins de grille d'une racine des paires hors étoile ne sont pas tous égaux.

**Explication (CALCULÉ, §6 bis).** La contradiction est une pure affaire de parité, mais **son certificat n'est pas linéaire dans
les variables des solveurs**. Il faut sommer, pour chaque orbite, les contributions des deux classes χ = 0 et χ = 1, c'est-à-dire
utiliser l'identité [χ=0]·Z + [χ=1]·Z = Z. Or dans CNF + XOR, [χ=ε]·Z est une variable auxiliaire (un ET), et cette identité n'est pas
linéaire en ces variables. L'élimination de Gauss de CryptoMiniSat ne la voit donc pas, et le CDCL doit énumérer les χ un par un.
Chacun est réfuté en 0,0 s, mais ils sont très nombreux.

## 6 bis. LEMME DES ÉTOILES : trois paires sœurs ne partagent jamais un bloc (DÉRIVÉ, preuve humaine courte)

### Comment on l'a trouvé (CALCULÉ)

1. À χ fixé, le système signé de K₁,₃ est réfuté **instantanément** : 12 χ tirés au hasard, 0,0 s chacun (`scripts/schi_fixchi.py`),
   avec ou sans (aug). La difficulté pour les solveurs vient donc uniquement du nombre énorme de χ.
2. Les noyaux à χ fixé (`scripts/schi_mus_fixed.py`) sont de deux types :
   - (sbloc) d'une seule paire, sur ses 5 blocs ;
   - (sbloc) + (sint) des trois paires.
3. Paire seule, énumération exhaustive (`scripts/signable_chi.py`) : 3436 χ_p valides (fibre + bloc), dont 1712 signables.
   **Signable ⟺ #{orbites « − » W avec χ_p(W) = 1} pair**, sans aucune exception sur les 3436.
4. Pour 300 χ tirés, le système linéaire de parité L(χ) (conséquences XOR de (sbloc) et (sint)) est **incohérent 300 fois sur 300**,
   comme le système exact (`scripts/parity_star.py`).
5. Les certificats minimaux d'incohérence (`scripts/parity_cert.py`) :
   - soit 5 équations (la parité d'une paire seule) ;
   - soit 28 équations qui, sommées, **ne dépendent plus de χ**.
6. D'où le système de parité indépendant de χ, (L1) + (L2) + (L3) (`scripts/parity_L12.py`). Il est **incohérent pour K₁,₃**, avec
   un certificat de 9 équations : 6 × (L1) et 3 × (L2).

**Classification par la parité seule** (`scripts/parity_classify.py`, `logs/parity_classify.txt`) :
- Avec (L1)–(L3) : 1015 graphes sur 1044 sont incohérents ; **l'unique atome est K₁,₃**. Les 29 graphes cohérents sont exactement
  ceux de degré maximal ≤ 2 (unions disjointes de chemins et de cycles).
- On ajoute (L4), tiré de (sbij) sommé : Z_p(U_q⁰) + Z_p(U_q¹) = Z_q(U_p⁰) + Z_q(U_p¹), indépendant de χ puisque la bijection
  apparie les orbites. On obtient 1016 incohérents, avec un **second atome : K₃ + C₄** (12 15 25 34 36 47 67, degré 2). Il était déjà
  exclu, car il contient K₃ + K₂.
- La parité indépendante de χ ne tue aucun des 12 survivants. Les éliminations de C₅, P₆ et C₄+K₂ passent par des cardinalités ou
  par des parités qui dépendent de χ.

### Énoncé et preuve (DÉRIVÉ)

**Lemme des étoiles.** Si {c,a}, {c,b}, {c,d} sont trois paires sœurs, on aboutit à une contradiction. Donc **Σ est de degré
maximal ≤ 2**.

*Notations.*
- L = {a, b, d} (les feuilles) et R = les 3 autres blocs.
- Pour x ∈ L : G_x = {±e_c ± e_x}, la grille de la paire {c,x}.
- Pour une racine w évitant {c,x} : c_x(w) ∈ G_x est son unique voisin dans G_x (G1, note 04), avec c_x(−w) = −c_x(w).
- τ_x(w) := s_c(c_x(w)) ∈ {±1} est le signe en c de c_x(w). On a τ_x(−w) = −τ_x(w).

**Fait A** (μ = 2 ; c'est (I)). Soit ℓ ∉ {c,x}. Parmi les 8 racines qui contiennent +e_ℓ et évitent {c,x}, exactement 4 ont
τ_x = +1.
*Preuve.*
- Soit g ∈ G_x avec s_c(g) = +. Comme g ≁ e_ℓ, μ(g, e_ℓ) = 2. Les voisins de e_ℓ sont x, −e_ℓ et les racines contenant +e_ℓ. Les
  deux voisins communs sont donc des racines contenant +e_ℓ.
- Par S1(a), les voisins de g qui rencontrent c ou x sont seulement ses deux voisins de grille. Les deux voisins communs évitent donc
  {c,x}.
- Les deux racines de G_x de signe + en c donnent ainsi 2 + 2 racines, distinctes par unicité de c_x. ∎

**Fait B** (μ = 2 ; c'est (P)). Soient x ≠ y dans L. Parmi les 12 orbites de racines qui évitent {c,x,y}, exactement 4 vérifient
τ_x = τ_y. (Changer w en −w change les deux signes, donc la propriété ne dépend pas du représentant.)
*Preuve.*
- Soient g ∈ G_x et h ∈ G_y de même signe en c. Par S1(a), g ≁ h. Ils partagent le sommet intérieur (c, ±) et aucun autre. Par
  μ = 2, ils ont donc exactement un voisin racine commun. Par S1(a) appliqué aux deux grilles, ce voisin évite {c,x,y}.
- Inversement, toute racine w évitant {c,x,y} avec τ_x(w) = τ_y(w) est ce voisin commun pour (g, h) = (c_x(w), c_y(w)).
- Il y a 2 · 2 · 2 = 8 tels couples (g, h), donc 8 racines, donc 4 orbites. ∎

**Parité.**
- On choisit un représentant w_W dans chaque orbite W qui évite c, et on pose ε_ℓ(W) = s_ℓ(w_W) pour ℓ ∈ W.
- La racine de W qui contient +e_ℓ est ε_ℓ(W)·w_W. Le fait A s'écrit donc :

  Π_{W ∋ ℓ, W ∩ {c,x} = ∅} τ_x(w_W) = Π_{W ∋ ℓ, W ∩ {c,x} = ∅} ε_ℓ(W).     (A_{x,ℓ})

- Le fait B s'écrit : Π_{W ∩ {c,x,y} = ∅} τ_x(w_W) τ_y(w_W) = (+1)⁴ (−1)⁸ = +1.     (B_{x,y})

On multiplie les six (A_{x,ℓ}), pour x ∈ L et ℓ ∈ L ∖ {x}, puis les trois (B_{x,y}).

*Membres de gauche : ils sont égaux.* Pour x fixé :
- dans A, les orbites sur la paire des deux autres feuilles apparaissent deux fois et se simplifient ; il reste les orbites sur
  {y,r} et {z,r}, avec r ∈ R ;
- dans B, τ_x apparaît dans B_{x,y} et dans B_{x,z}, sur les orbites {z,r} ∪ (paires de R) et {y,r} ∪ (paires de R) ; les paires de R
  se simplifient.

*Membres de droite : ils diffèrent.*
- Dans A, les orbites sur {ℓ,r} apparaissent deux fois et se simplifient. Pour chaque paire de feuilles {ℓ,z}, il reste
  Π_{W sur {ℓ,z}} ε_ℓ(W)ε_z(W).
- Ce produit vaut (+1)·(−1) = −1, car l'orbite ±(e_ℓ + e_z) a des signes égaux et l'orbite ±(e_ℓ − e_z) des signes opposés,
  quel que soit le représentant.
- Avec 3 paires de feuilles, le produit A vaut (−1)³ = −1, alors que le produit B vaut +1. **Contradiction.** ∎

### Ingrédients et contrôles

La preuve n'utilise que :
- G1 (Wilbrink–Brouwer : tout sommet hors d'une grille y a exactement un voisin, note 04) ;
- S1(a) (note 03) ;
- μ = 2, deux fois.

Elle ne dépend d'aucun encodage.

**Pourquoi rien de tel à m = 11 (BvLS, toutes les paires sœurs).** G1 échoue : la grille ne domine que 171 sommets sur 243, donc c_x
n'est pas partout défini. Le Fait A échoue avec lui.

**Contrôles machine** (`logs/star_lemma_check.txt`), tous dans RSF, c'est-à-dire les contraintes du modèle complet certifié sur les
seules lignes sœurs :
- **Fait A** : RSF + (compte ≠ 4) est UNSAT pour 9 couples (p, ℓ), en 0,0–0,2 s chacun. C'est la somme de deux contraintes (I).
- **Fait B, forme éclatée** : pour chaque (e,f), RSF + (Σ_{W ∉ {c,a,b}} (a_{pe,W}a_{qf,W} + b_{pe,W}b_{qf,W}) ≠ 1) est UNSAT. On l'a
  testé sur 12 cas (3 couples de paires × 4 couples (e,f)), en 0,0–0,2 s chacun.
  - C'est l'équation (P) « same », et S1 annule les termes restants.
  - L'accord τ_x = τ_y d'une orbite vaut Σ_{e,f} (aa + bb), puisque, par S1, exactement une des quatre variables a_{p±}, b_{p±}
    vaut 1. D'où le compte 1 + 1 + 1 + 1 = 4.
  - La forme globale (compte ≠ 4 sur l'indicateur d'accord) n'a pas abouti en 40 min de CDCL, qui doit sommer quatre cardinalités.
    Elle a été abandonnée au profit de la forme éclatée.
- Algèbre linéaire du certificat : `scripts/parity_L12.py` (9 équations, incohérentes).

**Certificats DRAT des ingrédients (`scripts/make_star_fact_cnfs.py`, `scripts/cert_starfacts.sh`,
`data/cnf/MANIFEST_starfacts.txt`).** Les 18 implications utilisées pour c = 1 et L = {2,3,4} sont certifiées :
- 6 Faits A ;
- 12 Faits B éclatés.

Chaque CNF « RSF + négation » est UNSAT, avec DRAT VERIFIED (kissat + drat-trim ; lignes `factA_*`, `factB_*` de
`data/cert_results.txt`). Le cas général suit par symétrie S₇ × (Z₂)⁷ du problème : les énoncés des Faits A et B ne dépendent
d'aucune convention de représentant.

**Statut : DÉRIVÉ, ingrédients certifiés.** Le raccord (produit des identités, parité (−1)³) est écrit à la main. Il est vérifié
comme système linéaire sur F₂ (`scripts/parity_L12.py`).

**Portée.** Le lemme tue **24 des 39 survivants**, tous ceux qui contiennent K₁,₃. Il subsume aussi g07_ca15a23af4, K4, allsib et
les atomes 02, 03, 04 et 07–11 du système χ, qui ont tous un sommet de degré ≥ 3. Les atomes restants (01 = K₃+K₂, 05 = C₆,
06 = C₅+K₂) sont de degré ≤ 2 : le système χ reste nécessaire pour eux.

## 7. Le cœur sans grille (a)

**Image géométrique (DÉRIVÉ ; reformulation de la note 07).** Un carré D (u, v, −u, −v) avec ses 4 sommets-triangles forme une grille
3×3 « centrée en x » dont le centre est plus ou moins cassé :
- **sib** : la grille complète par x ;
- **one** : la grille privée de la droite {x, w₀, −w₀}, où ±w₀ sont les racines-triangles ;
- **dis** : la grille privée de x lui-même et de ses deux droites.

Les défauts de Wilbrink–Brouwer valent respectivement 0, 2 et 8 (note 07). Une grille t-invariante contient forcément x : une
involution sur 9 points a un nombre impair de points fixes. **Sans grille par x = sans aucune grille t-invariante.**

**Sondes locales (CALCULÉ).** Aucune ne conclut.

| Système | S | Données | Verdict |
|---|---|---|---|
| RS (étage Q), 4 blocs | 12 orbites | Σ\|B = ∅ ou 1 arête | TIMEOUT 300 s ; les 9 autres graphes : SAT |
| RSF, star(1) | 12 orbites | aucune sœur | TIMEOUT 900 s |
| RSF, orbites de {1,2,3,4} | 12 orbites | aucune sœur | TIMEOUT 900 s |
| RSF, star(1) ∪ star(2) | 22 orbites | aucune sœur | TIMEOUT 900 s |

**Type local d'un bloc (`logs/rsf_star_d.txt`).** On prend RSF(star(1)), sans sœur, avec exactement d arêtes D internes à star(1) :
- d = 5 : **UNSAT** en 6 s. C'est le contrôle attendu : il resterait 2 orbites, et un cycle alterné A₁/B₁ de longueur 2 est impossible.
- d = 6 : TIMEOUT à 900 s.
- d = 0 à 4 : jamais terminés (lot abandonné ; aucune conclusion, relevé lors de la revue du 24/09 au soir).

**Étoiles mixtes (`logs/star_mixed_probe.txt`) : le lemme des étoiles ne s'étend pas localement *sur ces 6 lignes* (non testé sur les 12 lignes de star(1) ; revue du 24/09).** On prend RSF sur les seules lignes
des 6 orbites de trois arêtes D internes à star(1). On obtient **SAT** en 0,1–0,2 s pour chacun de ces cas :
- 2 sœurs + 1 arête one de pivot 1 ;
- 1 sœur + 2 arêtes one ;
- 3 arêtes one.

Or 3 sœurs donnent UNSAT (§6 bis). L'obstruction de parité est propre aux grilles. Elle vient de S1 : le voisin de grille d'une
racine évite les deux blocs de la grille, ce qui échoue pour les carrés D one.

**Structure générale au sommet e_c (DÉRIVÉ, classique).** Par μ = 2 :
- les 60 racines qui évitent c sont en bijection avec les arêtes de K₁₂ − A_c, où A_c est le couplage de N(e_c) ;
- chaque racine w correspond à ses deux voisins de star(c) de signe + en c.

Le Fait B du lemme des étoiles en est un cas particulier : les 4 arêtes entre deux arêtes de A_c.

## 8. Certification (DRAT, `data/cert_results.txt`)

| Nom | CNF | kissat | drat-trim |
|---|---|---|---|
| rsf_S6 | RSF(lignes sœurs) de S6, sha 1479b1c1… (`data/cnf/MANIFEST_rsf.txt`) | UNSAT, 145 s, 1,5 M conflits | **VERIFIED** (preuve 197 Mo) |
| rsf_C5 | RSF(lignes sœurs) de C₅ = 12 15 23 34 45, sha fa1a4be5… | UNSAT, 379 s, 4,8 M conflits | **VERIFIED** |
| rsf_P6 | RSF(lignes sœurs) de P₆ = 12 17 45 56 67, sha a19ea3d5… | UNSAT, 73 s, 0,87 M conflits | **VERIFIED** |
| rsf_C4K2 | RSF(lignes sœurs) de C₄+K₂ = 25 34 36 47 67, sha 899e39a3… | UNSAT, 20 s, 0,31 M conflits | **VERIFIED** |

Pour le lemme des étoiles, pas de DRAT global : le CDCL ne trouve pas le certificat de parité. On a à la place :
- la preuve humaine (§6 bis) ;
- **18 certificats DRAT VERIFIED** pour ses ingrédients : `factA_x{2,3,4}_l*` et `factB_{23,24,34}_{00,01,10,11}`, 0–1 s chacun.

## 9. Bilan

**Corollaire : au plus 4 grilles par x, et au plus 2 par droite de x (DÉRIVÉ, CALCULÉ).** Les 29 graphes de degré ≤ 2 ont été
revus un à un. Tous ceux qui ont 5 arêtes ou plus sont exclus, par un certificat, un atome χ ou le système signé ; plusieurs graphes à
4 arêtes le sont aussi (K2K2P3, K₃+K₂). Donc n_sib = |Σ| ≤ 4. La borne précédente était 7.

**Tâche (b), les survivants : 39 → 12.**
- Le lemme des étoiles élimine les 24 survivants qui contiennent K₁,₃.
- Le système signé élimine C₅, P₆ et C₄+K₂, tous trois certifiés par DRAT sur RSF. S6, qui contient aussi K₁,₃, est lui aussi
  certifié par DRAT.
- Restent 12 graphes, tous de degré ≤ 2 et tous SAT pour le système signé des lignes sœurs (`data/survivors_after19.txt`) :
  ∅, K₂, P₃, 2K₂, K₃, P₄, P₃+K₂, 3K₂, C₄, P₅, P₄+K₂, 2P₃.

**Ce qu'on a appris.**
1. Le système χ (note 18) est exactement « l'étage Q sur les lignes sœurs ». Le complément décisif, ce sont les **signes**, pas d'autres
   lignes. Les 8 configurations χ-SAT mais certifiées UNSAT meurent toutes dès qu'on garde les signes sur les seules lignes sœurs.
2. Le système signé des lignes sœurs est une théorie de jauge : une connexion D₄ sur les paires sœurs (note 03), et des signes σ_p.
   Ses conséquences de parité indépendantes de χ donnent le **lemme des étoiles**. Sa preuve est humaine et courte. Elle n'utilise que
   G1, S1(a) et μ = 2, donc elle est propre à k = 14.
3. Pour tout graphe de degré ≤ 2, l'information des lignes sœurs, signes compris, est **épuisée** : les 12 survivants sont SAT. Il faut
   des lignes non sœurs, exactement comme pour le cœur sans grille. **Les deux tâches se rejoignent.**

**Tâche (a), le cœur sans grille.**
- Aucune sonde locale ne conclut : RS ou RSF sur star(1), sur 4 blocs, sur star(1) ∪ star(2), et le type local d_1.
- Le mécanisme des étoiles ne s'étend pas localement aux carrés D de type one : les étoiles mixtes sont SAT sur leurs lignes.
- L'obstruction, si elle existe, n'est donc pas visible sur ≤ 22 lignes en 15 min. Pour les carrés sib, une telle obstruction était
  visible, de nature parité.

## 10. Parité des orbites « moins » : une contrainte que l'étage Q n'a pas (DÉRIVÉ, CALCULÉ)

**Énoncé.** Pour toute orbite U, le nombre d'orbites V avec Q[U,V] = 1 qui sont des orbites « − » (e_V = 1, soit ±(eᵢ − eⱼ)) est
**pair**.

*Preuve.* On somme sur tous les blocs ℓ les parités des contraintes (I) de la ligne U :
- (I)(U, ℓ) : Σ_{V ∋ ℓ, Q=1} (ζ_ℓ(V) ⊕ Z[U,V]) + [D(U) ∋ ℓ] ≡ n(ℓ), où ζ_ℓ(V) = [rep V porte +e_ℓ] et n(ℓ) vaut 1 ou 2 ;
- chaque Z[U,V] apparaît deux fois, une par bloc de V, donc disparaît ;
- Σ_{ℓ ∈ V} ζ_ℓ(V) ≡ e_V ;
- Σ_ℓ n(ℓ) = 2 + 2(m − 2) ≡ 0 et |blocs(D(U))| = 2.

Il reste Σ_{V ∈ N₁(U)} e_V ≡ 0. Le calcul vaut pour tout m. ∎

**Contrôles (`scripts/minus_parity_check.py`).**
- **BvLS (m = 11, graphe réel)** : les 110 lignes vérifient la parité (valeurs 6 et 12).
- **Ce n'est pas une conséquence de l'étage Q.** L'étage Q est invariant par l'échange des deux orbites d'une même paire, puisqu'elles
  ont les mêmes blocs. C'est une symétrie (Z₂)²¹, absente du vrai problème, dont la symétrie est (Z₂)⁷. Échanger U₁₂⁺ et U₁₂⁻ dans
  la table BvLS donne une solution de l'étage Q qui viole la parité sur 36 lignes.

**Portée.**
- Ce sont 42 équations XOR peu coûteuses qui cassent la symétrie parasite 2¹⁴ de l'étage Q. Ce sont des conséquences exactes du
  modèle complet, donc valides dans toute relaxation.
- Candidat de transfert vers les calculs d'étage Q du dépôt principal (décision de l'utilisateur).
- Sur les lignes sœurs, c'est exactement la « signabilité » de χ_p (§6 bis, point 3).

**Lien avec le théorème de rang F₂ du dépôt** : rang_F₂(A₁ + Nb Nbᵀ) = 20 à m = 7. La parité des orbites « − » dit exactement que
e ∈ ker_F₂(A₁ + Sh). En effet Sh·e ≡ 0, car chaque bloc est dans 6 orbites « − ». Un changement de signe sur un bloc ℓ remplace e par
e + Nb_ℓ, et les colonnes de Nb sont elles aussi dans le noyau. La classe [e] modulo ⟨Nb⟩ est donc canonique.
- Sur BvLS (`scripts/f2_kernel_bvls.py`) : le noyau est de dimension 66 et contient ⟨Nb, e⟩, de dimension 11.
- À m = 7 : le noyau est de dimension 22 et contient ⟨Nb, e⟩, de dimension 7. Les 15 autres dimensions dépendent de la
  configuration.
- **Correction** (24/09). La première version de ce paragraphe donnait « rang 13, noyau de dimension 29 », en prenant la
  multiplicité de 3 dans S_out (20) au lieu de S_full (27).
  - Le calcul correct : S_full ≡ projecteur 2-entier sur son espace propre de valeur propre 3, donc rang_F₂ S_full = 27.
  - Le complément de Schur par rapport au bloc I₇ donne alors rang(A₁ + Sh) = 27 − 7 = 20.
  - C'est cohérent avec BvLS : 55 − 11 = 44, et le rang calculé y vaut bien 44.

C'est la partie locale et explicite du théorème de rang, ligne par ligne.

## 11. Le modèle complet décide les petits survivants (CALCULÉ, DRAT)

Tous les survivants ont au plus 4 arêtes, donc on relance le **modèle complet** (toutes les lignes, `make_cnf.py`, kissat 600 s,
DRAT si UNSAT ; `scripts/cert_survivors.sh`, `logs/cert_survivors.out`). La sémantique est « au moins ces paires sœurs ».

| Survivant | Modèle complet |
|---|---|
| **C₄ = 23 25 36 56** | **UNSAT**, 495 s, 1,07 M conflits, **DRAT VERIFIED** (surv_C4) |
| **P₄+K₂ = 17 24 56 67** | **UNSAT**, 252 s, 0,34 M conflits, **DRAT VERIFIED** (surv_P4K2) |
| P₅ = 12 23 34 45 | UNKNOWN à 600 s (0,74 M conflits) ; relancé en sémantique exacte |
| 2P₃ = 14 15 36 37 | UNKNOWN à 600 s (0,79 M conflits) ; relancé en sémantique exacte |

Puis viennent les survivants à 3 arêtes, en sémantique **exacte** (Σ = H exactement, les 18 autres paires interdites sœurs) :
K₃, P₄, P₃+K₂, 3K₂ (`scripts/cert_survivors_exact.sh`). Résultats (ajoutés à la revue du 24/09) : **survx_K3 et survx_P4 UNKNOWN à 600 s**
(0,70 M et 0,67 M conflits) ; P₃+K₂ et 3K₂ non lancés.

Leçon (corrigée à la revue du 24/09) : les lignes non sœurs, que les sondes locales ne savaient pas exploiter, ont suffi au solveur global
en quelques minutes **pour C₄ et P₄+K₂** — mais pas pour P₅ ni 2P₃, qui ont aussi 4 arêtes (UNKNOWN à 600 s). Plus Σ est pauvre, plus c'est dur. Le cas Σ ∋ une seule paire, c'est le cas sib du dépôt principal.

## 12. Quelles lignes non sœurs tuent les petits survivants ? L'étoile d'un bloc libre (CALCULÉ, DRAT)

**Noyaux DRAT des réfutations du modèle complet.** On extrait les noyaux avec `scripts/core_run.sh`, c'est-à-dire drat-trim avec
l'option `-c`. On les rattache aux groupes de contraintes par une reconstruction étiquetée, identique au sha256 près
(`scripts/core_groups.py`).
- **P₄+K₂** = 17 24 56 67 (bloc libre : 3) : 41 lignes sur 42 servent. Les paires non sœurs les plus sollicitées dans (P) sont celles
  du **bloc libre 3** : 23:61, 34:59, 13:55, 35:54, 36:45, 37:39.
- **C₄** = 23 25 36 56 (blocs libres : 1, 4, 7) : 25 lignes sur 42 servent, dont **toute l'étoile star(1)** (les 12 orbites
  sur {1,m}), plus 34+, 37−, 47±, 67+.

**Test direct (DRAT).** RSF(lignes sœurs de P₄+K₂ + les 12 lignes de star(3)), Σ exact, donne **UNSAT en 100 s, DRAT VERIFIED**
(`rsfx_P4K2_star3`). Vingt lignes suffisent : les grilles plus l'étoile du bloc libre. Le noyau de cette réfutation
(`scripts/core_groups_rsf.py`) est dense : il utilise les 20 lignes et 346 des 380 équations (P). Il n'y a pas de petit sous-noyau
apparent.

**Programme « étoile libre ».** On teste la même recette sur les 10 survivants (et C₄ en contrôle) : lignes sœurs + star(c) pour
un bloc libre c, Σ exact, kissat 900 s (`scripts/cert_freestar.sh`). Résultats au §13.

**Système linéaire complet des parités de signes, L(Q) (`scripts/sign_parity_system.py`, contrôle BvLS).** À Q fixé, les parités
suivantes sont **linéaires** en les signes Z (un par entrée Q = 1) :
- toutes les contraintes (I) ;
- toutes les équations (P) « cross ».

Sur BvLS (m = 11), L(Q) compte 8415 équations pour 990 signes. On trouve **rang(A) = 990**, et le système est cohérent.
- **Les signes sont déterminés par Q** à travers les seules parités. La cohérence de L(Q) impose donc des conditions linéaires sur le second membre b(Q)
  (7425 = 8415 − 990 est la dimension du noyau à gauche, pas un nombre de restrictions non triviales sur Q) ; b(Q) dépend lui-même de Q.
  « Filtre extrêmement fort » est une HEURISTIQUE : testé sur BvLS seulement (revue du 24/09).
- La parité des orbites « − » n'en est qu'une petite partie. La table échangée (U₁₂⁺ ↔ U₁₂⁻, encore solution de l'étage Q) rend L
  incohérent (rang [A|b] = 991).
- Conséquence pour les solveurs (HEURISTIQUE, BvLS seulement) : l'étage Q + « L(Q) cohérent » équivaudrait presque au modèle complet. Mais les coefficients de L
  dépendent de Q, et CNF + XOR ne peut pas l'exprimer linéairement.

## 13. Programme « étoile libre » et état des calculs lourds (CALCULÉ)

**Étoile libre.** On prend RSF(lignes sœurs de Σ + star(c), c libre), avec Σ exact et kissat 900 s (`scripts/cert_freestar.sh`,
deux voies en parallèle).
- C₄ + star(1) : UNKNOWN à 900 s (4,5 M conflits). Pourtant le modèle complet tue C₄ en 495 s : le noyau de C₄ utilise, en plus de
  star(1), les lignes 34, 37, 47 et 67. Pour kissat, l'étoile libre seule n'est **pas** le bon sous-système pour C₄.
- 2P₃ + star(2) : UNKNOWN à 900 s.
- Tous les autres (P₅, 3K₂, P₃+K₂, P₄, K₃, 2K₂, P₃, K₂, ∅) ont été **interrompus par la surveillance mémoire** : la mémoire libre est
  tombée sous 3 Go entre 17:37 et 17:58, à cause des autres applications de la machine combinées aux deux conteneurs.
- Reprise sur une seule voie (`scripts/cert_freestar2.sh`, `logs/cert_freestar2.out`) :
  - P₅ + star(6) : UNKNOWN à 900 s (4,4 M conflits) ;
  - 3K₂ et ∅ : **non lancés**, la mémoire libre restait sous le seuil de 3,8 Go.
  Les calculs sont suspendus tant que la machine sert à autre chose.

**Sans grille, parité explicite.**
- RS(star(1)) sans sœur, plus les 12 XOR de la parité des orbites « − », sous CryptoMiniSat : TIMEOUT à 900 s.
- La variante RSF(star(1)), plus les 168 XOR de toutes ses contraintes (I), sous CryptoMiniSat : TIMEOUT à 900 s. Même avec les
  parités explicites, une étoile sans grille ne livre aucune contradiction locale en 15 min.

**Bilan de méthode.**
- Pour les petits survivants, le **modèle complet** reste le meilleur format pour kissat : C₄ en 495 s, P₄+K₂ en 252 s.
- Les sous-systèmes « bien choisis » ne sont pas plus faciles, sauf P₄+K₂ + star(3), en 100 s.
- L'étoile du bloc libre est bien la zone que sollicitent les réfutations, mais pas un certificat autonome en général.
- Les survivants restants (P₅, 2P₃, K₃, P₄, P₃+K₂, 3K₂, P₃, 2K₂, K₂, ∅) demandent des calculs de 30 à 60 min chacun, ou un découpage
  en cubes. Mieux vaut les faire sur une machine libre (voir REPRISE §6).
