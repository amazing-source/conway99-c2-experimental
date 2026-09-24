"""I-05: how do Q_out (even functions) and S_out (odd functions) of the controls act on 'root harmonics'?

Even functions on D_m roots (= functions on the N outer orbits):
  const (1), diagonal traceless quadratics y_f(U)=f_i+f_j, sum f=0  (m-1)  [known: eigenvalue k-2, -2],
  off-diagonal quadratics q_ij(U) = (-1)^e if pair(U)={i,j} else 0     (C(m,2))  <- test
  pair functions h(U) = g({i,j}) orthogonal to vertex sums              (C(m,2)-m)
Odd functions: phi_ij(U) for ordered pairs; linear part (m) is ker S_out.
We compute the matrix of Q_out restricted/projected on these subspaces and report invariance defects and Rayleigh spectra.
"""
import json, os, sys, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
from involution_frame import Frame, paley9, table_from_graph  # noqa


def load(m):
    if m == 11:
        T = json.load(open(os.path.join(HERE, "..", "data", "bvls_table_m11.json")))["T"]
        return Frame(11), T
    A, pts = paley9()
    neg = {p: pts.index(((-p[0]) % 3, (-p[1]) % 3)) for p in pts}
    fixed = [i for i in range(9) if neg[pts[i]] == i]
    fr, T, blocks, lab = table_from_graph(A, fixed[0], 2)
    return fr, T


def orth(B):
    q, r = np.linalg.qr(B)
    keep = np.abs(np.diag(r)) > 1e-9
    return q[:, keep]


def analyse(m):
    fr, T = load(m)
    Q = fr.Q_out(T).astype(float); S = fr.S_out(T).astype(float)
    N = fr.N; outer = fr.outer; pairs = list(itertools.combinations(range(1, m + 1), 2))
    # even subspaces
    const = np.ones((N, 1))
    diag = np.array([[1.0 if l in (i, j) else 0.0 for l in range(1, m + 1)] for (i, j, e) in outer])
    diag = diag - diag.mean(axis=0)            # centred block incidences span the (m-1)-dim space + 0
    qoff = np.array([[((-1.0) ** e if (i, j) == p else 0.0) for p in pairs] for (i, j, e) in outer])
    pairf = np.array([[1.0 if (i, j) == p else 0.0 for p in pairs] for (i, j, e) in outer])
    Bc = orth(const); Bd = orth(diag); Bq = orth(qoff)
    Bp = orth(pairf - Bc @ (Bc.T @ pairf) - Bd @ (Bd.T @ pairf))
    print("=== m=%d  dims: const %d, diag %d, offdiag-quad %d, pair-rest %d  (total %d of %d)" %
          (m, Bc.shape[1], Bd.shape[1], Bq.shape[1], Bp.shape[1], Bc.shape[1] + Bd.shape[1] + Bq.shape[1] + Bp.shape[1], N))
    for name, Bx in (("const", Bc), ("diag", Bd), ("offquad", Bq), ("pairrest", Bp)):
        if Bx.shape[1] == 0: continue
        QB = Q @ Bx
        inside = Bx @ (Bx.T @ QB)
        defect = np.linalg.norm(QB - inside) / max(np.linalg.norm(QB), 1e-12)
        ev = np.linalg.eigvalsh(Bx.T @ Q @ Bx)
        u, c = np.unique(np.round(ev, 4), return_counts=True)
        print("  Q_out on %-8s invariance defect %.3e ; compressed spectrum %s" % (name, defect, dict(zip(u, c))))
    # odd: phi_ij, linear part
    ordp = [(i, j) for i in range(1, m + 1) for j in range(1, m + 1) if i != j]
    phi = np.zeros((N, len(ordp)))
    for t, (i, j, e) in enumerate(outer):
        a, b = 1.0, (-1.0) ** e          # rep root = e_i + (-1)^e e_j
        phi[t, ordp.index((i, j))] = a; phi[t, ordp.index((j, i))] = b
    lin = orth(fr.C.astype(float))
    rest = orth(phi - lin @ (lin.T @ phi))
    print("  odd: linear %d, rest %d" % (lin.shape[1], rest.shape[1]))
    for name, Bx in (("linear", lin), ("oddrest", rest)):
        SB = S @ Bx; defect = np.linalg.norm(SB - Bx @ (Bx.T @ SB)) / max(np.linalg.norm(SB), 1e-12)
        ev = np.linalg.eigvalsh(Bx.T @ S @ Bx); u, c = np.unique(np.round(ev, 4), return_counts=True)
        print("  S_out on %-8s invariance defect %.3e ; compressed spectrum %s" % (name, defect, dict(zip(u, c))))
    # finer: decompose the odd rest under S_m-type splitting: antisymmetric X (X_ij = -X_ji) vs symmetric X, both with zero row sums
    # f_X(alpha = a e_i + b e_j) = a X_ij + b X_ji
    def fX(X):
        v = np.zeros(N)
        for t, (i, j, e) in enumerate(outer):
            a, b = 1.0, (-1.0) ** e
            v[t] = a * X[i - 1, j - 1] + b * X[j - 1, i - 1]
        return v
    sym, anti = [], []
    for (i, j) in pairs:
        X = np.zeros((m, m)); X[i - 1, j - 1] = X[j - 1, i - 1] = 1; sym.append(fX(X))
        X = np.zeros((m, m)); X[i - 1, j - 1] = 1; X[j - 1, i - 1] = -1; anti.append(fX(X))
    for name, M in (("symX", np.array(sym).T), ("antiX", np.array(anti).T)):
        Bx = orth(M - lin @ (lin.T @ M))
        SB = S @ Bx; defect = np.linalg.norm(SB - Bx @ (Bx.T @ SB)) / max(np.linalg.norm(SB), 1e-12)
        ev = np.linalg.eigvalsh(Bx.T @ S @ Bx); u, c = np.unique(np.round(ev, 4), return_counts=True)
        print("  S_out on %-8s (dim %d) invariance defect %.3e ; compressed spectrum %s" % (name, Bx.shape[1], defect, dict(zip(u, c))))


if __name__ == "__main__":
    for m in (2, 11):
        analyse(m)
