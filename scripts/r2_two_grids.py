"""Recollement de deux grilles (notes/15, etape 3).  Enumeration exacte, sans SAT, sans etiquettes.

Deux grilles L, L' hors de x passant par w = e1 et partageant la droite l1 = {w, al, be} ; images tL, tL'.
Faits (G1 + R1) : L n L' = l1 ; aucune arete entre L \\ l1 et L' \\ l1 (chaque sommet de L' \\ l1 a son unique voisin
de L dans l1) ; aretes L-tL = pi = t o phi ; L'-tL' = pi' = t o phi' ; L'-tL = couplage parfait psi (on suppose L' n tL vide) ;
L-tL' = t(psi).  Contraintes forcees : psi(u) = t.phi(u) pour u dans l1 ; psi^-1(t.al) = phi'(al), psi^-1(t.be) = phi'(be) ;
phi(al) = be <=> phi'(al) = be.
Le sous-graphe induit sur les 30 sommets est alors entierement determine par (phi, phi', psi) : on teste lambda = 1, mu = 2
(nombre de voisins communs internes <= 1 pour une arete, <= 2 sinon) pour toutes les paires.
"""
import sys, itertools, time
import numpy as np
from collections import Counter, defaultdict

POS = [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)]    # w al be ga de z_ac z_ad z_bc z_bd
NM = ["w", "al", "be", "ga", "de", "z_ac", "z_ad", "z_bc", "z_bd"]
NMp = ["w", "al", "be", "ep", "ze", "z_ae", "z_af", "z_be", "z_bf"]
# indices : L = 0..8 ; L' = 0,1,2 puis 9..14 (positions 3..8 de L') ; tL = 15..23 ; tL' = 15,16,17 puis 24..29
def idxL(p):  return p
def idxLp(p): return p if p < 3 else 6 + p          # 3..8 -> 9..14
def t(i):     return i + 15
N = 30

def grid_adj(p, q):
    a, b = POS[p], POS[q]
    return p != q and (a[0] == b[0] or a[1] == b[1])

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

PHIS = [{**d, 0: 0} for d in involutions(list(range(1, 9)))]   # sur les positions 0..8, w fixe
REFL = {p: POS.index(((-POS[p][0]) % 3, (-POS[p][1]) % 3)) for p in range(9)}

def base_matrix():
    A = np.zeros((N, N), dtype=np.int16)
    for p in range(9):
        for q in range(9):
            if grid_adj(p, q):
                for f in (idxL, idxLp):
                    A[f(p), f(q)] = 1
                    A[t(f(p)), t(f(q))] = 1
    A[0, t(0)] = A[t(0), 0] = 1                        # w ~ tw
    return A

BASE = base_matrix()

def check(phi, phip, out_counts):
    """Enumere psi ; renvoie le nombre de psi valides."""
    A0 = BASE.copy()
    for p in range(1, 9):                              # pi et pi'
        A0[idxL(p), t(idxL(phi[p]))] = A0[t(idxL(phi[p])), idxL(p)] = 1
        A0[idxLp(p), t(idxLp(phip[p]))] = A0[t(idxLp(phip[p])), idxLp(p)] = 1
    # psi : L' -> tL (sommets de L' : positions 0..8 de L') ; forcees
    forced = {0: t(0), 1: t(idxL(phi[1])), 2: t(idxL(phi[2]))}
    for p, target in ((phip[1], t(1)), (phip[2], t(2))):
        if p in forced and forced[p] != target:
            return 0
        forced[p] = target
    if len(set(forced.values())) != len(forced):
        return 0
    free_src = [p for p in range(9) if p not in forced]
    used = set(forced.values())
    free_dst = [t(q) for q in range(9) if t(q) not in used]
    if len(free_src) != len(free_dst):
        return 0
    good = 0
    perms = list(itertools.permutations(free_dst))
    B = np.repeat(A0[None, :, :], len(perms), axis=0)
    for k, perm in enumerate(perms):
        ps = dict(forced); ps.update(zip(free_src, perm))
        for p, tv in ps.items():
            u = idxLp(p)
            B[k, u, tv] = B[k, tv, u] = 1                 # L' - tL
            v = tv - 15                                     # t(psi) : tL' - L
            B[k, t(u), v] = B[k, v, t(u)] = 1
    Bf = B.astype(np.float32); B2 = np.matmul(Bf, Bf)
    lim = np.where(B == 1, 1, 2)
    eye = np.eye(N, dtype=bool)
    ok = ((B2 <= lim) | eye[None, :, :]).all(axis=(1, 2))
    # sommets partages l1 : les memes indices, les aretes doivent rester simples (0/1)
    ok &= (B.max(axis=(1, 2)) <= 1)
    return int(ok.sum())

if __name__ == "__main__":
    try:
        import ctypes; k = ctypes.windll.kernel32
        k.GetCurrentProcess.restype = ctypes.c_void_p; k.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        k.SetPriorityClass(k.GetCurrentProcess(), 0x40)
    except Exception:
        pass
    t0 = time.time()
    res = {}
    for i, phi in enumerate(PHIS):
        for j, phip in enumerate(PHIS):
            if (phi[1] == 2) != (phip[1] == 2):          # J2 : statut de la droite partagee
                continue
            res[i, j] = check(phi, phip, None)
    comp = {k: v for k, v in res.items() if v > 0}
    print("paires (phi, phi') testees : %d ; compatibles : %d ; temps %.0f s" % (len(res), len(comp), time.time() - t0))
    phi_ok = Counter(i for i, j in comp)
    def shape(phi, nm):
        return " ".join("(%s %s)" % (nm[p], nm[phi[p]]) for p in range(1, 9) if p < phi[p])
    lines = lambda phi: (phi[1] == 2) + (phi[3] == 4)
    print("phi de L ayant au moins un partenaire (phi', psi) : %d / %d" % (len(phi_ok), len(PHIS)))
    dead = [i for i in range(len(PHIS)) if i not in phi_ok]
    print("phi de L sans aucun partenaire (%d) :" % len(dead))
    for i in dead:
        print("   ", shape(PHIS[i], NM), "| reflexion" if PHIS[i] == REFL else "", "| droites R2 %d/2" % lines(PHIS[i]))
    r = PHIS.index(REFL)
    print("reflexion : %d partenaires phi' compatibles" % sum(1 for (i, j) in comp if i == r))
    by_status = defaultdict(lambda: [0, 0])
    for (i, j), v in res.items():
        k = ("l1 fermante" if PHIS[i][1] == 2 else "l1 non fermante")
        by_status[k][0] += 1; by_status[k][1] += (v > 0)
    for k, (n, c) in by_status.items():
        print("  %s : %d paires, %d compatibles" % (k, n, c))
