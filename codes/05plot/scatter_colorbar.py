import matplotlib.pyplot as plt
import numpy as np 

cm = plt.cm.get_cmap('RdYlBu')
xy = np.linspace(0, 1, 20)
z = xy
sc = plt.scatter(xy, xy, c=z, vmin=0, vmax=1, s=35, cmap=cm)
plt.colorbar(sc)
plt.show()