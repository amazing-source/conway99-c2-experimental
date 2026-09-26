"""Experiment (note 43): structures' pair-level LP + OUTER APPROXIMATION of the general balance identity (star), no integrality.
(star) gives, for every block k and set S (k not in S):  h_S(phi) = sum_W delta_W^2 + sum_W eps_W^2 + sum_{o in Lab} (g_o^2 + 3 g_o) - 20 s = 0,
with h_S convex quadratic (delta, eps, g affine in phi).  The convex relaxation h_S <= 0 is imposed by tangent cuts
    h_S(x*) + grad h_S(x*) . (x - x*) <= 0      (valid: h_S convex, and h_S = 0 on every solution).
Loop: LP -> point x* -> add the violated tangent cuts -> repeat, until the LP is infeasible (leaf dead) or no cut is violated.
Usage: python star_cuts_test.py <ci> <job> <leaf indices...>    env SETS = comps | all (default all)"""
import sys, os, time, itertools
import numpy as np, scipy.sparse as sp, highspy
sys.path.insert(0, "scripts"); sys.path.insert(0, "external_structures/ad")
import pair_blockdfs as PB
from general_model import build, pr
N = 7


def star_family(orbs, phi, mode):
    """list of (k, S, terms): terms = list of (weight kind, const, [(var, coef)]) for delta/eps (squared) and g (g^2 + 3g)"""
    n = len(orbs); fam = []
    for k in range(N):
        others = [m for m in range(N) if m != k]
        Ss = [frozenset(S) for r in range(1, 6) for S in itertools.combinations(others, r)]
        for S in Ss:
            s = len(S); sq = []; gl = []
            for W in range(n):
                P = orbs[W]['pair']
                lin = [(phi[(W, pr(k, m))], 1.0) for m in S]
                if k not in P: sq.append((len(set(P) & S) - s, lin))
                elif sum(P) - k in S: gl.append(lin)
                else: sq.append((0, lin))
            fam.append((k, S, sq, gl, s))
    return fam


def h_and_grad(x, sq, gl, s, nvar):
    h = -20.0 * s; grad = {}
    for c0, lin in sq:
        v = c0 + sum(x[j] * a for j, a in lin); h += v * v
        for j, a in lin: grad[j] = grad.get(j, 0.0) + 2 * v * a
    for lin in gl:
        g = sum(x[j] * a for j, a in lin); h += g * g + 3 * g
        for j, a in lin: grad[j] = grad.get(j, 0.0) + (2 * g + 3) * a
    return h, grad


if __name__ == "__main__":
    ci, job = sys.argv[1], int(sys.argv[2]); po = PB.load_job(ci, job); In = {int(x): v for x, v in po["In"].items()}
    for t in map(int, sys.argv[3:]):
        L = [tuple(z) for z in po["leaves"][t]]
        orbs = PB.orbit_list(In, {c: tuple(z for z in L if z[0] == c) for c in range(N) if c != po["A"]})
        A, lo, hi, lb, ub, nvar, phi, ns = build(orbs); A = sp.csr_matrix(A)
        fam = star_family(orbs, phi, os.environ.get('SETS', 'all'))
        h = highspy.Highs(); h.setOptionValue('output_flag', False); h.setOptionValue('threads', 1)
        lp = highspy.HighsLp(); lp.num_col_ = nvar; lp.num_row_ = A.shape[0]
        lp.col_cost_ = np.zeros(nvar); lp.col_lower_ = lb; lp.col_upper_ = ub; lp.row_lower_ = lo; lp.row_upper_ = hi
        Ac = sp.csc_matrix(A); lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
        lp.a_matrix_.start_ = Ac.indptr; lp.a_matrix_.index_ = Ac.indices; lp.a_matrix_.value_ = Ac.data.astype(float)
        h.passModel(lp); t0 = time.time(); it = 0; ncuts = 0; verdict = None
        while it < int(os.environ.get('ITERS', 60)):
            it += 1; h.run(); st = h.getModelStatus()
            if st == highspy.HighsModelStatus.kInfeasible: verdict = 'DEAD (LP + star cuts infeasible)'; break
            if st != highspy.HighsModelStatus.kOptimal: verdict = 'solver status %s' % h.modelStatusToString(st); break
            x = np.array(h.getSolution().col_value); added = 0; worst = 0.0
            for (k, S, sq, gl, s) in fam:
                hv, gr = h_and_grad(x, sq, gl, s, nvar)
                if hv > 1e-6:
                    worst = max(worst, hv)
                    idx = np.array(sorted(gr), dtype=np.int32); val = np.array([gr[j] for j in idx])
                    rhs = -hv + float(val @ x[idx])
                    h.addRow(-highspy.kHighsInf, rhs, len(idx), idx, val); added += 1
            ncuts += added
            if added == 0: verdict = 'ALIVE (no violated star cut)'; break
        print("leaf %d: %s after %d rounds, %d cuts, %.1fs" % (t, verdict or 'iteration cap', it, ncuts, time.time() - t0)); sys.stdout.flush()
