"""Feasible orientations of the orientation-first campaign (logs/orient_<ci>.jsonl) -> ptype list for run_U_fix.py (note 43).
ptype: pair {c,x} with x in In[c] -> ["anch", c]; twisted pair -> ["tw"].
Usage: python orient_to_ptype.py <ci> > logs/orient_<ci>_feasible_ptype.json"""
import sys, json
sys.path.insert(0, "scripts")
import mix_filter6 as F
ci = int(sys.argv[1]); twE = {tuple(sorted(e)) for e in F.twisted_classes()[ci]}; out = []
for line in open("logs/orient_%d.jsonl" % ci):
    r = json.loads(line)
    if r["status"] != "feasible": continue
    In = {int(c): v for c, v in r["In"].items()}; pt = {}
    for a in range(7):
        for b in range(a + 1, 7):
            if (a, b) in twE: pt["%d,%d" % (a, b)] = ["tw"]
            elif a in In[b]: pt["%d,%d" % (a, b)] = ["anch", b]
            else: assert b in In[a]; pt["%d,%d" % (a, b)] = ["anch", a]
    out.append({"tag": "c%d_o%d" % (ci, r["idx"]), "ptype": pt})
print(json.dumps(out))
