"""Systeme de parite INDEPENDANT de chi (notes/19 §6) : (L1) pour toute paire soeur p et tout bloc l hors p,
(L2) pour toute paire de paires soeurs secantes, (L3) pour toute paire de paires soeurs disjointes.
  (L1) sum_{W in O_p, W contient l} Z_p(W) = sum_{W in O_p, W contient l} z_l(W)          [somme de (sbloc)(p,l,0) et (p,l,1)]
  (L2) sum_{W in O_p cap O_q} (Z_p(W) + Z_q(W)) = 0                                        [somme des 4 (sint)(p,q,e,f)]
  (L3) sum_{W sur les 3 blocs restants} (Z_p(W) + Z_q(W)) + Z_q(U_p^0) + Z_q(U_p^1) = 0     [somme des 2 (sdisj)(p,q,eps)]
Chaque equation est une consequence exacte du systeme signe (qui contient (bloc), (int), (disj) non signes).
Si ce systeme lineaire sur F2 est incoherent, Sigma (au moins) est impossible, avec un certificat lisible a la main.
Usage : python parity_L12.py "<paires>" [...]
"""
import itertools, sys
import numpy as np
sys.path.insert(0, "scripts")
from schi_system import s_at
from chi_system import ALLPAIRS, BLOCKS
from parity_star import rank_f2

def system(E, use=("L1", "L2", "L3", "L4")):
    E = [tuple(sorted(p)) for p in E]
    disj = lambda a, b: not (set(a) & set(b))
    O = {p: [(r, e) for r in ALLPAIRS if disj(r, p) for e in (0, 1)] for p in E}
    idx = {}
    for p in E:
        for W in O[p]: idx[p, W] = len(idx)
    eqs = []; nm = lambda p: "%d%d" % p
    if "L1" in use:
        for p in E:
            for l in BLOCKS:
                if l in p: continue
                Ws = [W for W in O[p] if l in W[0]]
                eqs.append(("L1(%s,%d)" % (nm(p), l), [idx[p, W] for W in Ws], sum(1 for W in Ws if s_at(W, l) == -1) % 2))
    for p, q in itertools.combinations(E, 2):
        common = [W for W in O[p] if W in O[q]]
        if len(set(p) & set(q)) == 1 and "L2" in use:
            eqs.append(("L2(%s,%s)" % (nm(p), nm(q)), [idx[p, W] for W in common] + [idx[q, W] for W in common], 0))
        if disj(p, q) and "L3" in use:
            eqs.append(("L3(%s,%s)" % (nm(p), nm(q)), [idx[p, W] for W in common] + [idx[q, W] for W in common] + [idx[q, (p, 0)], idx[q, (p, 1)]], 0))
        if disj(p, q) and "L4" in use:
            # (sbij) : si chi_p(U_q^f) = e alors Z_p(U_q^f) = Z_q(U_p^e) ; la bijection apparie les deux orbites de q avec celles de p,
            # donc, en sommant : Z_p(U_q^0) + Z_p(U_q^1) = Z_q(U_p^0) + Z_q(U_p^1)   (independant de chi)
            eqs.append(("L4(%s,%s)" % (nm(p), nm(q)), [idx[p, (q, 0)], idx[p, (q, 1)], idx[q, (p, 0)], idx[q, (p, 1)]], 0))
    return eqs, len(idx)

def incons(eqs, n):
    A = np.zeros((len(eqs), n + 1), dtype=np.uint8)
    for i, (_, vs, rhs) in enumerate(eqs):
        for v in vs: A[i, v] ^= 1
        A[i, n] = rhs
    return rank_f2(A[:, :n]) < rank_f2(A)

def min_cert(eqs, n):
    cur = list(eqs); i = 0
    while i < len(cur):
        t = cur[:i] + cur[i + 1:]
        if incons(t, n): cur = t
        else: i += 1
    return cur

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        E = [tuple(sorted((int(x[0]), int(x[1])))) for x in arg.split()]
        eqs, n = system(E)
        bad = incons(eqs, n)
        print("%-26s L1..L4 : %s (%d equations, %d variables)" % (arg, "INCOHERENT" if bad else "coherent", len(eqs), n), flush=True)
        if bad:
            print("    certificat minimal :", " ".join(e[0] for e in min_cert(eqs, n)))
