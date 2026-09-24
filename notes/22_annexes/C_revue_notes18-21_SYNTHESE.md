# Annexe C — revue des notes 18–21, des ponts B01–B07, de SYNTHESE et REPRISE (relecteur indépendant, 24/09/2026 soir, lecture seule)

Rapport brut du relecteur (en anglais), conservé tel quel. Corrections appliquées : note 22 §3. Échelles P, C : voir l'annexe A.

Checks run (lab .venv, each under 15 s):
- Hashes: all 57 `drat=VERIFIED` lines of `data/cert_results.txt` match their manifest hashes and the CNFs on disk. 11 CNFs are missing from
  disk (g06_*, g08_*, S7b, S7c, K114, g07_bf58…, g07_ca15 full model); every one has a vertex of degree ≥3, so none is needed for the chain.
  No DRAT or LRAT proof file is archived anywhere.
- Counts: "3436 χ_p valides … 1712 signables" (19:205-206) reproduces.
- Type table: all 11 |Stab(μ)| values and τ-type counts of 20:79-82 (total "2 903") reproduce by Burnside counting.
- By hand: (Q1)–(Q4), the χ system, Lemma T, the star lemma, the minus-orbit parity, (i)–(iii) of the compact formulation, the linear
  identity and the Krein values.

## 1. Inventory

| id | idea / result | source | lab status | verdict | P | C | note |
|---|---|---|---|---|---|---|---|
| 18a | Stage-Q (Q1)–(Q4); χ system | 18:19-78 | ÉTABLI (repo) / DÉRIVÉ | OK | 2 | 1 | Re-derived from λ=1, μ=2; monotone relaxation |
| 18b | χ classification 988/56; 11 atoms DRAT; g07_ca15a23af4 closed at stage Q | 18:104-132 | CALCULÉ+DRAT | OK | 1 | 1 | Only atom 01 is still chain-critical |
| 18c | Lemma T: human proof of K₃+K₂ | 18:144-166 | DÉRIVÉ | OK | 2 | 1 | Re-verified |
| 18d | Human proofs of atoms 02–11; "χ à défauts" | 18:176-188 | open | SUPERSEDED | 1 | 2 | Star lemma covers 02–04 and 07–11 |
| 19a | RS≡χ; RSF byte-validated filter; signs kill 8 configs + S6 | 19:28-82 | CALCULÉ | OK | 2 | 1 | RSF ⊂ full CNF underpins every RSF certificate |
| 19b | Signed χ system, D₄ connection, holonomy | 19:84-147 | DÉRIVÉ | OK | 2 | 2 | sdisj not re-derived |
| 19c | Parity certificate non-linear in solver variables | 19:190-194 | CALCULÉ | UNDER-EXPLOITED | 3 | 2 | Explains why K₁,₃ resists solvers; I-33 fix never built |
| 19d | Star lemma: three sister pairs never share a block | 19:224-313 | DÉRIVÉ, ingredients DRAT | OK | 3 | 1 | Proof re-verified; uses only star(c) rows |
| 19e | χ-free parity: K₁,₃ sole atom; (L4) adds K₃+C₄ | 19:215-222 | CALCULÉ | OK | 1 | 1 | Sister-row parity exhausted |
| 19f | C₅, P₆, C₄+K₂ killed (RSF DRAT); n_sib ≤ 4 | 19:149-163, 355-379 | CALCULÉ+DRAT | OK | 2 | 1 | All 29 degree-≤2 graphs re-enumerated |
| 19g | Sister rows exhausted for the 11 survivors | 19:165-168 | CALCULÉ | OK | 2 | 1 | Non-sister rows are needed |
| 19h | Grid-free probes; local type d; mixed stars | 19:315-353 | CALCULÉ | OVERCLAIMED | 2 | 3 | TIMEOUTs uninformative; d=0–4 never reported; mixed stars on 6 rows only |
| 19i | Minus-orbit parity (42 XORs), invisible to stage Q | 19:396-433 | DÉRIVÉ | UNDER-EXPLOITED | 3 | 1 | Breaks stage Q's parasitic (Z₂)²¹ symmetry; never used in a run |
| 19j | Full model on survivors: C₄, P₄+K₂ DRAT | 19:435-451 | CALCULÉ+DRAT | OK | 3 | 4 | P₅, 2P₃ UNKNOWN; survx_K3, survx_P4 UNKNOWN but unreported |
| 19k | DRAT cores point to the free block's star; P₄+K₂+star(3) DRAT | 19:453-469 | CALCULÉ | OK | 2 | 3 | Shape of certificates, not a lemma |
| 19l | L(Q): sign parities linear once Q is fixed | 19:471-482 | CALCULÉ | OVERCLAIMED | 3 | 3 | BvLS only; the I-35 propagator is the real lever |
| 20a | Free-star reduction ⇒ C2 impossible | 20:3-19 | DÉRIVÉ (lemma CONJECTURE) | OK (framing OVERCLAIMED) | 3 | 5 | Globally equivalent to the goal |
| 20b | Prism correction n₃/3 ≡ n_one (mod 2) | 20:25-31 | CALCULÉ | OK | 1 | 1 | Re-derived |
| 20c | 11 RSF cubes of star(1) | 20:21-23, 41 | CALCULÉ | OK (inconclusive) | 2 | 4 | 3 UNKNOWN, 8 never finished |
| 20d | Ideas 1–4, 6, 8–12 | 20:37-48 | tested | OK (closed) | 1 | 3 | Calibration valid |
| 20e | Compact formulation (i)–(iii) of RSF(star(1)) | 20:50-71 | DÉRIVÉ | OK | 4 | 3 | Correct and complete; overlaps I-33 and 19:349-353 |
| 20f | Linear identity; for μ=σ, ⟨Φ(z),z⟩≥0 and path+cycles | 20:73-76 | DÉRIVÉ | OK | 3 | 2 | Sign or parity invariants needed |
| 20g | 2 903 (μ,τ) types up to B₆ | 20:77-84 | CALCULÉ | OK | 2 | 1 | Reproduced exactly |
| 21a | C3 spark; genus transfer closed | 21:6-40 | ÉTABLI (C3) / DÉRIVÉ | OK | 1 | 1 | Consistent with 09–10 and B02 |
| 21b | J1 grids = perfect codes, "jamais utilisé" | 21:56 | untried (claimed) | ERROR | 1 | 1 | Note 04's G1 |
| 21c | J2, J4, J6, J7 | 21:57-62 | untried (claimed) | SUPERSEDED | 2 | 3 | Duplicates I-03, I-11, I-12, I-27 |
| 21d | J3 projections, interlacing, integer Gram | 21:58 | untried (claimed) | DOUBTFUL | 2 | 3 | Partly tried: 04:42-43, N07, psd_gen |
| 21e | J5 "next invariant" of the compact formulation | 21:60 | untried | UNDER-EXPLOITED | 3 | 2 | The only genuinely new J item |
| B01 | Hamming ball in F₃⁷; not a coset graph | B01:14-25 | DÉRIVÉ | OK | 1 | 1 | l.23 stale |
| B04 | Lattices from 3I−S and S+4I; tight frames | B04:10-24 | DÉRIVÉ | OK | 2 | 3 | Case ρ=22 (odd unimodular, dim 22, classified) never examined |
| B05 | Star complements of S (22 / 27 vertices) | B05:13-21 | idea | OK (untested) | 2 | 3 | BvLS test never done |
| B06 | Intriguing sets; G1 | B06:14-24 | RÉUSSI | OK | 1 | 1 | l.15 "exactement pour k = 14" vs 04:15 k∈{4,14} |
| B02/03/07 | van Eijl, Krein, Niemeier bridges | B02, B03, B07 | RÉFUTÉ / HEURISTIQUE | OK | 1 | 4 | Recomputed |
| DOC | SYNTHESE §3; REPRISE | SYNTHESE:31-37; REPRISE:42-48 | — | SUPERSEDED | 1 | 1 | "53 graphes", "12 restants", target lemma (P) |

## 2. Errors, doubts, overclaims (corrections applied: note 22 §3)
1. J1 is not new (21:56, 21:64): G1 of note 04 (Cor. 1 at 04:25 is exactly J1), ingredient of the star lemma; "seulement m = 7"
   contradicts k ∈ {4,14}.
2. Other duplications: J2 = I-03 + note 10 §4; J3 partly tried; J4 = I-11; J6 = I-12 and 00:48; J7 = I-27, 09:80, SYNTHESE:52;
   note 20 §3 restates I-33 (IDEES:223-227) and 19:349-353 without citing; idea 3 (20:39) is 04:32-35.
3. 21:48 "lemme des étoiles (DRAT)": only the 18 ingredients are DRAT; the gluing is by hand.
4. 19:450-451 "dès que Σ a 4 arêtes": contradicted by P₅ and 2P₃ (UNKNOWN at 600 s).
5. Unreported: survx_K3 and survx_P4 UNKNOWN at 600 s (cert_results:60-61); "d = 0 à 4 : en cours" (19:338) never closed.
6. 19:477-482 (L(Q)): 7425 = 8415 − 990 is the left-kernel dimension; "filtre extrêmement fort" and "équivaut presque" are HEURISTIQUE.
7. 19:340 "ne s'étend pas localement": shown only on the 6-row subsystem.
8. 20:3-19: lemma never stated; the global statement is equivalent to "C2 does not exist" given the certificates; only the local form
   has content; the BvLS "compatible" evidence is empty (deg Σ = 10 is impossible at m=7).
9. 18:80-84: table includes S7a, S8, g07_0b2e5dbb0c without full-model DRAT (harmless: vertex of degree ≥3).
10. Stale records: SYNTHESE:36; SYNTHESE:106 date; B01:23; REPRISE:42-43, 47-48, 122, 146.

## 3. Chain check (reviewer)
0. Trust base: the full model encodes C2; its base CNF is identical to the main repository's k14_none.cnf; stage Q follows from it.
1. Stage Q ⇒ χ system: re-derived, correct.
2. Star lemma: re-verified end to end (G1; S1(a) from (Q3); Facts A and B; (−1)³ against +1). Removes every Σ with a vertex of degree ≥3
   (1015 of 1044).
3. The 29 graphs of degree ≤2, all exclusions in monotone "au moins" semantics, each matched to a certificate (atom 01 + Lemma T;
   full-model DRAT; rsf_C5; rsf_P6; rsf_C4K2; surv_C4; surv_P4K2). What remains is exactly the 10 graphs of survivors_after19.txt. ✓
4. Free blocks: every survivor has an isolated vertex; conversely K₂+K₂+P₃ is forced and DRAT-certified. ✓
5. "Free-star lemma ⇒ no C2" is valid, but globally equivalent to the goal.
Verdict: sound, apart from the trust base (step 0) and the non-archived proofs ("VERIFIED" is a log line; re-checking means re-running
kissat, 20–495 s per chain-critical CNF).

Compact formulation (note 20 §3): (i) from λ/μ on (e₁+b, e₁+b′); (ii) from (a, e₁+b); (iii) from (e₁+b, −e₁−d); D condition = diagonal
of (iii); (x−), (−−) by t; pairs with ±e₁ give only μ, τ and |Φ(z)|=2; every constraint on far rows touches far–far variables, so RSF
drops it. Hence exactly RSF(star(1)) with block 1 free: complete. Caveat: validated for soundness only on BvLS (μ=τ=σ).

## 4. Top leads (reviewer)
1. Split (iii) off: it depends on Φ only through the involution ι = Φ∘(−1)∘Φ⁻¹ on the 60 non-μ pairs; solve ι alone for the 4 A111111
   types, then an ι-equivariant Φ for (ii).
2. Find out whether the local lemma is true: structure-aware exact search on A111111 (H_a path+cycles, ⟨Φ(z),z⟩ ≥ 0, Σ|z∩Φ(z)| = 12).
3. Replay the star lemma with the parity made linear: Z-variables, (I)-parity XORs and star(1)'s 12 minus-orbit XORs; validate on K₁,₃
   (should become instant), then A111111 and A6 with Gaussian elimination.
4. Finish the 9 non-empty survivors in exact semantics (cube-and-conquer seeded by the free block's A_c type).
5. Lock the chain: archive LRAT proofs for the ~11 chain-critical certificates; write the star lemma and Lemma T as ÉTABLI; fix REPRISE,
   SYNTHESE, the J list.
