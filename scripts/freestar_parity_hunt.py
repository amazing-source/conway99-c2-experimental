"""Chasse au « lemme de l'etoile libre » (notes/20) — meme methode que pour le lemme des etoiles.

1. On tire des solutions Q (etage Q, lignes de star(c) seulement, AUCUNE paire soeur parmi les paires {c,m}) : RS(star(c)).
2. Pour chaque Q (lignes de star(c) fixees), les parites des contraintes (I) de ces lignes et des equations (P) « cross » ENTRE ces
   lignes sont LINEAIRES en les signes Z[U,V] (U dans star(c), Q[U,V] = 1) : systeme L(Q) sur F2.
3. Si L(Q) est incoherent pour tous les Q tires (comme pour K13 a chi fixe), on extrait des certificats et on cherche leur partie
   independante de Q.
Usage : python freestar_parity_hunt.py <c> <nb_solutions> <T_premiere_solution>
"""
import sys, time, itertools
import numpy as np
sys.path.insert(0, "scripts")
from pysat.solvers import Solver
import row_system
from rs_experiments import idle
from sign_parity_system import gf2_rank

M = 7
outer = [(i, j, e) for i in range(1, M + 1) for j in range(i + 1, M + 1) for e in (0, 1)]
N = len(outer)
rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
inner = [(i, s) for i in range(1, M + 1) for s in (0, 1)]

def L_rows(Q, S):
    """Systeme de parite des signes restreint aux lignes de S (Q : dict (U,V) -> 0/1/2 pour U dans S). Variables : paires {U,V}
    avec U ou V dans S et Q = 1.  Equations : (I)(U,c) pour U dans S ; cross(U,V) pour U,V dans S (termes W quelconques : Z_UW + Z_VW)."""
    S = sorted(S); Sset = set(S)
    def q(U, V):
        if U in Sset: return Q[U, V]
        if V in Sset: return Q[V, U]
        return None
    keys = sorted({(min(U, V), max(U, V)) for U in S for V in range(N) if V != U and q(U, V) == 1})
    vid = {kk: t for t, kk in enumerate(keys)}
    z = lambda U, V: vid[(min(U, V), max(U, V))]
    rows = []; rhs = []; names = []
    for U in S:
        for c in inner:
            row = np.zeros(len(keys), dtype=np.uint8); const = 0
            target = 1 if (c in rep[U] or (c[0], 1 - c[1]) in rep[U]) else 2
            for V in range(N):
                if V == U: continue
                qq = q(U, V)
                if qq == 2:
                    const += (c in rep[V]) + (c in trep[V])
                elif qq == 1:
                    if (c in rep[V]) != (c in trep[V]):
                        const += (c in rep[V]); row[z(U, V)] ^= 1
                    else:
                        const += (c in rep[V])
            rows.append(row); rhs.append((target - const) % 2); names.append(("I", U, c))
    for U, V in itertools.combinations(S, 2):
        row = np.zeros(len(keys), dtype=np.uint8); const = 0
        for W in range(N):
            if W in (U, V): continue
            qu, qv = Q[U, W], Q[V, W]
            if qu == 0 or qv == 0: continue
            if qu == 2 and qv == 2: const += 2
            elif qu == 2 or qv == 2: const += 1
            else:
                row[z(U, W)] ^= 1; row[z(V, W)] ^= 1
        if Q[U, V] == 2: const += 1
        elif Q[U, V] == 1: row[z(U, V)] ^= 1
        target = 2 - len(rep[U] & trep[V])
        rows.append(row); rhs.append((target - const) % 2); names.append(("X", U, V))
    return np.array(rows, dtype=np.uint8), np.array(rhs, dtype=np.uint8), names, keys

if __name__ == "__main__":
    idle()
    c, K, T0 = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    S = [U for U, (i, j, e) in enumerate(outer) if c in (i, j)]
    cnf, pool = row_system.build(S, sigma=[])            # aucune paire soeur parmi les paires {c,m}
    o, X, Y = row_system.base(M)[:3]
    s = Solver(name="cadical195", bootstrap_with=cnf.clauses)
    stats = {"coherent": 0, "INCOHERENT": 0}
    t0 = time.time()
    for it in range(K):
        ok = s.solve()
        if not ok:
            print("plus de solution Q apres", it); break
        val = set(l for l in s.get_model() if l > 0)
        Q = {}
        for U in S:
            for V in range(N):
                if V != U:
                    Q[U, V] = (X[U, V] in val) + (Y[U, V] in val)
        Amat, b, names, keys = L_rows(Q, S)
        rA = gf2_rank(Amat); rAb = gf2_rank(np.hstack([Amat, b[:, None]]))
        verdict = "coherent" if rA == rAb else "INCOHERENT"
        stats[verdict] += 1
        dD = sum(1 for (U, V) in itertools.combinations(S, 2) if Q[U, V] == 2)
        print("Q #%d (%.0f s) : %d eq., %d signes, rang %d/%d -> %s ; aretes D internes a star(%d) : %d"
              % (it, time.time() - t0, Amat.shape[0], Amat.shape[1], rA, rAb, verdict, c, dD), flush=True)
        # bloquer cette solution (sur les entrees Q des lignes de S)
        s.add_clause([-(X[U, V]) if X[U, V] in val else X[U, V] for U in S for V in range(N) if V != U and U < V or (V not in S and V != U)])
    print("bilan :", stats)
