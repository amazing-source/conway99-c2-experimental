"""Unified orbit model with the dd pairs fixed and the ORIENTATION of every other (anchored) pair VARIABLE (note 41): tests
whether a whole AD family (given its set of doubly-disjoint pairs) dies in ONE LP.
Orbits: (pair, s).  dd pairs: both orbits dis (columns as in orbit_colmodel_U, near candidates = every orbit of a pair {i,r},
r != j: whether it is free at i is enforced by the coupling rows).  Anchored pairs {a,b}: each orbit chooses its pivot in {a,b}
(columns for both), rows piv[R]: P(orbit 0 has pivot a) - P(orbit 1 has pivot a) = 0 (both orbits of an anchored pair share the
pivot).  One-block columns: partner = an anchored-pair orbit of {i,k} (its pivot choice must be i: enforced by coupling, since a
column with pivot k has no neighbour in the pairs {k,.} except its partner), free neighbours = orbits of pairs {j,r}, r != i.
No cut rows (free sets are variable).  Exact check as in orbit_colmodel_T.
Usage: python orbit_colmodel_UT.py <dd pairs, e.g. 01,23>"""
import sys, itertools, time, os, json
from collections import defaultdict
import numpy as np
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_U as OU, orbit_colmodel_T as OT
from gen_colmodel_lam import far_solutions
N = 7

class OrbitModelUT(OT.OrbitModelT):
    def __init__(self, ddpairs, use_I=True):
        self.use_I = use_I; self.dd = {frozenset(p) for p in ddpairs}
        self.T = []; self.pivopts = []; self.otype = []
        for a in range(N):
            for b in range(a + 1, N):
                R = frozenset((a, b))
                for s in (0, 1):
                    self.T.append((a, b, None))
                    if R in self.dd: self.pivopts.append([]); self.otype.append(('dis',))
                    else: self.pivopts.append([a, b]); self.otype.append(('one', None))
        n = self.n = 42
        self.pair = [frozenset(t[:2]) for t in self.T]
        self.orbs_of = defaultdict(list)
        for s in range(n): self.orbs_of[self.pair[s]].append(s)
        self.sis = [next(u for u in self.orbs_of[self.pair[s]] if u != s) for s in range(n)]
        self.Sh = np.array([[2 if self.pair[a] == self.pair[b] else len(self.pair[a] & self.pair[b]) for b in range(n)] for a in range(n)])
        self.tw = set(); self.forbid = set()
        self.build_columns(); self.free = {c: [] for c in range(N)}; self.build_rows(); self.add_piv_rows(); self.fdeg = {}

    def add_piv_rows(self):
        self.pivrow = {}
        for R, (o0, o1) in self.orbs_of.items():
            if R in self.dd: continue
            r = len(self.rname); name = ('piv', R); self.rows[name] = r
            self.rname.append(name); self.rkind.append('eq'); self.rrhs.append(0)
            self.pivrow[o0] = (r, 1, min(R)); self.pivrow[o1] = (r, -1, min(R))

    def build_columns(self):
        self.cols = []; self.cpiv = []
        other = lambda F, blk: next(iter(self.pair[F] - {blk}))
        for Z in range(self.n):
            a, b, _ = self.T[Z]; mats = []; pv = []
            if self.otype[Z][0] == 'one':
                for i in (a, b):
                    j = a + b - i
                    cand = [F for F in range(self.n) if j in self.pair[F] and i not in self.pair[F] and F != Z]
                    fb = [t for t in range(N) if t not in (i, j)]
                    for k in fb:
                        for Dz in self.orbs_of[frozenset((i, k))]:
                            if self.otype[Dz][0] != 'one': continue
                            for F1, F2 in itertools.combinations(cand, 2):
                                r1, r2 = other(F1, j), other(F2, j)
                                if r1 == r2 == k: continue
                                nv = defaultdict(int); nv[r1] += 1; nv[r2] += 1
                                deg = {t: 4 - 2 * (t == k) - nv[t] for t in fb}
                                if min(deg.values()) < 0: continue
                                prs, sols = far_solutions(fb, deg)
                                base = np.zeros(42, dtype=np.int8); base[Dz] = 2; base[F1] += 1; base[F2] += 1
                                blk = OU.OrbitModelU._expand(self, base, [frozenset(p) for p in prs], sols)
                                mats += blk; pv += [np.full(len(x), i, dtype=np.int8) for x in blk]
            else:
                i, j = a, b; Zs = self.sis[Z]; fb = [t for t in range(N) if t not in (i, j)]
                loops = (0, 1)
                ci = [F for F in range(self.n) if i in self.pair[F] and j not in self.pair[F]]
                cj = [F for F in range(self.n) if j in self.pair[F] and i not in self.pair[F]]
                for Dz in range(self.n):
                    if self.otype[Dz] != ('dis',) or (self.pair[Dz] & self.pair[Z]): continue
                    R = self.pair[Dz]; k, l = tuple(R)
                    for loop in loops:
                        ni = 2 - loop
                        for Fi in itertools.combinations(ci, ni):
                            ri = [other(F, i) for F in Fi]
                            if ni == 2 and ri[0] == ri[1] and ri[0] in (k, l): continue
                            for Fj in itertools.combinations(cj, ni):
                                rj = [other(F, j) for F in Fj]
                                if ni == 2 and rj[0] == rj[1] and rj[0] in (k, l): continue
                                nv = defaultdict(int)
                                for r in ri + rj: nv[r] += 1
                                deg = {t: 4 - nv[t] for t in fb}
                                if min(deg.values()) < 0: continue
                                prs, sols = OU.far_sols_dis(fb, deg, R)
                                if not sols: continue
                                base = np.zeros(42, dtype=np.int8)
                                for F in Fi + Fj: base[F] += 1
                                if loop: base[Zs] += 1
                                blk = OU.OrbitModelU._expand(self, base, prs, sols, Dpair=R, Dz=Dz)
                                mats += blk; pv += [np.full(len(x), -1, dtype=np.int8) for x in blk]
            M = np.concatenate(mats); assert (M.sum(axis=1) == 12).all()
            self.cols.append(M); self.cpiv.append(np.concatenate(pv))

if __name__ == "__main__":
    dd = [tuple(int(c) for c in p) for p in sys.argv[1].split(",")]
    t0 = time.time(); g = OrbitModelUT(dd, use_I={'none': False}.get(os.environ.get('MODE'), True))
    print("UT dd=%s: columns %d rows %d built %.0fs" % (dd, sum(len(M) for M in g.cols), len(g.rname), time.time() - t0)); sys.stdout.flush()
    obj, y = g.solve(tlimit=float(os.environ.get('TL', 6000)), verbose=os.environ.get('V') is not None)
    if g.done and obj > 1e-6:
        ok, b = g.verify(y); print("UT dd=%s: INFEASIBLE (orientation variable) slack %.4f exact %s %s %.0fs" % (dd, obj, "VALID" if ok else "FAILED", b, time.time() - t0))
    else: print("UT dd=%s: %s obj %.5f %.0fs" % (dd, "FEASIBLE" if g.done else "TIME CAP", obj, time.time() - t0))
