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
