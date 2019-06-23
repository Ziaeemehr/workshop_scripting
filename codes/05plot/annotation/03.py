import matplotlib.pyplot as plt
import numpy as np

# Make some fake data and a sample plot
x = np.arange(1, 10)
y = x**2
fig, ax = plt.subplots(1, figsize=(12, 8))
# ax = plt.axes()
ax.plot(x, y)

# Adjust the fontsizes on tick labels for this plot
fs = 14.0

ax.annotate(
    'S', xytext=(-0.11, 0.477), xy=(-0.1, 0.5),
    xycoords='axes fraction',
    fontsize=fs*1.5, ha='center', va='bottom',
    bbox=dict(boxstyle='square', fc='white'),
    arrowprops=dict(arrowstyle='-[, widthB=10.0, lengthB=0.5, angleB=90',
                    lw=2.0))

# plt.tight_layout()
plt.savefig('03')
