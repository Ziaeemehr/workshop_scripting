import gzip
import numpy as np 


n = 1000
a = np.random.rand(n,n)
np.savetxt("file.txt", a, fmt="%15.9f")

with gzip.open('file.gz', 'wb') as f:
    f.write(a)
np.savez("file", a=a)