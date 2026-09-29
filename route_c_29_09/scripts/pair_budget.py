"""Per-pair component-budget pre-filter (C2, 28/09 night). Sound: for a fixed (y1, y2), the frame identity summed over each root
component R_i (and on the orthogonal complement of the root span) gives, for the 42 u and 7 h,
    sum_u |P_i u|^2 + sum_h |P_i h|^2 = 7 rank_i - |P_i y1|^2 - |P_i y2|^2        (EXACT, every i, incl. the perp part),
with the u among the norm-3 vectors orthogonal to y1, y2 and the h among the admissible norm-4 vectors orthogonal to y1, y2.
Integer program on types (counts), HiGHS; infeasible => the pair is EXCLUDED before any h-search.
Usage: python pair_budget.py <id> <pairs.json> <n_sample> [seed]"""
import sys, os, json, time, random, numpy as np
from fractions import Fraction as F
from math import lcm
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frame_dfs as FD


def components(R, G):
    n = len(R); P = (R @ G) @ R.T; comp = -np.ones(n, dtype=int); c = 0
    for s0 in range(n):
        if comp[s0] >= 0: continue
        st = [s0]; comp[s0] = c
        while st:
            a = st.pop()
            for b in np.flatnonzero(P[a] != 0):
                if comp[b] < 0: comp[b] = c; st.append(b)
        c += 1
    return comp, c
from scipy.optimize import milp, LinearConstraint, Bounds
LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def setup(lid, L=None):
    if L is None:
        rec = json.load(open(os.path.join(LAB, "external_runs", "structures_3eceb4d", "U", "%s.json" % lid)))
        L = FD.lattice_data(rec["gens"])
    G = L["G"]; R = L["R"]
    comp, k = components(R, G)
    ranks = [int(np.linalg.matrix_rank(R[comp == i].astype(float))) for i in range(k)]
    hs = [F(2 * int((comp == i).sum()), ranks[i]) for i in range(k)]
    Bq = np.array([[F(x) for x in row] for row in L["B"]], dtype=object); Binv = np.linalg.inv(np.array([[float(x) for x in r] for r in L["B"]]))
    return L, G, R, comp, k, ranks, hs, Bq, Binv


def tvec(rows, G, R, comp, k, hs, norm):
    A = rows @ G @ R.T
    out = []
    for row in A:
        t = [F(int((row[comp == i] ** 2).sum()) * 2) / (2 * hs[i]) for i in range(k)]
        out.append(tuple(t + [F(norm) - sum(t)]))
    return out


def pair_test(ctx, y1, y2, ps=None):
    """exact integer program: for every root class (component i, value v = Y(alpha)), sum over the 42 u and 7 h of
    sum_{alpha in class} (alpha, f)^2 = (14 - v) * #class  (frame identity at each root, the y part being known);
    plus the perp-of-root-span budget  sum |P_perp f|^2 = 7 (24 - rank R) - sum_y |P_perp y|^2  (rational)."""
    L, G, R, comp, k, ranks, hs, Bq, Binv = ctx
    Y = np.array([y1, y2])
    if ps is None:
        ps, why = FD.pair_setup(L, y1, y2)
        if ps is None: return "EXCLUDED (%s)" % why
    W, H = ps["W"], ps["H"]
    if len(W) < 42 or len(H) < 7: return "EXCLUDED (too few candidates)"
    YR = (Y @ G @ R.T) ** 2; Yal = YR.sum(axis=0)                      # Y(alpha) per positive root
    if Yal.max() > 6: return "EXCLUDED (a root has Y > 6)"
    keys = sorted(set(zip(comp.tolist(), Yal.tolist())))
    idx = {kk: np.flatnonzero((comp == kk[0]) & (Yal == kk[1])) for kk in keys}
    def types(rows, norm):
        A = (rows @ G @ R.T) ** 2
        cl = np.stack([A[:, idx[kk]].sum(axis=1) for kk in keys], axis=1)          # integers
        tot = A.sum(axis=1) if False else None
        # perp part |P_perp x|^2 = norm - sum_i |P_i x|^2, |P_i x|^2 = (2 * sum_{alpha in R_i^+} (alpha,x)^2) / (2 h_i)
        perp = [F(norm) - sum(F(int(2 * A[r_, comp == i].sum())) / (2 * hs[i]) for i in range(k)) for r_ in range(len(rows))]
        return [tuple(int(x) for x in cl[r_]) + (perp[r_],) for r_ in range(len(rows))]
    Tu = sorted(set(types(W, 3))); Th = sorted(set(types(H, 4)))
    tyv = types(Y, 7)
    need = [(14 - kk[1]) * len(idx[kk]) - 0 for kk in keys]                         # u + h part (y part = Y(alpha) removed)
    perp_need = F(7 * (24 - sum(ranks))) - tyv[0][-1] - tyv[1][-1]
    D = lcm(*[t[-1].denominator for t in Tu + Th] + [perp_need.denominator])
    cols = [("u", t) for t in Tu] + [("h", t) for t in Th]
    m = len(keys)
    A = np.zeros((m + 3, len(cols))); b = np.zeros(m + 3)
    for j, (nm, t) in enumerate(cols):
        A[:m, j] = t[:m]; A[m, j] = int(t[-1] * D); A[m + 1 + (0 if nm == "u" else 1), j] = 1
    b[:m] = need; b[m] = int(perp_need * D); b[m + 1:] = [42, 7]
    r = milp(np.zeros(len(cols)), constraints=LinearConstraint(A, b, b), integrality=np.ones(len(cols)), bounds=Bounds(0, np.inf),
             options={"time_limit": 20})
    return "EXCLUDED (pair budget)" if r.status == 2 else ("feasible" if r.status == 0 else "undecided %d" % r.status)


if __name__ == "__main__":
    lid = "%03d" % int(sys.argv[1]); P = json.load(open(sys.argv[2]))["pairs"]; n = int(sys.argv[3])
    random.seed(int(sys.argv[4]) if len(sys.argv) > 4 else 0)
    ks = random.sample(range(len(P)), min(n, len(P)))
    t0 = time.time(); ctx = setup(lid); ts = time.time() - t0
    cnt = {}; t1 = time.time()
    for kk in ks:
        yy = []
        for c in P[kk]:
            v = np.array([float(F(x)) for x in c]); cf = np.rint(v @ ctx[8]).astype(np.int64); yy.append(cf)
        v_ = pair_test(ctx, yy[0], yy[1]); cnt[v_] = cnt.get(v_, 0) + 1
    print(json.dumps({"id": lid, "sampled": len(ks), "verdicts": cnt, "setup_s": round(ts, 1), "per_pair_s": round((time.time() - t1) / len(ks), 3)}))
