from decimal import *
import time
start = time.clock()

getcontext().prec = 6
print Decimal(1) / Decimal(7)


getcontext().prec = 28
print Decimal(1) / Decimal(7)

end = time.clock()
print end - start

#print 1/7
print "%.28f"% (1./7)

#for i in range(len(list)):

#for in in list
