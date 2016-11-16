#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
# vstack Stack arrays in sequence vertically (row wise).
A = np.vstack([x, np.ones(len(x))]).T
print A
#We can rewrite the line equation as y = Ap, where A = [[x 1]] and p = [[m], [c]]. Now use lstsq to solve for p:
m, c = np.linalg.lstsq(A, y)[0]
print m, c


plt.plot(x, y, 'o', label='Original data', markersize=5)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend(frameon=False)
plt.show()