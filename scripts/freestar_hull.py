"""Enveloppe affine des matrices (iii) induites par les solutions de (i)+(ii) (note 22, cocycle a defauts).
On echantillonne des solutions de (i)+(ii) (cube A<part>, type tau), on calcule I_obs[b,d] = #{z : b in Phi(z), d in Phi(-z)}, puis on
teste si la cible T de (iii) est dans l'enveloppe affine des I_obs (sur Q, et modulo 2). Si non : un invariant lineaire separe."""
import sys, os, random, itertools, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_core_families import build_partial
from freestar_compact import types, far_roots, targets

def rank_q(M):
    return np.linalg.matrix_rank(np.array(M, dtype=float))
def rank2(rows):
    rows = [int("".join(str(int(x) % 2) for x in r), 2) for r in rows]; piv = []
    for r in rows:
        for p in piv:
            r = min(r, r ^ p)
        if r: piv.append(r)
    return len(piv)

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    from pysat.solvers import Solver
    part = tuple(int(c) for c in sys.argv[1]); i = int(sys.argv[2]); K = int(sys.argv[3])
    mu, reps, st = types(part); tau = reps[i]
    cnf = build_partial(mu, tau, "iii")
    Ws = far_roots(7); nW = len(Ws)
    pairs = [p for p in itertools.combinations(range(12), 2) if mu[p[0]] != p[1]]
    from pysat.formula import IDPool
    # retrouver les variables y : build_partial cree y[(w,h,p)] en premier dans l'IDPool, dans cet ordre
    yid = {}; k = 1
    for w in range(nW):
        for h in (0, 1):
            for p in pairs:
                yid[w, h, p] = k; k += 1
    Cx, T = targets(mu, tau, 12)
    s = Solver(name="cadical195", bootstrap_with=cnf.clauses)
    rng = random.Random(7); samples = []; t0 = time.time(); tries = 0
    while len(samples) < K and tries < 20 * K:
        tries += 1
        ass = [yid[rng.randrange(nW), rng.randrange(2), pairs[rng.randrange(len(pairs))]] for _ in range(4)]
        if not s.solve(assumptions=ass): continue
        val = set(l for l in s.get_model() if l > 0)
        phi = {}
        for w in range(nW):
            for h in (0, 1):
                phi[w, h] = [p for p in pairs if yid[w, h, p] in val][0]
        I = np.zeros((12, 12), dtype=int)
        for w in range(nW):
            for h in (0, 1):
                for b in phi[w, h]:
                    for d in phi[w, 1 - h]: I[b, d] += 1
        v = tuple(I.flatten())
        if v not in {tuple(x) for x in samples}: samples.append(np.array(v))
    S = np.array(samples); Tv = T.flatten()
    D = S[1:] - S[0]; DT = np.vstack([D, Tv - S[0]])
    rq, rqT = rank_q(D), rank_q(DT)
    r2, r2T = rank2([list(r) for r in D]), rank2([list(r) for r in DT])
    print("A%s tau#%d : %d solutions distinctes de (i)+(ii) en %.0f s (%d essais)" % (sys.argv[1], i, len(S), time.time() - t0, tries))
    print("  enveloppe affine sur Q : dim %d ; avec la cible : %d -> cible %s" % (rq, rqT, "DEDANS" if rq == rqT else "DEHORS"))
    print("  enveloppe affine mod 2 : dim %d ; avec la cible : %d -> cible %s" % (r2, r2T, "DEDANS" if r2 == r2T else "DEHORS"))
    # invariants lineaires : sommes constantes sur l'echantillon (ex. traces, sommes par ligne)
    diag = S[:, [b * 12 + b for b in range(12)]].sum(axis=1)
    print("  somme diagonale (orbites D) sur l'echantillon : min %d max %d ; cible %d" % (diag.min(), diag.max(), sum(T[b, b] for b in range(12))))
