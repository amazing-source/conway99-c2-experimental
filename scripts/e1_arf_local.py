# E1 (c2_experimental). Real srgs with v odd, integer eigenvalues r, s, r - s odd (E_theta 2-integral),
# and an involution sigma fixing exactly one vertex x (Cayley graphs on odd abelian groups, sigma = inversion).
# Checks, for theta in {r, s}:
#   (a) f even, a(sigma) = k                       (free Z_2[C_2]-module, trace 0)
#   (b) Lambda_theta even (E_theta 1 = 0)
#   (c) the §23 criterion  det_odd == 1 + f/v (mod 4)  and the claim that it is the tautology det_odd == (-1)^(f/2) (mod 4)
#   (d) NEW: Arf(Lambda_theta (x) Z_2) computed globally (det mod 8) equals the local value q(w) = w.w/2 mod 2,
#       w = E_theta w0,  w0 = (E_xx/2) e_x + sum_{u in reps} E_ux e_u   (so that (1+sigma) w = E_theta e_x).
# det Lambda_theta odd part = u+ u- (invariant / anti-invariant eigen-sublattices, index 2^(f/2)).
import sys, itertools
from fractions import Fraction
import numpy as np

def int_kernel(M):
    M = [list(map(int, r)) for r in M]; m, n = len(M), len(M[0])
    U = [[int(i == j) for j in range(n)] for i in range(n)]
    col = 0
    for r in range(m):
        while True:
            nz = [c for c in range(col, n) if M[r][c] != 0]
            if len(nz) <= 1: break
            p = min(nz, key=lambda c: abs(M[r][c]))
            for c in nz:
                if c != p:
                    q = M[r][c] // M[r][p]
                    for i in range(m): M[i][c] -= q * M[i][p]
                    for i in range(n): U[i][c] -= q * U[i][p]
        nz = [c for c in range(col, n) if M[r][c] != 0]
        if nz:
            p = nz[0]
            for i in range(m): M[i][col], M[i][p] = M[i][p], M[i][col]
            for i in range(n): U[i][col], U[i][p] = U[i][p], U[i][col]
            col += 1
    return [[U[i][c] for i in range(n)] for c in range(col, n)]

def det_frac(G):
    G = [[Fraction(x) for x in r] for r in G]; n = len(G); d = Fraction(1)
    for i in range(n):
        p = next(k for k in range(i, n) if G[k][i] != 0)
        if p != i: G[i], G[p] = G[p], G[i]; d = -d
        d *= G[i][i]
        for k in range(i + 1, n):
            f = G[k][i] / G[i][i]
            if f: G[k] = [a - f * b for a, b in zip(G[k], G[i])]
    return d

def odd_part(z):
    z = int(z)
    while z % 2 == 0: z //= 2
    return z

def mod2adic(fr, m):  # a 2-adic integer Fraction reduced mod m (m a power of 2)
    assert fr.denominator % 2 == 1, fr
    return (fr.numerator * pow(fr.denominator, -1, m)) % m

def half_lattice_det(A, sig, x, theta, sign):
    n = len(A); orbs = []; seen = set()
    for u in range(n):
        if u in seen or u == x: continue
        seen |= {u, sig[u]}; orbs.append((u, sig[u]))
    basis = ([[1 if i == x else 0 for i in range(n)]] if sign > 0 else []) + \
            [[(1 if i == u else (sign if i == w else 0)) for i in range(n)] for (u, w) in orbs]
    B = np.array(basis, dtype=np.int64).T
    reps = ([x] if sign > 0 else []) + [u for (u, w) in orbs]
    Qm = (A @ B)[reps, :]
    d = Qm.shape[0]
    K = int_kernel((Qm - theta * np.eye(d, dtype=np.int64)).tolist())
    V = np.array(K, dtype=object).T
    Gf = np.diag([1 if (sign > 0 and i == 0) else 2 for i in range(d)]).astype(object)
    G = (V.T.dot(Gf)).dot(V)
    return len(K), det_frac(G.tolist()), orbs

def run(name, A, sig, x):
    n = len(A); k = int(A[0].sum())
    assert all(sig[sig[u]] == u for u in range(n)) and [u for u in range(n) if sig[u] == u] == [x]
    assert all(A[sig[u], sig[w]] == A[u, w] for u in range(n) for w in range(n) if A[u, w])
    ev = np.round(np.linalg.eigvalsh(A.astype(float))).astype(int)
    vals = sorted(set(ev.tolist()) - {k}, reverse=True)
    assert len(vals) == 2, vals
    r, s = vals
    if (r - s) % 2 == 0:
        print(f"{name}: r - s = {r - s} even, skipped"); return
    a = sum(1 for u in range(n) if A[u, sig[u]])
    out = []
    for theta, other in ((r, s), (s, r)):
        f = int(sum(ev == theta))
        c = Fraction(k - other, n)
        # E_theta = (A - other I - c J)/(theta - other)
        E = lambda i, j: (Fraction(int(A[i, j]) - (other if i == j else 0)) - c) / (theta - other)
        rp, Dp, orbs = half_lattice_det(A, sig, x, theta, +1)
        rm, Dm, _ = half_lattice_det(A, sig, x, theta, -1)
        assert rp + rm == f and rp == rm == f // 2
        dodd = odd_part(Dp.numerator) * odd_part(Dm.numerator)
        crit = mod2adic(1 + Fraction(f, n), 4)
        taut = 1 if (f // 2) % 2 == 0 else 3
        arf_glob = 0 if (dodd * (1 if (f // 2) % 2 == 0 else -1)) % 8 == 1 else (1 if (dodd * (1 if (f // 2) % 2 == 0 else -1)) % 8 == 5 else None)
        # local: w0 = (E_xx/2) e_x + sum_{reps} E_ux e_u ;  q(w) = w0^T E w0 / 2
        reps = [u for (u, w) in orbs]
        w0 = {x: E(x, x) / 2}
        for u in reps: w0[u] = E(u, x)
        supp = list(w0)
        Ew0 = [sum(E(i, j) * w0[j] for j in supp) for i in range(n)]
        # check (1 + sigma) E w0 == E e_x
        assert all(Ew0[i] + Ew0[sig[i]] == E(i, x) for i in range(n))
        qw = sum(w0[i] * Ew0[i] for i in supp) / 2
        arf_loc = mod2adic(qw, 2)
        out.append((theta, f, dodd % 8, crit, taut, arf_glob, arf_loc))
    print(f"{name}: v={n} k={k} r={r} s={s} a(sigma)={a} (k={k})")
    for (theta, f, d8, crit, taut, ag, al) in out:
        flag = "OK" if (d8 % 4 == crit == taut and ag == al) else "<<< MISMATCH"
        print(f"   theta={theta:>3} f={f:>4}  det_odd mod 8={d8}  crit 1+f/v mod4={crit}  (-1)^(f/2) mod4={taut}  Arf global={ag} local={al}  {flag}")
    sys.stdout.flush()

def net_graph(n, dirs):
    # Cayley graph on Z_n^2, n odd prime, connection set = nonzero multiples of the given directions
    V = list(itertools.product(range(n), repeat=2)); ix = {p: i for i, p in enumerate(V)}
    S = {((t * d0) % n, (t * d1) % n) for (d0, d1) in dirs for t in range(1, n)}
    A = np.zeros((n * n, n * n), dtype=np.int64)
    for p in V:
        for d in S: A[ix[p], ix[((p[0] + d[0]) % n, (p[1] + d[1]) % n)]] = 1
    sig = [ix[((-p[0]) % n, (-p[1]) % n)] for p in V]
    return A, sig, ix[(0, 0)]

def paley_sq(q, nonsq):
    # Paley graph on F_{q^2} = F_q[i]/(i^2 - nonsq), q odd prime
    V = list(itertools.product(range(q), repeat=2)); ix = {p: t for t, p in enumerate(V)}
    mul = lambda a, b: ((a[0] * b[0] + nonsq * a[1] * b[1]) % q, (a[0] * b[1] + a[1] * b[0]) % q)
    sq = {mul(z, z) for z in V if z != (0, 0)}
    A = np.zeros((q * q, q * q), dtype=np.int64)
    for p in V:
        for d in sq: A[ix[p], ix[((p[0] + d[0]) % q, (p[1] + d[1]) % q)]] = 1
    sig = [ix[((-p[0]) % q, (-p[1]) % q)] for p in V]
    return A, sig, ix[(0, 0)]

if __name__ == "__main__":
    for q, ns in ((3, 2), (5, 2), (7, 3), (11, 2), (13, 2)):
        A, sg, x = paley_sq(q, ns); run(f"Paley({q}^2)", A, sg, x)
    for n in (5, 7, 11, 13):
        dirs_all = [(1, 0), (0, 1), (1, 1), (1, n - 1), (1, 2), (2, 1)]
        for m in range(2, min(n, 6) + 1):
            A, sg, x = net_graph(n, dirs_all[:m]); run(f"Net L_{m}({n})", A, sg, x)
    sys.path.insert(0, "data")
    from control_bvls_copy import bvls
    A, V, ix, cols, neg = bvls(); A = A.astype(np.int64)
    run("BvLS", A, [ix[neg(v)] for v in V], ix[(0,) * 5])
