import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)
j = 1
y = np.sin( np.pi*x*j ) / ( np.pi*x*j )
fig = plt.figure()
ax = fig.add_subplot(111)
#plot a line along points x,y
line, = ax.plot(x, y)
#update data
j = 2
y2 = np.sin( np.pi*x*j ) / ( np.pi*x*j )
#update the line with the new data
line.set_ydata(y2)

plt.show()