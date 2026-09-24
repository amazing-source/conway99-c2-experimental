"""Propagateur de Gauss sur les parites bilineaires du modele d'orbites (notes/22 §5, piste « parite rendue lineaire », IDEES I-35).

Les consequences modulo 2 du modele complet restreint aux lignes S sont :
  (R)  sum_V (a_UV + b_UV) = 0                                   (degre 12 pair)
  (D)  sum_V a_UV b_UV = 1                                       (un seul partenaire D)
  (I)  sum_V a_UV [c in rep V] + b_UV [c in trep V] = cible(c)   (lineaire)
  (P=) sum_W (a_UW a_VW + b_UW b_VW) + a_UV = 2 - |rep U ∩ rep V|
  (Px) sum_W (a_UW b_VW + b_UW a_VW) + b_UV = 2 - |rep U ∩ trep V|
Chaque contrainte est bilineaire. Des qu'un facteur de chaque produit est affecte, elle devient lineaire en les variables libres.
Le propagateur (IPASIR-UP, CaDiCaL 1.9.5 via pysat) linearise sous l'affectation courante, fait une elimination de Gauss-Jordan
en suivant les combinaisons de contraintes, et renvoie :
  - un conflit : clause falsifiee = negation des affectations utilisees par la combinaison ;
  - des implications : literal + raison (meme construction).
Correction : toutes ces contraintes sont des consequences du CNF, donc l'ajout est sain (il ne coupe aucune solution).
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from pysat.engines import Propagator

def parity_constraints(S, A, B, outer, m=7):
    """Contraintes modulo 2 pour les lignes S (liste de (monomes, rhs)) ; monome = (v,) ou (v, w)."""
    N = len(outer)
    rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
    trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
    inner = [(i, s) for i in range(1, m + 1) for s in (0, 1)]
    S = sorted(set(S)); cons = []
    for U in S:
        others = [V for V in range(N) if V != U]
        cons.append(([(A[U, V],) for V in others] + [(B[U, V],) for V in others], (2 * m - 2) % 2))
        cons.append(([(A[U, V], B[U, V]) for V in others], 1))
        for c in inner:
            partner = (c[0], 1 - c[1]); mons = []
            for V in others:
                if c in rep[V]: mons.append((A[U, V],))
                if c in trep[V]: mons.append((B[U, V],))
            cons.append((mons, (1 if (c in rep[U] or partner in rep[U]) else 2) % 2))
    for x in range(len(S)):
        for y in range(x + 1, len(S)):
            U, V = S[x], S[y]
            Ws = [W for W in range(N) if W != U and W != V]
            same = [(A[U, W], A[V, W]) for W in Ws] + [(B[U, W], B[V, W]) for W in Ws] + [(A[U, V],)]
            cross = [(A[U, W], B[V, W]) for W in Ws] + [(B[U, W], A[V, W]) for W in Ws] + [(B[U, V],)]
            cons.append((same, (2 - len(rep[U] & rep[V])) % 2))
            cons.append((cross, (2 - len(rep[U] & trep[V])) % 2))
    return cons

class GaussBilinear(Propagator):
    def __init__(self, cons):
        super().__init__()
        self.cons = cons
        self.vars = sorted({v for mons, _ in cons for mon in mons for v in mon})
        self.val = {}; self.trail = []; self.levels = []
        self.reasons = {}; self.pending = None
        self.stats = {"propagate": 0, "conflits": 0, "implications": 0}
        self.by_var = {}
        for ci, (mons, _) in enumerate(cons):
            for mon in mons:
                for v in mon: self.by_var.setdefault(v, set()).add(ci)

    # --- suivi de l'affectation
    def on_assignment(self, lit, fixed=False):
        v = abs(lit)
        if v not in self.val:
            self.val[v] = 1 if lit > 0 else 0; self.trail.append(v)
    def on_new_level(self):
        self.levels.append(len(self.trail))
    def on_backtrack(self, to):
        if to < len(self.levels):
            keep = self.levels[to]
            for v in self.trail[keep:]: del self.val[v]
            del self.trail[keep:]; del self.levels[to:]
        self.pending = None

    # --- linearisation et Gauss
    def _system(self):
        rows = []                      # (bits sur variables libres, constante, dependances (set de variables affectees))
        val = self.val
        for mons, rhs in self.cons:
            bits = 0; const = rhs; deps = set(); ok = True
            for mon in mons:
                if len(mon) == 1:
                    v = mon[0]
                    if v in val: const ^= val[v]; deps.add(v)
                    else: bits ^= 1 << v
                else:
                    v, w = mon
                    iv, iw = v in val, w in val
                    if iv and iw:
                        const ^= val[v] & val[w]; deps.add(v); deps.add(w)
                    elif iv:
                        deps.add(v)
                        if val[v]: bits ^= 1 << w
                    elif iw:
                        deps.add(w)
                        if val[w]: bits ^= 1 << v
                    else:
                        ok = False; break
            if ok:
                rows.append([bits, const, deps])
        return rows

    def _clause_from(self, deps, lit=None):
        cl = [(-v if self.val[v] else v) for v in deps]
        if lit is not None: cl = [lit] + cl
        return cl

    def propagate(self):
        self.stats["propagate"] += 1
        rows = self._system()
        # elimination de Gauss-Jordan, dependances = union des lignes combinees
        piv = {}
        order = []
        for r in rows:
            bits, const, deps = r[0], r[1], set(r[2])
            for p in order:
                if bits >> p & 1:
                    pb, pc, pd = piv[p]
                    bits ^= pb; const ^= pc; deps |= pd
            if bits == 0:
                if const:
                    self.stats["conflits"] += 1
                    self.pending = self._clause_from(deps)
                    return []
                continue
            p = bits.bit_length() - 1
            for q in order:                       # reduction des pivots existants (Gauss-Jordan)
                qb, qc, qd = piv[q]
                if qb >> p & 1:
                    piv[q] = (qb ^ bits, qc ^ const, qd | deps)
            piv[p] = (bits, const, deps); order.append(p)
        out = []
        for p in order:
            bits, const, deps = piv[p]
            if bits & (bits - 1) == 0:            # une seule variable libre
                v = p; lit = v if const else -v
                if v not in self.val:
                    self.reasons[lit] = self._clause_from(deps, lit)
                    out.append(lit); self.stats["implications"] += 1
        return out

    def provide_reason(self, lit):
        return self.reasons[lit]
    def check_model(self, model):
        val = {abs(l): (1 if l > 0 else 0) for l in model}
        for mons, rhs in self.cons:
            s = 0
            for mon in mons:
                t = 1
                for v in mon: t &= val.get(v, 0)
                s ^= t
            if s != rhs:
                return False
        return True
    def has_clause(self):
        return self.pending is not None
    def add_clause(self):
        cl = self.pending; self.pending = None
        return cl if cl is not None else []

def solve_with_gauss(clauses, S, A, B, outer, T):
    import threading
    from pysat.solvers import Solver
    cons = parity_constraints(S, A, B, outer)
    prop = GaussBilinear(cons)
    s = Solver(name="cadical195", bootstrap_with=clauses)
    s.connect_propagator(prop)
    for v in prop.vars: s.observe(v)
    t0 = time.time(); r = s.solve(); dt = time.time() - t0
    model = s.get_model() if r else None
    ok_model = prop.check_model(model) if r else None
    return r, round(dt, 1), prop.stats, len(cons), ok_model

def child(E, q):
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    import row_system_full as R
    from rs_experiments import sister_orbits
    cl, nv, outer, A, B = R.build(sister_orbits(E), sigma=E)
    q.put(solve_with_gauss(cl, sister_orbits(E), A, B, outer, None))

if __name__ == "__main__":
    import multiprocessing as mp
    tests = {"K13": [(1, 2), (1, 3), (1, 4)], "K2": [(1, 2)], "2K2": [(1, 2), (3, 4)]}
    which = sys.argv[1]; T = float(sys.argv[2])
    q = mp.Queue(); p = mp.Process(target=child, args=(tests[which], q)); p.start(); p.join(T)
    if p.is_alive():
        p.terminate(); p.join(); print("%s (lignes soeurs, cadical + Gauss) : TIMEOUT %.0f s" % (which, T))
    else:
        r, dt, stats, nc, okm = q.get(timeout=10)
        print("%s (lignes soeurs, cadical + Gauss) : %s en %s s ; %d contraintes de parite ; stats %s ; modele verifie : %s"
              % (which, "SAT" if r else "UNSAT", dt, nc, stats, okm))

# ---------------------------------------------------------------- version (q, b) : q = a xor b (parite de Q), b = signe
# Modulo 2 : a_U b_V + b_U a_V = q_U b_V + q_V b_U ;  a_U a_V + b_U b_V = q_U q_V + q_U b_V + q_V b_U ;  a b = q b + b.
# Aucun terme b.b : a q fixes, tout est lineaire en les signes b (c'est L(Q), note 19). On branche d'abord sur les q (decide).
def qb_constraints(S, A, B, outer, pool, m=7):
    """Renvoie (clauses definissant q = a xor b, contraintes en (q, b), liste des q)."""
    N = len(outer)
    rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
    trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
    inner = [(i, s) for i in range(1, m + 1) for s in (0, 1)]
    S = sorted(set(S)); Sset = set(S)
    qv = {}; clauses = []
    def q(U, W):
        key = (min(U, W), max(U, W))
        if key not in qv:
            x = pool.id(("q",) + key); a, b = A[U, W], B[U, W]; qv[key] = x
            clauses.extend([[-x, a, b], [-x, -a, -b], [x, -a, b], [x, a, -b]])
        return qv[key]
    cons = []
    for U in S:
        others = [V for V in range(N) if V != U]
        cons.append(([(q(U, V),) for V in others], (2 * m - 2) % 2))                          # (R)
        cons.append(([(q(U, V), B[U, V]) for V in others] + [(B[U, V],) for V in others], 1))  # (D)
        for c in inner:                                                                       # (I)
            partner = (c[0], 1 - c[1]); mons = []
            for V in others:
                if c in rep[V]: mons += [(q(U, V),), (B[U, V],)]
                if c in trep[V]: mons.append((B[U, V],))
            cons.append((mons, (1 if (c in rep[U] or partner in rep[U]) else 2) % 2))
    for x_ in range(len(S)):
        for y_ in range(x_ + 1, len(S)):
            U, V = S[x_], S[y_]
            Ws = [W for W in range(N) if W != U and W != V]
            same = [(q(U, W), q(V, W)) for W in Ws] + [(q(U, W), B[V, W]) for W in Ws] + [(q(V, W), B[U, W]) for W in Ws] \
                + [(q(U, V),), (B[U, V],)]
            cross = [(q(U, W), B[V, W]) for W in Ws] + [(q(V, W), B[U, W]) for W in Ws] + [(B[U, V],)]
            cons.append((same, (2 - len(rep[U] & rep[V])) % 2))
            cons.append((cross, (2 - len(rep[U] & trep[V])) % 2))
    return clauses, cons, sorted(qv.values())

class GaussQB(GaussBilinear):
    """Meme moteur de Gauss ; en plus, decide() branche d'abord sur les q libres (niveau Q), polarite q = 0."""
    def __init__(self, cons, qvars):
        super().__init__(cons)
        self.qvars = qvars
    def decide(self):
        for x in self.qvars:
            if x not in self.val:
                return -x
        return 0

def solve_qb(clauses, S, A, B, outer, nv, branch_q=True):
    from pysat.formula import IDPool
    from pysat.solvers import Solver
    pool = IDPool(start_from=nv + 1)
    qcl, cons, qvars = qb_constraints(S, A, B, outer, pool)
    prop = GaussQB(cons, qvars) if branch_q else GaussBilinear(cons)
    s = Solver(name="cadical195", bootstrap_with=clauses + qcl)
    s.connect_propagator(prop)
    for v in prop.vars: s.observe(v)
    t0 = time.time(); r = s.solve(); dt = time.time() - t0
    okm = prop.check_model(s.get_model()) if r else None
    return r, round(dt, 1), prop.stats, len(cons), okm

def child_qb(E, facts, q):
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    import row_system_full as R
    from rs_experiments import sister_orbits
    if facts:
        from k13_facts_gauss import build
        cl, S, A, B, outer = build(); nv = max(abs(l) for c in cl for l in c)
    else:
        cl, nv, outer, A, B = R.build(sister_orbits(E), sigma=E); S = sister_orbits(E)
    q.put(solve_qb(cl, S, A, B, outer, nv))

def run_qb(name, E, facts, T):
    import multiprocessing as mp
    q = mp.Queue(); p = mp.Process(target=child_qb, args=(E, facts, q)); p.start(); p.join(T)
    if p.is_alive():
        p.terminate(); p.join(); print("%s (q,b + Gauss, branche Q) : TIMEOUT %.0f s" % (name, T)); return
    r, dt, stats, nc, okm = q.get(timeout=10)
    print("%s (q,b + Gauss, branche Q) : %s en %s s ; %d contraintes ; stats %s ; modele verifie : %s"
          % (name, "SAT" if r else "UNSAT", dt, nc, stats, okm), flush=True)
