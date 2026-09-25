# 30 — La famille H se réduit exactement à H-β (paire liée tordue), et la règle typée n_k ≤ 1 (26/09/2026)

Session principale C2. **Statut : DÉRIVÉ à la main**, confirmé par le filtre sain `scripts/m1_blocks4.py` (petit test < 5 min,
avec contrôles).

## 1. Lemme 30.1 (paire liée tordue)
**Énoncé.** Cadre : Σ = ∅, carrés « un bloc » (M1, H, tout-tordu). On suppose :
- en un bloc c, une structure liée fermée, c'est-à-dire une composante L_c = {a, b} de G_c ;
- les paires {c, a} et {c, b} sont ancrées en c ;
- la paire {a, b} est **tordue**.

Alors **f_a ≥ 8 et f_b ≥ 8**, où f = 2·out + t est le nombre d'orbites libres.

**Preuve** (en a ; b est symétrique). Les orbites libres en a sont de trois sortes :
- **X₁, X₂** : les deux sœurs de {a, c}. Elles sont appariées par c et donc libres en a. Par 19.1, elles ne sont pas voisines.
- **P** : l'orbite de la paire tordue {a, b} appariée par b, donc libre en a. Son triple est (b, a, ·).
- **B** : les f_a − 3 autres orbites libres. Chacune est dans une paire {a, r} avec r ∉ {b, c}.

Deux applications de l'équilibre en c (27.1(b)), sur la composante L_c = {a, b} :
- pour P, on a {i, j} = {b, a} ⊂ L_c, donc φ_P({c,a}) + φ_P({c,b}) = 2 − 2 = 0. **P n'est voisine ni de X₁ ni de X₂** sur le cycle libre en a ;
- pour Z ∈ B, on a {i, j} = {r, a}, avec une intersection de taille 1, donc φ_Z({c,a}) + φ_Z({c,b}) = 1. **Chaque Z ∈ B a au plus un voisin
  parmi X₁, X₂.**

Posons A = {X₁, X₂, P}. Il n'y a aucune arête à l'intérieur de A. Ses 6 extrémités d'arêtes tombent donc dans B.
- Si f_a = 6, alors |B| = 3. Les 6 extrémités d'arêtes de B tombent toutes dans A, et chaque Z ∈ B a au plus un voisin X. Chaque Z ∈ B est donc
  voisin de P, et P aurait 3 voisins. ✗
- Si f_a = 4, alors |B| = 1, ce qui est impossible. ∎

(C'est l'analogue « tordu » de 28.5, qui traitait une paire liée ancrée.)

## 2. Théorème 30.2 : H = H-β
Dans H (T hamiltonien, tous les degrés égaux à 2), on a f = 2·2 + 2 = 6 en tout bloc. Soit un bloc α (structure liée sur In(c)) :
- **28.5** : si In(c) est une paire ancrée (corde), la queue a f ≥ 8. ✗
- **30.1** : si In(c) est une paire tordue (arête de T), f ≥ 8. ✗

**Aucun bloc de H n'est α.** Les survivants de H sont exactement les squelettes tout-β, soit 60 orientations × 2⁷ ordres. C'est le cœur.

## 3. Contrôle machine (`scripts/m1_blocks4.py`, `logs/m1_blocks4.log`)
Il s'agit du filtre au niveau bloc v2/v3 (19.1, profils, 28.x), sain. Il est appliqué à une orientation par orbite de D₇ (6 orbites sur 60),
avec des comptes pondérés. Les poids totalisent bien 123 540 = 131 220 − 7 680.
- **Squelettes avec au moins un bloc α : 0 survivant sur 123 540**, que la règle typée soit active ou non.
- Diagnostic sur les squelettes à un seul bloc α (`scripts/h_alpha_diag.py`, 65 s) :
  - 1 280 sont tués avant le niveau bloc, par 28.4/28.5 (In = corde) ;
  - tous les autres le sont par le 2-facteur au bloc c+2, c+3 ou c+4, **exactement au bloc a ∈ In(c) prévu par 30.1**.
- Tout-β : 896 sur 896 survivent sur les 7 premières orientations (course typée, plafond de temps). C'est attendu : c'est le cœur.

## 4. Règle typée n_k ≤ 1 (de « structures », 26/09, redémontrée ici)
Pour une orbite x = (i, j, k), les deux R_j-voisins m_j(x) et π_j(x) ne sont **jamais tous deux dans {j, k}**.

*Preuve.* On écrit m_j = (j,β)(k,γ) et π_j = (j,−β)(k,δ).
- δ = −γ en ferait des σ-conjuguées, et x serait le partenaire D d'une orbite de {j, k}, alors que D(x) ⊂ {i, k}. Donc δ = γ.
- v et σv mettent déjà un voisin sur chaque signe de k. Le sommet intérieur (k,γ) verrait donc 3 voisins de u, alors que μ = 2. ∎

**Effet mesuré : nul** sur M1 et sur H, aux contrôles près (n = 3 : 48 → 48 ; n = 5 partiel : identique). La règle est juste, mais
faible au niveau bloc.
- Avec « structures » : le PPE signé au premier ordre a un relâchement linéaire faisable sur les échantillons à 1 triangle (leur test
  du 26/09). **Le signe au premier ordre ne ferme pas le cœur.**

## 5. État du cœur après cette note
- **H-β** (7 680 squelettes, 60 orientations eulériennes × 2⁷) : tous les leviers locaux sont satisfaits.
- **Tout-tordu à au plus 1 triangle** : « structures » y travaille, et le signe au premier ordre ne suffit pas.
- **M1 avec un bloc A** : survivants du filtre v2/v3 ; n = 3 : 48.
- **Carrés disjoints** : non attribués.
- **Outil suivant** : les identités de second ordre (P2) de C1 (notes/116), vérifiées par « structures ». Pour R ≠ R′ :

  Σ_Z φ_Z(R)·φ_Z(R′) = 16 − E[R][R′] − 4·[R ∩ R′ ≠ ∅].

  Rederivé ici : c'est λ/μ sommé sur R × R′ ; les sommets intérieurs apportent 8 quand les paires partagent un bloc. Ces identités font
  entrer au second ordre les cycles libres, via les termes n_b·n_c aux blocs partagés.
