# 35 — Suite du 26/09 (matin) : M1-A n = 4…6 et mélanges en calcul ; conception du modèle unifié (carrés disjoints, Σ ≠ ∅)

Session principale C2. L'utilisateur a donné son accord le 26/09 au matin (« do whatever u want ») pour les calculs plafonnés et
certifiés. La machine (Ryzen 7 7800X3D, 16 fils, 31 Go) est partagée : les processus tournent en priorité « inférieure à la
normale », et une veille abaisse la priorité des nouveaux processus.

## 1. M1 à bloc A, n = 4, 5, 6 (`scripts/m1a_pipeline.sh`)
- Les orientations sont d'abord réduites à des classes sous le groupe de la famille (n = 4 : 1 344 orientations, 30 classes). On
  applique le filtre sain à chaque représentant, puis on réduit les squelettes survivants à des classes.
- **Justification de la couverture.** Un squelette étiqueté repose sur une orientation g(O), où O est un représentant. g envoie ses
  squelettes bijectivement sur ceux de O, et le filtre comme le PL sont invariants par renommage des blocs.
- n = 4 : **214 classes**. Les premières sont toutes certifiées, avec des écarts de 69 à 84 et environ 150 s par classe. Les résultats
  sont dans `logs/m1a_res_4_*.jsonl`.
- n = 5 et 6 enchaînent automatiquement.

## 2. Mélanges à plusieurs cycles tordus (`scripts/mix_enum.py`, `mix_filter.py`, `mix_pipeline.sh`)
- Le sous-graphe tordu est un sous-graphe pair de K₇ (espace des cycles, de dimension 15). À isomorphisme près, il y a 54 classes : le vide,
  K₇ (le tout-tordu), 5 cycles simples (M1) et **47 mélanges**.
- **Lemmes de degrés prouvés.**
  - t_c = 2 implique out_c ≥ 2 : f = 2·out + 2, avec out = 0 on a une digone, et avec out = 1 un 4-cycle contenant deux sœurs.
  - t_c = 0 implique d_c ∈ {0, 2, 3, 6} (26.2).
- **Graphe D en un pivot c** : multigraphe sur les paires {c,x} qui ont une orbite de pivot c. Les ancrées en c y sont de degré 2, les
  tordues de degré 1, sans boucle (Σ = ∅). On l'énumère exhaustivement.
- **Filtre général, sain.**
  - Composantes certaines de G_c : les cycles D fermés, c'est-à-dire les composantes du graphe D en c sans paire tordue, et leur
    complément. Un bloc non encore affecté compte pour une seule composante.
  - Profils 27.1 (F1 plus équilibre sur ces composantes).
  - 2-facteur par bloc (19.1) avec la règle typée.
  - Élagage partiel en profondeur : on vérifie un bloc dès que tous les pivots de ses orbites libres sont affectés.
  - Symétrie : Aut(graphe tordu).
- **Contrôle** : sur T = triangle (M1, n = 3), le filtre redonne **exactement les 23 classes** du filtre M1 spécifique.
- **Au niveau orientation, le PL général est faisable** sur 3 orientations aléatoires à deux triangles disjoints. Il faut donc
  passer par les squelettes : filtre, puis PL par classe.

## 3. Modèle unifié : carrés « frère », « un bloc » et « disjoint » (conception, carnet §7–§11 et 19.1)
Pour une racine u = (a)(b), avec a dans le bloc i et b dans le bloc j :

**Comptes λ/μ.**
- Pour chaque bloc lointain t, u a 2 voisins dans star((t,+)) et 2 dans star((t,−)).
- Au bloc i, u a 1 voisin m_i dans star(a) et 1 voisin π_i dans star(−a). Même chose au bloc j.
- Une **boucle** (voisin sœur (a)(−b)) sert à la fois de m_i et de π_j.

**Types de carrés.**
- **Frère** (n_s = 2) : m_i, π_i, m_j et π_j sont les deux racines sœurs. Donc φ(P) = 2, aucun autre voisin dans une paire qui touche i
  ou j, et 10 voisins lointains. L'orbite n'est libre nulle part : elle forme une digone dans R_i et R_j.
  - En plus : grille parfaite (8.1). Une orbite disjointe de P a exactement 1 voisin dans P, et une orbite qui partage un bloc avec P
    en a 0.
- **Un bloc** via i (n_s = 0) : F1 (φ({i,k}) = 2, les autres {i,r} valent 0). L'orbite est libre en j.
- **Disjoint** (partenaire W dans R_D = {k,l}) : φ(R_D) = 2 (11.2). L'orbite est libre en i et en j : n^i et n^j lus sur R_i et R_j.
  - n_s(P) ∈ {0,1}. n_s = 1 est une boucle : c'est une arête sœur dans R_i **et** dans R_j (19.1 n'exclut les arêtes sœurs que pour
    n_s = 0). On a alors 8 + n_s voisins lointains.
  - Sommes lointaines par bloc t : 4 − n^i_t − n^j_t.

**Identités globales**, valables dans tous les cas (contrôlées sur BvLS, tout frère) :
- S = 24, colonnes comprises ;
- PPE Σφ² = 32 − e(R), avec e(R) = 2n_s(R) ;
- couplage ;
- (P2) : 16 − E − 4[partage].

**Colonnes** : (orbite, type, partenaire D, voisins libres à chaque bloc libre, drapeau de boucle, rang lointain exact). Les lignes
de liaison sont : couplage D symétrique, graphes R_s symétriques (2-réguliers sur les orbites libres, coupes impaires, sœurs ≤ 1 si
n_s = 0), n_s cohérent pour les deux sœurs, et grilles frères.

**Portée.** Ce modèle couvrirait :
- les carrés disjoints (famille 4) ;
- les 9 motifs Σ ≠ ∅ encore survivants : K₂, P₃, 2K₂, K₃, P₄, P₃+K₂, 3K₂, P₅, 2P₃ (`data/survivors_after19.txt`) ;
- et, comme cas particuliers, tout ce qui précède.

C'est le travail suivant après les calculs en cours.

## 4. Mélanges : l'explosion, et le bloc A générique (26/09, fin de matinée)
**Constat.**
- Classe « papillon » (deux triangles tordus partageant le bloc 0) : le filtre laisse **12 072 classes de squelettes**. À environ
  60 s de PL chacune (IPM), cela ferait environ 200 h CPU.
- **Tous** ces squelettes ont un bloc A de degré 6 et ne diffèrent que par la structure D de A. Il n'y a que **212 parties hors A**.

**Méthode.**
- **Filtre v3** (`mix_filter3.py`, sain) : la structure de A n'est pas énumérée.
  - Ses orbites entrent dans les graphes libres des autres blocs comme emplacements de triplet inconnu, avec tout vecteur n admis.
  - G_A compte pour une seule composante.
  - Les feuilles sont des parties hors A.
- **PL par partie hors A** (`mix_Agroup3.py`, `gen_colmodel_lam.py`) :
  - les triplets hors A sont fixés ; la structure de A est **variable**, λ_{A,g} parcourant tous ses graphes D ;
  - liaison au niveau paires (Σ sur les 2 orbites de R de la masse des colonnes (pivot c, k) = Σ_g λ_{c,g}·mult_g) ;
  - certificat exact sur toutes les colonnes.
- **Modèle λ** (enveloppe exacte des structures d'un bloc), comparé aux variables m par orbite : plus serré. L'orientation H
  circulante donne un écart de 10,09 au lieu de 7,42. L'orientation (1,0,5) seule reste faisable.

**Contrôles.**
- Sur M1 n = 3, le filtre v3 donne 1 partie hors A. Les 23 classes de référence se réduisent, elles aussi, à 1 partie hors A.
- Le PL la tue : écart 56, certificat exact.
- Filtre v2 avec paires sœurs, sans sœur : **mêmes 23 classes** que le filtre M1 spécifique. Le lemme de queue 26.2 y était
  redondant.
- Papillon, 3 groupes tirés au hasard : infaisables et certifiés, écarts de 14 à 46, environ 70 s chacun.

**Lancé** (`mix3_filter_all.sh`) : filtre v3 sur M1 n = 5 et 6 (cycles simples), puis sur les 47 classes de mélanges. L'étape PL
suivra. L'ancien pipeline M1 s'arrête après n = 4 : n = 5 et 6 passent par v3.

**Modèle unifié, contrôle tout-frère** (`sis_colmodel.py`) : Σ = K₇ donne un PL **faisable** (42 colonnes, toutes les valeurs
lointaines à 1). La contradiction du Théorème D est dans la partie signée (Alt), invisible au niveau paires non signé. Pour Σ ≠ ∅, il
faudra le niveau orbite (identité de « structures », 903 lignes, qui voit la partie antisymétrique) ou les signes.
