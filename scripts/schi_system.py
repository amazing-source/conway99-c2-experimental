"""Systeme chi SIGNE des paires soeurs (notes/19 §4) : forme compacte de RSF(orbites soeurs).

Pour une paire soeur p = {i<j} : grille G_p = {+-r_p, +-r'_p}, r_p = rep U_p^+ = {(i,0),(j,0)}, r'_p = rep U_p^- = {(i,0),(j,1)}.
Toute racine w sur une paire disjointe de p a exactement un voisin c_p(w) dans G_p ; c_p(-w) = -c_p(w).
Niveau orbites : c_p(rep W) = sigma_p(W) . rep U_p^{chi_p(W)} ; variables X[p,W] = chi_p(W), Z[p,W] = [sigma_p(W) = -1].
Contraintes (toutes derivees de (R),(D),(I),(P) de orbit_sat restreintes aux lignes soeurs, notes/19 §4) :
  systeme chi non signe (bij, disj, int, fibre, bloc)                                          (notes/18)
  (sbloc) p, eps, l hors p : parmi les 8 orbites W sur {l,m} (m hors p), celles avec chi_p = eps (4) ont pi_l(W) = +1 pour 2 d'entre
          elles exactement, pi_l(W) = sigma_p(W) . s_l(rep W)  (signe en l de la racine envoyee sur +rep U_p^eps)
  (sbij)  p,q disjointes : c_p(rep U_q^f) = z.rep U_p^e  <=>  c_q(rep U_p^e) = z.rep U_q^f   (adjacence symetrique)
  (sdisj) p,q disjointes, W sur les 3 blocs restants : rho(W) = sigma_q(W) sigma_p(W) sigma_q(U_p^{chi_p(W)}) ;
          pour chaque eps, exactement une des 3 orbites W avec chi_p(W) = eps a rho(W) = +1
  (sint)  p = {i,j}, q = {i,k} : pour chaque (e,f), parmi les 3 orbites W (hors {i,j,k}) avec (chi_p,chi_q) = (e,f), exactement une
          a  s_i(c_p(rep W)) = s_i(c_q(rep W)),  s_i = signe en i.
Usage : python schi_system.py [T] [config ...]
"""
import itertools, sys, time
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver
sys.path.insert(0, "scripts")
from chi_system import ALLPAIRS, BLOCKS

def s_at(W, l):
    """signe en l de rep W, W = ((k,l2), e) : rep = {(k,0),(l2,e)}."""
    (k, l2), e = W
    if l == k:
        return 1
    if l == l2:
        return -1 if e else 1
    raise ValueError

def build(S, signed=True, unsigned=True, cards=None, xors=None, aug=False):
    """cards / xors (listes optionnelles) : recoivent (litteraux, k) pour chaque cardinalite et (a, b, z) pour chaque z = a xor b,
    afin qu'un solveur XOR (schi_cms.py) ajoute les consequences de parite."""
    S = [tuple(sorted(p)) for p in S]
    pool = IDPool(); cnf = CNF()
    def eq(lits, k):
        if cards is not None:
            cards.append((list(lits), k))
        if k < 0 or k > len(lits):
            cnf.append([]); return
        cnf.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    def AND(*lits):
        z = pool.id(("and",) + tuple(sorted(lits)))
        cnf.extend([[-z, l] for l in lits]); cnf.append([z] + [-l for l in lits]); return z
    def XOR(a, b):
        z = pool.id(("xor",) + tuple(sorted((a, b))))
        cnf.extend([[-z, a, b], [-z, -a, -b], [z, -a, b], [z, a, -b]])
        if xors is not None:
            xors.append((a, b, z))
        return z
    disj = lambda a, b: not (set(a) & set(b))
    O = {p: [(r, e) for r in ALLPAIRS if disj(r, p) for e in (0, 1)] for p in S}
    X = {(p, W): pool.id(("chi", p, W)) for p in S for W in O[p]}
    Z = {(p, W): pool.id(("sgn", p, W)) for p in S for W in O[p]}
    lit = lambda v, val: v if val else -v
    if unsigned:
        import chi_system
        # reutilise exactement l'encodage non signe (memes variables X via un pool partage)
        c2, _ = chi_system_build_shared(S, pool, X, cnf, cards)
    for p, q in itertools.combinations(S, 2):
        if disj(p, q) and signed:
            # (sbij)
            for e in (0, 1):
                for f in (0, 1):
                    for z in (0, 1):
                        a = AND(lit(X[p, (q, f)], e), lit(Z[p, (q, f)], z))
                        b = AND(lit(X[q, (p, e)], f), lit(Z[q, (p, e)], z))
                        cnf.extend([[-a, b], [a, -b]])
            # (sdisj)
            common = [W for W in O[p] if W in O[q]]
            for e in (0, 1):
                lits = []
                for W in common:
                    m = pool.id(("mux", p, q, W))      # m = Z[q, U_p^{chi_p(W)}]
                    x = X[p, W]; z0 = Z[q, (p, 0)]; z1 = Z[q, (p, 1)]
                    cnf.extend([[x, -m, z0], [x, m, -z0], [-x, -m, z1], [-x, m, -z1]])
                    r = XOR(XOR(Z[q, W], Z[p, W]), m)   # r = 0 <=> rho = +1
                    lits.append(AND(lit(x, e), -r))
                eq(lits, 1)
        elif len(set(p) & set(q)) == 1 and signed:
            (i,) = set(p) & set(q)
            common = [W for W in O[p] if W in O[q]]
            for e in (0, 1):
                for f in (0, 1):
                    kap = s_at((p, e), i) * s_at((q, f), i)
                    lits = []
                    for W in common:
                        d = XOR(Z[p, W], Z[q, W])             # d = 1 <=> sigma_p sigma_q = -1
                        lits.append(AND(lit(X[p, W], e), lit(X[q, W], f), lit(d, kap == -1)))
                    eq(lits, 1)
    if signed:
        for p in S:
            for l in BLOCKS:
                if l in p:
                    continue
                Wl = [W for W in O[p] if l in W[0]]
                for e in (0, 1):
                    lits = []
                    for W in Wl:
                        # pi_l(W) = +1 <=> sigma_p(W) = s_l(rep W) <=> Z = [s_l = -1]
                        lits.append(AND(lit(X[p, W], e), lit(Z[p, W], s_at(W, l) == -1)))
                    eq(lits, 2)
    if aug:
        # (aug) ligne (I) d'une orbite QUELCONQUE W au bloc l hors de W (notes/19 §6) : rep W a exactement 2 voisins racines contenant
        # (l,0) et 2 contenant (l,1) ; parmi eux, les voisins de grille c_p(rep W) (p soeur, l dans p, p disjointe de W), de signe en l
        # sigma_p(W).s_l(rep U_p^chi_p(W)).  Donc au plus 2 voisins de grille de chaque signe en l.
        for W in [(r, e) for r in ALLPAIRS for e in (0, 1)]:
            for l in BLOCKS:
                if l in W[0]:
                    continue
                P = [p for p in S if l in p and disj(p, W[0])]
                if len(P) < 3:
                    continue
                plus = []
                for p in P:
                    if l == p[0]:
                        plus.append(-Z[p, W])                          # s_l(rep U_p^e) = +1
                    else:
                        plus.append(-XOR(Z[p, W], X[p, W]))            # s_l(rep U_p^e) = (-1)^e : signe + <=> Z = chi
                cnf.extend(CardEnc.atmost(lits=plus, bound=2, vpool=pool, encoding=EncType.seqcounter).clauses)
                cnf.extend(CardEnc.atmost(lits=[-x for x in plus], bound=2, vpool=pool, encoding=EncType.seqcounter).clauses)
    return cnf, pool, X, Z

def chi_system_build_shared(S, pool, X, cnf, cards=None):
    """Encodage non signe de notes/18 (copie de chi_system.build) sur les variables X donnees."""
    def eq(lits, k):
        if cards is not None:
            cards.append((list(lits), k))
        if k < 0 or k > len(lits):
            cnf.append([]); return
        cnf.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
    disj = lambda a, b: not (set(a) & set(b))
    O = {p: [(r, e) for r in ALLPAIRS if disj(r, p) for e in (0, 1)] for p in S}
    def xor_eq(a, b, c):
        cnf.extend([[-a, b, c], [-a, -b, -c], [a, -b, c], [a, b, -c]])
    for p, q in itertools.combinations(S, 2):
        if not disj(p, q):
            continue
        cnf.extend([[X[p, (q, 0)], X[p, (q, 1)]], [-X[p, (q, 0)], -X[p, (q, 1)]]])
        cnf.extend([[X[q, (p, 0)], X[q, (p, 1)]], [-X[q, (p, 0)], -X[q, (p, 1)]]])
        a, b = X[p, (q, 0)], X[q, (p, 0)]
        cnf.extend([[-a, b], [a, -b]])
        c = X[p, (q, 0)]
        common = [W for W in O[p] if W in O[q]]
        for W in common:
            xor_eq(X[q, W], X[p, W], c)
        eq([X[p, W] for W in common], 3)
    for p, q in itertools.combinations(S, 2):
        if len(set(p) & set(q)) != 1:
            continue
        common = [W for W in O[p] if W in O[q]]
        for e in (0, 1):
            for f in (0, 1):
                lits = []
                for W in common:
                    z = pool.id(("and_u", p, q, W, e, f))
                    a = X[p, W] if e else -X[p, W]
                    b = X[q, W] if f else -X[q, W]
                    cnf.extend([[-z, a], [-z, b], [z, -a, -b]])
                    lits.append(z)
                eq(lits, 3)
    for p in S:
        eq([X[p, W] for W in O[p]], 10)
        for l in BLOCKS:
            if l in p:
                continue
            eq([X[p, W] for W in O[p] if l in W[0]], 4)
    return cnf, pool

def run(S, signed=True, aug=False):
    t0 = time.time()
    cnf, pool, X, Z = build(S, signed=signed, aug=aug)
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        r = s.solve()
    return ("SAT" if r else "UNSAT"), time.time() - t0, pool.top, len(cnf.clauses)

if __name__ == "__main__":
    from chi_system import CONFIGS
    names = sys.argv[1:] or list(CONFIGS)
    for n in names:
        E = CONFIGS[n] if n in CONFIGS else [tuple(sorted((int(x[0]), int(x[1])))) for x in n.replace("_", " ").split()]
        res, dt, nv, nc = run(E)
        print("%-16s %-28s schi: %-5s (%d vars, %d clauses, %.2f s)" % (n, " ".join("%d%d" % p for p in E), res, nv, nc, dt), flush=True)
