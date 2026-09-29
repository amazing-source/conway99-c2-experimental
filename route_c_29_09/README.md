# Route (C) — C2 state on 29/09/2026, for Astra

## Message
Thank you — it works. Measured on our runs (all proofs re-checked by C2):
* **Characteristic trap** (norm-16 z, (z,y1)^2+(z,y2)^2 <= 66): kills 35–53 % of all ordered pairs, ~1 ms each.
* **Unordered-pair swap rule**: another 30–48 % skipped.
* **Endpoint confinement + 16 boundary points (Y_z = 58)**: search trees 3–8x smaller; a 044 pair stuck ~1 day now dies in 1 s.
* Net: 0.5 s -> ~0.05 s per pair (root-poor 051); only ~9 % of pairs reach a real search. **58/156 lattices excluded** (47 yesterday).

**Still not enough:** 075 had 249k pairs, 074 ~390k; ~50 root-poor envelopes remain (~1.5 days of full CPU). Everything is still
**pair by pair**; engineering is nearly exhausted (shared per-y1 setup is the last x1.5–2). **The only big jump left is a theorem that
kills a whole y1 orbit, or a whole envelope, at once.** Please focus on that.

### Theorem targets
1. **Averaged characteristic trap (y1- or lattice-level).** Pointwise: (z,y1)^2+(z,y2)^2 <= 66 for every norm-16 characteristic z. Over
   the whole shell, theta-series / harmonic identities (as sum_beta (beta,x)^2 = 2h|x|^2 for Niemeier roots) should give
   sum_z (z,y)^2 = c1|y|^2 + c2 E(y) + ..., and degree-4 analogues. With the caps, can one show that **no norm-7 y2 ⊥ y1** survives for a
   given y1 — or exclude an envelope from theta data alone? Weighted variants: only z with (z,y1)^2 = 25 or 49 (forcing (z,y2)^2 <= 41 or 17).
2. **Counting the boundary points.** Every surviving pair has max Y_z = 58 exactly; those z behave like non-y-hit new roots (coverage 1/3,
   1 only if u-hit). An **exact count** of the Y_z = 58 points (shell design identities) against the coverage identities and the
   u-packing (sum_u m(u)) could give a pair-free, y1-level contradiction.
3. **Partner shell after the trap.** For fixed y1, y2 must satisfy (z,y2)^2 <= 66 - (z,y1)^2 for ALL z: finitely many caps. Can a
   quadratic-form / PSD / design argument show the surviving norm-7 vectors ⊥ y1 cannot carry the frame (42 u and 7 h in y2's complement,
   rank-22 lattice N, min N* >= 8/7)?

Any **proven** y1- or lattice-level statement — even only for root-poor envelopes (r <= 112) — beats any further per-pair filter.

## Files
* `56_PROMPT_ASTRA_ROUTE_C_28_09.md` — full brief (setup, proofs, all measurements, what failed), with appended results.
* `scripts/frame_dfs.py` — production search: `char_trap` (FD_CHAR), endpoint confinement folded into the bad-u mask (FD_EC), 16 boundary
  points (FD_BND), symmetry breaking (FD_SYM), Lemma U+. `scripts/hstage_stream.py` — stream consumer with the swap rule.
  `scripts/stream_lattice.py` (driver; Gamma = {I} fallback, still complete), `stream_finish.py`, `finish_gpairs.py` (tracker updates).
* `scripts/footprint_tables.py` — independent re-derivation of the root / norm-3 / norm-4 footprint tables (match yours and 5.6low's).
  `camp1-4.py`, `dfs_fp.py` — the 2-minute campaigns (static/node footprints, node-level trap, EC + boundary points).
* `data/U078_char16_and_gram.npz` — U078: Gram G, basis B (rational strings), all 96,000 norm-16 characteristic vectors z (coefficient rows, one per ±).
* `data/finishC_tracker_29_09.json` — per-envelope status and method.
Anything else on request: partner lists per y1, survivor statistics, shells of other envelopes.
