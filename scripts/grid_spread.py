"""Ansatz « partition en 11 grilles » pour srg(99,14,1,2) (theoreme reve 4, notes/12).
Si V = Lambda_0 u ... u Lambda_10 (grilles K3xK3 disjointes), G1 (code parfait) force : entre deux grilles, un couplage parfait.
Variables m[i,j,g,h] (i<j) : (i,g) ~ (j,h).  Contraintes srg, pour chaque paire i<j et chaque (g,h) :
    L + R + common + m = 2,   L = [pi_ji(h) ~ g], R = [pi_ij(g) ~ h], common = #{k : pi_ik(g) = pi_jk(h)}
(m=1 : lambda = 1 ; m=0 : mu = 2 ; les paires internes a une grille sont automatiquement correctes).
UNSAT => aucun srg(99,14,1,2) n'admet de partition en grilles (non certifie).  Mono-fil, delai dur.
"""
import sys, time, itertools, multiprocessing as mp

def worker(q):
    from pysat.formula import CNF, IDPool
    from pysat.card import CardEnc, EncType
    from pysat.solvers import Solver
    G = 11
    P = [(a, b) for a in range(3) for b in range(3)]
    nb = {g: [h for h in range(9) if (P[g][0] == P[h][0]) != (P[g][1] == P[h][1])] for g in range(9)}
    pool = IDPool(); cnf = CNF()
    def m(i, j, g, h):
        return pool.id(("m", i, j, g, h)) if i < j else pool.id(("m", j, i, h, g))
    def card_eq(lits, k):
        cnf.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    for i, j in itertools.combinations(range(G), 2):
        for g in range(9):
            card_eq([m(i, j, g, h) for h in range(9)], 1)
            card_eq([m(i, j, h, g) for h in range(9)], 1)
    def AND(a, b):
        z = pool.id(("and", a, b)); cnf.extend([[-z, a], [-z, b], [z, -a, -b]]); return z
    for i, j in itertools.combinations(range(G), 2):
        for g in range(9):
            for h in range(9):
                L = [m(i, j, gp, h) for gp in nb[g]]
                R = [m(i, j, g, hp) for hp in nb[h]]
                C = [AND(m(i, k, g, f), m(j, k, h, f)) for k in range(G) if k not in (i, j) for f in range(9)]
                card_eq(L + R + C + [m(i, j, g, h)], 2)
    # brisure de symetrie legere : Aut(K3xK3) transitif -> pi_01(0) = 0
    cnf.append([m(0, 1, 0, 0)])
    t0 = time.time()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as sv:
        r = sv.solve()
        q.put(("SAT" if r else "UNSAT", round(time.time() - t0, 1), pool.top, len(cnf.clauses)))

if __name__ == "__main__":
    T = float(sys.argv[1]) if len(sys.argv) > 1 else 300
    q = mp.Queue(); p = mp.Process(target=worker, args=(q,)); p.start(); p.join(T)
    if p.is_alive():
        p.terminate(); p.join(); print("partition en grilles : TIMEOUT %.0f s" % T, flush=True)
    else:
        print("partition en grilles :", q.get(), flush=True)
