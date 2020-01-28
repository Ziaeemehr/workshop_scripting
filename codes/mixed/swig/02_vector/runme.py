# file: runme.py

import example
from sys import exit

# Call average with a Python list...

print example.average([1, 2, 3, 4])
# print example.averagePair([1, 2], [3, 4])
# ... or a wrapped std::vector<int>

v = example.IntVector(4)
for i in range(len(v)):
    v[i] = i + 1
print example.average(v)


# half will return a Python list.
# Call it with a Python tuple...

print example.half((1.0, 1.5, 2.0, 2.5, 3.0))

# ... or a wrapped std::vector<double>

v = example.DoubleVector()
for i in [1, 2, 3, 4]:
    v.append(i)
print example.half(v)
print type(example.half(v)) #returns a tuple

# now halve a wrapped std::vector<double> in place

example.halve_in_place(v)
for i in range(len(v)):
    print v[i], "; ",
print


int2d = example.reshape_2d([1, 2, 3, 4], 2)
print int2d

