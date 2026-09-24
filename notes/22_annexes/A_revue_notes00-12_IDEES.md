# Annexe A — revue des notes 00–12 et d'IDEES (relecteur indépendant, 24/09/2026 soir, lecture seule)

Rapport brut du relecteur (en anglais), conservé tel quel. Les corrections qu'il a suscitées sont listées dans la note 22 §3.
Échelles : P = potentiel restant pour tuer C2 ou réduire nettement l'analyse de cas (1–5) ; C = coût de la prochaine étape décisive
(1 = minutes … 5 = semaines).

Checks run by the reviewer (lab .venv, under a second in total), all passed: the Cor.2 spectrum {14, 3⁹, (−4)⁸}, the Gram eigenvalues
350/154/44, det K = 2⁷·3·5⁶, the Wilbrink–Brouwer defects 0/2/8, the Legendre symbols of notes 09–10, χ(X/t) = 869, the n₃ bounds.

## 1. Inventory

| id | idea / result | source | lab status | verdict | P | C | note |
|---|---|---|---|---|---|---|---|
| 00a | Fix(t)={x}, t=σ, D matching; exact model (R,D,I,P) | 00:11-23 | ÉTABLI/DÉRIVÉ | OK | 2 | – | base of every certificate |
| 00b | Spectra, F₂/F₃ ranks, Smith, s=1 structure, c₄=2079 | 00:26-37 | DÉRIVÉ | OK | 1 | – | redundant by design |
| 00c | Generic solvers; Z₈, Kneser 2-lift, 208 order-7 formulas | 00:40-41; 01:7-24 | CALCULÉ | OK | 1 | – | exhausted |
| 00d | "Z₇ jamais étudié"; allsib "non certifié" | 00:31,42; 01:18; 05:3 | SUGGÉRÉ/CALCULÉ | SUPERSEDED | 1 | – | done in notes 09–10; DRAT + human proof |
| 00e | Controls m=2, m=11 mandatory | 00:43-44 | rule | OK | 2 | 1 | both allsib: can't test one/dis or free-block claims |
| 00f | psd_gen at m=7; q:gen/orbit/code; Arf | 00:47-48; 01:13-14 | SUGGÉRÉ | UNDER-EXPLOITED | 2 | 3 | never run |
| 02 | Z⁷/D₇ Hamming chart; (I) ⇔ cover counts; not an H(7,3) quotient | 02:3-24 | DÉRIVÉ | OK | 2 | – | re-checked |
| 03a | Lemma S1: sib pair perfect code ⇔ m∈{2,7}; quotient {5,1,−1,−1} | 03:9-28 | DÉRIVÉ | OK | 3 | – | engine of star lemma |
| 03b | c_p preserves sisters; D₄ holonomy; GQ(2,2) 2-covers; I-13 | 03:34-38; 05; IDEES:121 | DÉRIVÉ | SUPERSEDED | 1 | – | correct; allsib dead |
| 04a | G1: exactly one neighbour in any grid (k∈{4,14}) | 04:13-22 | DÉRIVÉ | OK | 3 | – | lever |
| 04b | Intriguing set; 18-cell partition; grid Gram (≤11 disjoint) | 04:24-31,42-43 | DÉRIVÉ | OK | 2 | 2 | natural cube split for Σ=K₂ |
| 04c | g−(N/11)𝟏∈V₃; N = n_sib + 2Σg′ | 04:32,36 | DÉRIVÉ | OK, tautological | 1 | – | this is G1 summed |
| 04d | Off-x grid ⇒ ±1 eigenvector of S, "support ≤ 9" | 04:37-38 | DÉRIVÉ | DOUBTFUL | 2 | 3 | notation, §2 |
| 04e | Q-G1…Q-G3 | 04:42-45 | open | Q-G3 SUPERSEDED | 2 | 3 | Q-G2 still open |
| 06 | 6 DRAT-certified forbidden Σ; "63 graphes", n_sib ≤ 9 | 06:8-33 | CALCULÉ | OK / SUPERSEDED | 2 | – | K₁,₁,₄ has degree 5 |
| 07 | WB defects: sib 0, one 2, dis 8 | 07:10-24 | DÉRIVÉ | UNDER-EXPLOITED | 4 | 2 | lead 1 |
| 08a | Σc = 6P, c̄ = 4 − 2n₃/2079; n₃<2079 ⇒ grid | 08:8-19 | DÉRIVÉ | OK | 2 | 1 | stronger form unstated: n₃ ≥ 2079−9N |
| 08b | 2n_sib+n_one invariant prisms; n₃/3 ≡ n_one (mod 2) | 08:21-31 | DÉRIVÉ (corrected) | OK | 1 | – | re-derived independently |
| 09a | C3 transfer at p=2: ρ₊+ρ₋ even (+ I-27) | 09:15-25; IDEES:135 | RÉFUTÉ as obstruction | OK | 1 | – | I-27 omits note 10 |
| 09b | "No genus obstruction can kill C2" | 09:27-39; 10:47-53 | DÉRIVÉ heading / HEURISTIQUE | OVERCLAIMED | 1 | 4 | §2 |
| 09c | rank₇(A−3I) odd; D₇(N₃) minus type; form 2A+I−J | 09:42-60 | DÉRIVÉ | OK | 2 | 3 | re-derived; implies ρ ≥ 2 |
| 09d | Theta series of √77·N₃*; isotropic subspaces | 09:79-83 | SPÉCULATION | OK | 2 | 5 | |
| 10a | Twisted Brown invariants; ρ_S, ρ₊, S_out, Q_out 7-ranks even | 10:7-45 | DÉRIVÉ | OK | 1 | – | hold for every integer solution, so never a filter |
| 10b | Stage S alone by CP-SAT | 10:54-55 | en cours | OK | 2 | 3 | no result recorded |
| 11a | R1: off-x grid disjoint from image; involution φ fixes w; label partition | 11:10-40 | DÉRIVÉ | OK | 2 | 2 | re-verified; lead 2 |
| 11b | R2 point-reflection renormalisation | 11:42-55 | CONJECTURE | SUPERSEDED | 1 | – | complete R2 false with sister lines (15.3) |
| 12A | No grid off x; translation triangle; spread; constant g | 12:17-47 | dreams | A.2 stale; A.5 RÉFUTÉ | 2 | 2 | A.3 live (K₃ survives) |
| 12B | Hamming rigidity, curvature, monodromy; Krein, Norton, uniqueness | 12:49-67,108-127 | dreams | κ stale; E.22 trivial | 1 | 4 | compass only |
| 12C | Line code, syzygies, two-graph, inertia, Delsarte, D-graph | 12:69-92 | dreams | C.11 DOUBTFUL | 2 | 2 | C.15 proof correct |
| 12D | Δ = 7 triangles; couplings → translation; n_dis = 0 | 12:94-106 | dreams | UNDER-EXPLOITED | 3 | 3 | lead 5 |
| I-01/17 | Grids at fixed point; grid theory | IDEES:7-31 | EN TEST/SURVIT | labels stale | 2 | – | achieved (DRAT, star lemma) |
| I-18 | Grid propagation E7 | IDEES:33-35 | EN TEST | UNDER-EXPLOITED | 3 | 2 | 6/10 survivors contain P₃ |
| I-19 | Σ\|N(β)∩P_p\| = 32+2s_p | IDEES:48-51 | OUVERTE | OK | 2 | 2 | free block ⇒ s_p ≤ 2 |
| I-02 | F₃ line defects, Aφᵢ ≡ −φᵢ+Δᵢ | IDEES:53-62 | OUVERTE | OK | 2 | 2 | identity checked; untested |
| I-03/04/12 | 7-adic code R_S; star complement; MacWilliams | IDEES:64-81,117 | OUVERTE | partly SUPERSEDED | 2 | 3 | ignores 09–10 |
| I-05 | Harmonics on D₇ roots | IDEES:83-88 | OUVERTE | UNDER-EXPLOITED | 2 | 1 | "test rapide" never run |
| I-06/10/11/14-16 | Transitions, AP, W²=49I, re-rooting, intriguing sets | IDEES:90-133 | OUVERTE | OK | 1 | 3 | |
| I-07/31 | Symmetrised moment relaxations | IDEES:95,193-202 | OUVERTE | OK | 2 | 5 | degree 3 feasible even for allsib |
| I-08/29 | Complex X_Γ; tr H₂ − tr H₁ = 21; χ(X/t)=869 | IDEES:102,165; 12:120 | DÉRIVÉ/OUVERTE | OK | 2 | 2 | L(t)=22 recounted; H₁(BvLS) not computed |
| I-09/20-26 | Z[C₂] object; second round; I-24 fact | IDEES:37-46,108 | ABANDONNÉE | OK | 1 | – | I-24 follows from R1(2) |
| I-28 | Reflection / renormalisation | IDEES:144-163 | AFFAIBLIE | OK | 2 | 3 | |
| I-30 | Hall programme, lemma (P) | IDEES:172-191 | OUVERTE | stale bounds | 2 | 4 | (P) ⇔ death of C2 |
| I-32 | Recollement cocycles | IDEES:204-211 | SURVIT | UNDER-EXPLOITED | 4 | 4 | "cocycle à défauts" = lead 1 |
| I-33 | Connection parity beyond star lemma | IDEES:213-233 | OUVERTE | OK | 4 | 3 | Piste 1 needs note 07 |
| I-34 | Finish survivors with the full model | IDEES:235-243 | OUVERTE | OK | 3 | 3 | lead 3 |
| I-35 | DPLL(T) Gauss propagator on L(Q) | IDEES:245-254 | OUVERTE | OK | 4 | 4 | lead 4 |

## 2. Errors, doubts, overclaims (corrections applied: note 22 §3)

1. Stale bounds on Σ, predating the star lemma: 12:27 "n_sib ≤ 7, donc n₃ ≥ 2016"; 12:56 "κ ≥ 28"; 11:52 "au plus 7 arêtes"; IDEES:180,186;
   06:16 and 06:30-33. With |Σ| ≤ 4: n₃ ≥ 2043 (under "no grid off x"), κ(x) = 84 − 4n_sib − 2n_half ≥ 34, 4n_sib ≤ 16. In general,
   6P ≤ 4·9N + 2(2079 − 9N) gives n₃ ≥ 2079 − 9N.
2. Overclaim at 09:37-39 (under a DÉRIVÉ heading, rests on a heuristic); 10:52-53 covers only the 32 768 forms tested.
3. Tautology at 04:32/04:36 (G1 summed): test #3 of note 20 and dream A.6 could never pay off.
4. Doubtful premise at 12:71: the Smith form of NNᵀ = A+7I does not fix rank₃(N).
5. Notation at 04:38: that lattice is N₃⁻ of note 09 (det 7^{ρ_S}); R₊ defined differently at IDEES:70 and 09:74.
6. Trivial or redundant statements: 12:117; 10:32. Unstated corollary: ρ ≥ 2, hence ρ_S ≥ 8 (with 00:31 and parity).
7. Stale labels: IDEES:8,15; 11:54 ("Résultat ci-dessous" missing); 11:47-53 (no pointer to 15.3).
8. n₃ correction consistent in these files; JOURNAL.md:76 still stated the old claim (corrected by JOURNAL.md:265).

## 3. Top leads (reviewer)
1. Note 07 → S1-type lemmas for one and dis D-squares (I-33 Piste 1, I-32 "cocycle à défauts"). Hand derivation to check, for a one-square
   α=e₁+e₂, β=e₁+e₃: y₂ − x₀ = 2(r_α + r_β) (r_α = neighbours of α among ±e₂±e₃), hence r_α + r_β ≤ 1 and w ∉ {±e₂±e₃}.
2. E7 for the six survivors containing P₃ (P₃, P₄, P₅, 2P₃, K₃, P₃+K₂).
3. I-34 with 04b: survivors in exact semantics; cube K₂ along its 18-cell partition.
4. I-35 parity propagator (Gaussian elimination on partially assigned Q).
5. Programme Δ (12D + note 07): certify bounds on n_one, n_dis with n₃/3 ≡ n_one (mod 2).
