"""Test spectral « Gram tordu » pour l'etoile libre (note 22, cocycle a defauts).
X = [N_x | Phi] (60 x 24, incidences des racines lointaines), Q = permutation z -> -z (involution orthogonale sans point fixe).
Connu pour chaque type (mu, tau) :
  X^T X   = [[9I + J - P_s, C], [C^T, 9I + J - P_mu]]            ((i), (ii) et la carte)
  X^T Q X = [[J + 9P_s - I, P_s C], [C^T P_s, T]]                 ((iii), la carte, Q N = N P_s)
avec C = cible de (ii), T = cible de (iii). Comme Q = Pi_+ - Pi_-, les matrices (X^T X +/- X^T Q X)/2 = X^T Pi_+/- X sont des
matrices de Gram : elles doivent etre semi-definies positives. Un type qui viole cela est impossible (certificat : vecteur propre)."""
import sys, os, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types

def perm(f):
    n = len(f); P = np.zeros((n, n))
    for i in range(n): P[i, f[i]] = 1
    return P

def twisted(mu, tau, n2=12):
    Cx, Ct = targets(mu, tau, n2)
    I = np.eye(n2); J = np.ones((n2, n2)); Ps = perm([b ^ 1 for b in range(n2)]); Pm = perm(mu)
    M = np.block([[9 * I + J - Ps, Cx], [Cx.T, 9 * I + J - Pm]])
    Ms = np.block([[J + 9 * Ps - I, Ps @ Cx], [Cx.T @ Ps, Ct]])
    return M, Ms

if __name__ == "__main__":
    from make_freestar_cubes import PARTS
    worst = []; nbad = 0; ntot = 0
    for part in PARTS:
        mu, reps, st = types(part)
        bad_here = 0
        for i, tau in enumerate(reps):
            M, Ms = twisted(mu, tau)
            assert np.allclose(M, M.T) and np.allclose(Ms, Ms.T)
            lp = np.linalg.eigvalsh((M + Ms) / 2).min(); lm = np.linalg.eigvalsh((M - Ms) / 2).min()
            ntot += 1
            if min(lp, lm) < -1e-9:
                nbad += 1; bad_here += 1
            worst.append((min(lp, lm), "".join(map(str, part)), i))
        print("A%s : %d types, %d violent la positivite" % ("".join(map(str, part)), len(reps), bad_here), flush=True)
    worst.sort()
    print("total : %d types, %d impossibles par le Gram tordu ; 5 plus petites valeurs propres : %s" % (ntot, nbad, worst[:5]))
