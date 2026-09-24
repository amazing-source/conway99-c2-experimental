"""Liste explicite des 39 survivants chi-SAT (notes/18 §8) : graphes a 7 sommets sans configuration certifiee (DRAT) et chi-SAT.
Ecrit data/survivors39.txt (une ligne par graphe : aretes, degres)."""
import sys
import networkx as nx
sys.path.insert(0, "scripts")
from sigma_survivors_v2 import edges_of, contains
def _certified_safe():
    out = {}
    for line in open("data/cert_results.txt", encoding="utf-8"):
        f = line.split()
        if len(f) >= 6 and f[1] == "UNSAT" and f[5] == "drat=VERIFIED" and not f[0].startswith("chi_"):
            out[f[0]] = edges_of(f[0][len("stageQ_"):] if f[0].startswith("stageQ_") else f[0])
    return out
from schi_classify import graph
from rs_experiments import MAXSAT, parse, edges_str
forb = {k: v for k, v in _certified_safe().items()}
maxg = [graph(parse(s)) for s in MAXSAT]
atlas = [nx.relabel_nodes(g, {i: i + 1 for i in range(7)}) for g in nx.graph_atlas_g() if g.number_of_nodes() == 7]
surv = [g for g in atlas if not any(contains(g, e) for e in forb.values())]
chisat = [g for g in surv if any(contains(h, list(g.edges())) for h in maxg)]
k13 = nx.star_graph(3)
with open("data/survivors39.txt", "w", encoding="utf-8", newline="\n") as f:
    for g in sorted(chisat, key=lambda g: g.number_of_edges()):
        E = sorted(tuple(sorted(e)) for e in g.edges())
        line = "%-24s aretes=%d degmax=%d K13=%s" % (edges_str(E), len(E), max(dict(g.degree()).values()), "oui" if contains(g, list(k13.edges())) else "non")
        print(line); f.write(line + "\n")
print(len(surv), len(chisat))
