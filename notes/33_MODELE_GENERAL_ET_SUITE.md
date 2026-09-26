# 33 — Le modèle général par colonnes : portée mesurée, limites, et ce qu'il faut pour finir (26/09/2026)

Session principale C2. **Statut** : petits tests uniquement, moins de 5 min chacun ; aucun calcul hors plafond. L'autorisation du
26/09 couvrait H-β seulement.

## 1. Le modèle (`scripts/gen_colmodel.py`)
- On fixe **l'orientation** : chaque paire est tordue ou ancrée en l'un de ses blocs. Hypothèses : Σ = ∅, carrés « un bloc ».
- Tout le reste est variable :
  - le pivot des orbites des paires tordues, les deux sœurs étant sur des pivots différents ;
  - le **couplage D** en chaque pivot (variables m sur les couples d'orbites qui partagent exactement le pivot) ;
  - les **graphes libres** (variables e sur les couples qui partagent exactement le bloc libre) ;
  - les rangs lointains.
- Colonnes : (orbite, pivot, troisième bloc, vecteur n, rang lointain exact). Contraintes : S, PPE, couplage, (P2), coupes
  triangulaires et coupes de 5-cycles (valides pour tout f), sœurs ≤ 1, règle typée.
- Résolution par **génération de colonnes** (tarification exacte par énumération des rangs lointains).
- Certificat vérifié en entiers sur **toutes** les colonnes, énumérées, et sur les bornes des variables m et e.

## 2. Mesures
| orientation | (P2) | résultat |
|---|---|---|
| H circulante (In(c) = {c−2, c−3}), α et β libres | non | faisable |
| H circulante | oui | **infaisable, certifiée** (7,42 > UB 0,0013) : l'orientation entière est tuée |
| M1 (1,0,3), première orientation survivante du filtre | oui | **infaisable, certifiée** (22,7 > 2,25), en 84 s |
| M1 (1,0,5), In(5) = tout, bloc 6 de degré 0 | oui | **faisable** au niveau orientation |
| M1 (1,0,4), première orientation survivante | oui | faisable au niveau orientation |
| M1 (1,0,6), première orientation survivante | oui | faisable au niveau orientation |
| orientation variable (tout libre) | oui | faisable |
| T = C₇ tordu, ancrages variables | oui | faisable |
| tout tordu, décomposition variable | oui | faisable |

- **Lecture.** Au niveau « orientation fixée », le PL tue parfois tout, mais pas toujours : les structures D fractionnaires
  (mélanges de squelettes) peuvent le satisfaire. Au niveau « squelette fixé », il a tué 552 classes sur 552 (note 32).
- **Branchement au niveau des paires** (M_{c;x,y} = 0 contre ≥ 1), orientation (1,0,5) : 28 nœuds, 9 élagages certifiés, encore
  ouvert à 280 s (profondeur 14). M1 à bloc A coûtera cher par ce moteur seul : il faut d'abord réduire les structures de A par des
  lemmes.
- **Branchement sur les variables m** (DFS, élagage certifié), testé sur l'orientation (1,0,5) : profondeur 14 sans aucun élagage en
  270 s. Brancher orbite par orbite est trop fin, à cause de la symétrie des sœurs. Il faut brancher sur le **graphe D au niveau des
  paires** en chaque pivot, par exemple d'abord sur la structure du bloc A (130 structures), comme au niveau squelette.

## 3. Lecture humaine des certificats (avec C1)
- Squelette circulant : W, la matrice des multiplicateurs (P2) et (PPE), est indéfinie ; la restriction de rang 8 suffit, celle de
  rang ≤ 6 non.
- **Une seule identité circulante**, W symétrisée par Z₇ puis arrondie aux demis (diagonale −1, valeurs {0, ±½}), tue ce squelette
  (écart 22,4). Les ansätze de Johnson purs (I, A_J, A_K) ne suffisent pas.
- La forme du certificat : pénaliser les doubles, récompenser la co-occurrence de blocs qui partagent une classe, avec une correction
  circulante sur les paires disjointes (C1).
- Test sur les 552 classes (W de chaque certificat, 2W arrondie, une seule identité) : `logs/hb_round_*.jsonl`, voir la note 32 §7.

## 4. Ce qu'il reste pour la branche C2, et le coût d'une fin par cette méthode
1. **M1 avec un bloc A** : (1,0,n) pour n = 3…6, et (1,1,4), (1,1,5).
   - Il y a 744 orientations étiquetées survivant au filtre de blocs.
   - Au niveau orientation, le PL tue certaines d'entre elles. Pour les autres, il faut brancher sur la structure de A (≤ 130) et sur
     les choix des blocs de T.
   - Estimation : quelques heures de calcul sur 8 processus, avec certificats. **Demande d'autorisation.**
2. **Mélanges à plusieurs cycles tordus** : les orientations ne sont pas encore énumérées. Il faut d'abord des lemmes de réduction
   (queue, 26.x, 28.x, degrés), à la main.
3. **Tout-tordu** : « structures », même moteur par décomposition fixée, calcul autorisé par l'utilisateur. **Le tout-tordu à
   1 triangle est impossible et certifié** (NOTE_S17, 44264f9) : 15 classes (41 790 étiquetées), 84 certificats entiers revérifiés
   indépendamment, couverture vérifiée. Le cas sans triangle (14 classes) est en cours.
4. **Carrés disjoints** : à modéliser. Un type d'orbite « libre aux deux blocs » avec φ(paire D) ≥ 2 s'ajoute naturellement aux
   colonnes.
5. **Σ ≠ ∅** : les 10 survivants de la note 20 (au moins un bloc libre) sont à revoir avec ce moteur.
