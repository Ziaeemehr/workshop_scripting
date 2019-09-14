from timeit import timeit
from numba import jit

@jit
def f(x, y):
    return x+y


def fp(x, y):
    return x+y


print f([1], [2])
# print fp([1], [2])
