import numpy as np 
import csv 


a = [[1,5],[4,8]]
with open('data/01.txt', 'w') as writeFile:
    writer = csv.writer(writeFile, delimiter=' ')
    writer.writerows(a)

writeFile.close()

with open('data/01.txt', 'r') as readFile:
    reader = csv.reader(readFile, delimiter=' ')
    lines = list(reader)

    
lines = [map(float, line) for line in lines]
print lines
print type(lines[0][0])