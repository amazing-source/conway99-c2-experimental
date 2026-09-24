"""Write DIMACS CNFs (LF line endings) of the exact orbit model m=7 + forced sib pairs, for certification with kissat + drat-trim.
Usage: python make_cnf.py <name> "<pairs e.g. 12 34 56 67>" [exact]
  exact: additionally forbid every other sib pair.
Writes data/cnf/<name>.cnf and appends '<sha256>  <name>.cnf  vars clauses pairs' to data/cnf/MANIFEST.txt
"""
import hashlib, itertools, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
import orbit_sat  # noqa

M = 7
OUTDIR = os.path.join(HERE, "..", "data", "cnf")


def main():
    name = sys.argv[1]
    pairs = [(int(x[0]), int(x[1])) for x in sys.argv[2].split()] if sys.argv[2].strip() else []
    exact = len(sys.argv) > 3 and sys.argv[3] == "exact"
    cnf, pool, outer, rep, trep, A, B = orbit_sat.build(M, "none")
    extra = []
    for (i, j) in pairs:
        U = outer.index((i, j, 0)); V = outer.index((i, j, 1))
        extra += [[A[U, V]], [B[U, V]]]
    if exact:
        for (i, j) in itertools.combinations(range(1, M + 1), 2):
            if (i, j) in pairs: continue
            U = outer.index((i, j, 0)); V = outer.index((i, j, 1))
            extra.append([-A[U, V], -B[U, V]])
    clauses = cnf.clauses + extra
    nv = pool.top
    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, name + ".cnf")
    h = hashlib.sha256()
    with open(path, "w", newline="\n") as f:
        head = "c C2 orbit model m=7, sib pairs %s%s\np cnf %d %d\n" % (sys.argv[2], " exact" if exact else "", nv, len(clauses))
        f.write(head); h.update(head.encode())
        for c in clauses:
            line = " ".join(map(str, c)) + " 0\n"
            f.write(line); h.update(line.encode())
    with open(os.path.join(OUTDIR, "MANIFEST.txt"), "a", newline="\n") as f:
        f.write("%s  %s.cnf  vars=%d clauses=%d pairs=[%s]%s\n" % (h.hexdigest(), name, nv, len(clauses), sys.argv[2], " exact" if exact else ""))
    print(name, nv, len(clauses), h.hexdigest())


if __name__ == "__main__":
    main()
