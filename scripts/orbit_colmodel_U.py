"""UNIFIED orbit-level column model (note 40): one-block AND disjoint squares, types fixed per pair, every D-partner variable.
Pair types: ('anch', c) both orbits one-block via c; ('tw',) orbit 0 via min, orbit 1 via max; ('dd',) both orbits dis;
('mix', c) orbit 0 one-block via c, orbit 1 dis.  (Sigma = empty here.)
Columns (all proved; notes 27-31, 39, 40):
  one-block Z (pivot i, free j): as orbit_colmodel_gen (partner = one-block orbit of {i,k} with pivot i, typed rule).
  dis Z of P = {i,j}: partner W = a dis orbit of a pair R = {k,l} disjoint from P, q[W] = 2, q[W'] = x in {0,1} ((2,0) or (2,1));
     loop (n_s = 1, only if the sister is dis, 39.3): q[sister] = 1, counting as one neighbour at i AND one at j;
     near: 2 - loop free neighbours at i (pairs {i,r}, r != j) and at j, never both in {i,k} (or {i,l}, {j,k}, {j,l}):
       two such roots would carry the same sign at k and, with w or sigma w, give (k,.) three neighbours (mu = 2);
     far: pairs disjoint from P, block sums 4 - n^i_t - n^j_t, v(R) = 2 + x, v <= 2 elsewhere; v = 2 -> (1,1), v = 1 -> one orbit.
Rows: those of orbit_colmodel (one, S, C, I, cuts on the free graphs; a loop is an edge of R_i and of R_j).
Usage: see __main__ (tests)."""
import sys, itertools, time, os, json
from collections import defaultdict
import numpy as np
sys.path.insert(0, "scripts")
import orbit_colmodel as OM
from gen_colmodel_lam import far_solutions
N = 7

def far_sols_dis(blocks5, deg, R):
    """far rows with v(R) in {2,3} and v <= 2 elsewhere, block sums deg"""
    out = []
    for vR in (2, 3):
        d2 = dict(deg); a, b = tuple(R)
        d2[a] -= vR; d2[b] -= vR
        if min(d2.values()) < 0: continue
        prs, sols = far_solutions(blocks5, d2)
        iR = prs.index(frozenset(R))
        for s in sols:
            if s[iR] != 0: continue                    # the R-entry is carried by vR
            s2 = list(s); s2[iR] = vR; out.append(tuple(s2))
    prs = [frozenset(p) for p in itertools.combinations(blocks5, 2)]
    return prs, out

class OrbitModelU(OM.OrbitModel):
    def __init__(self, ptype, use_I=True):
        self.use_I = use_I; self.T = []; self.otype = []
        for a in range(N):
            for b in range(a + 1, N):
                t = ptype[(a, b)]
                for s in (0, 1):
                    if t[0] == 'anch': ty = ('one', t[1])
                    elif t[0] == 'tw': ty = ('one', (a, b)[s])
                    elif t[0] == 'dd': ty = ('dis',)
                    elif t[0] == 'mix': ty = ('one', t[1]) if s == 0 else ('dis',)
                    else: raise ValueError(t)
                    self.T.append((a, b, None)); self.otype.append(ty)
        n = self.n = 42
        self.pair = [frozenset(t[:2]) for t in self.T]
        self.orbs_of = defaultdict(list)
        for s in range(n): self.orbs_of[self.pair[s]].append(s)
        self.sis = [next(u for u in self.orbs_of[self.pair[s]] if u != s) for s in range(n)]
        self.free = {c: [s for s in range(n) if c in self.pair[s] and (self.otype[s][0] == 'dis' or self.otype[s][1] != c)] for c in range(N)}
        self.Sh = np.array([[2 if self.pair[a] == self.pair[b] else len(self.pair[a] & self.pair[b]) for b in range(n)] for a in range(n)])
        self.use_sis5 = False
        self.build_columns(); self.build_rows()

    def _expand(self, base, prs, sols, Dpair=None, Dz=None):
        mats = []
        for s in sols:
            v = base.copy(); opts = []
            for R, val in zip(prs, s):
                o1, o2 = self.orbs_of[R]
                if R == Dpair:
                    Wp = o2 if Dz == o1 else o1
                    v[Dz] += 2; v[Wp] += val - 2
                elif val == 2: v[o1] += 1; v[o2] += 1
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
            a, b, _ = self.T[Z]; ty = self.otype[Z]; mats = []
            other = lambda F, blk: next(iter(self.pair[F] - {blk}))
            if ty[0] == 'one':
                i = ty[1]; j = a + b - i
                cand = [F for F in self.free[j] if F != Z and i not in self.pair[F]]
                fb = [t for t in range(N) if t not in (i, j)]
                for k in fb:
                    for Dz in self.orbs_of[frozenset((i, k))]:
                        if self.otype[Dz] != ('one', i): continue
                        for F1, F2 in itertools.combinations(cand, 2):
                            r1, r2 = other(F1, j), other(F2, j)
                            if r1 == r2 == k: continue
                            nv = defaultdict(int); nv[r1] += 1; nv[r2] += 1
                            deg = {t: 4 - 2 * (t == k) - nv[t] for t in fb}
                            if min(deg.values()) < 0: continue
                            prs, sols = far_solutions(fb, deg)
                            base = np.zeros(42, dtype=np.int8); base[Dz] = 2; base[F1] += 1; base[F2] += 1
                            mats += self._expand(base, [frozenset(p) for p in prs], sols)
            else:
                i, j = a, b; Zs = self.sis[Z]; fb = [t for t in range(N) if t not in (i, j)]
                loops = (0, 1) if self.otype[Zs] == ('dis',) else (0,)
                for Dz in range(self.n):
                    if self.otype[Dz] != ('dis',) or (self.pair[Dz] & self.pair[Z]): continue
                    R = self.pair[Dz]; k, l = tuple(R)
                    ci = [F for F in self.free[i] if F not in (Z, Zs) and j not in self.pair[F]]
                    cj = [F for F in self.free[j] if F not in (Z, Zs) and i not in self.pair[F]]
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
                                prs, sols = far_sols_dis(fb, deg, R)
                                if not sols: continue
                                base = np.zeros(42, dtype=np.int8)
                                for F in Fi + Fj: base[F] += 1
                                if loop: base[Zs] += 1
                                mats += self._expand(base, prs, sols, Dpair=R, Dz=Dz)
            M = np.concatenate(mats) if mats else np.zeros((0, 42), dtype=np.int8)
            if len(M): assert (M.sum(axis=1) == 12).all(), (Z, ty)
            self.cols.append(M)

def orient_types(In):
    """pair types for a one-block orientation dict (block -> anchored-at list); other pairs twisted"""
    pt = {}
    for a in range(N):
        for b in range(a + 1, N): pt[(a, b)] = ('tw',)
    for c, xs in In.items():
        for x in xs: pt[(min(c, x), max(c, x))] = ('anch', c)
    return pt

if __name__ == "__main__":
    import glob
    mode = sys.argv[1]
    if mode == "regress":                     # must reproduce orbit_colmodel_gen on a pure one-block orientation
        jobs = []
        for f in sorted(glob.glob("logs/mix6_cls_E01_12_23_34_45_05_S_*.json")):
            d = json.load(open(f))
            for po in d["per_orient"]:
                if po["leaves"]: jobs.append(po)
        In = {int(x): v for x, v in jobs[int(sys.argv[2])]["In"].items()}
        t0 = time.time(); g = OrbitModelU(orient_types(In))
        print("U-model (one-block only): columns %d rows %d %.0fs" % (sum(len(M) for M in g.cols), len(g.rname), time.time() - t0)); sys.stdout.flush()
        obj, y = g.solve(tlimit=float(os.environ.get('TL', 3000)), verbose=os.environ.get('V') is not None)
        if g.done and obj > 1e-6:
            ok, b = g.verify(y); print("INFEASIBLE slack %.4f exact %s %s" % (obj, "VALID" if ok else "FAILED", b))
        else: print("%s obj %.5f" % ("FEASIBLE" if g.done else "TIME CAP", obj))
