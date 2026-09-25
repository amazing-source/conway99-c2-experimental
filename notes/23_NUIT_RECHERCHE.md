# 23 — Nuit de recherche autonome (24→25/09/2026) : structures de l'étoile libre, et ce qui ne marche pas

Consigne de l'utilisateur : 8–10 h de recherche seul, **sans rafales de solveurs** (les UNKNOWN ne disent rien) ; mathématiques,
et calculs seulement s'ils se terminent par une réponse définitive.

Notations : bloc libre c (= 1 dans les calculs), X = les 12 vecteurs signés des autres blocs, σ(b) = −b ; formulation compacte
(μ, τ, Φ) de la note 20 §3 ; « cube A111111 » : μ = σ (le couplage M_c n'a que des boucles).

## 1. Faits nouveaux démontrés à la main (DÉRIVÉ)

**1.1 Cycle de coins d'une paire de blocs.** Pour toute paire {i, j}, les 4 racines ±e_i ± e_j sont sur un cycle t-invariant de
longueur **8 − 2·(nombre de boucles de la paire)**. Chaque boucle manquante est comblée par un « sommet de lien » (second voisin
commun, par μ = 2) :
- longueur 4 : paire sœur (le carré de grille) ;
- longueur 6 : une seule boucle (hexagone) ;
- longueur 8 : aucune boucle (octogone).

À l'échelle du graphe, les liens comptés sur tous les triplets (sommet, paire de droites) valent exactement 2n₃ : c'est la
« courbure » de la note 12.

**1.2 Liens de colonne à un bloc libre.** Soit une paire {c, m} non sœur (e_c + e_m ≁ −e_c + e_m). Le second voisin commun de ces
deux racines (en plus de e_m) est une racine z_m. C'est **exactement** le « lien σ » de la formulation compacte : e_m ∈ Φ(z_m) et
−e_m ∈ Φ(−z_m). L'entrée σ de (iii) n'est donc que μ = 2 pour cette paire.
- Dans le cube A111111, z_m évite le bloc m : s'il contenait −e_m, on aurait e_m ∈ Φ(z_m) contre C[−e_m, e_m] = 0.
- Les quatre racines de la paire et ±z_m forment un **hexagone induit t-invariant** :
  (e_c+e_m) – z_m – (−e_c+e_m) – (−e_c−e_m) – (−z_m) – (e_c−e_m) – (e_c+e_m).

**1.3 Holonomie autour de la droite libre** (cube A111111, τ de type (2,2,2)).
- Les trois arêtes de la droite ℓ_c = {x, e_c, −e_c} sont entièrement prismatiques (6 prismes chacune).
- Le transport des directions x → e_c → −e_c → x envoie la droite ℓ_m sur ℓ_{τ-partenaire(m)}. C'est une involution sans point
  fixe des 6 autres directions : une **courbure non nulle concentrée sur la droite libre**.
- Dans BvLS, repli plat de H(11,3) par le code de Golay, l'holonomie est triviale partout.

**1.4 Le théorème C3 dans C2.**
- Si une seconde négation de carte ι_y (y ≠ x, note 13 O3) était un automorphisme, ρ = t∘ι_y en serait un aussi. Or ρ permute
  circulairement une droite : son ordre serait divisible par 3, ce que C3 interdit (preuve Lean).
- Donc, en C2, **t est la seule négation de carte automorphe, et Aut(Γ) = {1, t}**.
- Toute preuve qui ferait apparaître une seconde symétrie cachée tuerait C2.

**1.5 Lemme des carrés one** (proposé par le relecteur A, vérifié) : r_α + r_β ≤ 1 (note 22 §5).

## 2. Obstructions « bon marché » écartées, avec certitude (pas des TIMEOUT)

| famille de certificats | résultat | outil |
|---|---|---|
| invariants linéaires sur Q, F₂, F₃, F₅, F₇, F₁₁ | la cible de (iii) est dans l'enveloppe affine des solutions de (i)+(ii) : dim 66 = tout l'espace permis | `freestar_hull.py`, `freestar_hull_p.py` |
| positivité spectrale (Gram tordu par t) | semi-défini positif pour les 2 903 types | `freestar_twisted_gram.py` |
| parités de Burnside à l'ordre 7 | toutes cohérentes | `order7_burnside.py` |
| identité trace–rang d'Ishida (sommets, droites, arêtes) | cohérente : avec un seul point fixe, les rangs mod 2 sont nuls | à la main |
| comptes de grilles autour d'une droite | identités (N = g₀ + g₁ + g₃) | à la main |

## 3. Heuristique du nombre de solutions
- Une bijection aléatoire des 60 racines satisfait (i)+(ii) avec une probabilité d'environ 10⁻⁶⁰. Il y a environ 10⁸² bijections,
  soit ~10²² solutions de (i)+(ii) (cohérent : SAT en 2 s).
- (iii) multiplie encore par ~10⁻⁴⁰, soit une espérance ~10⁻¹⁸.
- Donc le lemme local de l'étoile libre est **probablement vrai**, mais c'est le profil d'un système surdéterminé **sans certificat
  court évident**. Cela explique l'échec uniforme des solveurs : ce n'est pas un défaut d'encodage.

## 4. Recherches exhaustives sous symétrie (réponses définitives par groupe)
`scripts/freestar_ansatz_search.py`, journal `logs/freestar_ansatz.log`. Φ équivariante sous H ≤ Stab(μ, τ), −id ∉ H. Seuls les
groupes dont la recherche se termine sont comptés.
- A111111, type τ#3 (|Stab| = 12) : aucune solution invariante par le groupe entier (ordre 12) ni par deux des trois sous-groupes
  d'ordre 6 (définitif). En cours : les autres sous-groupes et les types τ#1, τ#2.

## 5. Décomposition κ de la contrainte (iii) (DÉRIVÉ ; calculs CALCULÉ)

**Observation.** (iii) ne dépend de Φ qu'à travers l'involution sans point fixe **κ = Φ ∘ neg ∘ Φ⁻¹** des 60 paires hors μ :
#{w : b ∈ w, d ∈ κ(w)} = Ct[b, d]. Le problème local se scinde donc en deux étages :
- le **problème κ** : trouver un couplage parfait des 60 paires avec les comptes Ct. Ct[b, b] = 2 impose exactement une paire κ
  « partageante » {b+p, b+q} par b, qui est le D-partenaire de l'orbite de e_c + b ;
- l'**étage λ** (λ = Φ⁻¹) : envoyer chaque paire κ sur une paire antipodale {z, −z}, avec (ii).

Reformulations équivalentes de (ii) : G_a = Φ(star a) est un chemin a → τσa plus des cycles évitant −a, et G_{−a} = κ(G_a).
En fermant chaque chemin par l'arête virtuelle {a, τσa} et en bouchant les cycles de τσ, on obtient une **pseudo-surface fermée**
de faces G_a, dont les liens aux sommets sont les Φ⁻¹(star v). C'est une piste topologique, non exploitée.

| test (A111111, 4 types) | résultat | outil |
|---|---|---|
| problème κ seul | **SAT** pour les 4 types (solution revérifiée) | `kappa_cpsat.py` |
| étage λ sur ces κ | **INFAISABLE** en 0,2 s (présolve) pour les 4 | `lambda_given_kappa.py` |
| noyau minimal de cette infaisabilité | 16 cases de (ii), toutes dans les lignes a = ±e_i d'un **seul** bloc (condition de face G_a, κ(G_a)) | `lambda_core.py` |
| κ + une paire de faces (a = +e_6) | SAT pour τ#2 ; rien de conclu pour les autres | `kappa_faces.py` |

La recherche exhaustive maison du problème κ (`kappa_search.py`, `kappa_cover.py`) ne termine pas : l'arbre est trop grand.

## 6. Deux contraintes locales NOUVELLES, absentes de RSF(star(c)) (DÉRIVÉ)

RSF(star(c)), et donc (i)–(iii), ne contient que les conditions λ/μ entre sommets de N(ℓ_c) = X ∪ P_{e_c} ∪ P_{−e_c}.
Deux conséquences valides n'y figurent pas :
- **(iv) μ ≤ 2 entre lointains.** Deux lointains z ≠ z′ ont au plus 2 voisins communs dans N(ℓ_c). Le seul cas non automatique :
  si z et z′ partagent a ∈ X, alors [Φ(z), Φ(z′) adjacentes] + [Φ(−z), Φ(−z′) adjacentes] ≤ 1. Autrement dit, κ envoie deux
  arêtes adjacentes de la face G_a sur deux arêtes disjointes de G_{−a}.
- **(v) λ = 1 entre N(ℓ_c) et les lointains** (cube A111111). Le lointain z_a, l'unique z ∋ a tel que a ∈ Φ(z), vérifie
  −a ∉ Φ(−z_a) et τ(a) ∉ Φ(−z_a).

Toute preuve du lemme de l'étoile libre peut s'en servir.

## 7. Le graphe lointain F (60 sommets, 8-régulier) : tests spectraux (DÉRIVÉ, CALCULÉ ; résultat NÉGATIF définitif)

Notations : B est l'incidence N(ℓ) × F, et BBᵀ (36 × 36) est connu au niveau du TYPE (μ, τ) : ce sont les comptes (ii), (iii) et
leurs symétriques.
- A_F² + A_F = 12I + 2J − BᵀB.
- A_F Bᵀ = −Bᵀ(I + A_NN) + 2J.
- tr A_F³ = 6(32 − T), avec T = #{b : τb = σb} le nombre de droites transversales ; il y a 32 − T droites entièrement dans F.

Le spectre de A_F est donc fixé par le type, sauf la répartition 3 / −4 sur ker B. Le test exact (polynôme caractéristique de BBᵀ
sur ℚ, facteurs de p(12 − t − t²), multiplicités entières, traces 1 et 3) est `far_spectrum_exact.py`,
`logs/far_spectrum_exact_all.txt`. **Les 2 903 types passent** : aucune obstruction de ce côté. Par exemple, pour
A111111/(2,2,2) : spec A_F = {8, 3¹⁸, 2³, 1⁶, 0³, −1¹⁰, −2³, −3⁶, −4¹⁰}, avec 189 quadrilatères dans F.

## 8. Lemme d'équilibre (DÉRIVÉ, preuve humaine complète)

**Lemme.** Soit ℓ une droite quelconque de Γ, et C une composante connexe du graphe induit sur N(ℓ) (3-régulier : couplages
internes + couplages entre classes). Alors **chaque sommet lointain de ℓ a exactement |C|/6 voisins dans C**.

*Preuve.* On a BBᵀ = 12I − A_NN − A_NN² + 2J − diag(J₁₂). Comme A_NN 𝟏_C = 3·𝟏_C et que C coupe chaque classe en |C|/3
sommets, on obtient Σ_{u′∈C} BBᵀ[u, u′] = 2|C| − |C|/3 pour u ∈ C. D'où Σ_z n_C(z)² = 5|C|²/3. Par ailleurs Σ_z n_C(z) = 10|C|.
La variance de n_C sur les 60 lointains est donc nulle. ∎

Pour ℓ = ℓ_c, les composantes correspondent aux orbites S de ⟨σ, μ, τ⟩ sur X (|C| = 3|S|, donc |S|/2 voisins par composante).
Pour une droite d'une grille 3×3, les deux autres lignes forment une composante de taille 6 : tout lointain de la droite a
exactement un voisin parmi elles.

Conséquences pour A111111/(2,2,2), dont les composantes sont 3 « quads » de 12 sommets :
- chaque lointain a exactement 2 jetons (voisins) par quad ;
- les comptes de profils par quad sont **exactement** les coefficients de BBᵀ ;
- chaque paire κ porte au plus 2 jetons par quad.

| relaxation, avec équilibre | résultat |
|---|---|
| κ + équilibre (τ#0, τ#1, τ#2) | SAT |
| système des types de profils de quads (τ#0) | 27 solutions |
| niveau des blocs, signes oubliés (τ#0) | SAT (0,3 s) |
| modèle complet + (iv) + (v) + équilibre, CP-SAT 240 s | aucune réponse (non consigné comme résultat) |

Bilan : l'équilibre et (iv)/(v) sont des faits nouveaux et démontrés. Ils ne suffisent pas encore à conclure.

## 9. D'où vient l'équilibre, et ce que la littérature dit du cas C2 (DÉRIVÉ ; lecture)

**Principe d'extension.** Soit U un ensemble quelconque de sommets de Γ et W son complémentaire. Comme A² = 12I − A + 2J, on a
B_{UW} B_{UW}ᵀ = 12I − A_UU − A_UU² + 2J. Si w ⊥ 𝟏_U est vecteur propre de A_UU de valeur α, alors
‖B_{UW}ᵀ w‖² = (3 − α)(4 + α)‖w‖².

**Tout vecteur propre ⊥ 𝟏 d'un sous-graphe induit, de valeur 3 ou −4, se prolonge par zéro en vecteur propre de Γ.** Chaque sommet
extérieur voit alors une somme pondérée nulle.

Le lemme d'équilibre (§8) en est le cas U = N(ℓ), qui est 3-régulier : ses composantes portent la valeur propre 3.
- Cette coïncidence est **propre à k = 14**. Le degré interne de N(ℓ) vaut 3 pour tout m, mais 3 n'est valeur propre de Γ qu'à m = 7.
- Pour BvLS (m = 11), la variance vaut 0,24·|C|… > 0 : il n'y a pas d'équilibre. La vérification de BvLS ne s'applique donc pas à ce
  lemme.
- C'est une rigidité du même ordre que « les grilles sont des codes parfaits » (m ∈ {2, 7}, note 04).

Portée : parmi les 2 903 types (μ, τ), **233** ont plusieurs composantes, et le lemme n'agit que sur eux :
- (4, 8) : 168 types ;
- (6, 6) : 55 ;
- (4, 4, 4) : 10.

Les **2 670** autres sont à composante unique, et l'équilibre y est vide.

**Condition (N, F) exacte** (DÉRIVÉ, non exploitée). A_F Bᵀ = −Bᵀ(I + A_NN) + 2J donne, pour tout lointain z et tout u ∈ N(ℓ) :
|N_F(z) ∩ S_u| = 2 − [z ∼ u] − #{u′ ∈ N_{N(ℓ)}(u) : z ∼ u′}, où S_u désigne les lointains voisins de u. Le profil N(ℓ) des 8
voisins lointains de z est donc imposé par les seules données locales. C'est une somme de 8 profils à trouver, pour chaque z.

**Littérature** (lecture du 25/09, 01 h 40).
- Cesarz–Woldar (Algebraic Combinatorics, arXiv 2308.02978) : si 2 divise |Aut|, alors |Aut| divise 6. Pas d'élément d'ordre 14.
  Leur lemme 3.2 est exactement notre cadre (t = (iL iR), point fixe unique x), mais sans t isolé.
- « No involutions in the missing Moore graph » (arXiv 2606.29183) : l'identité trace–rang d'Ishida, appliquée à p = 2, élimine
  l'involution à étoile K₁,₅₅ fixe. Pour C2, le sous-graphe fixe est {x} et l'identité est vide. Je l'ai vérifié aussi sur le graphe
  des arêtes et sur celui des non-arêtes : elle s'y réduit à Burnside mod 2, déjà cohérent (note 20).
- arXiv 2608.11211 : bornes heuristiques, aucune structure de droites.

Aucun de ces travaux ne traite le cas C2.
