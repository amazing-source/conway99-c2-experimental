"""Graphes Sigma survivants apres les certificats DRAT (notes/18).

Interdits = configurations de data/cert_results.txt au verdict UNSAT drat=VERIFIED (modele complet, ou etage Q pour les lignes stageQ_*),
avec leurs aretes lues dans data/cnf/MANIFEST.txt.  Semantique « au moins ces paires » : un graphe Sigma contenant une configuration
interdite comme sous-graphe (non necessairement induit) est impossible.
Sortie : nombre de survivants par nombre d'aretes, survivants maximaux ; et, si demande, le statut chi de chaque survivant.
Usage : python sigma_survivors_v2.py [chi]
"""
import itertools, sys
import networkx as nx
from networkx.algorithms import isomorphism as iso
sys.path.insert(0, "scripts")

def edges_of(name):
    for line in open("data/cnf/MANIFEST.txt", encoding="utf-8"):
        if line.split()[1] == name + ".cnf":
            return [(int(p[0]), int(p[1])) for p in line.split("pairs=[")[1].split("]")[0].split()]
    raise KeyError(name)

def certified():
    out = {}
    for line in open("data/cert_results.txt", encoding="utf-8"):
        f = line.split()
        if len(f) >= 6 and f[1] == "UNSAT" and f[5] == "drat=VERIFIED":
            name = f[0][len("stageQ_"):] if f[0].startswith("stageQ_") else f[0]
            out[f[0]] = edges_of(name)
    return out

def contains(host, pat_edges):
    pat = nx.Graph(); pat.add_edges_from(pat_edges)
    return iso.GraphMatcher(host, pat).subgraph_is_monomorphic()

if __name__ == "__main__":
    forb = certified()
    print("configurations interdites certifiees (DRAT) : %d" % len(forb))
    atlas = [g for g in nx.graph_atlas_g() if g.number_of_nodes() == 7]
    host = lambda g: nx.relabel_nodes(g, {i: i + 1 for i in range(7)})
    surv = [g for g in atlas if not any(contains(host(g), e) for e in forb.values())]
    by_m = {}
    for g in surv:
        by_m.setdefault(g.number_of_edges(), []).append(g)
    print("graphes a 7 sommets : %d ; survivants : %d ; aretes max : %d" % (len(atlas), len(surv), max(by_m)))
    for m in sorted(by_m):
        print("   %2d aretes : %d" % (m, len(by_m[m])))
    maxi = []
    for g in surv:
        ext = False
        for u, v in itertools.combinations(range(7), 2):
            if g.has_edge(u, v):
                continue
            h = g.copy(); h.add_edge(u, v)
            if not any(contains(host(h), e) for e in forb.values()):
                ext = True; break
        if not ext:
            maxi.append(g)
    print("survivants maximaux : %d" % len(maxi))
    for g in sorted(maxi, key=lambda g: -g.number_of_edges()):
        print("   %d aretes : %s" % (g.number_of_edges(), " ".join("%d%d" % (a + 1, b + 1) for a, b in sorted(g.edges()))))
    if len(sys.argv) > 1 and sys.argv[1] == "chi":
        from chi_system import run
        st = {}
        for g in surv:
            S = [(a + 1, b + 1) for a, b in g.edges()]
            st[id(g)] = run("s", S)[0]
        n_unsat = sum(1 for g in surv if st[id(g)] == "UNSAT")
        print("parmi les survivants : chi-UNSAT %d, chi-SAT %d" % (n_unsat, len(surv) - n_unsat))
        for g in sorted(surv, key=lambda g: -g.number_of_edges()):
            if st[id(g)] == "UNSAT":
                print("   chi-UNSAT : %d aretes : %s" % (g.number_of_edges(), " ".join("%d%d" % (a + 1, b + 1) for a, b in sorted(g.edges()))))
