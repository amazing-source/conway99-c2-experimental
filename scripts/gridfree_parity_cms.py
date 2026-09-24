"""Coeur sans grille : RS(star(1)) (etage Q, lignes de star(1)), sans paire soeur, AVEC les 12 XOR de la parite des orbites « - »
(notes/19 §10), resolu par CryptoMiniSat (Gauss-Jordan) ; variante RSF(star(1)) + consequences XOR explicites de chaque cardinalite.
La parite « - » n'est pas une consequence de l'etage Q : c'est une vraie information nouvelle pour RS.
Usage : python gridfree_parity_cms.py <T> [rs|rsf]
"""
import sys, time, itertools
from collections import Counter
sys.path.insert(0, "scripts")
from pycryptosat import Solver
from rs_experiments import idle

def add_parity(s, lits, k):
    cnt = Counter(abs(l) for l in lits)
    rhs = (k + sum(1 for l in lits if l < 0)) % 2
    vs = [v for v, c in cnt.items() if c % 2]
    if vs:
        s.add_xor_clause(vs, bool(rhs))
    elif rhs:
        s.add_clause([])

if __name__ == "__main__":
    idle()
    T = float(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else "rs"
    outer = [(i, j, e) for i in range(1, 8) for j in range(i + 1, 8) for e in (0, 1)]
    S = [U for U, (i, j, e) in enumerate(outer) if i == 1]
    s = Solver(threads=1, time_limit=T)
    t0 = time.time()
    if mode == "rs":
        import row_system
        o, X, Y = row_system.base(7)[:3]
        cnf, pool = row_system.build(S, sigma=[])            # sigma=[] : aucune paire soeur parmi les paires de S (exact)
        s.add_clauses(cnf.clauses)
        # parite « - » : pour U dans S, sum_{V moins} [Q[U,V] = 1] pair ; [Q=1] = X xor Y (Y -> X)
        for U in S:
            lits = []
            for V in range(len(o)):
                if V != U and o[V][2] == 1:
                    lits += [X[U, V], Y[U, V]]
            add_parity(s, lits, 0)
        extra = len(S)
    else:
        import row_system_full
        from pysat.card import CardEnc, EncType
        clauses, nv, o, A, B = row_system_full.build(S, sigma=(), sigma_exact=True)
        s.add_clauses(clauses)
        # parites de chaque contrainte (I) : exactement n parmi L -> xor(L) = n mod 2
        rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in o]
        trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in o]
        inner = [(i, t) for i in range(1, 8) for t in (0, 1)]
        extra = 0
        for U in S:
            others = [V for V in range(len(o)) if V != U]
            for c in inner:
                partner = (c[0], 1 - c[1]); lits = []
                for V in others:
                    if c in rep[V]: lits.append(A[U, V])
                    if c in trep[V]: lits.append(B[U, V])
                add_parity(s, lits, 1 if (c in rep[U] or partner in rep[U]) else 2); extra += 1
    r, sol = s.solve()
    print("star(1) sans soeur, %s + %d XOR, CryptoMiniSat : %s (%.1f s)" % (mode.upper(), extra, {True: "SAT", False: "UNSAT", None: "TIMEOUT"}[r], time.time() - t0), flush=True)
