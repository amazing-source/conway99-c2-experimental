"""Decoupage SAIN du CNF fsos (make_freestar_sos_cnf.py) en cubes, par symetrie.
Le PROBLEME (pas l'encodage) est invariant par G = Stab(mu, tau) dans B_6 : cibles (ii), (iii), orbites d'equilibre, (iv), (v)
sont definies a partir de mu, tau, sigma seulement.  Donc si une solution Phi existe, g.Phi en est une pour tout g dans G, et pour
la paire antipodale k0 choisie, l'option de g.Phi en k0 parcourt toute l'orbite (sous Stab_G(k0)) de l'option de Phi.
Cubes = CNF + clause unitaire y[k0, o] pour o parcourant des representants des orbites des options de k0 sous Stab_G(k0).
Si tous les cubes sont UNSAT, il n'y a pas de solution.
Usage : python make_fsos_cubes.py <tau_index> <k0>
"""
import sys, os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import types
from freestar_ansatz import stab
import make_freestar_sos_cnf as M

if __name__ == "__main__":
    ti = int(sys.argv[1]); k0 = int(sys.argv[2])
    mu, reps, st = types((1, 1, 1, 1, 1, 1)); tau = reps[ti]
    cnf, Y, opts, zreps, P = M.build(mu, tau, use_iv=True)
    G = stab(mu, tau)
    neg = lambda z: tuple(sorted((z[0] ^ 1, z[1] ^ 1)))
    act = lambda g, pair: tuple(sorted((g[pair[0]], g[pair[1]])))
    z0 = zreps[k0]
    H = [g for g in G if act(g, z0) in (z0, neg(z0))]
    print("tau#%d : |G| = %d ; paire k0 = %s ; |Stab(k0)| = %d ; %d options" % (ti, len(G), z0, len(H), len(opts[k0])))
    idx = {o: i for i, o in enumerate(opts[k0])}
    seen = set(); repsel = []
    for i, (wi, vi) in enumerate(opts[k0]):
        if i in seen: continue
        orb = set()
        for g in H:
            w2, v2 = P.index(act(g, P[wi])), P.index(act(g, P[vi]))
            if act(g, z0) == neg(z0): w2, v2 = v2, w2
            j = idx.get((w2, v2))
            assert j is not None, "option hors du domaine : symetrie non respectee par les filtres"
            orb.add(j)
        seen |= orb; repsel.append(i)
    print("  %d cubes (orbites d'options)" % len(repsel))
    base = os.path.join(HERE, "..", "data", "cnf")
    for c, i in enumerate(repsel):
        name = "fsos_A111111_t%d_k%d_c%02d" % (ti, k0, c)
        with open(os.path.join(base, name + ".cnf"), "w") as f:
            f.write("p cnf %d %d\n" % (cnf.nv, len(cnf.clauses) + 1))
            for cl in cnf.clauses:
                f.write(" ".join(map(str, cl)) + " 0\n")
            f.write("%d 0\n" % Y[k0, i])
    print("  ecrits : fsos_A111111_t%d_k%d_c00 .. c%02d" % (ti, k0, len(repsel) - 1))
