"""Orbit-level column model with the D-structure of the degree-6 block A VARIABLE (note 40).
Orbits: the 30 orbits of pairs not containing A keep their triples (pivot, free, third) from the leaf; the 12 orbits of the pairs
{A,x} (all anchored at A, free at x) are labelled (A, x, s), s in {0,1}.  A column of (A,x,s) chooses its third block y and its
partner orbit (A,y,s'), then free neighbours at x and a far row exactly as in orbit_colmodel (third y, typed rule n_y <= 1).
The coupling rows q_Z(W) = q_W(Z) make the q = 2 entries a perfect matching of the A-orbits between different pairs, i.e. a
2-regular loopless D-graph at A: every A-structure is represented, nothing else at integer level.  Rows and exact check are those
of orbit_colmodel (I rows, S, C, cuts).
Usage: python orbit_colmodel_var.py <mix6 class json glob> <job index> [leaf indices]   (leaves of one orientation job)"""
import sys, json, glob, itertools, time
from collections import defaultdict
import numpy as np
sys.path.insert(0, "scripts")
import orbit_colmodel as OM
from gen_colmodel_lam import far_solutions
N = 7

class OrbitModelVar(OM.OrbitModel):
    def __init__(self, leaf, A, use_I=True):
        self.use_I = use_I; self.A = A
        fixed = [tuple(t) for t in leaf]
        self.T = fixed + [(A, x, None) for x in range(N) if x != A for s in (0, 1)]
        n = self.n = len(self.T); assert n == 42
        self.pair = [frozenset(t[:2]) for t in self.T]
        self.orbs_of = defaultdict(list)
        for s in range(n): self.orbs_of[self.pair[s]].append(s)
        assert all(len(v) == 2 for v in self.orbs_of.values()) and len(self.orbs_of) == 21
        self.sis = [next(u for u in self.orbs_of[self.pair[s]] if u != s) for s in range(n)]
        self.isA = [self.T[s][0] == A and self.T[s][2] is None for s in range(n)]
        byt = defaultdict(list)
        for s in range(30): byt[self.T[s]].append(s)
        self.D = [None] * n
        for s in range(30):
            i, j, k = self.T[s]; self.D[s] = byt[(i, k, j)][byt[(i, j, k)].index(s)]
        assert all(self.D[self.D[s]] == s for s in range(30))
        self.free = {c: [s for s in range(n) if self.T[s][1] == c] for c in range(N)}
        self.Sh = np.array([[2 if self.pair[a] == self.pair[b] else len(self.pair[a] & self.pair[b]) for b in range(n)] for a in range(n)])
        self.build_columns(); self.build_rows()

    def _cols_for(self, Z, i, j, k, Dz):
        cand = [F for F in self.free[j] if F != Z and F != self.sis[Z]]
        far_blocks = [t for t in range(N) if t not in (i, j)]
        blocks_of = lambda F: next(iter(self.pair[F] - {j}))
        mats = []
        for F1, F2 in itertools.combinations(cand, 2):
            r1, r2 = blocks_of(F1), blocks_of(F2)
            if r1 == r2 == k: continue
            nv = defaultdict(int); nv[r1] += 1; nv[r2] += 1
            deg = {t: 4 - 2 * (t == k) - nv[t] for t in far_blocks}
            if min(deg.values()) < 0: continue
            prs, sols = far_solutions(far_blocks, deg)
            base = np.zeros(42, dtype=np.int8); base[Dz] = 2; base[F1] += 1; base[F2] += 1
            for s in sols:
                v = base.copy(); opts = []
                for R, val in zip(prs, s):
                    o1, o2 = self.orbs_of[R]
                    if val == 2: v[o1] += 1; v[o2] += 1
                    elif val == 1: opts.append((o1, o2))
                m = len(opts)
                if m == 0: mats.append(v[None, :]); continue
                ch = ((np.arange(1 << m)[:, None] >> np.arange(m)[None, :]) & 1).astype(bool)
                blk = np.repeat(v[None, :], 1 << m, axis=0)
                for t, (o1, o2) in enumerate(opts):
                    blk[~ch[:, t], o1] += 1; blk[ch[:, t], o2] += 1
                mats.append(blk)
        return mats

    def build_columns(self):
        self.cols = []
        for Z in range(self.n):
            if not self.isA[Z]:
                i, j, k = self.T[Z]; mats = self._cols_for(Z, i, j, k, self.D[Z])
            else:
                A, x, _ = self.T[Z]; mats = []
                for y in range(N):
                    if y in (A, x): continue
                    for Dz in self.orbs_of[frozenset((A, y))]: mats += self._cols_for(Z, A, x, y, Dz)
            M = np.concatenate(mats); assert (M.sum(axis=1) == 12).all()
            self.cols.append(M)

if __name__ == "__main__":
    import os
    pat, job = sys.argv[1], int(sys.argv[2])
    jobs = []
    for f in sorted(glob.glob(pat)):
        d = json.load(open(f))
        for po in d["per_orient"]:
            if po["leaves"]: jobs.append((po, [tuple(map(tuple, L)) for L in po["leaves"]]))
    po, leaves = jobs[job]
    idx = [int(a) for a in sys.argv[3:]] or list(range(len(leaves)))
    for t in idx:
        t0 = time.time(); g = OrbitModelVar(leaves[t], po["A"])
        print("job %d leaf %d: columns %d rows %d built %.0fs" % (job, t, sum(len(M) for M in g.cols), len(g.rname), time.time() - t0)); sys.stdout.flush()
        obj, y = g.solve(tlimit=float(os.environ.get('TL', 280)), verbose=os.environ.get('V') is not None)
        if g.done and obj > 1e-6:
            ok, b = g.verify(y)
            if ok: OM.save_cert(g, y, "logs/orbit_certs/var_%s_%d_%d.json.gz" % (os.environ.get('TAG', 'x'), job, t), "var", {"leaf": [list(z) for z in leaves[t]], "A": po["A"]}, b)
            print("job %d leaf %d: INFEASIBLE (A variable), slack %.4f, exact %s %s %.0fs" % (job, t, obj, "VALID" if ok else "FAILED", b, time.time() - t0))
        else: print("job %d leaf %d: %s obj %.5f %.0fs" % (job, t, "FEASIBLE" if g.done else "TIME CAP", obj, time.time() - t0))
        sys.stdout.flush()
