# 34 — M1 à bloc A, n = 3 : impossible (certificats exacts), et coût des autres familles (26/09/2026, 06 h 50)

Session principale C2. **Statut : PROUVÉ, preuve assistée.** Le calcul a été fait en petits lots, chaque processus étant plafonné à
5 min. Même moteur que la note 32 (modèle par colonnes avec (P2)), généralisé.

## 1. Généralisation du modèle (`scripts/m1a_colmodel.py`)
- Les orbites deviennent des quadruplets (i, j, k, s). s distingue les deux sœurs d'une paire liée par A : elles ont le même triplet.
- Coupes de sous-tours : tailles 3 et 5 **toujours**, taille 4 **seulement si le bloc a exactement 6 orbites libres**.
  - Les tailles 3 et 5 sont valides pour tout f : le graphe libre n'a que des cycles pairs de longueur ≥ 4 (19.1).
  - Un 4-cycle est possible dès que f ≥ 8, d'où l'absence de coupe de taille 4 dans ce cas.
- Tout le reste est inchangé : valeurs proches (F1, voisins libres), règle typée, sœurs ≤ 1, S, PPE (e(R) = 0 : Σ = ∅, carrés
  « un bloc »), couplage, (P2).

## 2. Famille (a = 1, n = 3)
**Énumération.** `scripts/m1a_classes.py` parcourt toutes les orientations à bloc A (T = (0,1,2)) et tous les choix de structures D
(structures de A comprises). Le filtre sain de blocs (`m1_blocks4.check`) garde **2 928 squelettes étiquetés**.
- Le filtre n'élimine que par des lemmes démontrés : 19.1, profils, 28.x, 30.1 via le 2-facteur, règle typée.
- Classes sous le groupe de la famille (diédral de T × permutations des 4 autres blocs, 144 éléments) : **23 classes**.

**Résultat.** Les 23 classes sont **PL-infaisables**, avec certificat de Farkas rationnel vérifié exactement, écart minimal 75,2.
- **Revérification indépendante** à partir des multiplicateurs stockés (`scripts/m1a_verify_certs.py`, fractions, sans solveur) :
  **23/23, 2 928 squelettes couverts**.
- Certificats : `logs/m1a_certs/*.gz`.

**Théorème 34.1.** La famille M1 (a = 1, n = 3) est impossible. (1,0,3) tombe ici. (1,1,3) était déjà morte (Théorème 28.7), et le
filtre ne lui laisse d'ailleurs aucun survivant.

## 3. Contre-vérification de H-β par « structures » (26/09, 06 h 45)
« Structures » a écrit un vérificateur séparé (`verify_hb_independent.py`, dans son labo), à partir de la seule description.
- Couverture régénérée : les **mêmes 552 classes avec les mêmes multiplicités**.
- Nombre de colonnes **identique** au `ncols` stocké, sur tous les enregistrements testés.
- 8 certificats tirés au hasard : **8/8 valides**.
- La vérification complète des 552 (environ 4,5 h) attend l'accord de l'utilisateur.

## 4. Coût des familles restantes (mesuré en petits tests)
- **n = 4** : l'énumération par le filtre de blocs **dépasse 8 × 280 s**. Partiellement, on a déjà plus de 1 200 squelettes et
  plusieurs centaines de classes (le groupe n'a plus que 48 éléments). Il faut plus de temps pour énumérer, puis environ 50 s de PL
  par classe.
- **n = 5 et n = 6** : non mesurés. Ils sont probablement du même ordre ou plus gros.
- **Estimation** pour clore M1 entièrement par cette voie : quelques heures sur 8 processus. **À soumettre à l'utilisateur.**
- Pistes pour réduire : des lemmes à la main sur la structure de A (l'équilibre en A, dont les composantes sont les cycles de A),
  et un PL plus rapide (`highs-ipm`, conseil de « structures »).
