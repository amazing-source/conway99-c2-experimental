"""Which graphs on the 7 blocks can be the sib graph (edges = sib pairs = grids through x) if the listed configurations are impossible?
'At least' semantics: a sib graph containing a forbidden configuration as a (not necessarily induced) subgraph is impossible.
Uses networkx's graph atlas (all 1253 graphs on 7 vertices) and subgraph monomorphism.
"""
import itertools, json, os, sys
import networkx as nx
from networkx.algorithms import isomorphism as iso

def G(edges):
    g = nx.Graph(); g.add_nodes_from(range(1, 8)); g.add_edges_from(edges); return g

FORBIDDEN = {
    "K2K2P3": [(1, 2), (3, 4), (5, 6), (6, 7)],
    "K3K2K2": [(1, 2), (1, 3), (2, 3), (4, 5), (6, 7)],
    "K2P5": [(1, 2), (3, 4), (4, 5), (5, 6), (6, 7)],
    "K2spider": [(1, 2), (3, 4), (4, 5), (5, 6), (4, 7)],
    "P4P3": [(1, 2), (2, 3), (3, 7), (4, 5), (5, 6)],
    "K13P3": [(1, 2), (1, 3), (1, 4), (5, 6), (6, 7)],
    "K4": [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)],
    "K3K3": [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)],
    "C6": [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 6)],
    "K2K3pend": [(1, 2), (3, 4), (3, 5), (3, 7), (5, 7)],
    # wave 2 (maximal survivors of wave 1 found UNSAT by CaDiCaL; relabelled 0..6 -> 1..7)
    "K114": [(1, 5), (1, 6), (2, 5), (2, 6), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)],
    "S8": [(1, 2), (1, 3), (1, 5), (1, 6), (2, 3), (2, 5), (3, 6), (5, 6)],
    "S7a": [(1, 4), (1, 5), (3, 4), (3, 5), (3, 6), (3, 7), (4, 5)],
    "S7b": [(1, 3), (1, 4), (1, 6), (2, 3), (2, 6), (3, 5), (5, 6)],
    "S7c": [(2, 3), (2, 6), (3, 4), (3, 5), (4, 7), (5, 6), (6, 7)],
    "S6": [(1, 2), (2, 6), (2, 7), (4, 7), (5, 6), (6, 7)],
}

def contains(host, pat_edges):
    pat = nx.Graph(); pat.add_edges_from(pat_edges)
    return iso.GraphMatcher(host, pat).subgraph_is_monomorphic()

def main(which):
    forb = {k: v for k, v in FORBIDDEN.items() if k in which}
    atlas = [g for g in nx.graph_atlas_g() if g.number_of_nodes() == 7]
    surv = []
    for g in atlas:
        if not any(contains(g, e) for e in forb.values()):
            surv.append(g)
    by_m = {}
    for g in surv: by_m.setdefault(g.number_of_edges(), []).append(g)
    print("graphs on 7 vertices: %d ; surviving: %d ; max edges among survivors: %d" % (len(atlas), len(surv), max(by_m)))
    for m in sorted(by_m):
        print("  %2d edges: %d graphs" % (m, len(by_m[m])))
    # maximal survivors (not contained in another survivor with one more edge)
    maxi = []
    for g in surv:
        ext = False
        for u, v in itertools.combinations(range(7), 2):
            if g.has_edge(u, v): continue
            h = g.copy(); h.add_edge(u, v)
            if not any(contains(h, e) for e in forb.values()):
                ext = True; break
        if not ext: maxi.append(g)
    print("maximal surviving sib graphs: %d" % len(maxi))
    for g in sorted(maxi, key=lambda g: -g.number_of_edges()):
        degs = sorted((d for _, d in g.degree()), reverse=True)
        comps = sorted((len(c) for c in nx.connected_components(g)), reverse=True)
        print("   edges=%d degrees=%s components=%s edgelist=%s" % (g.number_of_edges(), degs, comps, sorted(g.edges())))

if __name__ == "__main__":
    which = sys.argv[1].split(",") if len(sys.argv) > 1 else list(FORBIDDEN)
    main(which)
