
from joblib import Parallel, delayed
import time
# def myfun(arg):
#      do_stuff
#      return result

# results = Parallel(n_jobs=-1, verbose=verbosity_level, backend="threading")(
#              map(delayed(myfun), arg_instances))

def myfun(i):
     return i*i

from os import system

def run_command(i):
	command = "echo %d" %i
	system(command)
	time.sleep(5)

Parallel(n_jobs=2, backend="threading")(
        map(delayed(run_command), range(10)))







# import multiprocessing
# import numpy as np

# if __name__ == "__main__":
#    #the previous line is necessary under windows to not execute 
#    # main module on each child under windows

#    X = np.random.normal(size=(10, 3))
#    F = np.zeros((10, ))

#    pool = multiprocessing.Pool(processes=16)
#    # if number of processes is not specified, it uses the number of core
#    F[:] = pool.map(my_function, (X[i,:] for i in range(10)) )
