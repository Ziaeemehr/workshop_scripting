from joblib import Parallel, delayed
from copy import deepcopy


def run_command(args):
    for i in args:
        print (i, args[i])

params = {"a": 1,
         "b": 2}

args = []
params["a"] = 20
args.append(deepcopy(params))
params["a"] = 10
args.append(deepcopy(params))

# print(args)

Parallel(n_jobs=1)(map(delayed(run_command), args))
