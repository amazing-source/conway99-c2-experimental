# 43 — Moteur par paires, équilibre général (★), campagnes du 26/09 (nuit)

Session principale C2 : 4 cœurs, priorité idle, ~6 Go de RAM au plus, car l'utilisateur se sert du PC.

## 1. Bilan des fermetures
- **M1 n = 6 : FERMÉ.**
  - Les 16 orientations sont mortes. La dernière, l'orientation 12, est tombée par fixation de blocs : 7 nœuds, tous morts, certificats `fc_*`.
  - Les refaits avec certificats stockés sont en file (jobs 2 à 6 et 8).
- **M1 n = 5.**
  - Jobs 0 à 9 : morts à la racine d'orientation, avec certificats stockés.
  - Job 10 : fixation de blocs en cours. Racine faisable ; bloc 0, option 6 faisable ; enfants à deux blocs morts.
- **AD2 : FERMÉ.** Les 322 classes d'orientation meurent :
  - 308 par la queue (24.1) ;
  - 14 au PL d'orbite unifié, modèle U.
- **Revérification indépendante.**
  - `orbit_verify_certs.py` : les 80 certificats d'orbite (gen, fc, fix, leaf, surv) sont VALIDES.
  - `orbit_verify_U.py` : les 15 certificats `ad2_*` sont VALIDES.

## 2. Le modèle par paires de « structures » comme moteur
Référence : `external_structures/ad/general_model.py`, cloné et gitignoré, relu sain en note 41.
- **DFS de blocs relâché (blocs non fixés = partenaires libres) : inutile.**
  - Classe 9 job 42 : de 1 à 5 blocs fixés, résultat « inconnu » partout (B&B de 60 nœuds).
  - Seules les feuilles meurent. « structures » arrive au même constat.
- **Bloc A libre : inutile.** 24 feuilles avec A (M1 n = 6 job 12, classe 0 job 3, classe 3 job 10) sont toutes inconnues à 100 nœuds. Les feuilles avec A restent donc au PL d'orbite.
- **Par feuille (sans A).**

  | échantillon | mortes au PL | remarque |
  |---|---|---|
  | classe 12, 40 feuilles | 40 | |
  | classe 13, 15 feuilles | 13 | |
  | classe 9, 240 feuilles | environ 60 % | le reste demande du branchement, souvent au-delà de 400 nœuds |

  Sans dichotomie, 0 feuille sur 45 meurt ; sans équilibre, 0 sur 45 non plus. Les deux sont indispensables.
- **Les feuilles dures sont celles sans classe D fermée.** Classe 9 job 42, 240 feuilles :

  | classes fermées | mortes au PL |
  |---|---|
  | 0 | 3 sur 61 |
  | 1 | 93 sur 126 |
  | 2 ou plus | 53 sur 53 |

- **`scripts/pair_fast.py` : même modèle que general_model, résolu vite.**
  - Mêmes variables et mêmes lignes. Un seul modèle HiGHS par job ; d'une feuille à l'autre ne changent que :
    - les bornes de pivot ;
    - les lignes d'équilibre (sur-ensemble, activées par leurs bornes) ;
    - les coefficients de dichotomie.
  - Phase 1 en IPM à la racine : de 0,15 à 0,4 s par feuille selon la charge.
  - Les certificats de Farkas sont rationalisés (10⁶), vérifiés ici en entiers exacts, puis exportés dans l'indexation de lignes de general_model.
  - **Revérification par le code de structures** (`scripts/pair_verify_leaves.py`) : le squelette est reconstruit indépendamment, puis viennent general_model.build et certify.check en rationnels exacts. Résultat : 40 sur 40 valides.

## 3. Lemme (★) : équilibre général, pour TOUT ensemble de blocs — PROUVÉ
**Énoncé.** Soit k un bloc et S un ensemble de blocs avec k ∉ S ; on note s = |S|. On pose :
- Lab = les 2s orbites des paires {k,m}, m ∈ S ;
- g_o = Σ_{m∈S} φ_o(km) pour o ∈ Lab, paire propre comprise : c'est le nombre de voisins d'une racine de o dans Lab ;
- δ_W = |P_W ∩ S| + Σ_{m∈S} φ_W(km) − s, pour une orbite W dont la paire évite k ;
- ε_W = Σ_{m∈S} φ_W(km), pour une orbite W par k hors de Lab.

Alors
  **Σ_{W : k∉P_W} δ_W² + Σ_{W∋k, W∉Lab} ε_W² = Σ_{o∈Lab} (2 − g_o)(g_o + 5).**

*Preuve.*
- On pose f = s·e_x + s·1_{(k,±)} + 1_{(m,±), m∈S} + 1_Lab. Alors ‖f‖² = 3s² + 6s et 1ᵀf = 9s.
- De plus fᵀAf = 2(9s² + 5s + E_L), où E_L est le nombre d'arêtes internes à Lab.
- Avec E₋₄ = (3I − A)/7 + J/63, on obtient ‖E₋₄f‖² = (8s − 2E_L)/7.
- Or Af = 3f + s·1 − 7E₋₄f (car 11E₁₄f = s·1). Donc Σ_w ((Af)_w − 3f_w − s)² = 7(8s − 2E_L).
- Valeur de l'écart (Af)_w − 3f_w − s selon le sommet w :
  - 0 en x, en (k,±), en (m,±), et aux intérieurs des autres blocs ;
  - deg_Lab(r) − 2 en une racine r de Lab ;
  - δ_W en une racine qui évite k ;
  - ε_W en une racine par k hors de Lab.
- On a E_L = Σ_{o∈Lab} g_o. On divise par 2, puisque σ fixe chaque bloc et que les deux racines d'une orbite ont les mêmes comptes.
- Enfin, (g − 2)² + 7g − 14 = (g − 2)(g + 5). ∎

**Remarques.**
- Aucune hypothèse sur D : l'énoncé vaut aussi avec des paires dis et frères.
- Par F1 en k, g_o ≤ 2, donc chaque terme de droite vaut 10 (g = 0), 6 (g = 1) ou 0 (g = 2).
- **Classe D fermée** : g_o = 2 partout, donc tous les écarts sont nuls. C'est l'équilibre 24.0 avec ses zéros ; s = 3 redonne le lemme du triangle (note 42 §4).
- **Composante ouverte** : il reste un budget d'écart de 10 par orbite de Lab à g = 0 et de 6 à g = 1. C'est exactement là où l'équilibre usuel est vide (G_k connexe, riches en dd, « tout dis »).
- **Au niveau orbite, (★) est IMPLIQUÉ par les lignes du modèle.**
  - Sa partie quadratique Σ_W (ℓ·q_W)² vaut Σ_{a,b∈Lab} (Q²)_{ab}, fixée par les lignes I à Σ_{a∈Lab} g_a près.
  - Sa partie linéaire se ramène, via C, à Σ_{a∈Lab} Σ_{t∈S} D_a(t), où D_a(t) est le nombre de voisins racines de a dans les paires par t. On a D_a(t) = 4 si t ∉ P_a et 2 sinon, par μ = 2 avec (t,±) et F1 ; c'est construit dans chaque colonne.
  - (★) ne renforce donc que les modèles par paires, qui n'ont pas l'identité quadratique.
- **Test** (`scripts/star_test.py`, MILP, carrés linéarisés en one-hot) sur les feuilles 101, 102 et 103 de classe 9 job 42, inconnues à 401 nœuds dans certify de structures :
  - (★) sur les composantes D de chaque bloc : la 101 meurt en 1,6 s, les 102 et 103 ne sont pas résolues à 120 s ;
  - (★) sur tous les S : 111 000 variables, trop gros.
- Envoyé à structures et à C1 ; C1 l'ajoute à sib_model.

## 4. Campagne des mélanges Σ = ∅ : plan en deux étapes
- **Taille des classes filtrées** (3 à 14 et 17, plus 0 à 2) : 373 jobs.
  - 288 jobs sans A, 976 776 feuilles : 181 jobs entre 1 000 et 10 000 feuilles, 13 entre 10 000 et 100 000, et le job 42 de la classe 9 à 146 331.
  - 85 jobs avec A, 12 834 feuilles.
- **Étape 1** (`scripts/pairfast_queue.sh`, `logs/pairfast_tasks.txt`, petits jobs d'abord) : pair_fast sur chaque feuille sans A, PL seul, sans branchement.
  - Sorties : `logs/pair_certs/leaf_<ci>_<job>.jsonl.gz` et la liste des feuilles ouvertes `open_<ci>_<job>.json`.
  - Les petits jobs meurent entièrement au PL.
- **Étape 2** : fixation de blocs au PL d'orbite (`orbit_fixcamp.py`) sur les seules feuilles ouvertes. Les jobs avec A passent directement à l'étape 2 : classes 0 à 2 dans `fixcamp_tasks1`, les autres dans `fixcamp_tasks2`.

## 5. Σ ≠ ∅ (appui à C1)
- **Modèle U avec colonnes frères** : q[sœur] = 2, sommes lointaines de 4, frères jamais libres, filtre grille 8.1 sur toutes les colonnes. Le vérificateur indépendant `orbit_verify_U.py` est étendu aux frères, sans régression sur AD2.
- **Les 27 orientations ancrées survivantes de C1** (`logs/ptype_anchored_C1.json` : K₃ ×1, 3K₂ ×2, 2K₂ ×24) passent en PL U (`scripts/run_U.py`, sortie `logs/run_U_sibanch.out`). Tailles : de 0,3 à 2 M colonnes.
- **Famille TORDUE.**
  - Le filtre v6 avec Σ et un grand T explose : de 60 000 à 130 000 feuilles en 15 min pour K₃ avec |T| entre 15 et 18. C'est l'absence du lemme de queue plus beaucoup de pivots tordus. La campagne est **arrêtée**.
  - Classes d'orientation après 19.1, sommées sur tous les T pairs qui évitent Σ :

    | motif | classes d'orientation |
    |---|---|
    | K₃ | 212 |
    | 3K₂ | 625 |
    | 2K₂ | 4 078 |
    | K₂ | 5 720 |

  - Proposition à C1 : un PL U par orientation pour K₃ et 3K₂ ; pour 2K₂ et K₂, il faut de la théorie d'abord.

## 6. Résidus AD de « structures » (n_dd = 7 et 8, bloc A)
- Données : 10 classes, dans `logs/ad_residues_n7_8.json`.
- Taille : 17,7 à 18 M colonnes, environ 8 300 lignes.
- Nouveau mode `LOWMEM` dans `orbit_colmodel.py` : tarification par morceaux de 400 000 colonnes, sans cache float32, et vérification exacte elle aussi par morceaux. Le modèle tient ainsi en environ 1 Go.
- En cours sur une voie (`logs/run_U_adres.out`).
