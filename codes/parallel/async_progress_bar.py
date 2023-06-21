from multiprocessing import Pool
import tqdm
import numpy as np

def f(x):
    import time
    time.sleep(np.random.randint(1,3)) # for demo purposes
    return x*x

# Required by Windows:
if __name__ == '__main__':
    pool_size = 4
    
    # imap 
    results = []
    with Pool(processes=pool_size) as pool:
        with tqdm.tqdm(total=10) as pbar:
            for result in pool.imap(f, range(10)):
                results.append(result)
                pbar.update()
    print(results)
    
    # apply_async

    def my_callback(_):
        # We don't care about the actual result.
        # Just update the progress bar:
        pbar.update()

    with Pool(processes=pool_size) as pool:
        with tqdm.tqdm(total=10) as pbar:
            async_results = [pool.apply_async(f, args=(x,), callback=my_callback) for x in range(10)]
            results = [async_result.get() for async_result in async_results]
    print(results)

