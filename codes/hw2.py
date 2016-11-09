#!/usr/bin/env python
import sys, math
ipt = sys.argv
n = len(ipt)

for i in range(n-1):
    r = float(sys.argv[i+1])
    s = math.sin(r)
    print  r, s
    


