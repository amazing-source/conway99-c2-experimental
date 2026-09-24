"""R2 et contraintes d'etiquettes (notes/15).  Enumeration exacte, sans SAT.

Cadre (notes/11, R1) : grille L hors de x passant par w = e1, droites {w, al, be} et {w, ga, de}, al = [e1,a], be = [e1,b],
ga = [e1,c], de = [e1,d] ; coins z_pq (p in {a,b}, q in {c,d}) portant les 8 demi-etiquettes restantes R8 (R1(6)).
phi = t o pi : involution de L de point fixe unique w.

Multiplicites (DERIVE, notes/15 §1) : pour u != v dans L \\ {w},
    m(u,v) := #{voisins communs de u et tv hors de L u tL} = 2 - [u ~ phi(v)] - [phi(u) ~ v] - [phi(u) = v].
Contraintes testees :
  (C3) bloc : le sommet interieur h est voisin commun de lambda(h) et t.lambda(-h), donc m(lambda(h), lambda(-h)) >= 1
       pour chacun des 6 blocs k = 2..7 ;
  (C4) disjonction : L et tL sont disjointes, donc aucune racine de L n'a pour etiquettes les opposees de celles d'une autre.
Coordonnees de grille : w = (0,0), al = (1,0), be = (2,0), ga = (0,1), de = (0,2), z_pq = (i,j).
"""
import itertools, sys
from collections import defaultdict, Counter

PTS = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)]
W = (0, 0)
NAME = {(1, 0): "al", (2, 0): "be", (0, 1): "ga", (0, 2): "de",
        (1, 1): "z_ac", (1, 2): "z_ad", (2, 1): "z_bc", (2, 2): "z_bd"}
REFL = {p: ((-p[0]) % 3, (-p[1]) % 3) for p in PTS}      # reflexion ponctuelle en w

def adj(u, v):
    return u != v and (u[0] == v[0] or u[1] == v[1])

def involutions(pts):
    if not pts:
        yield {}
        return
    p = pts[0]
    for i in range(1, len(pts)):
        q = pts[i]
        rest = pts[1:i] + pts[i + 1:]
        for m in involutions(rest):
            d = dict(m); d[p] = q; d[q] = p
            yield d

PHIS = list(involutions(PTS))                          # 105

def mult(phi, u, v):
    return 2 - adj(u, phi[v]) - adj(phi[u], v) - (phi[u] == v)

# types de {a,b,c,d} : demi-etiquettes (bloc, signe), blocs 2..7
TYPES = {
    "T1 SS (b=-a, d=-c)":        ((2, 1), (2, -1), (3, 1), (3, -1)),
    "T2 S. (b=-a)":              ((2, 1), (2, -1), (3, 1), (4, 1)),
    "T3 NN (4 blocs)":           ((2, 1), (3, 1), (4, 1), (5, 1)),
    "T4a (c=-a)":                ((2, 1), (3, 1), (2, -1), (4, 1)),
    "T4b (c=-a, d=-b)":          ((2, 1), (3, 1), (2, -1), (3, -1)),
}

def layouts(r8):
    """Repartitions de R8 sur les 4 coins (ordonnes), 2 etiquettes de blocs differents par coin."""
    r8 = sorted(r8)
    def rec(rest, k):
        if k == 4:
            yield []
            return
        first = rest[0]
        for j in range(1, len(rest)):
            s = rest[j]
            if s[0] == first[0]:
                continue
            for tail in rec(rest[1:j] + rest[j + 1:], k + 1):
                yield [(first, s)] + tail
    corners = [(1, 1), (1, 2), (2, 1), (2, 2)]
    for pairs in rec(r8, 0):
        for perm in itertools.permutations(pairs):
            yield dict(zip(corners, perm))

def analyse(tname, abcd, out):
    a, b, c, d = abcd
    H = [(k, s) for k in range(2, 8) for s in (1, -1)]
    r8 = [h for h in H if h not in abcd]
    lab = {(1, 0): {a}, (2, 0): {b}, (0, 1): {c}, (0, 2): {d}}   # etiquette hors e1 des racines de P
    neg = lambda h: (h[0], -h[1])
    phi_ok = Counter(); phi_lay = defaultdict(int); n_lay = 0
    for lay in layouts(r8):
        L = dict(lab)
        for z, pr in lay.items():
            L[z] = set(pr)
        # (C4) aucune racine de L n'est t d'une autre (seuls les coins comptent : P contient e1)
        ok4 = all(L[z2] != {neg(h) for h in L[z1]} for z1 in lay for z2 in lay if z1 != z2)
        if not ok4:
            continue
        n_lay += 1
        where = {}
        for p, S in L.items():
            for h in S:
                where[h] = p
        blocks = [(where[(k, 1)], where[(k, -1)]) for k in range(2, 8)]
        for idx, phi in enumerate(PHIS):
            if all(mult(phi, u, v) >= 1 for u, v in blocks):      # (C3)
                phi_ok[idx] += 1
    out.append("== %s : %d dispositions valides (C4)" % (tname, n_lay))
    for idx, cnt in sorted(phi_ok.items(), key=lambda kv: -kv[1]):
        phi = PHIS[idx]
        pairs = sorted({tuple(sorted((NAME[u], NAME[v]))) for u, v in phi.items()})
        lines = (phi[(1, 0)] == (2, 0)) + (phi[(0, 1)] == (0, 2))
        tag = "REFLEXION" if phi == REFL else ("droites R2" if lines == 2 else "droites R2 : %d/2" % lines)
        out.append("   phi = %-58s  %-16s  dispositions : %d" % (" ".join("(%s %s)" % p for p in pairs), tag, cnt))

if __name__ == "__main__":
    out = ["involutions phi : %d" % len(PHIS)]
    for tname, abcd in TYPES.items():
        analyse(tname, abcd, out)
    print("\n".join(out))


# ---------------------------------------------------------------------------------------------------------------
# (C8) Lemme S1 vu depuis w (valable dans toute carte, sans involution) : L est une grille par le centre w.
# Les 40 w-racines evitant les blocs {al,be}, {ga,de} se partitionnent en N0(z) (z coin, cls(y) = unique coin voisin) ;
# un y evitant a exactement 1 voisin evitant dans sa classe, 1 dans chaque classe soeur, 2 dans la classe opposee.
# (C8') une w-racine touchant un seul bloc, par le point eps de P, a 1 voisin evitant dans N0(z) pour les 2 coins z ~ eps,
# 2 pour les 2 autres.
# Sommets connus : h in R8 (evitant, classe lambda(h)) ; h in {a,b,c,d} (touche par lambda(h)) ;
# tu (u != w) : evitant de classe phi(u) si phi(u) est un coin, sinon touche par phi(u).
# Aretes connues : h ~ -h ; h ~ tu ssi -h in L(u) ; tu ~ tv ssi u ~ v dans la grille.
def s1w_ok(phi, L, where, r8, abcd):
    corners = [(1, 1), (1, 2), (2, 1), (2, 2)]
    isK = lambda p: p in corners
    neg = lambda h: (h[0], -h[1])
    nodes = {}                                   # nom -> ("av", classe) ou ("t1", eps)
    for h in r8:
        nodes[("h", h)] = ("av", where[h])
    for h in abcd:
        nodes[("h", h)] = ("t1", where[h])
    for u in PTS:
        nodes[("t", u)] = ("av", phi[u]) if isK(phi[u]) else ("t1", phi[u])
    def nbrs(n):
        kind, obj = n
        out = []
        if kind == "h":
            if ("h", neg(obj)) in nodes:
                out.append(("h", neg(obj)))
            out += [("t", u) for u in PTS if neg(obj) in L[u]]
        else:
            out += [("h", neg(h)) for h in L[obj] if h != (1, 1) and ("h", neg(h)) in nodes]
            out += [("t", v) for v in PTS if adj(obj, v)]
        return out
    for n, (st, lab) in nodes.items():
        cnt = Counter(nodes[m][1] for m in nbrs(n) if nodes[m][0] == "av")
        for z, k in cnt.items():
            if st == "av":
                cap = 1 if (z == lab or adj(z, lab)) else 2          # propre / soeur : 1 ; opposee : 2
            else:
                cap = 1 if adj(z, lab) else 2                         # coin voisin de eps : 1 ; sinon 2
            if k > cap:
                return False
    return True

def analyse2(tname, abcd, out):
    a, b, c, d = abcd
    H = [(k, s) for k in range(2, 8) for s in (1, -1)]
    r8 = [h for h in H if h not in abcd]
    neg = lambda h: (h[0], -h[1])
    phi_ok = Counter(); n_lay = 0
    for lay in layouts(r8):
        L = {(1, 0): {(1, 1), a}, (2, 0): {(1, 1), b}, (0, 1): {(1, 1), c}, (0, 2): {(1, 1), d}}   # (1,1) = e1
        for z, pr in lay.items():
            L[z] = set(pr)
        if not all(L[z2] != {neg(h) for h in L[z1]} for z1 in lay for z2 in lay if z1 != z2):
            continue
        n_lay += 1
        where = {}
        for p, S in L.items():
            for h in S:
                if h != (1, 1):
                    where[h] = p
        blocks = [(where[(k, 1)], where[(k, -1)]) for k in range(2, 8)]
        for idx, phi in enumerate(PHIS):
            if all(mult(phi, u, v) >= 1 for u, v in blocks) and s1w_ok(phi, L, where, r8, abcd):
                phi_ok[idx] += 1
    out.append("== %s : %d dispositions, %d phi survivants apres (C3)+(C4)+(C8)" % (tname, n_lay, len(phi_ok)))
    for idx, cnt in sorted(phi_ok.items(), key=lambda kv: -kv[1]):
        phi = PHIS[idx]
        pairs = sorted({tuple(sorted((NAME[u], NAME[v]))) for u, v in phi.items()})
        lines = (phi[(1, 0)] == (2, 0)) + (phi[(0, 1)] == (0, 2))
        tag = "REFLEXION" if phi == REFL else ("droites R2" if lines == 2 else "droites R2 : %d/2" % lines)
        out.append("   phi = %-58s  %-16s  dispositions : %d" % (" ".join("(%s %s)" % p for p in pairs), tag, cnt))

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "s1w":
    out = []
    for tname, abcd in TYPES.items():
        analyse2(tname, abcd, out)
    print("\n".join(out))
