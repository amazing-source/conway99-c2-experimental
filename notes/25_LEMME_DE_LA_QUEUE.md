# 25 — Lemme de la queue : l'équilibre (note 23 §8) tue toutes les configurations ancrées du carnet principal (25/09/2026)

Session principale C2, régime sans solveur.

**Statut : DÉRIVÉ, VÉRIFIÉ par la session « structures »** (relecture adverse du 25/09, étape par étape, avec un contrôle
numérique de l'identité d'équilibre générale sur BvLS). Une relecture interne indépendante est en cours.
- Aucun calcul n'est utilisé.
- Aucun contrôle positif possible : l'équilibre est propre à k = 14, et BvLS n'a que des carrés sœurs.

**Origine.** Croisement de deux résultats que ni le labo ni le carnet principal n'avaient rapprochés :
- le **lemme d'équilibre** du labo (note 23 §8, preuve humaine) ;
- les **configurations ancrées** du carnet principal (`MATH_C2_PROGRAMME.md` §18–§22). Les cas (6,3,3,3,2,2,2) et (6,0,3⁵) y
  étaient ouverts.

## 0. Cadre et notations
Carte en x₀ (le point fixe de t) :
- sommets intérieurs ±e_m ;
- racines ±e_i ± e_j ;
- t = −1.

Pour un bloc k, on note :
- ℓ_k = {x₀, e_k, −e_k} ;
- X_k = {±e_m : m ≠ k}, 12 étiquettes ;
- les 36 sommets de N(ℓ_k) : les intérieurs b ∈ X_k, puis les racines e_k + b et −e_k + b ;
- μ_k et τ_k : les couplages de la formulation compacte (note 20 §3). On a e_k + b ∼ e_k + μ_k(b) et e_k + b ∼ −e_k − τ_k(b).

Le graphe induit sur N(ℓ_k) est 3-régulier. Ses arêtes sont :
- b – (−b) : la droite par x₀ ;
- b – (e_k + b) et b – (−e_k + b) ;
- (e_k + b) – (e_k + μb), (e_k + b) – (−e_k − τb) et (−e_k + b) – (−e_k − μ(−b)).

Les trois sommets d'une même étiquette b sont dans la même composante, car l'intérieur b est adjacent aux deux racines
d'étiquette b. Les composantes correspondent donc aux parties S ⊂ X_k stables par μ_k, στ_k et σμ_kσ (σ = −1), avec
|C_S| = 3|S|.

**Lemme d'équilibre (note 23 §8, revérifié ici ligne à ligne).** Soit C une réunion de composantes. Toute racine lointaine z (qui
évite le bloc k ; il y en a 60) a exactement |C|/6 voisins dans C.
*Preuve (rappel).* On note B l'incidence entre N(ℓ) et les lointains.
- BBᵀ = (12I − A_NN + 2J) − Cls − A_NN², où Cls est l'indicatrice de « même voisin sur ℓ ».
- Pour u ∈ C : (BBᵀ1_C)_u = 12 − 3 + 2|C| − |C|/3 − 9 = 5|C|/3, car C coupe chaque classe en tiers (couplages croisés parfaits).
- Donc Σ_z n_C(z)² = 5|C|²/3 et Σ_z n_C(z) = 10|C|, sur 60 lointains : la variance est nulle. ∎
- Autre lecture : 1_C − (|C|/36)1_N est un vecteur propre de A_NN de valeur propre 3, orthogonal à 1_N (note 23 §9).

## 1. Lemme de la queue (forme générale)
**Lemme 25.1.** Soit X une orbite de la paire {i, j}, appariée par le bloc i (carré D de type « un bloc ») à une orbite D(X) de la
paire {i, k} ; k est le troisième bloc. Soit S ⊂ X_k la réunion des composantes, en k, qui contiennent les étiquettes ±e_i. Alors

  |S|/2 ≥ 3 + [x a son signe du bloc j dans S],

c'est-à-dire que S contient au moins 6 étiquettes (au moins 8 dans le second cas).

*Preuve.* On fixe x ∈ X. x évite k : c'est un lointain de ℓ_k. Par équilibre, x a exactement |S|/2 voisins dans C_S. Parmi eux :
- **l'intérieur s_i e_i**, qui est le signe de x au bloc i. Il est dans S, puisque ±e_i ∈ S ;
- **les deux sommets v, σv du carré D de x**, où D(X) = {v, σv} ⊂ paire {i, k}. On a v ∈ N(x) ∩ N(σx). Vus depuis ℓ_k, v est
  une racine d'étiquette ±e_i (classe ±e_k), et σv une racine d'étiquette ∓e_i. Tous deux sont dans C_S ;
- l'intérieur s_j e_j, s'il est dans S. ∎

## 2. Configurations ancrées (carnet principal §18) : la queue est de degré entrant ≤ 2
Dans une configuration ancrée :
- Σ = ∅, et chaque paire a ses deux orbites appariées « un bloc » par un même bloc, son ancre ;
- orientation : j → k si la paire jk est ancrée en k. d_k est le degré entrant, In(k) et Out(k) les voisinages entrant et
  sortant.

**Invariance.** On pose X_In(k) = {±e_m : m ∈ In(k)}. Pour b ∈ X_In(k), la paire {k, m} est ancrée en k, donc l'orbite de e_k + b est
appariée par k : μ_k(b) = τ_k(b) = b′. L'orbite partenaire, dans {k, m′}, est elle aussi appariée par k, donc m′ ∈ In(k). Ainsi
X_In(k) est stable par σ, μ_k, τ_k, et son complémentaire X_Out(k) aussi. X_Out(k) est une réunion de composantes, de taille
2(6 − d_k).

**Corollaire 25.2 (lemme de la queue).** Soit un carré de pivot i, de bras j et k (orbites X ⊂ ij et D(X) ⊂ ik ; les deux paires
sont ancrées en i, donc j → i et k → i). Alors **la queue de l'arc entre j et k a un degré entrant ≤ 2, et la tête ≤ 3.**

*Preuve.* On applique 25.1 à X, de troisième bloc k, avec S ⊂ X_Out(k). S contient bien ±e_i, puisque k → i, c'est-à-dire
i ∈ Out(k). Donc 6 − d_k = |X_Out(k)|/2 ≥ |S|/2. Plus précisément, par équilibre sur la réunion X_Out(k), x a exactement 6 − d_k
voisins dans C_Out(k), dont :
- l'intérieur s_i e_i ;
- v et σv ;
- l'intérieur s_j e_j si j ∈ Out(k).

Donc d_k ≤ 3 − [k → j]. Symétriquement, pour D(X), de troisième bloc j : d_j ≤ 3 − [j → k]. ∎

*Cohérence.* Pour une structure liée (h; s, w) avec s → w, 25.2 donne d_s ≤ 2, soit out(s) ≥ 4. C'est exactement la règle que
le carnet principal avait obtenue autrement (§20, par 19.1 et l'exclusion de K₂,₂). 25.2 l'étend aux triangles D et aux étoiles de
tout degré.

## 3. Conséquence : il n'existe aucune configuration ancrée
Par le corollaire 19.2 du carnet principal, les degrés entrants sont dans {0, 2, 3, 6}, et la suite des degrés est 3⁷,
(6,3,3,3,2,2,2) ou (6,0,3⁵).
- Un bloc de degré 6 n'est jamais un bras (il n'a pas d'arc sortant).
- En un bloc i de degré 3, le graphe D est un triangle sur In(i) = {j, k, m} : les trois paires de bras sont des carrés.
  - Tout arc entre deux éléments de In(i) a donc une queue de degré ≤ 2.
  - Un tournoi à 3 sommets a au moins deux queues distinctes.
  - **Au moins deux éléments de In(i) ont un degré entrant dans {0, 2}.**

**(a) 3⁷ (Théorème P).** Aucun bloc n'a de degré ≤ 2 : impossible. C'est une preuve en deux lignes du Théorème P.

**(b) (6, 0, 3⁵).**
- Z (degré 0) pointe vers tout le monde, et tout le monde pointe vers A (degré 6).
- Chaque bloc B, de degré 3, a In(B) = {Z, B₁, B₂}, où B₁ et B₂ sont deux blocs de degré 3.
- L'arc entre B₁ et B₂ a une queue de degré 3 : impossible.

**(c) (6, 3, 3, 3, 2, 2, 2)**, sans utiliser l'unicité du tournoi établie au §22 du carnet.
- Blocs : A (degré 6), C₁, C₂, C₃ (degré 3), L₁, L₂, L₃ (degré 2).
- *Au plus un C dans chaque In(C_j).* Un arc entre deux C de In(C_j) aurait une queue C, de degré 3.
- *Le sous-tournoi des C est cyclique.* S'il était transitif, un C recevrait deux C.
- *Structure des In(C_j).* Posons C_{j−1} → C_j. Alors In(C_j) = {C_{j−1}, L, L′}, et C_{j−1} doit être la tête de ses arcs vers
  L et L′ : L → C_{j−1} et L′ → C_{j−1}.
- *Les trois C partagent les mêmes deux L.* In(C_{j−1}) = {C_{j−2}} ∪ {L, L′}. En faisant tourner, les trois C ont la même paire
  {L, L′} dans leur In.
- *Contradiction.* Le troisième L ne pointe vers aucun C : les trois C pointent vers lui, et son degré est ≥ 3, alors que
  d_L = 2.
- Pour contrôle, le tournoi unique du §22 contient l'arc C_{j−1} → L_{j−1} dans In(C_j), avec une queue C : contradiction
  directe.

**Théorème 25.3.** Aucune configuration ancrée n'existe (Σ = ∅). Les deux cas qui restaient ouverts au §22 du carnet principal
sont fermés.

## 4. Ce qui reste, et la suite
- Hors configurations ancrées, en Σ = ∅, restent :
  - les **fourches** : une paire dont les deux orbites sont appariées par des blocs différents ;
  - les **chaînes tordues** ;
  - les **carrés disjoints** (type dis).
- 25.1 s'applique tel quel à toute orbite appariée « un bloc » : la composante de ±e_i au troisième bloc doit être grande (≥ 6
  étiquettes). Cela contraint les composantes de ⟨μ_k, στ_k, σμ_kσ⟩, donc les fourches.
- Pour les carrés dis, il faut un analogue. Le carré n'a pas de troisième bloc, mais ses 4 sommets rencontrent 4 blocs.

## 5. Précisions demandées par la relecture de « structures »
- **Stabilité de X_In(k).** Deux faits sont utilisés.
  - Une orbite de {k, m} appariée par k est une **digone de R_k**, car les digones sont exactement les paires D via k (carnet
    principal, Lemme 3). Sur elle, μ_k = τ_k (m_k = π_k).
  - Par définition de l'ancrage, la paire partenaire kr est appariée par k, donc ancrée en k, donc r ∈ In(k).
  Les quatre types d'arêtes de G(ℓ_k) (mate intérieur σ, intérieur–racine, μ_k dans R₊, σμ_kσ dans R₋, et π entre R₊ et R₋)
  restent dans X_In(k).
- **Comptage de contrôle.** x a exactement 6 voisins dans N(ℓ_k) : ses 2 éléments intérieurs, et 2 racines de chaque signe, car
  μ(x, ±e_k) = 2. L'inégalité 3 + [k → j] ≤ 6 − d_k ≤ 6 est donc cohérente. Les voisins énumérés sont distincts : v et σv sont de
  signes opposés en k.
- **Identité générale** (structures ; valable pour tout srg(v,k,1,2)) :
  BBᵀ1_C = (k − 14)1_C + (5/3)|C|1_N, Σn_C = (k − 4)|C| et Σn_C² = (k − 14)|C| + (5/3)|C|².
  - Vérifiée sur BvLS : 891 droites, 8910 composantes. Contrôle négatif : l'identité casse sur des 12-ensembles qui ne sont pas
    des réunions de composantes.
  - À k = 14 seulement, la variance est nulle.
- **Portée.** Toutes les configurations ancrées. Pas les chaînes tordues de longueur ≥ 4, ni les mélanges, ni les carrés
  disjoints.
