# https://www.youtube.com/watch?v=ifKintlPE_A
import pickle
from sys import exit 
from time import time, clock

start = time()

dict1 = {'a':100,
         'b':200,
         'c':300}

list1 = [400,500,600]

out = open('data.pkl', 'wb')
pickle.dump(dict1, out)
pickle.dump(list1, out)
out.close()

print '--------------------------'

inp = open('data.pkl', 'rb')
dict2 = pickle.load(inp)
list2 = pickle.load(inp)
inp.close()


# print dict2
print list2