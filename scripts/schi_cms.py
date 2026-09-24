"""Systeme chi signe resolu par CryptoMiniSat avec les consequences de PARITE explicites (notes/19).

Les contraintes signees sont des cardinalites sur des ET de litteraux et de XOR de signes : un solveur CDCL pur voit mal la parite.
On ajoute, comme clauses XOR natives (elimination de Gauss dans CMS) :
  - chaque definition z = a xor b ;
  - pour chaque cardinalite « exactement k parmi L », la consequence  xor(L) = k mod 2  (implication logique, donc sure).
Meme ensemble de solutions que schi_system.build (seules des consequences sont ajoutees).
Usage : python schi_cms.py <T> "12 16 17" [...]
"""
import sys, time
from collections import Counter
from pycryptosat import Solver
sys.path.insert(0, "scripts")
import schi_system

def add_parity(s, lits, k):
    cnt = Counter(abs(l) for l in lits)
    rhs = (k + sum(1 for l in lits if l < 0)) % 2
    vs = [v for v, c in cnt.items() if c % 2]
    if vs:
        s.add_xor_clause(vs, bool(rhs))
    elif rhs:
        s.add_clause([])

AUG = False
def run(E, T, parity=True):
    cards, xors = [], []
    t0 = time.time()
    cnf, pool, X, Z = schi_system.build(E, cards=cards, xors=xors, aug=AUG)
    s = Solver(threads=1, time_limit=T)
    s.add_clauses(cnf.clauses)
    if parity:
        for a, b, z in xors:
            add_parity(s, [a, b, z], 0)
        for lits, k in cards:
            add_parity(s, lits, k)
    r, sol = s.solve()
    verdict = {True: "SAT", False: "UNSAT", None: "TIMEOUT"}[r]
    return verdict, time.time() - t0, pool.top, len(cnf.clauses), len(cards) + len(xors)

if __name__ == "__main__":
    sys.path.insert(0, "scripts")
    from rs_experiments import idle
    idle()
    T = float(sys.argv[1])
    for arg in sys.argv[2:]:
        E = [tuple(sorted((int(x[0]), int(x[1])))) for x in arg.split()]
        v, dt, nv, nc, nx = run(E, T)
        print("%-24s CMS+parite : %-7s %.1f s (%d vars, %d clauses, %d XOR)" % (arg, v, dt, nv, nc, nx), flush=True)
