"""Relaxation de PARITE du modele complet (notes/20) : toutes les cardinalites de orbit_sat remplacees par leur parite.
Sur F2, avec X la matrice d'adjacence (inconnue) entre racines, c'est exactement :
    X^2 + X = K  (K[u,v] = |u cap v| mod 2, connue, fixee par les etiquettes D_m)   et   X E = E B  (contraintes (I) mod 2),
plus (D) mod 2 (nombre impair de V avec a = b = 1) et (R) mod 2 (degre pair).
Encodage : variables a[U,V], b[U,V] ; produits definis en CNF (ET) ; chaque equation = une clause XOR native (CryptoMiniSat, Gauss).
Controles : m = 2 (Paley(9), doit etre SAT), m = 3 (le vrai probleme n'a pas de solution ; la relaxation ?), puis m = 7.
Usage : python f2_relaxation.py <m> <T> [exactD]
  exactD : garde (D) exacte (un seul V avec a = b = 1) au lieu de sa parite.
"""
import sys, time, itertools
sys.path.insert(0, "scripts")
from pycryptosat import Solver
from pysat.formula import IDPool
from pysat.card import CardEnc, EncType

def build(m, exactD=False):
    k = 2 * m
    outer = [(i, j, e) for i in range(1, m + 1) for j in range(i + 1, m + 1) for e in (0, 1)]
    N = len(outer)
    rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
    trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
    pool = IDPool(); clauses = []; xors = []
    A = {}; B = {}
    for U in range(N):
        for V in range(U + 1, N):
            A[U, V] = A[V, U] = pool.id(("a", U, V)); B[U, V] = B[V, U] = pool.id(("b", U, V))
    prods = {}
    def prod(x, y):
        key = (min(x, y), max(x, y))
        if key not in prods:
            p = pool.id(("p",) + key); clauses.extend([[-p, x], [-p, y], [p, -x, -y]]); prods[key] = p
        return prods[key]
    def xor(vs, rhs):
        cnt = {}
        for v in vs:
            cnt[v] = cnt.get(v, 0) ^ 1
        vs2 = [v for v, c in cnt.items() if c]
        if vs2:
            xors.append((vs2, rhs % 2))
        elif rhs % 2:
            clauses.append([])
    inner = [(i, s) for i in range(1, m + 1) for s in (0, 1)]
    for U in range(N):
        others = [V for V in range(N) if V != U]
        xor([A[U, V] for V in others] + [B[U, V] for V in others], k - 2)                     # (R) mod 2
        ds = [prod(A[U, V], B[U, V]) for V in others]
        if exactD:
            clauses.extend(CardEnc.equals(lits=ds, bound=1, vpool=pool, encoding=EncType.seqcounter).clauses)
        else:
            xor(ds, 1)                                                                       # (D) mod 2
        for c in inner:                                                                      # (I) mod 2
            partner = (c[0], 1 - c[1]); lits = []
            for V in others:
                if c in rep[V]: lits.append(A[U, V])
                if c in trep[V]: lits.append(B[U, V])
            xor(lits, 1 if (c in rep[U] or partner in rep[U]) else 2)
    for U in range(N):                                                                       # (P) mod 2
        for V in range(U + 1, N):
            Ws = [W for W in range(N) if W != U and W != V]
            same = [prod(A[U, W], A[V, W]) for W in Ws] + [prod(B[U, W], B[V, W]) for W in Ws]
            cross = [prod(A[U, W], B[V, W]) for W in Ws] + [prod(B[U, W], A[V, W]) for W in Ws]
            xor(same + [A[U, V]], 2 - len(rep[U] & rep[V]))
            xor(cross + [B[U, V]], 2 - len(rep[U] & trep[V]))
    return clauses, xors, pool, outer, A, B

if __name__ == "__main__":
    sys.path.insert(0, "scripts")
    from rs_experiments import idle
    idle()
    m = int(sys.argv[1]); T = float(sys.argv[2]); exactD = "exactD" in sys.argv[3:]
    t0 = time.time()
    clauses, xors, pool, outer, A, B = build(m, exactD)
    s = Solver(threads=1, time_limit=T)
    s.add_clauses(clauses)
    for vs, rhs in xors:
        s.add_xor_clause(vs, bool(rhs))
    tb = time.time() - t0
    r, sol = s.solve()
    print("m=%d relaxation de parite%s : %d variables, %d clauses (ET), %d XOR ; construction %.1f s ; %s en %.1f s"
          % (m, " (D exacte)" if exactD else "", pool.top, len(clauses), len(xors), tb,
             {True: "SAT", False: "UNSAT", None: "TIMEOUT"}[r], time.time() - t0 - tb), flush=True)
