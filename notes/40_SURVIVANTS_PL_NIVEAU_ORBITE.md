# 40 — Le PL par paires laisse des survivants ; le niveau orbite les tue (26/09/2026, après-midi)

Session principale C2. Demande de l'utilisateur : accélérer le calcul ou le remplacer par des mathématiques, sans arrêter les
processus en cours. Les pipelines de la note 36 tournent toujours ; rien n'a été arrêté.

## 1. Contrôle des feuilles sans PL (`scripts/leafA_check.py`) : NÉGATIF
Pour une feuille (partie hors A) papillon, on énumère les 130 structures de A et on applique le filtre sain complet (19.1,
profils 27.1, règle typée).
- Mesure sur 18 feuilles : **aucune feuille tuée** ; 18 à 77 structures de A passent (6 à 20 s par feuille).
- Ce n'est pas un remplacement du branchement PL. Non intégré.

## 2. Le PL par paires laisse de vrais survivants
Les journaux du pipeline (`logs/mix6_ulp_*.jsonl`) contiennent des feuilles marquées **feasible (A fixed)** : feuille et structure
de A entièrement fixées, et le PL par paires (P2) reste faisable. `scripts/survivor_replay.py` rejoue la récursion depuis le
journal, sans PL, pour retrouver la structure de A de chaque survivant (`logs/lp_survivors.json`). Au 26/09 vers 12 h :
- M1 n = 6 (T = hexagone 0-1-2-3-4-5, A = 6) :
  - job 0, In = {0:[4], 1:[5], 2:[0], 3:[0,1], 4:[1,2], 5:[2,3]} : 2 survivants ;
  - job 2, In = {0:[4], 1:[4,5], 2:[0], 3:[0,1], 4:[2], 5:[2,3]} : 8 survivants.
- Mélange classe 1 (2C₃ : triangles tordus {0,1,5} et {2,3,4}), In = {0:[2,4], 1:[2,3], 2:[5], 3:[0], 4:[1], 5:[3,4]} :
  4 survivants.
- Tous sont du **cœur** au sens de la note 27 §4 : aucun cycle D fermé hors de A, G_c connexe en tout bloc, équilibre vide.

**Conséquence.** Le calcul par paires, même poussé jusqu'au bout, ne ferme pas M1 n = 6 ni les mélanges. Il faut un niveau
plus fin.

## 3. Modèle au niveau des orbites (`scripts/orbit_colmodel.py`), écrit indépendamment de « structures »
Squelette fixé. L'orbite Z = (i,j,k) a pour pivot i, bloc libre j et tiers k ; D(Z) est l'orbite (i,k,j), et les digones sont
appariées dans l'ordre, sans perte de généralité.

**Colonne de Z** : un vecteur q ∈ {0,1,2}⁴², où q[W] est le nombre de voisins d'une étiquette de Z dans W.
- q[D(Z)] = 2 ; q = 0 sur toutes les autres orbites des paires {i,r}, sœur comprise (F1).
- **Partie libre** : deux orbites distinctes F₁, F₂ libres en j, hors sœur, pas toutes deux dans {j,k} (règle typée).
  - Une orbite de pivot j est exclue : par F1 appliqué à elle, Z serait son partenaire D.
  - F₁ = F₂ est exclu : sinon un second 2 sur la ligne de Z.
- **Partie lointaine** : v sur les 10 paires des 5 blocs t ≠ i,j, de sommes 4 − 2[t = k] − n_t.
  - v = 2 donne (1,1) : une paire lointaine ne contient jamais D(Z).
  - v = 1 donne l'une des deux orbites.

**Lignes.**
- one[Z] ; S[W] : Σ_Z q_Z(W) = 12 ; C[a,b] : q_a(b) = q_b(a).
- **I[a,b]**, pour les 903 couples a ≤ b, doublées : 2Σ_Z q_Z(a)q_Z(b) + q_a(b) + q_b(a) = 2(12[a = b] + 4 − Sh(a,b)).
  - Sh vaut 2 pour une même paire, sinon le nombre de blocs communs.
  - C'est Q² + Q = 12I + 4J − Sh, quotient par σ de B² + B = 12I + 2J − CCᵀ. Lecture élémentaire : deux racines u, w ont
    exactement 2 − |u ∩ w| − [u ~ w] voisins-racines communs (λ = 1, μ = 2). La somme est faite sur les deux racines de l'orbite w.
- Coupes de R_c : au plus |S| − 1 arêtes dans S, pour toute taille |S| qui n'est pas une réunion de cycles pairs ≥ 4.

**Méthode.**
- PL de phase 1 par génération de colonnes. Le pricing est exact : toutes les colonnes-orbites sont énumérées, environ 420 000
  par squelette.
- **Contrôle exact en entiers** : y × 10⁶, arrondi, puis le maximum par orbite sur **toutes** les colonnes.
  yᵀb > Σ_Z max_c (Aᵀy)_c + Σ_{≤} max(0, y_r b_r) prouve qu'il n'y a pas de solution.

**Relecture.** « structures » a relu la sémantique des colonnes et des lignes (voisins libres exclus, doubles lointains (1,1),
Sh des sœurs) : juste.

## 4. Résultats
**Survivant 0** (M1 n = 6, job 0) : **infaisable** au niveau orbite. L'écart de phase 1 vaut 77,09, et le certificat exact est VALIDE.
Environ 4 min.

**Contrôles sur le même survivant.**

| lignes (I) | résultat |
|---|---|
| toutes (orbites) | infaisable, écart 77,09, certificat exact |
| comprimées par paires (Σ sur a ∈ R₁, b ∈ R₂) | **faisable**, comme le PL par paires indépendant |
| aucune | faisable |

La contradiction vient donc exactement de l'information d'orbite : **laquelle des deux orbites d'une paire reçoit un voisin**.

## 5. Les 14 survivants sont morts (certificats exacts, revérifiés indépendamment)
| survivant | famille | écart de phase 1 | marge revérifiée |
|---|---|---|---|
| 0–3 | 2C₃, classe 1, job 1 | 77,09 / 73,32 / 77,09 / 77,09 | VALIDE ×4 |
| 4–5 | M1 n = 6, job 0 | 88,35 / 93,23 | VALIDE ×2 |
| 6–13 | M1 n = 6, job 2 | 84,99 à 96,52 | VALIDE ×8 |

- Certificats : `logs/orbit_certs/surv_*.json.gz`, avec les multiplicateurs entiers (y × 10⁶) et les étiquettes de lignes.
- **Revérification indépendante** (`scripts/orbit_verify_certs.py`, aucun PL, aucune fonction commune avec le modèle) :
  - chaque ligne est reconstruite depuis son étiquette, avec son propre second membre ; 0 désaccord ;
  - les colonnes sont réénumérées avec un énumérateur lointain propre et une expansion propre ; mêmes nombres de colonnes ;
  - (Aᵀy)_c est calculé depuis la sémantique des lignes.
  - Résultat : **14/14 VALIDES**.
- **Contrôles négatifs du vérificateur.**
  - Certificat privé de ses lignes I : INVALIDE.
  - Triplets permutés : rejet, car les coupes ne sont plus des ensembles d'orbites libres.
  - Un seul multiplicateur perturbé de 30 % reste valide (marge 69). C'est normal vu la marge de 77.

## 6. Accélération : le niveau orbite avec A variable tue une feuille entière (`scripts/orbit_colmodel_var.py`)
- Les 12 orbites de A sont étiquetées (A, x, s). Une colonne choisit le tiers y et l'orbite partenaire (A, y, s′).
- Les lignes de couplage font des entrées q = 2 un couplage parfait entre paires différentes, c'est-à-dire un graphe D en A valide.
  Au niveau entier, on retrouve exactement les 130 structures de A.
- **M1 n = 6, job 0, feuille 17** (celle des survivants 4 et 5) : **infaisable avec A variable**. Écart 27,92, contrôle exact
  VALIDE, un seul PL de 705 s. Le pipeline par paires y avait passé environ 20 PL et laissé 2 survivants.


## 7. Orientation fixée, toutes les structures D libres (`scripts/orbit_colmodel_gen.py`)
- Chaque orbite est une étiquette (paire, s). Le pivot est donné par l'orientation : pour une paire tordue {a,b}, l'orbite 0 a le
  pivot a et l'orbite 1 le pivot b, sans perte de généralité.
- Une colonne choisit le tiers, l'orbite partenaire (de même pivot), les voisins libres et la ligne lointaine.
- Les lignes C, avec pivots fixés, donnent la symétrie exacte de D, même en fractionnaire. Les voisins libres sont restreints aux
  orbites libres en j.
- Vérificateur indépendant généralisé : modèles fixed / var / gen / all, restrictions « allowed » et « forbid ».

**Résultats, M1 n = 6** (16 orientations avec feuilles au filtre v6).

| orientation | niveau paires (ancien pipeline) | niveau orbite, D libre |
|---|---|---|
| 0 | 2 survivants, tués au §5 | **infaisable**, écart 5,03, certificat revérifié |
| 1, 3, 4, 5, 8 | morts | — |
| 2 | 8 survivants, tués au §5 | — |
| 6 | 11 survivants, **tués** (niveau orbite, squelette fixé) | — |
| 9, 10, 13, 14 | pas atteints | **infaisables** (écarts 12,84 / 8,98 / 14,36 / 7,60) |
| 7, 11, 12, 15 | pas atteints | faisables |

- **Encore faisables à la racine** : classe 2 job 6 (870 feuilles), papillon job 10 (450), M1 n = 5 job 10 (228), classe 1 jobs 0 et
  4, M1 n = 6 jobs 7, 11, 12 et 15.

**Essais de découpage (NÉGATIFS pour l'efficacité).**
- Branchement sur le partenaire d'une orbite : 10 branches uniformes (1/7 chacune) dès la racine. Arrêté.
- Union par feuilles : 48 feuilles faisables, puis 16 feuilles faisables (912 s par nœud). Arrêté.
- Lignes 11.5 (paires sœurs, au plus un double proche) : job 12 reste faisable.
- Modèle « tout libre » et « T fixé, orientation libre », même avec les lignes de degré libre : FAISABLES.

## 8. Niveau racine (signé) : `scripts/root_colmodel.py`
- Une colonne de Z est **le voisinage-racine complet** r ∈ {0,1}⁸⁴ de son représentant. Conventions de
  `vendor/involution_frame.py` : racine (a,s)(b,t), orbite ε = st, représentant (a,+)(b,ε).
- **Lignes** :
  - symétrie ;
  - l'identité complète B² + B = 12I + 2J − CCᵀ sur les 84 racines, les deux facteurs étant lus dans la colonne de X. Elle contient à
    la fois l'identité invariante (Q² + Q = 12I + 4J − Sh) et l'anti-invariante (S² + S = 12I − CCᵀ, celle du Théorème D) ;
  - les coupes.
- **Colonnes** :
  - voisins m et π **ordonnés**, dont les racines sont déterminées par le signe de z en j ;
  - les deux racines du partenaire D ;
  - 8 racines lointaines, au plus une par orbite, **équilibrées 2/2 en signe à chaque bloc lointain** (μ = 2 avec (c,±)).
- **Holonomie.** Pour les paires tordues, seule la classe modulo les retournements de blocs compte. L'hexagone en a 2.
- **Taille** : environ 11 M colonnes implicites (6 200 configurations proches × ensembles lointains en cache). Pricing en 3 s.
- **Contrôle prévu** (EVEN=1) : les seules lignes invariantes, sommes des lignes ± ; elles doivent redonner la faisabilité du
  niveau orbite.

## 9. Verdicts négatifs de l'après-midi (tests minuscules, sauf le §9.3)
1. **Système A-local signé** (`scripts/A_local_signed.py`).
   - Les 30 orbites hors de A ne portent que leurs vues signées des 12 orbites de A.
   - Lignes : Gram signée G = 11I − J + S (partie anti-invariante), Gram non signée H (1 / 2 / 3), 2 voisins libres par orbite de A,
     lignes 11.5, et équilibre 24.0 sur les cycles de D_A.
   - Résultat : **FAISABLE pour les 4 types** de D_A. Il n'y a pas de lemme « pas de bloc A » purement local, même signé.
2. **𝒫 = 6I − 2Q − Sh + J ⪰ 0** (Astra, via « structures ») est **impliqué** par le PL d'orbite. En effet, M₂ − Q̄² = Σ Cov ⪰ 0,
   Q̄ préserve span(Nb), donc Q̄² + Q̄ ⪯ R. Il reste utile seulement comme filtre exact sur des squelettes.
3. **Niveau racine (signé), orientation M1 n = 6 job 12** : **FAISABLE dans les deux classes d'holonomie**.
   - Convergence en 39 itérations, environ 65 min chacune ; le maître IPM monte à 250 s par itération (4 429 lignes).
   - L'information signée ne suffit donc pas, au niveau de l'orientation, pour ce job. Il faut fixer (au moins en partie) les
     structures D.
   - Relecture complète du modèle par « structures » (tests T1–T4, 0 erreur) : c'est un vrai signal, pas un artefact.
   - Solveurs essayés pour le maître : le simplexe à chaud et PDLP sont plus lents que l'IPM.

**Bilan honnête.**
- Au niveau de l'orientation, le PL d'orbite tue environ la moitié des orientations de M1 n = 6. Le reste demande de découper
  jusqu'aux feuilles, et plusieurs classes de mélanges en ont de 10⁴ à 10⁵ par classe (filtre v6 : classes 9, 13, 14…).
- Le calcul seul n'est pas une voie efficace pour les mélanges. Il faut un levier mathématique (lemmes structurels sur T,
  sur le bloc A, ou un autre découpage), le calcul restant un outil de test ciblé.
