"""Orbit-level column model with EVERYTHING variable (note 40): orientation (pivot of every orbit), D-structures, free graphs,
far rows.  Sigma = empty, one-block squares only (covers anchored, twisted, all mixtures, H).  No cut rows (the free sets are
variable); consistency of 'free at j' is enforced by the coupling rows: an orbit F with pivot j has, in the pairs {j,.}, only its
partner (q = 2), so q_F(Z) = 1 is impossible and a free neighbour of Z at j is automatically free at j.
Usage: python orbit_colmodel_all.py"""
import sys, itertools, time, os
from collections import defaultdict
import numpy as np
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_gen as OG
N = 7

class OrbitModelAll(OG.OrbitModelGen):
    def __init__(self, use_I=True):
        self.use_I = use_I
        self.T = []
        for a in range(N):
            for b in range(a + 1, N):
                for s in (0, 1): self.T.append((a, b, None))
        n = self.n = 42
        self.pair = [frozenset(t[:2]) for t in self.T]
        self.orbs_of = defaultdict(list)
        for s in range(n): self.orbs_of[self.pair[s]].append(s)
        self.sis = [next(u for u in self.orbs_of[self.pair[s]] if u != s) for s in range(n)]
        self.free = {c: [] for c in range(N)}                      # no cut rows
        self.Sh = np.array([[2 if self.pair[a] == self.pair[b] else len(self.pair[a] & self.pair[b]) for b in range(n)] for a in range(n)])
        self.build_columns(); self.build_rows()

    def build_columns(self):
        self.cols = []
        for Z in range(self.n):
            a, b, _ = self.T[Z]; mats = []
            for i, j in ((a, b), (b, a)):
                self.free[j] = [F for F in range(self.n) if j in self.pair[F] and i not in self.pair[F]]   # candidates only
                for k in range(N):
                    if k in (i, j): continue
                    for Dz in self.orbs_of[frozenset((i, k))]: mats += self._cols_for(Z, i, j, k, Dz)
            self.free = {c: [] for c in range(N)}
            M = np.concatenate(mats); assert (M.sum(axis=1) == 12).all()
            self.cols.append(M)

if __name__ == "__main__":
    t0 = time.time(); g = OrbitModelAll()
    print("ALL-variable model: columns %d rows %d built %.0fs" % (sum(len(M) for M in g.cols), len(g.rname), time.time() - t0)); sys.stdout.flush()
    obj, y = g.solve(tlimit=float(os.environ.get('TL', 280)), verbose=os.environ.get('V') is not None)
    if g.done and obj > 1e-6:
        ok, b = g.verify(y)
        if ok: OM.save_cert(g, y, "logs/orbit_certs/all.json.gz", "all", {}, b)
        print("ALL: INFEASIBLE, slack %.4f, exact %s %s %.0fs" % (obj, "VALID" if ok else "FAILED", b, time.time() - t0))
    else: print("ALL: %s obj %.5f %.0fs" % ("FEASIBLE" if g.done else "TIME CAP", obj, time.time() - t0))
