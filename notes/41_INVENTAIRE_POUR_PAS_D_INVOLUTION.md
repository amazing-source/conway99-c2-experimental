# 41 — Inventaire exact de ce qui reste pour « pas d'involution » (26/09/2026, soir)

Document de coordination pour C1, « structures » et C2 (pilote). Décision de l'utilisateur : C1 et « structures » rejoignent la
branche involution. Objectif : Aut(Γ) = 1, avec « pas d'ordre 3 » de C3, vérifié en Lean, et Aut ∈ {1, Z₂, Z₃} de la littérature.

## 0. Cadre et conventions (carnet §0–§1, labo notes 23–40)
- Γ = srg(99,14,1,2), σ une involution. σ fixe exactement un sommet x (Makhnev–Minakova), et sur N(x) c'est le retournement de
  chaque bloc.
- **Blocs** : les 7 droites par x, notées 0…6. **Intérieurs** : (c,±). **Racines** : les 84 sommets à distance 2, un par couple
  d'intérieurs de blocs différents. **Paires** : les 21 couples de blocs.
- **Orbites** : les 42 orbites de σ sur les racines ; chaque paire en a 2, dites sœurs.
- **Partenaire D** : l'unique orbite W avec q_U(W) = 2.
- **Types de carrés D** :
  - **frère** (sib) : D(U) = sœur de U ;
  - **« un bloc »** par i : D(U) dans une paire {i,k}. Le pivot est i, le bloc libre j, le tiers k ;
  - **« dis »** : D(U) dans une paire disjointe.
- **Σ** = l'ensemble des paires frères.

## 1. Arbre des cas
| famille | statut | références |
|---|---|---|
| Σ = K₇ (tout frère) | **MORT** (à la main) | Théorème D, carnet §7 |
| Σ ≠ ∅, N (paires non frères) à au plus 6 arêtes | **MORT** (à la main) | carnet §11–§13 |
| Σ ≠ ∅, motifs de Σ entre les deux | **MORT** sauf 9 motifs (systèmes χ / RSF, DRAT) | labo notes 18–19, `data/survivors_after19.txt` |
| **Σ ≠ ∅ : 9 motifs survivants** K₂, P₃, 2K₂, K₃, P₄, P₃+K₂, 3K₂, P₅, 2P₃ | **OUVERT** (paires non frères de type « un bloc » ou « dis ») | notes 19–20 |
| Σ = ∅, tout « un bloc », T = ∅ (tout ancré) | **MORT** (à la main) | lemme de la queue, carnet §24 |
| Σ = ∅, tout « un bloc », T = K₇ (tout tordu) | **MORT** (à la main pour ≥ 2 triangles ; certificats sinon, revérifiés par C2) | « structures » S8/S11/S17, carnet §32 |
| Σ = ∅, tout « un bloc », T = un cycle (M1), n = 3, 4 | **MORT** (certificats stockés, revérifiés) | carnet §30–§31, labo notes 34 et 36 |
| M1, n = 7 (H) | **MORT** (H = H-β à la main ; H-β : 552 classes, certificats revérifiés) | carnet §28–§29 |
| M1, n = 5 et n = 6 | **EN FERMETURE** (§2) | labo note 40 |
| Σ = ∅, tout « un bloc », T = mélange (47 classes à isomorphisme près) | **OUVERT**, hormis une partie des classes 0, 1 et 2 (§3) | labo notes 35–36 et 40 |
| **Σ = ∅, au moins un carré dis** | **OUVERT** | labo note 39 ; « structures » et Astra (dossier n° 4) |

Le « bloc A » (degré 6) n'est pas une famille : c'est un trait de nombreuses configurations. Le système A-local, même signé, est
faisable (note 40 §9) : il n'y a pas de lemme « pas de bloc A » local.

## 2. M1 n = 5 et n = 6 : état précis
- **Filtre sain v6** → orientations avec feuilles (`logs/mix6_cls_E01_12_23_34_04_S_*.json` pour n = 5,
  `logs/mix6_cls_E01_12_23_34_45_05_S_*.json` pour n = 6). Un job est une orientation avec feuilles, dans l'ordre des fichiers.
- **n = 6** : 16 jobs.
  - Morts au niveau paires par l'ancien pipeline : jobs 1, 3, 4, 5, 8, ainsi que les feuilles non survivantes des jobs 0, 2 et 6.
    **Contrôlés en exact, mais les certificats N'ONT PAS été stockés** (`mix_union_lp.py` ne sauvait pas y) : à refaire avec
    sauvegarde.
  - Survivants du niveau paires (0 : 2, 2 : 8, 6 : 11) : tués au niveau orbite, certificats stockés et revérifiés.
  - Jobs 0, 9, 10, 13 et 14 : tués au niveau orientation (orbite, D libre), certificats `gen_E01_12_23_34_45_05_*`.
  - Jobs 7, 11, 12 et 15 : en cours. Feuille par feuille (certificats `leaf_*`, tous revérifiés jusqu'ici), puis par **blocs
    fixés** (`fix_*`, `fc_*`).
- **n = 5** : 11 jobs.
  - Jobs 0 à 9 morts au niveau paires, **sans certificats stockés** (même remarque).
  - Job 10 (228 feuilles, 48 classes sous Z₅) : campagne par blocs fixés en cours.

## 3. Mélanges (Σ = ∅, tout « un bloc », T à au moins 2 cycles) : état précis
- **47 classes de T** : `mix_filter.twisted_classes()`. 1 797 classes d'orientations, M1 n = 5 et 6 compris.
- **Filtre v6 fait** pour les classes 0, 1, 2, 3–14 et 17. **Reste à faire** pour 15, 16 et 18–46 (arrêté pour ménager le PC).
- **Tailles après filtre** : classes 6–14 et 17, de 1,3·10⁴ à 2,2·10⁵ classes de squelettes chacune.
- **Classe 0 (papillon)** : jobs 0–9, 11, 12 morts au niveau paires (sans certificats stockés ; les 15 feuilles résistantes par
  branchement sur A, idem). Job 10 (450 feuilles) ouvert.
- **Classe 1** : jobs 1–3 morts (niveau paires, plus 4 survivants tués au niveau orbite avec certificats). Jobs 0 et 4 ouverts.
- **Classe 2** : 9 jobs sur 10 morts au niveau paires (sans certificats). Job 6 (870 feuilles) ouvert.
- **Méthode qui marche** : PL d'orbite avec la structure D **fixée à un seul bloc**, les autres libres.
  - Classe 9 job 42 (146 331 feuilles) : fixer le bloc 0 (21 options) → options 0 et 1 **mortes** (écarts 21,9 et 12,5), environ
    8 000 feuilles chacune en un seul PL.
  - M1 n = 6 job 12 : option 0 du bloc 0 **morte** (écart 2,3, 16 feuilles).
  - Coût : environ 15 à 30 min par PL à 4 cœurs, priorité idle. Il faut le nombre d'options du bloc le plus « ramifié » par
    orientation.

## 4. Carrés dis (Σ = ∅)
- **Lemmes prouvés** : 39.1 (apex), 39.2, 39.3 (boucle ⇒ doublement dis), 39.4 (équilibre sans paires à moitié), lemmes de degré
  AD (d_k ∉ {1,5} ; d_k = 4 ⇒ out_k = 0, dis_k = 2, avec boucles ; d_k ≤ 3 si out_k ≥ 1), dichotomie par paire.
  - Astra, vérifié par « structures » : apex intérieur ⇒ l'autre hors de T ; supports possibles de D(A) ; 3h ≤ 2n_dis.
- **Non tranché** : (2,0) contre (2,1) pour un partenaire dis. Le témoin local (2,1) d'Astra est cohérent.
- **Taille** : le plus petit sous-cas (AD, deux paires dd liées) a déjà **322 classes d'orientations** (niveau orientation,
  lemmes de degré appliqués).
- **Outil prêt** : `scripts/orbit_colmodel_U.py`, modèle unifié au niveau orbite (colonnes dis, boucles, option (2,1)). Il
  reproduit exactement le modèle « un bloc » en régression.

## 5. Σ ≠ ∅ (9 motifs)
- Les paires frères imposent des grilles parfaites (8.1) : toute orbite disjointe d'une paire frère y a exactement 1 voisin.
- Le filtre v6 accepte des paires sœurs (argument `sisE`). Les colonnes frère sont à ajouter au modèle unifié.
- Il faut aussi y traiter les paires dis.

## 6. Certificats : emplacement et format (pour la revérification indépendante)
- **Emplacement** : `logs/orbit_certs/*.json.gz` (dépôt `amazing-source/conway99-c2-experimental`). Vérificateur de référence de
  C2 : `scripts/orbit_verify_certs.py`, dont la docstring donne la sémantique complète.
- **Format** : {"model", "spec", "den": 10⁶, "rows": [[repr(étiquette), 'eq'|'le', rhs, y entier], …], "bounds"}.
  - **fixed** (ancien format, clé "triples") : 42 triplets (pivot, libre, tiers) ; les orbites sont indexées dans cet ordre, et
    D(i,j,k) = l'orbite (i,k,j), digones dans l'ordre.
  - **var** : spec {leaf : 30 triplets hors A, A}. Les orbites 30 à 41 sont (A,x,s), x croissant, s = 0 ou 1. Les orbites de A
    choisissent librement leur tiers et leur partenaire (orbite de {A,y}).
  - **gen** : spec {In : orientation, forbid : liste des (Z, Dz) interdits, allowed éventuel}.
    - Orbites : paires (a < b) dans l'ordre lexicographique, s = 0 ou 1 ; paire ancrée en c : pivot c ; paire tordue : s = 0 a
      pour pivot a, s = 1 a pour pivot b.
    - Partenaires : les orbites de {i,k} de même pivot i.
- **Lignes** :
  - ('one',Z) : 1 ; ('S',W) : Σ_Z q_Z(W) = 12 ; ('C',a,b) : q_a(b) − q_b(a) = 0 ;
  - ('I',a,b), doublée : 2Σ_Z q_Z(a)q_Z(b) + q_a(b) + q_b(a) = 2(12[a = b] + 4 − Sh) ;
  - ('cut',c,S), ≤ : ≤ 2(|S| − 1), pour |S| qui n'est pas une réunion de cycles pairs ≥ 4 ;
  - ('sis5',c,U,U′), ≤ 1 : quand elle est présente.
- **Colonnes** (docstring du vérificateur) :
  - partenaire à 2, F1 ;
  - deux voisins libres distincts parmi les orbites libres au bloc libre, hors sœur, règle typée ;
  - ligne lointaine de sommes de bloc 4 − 2[t = k] − n_t ; double lointain (1,1), valeur 1 sur l'une des orbites.
- **Couverture** :
  - par feuille : `leaf_<classe>_<job>_<t>` couvre la feuille t du job ;
  - par blocs fixés : `fix_<classe>_<job>_b<c>_o<t>` ou `fc_<classe>_<job>_<nœud>` (spec : forbid et assign). Les options d'un
    bloc sont les structures présentes dans les feuilles du job, donc leur réunion couvre toutes les feuilles ;
  - symétrie : REPS = stabilisateur de l'orientation, avec les jobs sym → rep consignés dans `logs/orbit_leaves_*.jsonl`.
