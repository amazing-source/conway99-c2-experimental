"""Replay the union-LP recursion of mix_union_lp.py from its log (no LP) to recover, for every 'feasible (A fixed)' leaf, the
A-structure (D-graph of the degree-6 block A) that survived.  Output: JSON list of survivors {tag, job, In, A, twE, leaf, Adg}.
Usage: python survivor_replay.py <glob of mix6_ulp jsonl> <out json>"""
import sys, json, glob
from collections import defaultdict, Counter
sys.path.insert(0, "scripts")
import mix_enum as ME

def split_A(a, dgs):
    for x in range(7):
        if x == a: continue
        sig = defaultdict(list)
        for g in dgs: sig[tuple(sorted(y for (u, y) in g if u == x) + sorted(u for (u, y) in g if y == x))].append(g)
        if len(sig) > 1: return list(sig.values())
    return [dgs]

def replay(r):
    log = r["log"]; pos = [0]; a = r["A"]; found = []
    def nxt():
        e = log[pos[0]]; pos[0] += 1; return e
    def recA(leaf, dgs):
        e = nxt(); assert e["nA"] == len(dgs), (e, len(dgs))
        if e["status"] == 'dead': return
        if len(dgs) == 1: found.append((leaf, dgs[0], e["status"])); return
        for part in split_A(a, dgs): recA(leaf, part)
    def rec(leaves):
        e = nxt(); assert e["nleaves"] == len(leaves)
        if e["status"] == 'dead': return
        if len(leaves) == 1:
            if e["status"] == 'feasible' and a is not None:
                for part in split_A(a, ME.dgraphs([x for x in range(7) if x != a], [])): recA(leaves[0], part)
            return
        best = None
        for c in range(7):
            sig = Counter(tuple(sorted(z for z in L if z[0] == c)) for L in leaves)
            if len(sig) > 1 and (best is None or len(sig) > best[1]): best = (c, len(sig))
        c = best[0]; groups = defaultdict(list)
        for L in leaves: groups[tuple(sorted(z for z in L if z[0] == c))].append(L)
        for gl in groups.values(): rec(gl)
    return rec, found, pos

if __name__ == "__main__":
    out = []
    for f in sorted(glob.glob(sys.argv[1])):
        for l in open(f):
            r = json.loads(l)
            if not any("A fixed" in st for L, st in r["unresolved"]): continue
            # leaves of the job, in the order used by the driver
            tag = f.split("mix6_ulp_")[1].rsplit("_", 1)[0]
            rec, found, pos = replay(r)
            # the driver's job leaves are needed: rebuild from the class files
            ci = tag.replace("edges_", "E") if tag.startswith("edges_") else tag
            jobs = []
            for g in sorted(glob.glob("logs/mix6_cls_%s_S_*.json" % ci)):
                d = json.load(open(g))
                for po in d["per_orient"]:
                    if po["leaves"]: jobs.append((po, [tuple(map(tuple, L)) for L in po["leaves"]]))
            po, leaves = jobs[r["job"]]
            assert po["In"] == r["In"]
            rec(leaves); assert pos[0] == len(r["log"]), (pos[0], len(r["log"]))
            for leaf, g, st in found:
                out.append({"tag": tag, "job": r["job"], "In": r["In"], "A": r["A"], "twE": r["twE"], "leaf": [list(z) for z in leaf], "Adg": [list(e) for e in g], "status": st})
            print(tag, "job", r["job"], "survivors", len(found), "(unresolved listed:", len(r["unresolved"]), ")")
    json.dump(out, open(sys.argv[2], "w"))
