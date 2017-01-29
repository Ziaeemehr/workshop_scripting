import numpy as np
import matplotlib.pyplot as plt


x = np.array([i*.1 for i in range(100)])
y = np.sin(x)
y2 = np.cos(x)


plt.plot(x,y,'o')
plt.plot(x,y2,'o')
plt.figure()
plt.scatter(x,y)
plt.scatter(x,y2)
plt.show()
