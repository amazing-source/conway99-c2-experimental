"""Orbit-level column model with the TWISTED GRAPH T fixed and everything else variable (note 40): the head of every anchored pair,
all D-structures, free graphs and far rows.  Sigma = empty, one-block squares.
Twisted pair {a,b} (a < b): orbit 0 has pivot a, orbit 1 pivot b (WLOG).  Pair not in T: its two orbits choose a common pivot:
rows piv[R] : (weight of R0's columns with pivot min R) - (weight of R1's columns with pivot min R) = 0.
No cut rows (free sets variable); 'free at j' is enforced by the coupling rows (see orbit_colmodel_all).
Usage: python orbit_colmodel_T.py <edges "01,12,..."> """
import sys, itertools, time, os, json
from collections import defaultdict
import numpy as np
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_gen as OG
N = 7

class OrbitModelT(OG.OrbitModelGen):
    def __init__(self, twE, use_I=True):
        self.use_I = use_I; self.tw = {frozenset(e) for e in twE}
        self.T = []; self.pivopts = []
        for a in range(N):
            for b in range(a + 1, N):
                R = frozenset((a, b))
                for s in (0, 1):
                    self.T.append((a, b, None)); self.pivopts.append([(a, b)[s]] if R in self.tw else [a, b])
        n = self.n = 42
        self.pair = [frozenset(t[:2]) for t in self.T]
        self.orbs_of = defaultdict(list)
        for s in range(n): self.orbs_of[self.pair[s]].append(s)
        self.sis = [next(u for u in self.orbs_of[self.pair[s]] if u != s) for s in range(n)]
        self.Sh = np.array([[2 if self.pair[a] == self.pair[b] else len(self.pair[a] & self.pair[b]) for b in range(n)] for a in range(n)])
        self.forbid = set()
        self.build_columns(); self.free = {c: [] for c in range(N)}; self.build_rows(); self.add_piv_rows()
        if os.environ.get('FDEG'): self.add_fdeg_rows()
        else: self.fdeg = {}

    def build_columns(self):
        self.cols = []; self.cpiv = []
        for Z in range(self.n):
            mats = []; pv = []
            for i in self.pivopts[Z]:
                j = next(iter(self.pair[Z] - {i}))
                # free candidates at j: twisted pair {j,r}: only its orbit with pivot r; other pairs: both orbits
                self.free = {c: [] for c in range(N)}
                self.free[j] = [F for F in range(self.n) if j in self.pair[F] and i not in self.pair[F]
                                and not (self.pair[F] in self.tw and self.pivopts[F] == [j])]
                for k in range(N):
                    if k in (i, j): continue
                    for Dz in self.orbs_of[frozenset((i, k))]:
                        if i not in self.pivopts[Dz]: continue
                        blk = self._cols_for(Z, i, j, k, Dz)
                        mats += blk; pv += [np.full(len(b), i, dtype=np.int8) for b in blk]
            M = np.concatenate(mats); assert (M.sum(axis=1) == 12).all()
            self.cols.append(M); self.cpiv.append(np.concatenate(pv))

    def add_piv_rows(self):
        self.pivrow = {}
        for R, (o0, o1) in self.orbs_of.items():
            if R in self.tw: continue
            r = len(self.rname); name = ('piv', R); self.rows[name] = r
            self.rname.append(name); self.rkind.append('eq'); self.rrhs.append(0); self.pivrow[o0] = (r, 1, min(R)); self.pivrow[o1] = (r, -1, min(R))

    def add_fdeg_rows(self):
        """R_j is 2-regular on the orbits FREE at j: for every orbit F and block j of F,
        #(columns of orbits Z free at j having F as a free neighbour) = 2 * (weight of F's columns with free block j)"""
        self.fdeg = {}
        for F in range(self.n):
            for j in self.pair[F]:
                r = len(self.rname); name = ('fdeg', F, j); self.rows[name] = r; self.fdeg[(F, j)] = r
                self.rname.append(name); self.rkind.append('eq'); self.rrhs.append(0)

    def piv_const(self, y, Z):
        out = 0
        if Z in self.pivrow:
            r, sg, a = self.pivrow[Z]
            out = sg * y[r] * (self.cpiv[Z] == a)
        if self.fdeg:
            M1 = (self.cols[Z] == 1)
            extra = np.zeros(len(self.cols[Z]), dtype=y.dtype)
            for j in self.pair[Z]:
                sel = (self.cpiv[Z] != j)                      # columns whose free block is j
                w = np.zeros(self.n, dtype=y.dtype)
                for F in range(self.n):
                    if j in self.pair[F] and F != Z: w[F] = y[self.fdeg[(F, j)]]
                extra = extra + sel * (M1.astype(y.dtype) @ w - 2 * y[self.fdeg[(Z, j)]])
            out = out + extra
        return out

    def solve(self, tlimit=280, per=3, verbose=True):
        t0 = time.time(); cols = []; keys = set()
        rng = np.random.default_rng(0)
        def ent(Z, t):
            e = self.entries(Z, self.cols[Z][t])
            if Z in self.pivrow and self.cpiv[Z][t] == self.pivrow[Z][2]: e = e + [(self.pivrow[Z][0], self.pivrow[Z][1])]
            if self.fdeg:
                j = next(iter(self.pair[Z] - {int(self.cpiv[Z][t])})); q = self.cols[Z][t]
                e = e + [(self.fdeg[(F, j)], 1) for F in range(self.n) if q[F] == 1 and j in self.pair[F]] + [(self.fdeg[(Z, j)], -2)]
                d = defaultdict(int)
                for r, c in e: d[r] += c
                e = [(r, c) for r, c in d.items() if c]
            return e
        for Z in range(self.n):
            for t in rng.choice(len(self.cols[Z]), size=3, replace=False): keys.add((Z, int(t))); cols.append(ent(Z, int(t)))
        it = 0
        while True:
            it += 1
            h = self.master(cols); obj = h.getInfo().objective_function_value
            y = np.array(h.getSolution().row_dual); added = 0; best = 0.0
            for Z in range(self.n):
                const, lin, Y = self.score_parts(y, Z)
                M = self.cols[Z].astype(np.float64)
                sc = const + M @ lin + np.einsum('ij,ij->i', M @ Y, M) + self.piv_const(y, Z)
                for t in np.argsort(-sc)[:per]:
                    if sc[t] > 1e-7 and (Z, int(t)) not in keys:
                        keys.add((Z, int(t))); cols.append(ent(Z, int(t))); added += 1; best = max(best, sc[t])
            if verbose: print("  iter %d obj %.5f cols %d added %d best %.3g %.0fs" % (it, obj, len(cols), added, best, time.time() - t0)); sys.stdout.flush()
            if added == 0 or time.time() - t0 > tlimit:
                self.done = added == 0; return obj, y

    def verify(self, y, den=10 ** 6):
        yi = np.array([int(round(v * den)) for v in y], dtype=np.int64)
        yb = int(sum(int(yi[r]) * int(self.rrhs[r]) for r in range(len(yi))))
        UB = 0; LB = 0
        for Z in range(self.n):
            const, lin, Y = self.score_parts(yi, Z)
            M = self.cols[Z].astype(np.int64)
            sc = int(const) + M @ lin + np.einsum('ij,ij->i', M @ Y, M) + np.asarray(self.piv_const(yi, Z), dtype=np.int64)
            UB += int(sc.max()); LB += int(sc.min())
        return (yb > UB or yb < LB), (yb / den, LB / den, UB / den)

if __name__ == "__main__":
    twE = [tuple(int(c) for c in e) for e in sys.argv[1].split(",")]
    t0 = time.time(); g = OrbitModelT(twE)
    print("T = %s: columns %d rows %d built %.0fs" % (twE, sum(len(M) for M in g.cols), len(g.rname), time.time() - t0)); sys.stdout.flush()
    obj, y = g.solve(tlimit=float(os.environ.get('TL', 280)), verbose=os.environ.get('V') is not None)
    if g.done and obj > 1e-6:
        ok, b = g.verify(y); print("T: INFEASIBLE (orientation variable), slack %.4f, exact %s %s %.0fs" % (obj, "VALID" if ok else "FAILED", b, time.time() - t0))
    else: print("T: %s obj %.5f %.0fs" % ("FEASIBLE" if g.done else "TIME CAP", obj, time.time() - t0))
