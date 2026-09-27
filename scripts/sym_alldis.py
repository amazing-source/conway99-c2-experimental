"""Family (B) of the finish line (note 46): the ALL-DIS configuration, by the orbit LP REDUCED BY SYMMETRY (C1 + C2, 27/09).

Model: orbit_colmodel_U with every pair of type 'dd' (both orbits dis; 7 free stars). Its rows (one, S, C, I, cut) depend only on
pairs, sister relations and blocks. So the LP is invariant under G = S7 (blocks) x Z2^21 (the two orbits of any pair swapped
independently), which is transitive on the 42 orbits.
- The feasible set is convex and G-invariant. So feasible <=> it has a G-invariant solution x, with x_{g Z, q o g^-1} = x_{Z,q}.
- For such x and any row r: r(x) = sum_{q0 in cols(Z0)} x_{Z0,q0} A_r(q0), with A_r(q0) = sum_Z coef_r(Z, q0 o g_Z^-1), for ANY
  choice of g_Z mapping Z0 to Z. All rows in a G-orbit have the same value, so one representative per row orbit suffices.
- The REDUCED system (x_{Z0} >= 0, sum = 1, the representative rows) is satisfied by x_{Z0} of every invariant solution.
  Hence REDUCED INFEASIBLE => the all-dis family (B) is empty.
- Farkas certificate for the reduced system: integers u (per equality row), v >= 0 (per cut row) such that
  max_q [u.A_eq(q) - v.A_cut(q)] < u.b_eq - v.b_cut.  It is checked exactly over ALL columns of Z0.
Row orbits under G:
- S: one orbit.
- C and I: by the relation of the two orbits (diag, sister, share a block, disjoint).
- cut[c,S], S in the free set at c (12 orbits of the 6 pairs at c): by (n1, n2), the number of pairs at c with one or with both
  orbits in S.
Usage: python sym_alldis.py            output: logs/sym_alldis.out, certificate logs/orbit_certs/sym_alldis.json"""
import sys, os, json, time, itertools
from collections import defaultdict
import numpy as np, highspy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import orbit_colmodel_U as OU
from orbit_colmodel import cycle_union_sizes
N = 7; INF = highspy.kHighsInf
PAIRS = [(a, b) for a in range(N) for b in range(a + 1, N)]
PIDX = {p: t for t, p in enumerate(PAIRS)}
ORB = [(a, b, s) for (a, b) in PAIRS for s in (0, 1)]                  # model orbit index = 2*pair index + s
OIDX = {o: t for t, o in enumerate(ORB)}


def z0_columns():
    """columns of orbit 0 (pair {0,1}, s = 0) of the all-'dd' unified model, built by the model's own dis-column code"""
    pt = {(a, b): ('dd',) for (a, b) in PAIRS}
    g = object.__new__(OU.OrbitModelU)
    g.use_I = True; g.T = []; g.otype = []; g.forbid = set(); g.colfilter = {}
    for (a, b) in PAIRS:
        for s in (0, 1): g.T.append((a, b, None)); g.otype.append(('dis',))
    g.n = 42; g.pair = [frozenset(t[:2]) for t in g.T]; g.orbs_of = defaultdict(list)
    for s in range(42): g.orbs_of[g.pair[s]].append(s)
    g.sis = [next(u for u in g.orbs_of[g.pair[s]] if u != s) for s in range(42)]
    g.free = {c: [s for s in range(42) if c in g.pair[s]] for c in range(N)}
    g.sibpairs = []
    # the model's dis-column code (orbit_colmodel_U.build_columns, 'dis' branch), run for Z = 0 only
    Z = 0; a, b, _ = g.T[Z]; i, j = a, b; Zs = g.sis[Z]; fb = [t for t in range(N) if t not in (i, j)]; mats = []
    other = lambda F, blk: next(iter(g.pair[F] - {blk}))
    loops = (0, 1) if g.otype[Zs] == ('dis',) else (0,)
    for Dz in range(g.n):
        if g.otype[Dz] != ('dis',) or (g.pair[Dz] & g.pair[Z]): continue
        R = g.pair[Dz]; k, l = tuple(R)
        ci = [F for F in g.free[i] if F not in (Z, Zs) and j not in g.pair[F]]
        cj = [F for F in g.free[j] if F not in (Z, Zs) and i not in g.pair[F]]
        for loop in loops:
            ni = 2 - loop
            for Fi in itertools.combinations(ci, ni):
                ri = [other(F, i) for F in Fi]
                if ni == 2 and (ri[0] == ri[1] and ri[0] in (k, l)): continue
                for Fj in itertools.combinations(cj, ni):
                    rj = [other(F, j) for F in Fj]
                    if ni == 2 and (rj[0] == rj[1] and rj[0] in (k, l)): continue
                    nv = defaultdict(int)
                    for r in ri + rj: nv[r] += 1
                    deg = {t: 4 - nv[t] for t in fb}
                    if min(deg.values()) < 0: continue
                    prs, sols = OU.far_sols_dis(fb, deg, R)
                    if not sols: continue
                    base = np.zeros(42, dtype=np.int8)
                    for F in Fi + Fj: base[F] += 1
                    if loop: base[Zs] += 1
                    mats += g._expand(base, prs, sols, Dpair=R, Dz=Dz)
    return g, np.concatenate(mats)


def g_to(Z):
    """an element of G (as a permutation of the 42 orbits) mapping orbit 0 to Z: a block permutation sending {0,1} to Z's pair,
    then a sister swap on that pair if needed"""
    a, b, s = ORB[Z]
    pi = [a, b] + [t for t in range(N) if t not in (a, b)]              # block 0 -> a, 1 -> b
    perm = []
    for (x, y, t) in ORB:
        u, v = sorted((pi[x], pi[y])); t2 = t ^ (s if {u, v} == {a, b} else 0)
        perm.append(OIDX[(u, v, t2)])
    assert perm[0] == Z
    return perm


def reduced_rows():
    """EXACT reduction: for each G-orbit (class) K of rows, the SUM of its rows, expressed on the columns q0 of Z0 as
    A_K(q0) = lin_K . q0 + q0^T quad_K q0 (with the chosen g_Z; summing over the whole class makes it independent of the choices,
    i.e. H-invariant), right-hand side |K| * b.  For a G-invariant x every row of K has the same value, so the summed row is
    equivalent to each row of K: the reduced system is feasible <=> the full LP has an invariant solution <=> the full LP is feasible."""
    ginv = []
    for Z in range(42):
        p = g_to(Z); inv = [0] * 42
        for o in range(42): inv[p[o]] = o
        ginv.append(inv)
    pairof = lambda o: PAIRS[o // 2]
    rel = lambda a, b: 'diag' if a == b else ('sister' if pairof(a) == pairof(b) else ('share' if set(pairof(a)) & set(pairof(b)) else 'disjoint'))
    Sh = lambda a, b: 2 if pairof(a) == pairof(b) else len(set(pairof(a)) & set(pairof(b)))
    classes = {}                                                        # key -> [kind, rhs_sum, lin(42), quad(42x42), size]
    def get(key, kind):
        if key not in classes: classes[key] = [kind, 0, np.zeros(42, dtype=np.int64), np.zeros((42, 42), dtype=np.int64), 0]
        return classes[key]
    for W in range(42):                                                 # S rows
        K = get(('S',), 'eq'); K[1] += 12; K[4] += 1
        for Z in range(42): K[2][ginv[Z][W]] += 1
    for a in range(42):
        for b in range(a, 42):
            r = rel(a, b)
            if a != b:                                                  # C rows
                K = get(('C', r), 'eq'); K[4] += 1
                K[2][ginv[a][b]] += 1; K[2][ginv[b][a]] -= 1
            K = get(('I', r), 'eq'); K[4] += 1; K[1] += 2 * (12 * (a == b) + 4 - Sh(a, b))
            for Z in range(42): K[3][ginv[Z][a], ginv[Z][b]] += 2
            if a != b: K[2][ginv[a][b]] += 1; K[2][ginv[b][a]] += 1
    bad = cycle_union_sizes(12)
    for c in range(N):                                                  # cut rows, every block, classified by (n1, n2)
        F = [o for o in range(42) if c in pairof(o)]
        for size in range(3, 12):
            if size in bad: continue
            for S in itertools.combinations(F, size):
                cnt = defaultdict(int)
                for o in S: cnt[o // 2] += 1
                n2 = sum(1 for v in cnt.values() if v == 2); n1 = size - 2 * n2
                K = get(('cut', n1, n2), 'le'); K[4] += 1; K[1] += 2 * (size - 1)
                for Z in S:
                    for Wo in S:
                        if Wo != Z: K[2][ginv[Z][Wo]] += 1
    rows = [(('one',), 'eq', 1, lambda Q: np.ones(len(Q), dtype=np.int64))]
    for key in sorted(classes, key=str):
        kind, rhs, lin, quad, size = classes[key]
        qs = quad + quad.T; qs = np.triu(qs) - np.diag(np.diag(quad))   # symmetric form q^T quad q = sum_{u<=v} w_uv q_u q_v
        nzq = [(u, v, int(qs[u, v])) for u in range(42) for v in range(u, 42) if qs[u, v]]
        def f(Q, lin=lin, nzq=nzq):
            Qi = Q.astype(np.int64); val = Qi @ lin
            for u, v, w in nzq: val = val + w * Qi[:, u] * Qi[:, v]
            return val
        rows.append(((key[0],) + tuple(key[1:]) + (size,), kind, int(rhs), f))
    return rows


def solve(Q, rows, chunk=400000, init=20000, tl=3600):
    """phase-1 LP by column generation: min sum of artificials s.t. sum_q A_r(q) x_q (+/- art) = / <= b_r, x >= 0"""
    m = len(rows); b = np.array([r[2] for r in rows], dtype=float); kinds = [r[1] for r in rows]
    h = highspy.Highs(); h.setOptionValue('output_flag', False); h.setOptionValue('threads', 1)
    lo = np.array([b[i] if kinds[i] == 'eq' else -INF for i in range(m)]); hi = b.copy()
    for i in range(m): h.addRow(lo[i], hi[i], 0, np.array([], dtype=np.int32), np.array([], dtype=float))
    for i in range(m):                                                  # artificials: +e_i and -e_i (cost 1)
        h.addCol(1.0, 0.0, INF, 1, np.array([i], dtype=np.int32), np.array([1.0]))
        h.addCol(1.0, 0.0, INF, 1, np.array([i], dtype=np.int32), np.array([-1.0]))
    rng = np.random.default_rng(0); inset = set()
    def add_cols(idx):
        for q in idx:
            q = int(q)
            if q in inset: continue
            inset.add(q); col = np.array([f(Q[q:q + 1])[0] if callable(f) else f for (_, _, _, f) in rows], dtype=float)
            nz = np.nonzero(col)[0]
            h.addCol(0.0, 0.0, INF, len(nz), nz.astype(np.int32), col[nz])
    add_cols(rng.choice(len(Q), size=min(init, len(Q)), replace=False))
    t0 = time.time(); it = 0
    while True:
        h.run(); it += 1
        obj = h.getInfo().objective_function_value; y = np.array(h.getSolution().row_dual)
        best = []
        for s in range(0, len(Q), chunk):
            Qc = Q[s:s + chunk]; red = -sum(y[i] * rows[i][3](Qc) for i in range(m))          # reduced cost of x_q (cost 0)
            k = np.argsort(red)[:200]; best += [(red[j], s + j) for j in k if red[j] < -1e-9]
        print("  it %d: phase-1 obj %.6g, %d candidate columns, %d in LP, %.0fs" % (it, obj, len(best), len(inset), time.time() - t0), flush=True)
        if not best or obj < 1e-9 or time.time() - t0 > tl: return obj, y, it
        best.sort(); add_cols([q for _, q in best[:500]])


def certify(Q, rows, y, dens=(10 ** 6, 10 ** 9, 10 ** 12)):
    """exact Farkas check over ALL columns: u = round(y * den) (cut rows: v = -u must be >= 0)"""
    for den in dens:
        u = [int(round(v * den)) for v in y]
        if any(rows[i][1] == 'le' and u[i] > 0 for i in range(len(rows))): u = [min(0, ui) if rows[i][1] == 'le' else ui for i, ui in enumerate(u)]
        rhs = sum(u[i] * rows[i][2] for i in range(len(rows)))
        mx = None
        for s in range(0, len(Q), 400000):
            Qc = Q[s:s + 400000]; val = sum(u[i] * rows[i][3](Qc) for i in range(len(rows)))
            m = int(val.max()); mx = m if mx is None else max(mx, m)
        if mx < rhs: return {"den": den, "u": u, "max_col": mx, "rhs": rhs}
    return None


if __name__ == "__main__":
    t0 = time.time(); g, Q = z0_columns()
    print("Z0 = orbit 0 (pair {0,1}): %d columns, built %.0fs" % (len(Q), time.time() - t0), flush=True)
    assert (Q.sum(axis=1) == 12).all()
    rows = reduced_rows()
    print("reduced rows: %d  (%s)" % (len(rows), ", ".join(str(r[0][:2]) for r in rows[:6]) + ", ..."), flush=True)
    obj, y, it = solve(Q, rows)
    rec = {"columns": len(Q), "rows": [str(r[0]) for r in rows], "phase1_obj": obj, "iterations": it, "secs": round(time.time() - t0)}
    if obj > 1e-6:
        c = certify(Q, rows, y); rec["status"] = "INFEASIBLE (certified)" if c else "infeasible (certificate rounding failed)"
        if c: json.dump({"model": "sym_alldis", "rows": rec["rows"], **c}, open("logs/orbit_certs/sym_alldis.json", "w"))
    else: rec["status"] = "FEASIBLE (invariant LP solution exists)"
    json.dump(rec, open("logs/root/sym_alldis.json", "w"))
    print("SYM ALL-DIS: %s  columns %d  %ds" % (rec["status"], len(Q), rec["secs"]), flush=True)
