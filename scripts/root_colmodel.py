"""ROOT-level (signed) column model, orientation fixed, every D-structure variable (note 40).
Orbit-level columns lose WHICH root of an orbit is adjacent; here a column of orbit Z is the full root neighbourhood r in {0,1}^84
of its representative z, so both the invariant identity (Q^2 + Q = 12I + 4J - Sh) and the anti-invariant one
(S^2 + S = 12I - C C^T, vendor/involution_frame.py) are rows.  Written independently of the orbit models.

Conventions (as vendor/involution_frame.py): pair p = (a,b), a < b; root (a,s)(b,t) has id 4p + 2[s = -] + [t = -];
orbit id 2p + e, e = [s t = -]; representative rep(2p+e) = 4p + e = (a,+)(b,(-1)^e); sigma(root) flips both signs.
Twisted pair (a,b): the orbit with pivot a has e = twe[(a,b)] (a holonomy choice: only the class modulo block flips matters).

Column of Z (pivot i, free j, sign beta of z at j):
  D-partner W (orbit of {i,k} with pivot i): both roots of W;  no other neighbour touches block i (F1);
  m-neighbour: the root containing (j, beta) of a free orbit F_m at j;  pi-neighbour: the root containing (j, -beta) of another
  free orbit F_pi at j (not the sister, not both in {j,k}: typed rule);
  far: 8 roots in pairs of the 5 blocks != i,j, at most one root per orbit, and at every far block c exactly two neighbours
  contain (c,+) and two contain (c,-)  (mu = 2 with the interior vertices (c,+-)).
Rows (all doubled to integers):
  one[Z]; symP(U,W): r_U(rep W) = r_W(rep U); symM(U,W): r_U(s rep W) = r_W(s rep U);
  I(U,W,+-): sum_X 2[r_X(u) r_X(v) + r_X(su) r_X(sv)] + r_U(v) + r_W(u~) = 2(12[u = v] + 2 - |u & v|),  v = rep W or s rep W
     (this is (B^2 + B)_{uv} = 12 I + 2 J - C C^T on the 84 roots, B = root adjacency; both factors read in X's column);
  cut[c,S]: free-graph subtour cuts on orbit level q = r(rep) + r(s rep).
Exact check: integer duals, max over ALL columns of every orbit (near configurations x cached far sets).
Usage: python root_colmodel.py <class id> <job> <holonomy bits, e.g. 0 or 01>"""
import sys, os, json, glob, itertools, time
from collections import defaultdict
import numpy as np
import highspy
from scipy.sparse import csc_matrix
N = 7
PAIRS = [(a, b) for a in range(N) for b in range(a + 1, N)]
PI = {pr: t for t, pr in enumerate(PAIRS)}

def root_id(a, b, sa, tb):                      # a < b, sa/tb = 0 for +, 1 for -
    return 4 * PI[(a, b)] + 2 * sa + tb
def sig(x): return (x & ~3) | ((x & 3) ^ 3)
def orbit_of(x): return 2 * (x >> 2) + (((x >> 1) & 1) ^ (x & 1))
def rep(o): return 4 * (o >> 1) + (o & 1)
def rsign(x, c):
    a, b = PAIRS[x >> 2]
    if c == a: return -1 if (x >> 1) & 1 else 1
    if c == b: return -1 if x & 1 else 1
    return 0
def blocks(x): return PAIRS[x >> 2]
def inter(x, y): return sum(1 for c in blocks(x) if c in blocks(y) and rsign(x, c) == rsign(y, c))

_farcache = {}
def far_sets(fb, need):
    """all sets of far roots (pairs inside the far blocks fb) with exactly need[(c,s)] roots containing (c,s), never x and sx"""
    key = (fb, tuple(sorted(need.items())))
    if key in _farcache: return _farcache[key]
    hv = [(c, s) for c in fb for s in (0, 1)]
    rem = dict(need); out = []; chosen = []; used = set()
    def rec(h):
        while h < len(hv) and rem[hv[h]] == 0: h += 1
        if h == len(hv):
            out.append(tuple(sorted(chosen))); return
        c, s = hv[h]
        cand = []
        for (d, t) in hv[h + 1:]:
            if d == c or rem[(d, t)] == 0: continue
            x = root_id(c, d, s, t) if c < d else root_id(d, c, t, s)
            if x in used or sig(x) in used: continue
            cand.append(((d, t), x))
        r = rem[(c, s)]
        for combo in itertools.combinations(cand, r):
            xs = [x for _, x in combo]
            if len(set(orbit_of(x) for x in xs)) < len(xs): continue
            if any(rem[dt] < sum(1 for dt2, _ in combo if dt2 == dt) for dt, _ in combo): continue
            rem[(c, s)] = 0
            for dt, x in combo: rem[dt] -= 1; used.add(x); chosen.append(x)
            rec(h + 1)
            for dt, x in combo: rem[dt] += 1; used.discard(x); chosen.pop()
            rem[(c, s)] = r
    rec(0)
    arr = np.array(out, dtype=np.int16).reshape(len(out), -1)
    _farcache[key] = arr
    return arr

class RootModel:
    def __init__(self, In, twe):
        anch = {}
        for c, xs in In.items():
            for x in xs: anch[(min(c, x), max(c, x))] = c
        self.pivot = {}
        for (a, b) in PAIRS:
            p = PI[(a, b)]
            if (a, b) in anch:
                for e in (0, 1): self.pivot[2 * p + e] = anch[(a, b)]
            else:
                ea = twe[(a, b)]; self.pivot[2 * p + ea] = a; self.pivot[2 * p + 1 - ea] = b
        self.n = 42
        self.free = {c: [o for o in range(42) if c in PAIRS[o >> 1] and self.pivot[o] != c] for c in range(N)}
        self.build_near(); self.build_rows()

    def build_near(self):
        """per orbit: list of (near roots tuple, far key, far array)"""
        self.near = []
        for Z in range(42):
            z = rep(Z); a, b = PAIRS[Z >> 1]; i = self.pivot[Z]; j = b if i == a else a
            beta = rsign(z, j); lst = []
            fb = tuple(t for t in range(N) if t not in (i, j))
            cand = [F for F in self.free[j] if F != Z and (F >> 1) != (Z >> 1)]
            for k in fb:
                for W in (2 * PI[(min(i, k), max(i, k))], 2 * PI[(min(i, k), max(i, k))] + 1):
                    if self.pivot[W] != i: continue
                    Droots = (rep(W), sig(rep(W)))
                    for Fm, Fp in itertools.permutations(cand, 2):
                        rm_ = next(iter(set(PAIRS[Fm >> 1]) - {j})); rp_ = next(iter(set(PAIRS[Fp >> 1]) - {j}))
                        if rm_ == k and rp_ == k: continue
                        xm = rep(Fm) if rsign(rep(Fm), j) == beta else sig(rep(Fm))
                        xp = rep(Fp) if rsign(rep(Fp), j) == -beta else sig(rep(Fp))
                        near = Droots + (xm, xp)
                        need = {(c, s): 2 for c in fb for s in (0, 1)}
                        ok = True
                        for x in near:
                            for c in blocks(x):
                                if c in fb:
                                    key = (c, 0 if rsign(x, c) > 0 else 1); need[key] -= 1
                                    if need[key] < 0: ok = False
                        if not ok: continue
                        F = far_sets(fb, need)
                        if len(F): lst.append((near, F))
            self.near.append(lst)

    def ncols(self): return sum(len(F) for lst in self.near for _, F in lst)

    def build_rows(self):
        self.rname = []; self.rkind = []; self.rrhs = []; self.rows = {}
        def add(name, kind, rhs):
            self.rows[name] = len(self.rname); self.rname.append(name); self.rkind.append(kind); self.rrhs.append(rhs)
        for Z in range(42): add(('one', Z), 'eq', 1)
        for U in range(42):
            for W in range(U + 1, 42):
                add(('symP', U, W), 'eq', 0); add(('symM', U, W), 'eq', 0)
        even = os.environ.get('EVEN') is not None           # control: only the invariant (summed) identity
        for U in range(42):
            for W in range(U, 42):
                for sg in (1, -1):
                    u = rep(U); v = rep(W) if sg > 0 else sig(rep(W))
                    rhs = 2 * (12 * (u == v) + 2 - inter(u, v))
                    if even and sg < 0:
                        r0 = self.rows[('I', U, W, 1)]; self.rrhs[r0] += rhs; self.rows[('I', U, W, sg)] = r0
                    else: add(('I', U, W, sg), 'eq', rhs)
        self.cuts = []
        for c in range(N):
            F = self.free[c]; f = len(F)
            if f == 0: continue
            bad = set()
            def parts(n_, mn):
                if n_ == 0: yield []; return
                for p_ in range(max(4, mn), n_ + 1, 2):
                    for r_ in parts(n_ - p_, p_): yield [p_] + r_
            for pr in parts(f, 4):
                for r_ in range(len(pr) + 1):
                    for cmb in itertools.combinations(pr, r_): bad.add(sum(cmb))
            for size in range(3, f):
                if size in bad: continue
                for S in itertools.combinations(F, size):
                    add(('cut', c, S), 'le', 2 * (size - 1)); self.cuts.append((c, S))
        # static maps: identity rows -> (u, v) quadratic positions; per-orbit linear maps
        self.Irows = []
        for U in range(42):
            for W in range(U, 42):
                for sg in (1, -1):
                    u = rep(U); v = rep(W) if sg > 0 else sig(rep(W)); ut = rep(U) if sg > 0 else sig(rep(U))
                    self.Irows.append((self.rows[('I', U, W, sg)], U, W, u, v, ut))
        self.linmap = [defaultdict(list) for _ in range(42)]       # Z -> root x -> [(row, coef)]
        for (r, U, W, u, v, ut) in self.Irows:
            self.linmap[U][v].append((r, 1)); self.linmap[W][ut].append((r, 1))
        for U in range(42):
            for W in range(U + 1, 42):
                rP = self.rows[('symP', U, W)]; rM = self.rows[('symM', U, W)]
                self.linmap[U][rep(W)].append((rP, 1)); self.linmap[W][rep(U)].append((rP, -1))
                self.linmap[U][sig(rep(W))].append((rM, 1)); self.linmap[W][sig(rep(U))].append((rM, -1))
        for (c, S) in self.cuts:
            r = self.rows[('cut', c, S)]
            for Z in S:
                for F in S:
                    if F != Z: self.linmap[Z][rep(F)].append((r, 1)); self.linmap[Z][sig(rep(F))].append((r, 1))

    def Ymat(self, y):
        Y = np.zeros((84, 84), dtype=y.dtype)
        for (r, U, W, u, v, ut) in self.Irows:
            yy = y[r]
            for (p, q) in ((u, v), (sig(u), sig(v))):
                if p == q: Y[p, p] += 2 * yy
                else: Y[p, q] += yy; Y[q, p] += yy
        return Y

    def lin(self, y, Z):
        L = np.zeros(84, dtype=y.dtype)
        for x, lst in self.linmap[Z].items():
            for r, c in lst: L[x] += c * y[r]
        return L

    def ffpart(self, Y):
        """far-far quadratic part per cached far array (independent of the orbit and of the near configuration)"""
        out = {}
        for Z in range(42):
            for near, F in self.near[Z]:
                if id(F) not in out:
                    Fi = F.astype(np.int64); out[id(F)] = Y[Fi[:, :, None], Fi[:, None, :]].sum(axis=(1, 2))
        return out

    def scores(self, y, Z, Y, L, ff=None):
        """per near configuration: (near, F, scores over F's rows)"""
        out = []
        c0 = y[self.rows[('one', Z)]]
        for near, F in self.near[Z]:
            nr = np.array(near, dtype=np.int64); Fi = F.astype(np.int64)
            s_near = c0 + L[nr].sum() + Y[np.ix_(nr, nr)].sum()
            cross = 2 * Y[nr][:, Fi].sum(axis=(0, 2))
            f2 = ff[id(F)] if ff is not None else Y[Fi[:, :, None], Fi[:, None, :]].sum(axis=(1, 2))
            out.append((near, F, s_near + cross + f2 + L[Fi].sum(axis=1)))
        return out

    def entries(self, Z, rset):
        d = defaultdict(int); d[self.rows[('one', Z)]] += 1
        for x in rset:
            for r, c in self.linmap[Z].get(x, ()): d[r] += c
        for (r, U, W, u, v, ut) in self.Irows:
            t = (1 if (u in rset and v in rset) else 0) + (1 if (sig(u) in rset and sig(v) in rset) else 0)
            if t: d[r] += 2 * t
        return [(r, c) for r, c in d.items() if c]

    def master(self, cols):
        m = len(self.rname); nx = len(cols)
        le = [r for r in range(m) if self.rkind[r] == 'le']; eq = [r for r in range(m) if self.rkind[r] == 'eq']
        ri, ci, data = [], [], []
        for c, ent in enumerate(cols):
            for r, v in ent: ri.append(r); ci.append(c); data.append(float(v))
        for t, r in enumerate(le): ri.append(r); ci.append(nx + t); data.append(1.0)
        for t, r in enumerate(eq):
            ri += [r, r]; ci += [nx + len(le) + 2 * t, nx + len(le) + 2 * t + 1]; data += [1.0, -1.0]
        nc = nx + len(le) + 2 * len(eq)
        A = csc_matrix((data, (ri, ci)), shape=(m, nc))
        lp = highspy.HighsLp(); lp.num_col_ = nc; lp.num_row_ = m
        lp.col_cost_ = np.concatenate([np.zeros(nx + len(le)), np.ones(2 * len(eq))])
        lp.col_lower_ = np.zeros(nc)
        lp.col_upper_ = np.concatenate([np.full(nx, highspy.kHighsInf), np.array([self.rrhs[r] for r in le], dtype=float), np.full(2 * len(eq), highspy.kHighsInf)])
        b = np.array(self.rrhs, dtype=float); lp.row_lower_ = b; lp.row_upper_ = b
        lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
        lp.a_matrix_.start_ = A.indptr; lp.a_matrix_.index_ = A.indices; lp.a_matrix_.value_ = A.data
        h = highspy.Highs(); h.setOptionValue("output_flag", False); h.setOptionValue("solver", "ipm"); h.setOptionValue("run_crossover", "off")
        h.passModel(lp); h.run()
        return h

    def solve(self, tlimit=3000, per=3, verbose=True):
        t0 = time.time(); cols = []; keys = set(); rng = np.random.default_rng(0)
        for Z in range(42):
            for t in rng.choice(len(self.near[Z]), size=min(3, len(self.near[Z])), replace=False):
                near, F = self.near[Z][t]; rs = frozenset(near + tuple(int(v) for v in F[0]))
                keys.add((Z, rs)); cols.append(self.entries(Z, rs))
        it = 0
        while True:
            it += 1; tm = time.time()
            h = self.master(cols); obj = h.getInfo().objective_function_value; tm = time.time() - tm
            y = np.array(h.getSolution().row_dual); Y = self.Ymat(y); added = 0; best = 0.0; tp = time.time()
            if obj > 1e-7:
                ff = self.ffpart(Y)
                for Z in range(42):
                    L = self.lin(y, Z); cand = []
                    for near, F, sc in self.scores(y, Z, Y, L, ff):
                        if len(sc) == 0: continue
                        t = int(np.argmax(sc)); cand.append((sc[t], near, F[t]))
                    cand.sort(key=lambda z_: -z_[0])
                    for sc_, near, frow in cand[:per]:
                        if sc_ <= 1e-6: break
                        rs = frozenset(near + tuple(int(v) for v in frow))
                        if (Z, rs) in keys: continue
                        keys.add((Z, rs)); cols.append(self.entries(Z, rs)); added += 1; best = max(best, sc_)
            if verbose: print("  iter %d obj %.5f cols %d added %d best %.3g %.0fs (master %.1fs, pricing %.1fs)" % (it, obj, len(cols), added, best, time.time() - t0, tm, time.time() - tp)); sys.stdout.flush()
            if added == 0 or time.time() - t0 > tlimit:
                self.done = added == 0; return obj, y

    def verify(self, y, den=10 ** 6):
        yi = np.array([int(round(v * den)) for v in y], dtype=np.int64)
        yb = int(sum(int(yi[r]) * int(self.rrhs[r]) for r in range(len(yi))))
        UB = sum(max(int(yi[r]) * int(self.rrhs[r]), 0) for r in range(len(yi)) if self.rkind[r] == 'le')
        Y = self.Ymat(yi); ff = self.ffpart(Y)
        for Z in range(42):
            L = self.lin(yi, Z)
            UB += max(int(sc.max()) for near, F, sc in self.scores(yi, Z, Y, L, ff) if len(sc))
        return yb > UB, (yb / den, UB / den)

if __name__ == "__main__":
    ci, job, hol = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    jobs = []
    for f in sorted(glob.glob("logs/mix6_cls_%s_S_*.json" % ci)):
        d = json.load(open(f))
        for po in d["per_orient"]:
            if po["leaves"]: jobs.append(po)
    po = jobs[job]; In = {int(x): v for x, v in po["In"].items()}
    anch = {(min(c, x), max(c, x)) for c, xs in In.items() for x in xs}
    tw = [pr for pr in PAIRS if pr not in anch]
    bits = [int(ch) for ch in hol]
    twe = {pr: (bits[t] if t < len(bits) else 0) for t, pr in enumerate(tw)}
    t0 = time.time(); g = RootModel(In, twe)
    print("root model %s job %d holonomy %s: twisted %s, columns %d, rows %d, built %.0fs" % (ci, job, hol, tw, g.ncols(), len(g.rname), time.time() - t0)); sys.stdout.flush()
    obj, y = g.solve(tlimit=float(os.environ.get('TL', 3000)), verbose=os.environ.get('V') is not None)
    if g.done and obj > 1e-6:
        ok, b = g.verify(y)
        if ok:
            import gzip; os.makedirs("logs/root_certs", exist_ok=True)
            yi = [int(round(v * 10 ** 6)) for v in y]
            json.dump({"model": "root", "class": ci, "job": job, "In": po["In"], "twe": [[a, b_, e] for (a, b_), e in twe.items()], "den": 10 ** 6,
                       "rows": [[repr(nm), g.rkind[r], g.rrhs[r], yi[r]] for r, nm in enumerate(g.rname) if yi[r]], "bounds": b},
                      gzip.open("logs/root_certs/root_%s_%d_h%s.json.gz" % (ci, job, hol), "wt"))
        print("ROOT %s job %d hol %s: INFEASIBLE slack %.4f exact %s %s %.0fs" % (ci, job, hol, obj, "VALID" if ok else "FAILED", b, time.time() - t0))
    else: print("ROOT %s job %d hol %s: %s obj %.5f %.0fs" % (ci, job, hol, "FEASIBLE" if g.done else "TIME CAP", obj, time.time() - t0))
