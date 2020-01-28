import time
from threading import Thread
from os import system

def myfunc(i):
    command = " echo thread %d is running" % i
    system(command)
    time.sleep(5)
    print ("finished running of thread %d" % i)

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()