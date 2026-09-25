"""CNF du probleme local de l'etoile libre (cube A111111, type tau donne) avec les contraintes DERIVEES de la note 23 :
  options par paire antipodale {z, -z} : (Phi(z), Phi(-z)), filtrees par
     - l'equilibre (lemme §8, propre a k = 14) : |z inter S| + |Phi(z) inter S| + |Phi(-z) inter S| = |S|/2 pour chaque orbite S
       de <s, mu, tau> ;
     - les zeros de (ii) (pour z et -z) et de (iii) ;
     - (v) (lambda = 1 entre N(l) et les lointains) ;
  cardinalites exactes : bijectivite de Phi, (ii) (144 cases), (iii) (78 cases) ;
  (iv) (mu <= 2 entre lointains) par variables auxiliaires B[y, b] = [b dans Phi(y)] et A[y, y'] = [Phi(y), Phi(y') adjacentes].
Validation : les formules (ii), (iii), (iv) sont verifiees sur la table BvLS (m = 11) par verify_bvls() (sans equilibre ni (v),
qui sont propres au cas k = 14 libre).
Usage : python make_freestar_sos_cnf.py <tau_index> [--no-iv] [--cube k0:o0]
"""
import sys, os, itertools, collections, hashlib
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types
from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool

def orbit_map(mu, tau, n2):
    orb = {}
    for a in range(n2):
        if a in orb: continue
        S = {a}; fr = [a]
        while fr:
            y = fr.pop()
            for g in (y ^ 1, mu[y], tau[y]):
                if g not in S: S.add(g); fr.append(g)
        for y in S: orb[y] = min(S)
    return orb

def build(mu, tau, use_iv=True, balance=True, use_v=True, n2=12):
    Cx, Ct = targets(mu, tau, n2)
    R = [(a, b) for a in range(n2) for b in range(a + 1, n2) if a // 2 != b // 2]          # racines lointaines
    P = [(a, b) for a in range(n2) for b in range(a + 1, n2) if mu[a] != b]                # images (paires hors mu)
    neg = lambda z: tuple(sorted((z[0] ^ 1, z[1] ^ 1)))
    zreps = []; seen = set()
    for z in R:
        if z in seen: continue
        seen.add(z); seen.add(neg(z)); zreps.append(z)
    orb = orbit_map(mu, tau, n2); osz = collections.Counter(orb.values())
    opts = []
    for z in zreps:
        nz = neg(z); lst = []
        for wi, w in enumerate(P):
            if any(Cx[a, b] == 0 for a in z for b in w): continue
            for vi, v in enumerate(P):
                if vi == wi: continue
                if any(Cx[a, b] == 0 for a in nz for b in v): continue
                if any(Ct[b, d] == 0 for b in w for d in v) or any(Ct[b, d] == 0 for b in v for d in w): continue
                if balance and any(sum(1 for y in z if orb[y] == o) + sum(1 for y in w if orb[y] == o) + sum(1 for y in v if orb[y] == o) != osz[o] // 2 for o in osz):
                    continue
                if use_v:
                    bad = any(a in w and ((a ^ 1) in v or tau[a] in v) for a in z) or any(a in v and ((a ^ 1) in w or tau[a] in w) for a in nz)
                    if bad: continue
                lst.append((wi, vi))
        opts.append(lst)
    pool = IDPool(); cnf = CNF()
    Y = {(k, o): pool.id(("y", k, o)) for k in range(len(zreps)) for o in range(len(opts[k]))}
    def card_eq(lits, bound):
        if bound == 0:
            for l in lits: cnf.append([-l])
            return
        if bound > len(lits):
            cnf.append([]); return
        enc = CardEnc.equals(lits=lits, bound=bound, top_id=pool.top, encoding=EncType.seqcounter)
        pool.occupy(pool.top + 1, enc.nv); pool.top = max(pool.top, enc.nv)
        cnf.extend(enc.clauses)
    for k in range(len(zreps)):
        card_eq([Y[k, o] for o in range(len(opts[k]))], 1)
    byroot = collections.defaultdict(list)
    for (k, o), v in Y.items():
        wi, vi = opts[k][o]; byroot[wi].append(v); byroot[vi].append(v)
    for w in range(len(P)):
        card_eq(byroot[w], 1)
    c2 = collections.defaultdict(list); c3 = collections.defaultdict(list)
    for (k, o), v in Y.items():
        z = zreps[k]; nz = neg(z); wi, vi = opts[k][o]; w, x = P[wi], P[vi]
        for a in z:
            for b in w: c2[a, b].append(v)
        for a in nz:
            for b in x: c2[a, b].append(v)
        for b in w:
            for d in x:
                c3[min(b, d), max(b, d)].append(v)
    for a in range(n2):
        for b in range(n2):
            card_eq(c2[a, b], int(Cx[a, b]))
    for b in range(n2):
        for d in range(b, n2):
            tgt = int(Ct[b, d]) // 2 if b == d else int(Ct[b, d])
            card_eq(c3[b, d], tgt)
    if use_iv:
        # B[y, b] <= options (implication option -> B) ; y indexe les 60 racines lointaines via (k, s) s=0 : z_k, s=1 : -z_k
        Bv = {}
        for (k, o), v in Y.items():
            wi, vi = opts[k][o]
            for s, img in ((0, P[wi]), (1, P[vi])):
                for b in img:
                    key = (k, s, b)
                    if key not in Bv: Bv[key] = pool.id(("B",) + key)
                    cnf.append([-v, Bv[key]])
        roots = [(k, s) for k in range(len(zreps)) for s in (0, 1)]
        rootset = {(k, s): (zreps[k] if s == 0 else neg(zreps[k])) for (k, s) in roots}
        Av = {}
        for y, y2 in itertools.combinations(roots, 2):
            if y[0] == y2[0]: continue
            if len(set(rootset[y]) & set(rootset[y2])) != 1: continue
            a = pool.id(("A", y, y2)); Av[y, y2] = a
            for b in range(n2):
                if (y[0], y[1], b) in Bv and (y2[0], y2[1], b) in Bv:
                    cnf.append([-Bv[(y[0], y[1], b)], -Bv[(y2[0], y2[1], b)], a])
        for (y, y2), a in Av.items():
            ny = (y[0], 1 - y[1]); ny2 = (y2[0], 1 - y2[1])
            key = (ny, ny2) if (ny, ny2) in Av else ((ny2, ny) if (ny2, ny) in Av else None)
            if key is not None and (y, y2) < key:
                cnf.append([-a, -Av[key]])
    return cnf, Y, opts, zreps, P

def verify_bvls():
    """(ii), (iii), (iv) sur BvLS m = 11 (table exacte) : verification directe des formules utilisees."""
    sys.path.insert(0, os.path.join(HERE, "vendor"))
    from sib_partition_check import load, outer_graph
    fr, T = load(11); roots, idx, Hm = outer_graph(fr, T)
    m = 11; n2 = 20
    def root(pairs):
        v = [0] * m
        for (blk, sg) in pairs: v[blk] = sg
        return idx[tuple(v)]
    xs = lambda x: (x // 2 + 1, 1 - 2 * (x % 2))
    e1p = lambda b: root([(0, 1), xs(b)])
    mu = [None] * n2; tau = [None] * n2
    for b in range(n2):
        nb = [b2 for b2 in range(n2) if b2 != b and Hm[e1p(b), e1p(b2)]]; mu[b] = nb[0]
        nc = [c for c in range(n2) if Hm[e1p(b), root([(0, -1), xs(c)])]]; tau[b] = nc[0] ^ 1
    Cx, Ct = targets(mu, tau, n2)
    R = [(a, b) for a in range(n2) for b in range(a + 1, n2) if a // 2 != b // 2]
    Phi = {}
    for z in R:
        zi = root([xs(x) for x in z]); Phi[z] = tuple(sorted(b for b in range(n2) if Hm[e1p(b), zi]))
    neg = lambda z: tuple(sorted((z[0] ^ 1, z[1] ^ 1)))
    C2 = np.zeros((n2, n2), int); C3 = np.zeros((n2, n2), int)
    for z in R:
        for a in z:
            for b in Phi[z]: C2[a, b] += 1
        for b in Phi[z]:
            for d in Phi[neg(z)]: C3[b, d] += 1
    ok2 = (C2 == Cx).all(); ok3 = (C3 == Ct).all()
    ok4 = True
    for z, z2 in itertools.combinations(R, 2):
        if len(set(z) & set(z2)) == 1:
            adj = lambda u, v: len(set(u) & set(v)) > 0
            if adj(Phi[z], Phi[z2]) + adj(Phi[neg(z)], Phi[neg(z2)]) > 1: ok4 = False
    print("BvLS m=11 : (ii) %s, (iii) %s, (iv) %s" % (ok2, ok3, ok4))

if __name__ == "__main__":
    if sys.argv[1] == "verify":
        verify_bvls(); sys.exit()
    ti = int(sys.argv[1]); use_iv = "--no-iv" not in sys.argv
    mu, reps, st = types((1, 1, 1, 1, 1, 1)); tau = reps[ti]
    cnf, Y, opts, zreps, P = build(mu, tau, use_iv=use_iv)
    name = "fsos_A111111_t%d%s" % (ti, "" if use_iv else "_noiv")
    out = os.path.join(HERE, "..", "data", "cnf", name + ".cnf")
    cnf.to_file(out)
    print(name, ": %d variables, %d clauses ; options par paire : min %d max %d" % (cnf.nv, len(cnf.clauses), min(len(o) for o in opts), max(len(o) for o in opts)))
    print("sha256", hashlib.sha256(open(out, "rb").read()).hexdigest())
