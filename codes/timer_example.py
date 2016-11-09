from timeit import default_timer as timer

a = ['Hello', 'Jello', 'Hello', 'Hello']

start = timer()
b = [1 if x == 'Hello' else 0 for x in a]
end = timer()
print('without cast: {}'.format(end - start))

start = timer()
b = [int(x == 'Hello') for x in a]
end = timer()
print('with cast   : {}'.format(end - start))