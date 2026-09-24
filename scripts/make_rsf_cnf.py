"""Ecrit le CNF DIMACS de RSF(orbites soeurs de Sigma) (modele complet orbit_sat restreint aux lignes soeurs, row_system_full.build)
avec au moins les paires soeurs de Sigma, pour certification kissat + drat-trim (scripts/cert_run.sh).
C'est un sous-ensemble des contraintes du modele complet (construction identique, verifiee par sha256 sur K2K2P3 : notes/19 §2),
donc UNSAT ici => Sigma (au moins) impossible dans le modele complet.
Usage : python make_rsf_cnf.py <nom> "<paires>"      -> data/cnf/<nom>.cnf + ligne dans data/cnf/MANIFEST_rsf.txt
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import row_system_full
from rs_experiments import sister_orbits, parse

name, ps = sys.argv[1], sys.argv[2]
E = parse(ps)
clauses, nv, outer, A, B = row_system_full.build(sister_orbits(E), sigma=E)
path = os.path.join(HERE, "..", "data", "cnf", name + ".cnf")
h = hashlib.sha256()
with open(path, "w", newline="\n") as f:
    head = "c RSF(orbites soeurs) du modele orbite m=7, paires soeurs %s\np cnf %d %d\n" % (ps, nv, len(clauses))
    f.write(head); h.update(head.encode())
    for c in clauses:
        line = " ".join(map(str, c)) + " 0\n"; f.write(line); h.update(line.encode())
with open(os.path.join(HERE, "..", "data", "cnf", "MANIFEST_rsf.txt"), "a", newline="\n") as f:
    f.write("%s  %s.cnf  vars=%d clauses=%d pairs=[%s]  (RSF lignes soeurs, scripts/row_system_full.build)\n" % (h.hexdigest(), name, nv, len(clauses), ps))
print(name, nv, len(clauses), h.hexdigest())
