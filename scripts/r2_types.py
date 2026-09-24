"""Types locaux des phi survivants autour d'une grille hors de x (notes/15).  Enumeration exacte, sans SAT.

Configuration locale = (disposition des 12 demi-etiquettes sur L \\ {w}, phi) passant les filtres exacts
(C3) blocs : m(lambda(h), lambda(-h)) >= 1 ; (C4) L et tL disjointes ; (C8) lemme S1 vu depuis w (voir r2_label_constraints.py).
Symetries locales (stabilisateur de w) : W(B6) (signes et permutations des blocs 2..7) x D4 (symetries de la grille fixant w).
Deux configurations equivalentes sous ce groupe = meme type local.

Objets calcules pour chaque type :
- forme de phi (transpositions P-P / P-K / K-K), statut « droites R2 », reflexion complete ;
- carres D internes (R1(5)) et leur type sib / one / dis ;
- tau force : phi echange [e1,p] et [e1,q] <=> tau(p) = q (tau = involution canonique autour de w : [e1,h] ~ t[e1,tau(h)]) ;
  hors de ces paires, tau n'est PAS determine par la configuration locale (seulement tau(p) dans R8 si phi envoie [e1,p] sur un coin) ;
- ombre sur les etiquettes Phi (definie seulement si phi(P) = P) : Phi envoie les etiquettes de u sur celles de phi(u) ;
  2 choix par echange de coins ; on donne le type de cycles de Phi.nu et l'existence d'elements d'ordre 3 dans <Phi, nu> ;
- stabilisateur du type (symetries locales g qui fixent tout) : candidats « g » a propager.
"""
import itertools, sys
from collections import Counter, defaultdict
from math import gcd

PTS = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)]
PPOS = PTS[:4]; KPOS = PTS[4:]
NAME = {(1, 0): "al", (2, 0): "be", (0, 1): "ga", (0, 2): "de",
        (1, 1): "z_ac", (1, 2): "z_ad", (2, 1): "z_bc", (2, 2): "z_bd", (0, 0): "w"}
E1 = (1, 1)                                   # demi-etiquette e1 (bloc 1, signe +)
neg = lambda h: (h[0], -h[1])

def adj(u, v):
    return u != v and (u[0] == v[0] or u[1] == v[1])

def involutions(pts):
    if not pts:
        yield {}
        return
    p = pts[0]
    for i in range(1, len(pts)):
        rest = pts[1:i] + pts[i + 1:]
        for m in involutions(rest):
            d = dict(m); d[p] = pts[i]; d[pts[i]] = p
            yield d

PHIS = list(involutions(PTS))
REFL = {p: ((-p[0]) % 3, (-p[1]) % 3) for p in PTS}

def mult(phi, u, v):
    return 2 - adj(u, phi[v]) - adj(phi[u], v) - (phi[u] == v)

# D4 : symetries de la grille F3^2 fixant w et preservant {droite 1, droite 2}
def d4():
    gens = [lambda p: ((-p[0]) % 3, p[1]), lambda p: (p[0], (-p[1]) % 3), lambda p: (p[1], p[0])]
    grp = {tuple(PTS)}
    frontier = [tuple(PTS)]
    while frontier:
        new = []
        for img in frontier:
            for g in gens:
                im2 = tuple(g(q) for q in img)
                if im2 not in grp:
                    grp.add(im2); new.append(im2)
        frontier = new
    return [dict(zip(PTS, img)) for img in grp]
D4 = d4()
assert len(D4) == 8

TYPES = {
    "T1": ((2, 1), (2, -1), (3, 1), (3, -1)),     # deux droites soeurs
    "T2": ((2, 1), (2, -1), (3, 1), (4, 1)),      # une droite soeur
    "T3": ((2, 1), (3, 1), (4, 1), (5, 1)),       # quatre blocs
    "T4a": ((2, 1), (3, 1), (2, -1), (4, 1)),     # c = -a
    "T4b": ((2, 1), (3, 1), (2, -1), (3, -1)),    # c = -a, d = -b
}
H = [(k, s) for k in range(2, 8) for s in (1, -1)]

def layouts(r8):
    r8 = sorted(r8)
    def rec(rest):
        if not rest:
            yield []
            return
        f = rest[0]
        for j in range(1, len(rest)):
            if rest[j][0] == f[0]:
                continue
            for tail in rec(rest[1:j] + rest[j + 1:]):
                yield [(f, rest[j])] + tail
    for pairs in rec(r8):
        for perm in itertools.permutations(pairs):
            yield dict(zip(KPOS, [frozenset(p) for p in perm]))

def residual_group(lab):
    """(d, s) avec d dans D4, s signe-permutation des blocs 2..7, s(lab[p]) = lab[d(p)] pour p dans P."""
    out = []
    pblocks = sorted({lab[p][0] for p in PPOS})
    free = [k for k in range(2, 8) if k not in pblocks]
    for d in D4:
        perm, sign, ok = {}, {}, True
        for p in PPOS:
            (k, e), (k2, e2) = lab[p], lab[d[p]]
            if k in perm and (perm[k] != k2 or sign[k] != e * e2):
                ok = False; break
            perm[k] = k2; sign[k] = e * e2
        if not ok or sorted(perm.values()) != pblocks:
            continue
        for fp in itertools.permutations(free):
            for sg in itertools.product((1, -1), repeat=len(free)):
                P2 = dict(perm); S2 = dict(sign)
                for k, k2, s_ in zip(free, fp, sg):
                    P2[k] = k2; S2[k] = s_
                out.append((d, P2, S2))
    return out

def act_label(g, h):
    d, P, S = g
    return h if h == E1 else (P[h[0]], h[1] * S[h[0]])

def act_layout(g, L):
    d = g[0]
    return {d[z]: frozenset(act_label(g, h) for h in L[z]) for z in KPOS}

def enc(L):
    return tuple(tuple(sorted(L[z])) for z in KPOS)

def full_labels(lab, L):
    F = {p: frozenset([E1, lab[p]]) for p in PPOS}
    F.update(L)
    return F

def c4_ok(L):
    return all(L[z2] != frozenset(neg(h) for h in L[z1]) for z1 in KPOS for z2 in KPOS if z1 != z2)

def c3_ok(phi, where):
    return all(mult(phi, where[(k, 1)], where[(k, -1)]) >= 1 for k in range(2, 8))

def c8_ok(phi, F, where, lab, r8):
    nodes = {}
    for h in r8:
        nodes[("h", h)] = ("av", where[h])
    for p in PPOS:
        nodes[("h", lab[p])] = ("t1", p)
    for u in PTS:
        nodes[("t", u)] = ("av", phi[u]) if phi[u] in KPOS else ("t1", phi[u])
    def nbrs(n):
        kind, obj = n
        if kind == "h":
            out = [("h", neg(obj))] if ("h", neg(obj)) in nodes else []
            return out + [("t", u) for u in PTS if neg(obj) in F[u]]
        return [("h", neg(h)) for h in F[obj] if h != E1 and ("h", neg(h)) in nodes] + [("t", v) for v in PTS if adj(obj, v)]
    for n, (st, labn) in nodes.items():
        cnt = Counter(nodes[m][1] for m in nbrs(n) if nodes[m][0] == "av")
        for z, k in cnt.items():
            cap = (1 if (z == labn or adj(z, labn)) else 2) if st == "av" else (1 if adj(z, labn) else 2)
            if k > cap:
                return False
    return True

def lcm(a, b):
    return a * b // gcd(a, b)

def cycles(perm):
    seen, cyc = set(), []
    for x in perm:
        if x in seen:
            continue
        n, y = 0, x
        while y not in seen:
            seen.add(y); y = perm[y]; n += 1
        cyc.append(n)
    return sorted(cyc, reverse=True)

def pos_class(u):
    return "P" if u in PPOS else "K"

def describe(lab, L, phi):
    F = full_labels(lab, L)
    trans = sorted({tuple(sorted((u, phi[u]))) for u in PTS})
    shape = " ".join("(%s %s)" % (NAME[u], NAME[v]) for u, v in trans)
    kinds = Counter(pos_class(u) + pos_class(v) for u, v in trans)
    lines = (phi[(1, 0)] == (2, 0), phi[(0, 1)] == (0, 2))
    # carres D internes (R1(5)) : echanges entre voisins de la grille
    dsq = []
    for u, v in trans:
        if not adj(u, v):
            continue
        side1 = {u, v} in ({(1, 0), (2, 0)}, {(0, 1), (0, 2)})          # troisieme point = w = e1 (interieur)
        side2 = bool(F[v] & frozenset(neg(h) for h in F[u]))
        dsq.append({2: "sib", 1: "one", 0: "dis"}[side1 + side2])
    # tau force et omega = tau.nu force
    tau = {}
    for u, v in trans:
        if u in PPOS and v in PPOS:
            tau[lab[u]] = lab[v]; tau[lab[v]] = lab[u]
    M1 = {lab[(1, 0)]: lab[(2, 0)], lab[(2, 0)]: lab[(1, 0)], lab[(0, 1)]: lab[(0, 2)], lab[(0, 2)]: lab[(0, 1)]}
    closing = sum(1 for p in tau if tau[p] == M1[p]) // 2
    arcs = sum(1 for p in tau if tau[p] == neg(p)) // 2
    omega = {neg(p): q for p, q in tau.items()}
    # ombre Phi sur les etiquettes (si phi(P) = P)
    shadow = None
    if all(phi[p] in PPOS for p in PPOS):
        base = {lab[p]: lab[phi[p]] for p in PPOS}
        cpairs = [(u, v) for u, v in trans if u in KPOS]
        res = []
        for choice in itertools.product((0, 1), repeat=len(cpairs)):
            Phi = dict(base)
            for (u, v), ch in zip(cpairs, choice):
                a1, a2 = sorted(L[u]); b1, b2 = sorted(L[v])
                if ch:
                    b1, b2 = b2, b1
                Phi[a1] = b1; Phi[b1] = a1; Phi[a2] = b2; Phi[b2] = a2
            PhiNu = {h: Phi[neg(h)] for h in H}
            cyc = cycles(PhiNu)
            o = 1
            for c_ in cyc:
                o = lcm(o, c_)
            commute = all(Phi[neg(h)] == neg(Phi[h]) for h in H)
            res.append((tuple(cyc), o, commute))
        shadow = res
    return dict(shape=shape, kinds=dict(kinds), lines=lines, refl=(phi == REFL), dsq=sorted(dsq),
                tau=tau, closing=closing, arcs=arcs, omega=omega, shadow=shadow)

def run(tname, abcd, out, summary):
    lab = dict(zip(PPOS, abcd))
    r8 = [h for h in H if h not in abcd]
    G = residual_group(lab)
    lays = [L for L in layouts(r8) if c4_ok(L)]
    seen = set(); reps = []
    for L in lays:
        e = enc(L)
        if e in seen:
            continue
        orb = {enc(act_layout(g, L)) for g in G}
        seen |= orb
        mn = min(orb)
        rep = next(act_layout(g, L) for g in G if enc(act_layout(g, L)) == mn)
        reps.append((rep, len(orb)))
    types = []
    for rep, osize in reps:
        F = full_labels(lab, rep)
        where = {h: p for p, S in F.items() for h in S if h != E1}
        stab = [g for g in G if enc(act_layout(g, rep)) == enc(rep)]
        surv = [phi for phi in PHIS if c3_ok(phi, where) and c8_ok(phi, F, where, lab, r8)]
        done = set()
        for phi in surv:
            key = tuple(sorted(phi.items()))
            if key in done:
                continue
            orbphi = set()
            for g in stab:
                d = g[0]
                ph2 = {d[u]: d[phi[u]] for u in PTS}
                orbphi.add(tuple(sorted(ph2.items())))
            done |= orbphi
            fixers = [g for g in stab if all(g[0][phi[u]] == phi[g[0][u]] for u in PTS)]
            types.append((rep, osize, phi, len(orbphi), len(fixers), fixers))
    out.append("== %s  a,b,c,d = %s : |groupe residuel| = %d ; dispositions : %d (%d orbites) ; types locaux : %d"
               % (tname, abcd, len(G), len(lays), len(reps), len(types)))
    shapes = defaultdict(list)
    for rep, osize, phi, nphi, nfix, fixers in types:
        D = describe(lab, rep, phi)
        shapes[D["shape"]].append((rep, osize, nphi, nfix, fixers, D))
    for shape, lst in sorted(shapes.items(), key=lambda kv: -len(kv[1])):
        D = lst[0][5]
        tag = "REFLEXION" if D["refl"] else ("droites R2" if all(D["lines"]) else "R2 %d/2" % sum(D["lines"]))
        out.append("  forme %-50s %-11s PP/PK/KK=%s  carres D internes=%s  tau force=%d paires (fermantes %d, arcs %d) : %d types"
                   % (shape, tag, "/".join(str(D["kinds"].get(k, 0)) for k in ("PP", "PK", "KK")), D["dsq"],
                      len(D["tau"]) // 2, D["closing"], D["arcs"], len(lst)))
        for rep, osize, nphi, nfix, fixers, D in lst:
            corners = " ".join("%s=%s" % (NAME[z], "".join(("+" if s > 0 else "-") + str(k) for k, s in sorted(rep[z]))) for z in KPOS)
            sh = ""
            if D["shadow"] is not None:
                cyc = Counter((c, o, cm) for c, o, cm in D["shadow"])
                sh = " ; ombre Phi : " + ", ".join("Phi.nu cycles %s ordre %d%s x%d" % (list(c), o, " (commute a nu)" if cm else "", n)
                                                    for (c, o, cm), n in sorted(cyc.items()))
            gs = ""
            if nfix > 1:
                nontriv = [g for g in fixers if not (all(g[0][u] == u for u in PTS) and all(g[1][k] == k and g[2][k] == 1 for k in range(2, 8)))]
                def lbl(g):
                    return "grille:" + ",".join("%s->%s" % (NAME[u], NAME[g[0][u]]) for u in PPOS if g[0][u] != u) + \
                           " etiq:" + ",".join("%d->%s%d" % (k, "+" if g[2][k] > 0 else "-", g[1][k]) for k in range(2, 8)
                                               if g[1][k] != k or g[2][k] != 1)
                gs = " ; stabilisateur %d : %s" % (nfix, " | ".join(lbl(g) for g in nontriv[:3]) + (" ..." if len(nontriv) > 3 else ""))
            out.append("     coins %s  (orbite de dispositions %d, phi par orbite %d)%s%s" % (corners, osize, nphi, sh, gs))
    summary.append((tname, len(reps), len(types), len(shapes), sum(1 for s in shapes.values() if s[0][5]["refl"]),
                    sum(len(v) for v in shapes.values() if all(v[0][5]["lines"]))))

if __name__ == "__main__":
    out, summary = [], []
    for tname, abcd in TYPES.items():
        run(tname, abcd, out, summary)
    print("RESUME : type | orbites de dispositions | types locaux (disposition, phi) | formes de phi | reflexion | types a droites R2")
    for row in summary:
        print("  %-4s | %4d | %5d | %3d | %d | %d" % row)
    print("\n".join(out))
