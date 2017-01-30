#!/usr/bin/python
import time

start = time.time()
print("hello")
end = time.time()
print(end - start)

#-------------------------------------------------

def procedure():
    time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"

# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"
#-------------------------------------------------



from timeit import default_timer as timer

a = ['Hello', 'Jello', 'Hello', 'Hello']

start = timer()
b = [1 if x == 'Hello' else 0 for x in a]
print b
end = timer()
print('without cast: {}'.format(end - start))
#or simply
print end-start

start = timer()
b = [int(x == 'Hello') for x in a]
print b
end = timer()
print('with cast   : {}'.format(end - start))
#-----------------------------------------------#

