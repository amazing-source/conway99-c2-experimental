"""q:parite (notes/22 §5) : parites de Burnside a l'ordre 7 sous t, pour C2.
Source des frequences d'ordre 7 : famille affine independante (repo_family_affine.json, archive en lecture seule), qui concorde avec
Reimbayev (arXiv 2608.19410) corrige de 4 coquilles (audit conway99-involution/notes/AUDIT_reimbayev_order7.md) :
f_H = p + q*n3 + r*z, z = z11/4, a (99,14).
En C2 : n3 = n_one (mod 2) [note 20], S = 0 (mod 4) et z11 = 4 n_one (mod 8) [note 22, via L18 de C1], donc z = n_one (mod 2).
Burnside : f_H = #{copies t-invariantes de H} (mod 2) ; toute copie t-invariante d'un graphe a 7 sommets contient x.
"""
import json, itertools, sys
from math import comb
from fractions import Fraction as F
SRC = r"C:/home/researcher/Desktop/conway99-lab-archive/temp_session_eeaf2d22/scratchpad/r7_check/repo_family_affine.json"
PAIRS = [(i, j) for i in range(7) for j in range(i + 1, 7)]
BIT = {p: b for b, p in enumerate(PAIRS)}
PERMS = list(itertools.permutations(range(7)))

def mask_of(edges):
    return sum(1 << BIT[(min(a, b), max(a, b))] for a, b in edges)
def edges_of(m):
    return [PAIRS[b] for b in range(21) if m >> b & 1]
def canon(m):
    E = edges_of(m)
    return min(mask_of([(p[a], p[b]) for a, b in E]) for p in PERMS)

d = json.load(open(SRC))
cls = d["classes"]; P = [F(x) for x in d["p"]]; Q = [F(x) for x in d["q"]]; R = [F(x) for x in d["r"]]
fam = {c: (P[i], Q[i], R[i]) for i, c in enumerate(cls)}
if __name__ == "__main__":
    ok = all(canon(c) == c for c in cls)
    print("classes : %d ; toutes canoniques (masque minimal, ordre lexicographique des paires) : %s" % (len(cls), ok))
    print("somme des p = %s ; C(99,7) = %d ; somme des q = %s ; somme des r = %s" % (sum(P), comb(99, 7), sum(Q), sum(R)))
    print("denominateurs : p %s, q %s, r %s" % ({x.denominator for x in P}, {x.denominator for x in Q}, {x.denominator for x in R}))
    H = canon(mask_of([(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (5, 6), (6, 3)]))     # K3 + C4
    print("K3 + C4 : masque canonique %d ; present : %s" % (H, H in fam))
    if H in fam:
        p, q, r = fam[H]
        print("  f = %s + %s n3 + %s z   (z = z11/4)" % (p, q, r))
        print("  f mod 2 = %d + %d * n_one   (avec n3 = z = n_one mod 2)" % (p % 2, (q + r) % 2))
        print("  Burnside : f = 5 n_sib + 4 n_one + 3 n_dis = 1 + n_one (mod 2)")

# ---------------------------------------------------------------- balayage systematique (types a >= 2 orbites interieures)
def adj(E):
    A = [[0] * 7 for _ in range(7)]
    for a, b in E: A[a][b] = A[b][a] = 1
    return A

def valid_involutions(m):
    """involutions de H a exactement 1 point fixe, compatibles avec C2 : pour chaque paire {u, gu} :
    u ~ gu  <=>  u ~ v  <=>  gu ~ v   (v = point fixe = x). Renvoie la liste des nombres d'orbites interieures."""
    E = edges_of(m); A = adj(E); Es = set(E); out = []
    for p in PERMS:
        if any(p[p[i]] != i for i in range(7)): continue
        fx = [i for i in range(7) if p[i] == i]
        if len(fx) != 1: continue
        if any((min(p[a], p[b]), max(p[a], p[b])) not in Es for a, b in E): continue     # automorphisme
        v = fx[0]; ok = True; ninner = 0
        for u in range(7):
            if u == v or u > p[u]: continue
            w = p[u]
            if not (A[u][w] == A[u][v] == A[w][v]): ok = False; break
            ninner += A[u][w]
        if ok: out.append(ninner)
    return out

def chart_AB_counts():
    """copies t-invariantes de types A (3 orbites interieures) et B (2 interieures + 1 racine), toutes determinees par la carte."""
    inner = [(c, s) for c in range(7) for s in (1, -1)]
    roots = [frozenset([(i, si), (j, sj)]) for i in range(7) for j in range(i + 1, 7) for si in (1, -1) for sj in (1, -1)]
    rorb = {}
    for r in roots:
        key = frozenset([r, frozenset((c, -s) for (c, s) in r)]); rorb[key] = 1
    rorb = list(rorb)
    tally = {}
    def add(verts):
        # verts : liste de 7 sommets ('x', ('i',c,s)) ou ('r', frozenset)
        E = []
        for a, b in itertools.combinations(range(7), 2):
            u, w = verts[a], verts[b]
            if u == "x" or w == "x":
                o = w if u == "x" else u
                if o[0] == "i": E.append((a, b))
            elif u[0] == "i" and w[0] == "i":
                if u[1] == w[1]: E.append((a, b))            # e_c ~ -e_c
            elif u[0] == "r" and w[0] == "r":
                pass                                          # meme orbite de racines : r non adjacent a -r
            else:
                i_, r_ = (u, w) if u[0] == "i" else (w, u)
                if (i_[1], i_[2]) in r_[1]: E.append((a, b))
        c = canon(mask_of(E)); tally[c] = tally.get(c, 0) + 1
    for trip in itertools.combinations(range(7), 3):
        verts = ["x"] + [("i", c, s) for c in trip for s in (1, -1)]
        add(verts)
    for pair in itertools.combinations(range(7), 2):
        for R in rorb:
            rr = list(R)
            verts = ["x"] + [("i", c, s) for c in pair for s in (1, -1)] + [("r", rr[0]), ("r", rr[1])]
            add(verts)
    return tally

def sweep():
    tally = chart_AB_counts()
    print("copies t-invariantes de types A/B : %d (attendu 35 + 882 = 917), classes touchees : %d" % (sum(tally.values()), len(tally)))
    rows = []
    for c in cls:
        inv = valid_involutions(c)
        if not inv: continue
        p, q, r = fam[c]
        det = all(n >= 2 for n in inv)
        rows.append((c, sorted(set(inv)), det, tally.get(c, 0), p, q, r))
    print("classes admettant une involution C2-compatible : %d" % len(rows))
    bad = []; cons = []
    for (c, inv, det, t, p, q, r) in rows:
        if not det: continue
        fp, fq = int(p) % 2, int(q + r) % 2
        verdict = ("coherent (identite)" if fq == 0 and fp == t % 2 else
                   "CONTRADICTION" if fq == 0 else
                   "contrainte : n_one = %d (mod 2)" % ((t - fp) % 2))
        if verdict.startswith("CONTRADICTION"): bad.append(c)
        if verdict.startswith("contrainte"): cons.append((c, (t - fp) % 2))
        print("  classe %6d : orbites interieures %s ; copies t-inv %d ; f = %s %+d n3 %+d z ; f mod 2 = %d + %d n_one -> %s"
              % (c, inv, t, p, int(q), int(r), fp, fq, verdict))
    print("classes non determinees par la carte (une involution avec 0 ou 1 orbite interieure) : %d" % sum(1 for x in rows if not x[2]))
    print("CONTRADICTIONS : %s ; contraintes sur n_one : %s" % (bad, cons))

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "sweep":
    sweep()
