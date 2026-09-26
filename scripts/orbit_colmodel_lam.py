"""Orbit-level LP, orientation fixed, with the D-matching at every non-A block c restricted to a convex combination of the
D-structures that occur in the FILTERED leaves (note 40).  lambda-variables per block c over all orbit-level lifts of the
allowed pair-level structures (label choices inside anchored pairs are free), rows
   L[c,{Z,W}] :  P(Z -> W) - sum_g lambda_{c,g} [g matches Z with W] = 0      (Z, W pivot-c orbits of different pairs)
   Lone[c]    :  sum_g lambda_{c,g} = 1.
Valid for the orientation: every leaf's structure at c is allowed, so every surviving skeleton is a feasible point.
Exact check: UB = sum_Z max over Z's columns + sum_c max over block c's lambda columns + le terms (every lambda-block is a
convex combination, like an orbit).
Usage: python orbit_colmodel_lam.py <class id> <job>"""
import sys, json, glob, time, os, itertools
from collections import defaultdict
import numpy as np
sys.path.insert(0, "scripts")
import orbit_colmodel as OM, orbit_colmodel_gen as OG
N = 7

def lifts(g0, c, triples):
    """orbit-level matchings at block c for a pair-level structure given by its triples (c, x, y); digons handled"""
    thirds = defaultdict(list)
    for (i, x, y) in triples: thirds[x].append(y)
    xs = sorted(thirds)
    orbs = {x: [o for o in g0.orbs_of[frozenset((c, x))] if g0.pivot[o] == c] for x in xs}
    out = set()
    for perm in itertools.product(*[list(itertools.permutations(orbs[x])) for x in xs]):
        has = defaultdict(list)                  # (x, y) -> orbits of {c,x} whose third is y
        for x, pos in zip(xs, perm):
            for o, y in zip(pos, sorted(thirds[x])): has[(x, y)].append(o)
        edges = sorted({(min(x, y), max(x, y)) for (x, y) in has})
        choices = []
        for (x, y) in edges:
            A_, B_ = has[(x, y)], has[(y, x)]
            assert len(A_) == len(B_)
            choices.append([list(zip(A_, pb)) for pb in itertools.permutations(B_)])
        for pick in itertools.product(*choices):
            M = frozenset(frozenset(e) for lst in pick for e in lst)
            if all(len(e) == 2 for e in M) and len(M) == sum(len(v) for v in has.values()) // 2: out.add(M)
    return out

class OrbitModelLam(OG.OrbitModelGen):
    def __init__(self, In, leaves, A):
        super().__init__(In)
        self.lam = defaultdict(list)             # c -> list of matchings (frozenset of frozenset pairs)
        for c in range(N):
            if c == A: continue
            structs = {tuple(sorted(z for z in L if z[0] == c)) for L in leaves}
            if not structs or structs == {()}: continue
            allm = set()
            for s in structs: allm |= lifts(self, c, s)
            self.lam[c] = sorted(allm, key=lambda M: sorted(tuple(sorted(e)) for e in M))
        # rows
        self.lamrow = {}
        for c, Ms in self.lam.items():
            r = len(self.rname); self.rows[('Lone', c)] = r; self.rname.append(('Lone', c)); self.rkind.append('eq'); self.rrhs.append(1)
            piv = [o for o in range(42) if self.pivot[o] == c]
            for Z, W in itertools.combinations(piv, 2):
                if self.pair[Z] == self.pair[W]: continue
                r = len(self.rname); nm = ('L', c, Z, W); self.rows[nm] = r; self.rname.append(nm); self.rkind.append('eq'); self.rrhs.append(0)
                self.lamrow[(Z, W)] = r; self.lamrow[(W, Z)] = r
        # a column of Z with partner W (Z < W) contributes +1 to L[c,Z,W]: add to the per-orbit partner map
        self.partner_rows = {}
        for (Z, W), r in self.lamrow.items():
            if Z < W: self.partner_rows[(Z, W)] = r
        self.lamcols = []
        for c, Ms in self.lam.items():
            for M in Ms:
                ent = [(self.rows[('Lone', c)], 1)]
                for e in M:
                    Z, W = sorted(e); ent.append((self.lamrow[(Z, W)], -1))
                self.lamcols.append((c, ent))

    def extra_scores(self, y, Z, M):
        out = super().extra_scores(y, Z, M)
        D = np.argmax(M == 2, axis=1)                   # partner of each column
        add = np.zeros(len(M), dtype=y.dtype)
        for W in np.unique(D):
            r = self.partner_rows.get((Z, int(W))) if Z < W else None
            if r is not None: add[D == W] += y[r]
        return out + add

    def entries(self, Z, q):
        ent = super().entries(Z, q)
        W = int(np.argmax(q == 2))
        if Z < W and (Z, W) in self.partner_rows: ent = ent + [(self.partner_rows[(Z, W)], 1)]
        return ent

    def solve(self, tlimit=3000, per=3, verbose=True, init=None):
        # lambda columns are permanent: prepend them through the init mechanism of the base class by monkey-patching master
        base_master = self.master
        lamc = [ent for c, ent in self.lamcols]
        def master(cols): return base_master(lamc + cols)
        self.master = master
        return super().solve(tlimit=tlimit, per=per, verbose=verbose, init=init)

    def verify(self, y, den=10 ** 6):
        ok, (yb, LB, UB) = super().verify(y, den)
        yi = np.array([int(round(v * den)) for v in y], dtype=np.int64)
        extra = 0
        for c in self.lam:
            best = None
            for cc, ent in self.lamcols:
                if cc != c: continue
                s = sum(int(yi[r]) * v for r, v in ent)
                best = s if best is None else max(best, s)
            extra += best
        UB2 = UB * den + extra
        return (yb * den > UB2), (yb, LB, UB2 / den)

if __name__ == "__main__":
    ci, job = sys.argv[1], int(sys.argv[2])
    jobs = []
    for f in sorted(glob.glob("logs/mix6_cls_%s_S_*.json" % ci)):
        d = json.load(open(f))
        for po in d["per_orient"]:
            if po["leaves"]: jobs.append((po, [tuple(map(tuple, L)) for L in po["leaves"]]))
    po, leaves = jobs[job]; In = {int(x): v for x, v in po["In"].items()}
    t0 = time.time(); g = OrbitModelLam(In, leaves, po["A"])
    print("lam model %s job %d: columns %d rows %d lambda-cols %s %.0fs" % (ci, job, sum(len(M) for M in g.cols), len(g.rname),
          {c: len(v) for c, v in g.lam.items()}, time.time() - t0)); sys.stdout.flush()
    obj, y = g.solve(tlimit=float(os.environ.get('TL', 3000)), verbose=os.environ.get('V') is not None)
    if g.done and obj > 1e-6:
        ok, b = g.verify(y); print("LAM %s job %d: INFEASIBLE slack %.4f exact %s %s %.0fs" % (ci, job, obj, "VALID" if ok else "FAILED", b, time.time() - t0))
    else: print("LAM %s job %d: %s obj %.5f %.0fs" % (ci, job, "FEASIBLE" if g.done else "TIME CAP", obj, time.time() - t0))
