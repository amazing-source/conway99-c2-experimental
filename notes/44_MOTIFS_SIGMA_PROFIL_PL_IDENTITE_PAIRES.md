# 44 — Motifs Σ au modèle U, profil du PL d'orbite, identité générale sur un ensemble de paires (26/09, nuit)

## 1. Motifs Σ ≠ ∅ ancrés (appui à C1) : modèle U à D fixé
C1 réduit les 27 orientations ancrées survivantes à 5 classes à symétrie de Σ près. Au niveau paires, il ne reste que 26
squelettes à D fixé (`logs/fixedD_anchored_C1.json`, `logs/ptype_anchored_C1*.json`).

| classe | U, D variable | U, D fixé (`scripts/run_U_fixed.py`) |
|---|---|---|
| 2K2_or15 (1 choix de D) | — | **MORT**, écart 103,7, 387 s |
| K2_or12, tournoi Z₅ (1 choix) | — | **MORT**, écart 157,2, 155 s |
| K2_or0 (2 choix) | — | a0 **MORT**, écart 70, 566 s ; a1 en cours |
| 3K2_or14 (1 choix) | faisable | **faisable**, 86 s. Solution PL sauvée, remise à C1, qui le tue par q:7 (notes/131 §7, relecture par structures) |
| K3_or0 (21 choix) | faisable | DFS des puits (`scripts/run_U_fix.py`, blocs forcés 1, 3, 5 fixés) : au bloc 0, 3 options mortes sur 6 pour l'instant |

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
