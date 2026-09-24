"""Certificats d'incoherence de L(chi) pour une etoile (notes/19 §6) : quelles equations de parite se combinent en 0 = 1 ?
Pour k chi tires du systeme non signe : sous-ensemble minimal (par suppression) d'equations de L(chi) encore incoherent ;
on affiche les familles (sbloc(p,l,eps), sint(p,q,e,f)) utilisees.
Usage : python parity_cert.py "<paires>" <k>
"""
import itertools, sys, collections
import numpy as np
sys.path.insert(0, "scripts")
from pysat.solvers import Solver
import schi_system
from schi_system import s_at
from chi_system import ALLPAIRS, BLOCKS
from parity_star import rank_f2
from rs_experiments import idle

def L_named(E, chi):
    E = [tuple(sorted(p)) for p in E]
    disj = lambda a, b: not (set(a) & set(b))
    O = {p: [(r, e) for r in ALLPAIRS if disj(r, p) for e in (0, 1)] for p in E}
    idx = {}
    for p in E:
        for W in O[p]: idx[p, W] = len(idx)
    eqs = []
    nm = lambda p: "%d%d" % p
    for p in E:
        for l in BLOCKS:
            if l in p: continue
            for e in (0, 1):
                Ws = [W for W in O[p] if l in W[0] and chi[p, W] == e]
                eqs.append(("sbloc(%s,%d,%d)" % (nm(p), l, e), [idx[p, W] for W in Ws], sum(1 for W in Ws if s_at(W, l) == -1) % 2))
    for p, q in itertools.combinations(E, 2):
        if len(set(p) & set(q)) != 1: continue
        (i,) = set(p) & set(q)
        common = [W for W in O[p] if W in O[q]]
        for e in (0, 1):
            for f in (0, 1):
                k = 1 if s_at((p, e), i) * s_at((q, f), i) == -1 else 0
                Ws = [W for W in common if chi[p, W] == e and chi[q, W] == f]
                eqs.append(("sint(%s,%s,%d,%d)" % (nm(p), nm(q), e, f), [idx[p, W] for W in Ws] + [idx[q, W] for W in Ws], k))
    return eqs, len(idx)

def incons(eqs, n):
    A = np.zeros((len(eqs), n + 1), dtype=np.uint8)
    for i, (_, vs, rhs) in enumerate(eqs):
        for v in vs: A[i, v] ^= 1
        A[i, n] = rhs
    return rank_f2(A[:, :n]) < rank_f2(A)

if __name__ == "__main__":
    idle()
    E = [tuple(sorted((int(x[0]), int(x[1])))) for x in sys.argv[1].split()]
    k = int(sys.argv[2])
    cnf_u, pool_u, Xu, Zu = schi_system.build(E, signed=False)
    keys = sorted(Xu)
    m = Solver(name="cadical195", bootstrap_with=cnf_u.clauses)
    pat = collections.Counter()
    for it in range(k):
        if not m.solve(): break
        val = set(l for l in m.get_model() if l > 0)
        chi = {key: int(Xu[key] in val) for key in keys}
        m.add_clause([-Xu[key] if chi[key] else Xu[key] for key in keys])
        eqs, n = L_named(E, chi)
        if not incons(eqs, n):
            print("chi #%d : L coherent" % it); continue
        cur = list(eqs); i = 0
        while i < len(cur):
            t = cur[:i] + cur[i + 1:]
            if incons(t, n): cur = t
            else: i += 1
        fam = tuple(sorted(collections.Counter(e[0].split("(")[0] for e in cur).items()))
        pat[fam] += 1
        if it < 6:
            print("chi #%d : certificat minimal de %d equations : %s" % (it, len(cur), " ".join(e[0] for e in cur)), flush=True)
    print("familles des certificats :", dict(pat))
