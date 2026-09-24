"""Controle independant du systeme chi (notes/18) : modele « etage Q » du depot (vendor/stage_q.py, encodage different)
avec la configuration Sigma imposee (Q = 2 entre les deux orbites de chaque paire soeur listee).
Le systeme chi etant une consequence de l'etage Q (+ S1, lui-meme consequence de l'etage Q), toute configuration chi-UNSAT doit etre
etage-Q-UNSAT.  Un SAT ici sur une configuration chi-UNSAT reveleraient une erreur de derivation.
Usage : python chi_crosscheck.py <secondes> config [config ...]
"""
import sys, os, time, multiprocessing as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor")); sys.path.insert(0, HERE)

def idle():
    try:
        import ctypes; k = ctypes.windll.kernel32
        k.GetCurrentProcess.restype = ctypes.c_void_p; k.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        k.SetPriorityClass(k.GetCurrentProcess(), 0x40)
    except Exception:
        pass

def worker(pairs, q):
    idle()
    import stage_q
    from pysat.solvers import Solver
    t0 = time.time()
    cnf, pool, outer, X, Y = stage_q.build_q(7)
    for (i, j) in pairs:
        U0, U1 = outer.index((i, j, 0)), outer.index((i, j, 1))
        cnf.append([Y[U0, U1]])
    tb = time.time() - t0
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as s:
        r = s.solve()
    q.put(("SAT" if r else "UNSAT", round(tb, 1), round(time.time() - t0 - tb, 1)))

if __name__ == "__main__":
    idle()
    from chi_system import CONFIGS
    T = float(sys.argv[1])
    for name in sys.argv[2:]:
        q = mp.Queue(); p = mp.Process(target=worker, args=(CONFIGS[name], q)); p.start(); p.join(T)
        if p.is_alive():
            p.terminate(); p.join(); print("%-16s etage Q : TIMEOUT %.0f s" % (name, T), flush=True)
        else:
            r, tb, ts = q.get(); print("%-16s etage Q : %s (construction %.1f s, resolution %.1f s)" % (name, r, tb, ts), flush=True)
