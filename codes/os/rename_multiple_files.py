import numpy as np 
import os
import glob


g   = np.arange(1, 5+1./16, 1./16)
tau = np.arange(4, 8+1./16, 1./16)

ni = len(g)
nj = len(tau)

for i in range(ni):
    for j in range(nj):
        old_name = "Cor-"+str("%.3f"%g[i])+"-"+str("%.3f"%tau[j])+".txt"
        new_name = "Cor-"+str("%.6f"%g[i])+"-"+str("%.6f"%tau[j])+".txt"
        os.rename(old_name, new_name)



>>> "%06.2f"%3.3
'003.30'
>>> "%04.f"%3.2
'0003'

# abc_2000.jpg
# abc_2001.jpg
# abc_2004.jpg
# abc_2007.jpg

# into the following ones:

# year_2000.jpg
# year_2001.jpg
# year_2004.jpg
# year_2007.jpg

files = glob.glob('year*.jpg')
for file in files:
    os.rename(file, 'year_{}'.format(file.split('_')[1]))

for file in files:
    parts = file.split('_') #[abc, 2000.jpg]
    new_name = 'year_{}'.format(parts[1]) #year_2000.jpg
    os.rename(file, new_name)
