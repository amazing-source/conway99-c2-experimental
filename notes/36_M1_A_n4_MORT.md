# 36 — M1 à bloc A, n = 4 : impossible (certificats exacts) ; état du pipeline des mélanges (26/09/2026)

Session principale C2. Calcul plafonné, fait avec l'accord de l'utilisateur (26/09 au matin), en priorité basse sur la machine
partagée. **Statut : PROUVÉ, preuve assistée.**

## 1. M1 (a = 1, n = 4)
- **Orientations.** Il y a 1 344 orientations à bloc A (T = (0,1,2,3)). Sous le groupe de la famille (diédral de T × S₃), elles
  forment **30 classes**. Pour chaque représentant, tous les choix de structures D passent par le filtre sain `m1_blocks4.check`.
  Les survivants se réduisent à **214 classes** de squelettes (`scripts/m1a_classes2.py`, `logs/m1a_classes_4.json`).
- **Couverture.** Tout squelette étiqueté repose sur une orientation g(O), où O est un représentant. Le filtre et le PL sont
  invariants par renommage.
- **Résultat.** 214 classes sur 214 sont PL-infaisables, avec le modèle par colonnes et (P2) (`m1a_colmodel.py`, coupes 3/5, et 4 si
  f = 6). Chaque certificat de Farkas rationnel est vérifié exactement. L'écart minimal est de 16,4.
- **Revérification indépendante** (`m1a_verify_certs.py`, fractions, sans solveur) : **214/214**.
- Certificats : `logs/m1a_certs/m1a_res_4_*.jsonl.gz`.

**Théorème 36.1.** La famille M1 (a = 1, n = 4) est impossible. Cela couvre (1,0,4) et (1,1,4).

## 2. Pipeline v6 pour M1 n = 5, 6 et les 47 mélanges (`mix6_pipeline.sh`)
**Filtre v6** (`mix_filter6.py`), sain :
- sous-graphe tordu quelconque, lemme de queue 26.2 si Σ = ∅ ;
- bloc A générique : un emplacement d'orbite de A n'admet que les vecteurs n faisables pour **au moins un** troisième bloc ;
- les feuilles sont enregistrées par orientation, dans l'étiquetage du représentant.

**PL d'union par orientation** (`mix_union_lp.py`) :
- un PL par orientation, avec la **réunion** des triplets de ses feuilles et la structure de A variable (λ). S'il est infaisable,
  toutes ses feuilles meurent, car le PL de chaque feuille est plus contraint ;
- sinon, on scinde les feuilles récursivement. Une feuille isolée qui reste faisable subit un **branchement sur la structure de A** :
  les 130 graphes D sont découpés selon le partenaire d'une paire A–x à la fois.

**Mesures.**
- Papillon (classe 0) : 13 orientations à feuilles, 773 feuilles. Beaucoup d'orientations meurent en un seul PL (24 feuilles en 113 s).
- Les feuilles résistantes (10) tombent par branchement sur A : 16 PL chacune, environ 20 min. Deux d'entre elles sont faites et
  certifiées, les autres sont en cours.
- M1 n = 5 : 163 classes au filtre v6. Les PL d'union sont en cours ; les premiers processus se terminent sans feuille résistante.
- Deux survivants au niveau paires avec A variable (papillon job 0, et M1 n = 5 partie 28 de l'ancien pipeline) : **toutes les 130
  structures de A tuées**, 16 PL chacun.

**Contrôles.** Filtre v2 sans sœur : mêmes 23 classes que le filtre M1 pour n = 3. v3 (A générique) donne 1 partie hors A, comme la
référence, et le PL la tue.
