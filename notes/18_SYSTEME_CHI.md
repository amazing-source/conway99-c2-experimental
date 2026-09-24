# 18 — Le système χ des paires sœurs : la preuve d'allsib généralisée à l'étage Q (24/09/2026)

Suite de la note 17, avec l'hypothèse de travail « C2 n'existe pas ». La preuve d'allsib n'utilise que des équations au niveau des
orbites. On l'étend à toute configuration Σ de paires sœurs.

- Script : `scripts/chi_system.py`.
- Contrôles : `scripts/chi_crosscheck.py` (modèle de l'étage Q du dépôt, encodage indépendant) et `scripts/chi_classify.py`
  (classification exhaustive).
- Journaux : `logs/chi_system.txt`, `logs/chi_crosscheck.txt`, `logs/chi_classify.txt`.

## 1. Cadre : l'étage Q (ÉTABLI dans le dépôt, validé)

- Orbites : les 42 t-orbites de racines. Pour une paire r = {i<j} :
  - U_r⁺ = {eᵢ+eⱼ, −eᵢ−eⱼ} (produit des signes +1) ;
  - U_r⁻ = {eᵢ−eⱼ, −eᵢ+eⱼ}.
- Q[U,V] ∈ {0, 1, 2} est le nombre de voisins, dans l'orbite V, d'une racine u ∈ U. Il ne dépend pas du choix de u (symétrie t),
  et Q est symétrique.

Faits exacts (conséquences du modèle complet ; `vendor/stage_q.py`, validé sur m = 2, m = 3 et BvLS planté) :
- **(Q1)** Σ_V Q[U,V] = 12.
- **(Q2)** Un seul V vérifie Q[U,V] = 2 : c'est D(U), le partenaire D.
- **(Q3)** Sommes par bloc : Σ_{V ∋ ℓ} Q[U,V] vaut 2 si ℓ ∈ blocs(U), et 4 sinon.
- **(Q4)** Gram : pour U ≠ V, Σ_{W ≠ U,V} Q[U,W]·Q[V,W] + Q[U,V] = 4 − Sh[U,V], où Sh[U,V] = |u ∩ v| + |u ∩ tv| compte les
  étiquettes partagées.

Une paire p est **sœur** (elle porte une grille par x) si et seulement si D(U_p⁺) = U_p⁻, c'est-à-dire Q[U_p⁺, U_p⁻] = 2. C'est
exactement ce qu'imposent les CNF certifiées (a = b = 1).

## 2. S1 au niveau des orbites (DÉRIVÉ)

Soit p = {i,j} sœur, ε = ±, et U = U_p^ε. Notons O_p les 20 orbites des 10 paires disjointes de p.

- **(a)** Q[U,V] = 0 pour toute V ≠ D(U) qui rencontre un bloc de p.
  *Preuve :* (Q3) avec ℓ ∈ p donne une somme 2, déjà atteinte par D(U) = U_p^{−ε}.
- **(b)** Les 10 autres orbites voisines de U sont dans O_p, avec Q = 1.
  *Preuve :* (Q1), (Q2) et (a).
- **(c)** Aucune orbite n'est voisine à la fois de U_p⁺ et de U_p⁻.
  *Preuve :* (Q4) pour (U_p⁺, U_p⁻) : Sh = 2 et Q = 2, donc la somme vaut 0.
- **(d)** Donc O_p = N(U_p⁺) ⊔ N(U_p⁻), avec 10 orbites de chaque côté. On définit **χ_p(W) ∈ Z₂** comme l'indice ε tel que
  Q[U_p^ε, W] = 1. On a alors Q[U_p^ε, W] = [χ_p(W) = ε].

## 3. Les contraintes du système χ (DÉRIVÉ, chacune à partir de §1–2)

**(fibre)** #{W ∈ O_p : χ_p(W) = ε} = 10. *Source : (b).*

**(bloc)** Pour ℓ ∉ p, les 8 orbites de O_p qui rencontrent ℓ se répartissent 4/4 selon χ_p.
*Source :* (Q3) pour U_p^ε. Les orbites rencontrant ℓ avec Q ≥ 1 sont dans O_p, puisque D(U) ne rencontre pas ℓ.

**(bij)** Si p et q sont sœurs et disjointes, χ_p(U_q⁺) ≠ χ_p(U_q⁻).
*Source :* sinon, une même orbite U_p^ε serait voisine des deux orbites de q, ce que (c) interdit pour q.

On pose c(p,q) := χ_p(U_q⁺), de sorte que χ_p(U_q^δ) = c + δ. La symétrie de Q donne c(p,q) = c(q,p).

**(disj)** Pour p et q sœurs disjointes, et pour les 6 orbites W qui évitent p ∪ q :
- χ_q(W) = χ_p(W) + c(p,q) ;
- les valeurs χ_p(W) se répartissent 3/3.

*Source :* (Q4) pour (U_p^ε, U_q^{ε′}), avec Sh = 0. Les seuls W qui contribuent sont :
- D(U), pour 2·[χ_q(U_p^{−ε}) = ε′] ;
- D(V), pour 2·[χ_p(U_q^{−ε′}) = ε] ;
- les W ∈ O_p ∩ O_q, pour [χ_p(W) = ε]·[χ_q(W) = ε′].

On distingue deux cas :
- si ε′ = ε + c, alors Q[U,V] = 1, les deux premiers termes sont nuls, et 3 orbites W tombent dans la classe (ε, ε′) ;
- si ε′ = ε + c + 1, alors Q[U,V] = 0, les deux premiers termes valent 2 chacun, et 0 orbite tombe dans la classe.

**(int)** Pour p = {i,j} et p′ = {i,k} sœurs, sur les 12 orbites qui évitent {i,j,k} : #{W : (χ_p, χ_p′)(W) = (ε, ε′)} = 3 pour
chacun des quatre couples.
*Source :* (Q4) avec Sh = 1 (un seul des deux représentants de V partage le signe de u sur i) et Q[U,V] = 0 par (a). Les termes
D(U) et D(V) sont nuls par (a), puisqu'ils rencontrent le bloc commun i.

**Sémantique.** Les paires non listées sont libres, sans aucune contrainte : le système χ est une **relaxation**. Donc :

> χ-UNSAT ⇒ étage-Q-UNSAT ⇒ la configuration est impossible.

Il est monotone : ajouter des paires sœurs ajoute des contraintes.

La preuve d'allsib (note 17) en est un cas particulier : (disj) donne le cocycle, (int) l'équirépartition 3/3/3/3.

## 4. Résultats sur les configurations certifiées (CALCULÉ, `logs/chi_system.txt`)

| Configurations | Système χ |
|---|---|
| allsib, K3K2K2, K13P3, K3K3, C6, K2K3pend, K114, S7a, S7b, S8, g06_a2deb2c4b2, g07_0b2e5dbb0c, g07_bf58f1eae5, **g07_ca15a23af4**, g08_7921acddcb, g08_6c28347c3c | **UNSAT**, en moins d'une seconde chacune |
| K2K2P3, K2P5, K2spider, P4P3, K4, S6, S7c, g06_03276f8462, g06_0fa0ea004a, g06_177a07b777 | SAT : le système χ ne suffit pas, il faut plus que les paires sœurs |

**Nouveau :**
- g07_ca15a23af4 = {12,13,14,15,16,17,47} est K₁,₆ plus une arête. C'était le seul cas **UNKNOWN** de la boucle certifiée (modèle
  complet, 900 s). Il est χ-UNSAT.
- S7a et S8 n'étaient qu'« UNSAT au solveur, sans DRAT ». Ils sont χ-UNSAT.

## 5. Contrôles (CALCULÉ)

Contrôle indépendant par le modèle de l'étage Q du dépôt (un autre encodage), configuration imposée (`logs/chi_crosscheck.txt`) :

| Configuration | Étage Q |
|---|---|
| allsib | UNSAT en 3 s |
| K3K3 | UNSAT en 7 s |
| **g07_ca15a23af4** | **UNSAT en 30 s** (le modèle complet restait UNKNOWN après 900 s) |
| K2K2P3 (témoin χ-SAT) | TIMEOUT à 240 s |
| atomes 01, 02, 03 (§6) | UNSAT en 28 s, 46 s et 25 s |

**Certificat.** g07_ca15a23af4 est UNSAT à l'étage Q :
- kissat conclut en 38 s ;
- drat-trim vérifie la preuve DRAT (543 Mo) en 41 s : VERIFIED ;
- sha256 de la CNF : ce5c286b… ; sha256 de la preuve : a9dad3d0… ;
- voir `data/cert_results.txt`, ligne `stageQ_g07_ca15a23af4`, et `data/cnf/MANIFEST_stageQ.txt`.

Le dernier cas indécis de la boucle Σ est ainsi fermé par un certificat.

## 6. Classification exhaustive et atomes (CALCULÉ, `logs/chi_classify.txt`)

Les 1044 graphes Σ sur 7 sommets (à isomorphisme près) se répartissent ainsi :
- **988 sont χ-UNSAT et 56 χ-SAT.**
- Tous les graphes à 8 arêtes ou plus sont χ-UNSAT. Le système χ retrouve seul la borne « au plus 7 grilles par x ».
- Graphes χ-SAT par nombre d'arêtes : 1, 1, 2, 5, 9, 15, 18, 5 (pour 0 à 7 arêtes).

**Atomes** (les 11 graphes χ-UNSAT minimaux ; tout χ-UNSAT en contient un, par monotonie et invariance par S₇) :

| # | Arêtes | Graphe |
|---|---|---|
| 01 | 13 15 35 67 | K₃ + K₂ |
| 02 | 12 23 24 25 67 | K₁,₄ + K₂ |
| 03 | 14 15 23 36 37 | P₃ + K₁,₃ |
| 04 | 13 16 23 26 35 56 | K₂,₃ |
| 05 | 12 16 23 34 45 56 | C₆ |
| 06 | 12 15 23 34 45 67 | C₅ + K₂ |
| 07–11 | 7 arêtes | 12 14 15 17 23 25 56 / 14 15 23 24 25 47 56 / 14 15 23 24 25 27 36 / 12 23 26 34 37 45 67 / 12 15 23 34 36 56 67 |

**Certificats.** Les CNF χ des 11 atomes (`data/cnf/chi_atom01…11.cnf`, empreintes dans `data/cnf/MANIFEST_chi.txt`) sont **UNSAT avec
DRAT VERIFIED** (kissat + drat-trim, `data/cert_results.txt`).

**Chaîne de preuve complète** pour « Σ ⊇ un atome est impossible » :
1. modèle complet ⇒ étage Q (dépôt, validé) ;
2. étage Q ⇒ système χ (§1–3, dérivation écrite) ;
3. système χ de l'atome UNSAT (DRAT vérifié).

Contrôle indépendant : l'étage Q, avec l'atome imposé, est UNSAT pour les atomes 01, 02 et 03 (§5).

**Noyaux minimaux** (`scripts/chi_mus.py`, `logs/chi_mus.txt`). Ils comptent de 11 à 26 instances de contraintes, qui sont presque
toujours des familles bij, disjX et int, parfois bloc et disjC.

## 7. Lemme du triangle et preuve humaine de K₃ + K₂ (DÉRIVÉ, vérifié)

**Lemme T.** Soit un triangle de paires sœurs {ab, ac, bc}, et soit C = [7] ∖ {a,b,c}, avec |C| = 4. Sur les 12 orbites des 6 paires
contenues dans C, posons v(W) = (χ_ab, χ_ac, χ_bc)(W) ∈ Z₂³. Alors chaque classe antipodale {c⃗, c⃗ + 111} de Z₂³ contient exactement
3 des 12 vecteurs.

*Preuve.*
- Par (int), pour chaque couple de coordonnées, les 4 valeurs apparaissent 3 fois chacune. Donc, pour un c⃗ fixé, exactement 6 orbites
  vérifient d_a = d_b, avec d = v + c⃗.
- Une orbite dont d est constant (000 ou 111) est « diagonale » pour les 3 couples. Sinon, elle l'est pour exactement 1 couple.
- Si k est le nombre d'orbites de la classe de c⃗, on obtient 3k + (12 − k) = 3 × 6, donc k = 3. ∎

**Corollaire (atome 01).** Aucune paire sœur q ⊂ C ne peut coexister avec le triangle.

*Preuve.* Soit q ⊂ C une paire sœur, et c⃗ = (c(ab,q), c(ac,q), c(bc,q)).
- Par (bij), v(U_q^δ) = c⃗ + δ·111 : les deux orbites de q sont dans la classe de c⃗.
- Par (disjX), sur les deux orbites de la paire C ∖ q, qui évitent chaque paire du triangle et q, on a χ_p = χ_q + c(p,q) pour les trois
  p. Donc v ∈ {c⃗, c⃗ + 111} : ces deux orbites sont aussi dans la classe de c⃗.
- On obtient 4 orbites dans une classe qui n'en contient que 3. ∎

**Vérification machine.**
- Le noyau exact de cette preuve (bij, disjX et int : 9 instances) est UNSAT.
- Le triangle seul est SAT, et le noyau privé de bij est SAT : chaque ingrédient est nécessaire.

## 8. Bilan pour Σ (CALCULÉ, `logs/sigma_survivors_v2.txt`)

- Avec les **21 configurations certifiées par DRAT** (20 dans le modèle complet, plus g07_ca15a23af4 à l'étage Q) : **52 graphes Σ
  survivent**, au plus 7 arêtes, 12 maximaux.
- Parmi ces 52, **13 sont χ-UNSAT**, dont le plus petit est {13, 15, 35, 67} = K₃ + K₂. Il reste **39 graphes Σ possibles** (χ-SAT et
  évitant les configurations certifiées).
- Dans ces 39 : le graphe vide (aucune grille par x) et tous les petits graphes.

## 9. Suite

- **Preuves humaines des atomes 02 à 11.** Les noyaux minimaux en donnent le squelette. Le lemme T traite les triangles ; il faut des
  lemmes analogues pour les étoiles et les cycles.
- **Les 39 survivants.** Le système χ ne suffit plus : il faut des contraintes qui touchent les orbites non sœurs.
- **Le cœur sans grille.** Il faut généraliser χ aux paires D de types one et dis. À l'étage Q, pour une paire D {U, D(U)},
  (Q4) donne Σ_W Q[U,W]·Q[D(U),W] = 2 − Sh :
  - 0 pour sib (partition exacte, c'est S1) ;
  - **1 pour one** (un seul chevauchement) ;
  - **2 pour dis** (deux chevauchements).

  Les voisinages restent presque des partitions : ce sont les « défauts » de la note 07. C'est le point de départ du système χ à
  défauts.
