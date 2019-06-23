import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(0, 1.5),
            arrowprops=dict(facecolor='red', shrink=0.1,
            width=1, headwidth=8),
            )

ax.annotate('local max', xy=(3, 1),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )

ax.annotate("",
            xy=(0.2, 0.2), xycoords='axes fraction',
            xytext=(0.8, 0.8), textcoords='axes fraction',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3, rad=0.3"),
            )
ax.set_ylim(-2,2)
plt.savefig('01')
