"""Etoiles : la refutation signee a chi fixe est-elle purement une affaire de PARITE ? (notes/19 §6)
(1) paire seule : signable (sbloc exact) <=> #{orbites « - » (e=1) avec chi_p = 1} pair ?  (verification exhaustive, 3436 chi_p)
(2) configuration Sigma : pour des chi tires du systeme non signe, systeme lineaire L(chi) sur F2 (parites de sbloc et sint) :
    coherent ou non, compare au verdict exact du systeme signe a chi fixe.
Usage : python parity_star.py "<paires>" <k>
"""
import itertools, sys, collections
import numpy as np
sys.path.insert(0, "scripts")
from pysat.solvers import Solver
import schi_system
from schi_system import s_at
from chi_system import ALLPAIRS, BLOCKS
from rs_experiments import idle

def rank_f2(M):
    M = M.copy() % 2; r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]: piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(rows):
            if i != r and M[i, c]: M[i] ^= M[r]
        r += 1
        if r == rows: break
    return r

def consistent(eqs, nvar):
    if not eqs: return True
    A = np.zeros((len(eqs), nvar + 1), dtype=np.uint8)
    for i, (vs, rhs) in enumerate(eqs):
        for v in vs: A[i, v] ^= 1
        A[i, nvar] = rhs
    return rank_f2(A[:, :nvar]) == rank_f2(A)

def L(E, chi):
    """chi : dict (p, W) -> 0/1.  Variables Z_p(W) numerotees."""
    E = [tuple(sorted(p)) for p in E]
    disj = lambda a, b: not (set(a) & set(b))
    O = {p: [(r, e) for r in ALLPAIRS if disj(r, p) for e in (0, 1)] for p in E}
    idx = {}; 
    for p in E:
        for W in O[p]: idx[p, W] = len(idx)
    eqs = []
    for p in E:
        for l in BLOCKS:
            if l in p: continue
            for e in (0, 1):
                Ws = [W for W in O[p] if l in W[0] and chi[p, W] == e]
                eqs.append(([idx[p, W] for W in Ws], sum(1 for W in Ws if s_at(W, l) == -1) % 2))
    for p, q in itertools.combinations(E, 2):
        if len(set(p) & set(q)) != 1: continue
        (i,) = set(p) & set(q)
        common = [W for W in O[p] if W in O[q]]
        for e in (0, 1):
            for f in (0, 1):
                k = 1 if s_at((p, e), i) * s_at((q, f), i) == -1 else 0
                Ws = [W for W in common if chi[p, W] == e and chi[q, W] == f]
                vs = [idx[p, W] for W in Ws] + [idx[q, W] for W in Ws]
                eqs.append((vs, k))            # exactement 1 parmi 3 => somme des (Z_p + Z_q) = k mod 2
    return eqs, len(idx)

if __name__ == "__main__":
    idle()
    E = [tuple(sorted((int(x[0]), int(x[1])))) for x in sys.argv[1].split()]
    k = int(sys.argv[2])
    cnf_u, pool_u, Xu, Zu = schi_system.build(E, signed=False)
    cnf_s, pool_s, Xs, Zs = schi_system.build(E, signed=True)
    keys = sorted(Xu)
    m = Solver(name="cadical195", bootstrap_with=cnf_u.clauses)
    sl = Solver(name="cadical195", bootstrap_with=cnf_s.clauses)
    tab = collections.Counter()
    for it in range(k):
        if not m.solve(): print("fin des chi apres", it); break
        val = set(l for l in m.get_model() if l > 0)
        chi = {key: int(Xu[key] in val) for key in keys}
        m.add_clause([-Xu[key] if chi[key] else Xu[key] for key in keys])
        eqs, n = L(E, chi)
        lin = consistent(eqs, n)
        exact = sl.solve(assumptions=[Xs[key] if chi[key] else -Xs[key] for key in keys])
        tab[(lin, exact)] += 1
    print("(L(chi) coherent, signe exact SAT) :", dict(tab))
