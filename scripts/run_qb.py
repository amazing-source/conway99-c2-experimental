import sys; sys.path.insert(0, "scripts")
from gauss_propagator import run_qb
if __name__ == "__main__":
    which, T = sys.argv[1], float(sys.argv[2])
    tests = {"K2": ([(1, 2)], False), "2K2": ([(1, 2), (3, 4)], False), "K13": ([(1, 2), (1, 3), (1, 4)], False),
             "K13facts": (None, True)}
    E, facts = tests[which]; run_qb(which, E, facts, T)
