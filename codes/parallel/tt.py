from multiprocessing import Pool
from time import sleep
import numpy as np
import os 

# from multiprocessing.dummy import freeze_support
# from tqdm import tqdm
# import multiprocessing as mp
# mp.set_start_method('spawn', force=True)


def sumj(i, arr): 
    print(i, os.getpid())

    sleep(0.5)
    return np.sum(arr)


if __name__ == "__main__":

    print("*"*10)
    mat = np.ones((40, 10))
    pool = Pool(processes=10)
    results = [pool.apply_async(sumj, args=(i, mat[i,:])) for i in range(40)]
    print([i.get() for i in results])


