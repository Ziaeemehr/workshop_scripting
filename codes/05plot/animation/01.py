import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#update set line a value(a list) of dict data
def update_line(num ,data, line):
    y = data[num*0.1]
    line.set_data(range(len(y)), y)

fig1 = plt.figure()

# just creat a dictionary of lists by variable length
data = {}
for i in range(200):
    t = i*0.1
    data[t] = [j*.5 for j in range(np.random.randint(2,5))]

l, = plt.plot([], [], 'r-')
line_ani = animation.FuncAnimation(fig1, update_line, 20, fargs=(data, l),
                                   interval=500, repeat=True)
plt.xlim(0,5)
plt.ylim(0,2.5)
plt.show()