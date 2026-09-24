"""Classification des graphes Sigma chi-SAT sous le systeme chi SIGNE = RSF(orbites soeurs) (modele complet restreint aux lignes soeurs).

chi-SAT = sous-graphes (monomorphes) d'un des 12 chi-SAT maximaux (notes/18, monotonie).  Ordre croissant du nombre d'aretes ;
un graphe contenant un graphe deja RSF-UNSAT est UNSAT par monotonie (herite) ; sinon on resout RSF(orbites soeurs) avec au moins
ces paires soeurs (clauses a=b=1 comme make_cnf.py), coupe a T secondes.  Ecrit au fil de l'eau dans logs/rsf_classify.txt.
Usage : python rsf_classify.py <T>
"""
import sys, os, time
import networkx as nx
from networkx.algorithms import isomorphism as iso
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from rs_experiments import solve_full, sister_orbits, MAXSAT, parse, edges_str, idle

def contains(host, pat):
    return iso.GraphMatcher(host, pat).subgraph_is_monomorphic()

def graph(E):
    g = nx.Graph(); g.add_nodes_from(range(1, 8)); g.add_edges_from(E); return g

if __name__ == "__main__":
    idle()
    T = float(sys.argv[1])
    maxg = [graph(parse(s)) for s in MAXSAT]
    atlas = [nx.relabel_nodes(g, {i: i + 1 for i in range(7)}) for g in nx.graph_atlas_g() if g.number_of_nodes() == 7]
    chisat = [g for g in atlas if any(contains(h, g) for h in maxg)]
    chisat.sort(key=lambda g: g.number_of_edges())
    out = open("logs/rsf_classify.txt", "a", encoding="utf-8")
    def log(s):
        print(s, flush=True); out.write(s + "\n"); out.flush()
    log("== %s : %d graphes chi-SAT, T=%.0f s" % (time.strftime("%Y-%m-%d %H:%M"), len(chisat), T))
    unsat = []
    for g in chisat:
        E = sorted(tuple(sorted(e)) for e in g.edges())
        if E and any(contains(g, u) for u in unsat):
            log("%-24s aretes=%d  UNSAT (herite)" % (edges_str(E), len(E))); continue
        if not E:
            log("%-24s aretes=0  SAT (aucune ligne)" % "-"); continue
        r = solve_full(sister_orbits(E), sigma=E, T=T)
        log("%-24s aretes=%d  %-7s resolution %.1f s" % (edges_str(E), len(E), r[0], r[2]))
        if r[0] == "UNSAT":
            unsat.append(graph(E))
