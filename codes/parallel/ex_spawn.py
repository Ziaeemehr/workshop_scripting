from multiprocessing.dummy import freeze_support
from multiprocessing import Pool
import multiprocessing as mp
from time import sleep
import numpy as np
from tqdm import tqdm
import os 
# mp.set_start_method('spawn', force=True)


def sumj(i, ): 
    print(i, os.getpid())

    sleep(0.5)
    # return np.sum(arr)
    return i


if __name__ == "__main__":

    # freeze_support()

    mat = np.ones((40, 10))

    # with Pool(processes=4) as pool:
    #     # data = [pool.apply(sumj, args=(i, mat[i, :])) for i in range(mat.shape[0])]
    #     data = [pool.apply(sumj, args=(i,)) for i in range(mat.shape[0])]
    #     # data = pool.map(sumj, range(mat.shape[0]))
    #     # print(p.map(f, [1,2,3,4,5,6,7,8]))
    # print(data)

    # n_total = mat.shape[0]
    # with Pool(processes=4) as pool:
    #     data = list(tqdm([pool.apply(sumj, args=(i, mat[i, :]))
    #                 for i in range(mat.shape[0])], total=n_total))

    pool = Pool(processes=10)
    for i in range(40):
        pool.apply(sumj, (i, ))
    #pool.apply_async(runBamHashWorker, (element, ))
    pool.close()
    pool.join()