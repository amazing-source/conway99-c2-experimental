# 45 — Famille « tout un bloc » (Σ = ∅) : réduction à 79 systèmes locaux (27/09/2026, nuit)

Travail commun : C2 pour le comptage et l'empaquetage, C1 pour les types et les fichiers, « structures » pour la relecture de la
réduction et la validité de l'encodage.

## 1. Énoncé visé
**Si Σ = ∅ et si tous les carrés sont « un bloc », alors l'involution est impossible**, dès que les 79 systèmes locaux listés
ci-dessous sont UNSAT (avec preuve DRAT vérifiée).
- Cet énoncé couvre M1 (tous les n), tous les mélanges (tout T pair), T = ∅ et T = K₇, **sans aucun PL d'orbite**.
- Resterait ensuite la seule famille « dis » : au moins un carré dis, avec Σ = ∅ ou non.

## 2. Preuve (modulo les 79 instances)
1. **Comptage (C2).**
   - Chaque orbite U a un pivot. En type « un bloc », D(U) est dans une paire {i,k} qui partage le bloc i avec la paire {i,j}
     de U.
   - Les 42 orbites donnent donc exactement 42 étiquettes de pivot, réparties sur 7 blocs : la moyenne est 6.
   - **Un bloc c porte au moins 6 étiquettes.**
2. **Profil du bloc.**
   - Pour chaque autre bloc x, la paire {c,x} donne 2 étiquettes en c si elle est ancrée en c, 1 si elle est tordue, 0 si
     elle est ancrée en x.
   - Profil (a, t) = (|ancrées en c|, |tordues en c|), avec 2a + t ≥ 6 et t pair (T est un sous-graphe pair de K₇, notes 26
     et 35).
   - Profils possibles : (3,0), (2,2), (1,4), (0,6), (4,0), (3,2), (2,4), (5,0), (4,2), (6,0).
3. **10 étiquettes : impossible (C1).**
   - Les 2 étiquettes non pivots devraient être appariées entre elles par τ ET par η, deux involutions sans point fixe.
   - Ce serait alors une arête commune, donc un pivot.
   - Donc (5,0) et (4,2) sont exclus.
4. **Classes pertinentes (C1).**
   - Pivots en c ⟺ arêtes communes de μ et τ.
   - Une paire pivot qui est une arête π ⟺ paire frère en c, exclue puisque Σ = ∅.
   - `classes_t_ge` énumère tous les couples valides à B₆ près ; les profils sont B₆-invariants à permutation près.
5. **Système local (structures).**
   - (i)–(iii) + L1/S1/S2 est nécessaire en tout bloc et B₆-invariant.
   - `sat_local.encode(mu, tau, ())` est valide pour μ, τ généraux (corrections K₂, K₃, L1, S1, S2 re-dérivées).
   - Limite : le contrôle positif BvLS ne teste que des blocs pleins.

## 3. Relectures
- **structures** (27/09) : réduction large-T CORRECTE.
  - (a) Complétude de l'énumération par profil : recompte indépendant (`involution/recount_profile24.py`), 15 classes de
    profil (2,4), dont 9 pertinentes, identique à C1.
  - (b) Validité de l'encodage en bloc non plein.
  - **Complément de structures (commit 67d5f57).**
    - L'échelle de C1 est VÉRIFIÉE : somme 42 + 2|Σ| − 2n_dis, parité par bloc, 10 pivots impossibles.
    - Recompte indépendant des classes par nombre de pivots : 0 → 1787, 2 → 958, 4 → 407, 6 → 106, 8 → 39, 12 → 11.
    - Classes pertinentes à ≥ 6 : **79**, identique à C1.
  - **Recompte au niveau des ensembles (structures, lab bce7fac, `involution/recount_profiles_ge6.py`, formes canoniques sous
    B₆)** : ses 156 classes à ≥ 6 pivots sont exactement all_ge6 de C1, avec le même profil et la même pertinence.
    - Les fichiers tier6_rel (56), tier12_rel (4), tier8_rel (9), tier_32 (6), tier_40 (4) et allonblock_ge6_rel (79) sont
      tous pertinents et distincts. **Recompte des tiers : ✔.**
  - Deux étapes sur les 9 types (2,4) : chaque ι trouvé meurt en étape 2 (6 au PL, 3 en PLNE). La classe 4 a un quasi-design,
    mort au PL.
  - Indice : sur 3 des 9 classes (2,4) pertinentes, les ι trouvés meurent en étape 2 (2 au PL, 1 en PLNE), comme pour les blocs
    pleins et mixtes. UNSAT probable.
- **C2** :
  - Les 79 classes (`allonblock_ge6_rel.json`, C1 040ec06) = tier8_rel 9 + tier6_rel 56 + tier12_rel 4 + tier_32 6 +
    tier_40 4, contrôlé comme multiensembles de (μ, τ).
  - Répartition par profil : (2,2) 24, (1,4) 18, (2,4) 9, (3,0) 7, (0,6) 7, (3,2) 6, (4,0) 4, (6,0) 4.
  - Le comptage des 42 étiquettes est retrouvé sur les données large-T : Σ_c (2a_c + t_c) = 2(21 − |T|) + 2|T| = 42.

## 4. Calcul (c2-compute)
- Tâche `tier FICHIER i secondes [proof]`, pour chaque instance :
  - CNF de `sat_local_batch.py` (C1, lex-leader sous Stab_B₆(μ, τ), préfixe 6), puis CaDiCaL avec plafond de temps ;
  - si SAT : `decode_model.py` contrôle chaque clause et écrit la solution locale {cfg, Phi} ;
  - avec `proof` : DRAT + drat-trim.
- Première passe SANS preuve, pour trier UNSAT / SAT / INCONNU. La preuve DRAT est rejouée ensuite pour les seuls UNSAT : une
  preuve de 4 h est trop grosse pour le disque.
- Fichiers de tâches :

  | fichier | contenu |
  |---|---|
  | tier8a / tier8b | (2,4), 5 + 4 |
  | tier6 | 56 classes |
  | tier3240 | (3,2) 6 et (4,0) 4 |
  | tier12 | (6,0) 4 ; secours de fb/sat, qui a l'encodage plein avec extras |

## 5. Hors de cette famille
- Les étoiles libres (0 étiquette) ne figurent pas dans cet énoncé. Elles ne deviennent inévitables que dans la famille dis
  (aucun pivot pour une orbite dis).
- La campagne des racines d'orbite (note 44 §8) continue en parallèle. C'est une route indépendante pour les mêmes cas, avec des
  certificats d'orbite déjà revérifiés.

## 6. Échelle de réduction pour tout le problème (C1, à relire par structures)
- **Étiquettes de pivot, cas général.**
  - Une orbite frère est pivot en ses 2 blocs ; une orbite un bloc en 1 bloc ; une orbite dis en aucun.
  - Total : **42 + 2|Σ| − 2n_dis** (2n_dis orbites dis).
  - Par bloc, le compte est **pair** : 2 × #arêtes communes de τ et η.
- **Échelle.** Les UNSAT successifs donnent :
  - les 156 classes à ≥ 6 pivots ⟹ n_dis ≥ |Σ| + 7 ;
  - plus les 407 à 4 pivots ⟹ n_dis ≥ |Σ| + 14 ;
  - plus les 958 à 2 pivots ⟹ il ne reste que « tout dis » (n_dis = 21, toutes étoiles libres), là où C1 a le q:7 (det carré ⟹
    K anisotrope, lignes rigides).
- **À relire par structures** :
  - arête π dans τ ∩ η ⟺ paire frère en c ;
  - la parité par bloc ;
  - la formule 42 + 2|Σ| − 2n_dis.
- **Cloud** : tierpi, les 77 classes à arête π (≥ 6 pivots, pour Σ ≠ ∅), après les 79 (c2-compute f0e73c7).

## 7. Lemme des coupes (structures, NOTE_S29 §9 ; généralise le lemme de C1, notes/134)
- **Énoncé.** Soit c un bloc de type quelconque (μ, τ), et p un bloc gauche ancré en c : p+ et p− sont pivots (μ = τ sur eux),
  sans paire frère. Posons Sp = {p+, p−, μp+, μp−}. Dans toute solution du système local en c :
  - aucun des 30 quadruplets e ∪ ι(e) ne contient les 4 étiquettes de Sp ;
  - au plus un en contient 3 ;
  - aucun n'en contient 3 si μp+ et μp− sont dans un même bloc.
- **Preuve.**
  - Le (ii) par blocs donne une couverture 2 de Sp par les 10 quadruplets passant par p.
  - L'inclusion-exclusion sur le quasi-design donne a₀ = 3 − a₃ − 3a₄ (2 − a₃ − 3a₄ pour un digone).
  - Les étiquettes de Sp sont des pivots, donc jamais centres d'une paire sécante (K₃[b,b] = 0).
- **Usage.** `sat_local2.py --cuts` (structures) ; l'énoncé est écrit en commentaire dans le DIMACS. Exemple : 132 clauses sur
  tier8_0.
- **Route LP indépendante.**
  - structures a exporté les 9 modèles d'étape 1' des types tier-8 (involution/s1p_tier8_0…8.npz, même disposition que les
    blocs pleins : 1 410 ι-paires, 22 560 variables, 1 635 lignes).
  - Correctif export_s1p : [b ∈ e] + [b ∈ f] pour les ι-paires sécantes.
  - `scripts/iota_dfs.py` : DFS sur les ι partiels, PL à chaque nœud, certificats de Farkas exacts, branchement orbital.
  - Correspondance : s1p_tier8_k ↔ tier8_rel[k] ↔ source 6 + k.

## 8. Les (0,6) et le trou du tout-tordu (27/09, matin)
- **Comptage (C2 ; vérifié par C1 et structures).**
  - Les étiquettes par bloc sont en nombre pair, donc dans {0, 2, 4, 6, 8, 12}.
  - Si toutes les classes pertinentes à ≥ 6 étiquettes sont UNSAT, SAUF (0,6), alors chaque bloc est (0,6) ou porte ≤ 4
    étiquettes.
  - Avec k blocs (0,6) : 42 ≤ 6k + 4(7 − k), donc k = 7. Tout bloc est alors (0,6), et T = K₇ (tout tordu).
- **TROU (structures, confirmé par C1).** « T = K₇ mort » (carnet §14/§26/§32, structures S8/S11/S17/S19) suppose que les
  chaînes de paires tordues sont des cycles SIMPLES de K₇ (les 121 215 décompositions de k7_cycle_decomp.py).
  - Or §14 ne prouve que la 2-régularité du graphe D.
  - En tout-tordu, D est un système de TRANSITIONS : en chaque bloc, les 6 orbites pivots sont appariées librement. Les circuits
    peuvent donc repasser par un bloc, par exemple le papillon i–a–b–i–c–d–i.
  - Il y a 15⁷ ≈ 1,7·10⁸ systèmes étiquetés, dont seulement 121 215 à circuits simples.
  - Restent valables pour le non-simple : S8.2, S8.5 et le lemme du coin.
- **Conséquence.** Le théorème Σ = ∅ « un bloc » demande les 79 instances, tier06 compris, OU les 72 plus une preuve du
  tout-tordu non simple. **tier06 reste sur le chemin critique.**
- **Attaque du tout-tordu non simple par le PL d'orbite (C2, 06:30).**
  - `scripts/root_K7.py` : orbit_colmodel_gen avec In[c] = [] pour tout c. Toute structure D y est, donc tout système de
    transitions, simple ou non. 1 764 000 colonnes.
  - Si la racine est faisable : fixation de blocs, 15 appariements par bloc, avec branchement orbital sous S₇.
- **Lemmes ajoutés aux encodages (structures, relus par C1)** : --digon (équilibre de digone, types à digone ancré) et --path
  (« exactement un excès » en chaque bloc chemin ancré non frère, lab 0d4f1fb). Les voies tier8 tournent en encodage 2 avec
  cuts + digon (types 6–8) et cuts + digon + path (types 9–14).
- **Lemme du coin (carnet §15), relu pas à pas par C1 le 27/09.** Il n'utilise ni la simplicité des circuits, ni Σ = ∅.
  - **Hypothèses.** Une paire ij, dont les orbites A₁ et B₁ ont leurs carrés D de même troisième bloc k : D(A₁) = A₂ ⊂ ik et
    D(B₁) = B₂ ⊂ jk.
  - **Conclusions.** e = G_{A₂B₂} = 0 ; ω(A₁) = ω(B₁) = 0 ; Y_A ∩ R_B = R_A ∩ Y_B = ∅ ; far(A₁,B₁) = 2 ; far(A₁,B₂) = 3.
  - **Dépendances.** Lemme 1, Lemme 3, l'identité G² + G = 8I + 4J − Sh − 2(GD + DG) − 2D, le lemme 9.2 et le compte μ = 2.
  - **Lignes d'orbite (C1)**, à ajouter au modèle U si l'arbre K₇ est trop gros :
    - R1 (e = 0, 840 lignes) ;
    - R2/R3 (Y ∩ R = ∅) ;
    - R4 (ω = 0) ;
    - aux nœuds où les transitions en i et j sont fixées, elles deviennent des suppressions de colonnes.
  - Relecture indépendante demandée à structures.
- **État K₇ (06:30).** Racine faisable (135 s) ; nœud 2 (bloc 0 = {12,34,56}) faisable (144 s) ; fixation en cours,
  `logs/run_U_fix_k7fix_K7_alltw.jsonl`.
- **K₇ par le PL d'orbite + coin (06:40) : ne ferme pas.**
  - Le lemme du coin est codé en suppressions de colonnes (R1 e = 0 et R4 ω = 0), re-dérivées par orbit_verify_U (lab c78f316).
  - Racine faisable. Bloc 0 : 1 option sous S₇, faisable. Bloc 1 : 4 options (stabilisateur d'ordre 8).
  - Le nœud {0: 12|34|56, 1: 03|25|46, 2: 06|15|34}, avec le coin (1,2,5), reste FAISABLE. Ensuite, 15 options par bloc et
    stabilisateur trivial : ~10⁵–10⁶ nœuds. Arrêté.
  - Le tout-tordu non simple repose donc sur les 7 SAT (0,6), passés en tête de la file kissat après les 9 tier-8. Autres voies
    possibles : un lemme de simplicité, ou q:7 dans la couche signée.
