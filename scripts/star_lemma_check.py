"""Verification machine des deux comptages exacts utilises par le lemme des etoiles (notes/19 §6 bis), DIRECTEMENT dans RSF
(modele complet restreint aux lignes soeurs, row_system_full.build, construction identique a orbit_sat) :

 (L1') p = {c,x} soeur, l hors p :  #{ racines w contenant +e_l, evitant p, adjacentes a une racine de G_p de signe + en c } = 4
 (L2') p = {c,a}, q = {c,b} soeurs :  #{ orbites W evitant {c,a,b} : s_c(c_p(rep W)) = s_c(c_q(rep W)) } = 4

On ajoute a RSF la NEGATION du comptage (<= 3 ou >= 5) : UNSAT attendu (implication).  c = 1 (plus petit bloc), de sorte que les
racines de G_p de signe + en c sont exactement rep U_p^+ et rep U_p^-, et qu'une racine rep W (resp. trep W = -rep W) est adjacente
a rep U_p^e ssi a[U_p^e, W] = 1 (resp. b[U_p^e, W] = 1).
Usage : python star_lemma_check.py
"""
import sys, time, itertools
sys.path.insert(0, "scripts")
from pysat.solvers import Solver
from pysat.formula import IDPool
from pysat.card import CardEnc, EncType
import row_system_full
from rs_experiments import sister_orbits, idle

outer = [(i, j, e) for i in range(1, 8) for j in range(i + 1, 8) for e in (0, 1)]
idx = {o: k for k, o in enumerate(outer)}
rep = {k: {(i, 0), (j, e)} for k, (i, j, e) in enumerate(outer)}
trep = {k: {(i, 1), (j, 1 - e)} for k, (i, j, e) in enumerate(outer)}

def negated_count(lits, k, pool):
    """clauses exprimant  sum(lits) != k  via un selecteur : (<= k-1) ou (>= k+1)."""
    s = pool.id(("sel",))
    lo = CardEnc.atmost(lits=lits, bound=k - 1, vpool=pool, encoding=EncType.seqcounter).clauses
    hi = CardEnc.atleast(lits=lits, bound=k + 1, vpool=pool, encoding=EncType.seqcounter).clauses
    return [c + [-s] for c in lo] + [c + [s] for c in hi]

def check_L1(c, x, l):
    E = [(c, x)]
    clauses, nv, _, A, B = row_system_full.build(sister_orbits(E), sigma=E)
    pool = IDPool(start_from=nv + 1)
    Up = [idx[(c, x, 0)], idx[(c, x, 1)]]
    lits = []
    for W, (i, j, e) in enumerate(outer):
        if l not in (i, j) or {i, j} & {c, x}:
            continue
        for U in Up:
            if (l, 0) in rep[W]:
                lits.append(A[U, W])      # rep W contient +e_l, adjacente a rep U
            if (l, 0) in trep[W]:
                lits.append(B[U, W])      # trep W contient +e_l, adjacente a rep U
    cl = negated_count(lits, 4, pool)
    with Solver(name="cadical195", bootstrap_with=clauses + cl) as s:
        return s.solve(), len(lits)

def check_L2(c, a, b):
    E = [(c, a), (c, b)]
    clauses, nv, _, A, B = row_system_full.build(sister_orbits(E), sigma=E)
    pool = IDPool(start_from=nv + 1); extra = []
    Pa = [idx[(c, a, 0)], idx[(c, a, 1)]]; Pb = [idx[(c, b, 0)], idx[(c, b, 1)]]
    agree = []
    for W, (i, j, e) in enumerate(outer):
        if {i, j} & {c, a, b}:
            continue
        # s_c(c_p(rep W)) = +  <=>  a[U_p^+,W] or a[U_p^-,W]
        pa = pool.id(("pa", W)); pb = pool.id(("pb", W)); g = pool.id(("ag", W))
        extra += [[-pa, A[Pa[0], W], A[Pa[1], W]], [pa, -A[Pa[0], W]], [pa, -A[Pa[1], W]]]
        extra += [[-pb, A[Pb[0], W], A[Pb[1], W]], [pb, -A[Pb[0], W]], [pb, -A[Pb[1], W]]]
        extra += [[-g, pa, -pb], [-g, -pa, pb], [g, pa, pb], [g, -pa, -pb]]      # g = (pa == pb)
        agree.append(g)
    extra += negated_count(agree, 4, pool)
    with Solver(name="cadical195", bootstrap_with=clauses + extra) as s:
        return s.solve(), len(agree)

if __name__ == "__main__" and not (len(sys.argv) > 1 and sys.argv[1] == "split"):
    idle()
    c = 1
    for x in (2, 5, 7):
        for l in [l for l in range(1, 8) if l not in (c, x)][:3]:
            t0 = time.time(); r, n = check_L1(c, x, l)
            print("(L1') p={%d,%d}, l=%d : %d litteraux ; RSF + (compte != 4) : %s (%.1f s)" % (c, x, l, n, "SAT -> ECHEC" if r else "UNSAT (implication verifiee)", time.time() - t0), flush=True)
    for (a, b) in ((2, 3), (2, 7), (4, 6)):
        t0 = time.time(); r, n = check_L2(c, a, b)
        print("(L2') p={%d,%d}, q={%d,%d} : %d orbites ; RSF + (compte != 4) : %s (%.1f s)" % (c, a, c, b, n, "SAT -> ECHEC" if r else "UNSAT (implication verifiee)", time.time() - t0), flush=True)

def check_L2_split(c, a, b, e, f):
    """Version eclatee de (L2') : pour (U_p^e, U_q^f), sum_{W evitant {c,a,b}} (a_{pe,W} a_{qf,W} + b_{pe,W} b_{qf,W}) = 1.
    C'est l'equation (P) « same » de orbit_sat pour (U_p^e, U_q^f) (valeur 2 - |rep U cap rep V| = 1), les termes restants etant
    nuls par S1.  (L2') en est la somme sur (e,f) : 1+1+1+1 = 4 (Fait B), l'accord etant sum_{e,f}(aa+bb) quand exactement une des
    quatre variables a_{p+},a_{p-},b_{p+},b_{p-} vaut 1 (S1)."""
    E = [(c, a), (c, b)]
    clauses, nv, _, A, B = row_system_full.build(sister_orbits(E), sigma=E)
    pool = IDPool(start_from=nv + 1); extra = []
    U = idx[(c, a, e)]; V = idx[(c, b, f)]
    terms = []
    for W, (i, j, ee) in enumerate(outer):
        if {i, j} & {c, a, b}:
            continue
        for (x, y) in ((A[U, W], A[V, W]), (B[U, W], B[V, W])):
            z = pool.id(("t", x, y)); extra += [[-z, x], [-z, y], [z, -x, -y]]; terms.append(z)
    extra += negated_count(terms, 1, pool)
    with Solver(name="cadical195", bootstrap_with=clauses + extra) as s:
        return s.solve()

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "split":
    for (a, b) in ((2, 3), (2, 7), (4, 6)):
        for e in (0, 1):
            for f in (0, 1):
                t0 = time.time(); r = check_L2_split(1, a, b, e, f)
                print("(L2' eclate) p={1,%d}^%d, q={1,%d}^%d : RSF + (somme != 1) : %s (%.1f s)" % (a, e, b, f, "SAT -> ECHEC" if r else "UNSAT (implication verifiee)", time.time() - t0), flush=True)
