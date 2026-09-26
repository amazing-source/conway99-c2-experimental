# 37 — Tout-tordu exclu (contre-vérification C2), contrôle « tout-frère » au niveau orbites, état des calculs (26/09/2026)

## 1. Contre-vérification indépendante des certificats de « structures » (tout-tordu sans triangle)
- **Scripts** : `scripts/xcheck_structures_orbit_certs.py`, `scripts/xcheck_structures_coverage.py`. Ils n'utilisent que le code C2,
  les fichiers de certificats de « structures » et leur sémantique documentée.
- **Reconstruction.**
  - Colonnes-orbites reconstruites avec mon système local : triplet lu sur la décomposition, voisins libres, rangs lointains exacts,
    expansion 2^m. On obtient 352 800 colonnes-orbites par classe, comme chez eux.
  - Lignes reconstruites depuis les étiquettes : Ysym, Ysub, PPE, C, et P2o doublées.
- **Farkas par orbite, en entiers** : **14/14 VALIDES**, low et high **identiques** aux valeurs stockées, 0 écart de bornes. Écarts
  × 10⁹ : de 0,3575 (zero_04) à 31,38 (zero_11).
- **Couverture** : je réénumère les décompositions de K₇ en cycles sans triangle et en trouve 30 360. Les 14 représentants sont deux
  à deux non isomorphes, et Σ 5040/|Aut| = 30 360.
- **Identité orbite** rederivée pour un k quelconque : Q² + Q = (k − 2)I + 4J − Sh.
- **Conclusion** (carnet §32) : le tout-tordu pur est entièrement exclu, avec trois vérifications. Ce sont celles de « structures »
  (générateur et vérificateur séparé) et la mienne.

## 2. Contrôle : Théorème D (tout-frère) au niveau orbites (`scripts/allsib_orbit.py`)
- 42 orbites frères. Chacune a q_U(U′) = 2, et exactement un voisin par paire disjointe (grille parfaite 8.1), soit 2¹⁰ colonnes par
  orbite (43 008 au total).
- Lignes : une colonne par orbite, couplage, P2o doublées.
- **PL faisable** (écart 0, 19 s). Le niveau orbite ne voit donc pas le Théorème D non plus.
- Explication : la preuve du Théorème D est un argument d'**intégralité et de parité**. Les signes χ = ±1 (I₂ ou X) donnent des triangles
  équilibrés, d'où 2(t₁ + t₂ + t₃) ≠ 0. Un mélange fractionnaire des deux choix (χ = 0) satisfait les identités.
- Conséquence pour Σ ≠ ∅ : quand les paires sœurs dominent, il faudra des arguments entiers (PLNE, ou la parité du Théorème D).
  Les survivants Σ ont au plus 4 paires sœurs, et le reste est non frère, où les PL mordent.

## 3. État des calculs (26/09, après-midi)
- **M1 n = 4 : mort** (note 36).
- **M1 n = 5** : 11 orientations et 163 classes au filtre. Tous les PL d'union sont terminés sans feuille résistante, sauf le dernier
  travail, en cours.
- **Papillon** (mélange, classe 0) :
  - 12 travaux sur 13 enregistrés ;
  - les feuilles résistantes des travaux 0, 3, 4 et 5 (10 feuilles) sont **toutes tuées** par branchement sur la structure de A, en 16 à
    24 PL chacune ;
  - travail 2 (5 feuilles) et travail 10 : en cours.
- **3 pipelines parallèles** (`mix6_pipeline2.sh`, 3 × 4 processus, priorité basse) : M1 n = 6 (370 classes au filtre) et les classes
  de mélanges 1 à 46.
