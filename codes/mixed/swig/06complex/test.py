import example
import numpy as np

c = example.my_class()

c.set_value(complex(1.0,3.5), [complex(1,1.2),complex(1,1.6)])
c.print_value()
com = [complex(i,j) for i,j in zip(range(10), range(10))]
print type(com)
H = c.half(com)
print type(H), type(H[0])
print "*****"
for i in H:
	print i

com = [complex(1,2)]
HH = c.half2(com)
print type(HH), type(HH[0]), type(HH[0][0])
for i in HH:
	print i

print np.asarray(HH).shape