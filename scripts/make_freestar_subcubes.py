"""Sous-cubes (mu, tau) de l'etoile libre dans le modele certifie RSF(star(1)) (note 22).
Pour un cube A<partition> et un type tau (representant d'orbite sous Stab(mu), freestar_compact.types), on fixe TOUS les bits
internes a star(1) : a[U_b,U_d] = [mu(b) = d], b[U_b,U_d] = [tau(b) = d]  (U_b = orbite de e_1 + b ; x = 2(m-2)+e <-> (1,m,e)).
Aucune paire {1,m} soeur (Sigma exact vide sur star(1)). Ecrit data/cnf/fsub_A<part>_t<i>.cnf + MANIFEST_fsub.txt.
Exhaustivite : les types tau couvrent toutes les orbites sous Stab(mu) (verifie : note 20/22), et les 11 cubes mu couvrent tout (10 395).
Usage : python make_freestar_subcubes.py <partition> [indices]"""
import sys, os, hashlib, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import row_system_full as R
from freestar_compact import types

def xorb(x):
    m = x // 2 + 2; e = x % 2
    return R.orbit(1, m, e)

if __name__ == "__main__":
    part = tuple(int(c) for c in sys.argv[1])
    mu, reps, st = types(part)
    sel = range(len(reps)) if len(sys.argv) < 3 else [int(i) for i in sys.argv[2].split(",")]
    outer = [(i, j, e) for i in range(1, 8) for j in range(i + 1, 8) for e in (0, 1)]
    S = [U for U, (i, j, e) in enumerate(outer) if i == 1]
    for i in sel:
        tau = reps[i]
        clauses, nv, o, A, B = R.build(S, sigma=(), sigma_exact=True)
        units = []
        for b, d in itertools.combinations(range(12), 2):
            U, V = xorb(b), xorb(d)
            units.append([A[U, V]] if mu[b] == d else [-A[U, V]])
            units.append([B[U, V]] if tau[b] == d else [-B[U, V]])
        allc = clauses + units
        name = "fsub_A%s_t%d" % (sys.argv[1], i)
        path = os.path.join(HERE, "..", "data", "cnf", name + ".cnf"); h = hashlib.sha256()
        with open(path, "w", newline="\n") as f:
            head = "c RSF(star(1)) etoile libre, mu type %s, tau %s\np cnf %d %d\n" % (part, tau, nv, len(allc))
            f.write(head); h.update(head.encode())
            for c in allc:
                line = " ".join(map(str, c)) + " 0\n"; f.write(line); h.update(line.encode())
        with open(os.path.join(HERE, "..", "data", "cnf", "MANIFEST_fsub.txt"), "a", newline="\n") as f:
            f.write("%s  %s.cnf  vars=%d clauses=%d  (mu %s, tau %s)\n" % (h.hexdigest(), name, nv, len(allc), part, tau))
        print(name, nv, len(allc), tau)
