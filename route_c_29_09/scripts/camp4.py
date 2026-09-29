import sys, os, time, pickle, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.update(FD_LEMMA_U="1", FD_SYM="1", FD_PREBUDGET="0", FD_CHAR="1")
import frame_dfs as FD, bench as B
cfg = {"base": ("0", "0"), "EC": ("1", "0"), "EC+4pts": ("1", "4"), "EC+16pts": ("1", "16")}
for lid in ("078", "097"):
    L = B.lat(lid); R = [r for r in pickle.load(open(f"data/bench/{lid}.pkl", "rb")) if FD.char_trap(L, r["y1"], r["y2"]) is None][:int(sys.argv[1])]
    for name, (ec, nb) in cfg.items():
        os.environ["FD_EC"], os.environ["FD_BND"] = ec, nb; t = time.time(); nd = []; k = 0
        for r in R:
            o = FD.search(L, r["y1"], r["y2"], node_limit=3_000_000); nd.append(sum(o["nodes"])); k += o["verdict"].startswith("EXCLUDED")
        print(lid, "%-9s killed %d/%d  nodes mean %8.0f  %.2fs/pair" % (name, k, len(R), np.mean(nd), (time.time() - t) / len(R)), flush=True)
