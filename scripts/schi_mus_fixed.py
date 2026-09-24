"""Pour une etoile : noyau minimal de contraintes SIGNEES qui refute un chi (non signe) FIXE (notes/19 §6).
On tire k solutions chi du systeme non signe ; pour chacune, MUS (par suppression) parmi les groupes signes de schi_mus.groups
(sbij, sdisj, sint, sbloc), les X etant imposes.  Affiche la composition des noyaux.
Usage : python schi_mus_fixed.py "<paires>" <k>
"""
import sys, time, collections
sys.path.insert(0, "scripts")
from pysat.solvers import Solver
import schi_system, schi_mus
from rs_experiments import idle

def mus_fixed(E, fix):
    G, defs, pool = schi_mus.groups(E)
    names = [n for n in G if n.startswith("s")]          # groupes signes seulement
    sel = {n: pool.id(("sel", n)) for n in names}
    # variables X de schi_mus.groups : memes cles ("chi", p, W)
    units = [[pool.id(("chi", k[0], k[1])) if v else -pool.id(("chi", k[0], k[1]))] for k, v in fix.items()]
    s = Solver(name="cadical195", bootstrap_with=defs + units)
    for n in names:
        for c in G[n]:
            s.add_clause(c + [-sel[n]])
    if s.solve(assumptions=[sel[n] for n in names]):
        return None
    core = [n for n in names if sel[n] in set(s.get_core())]
    i = 0
    while i < len(core):
        trial = core[:i] + core[i + 1:]
        if not s.solve(assumptions=[sel[n] for n in trial]):
            c2 = set(s.get_core()); core = [n for n in trial if sel[n] in c2]
        else:
            i += 1
    return core

if __name__ == "__main__":
    idle()
    E = [tuple(sorted((int(x[0]), int(x[1])))) for x in sys.argv[1].split()]
    k = int(sys.argv[2])
    cnf_u, pool_u, Xu, Zu = schi_system.build(E, signed=False)
    keys = sorted(Xu)
    m = Solver(name="cadical195", bootstrap_with=cnf_u.clauses)
    kinds = collections.Counter()
    for it in range(k):
        if not m.solve():
            break
        val = set(l for l in m.get_model() if l > 0)
        fix = {key: (Xu[key] in val) for key in keys}
        m.add_clause([-Xu[key] if fix[key] else Xu[key] for key in keys])
        t0 = time.time(); core = mus_fixed(E, fix)
        if core is None:
            print("chi #%d : SAT signe !" % it, flush=True); continue
        kinds[tuple(sorted(n.split("(")[0] for n in core))] += 1
        print("chi #%d : noyau %d groupes (%.1f s) : %s" % (it, len(core), time.time() - t0, " ".join(sorted(core))), flush=True)
    print("types de noyaux :", dict(kinds))
