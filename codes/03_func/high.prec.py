from decimal import *
import time
start = time.clock()

getcontext().prec = 6
Decimal(1) / Decimal(7)

getcontext().prec = 28
Decimal(1) / Decimal(7)

end = time.clock()
print end - start