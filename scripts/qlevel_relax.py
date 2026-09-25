"""Relaxation NON SIGNEE (niveau Q) du probleme local de l'etoile libre (note 23 §10).
Chaque orbite lointaine V_k = {z_k, -z_k} (30) recoit la paire kappa NON ORDONNEE {Phi(z_k), Phi(-z_k)} (deux paires images).
Variables : l[w, k] = « la racine image w est dans la paire kappa de l'orbite k » (chaque w : un k ; chaque k : deux w) ;
x[w, w'] = « w et w' forment une paire kappa ».  Contraintes :
  (iii) : #{paires kappa {w, w'} : b dans w, d dans w' (ou l'inverse)} = Ct[b, d] (diag : Ct/2) ;
  (ii) somme sur +-e_i : pour chaque bloc i du domaine et b dans X : sum_{k : V_k touche i} sum_{w contient b} l[w, k]
        = Cx[e_i, b] + Cx[-e_i, b] ;
  equilibre (§8) : |z_k inter S| + |w inter S| + |w' inter S| = |S|/2 (option) ;
  (optionnel) (ii) complet : non (signes oublies).
CP-SAT 1 fil : on ne consigne que les reponses definitives.
Usage : python qlevel_relax.py <partition> <indices> <secondes> [bal 0/1]
"""
import sys, os, time, itertools, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freestar_compact import targets, types
from make_freestar_sos_cnf import orbit_map
from ortools.sat.python import cp_model

def model(mu, tau, bal=True):
    Cx, Ct = targets(mu, tau, 12)
    P = [(a, b) for a in range(12) for b in range(a + 1, 12) if mu[a] != b]
    R = [(a, b) for a in range(12) for b in range(a + 1, 12) if a // 2 != b // 2]
    neg = lambda z: tuple(sorted((z[0] ^ 1, z[1] ^ 1)))
    zreps = []; seen = set()
    for z in R:
        if z in seen: continue
        seen.add(z); seen.add(neg(z)); zreps.append(z)
    orb = orbit_map(mu, tau, 12); osz = collections.Counter(orb.values())
    m = cp_model.CpModel()
    l = {(w, k): m.NewBoolVar("") for w in range(60) for k in range(30)}
    for w in range(60): m.AddExactlyOne(l[w, k] for k in range(30))
    for k in range(30): m.Add(sum(l[w, k] for w in range(60)) == 2)
    x = {}
    for w, v in itertools.combinations(range(60), 2):
        x[w, v] = m.NewBoolVar("")
        for k in range(30):
            m.AddBoolOr([l[w, k].Not(), l[v, k].Not(), x[w, v]])
    X = lambda w, v: x[min(w, v), max(w, v)]
    for w in range(60):
        m.AddExactlyOne(X(w, v) for v in range(60) if v != w)
    cov = collections.defaultdict(list)
    for (w, v), var in x.items():
        for b in P[w]:
            for d in P[v]:
                cov[min(b, d), max(b, d)].append(var)
    for b in range(12):
        for d in range(b, 12):
            tgt = int(Ct[b, d]) // 2 if b == d else int(Ct[b, d])
            m.Add(sum(cov[b, d]) == tgt)
    for i in range(6):
        ks = [k for k in range(30) if i in (zreps[k][0] // 2, zreps[k][1] // 2)]
        for b in range(12):
            m.Add(sum(l[w, k] for k in ks for w in range(60) if b in P[w]) == int(Cx[2 * i, b] + Cx[2 * i + 1, b]))
    if bal and len(osz) > 1:
        for k in range(30):
            z = zreps[k]
            for o in osz:
                need = osz[o] // 2 - sum(1 for y in z if orb[y] == o)
                m.Add(sum(l[w, k] * sum(1 for y in P[w] if orb[y] == o) for w in range(60)) == need)
    return m

if __name__ == "__main__":
    import ctypes; ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x40)
    part = tuple(int(c) for c in sys.argv[1]); T = float(sys.argv[3]); bal = (sys.argv[4] == "1") if len(sys.argv) > 4 else True
    mu, reps, st = types(part)
    for ti in [int(v) for v in sys.argv[2].split(",")]:
        m = model(mu, reps[ti], bal)
        s = cp_model.CpSolver(); s.parameters.num_workers = 1; s.parameters.max_time_in_seconds = T
        r = s.Solve(m)
        print("A%s tau#%d niveau Q (bal=%d) : %s (%.1f s)" % (sys.argv[1], ti, bal, s.StatusName(r), s.WallTime()), flush=True)
