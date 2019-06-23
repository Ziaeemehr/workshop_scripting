import matplotlib.pyplot as plt
import numpy as np

# Make some fake data and a sample plot
x = np.arange(1,10)
y = x**2
fig, ax = plt.subplots(1,figsize=(12,8))
# ax = plt.axes()
ax.plot(x,y)

# Adjust the fontsizes on tick labels for this plot
fs = 14.0
# [t.set_fontsize(fs) for t in ax.xaxis.get_majorticklabels()]
# [t.set_fontsize(fs) for t in ax.yaxis.get_majorticklabels()]
# ax.yaxis.get_offset_text().set_fontsize(fs)

# Here is the label and arrow code of interest
ax.annotate('SDL', xy=(0.5, 1.05), xytext=(0.5, 1.1), xycoords='axes fraction', 
            fontsize=fs*1.5, ha='center', va='bottom',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='-[, widthB=7.0, lengthB=0.5', lw=2.0))

ax.annotate('S', xytext=(-0.15, 0.477), xy=(-0.1, 0.5), xycoords='axes fraction', 
            fontsize=fs*1.5, ha='center', va='bottom',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='-[, widthB=10.0, lengthB=0.5', lw=2.0))

# plt.tight_layout()
plt.savefig('02')