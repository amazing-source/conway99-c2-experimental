"""CNF DIMACS des 18 implications utilisees par le lemme des etoiles (notes/19 §6 bis), pour certification DRAT (cert_run.sh).
Etoile de centre c = 1, feuilles L = {2,3,4} (sans perte de generalite par symetrie S_7 du modele).
  factA_x{x}_l{l}   : RSF(lignes soeurs de {1,x}) + (compte du Fait A != 4)          pour x in L, l in L \\ {x}   (6 CNF)
  factB_{x}{y}_{e}{f} : RSF(lignes soeurs de {1,x},{1,y}) + (somme (P)-same != 1)    pour {x,y} c L, e,f in {0,1} (12 CNF)
UNSAT de chaque CNF  <=>  l'implication correspondante est vraie dans le modele complet restreint aux lignes soeurs.
Ecrit data/cnf/<nom>.cnf et ajoute une ligne a data/cnf/MANIFEST_starfacts.txt.
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from pysat.formula import IDPool
import row_system_full
from rs_experiments import sister_orbits
from star_lemma_check import outer, idx, rep, trep, negated_count

def write(name, clauses, nv, desc):
    path = os.path.join(HERE, "..", "data", "cnf", name + ".cnf")
    h = hashlib.sha256()
    with open(path, "w", newline="\n") as f:
        head = "c %s\np cnf %d %d\n" % (desc, nv, len(clauses))
        f.write(head); h.update(head.encode())
        for c in clauses:
            line = " ".join(map(str, c)) + " 0\n"; f.write(line); h.update(line.encode())
    with open(os.path.join(HERE, "..", "data", "cnf", "MANIFEST_starfacts.txt"), "a", newline="\n") as f:
        f.write("%s  %s.cnf  vars=%d clauses=%d  (%s)\n" % (h.hexdigest(), name, nv, len(clauses), desc))
    print(name, nv, len(clauses))

def factA(c, x, l):
    E = [(c, x)]
    clauses, nv, _, A, B = row_system_full.build(sister_orbits(E), sigma=E)
    pool = IDPool(start_from=nv + 1)
    lits = []
    for W, (i, j, e) in enumerate(outer):
        if l not in (i, j) or {i, j} & {c, x}:
            continue
        for U in (idx[(c, x, 0)], idx[(c, x, 1)]):
            if (l, 0) in rep[W]: lits.append(A[U, W])
            if (l, 0) in trep[W]: lits.append(B[U, W])
    cl = negated_count(lits, 4, pool)
    return clauses + cl, pool.top

def factB(c, a, b, e, f):
    E = [(c, a), (c, b)]
    clauses, nv, _, A, B = row_system_full.build(sister_orbits(E), sigma=E)
    pool = IDPool(start_from=nv + 1); extra = []
    U = idx[(c, a, e)]; V = idx[(c, b, f)]
    terms = []
    for W, (i, j, ee) in enumerate(outer):
        if {i, j} & {c, a, b}:
            continue
        for (p, q) in ((A[U, W], A[V, W]), (B[U, W], B[V, W])):
            z = pool.id(("t", p, q)); extra += [[-z, p], [-z, q], [z, -p, -q]]; terms.append(z)
    extra += negated_count(terms, 1, pool)
    return clauses + extra, pool.top

if __name__ == "__main__":
    c, L = 1, (2, 3, 4)
    for x in L:
        for l in L:
            if l == x: continue
            cl, nv = factA(c, x, l)
            write("factA_x%d_l%d" % (x, l), cl, nv, "lemme des etoiles, Fait A : RSF(soeur {1,%d}) + compte(+e_%d) != 4" % (x, l))
    for (x, y) in ((2, 3), (2, 4), (3, 4)):
        for e in (0, 1):
            for f in (0, 1):
                cl, nv = factB(c, x, y, e, f)
                write("factB_%d%d_%d%d" % (x, y, e, f), cl, nv, "lemme des etoiles, Fait B eclate : RSF(soeurs {1,%d},{1,%d}) + (P)-same(U^%d,V^%d) != 1" % (x, y, e, f))
