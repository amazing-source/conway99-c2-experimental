"""Relaxation au niveau des BLOCS (signes oublies) du probleme local, type A111111/(2,2,2), avec le lemme d'equilibre (note 23 §8).
Chaque lointain z : jetons (fente, bloc) : x = blocs de z, + = blocs de Phi(z), r = blocs de Phi(-z).  Paire antipodale {z,-z} :
memes blocs x ; z : (+ : B+, r : Br), -z : (+ : Br, r : B+).  Contraintes (toutes DERIVEES de (ii), (iii), equilibre) :
 - 2 jetons exactement par quad (equilibre) ;
 - comptes par paire de jetons (s, beta), (s', beta') : somme de BB^T sur les blocs correspondants ;
 - Phi bijective : chaque paire de blocs est B+ pour exactement 4 lointains.
Reponse definitive par CP-SAT (petit modele) ; enumeration du nombre de solutions possible.
"""
import sys, os, itertools, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import types, targets
from far_spectrum_test import BBt
from ortools.sat.python import cp_model

def main(ti=0, T=600):
    mu, reps, st = types((1, 1, 1, 1, 1, 1)); tau = reps[ti]
    M = BBt(mu, tau)                      # 36 x 36 : classes x (0..11), + (12..23), r (24..35) ; r-jeton c <-> -c dans Phi(-z)
    blk = lambda y: y // 2
    # comptes par paires de jetons de blocs : slot s in {0:x,1:+,2:r}, bloc beta
    # jeton r d'un element d de Phi(-z) : sommet P_r de coordonnee c = -d, meme bloc
    cnt = collections.Counter()
    for u in range(36):
        for v in range(u + 1, 36):
            su, sv = u // 12, v // 12; bu, bv = blk(u % 12), blk(v % 12)
            key = tuple(sorted([(su, bu), (sv, bv)]))
            cnt[key] += int(M[u, v])
    # l'identite v != u compte chaque lointain adjacent a u et v ; par equilibre, dans un meme quad c'est le profil exact
    Zs = [(a, b) for a in range(12) for b in range(a + 1, 12) if blk(a) != blk(b)]
    antip = []
    seen = set()
    for z in Zs:
        if z in seen: continue
        mz = tuple(sorted((z[0] ^ 1, z[1] ^ 1))); seen.add(z); seen.add(mz); antip.append(z)
    BP = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    # quads : orbites de <s, tau> (mu = s) sur les blocs
    quad = {}
    for b in range(6):
        e = 2 * b; t = tau[e] // 2; quad[b] = min(b, t)
    m = cp_model.CpModel()
    y = {}
    for k, z in enumerate(antip):
        zb = (blk(z[0]), blk(z[1]))
        for p in range(15):
            for r in range(15):
                # equilibre : 2 jetons par quad (x : zb, + : BP[p], r : BP[r])
                c = collections.Counter(quad[b] for b in zb + BP[p] + BP[r])
                if any(v != 2 for v in c.values()) or len(c) != 3: continue
                y[k, p, r] = m.NewBoolVar("")
        m.AddExactlyOne(v for (kk, p, r), v in y.items() if kk == k)
    # bijectivite de Phi au niveau des blocs : chaque paire de blocs est B+ de 4 lointains (z et -z comptent : z donne p, -z donne r)
    for q in range(15):
        m.Add(sum(v for (k, p, r), v in y.items() if p == q) + sum(v for (k, p, r), v in y.items() if r == q) == 4)
    # comptes par paires de jetons
    contrib = collections.defaultdict(list)
    for (k, p, r), v in y.items():
        z = antip[k]; zb = (blk(z[0]), blk(z[1]))
        for (plus, rr) in ((BP[p], BP[r]), (BP[r], BP[p])):          # z puis -z
            toks = [(0, b) for b in zb] + [(1, b) for b in plus] + [(2, b) for b in rr]
            for t1, t2 in itertools.combinations(toks, 2):
                contrib[tuple(sorted([t1, t2]))].append(v)
    keys = set(cnt) | set(contrib)
    for key in keys:
        coeffs = collections.Counter(contrib.get(key, []))
        m.Add(sum(c * v for v, c in coeffs.items()) == cnt.get(key, 0))
    s = cp_model.CpSolver(); s.parameters.num_workers = 1; s.parameters.max_time_in_seconds = T
    r = s.Solve(m)
    print("A111111 tau#%d relaxation blocs+equilibre : %s (%.1f s), %d variables" % (ti, s.StatusName(r), s.WallTime(), len(y)), flush=True)

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
