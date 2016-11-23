#1/usr/bin/pytho

import numpy as np
import matplotlib.pyplot as plt
import scitools.std as st
from timeit import default_timer as timer

t = np.linspace(0,3,51)
y = t*t*np.exp(-t*t)

plt.plot(t,y,'--',label='$t^2 \exp(-t^2) $')
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.axis([0, 3, -0.05, 0.6])   # [tmin, tmax, ymin, ymax]
plt.title('My first plot')
plt.legend(frameon=False)
plt.savefig('fig.png')
plt.savefig('fig.pdf')


st.plot(t, y,
     xlabel='t',
    ylabel='y',
    legend='t^2*exp(-t^2)',
    axis=[0, 3, -0.05, 0.6],
    title='My First Easyviz Demo',
    savefig='tmp1.png',
    show=True) # display on the screen (default)
