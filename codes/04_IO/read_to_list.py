import numpy as np


def read_from_file(filename, n):
    spikes = []
    with open(filename, "r") as f:
        for i in range(n):
            data = f.readline().split()
            data = [float(i) for i in data]
            print i, data[0], type(data[0])
            spikes.append(data)
    return spikes    
    
A = read_from_file("data.txt",2)
print len(A)

for i in range(len(A)):
    for j in range(len(A[i])):
        print A[i][j],
    print ""