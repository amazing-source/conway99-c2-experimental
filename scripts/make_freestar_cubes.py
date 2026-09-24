"""« Lemme de l'etoile libre » (notes/20) : l'etoile star(1) peut-elle n'avoir AUCUNE paire soeur ?
Si non (pour un bloc c quelconque, par symetrie), toute droite de x est dans une grille par x ; avec |Sigma| <= 4 et deg <= 2
(note 19), Sigma devrait couvrir les 7 blocs avec 4 aretes, donc Sigma = K2K2P3, deja exclu (DRAT) : C2 n'existerait pas.

Instance : RSF(star(1)) (modele complet restreint aux 12 lignes de star(1)), aucune paire {1,m} soeur (exact).
Decoupage exhaustif (a symetrie pres) selon le couplage A_1 de N(e_1) sur les 12 racines contenant +e_1 : en variables,
A_1[U,V] = a[U,V] pour U, V dans star(1) (rep U et rep V contiennent (1,0)).  Sous S_6 (blocs 2..7) x (Z2)^6 (changements de signe
des blocs 2..7), un couplage parfait des 12 demi-aretes (m,e) est determine par le multigraphe 2-regulier qu'il induit sur les
6 blocs, donc par une partition de 6 en longueurs de cycles : 11 cubes, qui couvrent tous les cas.
Ecrit data/cnf/freestar_A<partition>.cnf + data/cnf/MANIFEST_freestar.txt.
"""
import hashlib, os, sys, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import row_system_full as R

PARTS = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1), (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]

def matching(part):
    blocks = [2, 3, 4, 5, 6, 7]; pos = 0; M = []
    for L in part:
        cyc = blocks[pos:pos + L]; pos += L
        if L == 1:
            M.append(((cyc[0], 0), (cyc[0], 1)))
        elif L == 2:
            M += [((cyc[0], 0), (cyc[1], 0)), ((cyc[0], 1), (cyc[1], 1))]
        else:
            for t in range(L):
                M.append(((cyc[t], 1), (cyc[(t + 1) % L], 0)))
    assert sorted(h for e in M for h in e) == sorted((m, e) for m in blocks for e in (0, 1))
    return M

if __name__ == "__main__":
    outer = [(i, j, e) for i in range(1, 8) for j in range(i + 1, 8) for e in (0, 1)]
    S = [U for U, (i, j, e) in enumerate(outer) if i == 1]
    for part in PARTS:
        clauses, nv, o, A, B = R.build(S, sigma=(), sigma_exact=True)
        M = matching(part)
        on = {frozenset((R.orbit(1, m1, e1), R.orbit(1, m2, e2))) for (m1, e1), (m2, e2) in M}
        units = []
        for U, V in itertools.combinations(S, 2):
            units.append([A[U, V]] if frozenset((U, V)) in on else [-A[U, V]])
        allc = clauses + units
        name = "freestar_A" + "".join(map(str, part))
        path = os.path.join(HERE, "..", "data", "cnf", name + ".cnf")
        h = hashlib.sha256()
        with open(path, "w", newline="\n") as f:
            head = "c RSF(star(1)) sans paire soeur, couplage A_1 de type %s\np cnf %d %d\n" % (part, nv, len(allc))
            f.write(head); h.update(head.encode())
            for c in allc:
                line = " ".join(map(str, c)) + " 0\n"; f.write(line); h.update(line.encode())
        with open(os.path.join(HERE, "..", "data", "cnf", "MANIFEST_freestar.txt"), "a", newline="\n") as f:
            f.write("%s  %s.cnf  vars=%d clauses=%d  (RSF(star(1)) exact sans soeur, A_1 cycles %s, scripts/make_freestar_cubes.py)\n"
                    % (h.hexdigest(), name, nv, len(allc), part))
        print(name, nv, len(allc))
