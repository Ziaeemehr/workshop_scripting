import time
#from scitools.std import *
from matplotlib.pyplot import *
from numpy import *



figure()
x = linspace(-1,1,51)
plot(sin(x))
for i in range(10):
    plot([sin(i+j) for j in x])
    # make it appear immediately
    draw()
    pause(0.5)

figure()
tstart = time.time()               # for profiling
x = arange(0,2*pi,0.01)            # x-array
line, = plot(x,sin(x))
for i in arange(1,50):
    line.set_ydata(sin(x+i/10.0))  # update the data
    draw()                         # redraw the canvas
    pause(0.01)

print 'FPS:' , 50/(time.time()-tstart)

show()