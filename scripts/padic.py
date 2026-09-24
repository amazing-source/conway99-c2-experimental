"""Small exact helpers: p-adic elementary divisors (Smith form over Z_(p)), ranks mod p, rational ranks."""
import numpy as np


def vp(x, p):
    x = int(x)
    if x == 0: return 10 ** 9
    v = 0
    while x % p == 0: x //= p; v += 1
    return v


def padic_elementary_divisors(M, p, K=12):
    """Exponents of p in the Smith normal form of the integer matrix M over Z_(p), computed mod p^K.
    Returns a list (one per diagonal position) of exponents; 'inf' (None) for zero (up to precision K)."""
    mod = p ** K
    A = [[int(x) % mod for x in row] for row in np.asarray(M, dtype=object)]
    n, m = len(A), len(A[0])
    exps = []
    r = 0
    cols = list(range(m))
    while r < min(n, m):
        # find pivot of minimal valuation in the remaining block
        best = None
        for i in range(r, n):
            for j in range(r, m):
                if A[i][j] % mod:
                    v = vp(A[i][j], p)
                    if best is None or v < best[0]:
                        best = (v, i, j)
                        if v == 0: break
            if best is not None and best[0] == 0: break
        if best is None: break
        v, pi, pj = best
        if v >= K: break
        A[r], A[pi] = A[pi], A[r]
        for row in A: row[r], row[pj] = row[pj], row[r]
        piv = A[r][r]
        u = piv // p ** v                  # unit part (mod p^(K-v))
        uinv = pow(u, -1, p ** (K - v)) if K - v > 0 else 0
        for i in range(r + 1, n):
            if A[i][r] % mod:
                f = ((A[i][r] // p ** v) * uinv) % mod   # A[i][r] has valuation >= v
                Ar = A[r]; Ai = A[i]
                for j in range(r, m):
                    Ai[j] = (Ai[j] - f * Ar[j]) % mod
        for j in range(r + 1, m):
            if A[r][j] % mod:
                f = ((A[r][j] // p ** v) * uinv) % mod
                for i in range(r, n):
                    A[i][j] = (A[i][j] - f * A[i][r]) % mod
        exps.append(v)
        r += 1
    return exps


def rank_mod_p(M, p):
    M = (np.array(M, dtype=np.int64) % p).copy(); rows, cols = M.shape; rk = 0
    for c in range(cols):
        piv = next((i for i in range(rk, rows) if M[i, c]), None)
        if piv is None: continue
        M[[rk, piv]] = M[[piv, rk]]
        inv = pow(int(M[rk, c]), -1, p); M[rk] = (M[rk] * inv) % p
        for i in range(rows):
            if i != rk and M[i, c]: M[i] = (M[i] - M[i, c] * M[rk]) % p
        rk += 1
    return rk
