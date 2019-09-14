import numpy as np
import time
from sys import exit


def generate_text_file(nrows=100, ncols=20):
    data = np.random.random((nrows, ncols))
    np.savetxt('large.txt', data, delimiter=',')


def iter_loadtxt(filename, skiprows=0, dtype=float):
    def iter_func():
        with open(filename, 'r') as infile:
            for _ in range(skiprows):
                next(infile)
            for line in infile:
                line = line.rstrip().split()
                for item in line:
                    yield dtype(item)
        iter_loadtxt.rowlength = len(line)

    data = np.fromiter(iter_func(), dtype=dtype)
    data = data.reshape((-1, iter_loadtxt.rowlength))
    return data


def iter_loadtxt1(filename, skiprows=0, dtype=float):
    def iter_func():
        with open(filename, 'r') as infile:
            for _ in range(skiprows):
                next(infile)
            for line in infile:
                line = line.rstrip().split()
                for item in line:
                    yield dtype(item)
        iter_loadtxt.rowlength = len(line)

    data = np.fromiter(iter_func(), dtype=dtype)
    data = data.reshape((-1, iter_loadtxt.rowlength))
    return data


data = generate_text_file()


t1 = time.clock()
data0 = iter_loadtxt('large.txt')
print "iter_loadtxt ", time.clock()-t1

t1 = time.clock()
data1 = np.loadtxt('pot2.txt')
print "loadtxt", time.clock()-t1

t1 = time.clock()
ifile = open('large_text_file.txt', 'r')
data2 = np.genfromtxt(ifile)
print "genfromtxt", time.clock()-t1
