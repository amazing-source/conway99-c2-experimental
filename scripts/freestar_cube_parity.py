"""Idee #6 (notes/20) : chasse de parite dans un cube de l'etoile libre, comme pour K13.
Cube A_1 (partition de 6) traduit au niveau Q (etage Q, lignes de star(1)) :
  paires du couplage A_1 : a = 1, donc Q >= 1 (X = 1) ;  autres paires internes a star(1) : a = 0, donc Q = b <= 1 (Y = 0) ;
  aucune paire {1,m} soeur (sigma exact vide).
On tire des solutions Q (cadical), et pour chacune on teste la coherence du systeme lineaire des parites de signes restreint aux
lignes de star(1) (freestar_parity_hunt.L_rows) ; on impose en plus a = 1 sur A_1 comme contrainte lineaire sur les signes
(a = 1 <=> Z = 0 sur une entree Q = 1 ; sur une entree Q = 2 rien a imposer).
Usage : python freestar_cube_parity.py <partition ex. 111111> <nb> <T_par_solution>
"""
import sys, time, itertools, multiprocessing as mp
import numpy as np
sys.path.insert(0, "scripts")
from rs_experiments import idle

def run(part, K, T, q):
    idle()
    from pysat.solvers import Solver
    import row_system
    from make_freestar_cubes import matching
    from freestar_parity_hunt import L_rows
    from sign_parity_system import gf2_rank
    M = 7
    outer = [(i, j, e) for i in range(1, M + 1) for j in range(i + 1, M + 1) for e in (0, 1)]
    N = len(outer)
    S = [U for U, (i, j, e) in enumerate(outer) if i == 1]
    cnf, pool = row_system.build(S, sigma=[])
    o, X, Y = row_system.base(M)[:3]
    Mt = matching(tuple(int(ch) for ch in part))
    orb = lambda m, e: outer.index((1, m, e))
    on = {frozenset((orb(m1, e1), orb(m2, e2))) for (m1, e1), (m2, e2) in Mt}
    for U, V in itertools.combinations(S, 2):
        if frozenset((U, V)) in on:
            cnf.append([X[U, V]])
        else:
            cnf.append([-Y[U, V]])
    s = Solver(name="cadical195", bootstrap_with=cnf.clauses)
    res = []
    for it in range(K):
        if not s.solve():
            res.append(("plus de solution", it)); break
        val = set(l for l in s.get_model() if l > 0)
        Q = {}
        for U in S:
            for V in range(N):
                if V != U:
                    Q[U, V] = (X[U, V] in val) + (Y[U, V] in val)
        Amat, b, names, keys = L_rows(Q, S)
        # a = 1 sur les paires de A_1 dont Q = 1  <=>  Z = 0
        extra = []
        for U, V in itertools.combinations(S, 2):
            if frozenset((U, V)) in on and Q[U, V] == 1:
                row = np.zeros(Amat.shape[1], dtype=np.uint8); row[keys.index((min(U, V), max(U, V)))] = 1
                extra.append(row)
        if extra:
            Amat = np.vstack([Amat] + extra); b = np.concatenate([b, np.zeros(len(extra), dtype=np.uint8)])
        rA = gf2_rank(Amat); rAb = gf2_rank(np.hstack([Amat, b[:, None]]))
        dD = sum(1 for U, V in itertools.combinations(S, 2) if Q[U, V] == 2)
        res.append(("coherent" if rA == rAb else "INCOHERENT", it, dD))
        s.add_clause([-X[U, V] if X[U, V] in val else X[U, V] for U in S for V in range(N) if V != U and (V not in S or U < V)])
    q.put(res)

if __name__ == "__main__":
    idle()
    part, K, T = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
    q = mp.Queue(); p = mp.Process(target=run, args=(part, K, T, q)); p.start(); p.join(T * K)
    if p.is_alive():
        p.terminate(); p.join(); print("cube A%s : TIMEOUT (pas de solution Q trouvee dans le temps imparti)" % part, flush=True)
    else:
        for r in q.get():
            print("cube A%s :" % part, r, flush=True)
