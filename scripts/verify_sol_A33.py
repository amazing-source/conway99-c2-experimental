"""INDEPENDENT re-check (C2, written from the statement of Sol's proof, without its verifier) of the A33 torsion certificates
(external_inputs/sol, certificats_A33.json, sha256 cebf1108...).  Checks, in exact integer arithmetic:
 1. the group of label permutations commuting with sigma and tau has order 72; the 400 points of the projective torsion space
    (a,b,-a-b,a,b,-a-b ; c,d,-c-d,c,d,-c-d) over F7 are partitioned by the orbits of the 17 given representatives;
 2. for each of the 15 certificates (representative, multiplier, integer lift psi): the bound B = sum lambda + <gamma,K2> +
    <delta,K3> + sum_centres alpha_b + 18 alpha_* + sum beta_Z exceeds s*E, E = 3|psi|^2/2; and for EVERY far pair Z = {z, sigma z}
    and EVERY ordered choice (e, f) of distinct shadows (edges of K12 - sigma) that respects the zeros of K2, the individual
    capacities of K3 and the congruence psi(e) - psi(f) + 2(psi(z) - psi(sigma z)) = 0 mod 7:
        s q^2 >= lambda_e + lambda_f + gamma.contrib_K2 + delta.contrib_K3 + alpha(centre of e,f or *) + beta_Z;
 3. the excluded class 9 has an empty admissible domain for some Z (no certificate needed);
 4. every point of the remaining class has all 12 coordinates non-zero (=> r0 <= 1).
Usage: python verify_sol_A33.py"""
import json, itertools
F = "external_inputs/sol/files/outputs__coupures_et_torsion__certificats_A33.json"
D = json.load(open(F))
L = list(range(12)); sig = [i ^ 1 for i in L]
tau = list(L)
for a, b in [(0, 5), (1, 2), (3, 4), (6, 11), (7, 8), (9, 10)]: tau[a], tau[b] = b, a
p = 7

# 1. group: permutations commuting with sigma and tau (propagate the images of 0 and 6 along the alternating cycles)
def extend(img0, img6):
    pi = [None] * 12
    for start, img in ((0, img0), (6, img6)):
        stack = [(start, img)]
        while stack:
            x, y = stack.pop()
            if pi[x] is not None:
                if pi[x] != y: return None
                continue
            pi[x] = y; stack += [(sig[x], sig[y]), (tau[x], tau[y])]
    return tuple(pi) if sorted(pi) == L else None
G = {g for i0 in L for i6 in L for g in [extend(i0, i6)] if g is not None}
G = [g for g in G if all(g[sig[x]] == sig[g[x]] and g[tau[x]] == tau[g[x]] for x in L)]
assert len(G) == 72, len(G)
def tors(a, b, c, d): return (a, b, (-a - b) % p, a, b, (-a - b) % p, c, d, (-c - d) % p, c, d, (-c - d) % p)
def proj(v):
    t = pow(next(x for x in v if x % p), p - 2, p); return tuple(t * x % p for x in v)
pts = {proj(tors(a, b, c, d)) for a, b, c, d in itertools.product(range(p), repeat=4) if (a, b, c, d) != (0, 0, 0, 0)}
assert len(pts) == 400
# the torsion vectors must lie in ker(I + P_sigma + P_tau) mod 7
for v in pts: assert all((v[x] + v[sig[x]] + v[tau[x]]) % p == 0 for x in L)
act = lambda v, g: proj(tuple(v[g[x]] for x in L))
seen = set(); sizes = []
for r in D["phi_reps"]:
    orb = {act(tuple(x % p for x in r), g) for g in G}
    assert not (orb & seen), "orbits overlap"
    seen |= orb; sizes.append(len(orb))
assert seen == pts, "orbits do not cover the 400 points"
assert sizes == D["orbit_sizes"], (sizes, D["orbit_sizes"])
print("1. group order 72, 17 orbits partition the 400 points, sizes", sizes)

# data
E = [e for e in itertools.combinations(L, 2) if sig[e[0]] != e[1]]            # 60 shadows (edges of K12 - sigma)
assert len(E) == 60
fl = lambda e: tuple(sorted(sig[x] for x in e))
Z = [z for z in E if z < fl(z)]                                               # 30 far pairs z / sigma z
assert len(Z) == 30
K2 = [[2 - (a == b) - 2 * (b == sig[a]) - (b == tau[sig[a]]) for b in L] for a in L]
K3 = [[2 - (d == sig[b]) - (d == tau[b]) - (d == tau[sig[b]]) - (d == sig[tau[b]]) for d in L] for b in L]

def admissible(psi, z):
    sz = fl(z); dz = sum(psi[x] for x in z) - sum(psi[x] for x in sz)
    for e in E:
        if any(K2[a][b] == 0 for a in z for b in e): continue
        for f in E:
            if f == e or any(K2[a][b] == 0 for a in sz for b in f): continue
            num = sum(psi[x] for x in e) - sum(psi[x] for x in f) + 2 * dz
            if num % p: continue
            c3 = {}
            for b in e:
                for d in f: c3[(b, d)] = c3.get((b, d), 0) + 1
            for b in f:
                for d in e: c3[(b, d)] = c3.get((b, d), 0) + 1
            if any(v > K3[b][d] for (b, d), v in c3.items()): continue
            yield e, f, num // p, c3

# 2. certificates
ok_all = True
for case in D["cases"]:
    k = case["index"]; m = case.get("multiplier", 1)
    ph = [(m * x) % p for x in D["phi_reps"][k]]
    lift = lambda x: x if x <= 3 else x - p
    psi = []
    for j in (0, 6):
        a, b = lift(ph[j]), lift(ph[j + 1]); psi += [a, b, -a - b, a, b, -a - b]
    assert all((psi[x] - ph[x]) % p == 0 for x in L)
    n2 = sum(x * x for x in psi); assert n2 % 2 == 0
    energy = 3 * n2 // 2; s = case["scale"]; cert = case["certificate"]
    lam = cert["price"][:60]; gam = cert["price"][60:204]; dlt = cert["price"][204:348]
    al = cert["dual_left"]; be = cert["dual_right"]
    assert len(al) == 30 and len(set(al[12:])) == 1 and len(be) == 30
    alpha_c, alpha_star = al[:12], al[12]
    B = sum(lam) + sum(gam[12 * a + b] * K2[a][b] + dlt[12 * a + b] * K3[a][b] for a in L for b in L) + sum(alpha_c) + 18 * alpha_star + sum(be)
    good = B > s * energy and B == cert["bound"]
    nchk = 0
    for iz, z in enumerate(Z):
        for e, f, q, c3 in admissible(psi, z):
            nchk += 1
            c2 = sum(gam[12 * a + b] for a in z for b in e) + sum(gam[12 * a + b] for a in fl(z) for b in f)
            c3v = sum(dlt[12 * b + d] * v for (b, d), v in c3.items())
            inter = set(e) & set(f)
            ac = alpha_c[inter.pop()] if len(inter) == 1 else alpha_star
            rhs = lam[E.index(e)] + lam[E.index(f)] + c2 + c3v + ac + be[iz]
            if s * q * q < rhs:
                good = False; print("  VIOLATION class %d Z=%s e=%s f=%s: %d < %d" % (k, z, e, f, s * q * q, rhs)); break
        if not good: break
    ok_all &= good
    print("2. class %2d (x%d): E=%d s=%d B=%d (B>sE: %s), inequality checked on %d admissible choices: %s" % (k, m, energy, s, B, B > s * energy, nchk, "OK" if good else "FAIL"))

# 3. class 9: some Z has no admissible choice
k9 = D["human_exclusion"]; ph = [x % p for x in D["phi_reps"][k9]]
lift = lambda x: x if x <= 3 else x - p
psi9 = []
for j in (0, 6):
    a, b = lift(ph[j]), lift(ph[j + 1]); psi9 += [a, b, -a - b, a, b, -a - b]
empty = [z for z in Z if not any(True for _ in admissible(psi9, z))]
print("3. class %d: far pairs with an empty admissible domain: %s" % (k9, empty))
ok_all &= bool(empty)

# 4. remaining class: all coordinates non-zero
kr = D["remaining_class"]; orb = {act(tuple(x % p for x in D["phi_reps"][kr]), g) for g in G}
nz = all(all(x % p for x in v) for v in orb)
print("4. remaining class %d: %d points, all coordinates non-zero: %s" % (kr, len(orb), nz))
covered = set(c["index"] for c in D["cases"]) | {k9}
print("classes excluded:", sorted(covered), "| not excluded:", sorted(set(range(17)) - covered))
ok_all &= nz and sorted(set(range(17)) - covered) == [kr]
print("ALL CHECKS PASSED" if ok_all else "SOME CHECK FAILED")
