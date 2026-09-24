"""Version EXACTE du test spectral du graphe lointain (note 23 §7).
Pour chaque facteur irreductible p (multiplicite k) du polynome caracteristique de B^T B sur 1^perp :
  A_F restreint a V_p a pour polynome caracteristique prod_q q^{n_q}, q parcourant les facteurs irreductibles de p(12 - t - t^2),
  avec sum_q n_q deg q = k deg p  et  n_q >= 0 entiers.
Contraintes globales : tr A_F = 0, tr A_F^3 = 6 (32 - T) (et tr A_F^2, tr A_F^4 automatiques).
On cherche s'il existe des n_q entiers ; sinon le type (mu, tau) est IMPOSSIBLE (aucun graphe lointain).
Usage : python far_spectrum_exact.py <partitions separees par des virgules> [indices]
"""
import sys, os, itertools, time
import numpy as np
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import types
from far_spectrum_test import BBt

t = sp.Symbol("t"); x = sp.Symbol("x")

def blocks(mu, tau):
    M = sp.Matrix(BBt(mu, tau).tolist())
    cp = M.charpoly(x).as_expr()
    # B^T B = BB^T + 24 zeros ; retirer la valeur 60 (vecteur 1)
    cp = sp.expand(cp * x ** 24)
    cp = sp.quo(cp, x - 60)
    fl = sp.factor_list(cp)[1]
    out = []
    for p, k in fl:
        P = sp.Poly(p, x)
        q_list = sp.factor_list(sp.expand(p.subs(x, 12 - t - t ** 2)))[1]
        qs = []
        for q, e in q_list:
            Q = sp.Poly(q, t)
            roots_deg = Q.degree()
            # sommes de puissances des racines de q (Newton) : p1, p3
            c = Q.all_coeffs(); c = [sp.Rational(ci, c[0]) for ci in c]
            n = roots_deg
            e_ = [1] + [(-1) ** i * c[i] for i in range(1, n + 1)]
            pw = [n]
            for kk in range(1, 4):
                s_ = 0
                for i in range(1, kk):
                    if i <= n: s_ += (-1) ** (i - 1) * e_[i] * pw[kk - i]
                if kk <= n: s_ += (-1) ** (kk - 1) * kk * e_[kk]
                pw.append(sp.nsimplify(s_))
            qs.append(dict(q=Q, deg=roots_deg, e=e, p1=pw[1], p3=pw[3]))
        out.append(dict(p=P, k=k, qs=qs))
    return out

def feasible(bl, T):
    """cherche des n_q entiers >= 0 : sum_q n_q deg q = k deg p (par facteur p), sum n_q p1(q) = -8, sum n_q p3(q) = 6(32-T) - 512."""
    target1 = -8; target3 = 6 * (32 - T) - 512
    # enumeration par facteur : liste des (contribution p1, p3) possibles
    options = []
    for b in bl:
        dp = b["p"].degree(); k = b["k"]; qs = b["qs"]
        need = k * dp
        opts = set()
        def rec(i, rem, s1, s3):
            if i == len(qs):
                if rem == 0: opts.add((s1, s3))
                return
            q = qs[i]
            for n in range(0, rem // q["deg"] + 1):
                rec(i + 1, rem - n * q["deg"], s1 + n * q["p1"], s3 + n * q["p3"])
        rec(0, need, sp.Integer(0), sp.Integer(0))
        options.append(sorted(opts))
    # combinaison (sac a dos sur les paires (s1, s3))
    reach = {(sp.Integer(0), sp.Integer(0))}
    for opts in options:
        reach = {(a + c, b + d) for (a, b) in reach for (c, d) in opts}
        if len(reach) > 200000: return None, len(reach)
    ok = (sp.Integer(target1), sp.Integer(target3)) in reach
    return ok, len(reach)

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    parts = sys.argv[1].split(",")
    sel = [int(v) for v in sys.argv[2].split(",")] if len(sys.argv) > 2 else None
    for ps in parts:
        part = tuple(int(c) for c in ps)
        mu, reps, st = types(part)
        idx = sel if sel is not None else range(len(reps))
        nbad = 0
        for ti in idx:
            tau = reps[ti]
            T = sum(1 for b in range(12) if tau[b] == (b ^ 1))
            t0 = time.time()
            bl = blocks(mu, tau)
            ok, nr = feasible(bl, T)
            desc = "; ".join("%s^%d->[%s]" % (b["p"].as_expr(), b["k"], ",".join(str(q["q"].as_expr()) for q in b["qs"])) for b in bl)
            if ok is not True: nbad += 1
            print("A%s tau#%d T=%d : %s (%.1f s) | %s" % (ps, ti, T, {True: "possible", False: "IMPOSSIBLE", None: "trop de cas"}[ok], time.time() - t0, desc), flush=True)
        print("A%s : %d types examines, %d non possibles" % (ps, len(list(idx)), nbad), flush=True)
