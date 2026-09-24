"""Automated discovery loop for the possible sib graphs Sigma (graphs on the 7 x-lines; edges = grids through x).

State file data/sib_state.json: {"forbidden": {name: {"edges": [...], "status": "certified"|"observed"}}, "hard": {name: {"edges", "tlimit"}}}
Loop: maximal survivors (graphs avoiding every forbidden one, maximal for this property) that are not known 'hard' are tested with kissat in
Docker (satbox-proof) with a binary DRAT proof checked by drat-trim (scripts/cert_run.sh).  UNSAT+VERIFIED -> forbidden(certified);
UNSAT without verification -> forbidden(observed); UNKNOWN -> hard.  Also certifies 'observed' entries.  Stops when nothing is left to test.
Usage: python sib_loop.py <kissat_seconds> <parallel>
"""
import itertools, json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
import networkx as nx
from networkx.algorithms import isomorphism as iso

HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.path.abspath(os.path.join(HERE, ".."))
STATE = os.path.join(LAB, "data", "sib_state.json")
PY = os.path.join(LAB, ".venv", "Scripts", "python.exe")


def G(edges):
    g = nx.Graph(); g.add_nodes_from(range(1, 8)); g.add_edges_from(edges); return g


def contains(host, pat_edges):
    pat = nx.Graph(); pat.add_edges_from(pat_edges)
    return iso.GraphMatcher(host, pat).subgraph_is_monomorphic()


def canon_name(g):
    return "g%02d_%s" % (g.number_of_edges(), nx.weisfeiler_lehman_graph_hash(g, iterations=4)[:10])


def maximal_survivors(forb):
    atlas = [nx.relabel_nodes(g, {i: i + 1 for i in range(7)}) for g in nx.graph_atlas_g() if g.number_of_nodes() == 7]
    surv = [g for g in atlas if not any(contains(g, e) for e in forb)]
    maxi = []
    for g in surv:
        ok = True
        for u, v in itertools.combinations(range(1, 8), 2):
            if g.has_edge(u, v): continue
            h = g.copy(); h.add_edge(u, v)
            if not any(contains(h, e) for e in forb):
                ok = False; break
        if ok: maxi.append(g)
    return surv, maxi


def load():
    if os.path.exists(STATE): return json.load(open(STATE))
    return {"forbidden": {}, "hard": {}}


def save(st):
    json.dump(st, open(STATE, "w"), indent=1)


def run_job(name, edges, tl):
    pairs = " ".join("%d%d" % (a, b) for a, b in sorted((min(e), max(e)) for e in edges))
    subprocess.run([PY, os.path.join(HERE, "make_cnf.py"), name, pairs], check=True, capture_output=True,
                   env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    env = dict(os.environ, MSYS_NO_PATHCONV="1")
    r = subprocess.run(["docker", "run", "--rm", "--cpus", "1", "-v", LAB.replace("\\", "/") + ":/lab", "satbox-proof",
                        "bash", "/lab/scripts/cert_run.sh", name, str(int(tl))], capture_output=True, text=True, env=env)
    line = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "ERR"
    try: os.remove(os.path.join(LAB, "data", "cnf", name + ".cnf"))
    except OSError: pass
    return line


def main():
    tl = float(sys.argv[1]); par = int(sys.argv[2])
    max_it = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    st = load()
    it = 0
    while it < max_it:
        it += 1
        forb = [v["edges"] for v in st["forbidden"].values()]
        surv, maxi = maximal_survivors(forb)
        todo = []
        for g in maxi:
            nm = canon_name(g)
            if nm in st["hard"] and st["hard"][nm]["tlimit"] >= tl: continue
            todo.append((nm, [list(e) for e in g.edges()]))
        obs = [(k, v["edges"]) for k, v in st["forbidden"].items() if v["status"] == "observed"]
        print("iteration %d: survivors %d, maximal %d, to test %d, observed-to-certify %d" % (it, len(surv), len(maxi), len(todo), len(obs)), flush=True)
        if not todo and not obs: break
        jobs = [("T", n, e) for n, e in todo] + [("C", n, e) for n, e in obs]
        with ThreadPoolExecutor(max_workers=par) as ex:
            res = list(ex.map(lambda j: (j, run_job(j[1], j[2], tl)), jobs))
        for (kind, nm, e), line in res:
            print("   %s %s %s" % (kind, nm, line), flush=True)
            parts = line.split()
            verdict = parts[1] if len(parts) > 1 else "ERR"
            drat = parts[5] if len(parts) > 5 else ""
            if verdict == "UNSAT":
                st["forbidden"][nm] = {"edges": e, "status": "certified" if drat == "drat=VERIFIED" else "observed_uncertifiable"}
            elif kind == "T":
                st["hard"][nm] = {"edges": e, "tlimit": tl, "result": verdict}
            elif kind == "C":
                st["forbidden"][nm]["status"] = "observed_timeout_in_kissat"
        save(st)
    surv, maxi = maximal_survivors([v["edges"] for v in st["forbidden"].values()])
    print("FINAL: survivors %d ; max edges %d ; maximal survivors:" % (len(surv), max(g.number_of_edges() for g in surv)), flush=True)
    for g in maxi:
        print("   ", canon_name(g), sorted(g.edges()), flush=True)


if __name__ == "__main__":
    main()
