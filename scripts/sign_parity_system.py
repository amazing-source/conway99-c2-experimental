"""Systeme lineaire de parite des signes L(Q) (notes/19 §10) : a Q fixe (solution de l'etage Q), les parites des contraintes (I) et des
equations (P) « cross » sont LINEAIRES en les signes Z[U,V] (Z = b sur les entrees Q = 1).  Coherence de L(Q) = condition necessaire
pour que Q se releve en solution du modele complet.
Controle sur BvLS (m = 11) : Q planted (coherent, forcement) ; puis Q' = Q avec U_12^+ et U_12^- echangees (encore solution de
l'etage Q) : L(Q') coherent ou non ? et combien de conditions independantes echouent (rang) ?
"""
import sys, itertools
import numpy as np
sys.path.insert(0, "scripts")
exec(open("scripts/minus_parity_check.py", encoding="utf-8").read().split("# echange des deux orbites")[0])

def gf2_rank(M):
    """rang sur F2 d'une matrice 0/1 (numpy uint8), elimination sur lignes empaquetees en bits."""
    M = np.packbits(M.astype(np.uint8), axis=1)
    rows, ncols = M.shape[0], M.shape[1] * 8
    r = 0
    for c in range(ncols):
        byte, bit = divmod(c, 8); mask = np.uint8(0x80 >> bit)
        piv = None
        col = (M[r:, byte] & mask) != 0
        nz = np.flatnonzero(col)
        if nz.size == 0: continue
        piv = r + nz[0]
        if piv != r: M[[r, piv]] = M[[piv, r]]
        hit = np.flatnonzero((M[:, byte] & mask) != 0)
        hit = hit[hit != r]
        M[hit] ^= M[r]
        r += 1
        if r == rows: break
    return r

def L_system(Q, m):
    outer_ = [(i, j, e) for i in range(1, m + 1) for j in range(i + 1, m + 1) for e in (0, 1)]
    N_ = len(outer_)
    rep_ = [frozenset([(i, 0), (j, e)]) for (i, j, e) in outer_]
    trep_ = [frozenset([(i, 1), (j, 1 - e)]) for (i, j, e) in outer_]
    var = {}
    for U in range(N_):
        for V in range(U + 1, N_):
            if Q[U, V] == 1:
                var[U, V] = var[V, U] = len(var) // 2 if False else None
    keys = sorted({(min(U, V), max(U, V)) for (U, V) in var})
    vid = {k: t for t, k in enumerate(keys)}
    def z(U, V): return vid[(min(U, V), max(U, V))]
    rows = []; rhs = []
    inner_ = [(i, s) for i in range(1, m + 1) for s in (0, 1)]
    for U in range(N_):
        for c in inner_:
            row = np.zeros(len(keys), dtype=np.uint8); const = 0
            target = 1 if (c in rep_[U] or (c[0], 1 - c[1]) in rep_[U]) else 2
            for V in range(N_):
                if V == U: continue
                if Q[U, V] == 2:
                    const += (c in rep_[V]) + (c in trep_[V])
                elif Q[U, V] == 1:
                    # racine voisine : rep V si Z = 0, trep V si Z = 1 ; contient c ?
                    if (c in rep_[V]) != (c in trep_[V]):
                        const += (c in rep_[V]); row[z(U, V)] ^= 1
                    else:
                        const += (c in rep_[V])
            rows.append(row); rhs.append((target - const) % 2)
    for U in range(N_):
        for V in range(U + 1, N_):
            row = np.zeros(len(keys), dtype=np.uint8); const = 0
            for W in range(N_):
                if W in (U, V): continue
                qu, qv = Q[U, W], Q[V, W]
                if qu == 0 or qv == 0: continue
                if qu == 2 and qv == 2: const += 2
                elif qu == 2: const += 1          # a_UW = b_UW = 1 : a_UW b_VW + b_UW a_VW = b_VW + a_VW = 1
                elif qv == 2: const += 1
                else:
                    row[z(U, W)] ^= 1; row[z(V, W)] ^= 1   # a b' + b a' = Z_UW xor Z_VW
            # terme b_UV
            if Q[U, V] == 2: const += 1
            elif Q[U, V] == 1: row[z(U, V)] ^= 1
            target = 2 - len(rep_[U] & trep_[V])
            rows.append(row); rhs.append((target - const) % 2)
    A_ = np.array(rows, dtype=np.uint8); b_ = np.array(rhs, dtype=np.uint8)
    return A_, b_

for tag, QQ in (("BvLS planted", Q),):
    A_, b_ = L_system(QQ, m)
    rA = gf2_rank(A_); rAb = gf2_rank(np.hstack([A_, b_[:, None]]))
    print("%s : %d equations, %d signes ; rang(A) = %d, rang([A|b]) = %d -> %s" % (tag, A_.shape[0], A_.shape[1], rA, rAb, "coherent" if rA == rAb else "INCOHERENT"), flush=True)
r = outer.index((1, 2, 0)); r2 = outer.index((1, 2, 1))
perm = list(range(N)); perm[r], perm[r2] = r2, r
Q2 = Q[np.ix_(perm, perm)]
A_, b_ = L_system(Q2, m)
rA = gf2_rank(A_); rAb = gf2_rank(np.hstack([A_, b_[:, None]]))
print("Q echangee (12+ <-> 12-) : rang(A) = %d, rang([A|b]) = %d -> %s" % (rA, rAb, "coherent" if rA == rAb else "INCOHERENT"), flush=True)
