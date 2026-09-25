# 27 — Équilibre croisé : profils φ des étiquettes, mort du survivant hamiltonien circulant, et diagnostic du cœur (25/09/2026)

Session principale C2, régime sans solveur. Tout est à la main : un seul modèle est calculé explicitement, aucune énumération.

**Statut.** DÉRIVÉ, à relire.

## 1. Le lemme de profil (équilibre croisé)
Notations du carnet §16 : pour une étiquette x (paire {i, j}) et une paire P′ ∌ x, φ_x(P′) est le nombre de voisins de x dans P′.
On suppose que le carré de x est « un bloc », par i, vers D(X) ⊂ {i, k} ; on note v, σv ses sommets.

**Lemme 27.1.**
(a) Les seuls voisins de x qui rencontrent le bloc i sont v et σv. Ce sont m_i(x) et π_i(x) (carnet, Lemme 3). Donc
    φ_x({i, k}) = 2, et φ_x({i, r}) = 0 pour r ≠ k.
(b) **Profil d'équilibre.** Pour tout bloc c ∉ {i, j} et toute composante C de G_c (orbites de ⟨σ, μ_c, τ_c⟩, note 25 §0) :

  Σ_{r ∈ C} φ_x({c, r}) = b_C − |{i, j} ∩ C|,

où b_C est le nombre de blocs de C. En effet, chaque racine de x en star(c) est dans une seule paire {c, r}.

(c) En particulier, pour c = k : si la composante C de G_k qui contient i contient aussi j, et si b_C = 4 (composante
    « serrée »), alors les racines de x dans C sont exactement v et σv. Donc φ_x({k, r}) = 0 pour tout r ∈ C ∖ {i}.

Tout cela n'est que l'équilibre, appliqué **à plusieurs blocs à la fois** à la même étiquette x.

## 2. Le survivant hamiltonien circulant est impossible
Modèle (note 26 §4, version circulante) :
- blocs Z₇ ; paires tordues {m, m+1} ;
- cordes {m, m+2} ancrées en m+2 et {m, m+3} ancrées en m+3, donc In(k) = {k−2, k−3} et Out(k) = {k+2, k+3} ;
- en chaque bloc, structure α : carré de chaîne direct entre P_k = {k−1, k} et P_{k+1} = {k, k+1} (orbites « par k »), plus une
  structure liée sur {k, k−2}, {k, k−3}.

**Composantes en c.**
- L_c = {c−2, c−3} : la structure liée, soit deux digones, avec b = 2.
- M_c = {c−1, c+1, c+2, c+3}, avec b = 4. La digone de chaîne relie c−1 et c+1. Les 6 orbites libres (une de c±1, deux de c+2, deux
  de c+3) forment un seul 6-cycle, car 4 + 2 est impossible.

**Théorème 27.2.** Cette configuration est impossible.
*Preuve.* Soit x dans A₁, l'orbite de la paire tordue {1, 2} appariée par 1 dans le carré de chaîne en 1 à l'orbite « par 1 » de
{0, 1}. Donc i = 1, j = 2, k = 0.
- **En c = 0**, x ⊂ {1, 2} ⊂ M₀ = {6, 1, 2, 3}, avec b = 4. Par 27.1(b) :
  φ({0,6}) + φ({0,1}) + φ({0,2}) + φ({0,3}) = 4 − 2 = 2.
  Or φ({0,1}) = 2 (v, σv), donc **φ_x({0,3}) = 0**.
- **En c = 3**, L₃ = {1, 0}, avec b = 2, et {1, 2} ∩ L₃ = {1}. Par 27.1(b) :
  φ({3,1}) + φ({3,0}) = 2 − 1 = 1.
  Or φ({3,1}) = 0 par 27.1(a), donc **φ_x({0,3}) = 1**.
- Contradiction. ∎
L'orientation miroir (m → m−2, m−3) tombe par symétrie.

## 3. Motif interdit général
Le raisonnement n'utilise que trois faits locaux. **Lemme 27.3.** Soit i un bloc de T. La configuration est impossible si les trois
conditions suivantes sont réunies :
1. la structure est α en i (carré de chaîne direct entre P_i et P_{i+1}) ;
2. il existe un bloc c tel que {c, i−1} et {c, i} soient ancrées en c et forment une structure liée, soit une composante L_c = {i−1, i} ;
3. la structure est α en i−1 avec d_{i−1} = 2, et i−1 → i+1 (la paire {i−1, i+1} est ancrée en i+1). On a alors Out(i−1) = {i+1, c}.

*Preuve.* Soit x dans l'orbite « par i » de P_{i+1} (donc k = i−1).
- En k, la composante M contient i, i+1 et c, et elle est serrée. En effet, c ∈ Out(i−1) ⊂ M_{i−1} : on a i−1 → c, et c ∉ Tw(i−1)
  car {i−2, i−1} est tordue. Donc φ_x({i−1, c}) = 0.
- En c, la composante L_c = {i−1, i} donne φ_x({c, i−1}) = 1.
- Contradiction. ∎

Les variantes (β en i−1, ou i+1 ∈ In(i−1)) desserrent l'une des deux égalités, sans réfutation directe.

## 4. Diagnostic : où l'équilibre est vide, et le vrai cœur
- **L'équilibre ne mord qu'aux blocs où G_c se scinde.** Or les composantes de G_c sont :
  - les **cycles D fermés en c**, c'est-à-dire des cycles du graphe D dont toutes les arêtes passent par c : structures liées,
    triangles D, etc. ;
  - le reste, où les **chemins D en c** (entre paires tordues, à travers des paires ancrées en c) et les cycles libres sont recollés
    par σ ;
  - éventuellement des composantes libres « purement sortantes », d'au moins 3 blocs.
- Un cycle du graphe D (sur les 21 paires) est **mono-pivot** si toutes ses arêtes passent par le même bloc, ce qui revient à ne
  contenir aucune paire tordue. Sinon il est **multi-pivot**.
  - Les configurations ancrées sont entièrement mono-pivot, et elles sont mortes (note 25).
  - Le circulant α mélange mono- et multi-pivot, et il est mort (27.2).
- **Le cœur véritable** : les configurations où G_c est connexe en (presque) tout bloc. C'est le cas quand il n'y a (presque) aucun
  cycle D fermé et que les chemins D traversent les paires ancrées. Exemples :
  - le tout-tordu pur (D décompose K₇ en cycles : G_c connexe partout, « structures ») ;
  - **H-β** : T hamiltonien, avec en chaque bloc le chemin D passant par les deux paires ancrées. Le graphe D est alors un seul
    21-cycle multi-pivot, et G_c est connexe partout.
- Sur ce cœur, l'équilibre est vide, comme les budgets 18.x (« structures », |D| ≤ 2) et les réseaux (N09, N24). **Il faut un levier
  global sur la partie lointaine inconnue.** C'est exactement le « cœur de torsion maximale » de C1.

## 5. Suite
- Classer à la main les mélanges non circulants de M1 avec le motif 27.3 et ses variantes. Les blocs α avec structure liée sont
  les prises.
- Reformuler le cœur de façon invariante : « G_c connexe en tout bloc ». Le proposer comme cible commune à « structures » (tout-tordu)
  et à C1 (torsion maximale).
