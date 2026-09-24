"""Quelles contraintes du modele complet une refutation DRAT utilise-t-elle ? (notes/19 §12)

Reconstruit orbit_sat.build(7, "none") (+ clauses unitaires Sigma comme make_cnf.py) en etiquetant chaque clause par son groupe :
  ("R",U) ("D",U) ("I",U,c) ("Psame",U,V) ("Pcross",U,V) ("def",...) (definitions de produits) ("sigma",paire).
Puis lit le noyau ecrit par drat-trim (-c) et compte, pour chaque groupe, combien de ses clauses y figurent.
Resume : lignes U dont (R)/(D)/(I) servent, couples (U,V) dont (P) sert, et leur position par rapport a Sigma.
Usage : python core_groups.py <nom_cnf> "<paires Sigma>" [exact]
"""
import sys, collections, itertools
sys.path.insert(0, "scripts")
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType

def build_labeled(m=7):
    k = 2 * m
    outer = [(i, j, e) for i in range(1, m + 1) for j in range(i + 1, m + 1) for e in (0, 1)]
    N = len(outer)
    rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
    trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
    pool = IDPool(); clauses = []; labels = []
    A = {}; B = {}
    for U in range(N):
        for V in range(U + 1, N):
            A[U, V] = A[V, U] = pool.id(("a", U, V)); B[U, V] = B[V, U] = pool.id(("b", U, V))
    def add(cls, lab):
        for c in cls:
            clauses.append(c); labels.append(lab)
    def prod(x, y):
        p = pool.id(("p", min(x, y), max(x, y)))
        add([[-p, x], [-p, y], [p, -x, -y]], ("def",)); return p
    def eq(lits, kk, lab):
        if kk < 0 or kk > len(lits):
            add([[]], lab); return
        add(CardEnc.equals(lits=lits, bound=kk, vpool=pool, encoding=EncType.seqcounter).clauses, lab)
    inner = [(i, s) for i in range(1, m + 1) for s in (0, 1)]
    for U in range(N):
        others = [V for V in range(N) if V != U]
        eq([A[U, V] for V in others] + [B[U, V] for V in others], k - 2, ("R", U))
        eq([prod(A[U, V], B[U, V]) for V in others], 1, ("D", U))
        for c in inner:
            partner = (c[0], 1 - c[1]); lits = []
            for V in others:
                if c in rep[V]: lits.append(A[U, V])
                if c in trep[V]: lits.append(B[U, V])
            eq(lits, 1 if (c in rep[U] or partner in rep[U]) else 2, ("I", U, c))
    for U in range(N):
        for V in range(U + 1, N):
            Ws = [W for W in range(N) if W != U and W != V]
            same = [prod(A[U, W], A[V, W]) for W in Ws] + [prod(B[U, W], B[V, W]) for W in Ws]
            cross = [prod(A[U, W], B[V, W]) for W in Ws] + [prod(B[U, W], A[V, W]) for W in Ws]
            eq(same + [A[U, V]], 2 - len(rep[U] & rep[V]), ("Psame", U, V))
            eq(cross + [B[U, V]], 2 - len(rep[U] & trep[V]), ("Pcross", U, V))
    return clauses, labels, outer, A, B, pool

if __name__ == "__main__":
    name, ps = sys.argv[1], sys.argv[2]
    exact = len(sys.argv) > 3 and sys.argv[3] == "exact"
    E = [(int(x[0]), int(x[1])) for x in ps.split()]
    clauses, labels, outer, A, B, pool = build_labeled()
    idx = {o: t for t, o in enumerate(outer)}
    for (i, j) in E:
        U, V = idx[(i, j, 0)], idx[(i, j, 1)]
        clauses += [[A[U, V]], [B[U, V]]]; labels += [("sigma", (i, j))] * 2
    if exact:
        for (i, j) in itertools.combinations(range(1, 8), 2):
            if (i, j) in E: continue
            U, V = idx[(i, j, 0)], idx[(i, j, 1)]
            clauses.append([-A[U, V], -B[U, V]]); labels.append(("nonsigma", (i, j)))
    where = collections.defaultdict(list)
    for t, c in enumerate(clauses):
        where[tuple(sorted(c))].append(t)
    core = []
    for line in open("data/tmp/%s.core.cnf" % name):
        if line.startswith(("c", "p")) or not line.strip():
            continue
        lits = tuple(sorted(int(x) for x in line.split()[:-1]))
        core.append(lits)
    used = collections.Counter(); unknown = 0
    for c in core:
        ts = where.get(c)
        if not ts:
            unknown += 1; continue
        for lab in set(labels[t] for t in ts):
            used[lab] += 1
    rows = collections.Counter(); pairs = collections.Counter(); kinds = collections.Counter()
    for lab, n in used.items():
        kinds[lab[0]] += n
        if lab[0] in ("R", "D", "I"):
            rows[lab[1]] += n
        elif lab[0] in ("Psame", "Pcross"):
            pairs[(lab[1], lab[2])] += n
    sis = set(E)
    def pr(U):
        i, j, e = outer[U]; return (i, j)
    def tag(U):
        return "S" if pr(U) in sis else "."
    print("%s : noyau de %d clauses (%d non retrouvees)" % (name, len(core), unknown))
    print("clauses du noyau par type :", dict(kinds))
    print("lignes dont (R)/(D)/(I) servent : %d sur 42" % len(rows))
    print("   ", " ".join("%d%d%s%s" % (outer[U][0], outer[U][1], "+-"[outer[U][2]], tag(U)) for U in sorted(rows)))
    print("couples (U,V) dont (P) sert : %d sur 861" % len(pairs))
    cls = collections.Counter()
    for (U, V) in pairs:
        cls[(tag(U) + tag(V)).replace(".S", "S.")] += 1
    print("   par statut (S = orbite d'une paire soeur) :", dict(cls))
    blocks_used = collections.Counter()
    for (U, V) in pairs:
        for W in (U, V):
            if tag(W) == ".":
                blocks_used[pr(W)] += 1
    print("   paires non soeurs impliquees dans (P), par frequence :", ", ".join("%d%d:%d" % (p[0], p[1], n) for p, n in blocks_used.most_common()))

def build_labeled_rsf(S, sigma=(), sigma_exact=False, m=7):
    """Copie etiquetee de row_system_full.build (meme ordre, memes identifiants) : renvoie (clauses, labels, outer, A, B)."""
    k = 2 * m
    outer = [(i, j, e) for i in range(1, m + 1) for j in range(i + 1, m + 1) for e in (0, 1)]
    N = len(outer)
    rep = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer]
    trep = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer]
    S = set(S)
    inrow = lambda U, V: U in S or V in S
    pool = IDPool(); clauses = []; labels = []
    A = {}; B = {}
    for U in range(N):
        for V in range(U + 1, N):
            A[U, V] = A[V, U] = pool.id(("a", U, V)); B[U, V] = B[V, U] = pool.id(("b", U, V))
    def add(cls, lab):
        for c in cls:
            clauses.append(c); labels.append(lab)
    def prod(x, y):
        p = pool.id(("p", min(x, y), max(x, y)))
        add([[-p, x], [-p, y], [p, -x, -y]], ("def",)); return p
    def eq(lits, kk, lab):
        if not lits:
            return
        if kk < 0 or kk > len(lits):
            add([[]], lab); return
        add(CardEnc.equals(lits=lits, bound=kk, vpool=pool, encoding=EncType.seqcounter).clauses, lab)
    inner = [(i, s) for i in range(1, m + 1) for s in (0, 1)]
    for U in range(N):
        others = [V for V in range(N) if V != U]
        if not all(inrow(U, V) for V in others):
            continue
        eq([A[U, V] for V in others] + [B[U, V] for V in others], k - 2, ("R", U))
        eq([prod(A[U, V], B[U, V]) for V in others], 1, ("D", U))
        for c in inner:
            partner = (c[0], 1 - c[1]); lits = []
            for V in others:
                if c in rep[V]: lits.append(A[U, V])
                if c in trep[V]: lits.append(B[U, V])
            eq(lits, 1 if (c in rep[U] or partner in rep[U]) else 2, ("I", U, c))
    for U in range(N):
        for V in range(U + 1, N):
            Ws = [W for W in range(N) if W != U and W != V]
            if not (inrow(U, V) and all(inrow(U, W) and inrow(V, W) for W in Ws)):
                continue
            same = [prod(A[U, W], A[V, W]) for W in Ws] + [prod(B[U, W], B[V, W]) for W in Ws]
            cross = [prod(A[U, W], B[V, W]) for W in Ws] + [prod(B[U, W], A[V, W]) for W in Ws]
            eq(same + [A[U, V]], 2 - len(rep[U] & rep[V]), ("Psame", U, V))
            eq(cross + [B[U, V]], 2 - len(rep[U] & trep[V]), ("Pcross", U, V))
    idx = {o: t for t, o in enumerate(outer)}
    for (i, j) in sigma:
        U = idx[(i, j, 0)]; V = idx[(i, j, 1)]
        add([[A[U, V]], [B[U, V]]], ("sigma", (i, j)))
    if sigma_exact:
        Es = set(tuple(sorted(p)) for p in sigma)
        for (i, j) in sorted({outer[U][:2] for U in S}):
            if (i, j) in Es: continue
            U = idx[(i, j, 0)]; V = idx[(i, j, 1)]
            add([[-A[U, V], -B[U, V]]], ("nonsigma", (i, j)))
    return clauses, labels, outer, A, B
