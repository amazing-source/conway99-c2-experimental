"""Classification des 56 graphes chi-SAT sous le systeme chi signe (schi_system, notes/19 §4-5).

Ordre croissant du nombre d'aretes ; un graphe contenant un graphe schi-UNSAT est UNSAT (monotonie, herite) ; sinon resolution
dans un processus fils Idle coupe a T secondes.  Ecrit au fil de l'eau dans logs/schi_classify.txt.
Usage : python schi_classify.py <T> [T_etoile]   (T_etoile : limite pour les graphes contenant K_{1,3}, plus durs ; defaut T)
"""
import sys, os, time, multiprocessing as mp
import networkx as nx
from networkx.algorithms import isomorphism as iso
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from rs_experiments import MAXSAT, parse, edges_str, idle, free_gb

def contains(host, pat):
    return iso.GraphMatcher(host, pat).subgraph_is_monomorphic()

def graph(E):
    g = nx.Graph(); g.add_nodes_from(range(1, 8)); g.add_edges_from(E); return g

def _w(E, q):
    idle()
    import schi_system
    q.put(schi_system.run(E))

def solve(E, T):
    q = mp.Queue(); p = mp.Process(target=_w, args=(E, q)); p.start(); t0 = time.time()
    while p.is_alive() and time.time() - t0 < T:
        p.join(1.0)
        if free_gb() < 3.0:
            p.terminate(); p.join(); return ("MEMSTOP", time.time() - t0)
    if p.is_alive():
        p.terminate(); p.join(); return ("TIMEOUT", T)
    try:
        r = q.get(timeout=10); return (r[0], r[1])
    except Exception:
        return ("ERREUR", 0)

if __name__ == "__main__":
    idle()
    T = float(sys.argv[1]); Tst = float(sys.argv[2]) if len(sys.argv) > 2 else T
    k13 = graph([(1, 2), (1, 3), (1, 4)])
    maxg = [graph(parse(s)) for s in MAXSAT]
    atlas = [nx.relabel_nodes(g, {i: i + 1 for i in range(7)}) for g in nx.graph_atlas_g() if g.number_of_nodes() == 7]
    chisat = sorted([g for g in atlas if any(contains(h, g) for h in maxg)], key=lambda g: g.number_of_edges())
    out = open("logs/schi_classify.txt", "a", encoding="utf-8")
    def log(s):
        print(s, flush=True); out.write(s + "\n"); out.flush()
    log("== %s : %d graphes chi-SAT, T=%.0f s (etoiles K13 : %.0f s)" % (time.strftime("%Y-%m-%d %H:%M"), len(chisat), T, Tst))
    unsat = []
    for g in chisat:
        E = sorted(tuple(sorted(e)) for e in g.edges())
        if E and any(contains(g, u) for u in unsat):
            log("%-24s aretes=%d  UNSAT (herite)" % (edges_str(E), len(E))); continue
        if not E:
            log("%-24s aretes=0  SAT (aucune ligne)" % "-"); continue
        r = solve(E, Tst if contains(g, nx.Graph(list(k13.edges()))) else T)
        log("%-24s aretes=%d  %-7s %.1f s" % (edges_str(E), len(E), r[0], r[1]))
        if r[0] == "UNSAT":
            unsat.append(graph(E))
