import collections

d = collections.deque(maxlen=10)
print(d)

for i in range(20):
    d.append(i)
    print(list(d))
