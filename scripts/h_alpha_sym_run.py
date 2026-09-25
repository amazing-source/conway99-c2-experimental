import sys, time
sys.path.insert(0, "scripts")
import m1_blocks4 as M
typed = sys.argv[1] == "typed"
surv, tot, nreps, done = M.run_H_sym(typed, 285, only_alpha=True)
print(sys.argv[1], "| D7-orbits of orientations:", nreps, "| alpha-skeletons (weighted):", dict(sorted(tot.items())))
print("  survivors:", dict(sorted(surv.items())), "" if done else "(TIME CAP: partial)")
