# 44 — Motifs Σ au modèle U, profil du PL d'orbite, identité générale sur un ensemble de paires (26/09, nuit)

## 1. Motifs Σ ≠ ∅ ancrés (appui à C1) : modèle U à D fixé
C1 réduit les 27 orientations ancrées survivantes à 5 classes à symétrie de Σ près. Au niveau paires, il ne reste que 26
squelettes à D fixé (`logs/fixedD_anchored_C1.json`, `logs/ptype_anchored_C1*.json`).

| classe | U, D variable | U, D fixé (`scripts/run_U_fixed.py`) |
|---|---|---|
| 2K2_or15 (1 choix de D) | — | **MORT**, écart 103,7, 387 s |
| K2_or12, tournoi Z₅ (1 choix) | — | **MORT**, écart 157,2, 155 s |
| K2_or0 (2 choix) | — | a0 **MORT**, écart 71,5 ; a1 **MORT**, écart 69,2 |
| 3K2_or14 (1 choix) | faisable | **faisable**, 86 s. Solution PL sauvée, remise à C1, qui le tue par q:7 (notes/131 §7, relecture par structures) |
| K3_or0 (21 choix) | faisable | DFS des puits (`scripts/run_U_fix.py`, blocs forcés 1, 3, 5 fixés) : les **6 graphes D du puits 0 meurent tous** (3 doubles digones, 3 C₄) : **MORT** sans fixer les puits 2 et 4 |

- **Bilan : la famille ANCRÉE des motifs Σ ≠ ∅ est entièrement morte.**
  - K₃, K₂ (ses deux classes) et 2K₂ : modèle U, secteur pair, certificats revérifiés indépendamment : 2 + 2 + 6 VALIDES,
    avec les mêmes nombres de colonnes.
  - 3K₂ : par q:7 (C1, notes/131 §7), relecture indépendante de « structures » en cours au moment de la panne de leur
    machine.
- **Revérification.** `orbit_verify_U.py` est étendu aux frères (q[sœur] = 2, sommes lointaines de 4, jamais libres), au
  filtre grille 8.1 et aux partenaires interdits. Les deux certificats `sibD_*` morts sont VALIDES, avec exactement les
  mêmes nombres de colonnes que le modèle (361 552 et 410 582).
- **Mécanisme.** Deux puits frères pleins meurent déjà dans le secteur PAIR. Les duaux d'IPM sont denses et ne montrent
  aucune concentration sur le bloc croisé des deux puits : il faudrait un certificat à support minimal.

## 2. Profil du PL d'orbite (M1 n = 6, job 0, racine d'orientation, 2,2 M colonnes, 2 202 lignes)
- **Le maître domine.** Il passe de 0,4 s à 120 s par itération à mesure que les colonnes s'accumulent ; la tarification
  reste à 0,6 s. Base : 39 itérations, 2 161 s, INFEASIBLE et VALIDE.

| variante | résultat |
|---|---|
| PER = 15 (plus de colonnes par itération) | pas de gain : le coût du maître suit aussi le nombre de colonnes |
| lissage de Wentges (SMOOTH = 0,6 : tarification au mélange du meilleur point de Lagrange et des duaux du maître) | 35 itérations, 1 725 s, VALIDE : **environ 20 % de gain**, activé pour l'orientation d'abord |
| IREL sans les lignes I entre orbites de paires disjointes (1 782 lignes) | **FAISABLE** : ces lignes sont indispensables |
| maître simplexe primal à démarrage à chaud (WS, WSPRIMAL) | plus lent que l'IPM |

- Options ajoutées dans `orbit_colmodel.py` (le comportement par défaut est inchangé) :
  - LOWMEM (tarification et vérification par morceaux) ;
  - PER, SMOOTH, WSPRIMAL.

## 3. Étape 1 des mélanges : cache de certificats
- Certificats de sommet (simplexe) au lieu de l'IPM. Ils sont creux (environ 770 lignes sur 2 400) et **réutilisables d'une
  feuille à l'autre** du même job : les lignes sont indexées par un sur-ensemble fixe.
- Classe 12 job 3, 250 feuilles : 178 tuées par un certificat en cache, 70 par un PL neuf, 2 ouvertes. Temps moyen : 0,17
  à 0,19 s par feuille au lieu de 0,3 à 0,4.
- Certificats exportés, cache compris, revérifiés par le checker de structures : **298 sur 298**.

## 4. Identité générale pour un ensemble quelconque de paires (généralise (★), note 43)
**Énoncé.** Soit 𝒫 un ensemble de paires ; son graphe des paires sur les blocs a des degrés d_c. On pose Lab = racines
des paires de 𝒫, E_L = arêtes internes à Lab, et f = |𝒫|·e_x + Σ_c d_c·1_{(c,±)} + 1_Lab. Alors 1ᵀf = 9|𝒫|, et l'écart
(Af)_w − 3f_w − |𝒫| :
- est nul en x et en tous les intérieurs ;
- vaut Σ_{c∈P_w} d_c + |N(w) ∩ Lab| − |𝒫| en une racine w ∉ Lab ;
- vaut deg_Lab(r) + d_a + d_b − 3 − |𝒫| en r ∈ Lab (paire ab).

La somme des carrés des écarts vaut **28|𝒫|² − 28 Σ_c d_c² + 84|𝒫| − 14E_L**.

*Preuve.*
- ‖f‖² = |𝒫|² + 2Σd_c² + 4|𝒫|.
- fᵀAf = 2(4|𝒫|² + 5Σd_c² + E_L).
- Σ_w dev_w² = 49‖E₋₄f‖² = 7(3‖f‖² − fᵀAf) + (7/9)(1ᵀf)². ∎

**Cas particuliers.**
- Étoile en k (d_k = s, d_m = 1) : (★).
- Triangle D tordu {i,j,k} (d = 2, |𝒫| = 3) : 14(12 − E_L). C'est le compte exact F5 de structures (S8), puisque les trois
  carrés D donnent E_L ≥ 12.
- D-cycle de longueur L (d = 2) : si chaque racine de Lab n'a que son carré D, le budget restant hors de Lab est
  4L(L − 3)(10 − L). Il est exact seulement pour L = 3.

Au niveau orbite, tout cela est impliqué par les lignes I (même argument qu'en note 43). C'est utile aux modèles par
paires sur les feuilles dures (sans classe fermée d'un bloc), où les composantes D mêlent paires ancrées et tordues.

## 5. Classes à grand T (orientation d'abord)
- Racines d'orientation : classe 22 MORTE (1 sur 1) ; classe 46 (|T| = 18) 2 sur 2 faisables ; classe 42 (|T| = 15) 3 sur 3
  faisables ; classe 44 (|T| = 16) faisable sur ses premières orientations.
- Les blocs entièrement tordus ont 15 graphes D possibles, soit jusqu'à environ 19 M feuilles par orientation. Essai de
  fixation de blocs sur 46/o1 (`logs/run_U_fix_c46.out`) pour mesurer à quelle profondeur l'arbre meurt.

## 6. Calcul cloud (essais du 26/09, soir)
- `scripts/cloud_worker.sh` + `scripts/cloud_stage1.py` : l'étape 1 sans les gros fichiers de feuilles.
  - Les feuilles de chaque orientation sont régénérées par le filtre v6 : même code, même ordre. Le « rep » est l'indice
    d'orientation de `mix_filter6.run`, et le job j est le j-ème rep AVEC feuilles.
  - Le PL par paires tourne ensuite par tranches ; un échantillon des certificats est revérifié par le checker de
    structures.
  - Le modèle de structures est vendorisé sans modification (`scripts/vendor_structures`, commit 746ee31).
- Essai local, classe 10 rep 0 : génération 31 s, 960 feuilles en 50 s, toutes mortes, 48 certificats échantillonnés
  VALIDES.
- Agents « remote » : non disponibles dans cette session (l'agent test a tourné en local et s'est arrêté).
- Session cloud de l'utilisateur : elle signale le dépôt conway comme dangereux, un faux positif sur le vocabulaire
  (« attaquer le cœur »). Pas de contournement caché ; en attente de la décision de l'utilisateur.
- Fichiers de tâches prêts : `logs/cloud_tasks_s1{a,b,c,d}.txt` (classes 9 ; 13 ; 12 ; 14 et 17 ; 883 000 feuilles).

## 7. Fin de soirée (26–27/09)
- **3K₂ ancré : MORT.** C1, notes/131 §7 et §7 bis (commit 1552b9e).
  - Étape 1 : 24 des 48 modèles par paires sont certifiés ici en exact (Farkas au PL, certify.check ; logs/c1_step1_certs.jsonl).
  - Les 24 autres (orbites (2,0) sur le groupe « suivant ») tombent par l'extension q:7 : aucune option (2,0) n'admet la
    permutation signée 8.1 avec la paire frère suivante.
  - Les 512 affectations « perm » sont tuées, énumération reproduite indépendamment par structures.
  - **La famille ANCRÉE des motifs Σ ≠ ∅ est donc entièrement morte**, sous réserve de la relecture par structures de §7 bis.
- **A111111 (3,3) (Sol) : MORT.**
  - Le signe de Witt est relu par structures.
  - Les 15 certificats, la couverture des 400 directions (groupe d'ordre 72), la classe 9 et la classe restante sont revérifiés
    ici indépendamment (`scripts/verify_sol_A33.py`, TOUT PASSE).
- **g⁻ = 16 impossible** (C1, notes/132). Les 8 modèles LP sont certifiés ici (logs/c1_g16_certs.jsonl). Donc g⁻ ∈ {18, 20}.
- **g⁻ = 18** : le balayage de C1 sur les 1 166 classes t = 0 scindées tourne ici (`scripts/c1_g18_sweep_wrap.py`,
  logs/c1_g18/).

## 8. Nuit du 27/09 : M1 fermé, « racine d'abord »
- **M1 n = 5 : FERMÉ.**
  - Le job 10 (228 feuilles) est ALL DEAD en 16 nœuds de fixation, avec branchement orbital (24 612 s).
  - `coverage_check.py E01_12_23_34_04` : 11/11 jobs couverts par des certificats stockés.
  - Les 11 certificats `fc_E01_12_23_34_04_10_*` sont revérifiés par `orbit_verify_certs.py` : ALL VALID
    (logs/verify_m1n5_job10.log).
  - Avec n = 6 (16/16), **M1 est entièrement certifié**.
- **Racine d'abord pour les mélanges.**
  - Constat : le PL racine au niveau orientation (toutes les D-structures, sans fixation de bloc, aucun fichier de feuilles)
    tue tous les jobs essayés.
    - Classe 12, échantillon de 8 jobs (0, 7, …, 49) : 8/8 morts à la racine, 190–380 s chacun.
    - Étape 2 (jobs avec feuilles ouvertes après l'étape 1 par paires) : 12/12 morts au nœud 1.
  - Donc l'étape 1 par feuille est superflue là où la racine meurt. Nouvel ordre : racine par orientation, et étape 1/2
    seulement pour les racines survivantes.
  - `scripts/root_job.py <ci> <rep>`.
    - L'orientation est reconstruite dans l'ordre exact de `mix_filter6.run` ; vérifié sur toutes les reps des classes
      12, 14 et 17 (0 écart).
    - Certificat `logs/orbit_certs/root_<ci>_<rep>.json.gz` (modèle 'gen', spec {In}), qui couvre toutes les feuilles de
      l'orientation.
  - Essai : racine 17/0 morte en 351 s, certificat VALIDE (orbit_verify_certs).
  - Cloud (c2-compute cd138be) :
    - rtA = classe 13 (58 reps) + classe 17 (reps 1–6) ;
    - rtB = classe 12 (45 reps restantes) + classe 14 (33 reps) ;
    - ils remplacent s1c/s1d (étape 1 sur 383 000 feuilles).
  - Local : `scripts/root_queue.sh logs/root_tasks_9.txt`, pour les 18 reps de la classe 9 qu'aucune étape 1 locale n'a
    traitées.
- **Cloud s1b (classe 13, étape 1 par paires) : terminé.**
  - 58 reps, 239 627 feuilles : 198 303 mortes, 41 324 ouvertes, 0 invalide sur les échantillons.
  - Reps 0, 4, 47 et 52 entièrement mortes. Résultats dans logs/cloud_results/.
  - Les ouvertes seront couvertes par les racines (rtA).
- **g⁺ ∈ {14, 16}** (C1, notes/135, test pair) : modules de C1 f66098b dans c2-compute/scripts/c1_gplus (b11a1a6), tâche gp,
  basse priorité, après fb/sat.
