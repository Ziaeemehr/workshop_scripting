import numpy as np 

np.random.seed(123) # if you want to set a seed 

N = 20
R = []
for i in range(N):
	while True:
		r = np.random.randint(20)
		if r not in R:
			break
	R.append(r)  # put r in R to avoid use it again	
	print i, r

print len(R)
print np.sort(R)	#print the produced data to be 
					#sure all points in interval 
					#have been chosen once