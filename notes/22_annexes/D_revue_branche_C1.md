# Annexe D — lecture de la branche C1 (instantané du dépôt amazing-source/conway99-c1, commit 9f68d8b, 24/09/2026 soir)

**Origine : NON INDÉPENDANTE**, lecture demandée par l'utilisateur (« you can even check c1s repo »). Instantané cloné dans le bloc-notes
de la session, lecture seule : aucun fichier de C1 modifié, aucune commande git sur son dépôt, rien écrit dans sa mémoire.
Rapport brut du relecteur (en anglais), conservé tel quel. P_C1 = potentiel pour C1, P_C2 = potentiel transféré à C2, C = coût.

## 1. C1 in brief
C1 assumes Aut Γ trivial and wants a contradiction from the axioms alone.
- Framing: Γ is H(7,3) "folded" at radius 2. Rooted at x, the only freedom is the transition system τ (matchings τ_a on the 12 other
  labels) plus the "disjoint" edges. Γ must be twisted (τ ≠ mate somewhere). Twisting is measured by W(x) (twisted label–class pairs),
  P (prisms), n₃ = ½Σ|W|, S (pairs E, σ_x(E) that are adjacent).
- Methods: exact rooted models (SAT / unit propagation, validated on Gewirtz "en 1,9 s"); twisted witness geometries (not SRGs);
  positivity (Krein, Gegenbauer, Hodge); p-adic genus arithmetic; Reimbayev subgraph-count identities.
- Results (C1 labels): L1 twisted [P][C]; L2 rank₇(A−3I) odd, L3 7-adic glue non-split [P][?]; L4 k(x) = rank₇(A−3I) − 15, even;
  L7/L8 no Hamming point [calcul exact][à certifier DRAT]; L10 g(x) ≤ 18; L11 twists touch ≥ 4 classes; L12/L13 local rules [P];
  L14 two twisted labels impossible except |C| = 5 (open), three labels 24/128 UNSAT; L15 P = 1386 − ⅙Σ|W|; L16 P ≤ 1151, hence
  Σ|W| ≥ 1410, n₃ ≥ 705 [P]; L17 local 70-space splits at 2, 3, 5 [P][C BvLS]; L18 z₁₁ = 4n₃ − 2S, 0 ≤ S ≤ n₃ [P][C].
- Stuck: every tool penalizes order (grids, prisms), so every result is a lower bound on twisting; a contradiction needs a
  "plafond de torsion" (Σ|W| ≤ 1409), and nothing points that way. No DRAT certificates, no CNF positive control on BvLS.

## 2. Inventory (reviewer's table)

|id|idea|file:line|C1 status|verdict|P_C1|P_C2|C|note|
|--|--|--|--|--|--|--|--|--|
|F1|Line holonomy ρ_ℓ; fixed points = prisms through ℓ|N10:13, N00:66|P→"TUÉE (entrelacement)"|UNDER-EXPLOITED|2|3|2|Same data as C2's star(1)|
|F2/F2′/F20|q=3 rigidity; universal cover; twisting ⇒ excess>0|N10:14,42; N20:23,28|"TUÉE"|OK|1|1|5|as hard as BvLS uniqueness|
|F3|Tight sets × transitions|N10:15|"TUÉE"|OK|1|1|–|–|
|F4|Fano class-coherence of τ|N10:16|"TUÉE (forme locale)"|OK|1|1|4|Fano SAT family never finished|
|F5/F6/F8|Genus/oddity; Arf; ker B lattice|N10:17-20|"SURVIT comme lemme"; "ABSORBÉE"|OK|1|2|1|Became L2–L4|
|F7/F9/F11/F19|T/Δ algebra; quadrangle surface; flat cube complex; Lam-type codes|N10:19-23,41|absorbed/killed|OK|1|1|–|–|
|F10|Partition into 11 grids|N10:22|P; not attacked|UNDER-EXPLOITED|2|1|3|C2 has grid_spread.py|
|F12|σ_x as approximate automorphisms|N10:24|P|UNDER-EXPLOITED|2|2|3|Grew into L18, Z, U_x|
|F13|Terwilliger algebra of a line|N10:25|killed with F1|OK|1|2|2|39-vertex model reusable|
|F14|Krein vanishing|N10:31|"T"|OK|1|1|–|–|
|F15|Hamming point|N10:32|stale labels|OK|1|1|–|Became L8|
|F16|Rigidity ⇒ some σ_x ∈ Aut|N10:33|P|OK|2|1|5|Only route by which killing C2 kills C1|
|F17|Twisting needs a projective plane of order t|N10:34|"P, falsifiable"|ERROR|1|1|4|§4|
|F18|Minimal twisted order n_min(t)|N10:35|P|OK|1|1|3|–|
|F21/F23/F23′|Hodge; Garland confinement; curl₀ avoidance|N10:43-46, N60:29|closed|OK|1|1|–|H0 kills every t≥2|
|F22|Hand rules from propagation refutations|N10:44|"en cours"|UNDER-EXPLOITED|2|3|2|Produced L12|
|L1|Grid-full ⇒ quotient of H(7,3) ⇒ 99∣3⁷|N30:7|[P][C]|OK|1|1|–|–|
|L2/L3|rank₇(A−3I) odd; non-split 7-glue|N30:27,43|[P][?]|OK|1|1|–|C2 has both|
|L4|k(x)=rank₇(A−3I)−15, even|N30:51|[P][C]|UNDER-EXPLOITED|1|2|1|§3a5|
|L5/L6|Tight grids; rooted counting identities|N30:191,194|[P][C]|OK|1|1|–|Same as C2's perfect codes|
|L7|Hamming point never an involution's fixed point|N30:64|exact, to certify|OK|1|1|2|Superseded in C2 by |Σ|≤4|
|L8|No Hamming point|N30:82|exact|DOUBTFUL|1|1|2|§4|
|L9/L10|Local grid-killing rule; g(x)≤18|N30:92-101|exact / P partial|OK|1|1|2|–|
|L11|Twisting confined to 3 classes impossible|N50:21|UNSAT 1,2 s|DOUBTFUL|1|1|2|Never written up|
|L12/R0|Twist propagation rule|N30:104|[P][C]|OK|2|3|1|Proof re-checked; §3a2|
|L13|A class is twisted by 0 or ≥2 labels|N30:125|[P]|OK|1|2|1|–|
|L14|Two twisted labels impossible|N30:136|exact, to certify|OK|2|1|3|∣C∣=5 open|
|L15|P = 1386 − ⅙Σ∣W∣|N30:142|[P]|OK|1|2|–|Underlies n₃/3 ≡ n_one|
|L16|Krein condition on lines: P ≤ 1151|N30:159|[P]|UNDER-EXPLOITED|2|3|3|Re-computed; §3a3|
|L17|70-space splits at 2, 3, 5|N30:170|[P][C BvLS]|OK|1|2|2|–|
|L18|z₁₁ = 4n₃ − 2S|N30:180|[P][C]|UNDER-EXPLOITED|2|3|3|§3a4|
|X1|Twisted witnesses t=2 (20 vertices), t=3 (39, 42)|N20:13-19,111|found|UNDER-EXPLOITED|2|3|1|§3a6|
|X2|Tri-incidence family; t=6 tri-circulant search|N20:99-110|found / "en cours"|OK|1|1|3|–|
|X3|Method validated on Gewirtz (q=2)|N20:144|"RÉUSSIE"|OK|2|2|1|–|
|X4|Reimbayev audit (n₃ identified, sum rule fails)|N60:95-109|done|OK|2|3|2|§3a4|
|X5|Literature (Lou–Murin, BR, Aut results)|N60:110-118|read|DOUBTFUL|1|1|2|Aut claim, §4|
|X6|Twisting = cubic moment of lines; degree ≤3 exhausted|N80:14-20|[P]|OK|1|1|–|–|
|X7|Degree-4 positivity (7–8-point configurations)|N80:72|proposed|UNDER-EXPLOITED|3|2|4|Only stated route to a ceiling|
|X8|Number field, Eisenstein lines, similitude U_x|N80:46-76, N90:100|no contradiction|OK|2|1|4|C2 is the U_x=±7 case|
|X9|Fusion frame; S²=13S+68I; line lattice Λ_L|N70:48-66|[P]; proposed|OK|1|2|3|Re-checked|
|X10|Attempts to strengthen the Krein bound|N70:51-60|"rien de plus"|OK|1|1|–|Don't repeat|
|X11|Twist-carrier identity|N80:78-88|verified|OK|1|2|2|Extra constraint on C2's Φ|
|X12|Reflection matrix Z|N90:57-63|not finished|OK|2|1|3|–|
|X13|Aborted grids; defect operator Δ ⪰ 0 on E₋₄|N90:65-76|[P]|OK|2|2|2|At C2's x, defect = 2·(number of arcs)|
|X14|Local Delsarte on the B₇ label scheme|N90:86-98|"triviale"|OK|1|1|–|Also trivial in C2|
|X15|728 motifs: 700 by propagation, 28 survive|N50:49-53|done|UNDER-EXPLOITED|2|1|2|Hand proofs possible|
|X16|Three-label, 4-class, sources, random-τ, Fano runs|N50:24-38, LAB:30-47|undecided|OK|2|1|4|Needs lab PC|
|X17|Impose one grid at x|LAB:42-46|proposed|UNDER-EXPLOITED|2|3|4|UNSAT ⇒ Σ=∅ in C2|
|X18|Cayley search for twisted graphs|RDM:43|negative for t=2,3|OK|1|1|–|–|
|X19|BvLS CNF positive control; DRAT certificates|LAB:8-28|to do|UNDER-EXPLOITED|3|1|2|C2 pipeline can do it|
|X20|"Plafond de torsion" reformulation|N80:94|conclusion|OVERCLAIMED|2|1|5|§4|
|X21|t=6 coincidences; forced ranks|N00:70-83|[P]|OK|1|1|–|Re-checked|

## 3. Transfers (reviewer)

### (a) C1 → C2
1. C2's free-star data is C1's line holonomy. For ℓ = {x, ±e₁}: C2's μ = C1's τ_{e₁}; C2's τ = σ∘ρ_ℓ. Prisms through ℓ = fixed points of
   ρ_ℓ = #{b : τb = −b} = 12 − t_ℓ(x). Interlacing on C1's 39-vertex line model: "0 violation" in 15 765 valid configurations — do not try
   spectral interlacing on the free star.
2. Twisting digraph at x (i→j when both labels of i twist j): a sister pair is a pair with no arc; R0: out-degree ∈ {0} ∪ [2,6]; L12:
   i→j implies j→i, or some k→j with k ∉ {i,j}. The star lemma becomes "minimum degree ≥ 4"; a free block has degree 6. |Σ| ≤ 4 forces
   |W(x)| ≥ 34, prisms through x = 84 − |W(x)| ≤ 50. Free pre-filter for the 10 survivors and the 11 cubes.
3. Krein on lines (L16) split by t: E₋₄ = V⁺ ⊕ V⁻ (22+22); Σ_{L∌x} e(L,tL) = 252 (confirmed as 84 + 2·84 by counting D-pairs); cubic tensor
   T = T₊₊₊ + T₊₋₋ gives −‖T‖²/3 ≤ X ≤ ‖T‖², X = Σ k_LM² k_{L,tM}, 64‖T‖² = 13860 − 12P; diagonal part (252 + 8P_inv)/16 with
   P_inv = 2n_sib + n_one. About one day to see whether the off-diagonal part reduces to orbit data.
4. Second free variable (L18) and parity: in C2, s(x) = 0, no copy of Z₂ is t-invariant, hence z₂ = S/2 even, S ≡ 0 (mod 4)
   [the reviewer's further claim "z₁₁ ≡ 0 (mod 8)" needs n₃ even; see note 22 §4]. Any 7-vertex count ≡ number of t-invariant copies
   through x (mod 2) — C2's "q:parite". Check Σz_i = C(99,7) before using the 207 rebuilt formulas (C1 found "z₁₇₆ = (1/8)… au lieu de
   (1/84)" and a leftover discrepancy B(k+6)).
5. L4 split by t: rank₇(S−3I) = 7 + k⁻, even side 8 + k⁺, 0 ≤ k^± ≤ 15, k⁺ ≡ k⁻ (mod 2). Parities only.
6. Witnesses: the t=2 graph (20 vertices, |Aut| = 240) and the t=3 graph (42 vertices, |Aut| = 672) have every σ_x as an automorphism and
   P = 0, so every block is free. **The free-star lemma cannot follow from the local axioms plus a point-reflection symmetry; it must use
   excess 0 (C2's constraint (i), Φ bijective).** Use them as controls at m = 3, 4.
7. Don't repeat: Gegenbauer degrees up to 16, flags, line-graph and local Krein on H, Hodge (H0), genus at 2/3/5 (L17), local Delsarte.

### (b) C2 → C1
1. rank₇ parity and D₇(N₃) minus type: already C1's L2/L3 (independent confirmation).
2. Each grid holds 6 prisms and each prism lies in at most one grid, so P ≥ 6N; with L16, N ≤ 191. A lower bound on N would give the lower
   bound on P that C1 lacks (N70:59).
3. Ready-made models: grid_spread.py (C1's F10); grid_offx_phi.py (C1's LAB item 4 bis).
4. D-matching as a new C1 statistic: count the E with N(E)∩N(σ_xE) not a σ_x-pair — candidate third relation between n₃ and S.
5. Infrastructure: C2's DRAT/Docker pipeline for C1's missing BvLS control and certificates; compact bijection encodings (C1's φ-model
   already beat its adjacency model, 34 s vs 201 s).
6. Stage S is the U = ±7 limit of C1's similitude U_x.

## 4. Errors and doubts in C1 (reviewer)
- ERROR N10:34: "t = 55 (Bruck–Ryser) ⇒ 6273 n'existe pas" — 55 ≡ 3 (mod 4), Bruck–Ryser says nothing about order 55.
- DOUBT N60:117: "2 | |Aut| ⟹ |Aut| divise 6 ; 7 | |Aut| ⟹ Aut ≅ Z₇" contradicts RAP:33, N20:155 and the C1/C2/C3 split.
- DOUBT L8 (N30:86): the symmetry-breaking justification "argumentée dans notes/40" is not in N40.
- DOUBT L11: never written up, though cited at N30:122, N50:21, RAP:18.
- DOUBT, all UNSAT lemmas: no BvLS CNF positive control and no DRAT.
- Stale labels: N40:56-58, N20:119 (vs L8); N30:140, N50:35 "en cours" although data/twolabel_dom234 is "UNSAT (1119.7s)" and dom2345
  "UNSAT (2695.1s)"; RDM:27 g(x) ≤ 17 vs N30:92 ≤ 18 (≤ 17 follows from L11 + R0/L12, not written).
- OVERCLAIMED N80:94 (L16 restated); N60:86, N60:121-122 superseded by L16.
- Minor: N90:103 should read BᵀB; N30:93 case g19A (killed by L13, hand proof correct).
- Verified correct: Krein parameters, L16 arithmetic ("46,98" ⇒ 1151), L15, L12/L13 proofs, spectrum of H, rank₂(A) = 54, per-line
  counts, S² = 13S + 68I.
