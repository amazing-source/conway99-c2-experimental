# 42 — Blocs fixés, configurations AD, et comptages exacts d'un triangle de bloc (26/09/2026, soir)

Session principale C2, à 4 cœurs en priorité idle et avec environ 6 Go de RAM : l'utilisateur se sert du PC.
Répartition décidée avec l'utilisateur :
- C2 pilote, et ferme M1 et les mélanges « un bloc » ;
- « structures » : AD, puis la famille dis générale, et la revérification indépendante des certificats ;
- C1 : motifs Σ ≠ ∅ ;
- Astra : dossiers ciblés.

## 1. Fixer la structure D d'UN seul bloc (`scripts/orbit_fixblock.py`, `scripts/orbit_fixcamp.py`)
Le PL d'orbite au niveau orientation est souvent faisable, alors qu'au niveau feuille il est très infaisable. Entre les deux, **fixer
un seul bloc suffit souvent**.

| cas | bloc fixé | résultat |
|---|---|---|
| classe 9 job 42 (146 331 feuilles, sans A) | bloc 0 (21 options) | options 0 et 1 **mortes**, écarts 21,9 et 12,5 (environ 8 000 feuilles chacune) |
| classe 9 job 42 | bloc 3 (3 options) | option 0 (**63 503 feuilles**) **morte**, écart 15,8 |
| M1 n = 6 job 12 (48 feuilles) | bloc 0 (3 options) | option 0 morte (écart 2,3) ; option 1 **faisable**, donc on fixe un second bloc |

- **Campagne `orbit_fixcamp.py`** : un nœud est une affectation partielle {bloc : option}.
  - Les options d'un bloc sont celles des feuilles filtrées compatibles avec les blocs déjà fixés ; leur réunion couvre toutes les
    feuilles.
  - Nœud mort : certificat `fc_*` (modèle gen + forbid). Nœud faisable : on fixe un bloc de plus, par défaut **le bloc qui a le moins
    d'options > 1**.
  - Démarrage à chaud : chaque enfant part des colonnes de son parent.
- **Couverture** (`scripts/coverage_check.py`) : chaque feuille de chaque job est couverte par un certificat **stocké** (gen, fc, fix,
  leaf), symétries du stabilisateur comprises.

## 2. Les morts de l'ancien pipeline par paires n'avaient pas de certificat stocké
`mix_union_lp.py` contrôlait y en exact mais ne le sauvait pas. Pour la revérification, tous ces jobs sont **refaits au niveau
orbite** : file `logs/fixcamp_tasks1.txt`, 45 jobs (M1 n = 5 et 6, papillon, classes 1 et 2).
- M1 n = 5, jobs 0, 1 et 3 : morts à la racine.

## 3. Configurations AD (paires ancrées + doublement dis, sans paire à moitié)
- **Énumération** (`scripts/ad_enum_all.py`), avec les lemmes de degré (39.4) et la queue (24.1) appliqués aux carrés forcés : digone
  si d = 2, triangle si d = 3, bras de A si d = 6.
  Survivants à S₇ près : n_dd = 2 → 14 (sur 322 orientations) ; 3 → 8 ; 4 → 510 ; 5 → 853 ; 6 → 4 594 ; 7 → 4 328 ; 8 → 6 707.
- **PL d'orbite unifié** (`scripts/orbit_colmodel_U.py`, colonnes dis, boucles, option (2,1)) : AD2 rep 0 meurt, écart 425 ; les
  survivants 69, 130, 132 et 183 meurent, écarts de 115 à 194.
  - **Vérificateur indépendant** `scripts/orbit_verify_U.py`, avec sa propre énumération des colonnes dis : VALIDE, mêmes nombres de
    colonnes.
- **« structures » tue AD au niveau paires** (équilibre sur les D-cycles fermés et F_k, zéros, dichotomie, preuves à UNE racine) :
  n_dd = 2 : 14/14 ; 3 : 8/8 ; 4 : 510/510 ; 5 en cours. La suite AD (n_dd ≤ 21) et la famille dis générale lui reviennent.

## 4. Lemme (comptages exacts d'un triangle de bloc) — PROUVÉ, relu par « structures »
**Énoncé.** Le bloc c porte trois paires {c,x}, {c,y}, {c,z} ancrées en c, formant un triangle D fermé par c. Soit Lab les 12 racines
de ces paires. Alors, pour toute racine w ∉ Lab :
- |N(w) ∩ Lab| = 0 si la paire de w contient c ;
- 2 si elle rencontre {x,y,z} en un bloc et évite c ;
- 1 si elle est incluse dans {x,y,z} ;
- 3 si elle évite {c,x,y,z}.
De plus, E_L = 12.

*Preuve.*
- On pose f = 3e_x + 3·1_{(c,±)} + 1_{(x,±),(y,±),(z,±)} + 1_Lab. Alors ‖f‖² = 45 et 1ᵀf = 27, et fᵀAf = 2(96 + E_L).
- Avec E₋₄ = (3I − A)/7 + J/63, on obtient ‖E₋₄f‖² = (24 − 2E_L)/7.
- Les trois carrés donnent E_L ≥ 12. Donc E_L = 12 et Af = 3f + 3·1.
- Lu en w (où f_w = 0) : 3[w ∋ c] + #(intérieurs de w dans {x,y,z}) + |N(w) ∩ Lab| = 3. ∎

Avec 16.2 (digone : 0/1/0/2), c'est l'équilibre de 23 §8 sur une composante fermée de G_c. Forme générale, due à « structures » :
#(intérieurs de w dans S) + Σ_{m∈S} φ_w(km) = |S|.
- **Filtre de colonnes** : `closed_structures` et `apply_exact_filters` dans `orbit_colmodel_U.py`. Sur AD2 rep 69, les colonnes
  passent de 3 531 272 à 189 280, et **deux orbites n'ont plus aucune colonne** : mort combinatoire, avant tout PL.

## 5. Coût restant (estimation) et ressources
- **Mélanges « un bloc »** : environ 345 jobs dans les 13 classes déjà filtrées, et sans doute autant dans les 31 autres.
  - Si le bloc le plus pauvre tue : environ 800 PL dans les classes filtrées ; si c'est le plus riche, environ 4 600.
  - Au total, de 1 000 à 1 500 h CPU environ. C'est deux semaines à 25 % de ce PC, 4 à 5 nuits à pleine puissance, ou moins d'une
    journée sur un cluster.
- **RAM** : à un moment, 1,4 Go libre seulement pendant que l'utilisateur jouait. Les tests lourds (modèle UT à 27 M colonnes, pilote
  classe 9) ont été arrêtés. Garder à peu près 6 Go au plus pour mes processus.
