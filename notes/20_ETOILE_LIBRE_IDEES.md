# 20 — Le lemme de l'étoile libre, et le registre des idées (24/09/2026, soir)

## 0. La réduction (DÉRIVÉ, à partir des notes 18–19)

**Étoile libre.** On dit qu'un bloc c est *libre* si aucune paire sœur ne le contient, c'est-à-dire si aucune grille par x ne
contient la droite {x, e_c, −e_c}.

**Réduction.** Si C2 existe, Σ est l'un des 10 survivants (`data/survivors_after19.txt`), et chacun a au moins un bloc libre.
Réciproquement, si aucun bloc n'était libre :
- Σ serait sans sommet isolé ;
- par le lemme des étoiles, Σ est de degré ≤ 2 ;
- par la classification, Σ a au plus 4 arêtes.

Couvrir 7 sommets avec au plus 4 arêtes et un degré ≤ 2 force Σ = K₂ + K₂ + P₃, exclu par DRAT.

> **Lemme de l'étoile libre (conjecture) ⇒ C2 n'existe pas.**
>
> Énoncés précis (ajoutés à la revue du 24/09, soir) :
> - **forme globale** (CONJECTURE) : dans toute configuration C2, chaque bloc appartient à une paire sœur. Compte tenu des certificats,
>   elle **équivaut** à « C2 n'existe pas » : elle ne réduit rien par elle-même ;
> - **forme locale** (CONJECTURE, strictement plus forte) : RSF(star(c)) avec c libre (aucune paire {c, m} sœur) est UNSAT. C'est elle
>   que testent les cubes et la formulation compacte du §3 ; à ce jour, aucun indice ni pour ni contre.

Les deux contrôles réels de la famille, Paley(9) à m = 2 et BvLS à m = 11, n'ont aucun bloc libre : toutes leurs paires sont sœurs. La
conjecture leur est donc compatible — mais cette compatibilité est **vide** : à m = 7, deg Σ ≤ 2, alors que BvLS a deg Σ = 10.

**Test direct en cours.** On prend RSF(star(1)), c'est-à-dire le modèle complet sur les 12 lignes de l'étoile du bloc 1, sans aucune
paire sœur. On le découpe de façon exhaustive, à symétrie S₆ × (Z₂)⁶ près, selon le couplage A_1 de N(e_1). Cela donne 11 cubes, un
par partition de 6 en longueurs de cycles (`scripts/make_freestar_cubes.py`, `scripts/cert_freestar_cubes1.sh`, kissat 900 s + DRAT).

## 1. Correction d'une erreur ancienne (CALCULÉ, contrôle BvLS)

La note 08 affirmait « aucun prisme σ-invariant ⇒ n₃ ≡ 0 (mod 6) ». C'est **faux**.
- Les prismes σ-invariants sont les {±e_c, ±a, ±b}, où {a,b} est une arête D interne à star(c). Il y en a 2 n_sib + n_one.
- BvLS en a 110, c'est-à-dire 2·55 (`scripts/burnside_prisms_bvls.py`).
- La bonne relation est **n₃/3 ≡ n_one (mod 2)**. Les 2K₃ et les hexagones (Burnside mod 2) redonnent exactement la même relation :
  c'est cohérent, sans contradiction.

## 2. Registre des idées (méthode « beaucoup d'idées, test bon marché, statut consigné »)

| # | Idée | Test | Statut |
|---|---|---|---|
| 1 | Relaxation de parité F₂ du modèle complet : A² = A sur F₂ (projecteur sur un code de dimension 54) | CryptoMiniSat : m=2 SAT, m=3 SAT, m=7 TIMEOUT 600 s | trop faible seule |
| 2 | Burnside mod 2 sur les sous-graphes d'ordre 6 (Reimbayev) | prismes, 2K₃, C₆, N3 | cohérent (n₃/3 ≡ n_one), aucune contradiction |
| 3 | Parité du nombre de grilles N ≡ n_sib, et g − (N/11)𝟏 ∈ V₃ | calcul | cohérent — **tautologique** (c'est G1 sommé, note 04 l. 32–35) : ne pouvait rien donner |
| 4 | Cohomologie de Tate de t sur le code C = im A | calcul | C libre comme F₂[C₂]-module, cohérent |
| 5 | Lemme de l'étoile libre (réduction §0) | 11 cubes RSF, kissat 900 s | A411, A2211, A42 : UNKNOWN (10–11 M conflits) ; A111111, A33, A21111 arrêtés par le garde-mémoire ; les 5 autres pas lancés (file arrêtée, §4) |
| 6 | Chasse de parité dans un cube, à l'étage Q (comme pour K₁,₃) | `freestar_cube_parity.py`, A111111 | aucune solution Q trouvée en 10 min : non concluant |
| 7 | **Formulation compacte** du problème local (§3) | validation BvLS, énumération des types (μ, τ) | **DÉRIVÉ**, validée sur BvLS ; 2 903 types (μ, τ) à symétrie près |
| 8 | Relaxation LP / MILP de la formulation compacte (niveau orbites lointaines) | `freestar_lp.py`, A111111 τ#0 | LP faisable (2 s) ; MILP 180 s : limite atteinte |
| 9 | CP-SAT 1 fil, cadical sur la formulation compacte | A111111 τ#0 | CP-SAT 300 s UNKNOWN ; cadical > 10 min sans réponse |
| 10 | Recherche locale (recuit) | `freestar_anneal.py` | **inutilisable** : échoue aussi sur des instances à solution plantée |
| 11 | Même problème local pour m = 3…6 (paramètres srg non entiers) | `freestar_family.py` | m = 3, 4, 5 : tous les types UNSAT (comptages impossibles, sans rapport avec l'étoile libre) ; m = 6 : un type UNKNOWN à 60 s. La difficulté n'est pas propre à m = 7 |
| 12 | Calibration : cibles plantées à m = 7 (une solution existe) | `freestar_planted.py` | cadical trouve 2 solutions sur 3 (11 s, 71 s), la 3e > 120 s. Un UNKNOWN de 10 min ne prouve donc rien |

## 3. Formulation compacte du problème local (DÉRIVÉ ; validée sur BvLS m = 11)

**Antériorité (revue du 24/09).** Cette formulation précise la « formulation universelle » d'IDEES I-33 (l. 223–227) et la note 19
(l. 349–353). **Portée de la validation** : correction vérifiée sur BvLS seulement (μ = τ = σ) ; aucune instance à bloc libre n'a été
confrontée au CNF RSF. La complétude (i)–(iii) ⇔ RSF(star(1)) a été revérifiée à la main par un relecteur indépendant.

**Données.** X est l'ensemble des 12 vecteurs signés ±e_m, m = 2…7, et σ(b) = −b. Les lignes de star(1) sont les 24 racines ±e_1 + b.
Le modèle RSF(star(1)) équivaut exactement aux trois données suivantes :
- μ, couplage parfait de X : μ(b) = b′ ⟺ e_1+b ~ e_1+b′. C'est le couplage A_1, les bits a internes à star(1).
- τ, couplage parfait de X : τ(b) = d ⟺ e_1+b ~ −(e_1+d). Ce sont les bits b internes à star(1). τ n'a pas de point fixe, car u ≁ −u.
- Φ : pour chaque racine lointaine z (sans le bloc 1, il y en a 60), Φ(z) = {b ∈ X : e_1+b ~ z}.

**Contraintes.**
- (i) Φ est une bijection des 60 racines lointaines sur les 60 paires de X qui ne sont pas des paires de μ.
- (ii) Pour a ≠ b : #{z : a ∈ z, b ∈ Φ(z)} = 2 − [b = σa] − [b = μa] − [b = τσa]. Pour a = b, la valeur est 1 − [τa = σa].
- (iii) #{z : b ∈ Φ(z), d ∈ Φ(−z)} = 2 − [d = σb] − [d = τμb] − [d = μτb] − [d = τb].
- La paire {1, m} est sœur ⟺ μ(b) = τ(b) = σ(b) pour b = ±e_m. Le partenaire D de l'orbite de e_1+b est interne à star(1) ⟺ μ(b) = τ(b).
- Étoile libre : aucun b tel que μ(b) = τ(b) = σ(b).

**Dérivation.** On regarde la droite ℓ_1 = {x, e_1, −e_1}. Son voisinage N(ℓ_1) se répartit en trois classes de 12 : N(x)∖ℓ_1, P_{e_1} et P_{−e_1}.
- Chaque classe porte un couplage interne. Sur N(x)∖ℓ_1, ce couplage **est σ** ; c'est ce qui est propre au point fixe.
- Les 60 sommets lointains ont chacun exactement 2 voisins dans chaque classe.
- Les conditions λ = 1 et μ = 2 entre sommets de N(ℓ_1) donnent (i), (ii) et (iii). (x−) et (−−) s'en déduisent par σ, et la condition D est la diagonale de (iii).

Contrôle BvLS (m = 11, |X| = 20, 180 racines lointaines, μ = τ = σ) : (i), (ii) et (iii) sont vérifiées exactement
(`freestar_compact.py validate`).

**Identité linéaire (DÉRIVÉ de (ii)).** Dans ℝ⁶, pour tout a ∈ X : Σ_{z ∋ a} Φ(z) = −μ(a) − τ(σa).
- Si μ = σ (cube A111111), on a ⟨Φ(z), z⟩ ≥ 0 pour tout z.
- Toujours si μ = σ, les 10 images Φ(z), z ∋ a, forment un chemin de a à τ(σa) plus des cycles, sur X∖{σa}.

**Types (μ, τ) à symétrie B₆ près** (étoile libre, plus la condition locale « non (τμb = σb et μτb = σb) ») :

| cube | A6 | A51 | A42 | A411 | A33 | A321 | A3111 | A222 | A2211 | A21111 | A111111 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| \|Stab(μ)\| | 12 | 20 | 32 | 64 | 72 | 48 | 288 | 384 | 256 | 1 536 | 46 080 |
| types τ | 1 000 | 508 | 471 | 203 | 215 | 253 | 53 | 89 | 85 | 22 | 4 |

Pour A111111, les 4 types sont les types de cycles de τ/σ sans boucle : (6), (4,2), (3,3), (2,2,2).

## 4. Bilan du 24/09 au soir, et ce que valent les solveurs ici

- Aucune méthode générique n'a tranché le problème local : kissat sur RSF, cadical, CP-SAT, MILP, recuit. La calibration (idée 12)
  montre que **UNKNOWN ne dit rien** sur ce problème : même avec une solution plantée, cadical en manque une sur trois à 120 s.
- Ce qui reste solide : les faits UNSAT **avec certificat DRAT vérifié** sur des encodages validés (lemme des étoiles, survivants
  éliminés).
- La file des cubes RSF est arrêtée : 900 s par cube ne suffisent pas, et continuer coûterait des heures de calcul sans information.
- Suite : chercher un argument **à la main** sur la formulation compacte, en commençant par A111111 (4 types). Pour μ = σ, la
  structure « chemin + cycles » de chaque Φ_a et l'identité linéaire ci-dessus sont les prises les plus directes.
- Garde-mémoire v2 (`scripts/mem_watchdog2.sh`) : il n'arrête les conteneurs que sur une baisse **soutenue**, c'est-à-dire deux lectures
  consécutives sous 3 Go. Kissat n'occupe que 65 Mo ; la machine virtuelle Docker en occupe environ 3 Go.
