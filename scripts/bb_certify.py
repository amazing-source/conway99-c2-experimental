"""Fast exact branch-and-bound certifier for all-integer models (A, lo, hi, lb, ub): find x integer in [lb, ub] with
lo <= A x <= hi, or prove there is none.  Same certificate format as structures' ad/certify.py (vendored): a tree whose leaves
are Farkas vectors y (one rational per row, U(y) < L(y)) and whose splits are {'var': j, 'le': k, 'lo': T1, 'hi': T2}; every
tree is re-checked with certify.check (exact rationals).  Speed: one persistent HiGHS phase-1 model, simplex warm-started
across nodes (only column bounds change).  Branching: most fractional variable, depth first; env STRONG=k: strong branching over the k most fractional variables.
Usage: python bb_certify.py <npz files...>      env MAXNODES (default 50000)
(.npz as exported by C1: A_data, A_indices, A_indptr, A_shape, lo, hi, lb, ub)"""
import sys, os, json, time
from fractions import Fraction
import numpy as np, scipy.sparse as sp, highspy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor_structures"))
from certify import check, leaf_ok
INF = highspy.kHighsInf


class BB:
    def __init__(self, A, lo, hi, lb, ub):
        self.A = sp.csr_matrix(A); m, n = self.A.shape; self.m, self.n = m, n
        self.lo, self.hi, self.lb0, self.ub0 = lo, hi, lb.astype(float), ub.astype(float)
        h = self.h = highspy.Highs(); h.setOptionValue('output_flag', False); h.setOptionValue('threads', 1)
        h.addVars(n, self.lb0, self.ub0)
        h.addVars(2 * m, np.zeros(2 * m), np.full(2 * m, INF))
        h.changeColsCost(2 * m, np.arange(n, n + 2 * m, dtype=np.int32), np.ones(2 * m))
        Ac = self.A.tocsr()
        for r in range(m):
            s, e = Ac.indptr[r], Ac.indptr[r + 1]
            idx = np.concatenate([Ac.indices[s:e], [n + r, n + m + r]]).astype(np.int32)
            val = np.concatenate([Ac.data[s:e].astype(float), [1.0, -1.0]])
            h.addRow(float(lo[r]), float(hi[r]), len(idx), idx, val)
        self.cur_lb, self.cur_ub = self.lb0.copy(), self.ub0.copy()

    def lp(self, lb, ub):
        ch = np.nonzero((lb != self.cur_lb) | (ub != self.cur_ub))[0]
        if len(ch): self.h.changeColsBounds(len(ch), ch.astype(np.int32), lb[ch], ub[ch])
        self.cur_lb, self.cur_ub = lb.copy(), ub.copy()
        self.h.run()
        if self.h.getModelStatus() != highspy.HighsModelStatus.kOptimal: return None, None, None
        sol = self.h.getSolution()
        return self.h.getInfo().objective_function_value, np.array(sol.row_dual), np.array(sol.col_value[:self.n])

    def cert(self, dual, lb, ub):
        for den in (10 ** 6, 10 ** 9, 10 ** 12):
            for sgn in (1, -1):
                y = [Fraction(int(round(sgn * v * den)), den) for v in dual]
                if leaf_ok(self.A, self.lo, self.hi, lb, ub, y): return {'cert': [str(v) for v in y]}
        return None

    def solve(self, maxnodes):
        stats = {'nodes': 0}

        def rec(lb, ub):
            stats['nodes'] += 1
            if stats['nodes'] > maxnodes: return 'limit'
            if np.any(lb > ub): return {'cert': []}
            obj, dual, x = self.lp(lb, ub)
            if obj is None: return 'lp-error'
            if obj > 1e-7:
                c = self.cert(dual, lb, ub)
                return c if c is not None else 'rounding'
            frac = [(abs(x[j] - round(x[j])), j) for j in range(self.n) if lb[j] < ub[j] and abs(x[j] - round(x[j])) > 1e-6]
            if not frac: return ('integral', x)
            ncand = int(os.environ.get('STRONG', 0))
            if ncand:                                    # strong branching: score both children of the most fractional candidates
                best = None
                for _, jj in sorted(frac, reverse=True)[:ncand]:
                    kk = int(np.floor(x[jj])); objs = []
                    for side in (0, 1):
                        l2, u2 = lb.copy(), ub.copy()
                        if side == 0: u2[jj] = kk
                        else: l2[jj] = kk + 1
                        o, _, _ = self.lp(l2, u2); objs.append(o if o is not None else 0.0)
                    score = (sum(o > 1e-7 for o in objs), min(objs), sum(objs))
                    if best is None or score > best[0]: best = (score, jj, kk)
                    if score[0] == 2: break
                _, j, k = best
            else:
                _, j = max(frac); k = int(np.floor(x[j]))
            out = {'var': int(j), 'le': k}
            ub1 = ub.copy(); ub1[j] = k; lb2 = lb.copy(); lb2[j] = k + 1
            for key, (l_, u_) in (('lo', (lb, ub1)), ('hi', (lb2, ub))):
                sub = rec(l_, u_)
                if not isinstance(sub, dict): return sub
                out[key] = sub
            return out
        sys.setrecursionlimit(100000)
        t = rec(self.lb0.copy(), self.ub0.copy())
        if isinstance(t, dict): return {'status': 'dead', 'nodes': stats['nodes'], 'tree': t}
        if isinstance(t, tuple): return {'status': 'alive', 'nodes': stats['nodes']}
        return {'status': 'unknown', 'why': t, 'nodes': stats['nodes']}


if __name__ == "__main__":
    maxn = int(os.environ.get('MAXNODES', 50000)); out = open("logs/bb_certify.jsonl", "a")
    for f in sys.argv[1:]:
        z = np.load(f); A = sp.csr_matrix((z['A_data'], z['A_indices'], z['A_indptr']), shape=tuple(z['A_shape']))
        t0 = time.time(); B = BB(A, z['lo'], z['hi'], z['lb'], z['ub']); r = B.solve(maxn); t1 = time.time()
        ok = check(A, z['lo'], z['hi'], z['lb'].astype(float), z['ub'].astype(float), r['tree']) if r['status'] == 'dead' else False
        rec = {"file": os.path.basename(f), "status": r['status'], "nodes": r['nodes'], "checked": ok, "why": r.get('why'),
               "solve_s": round(t1 - t0, 1), "check_s": round(time.time() - t1, 1)}
        out.write(json.dumps(dict(rec, tree=r.get('tree'))) + chr(10)); out.flush()
        print(rec); sys.stdout.flush()
