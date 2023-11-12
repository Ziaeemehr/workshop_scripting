#!/usr/bin/env python

import numpy as np
import time

def sumsquare(n):
    return sum(i*i for i in range(n))

print sumsquare(100), sumsquare(500)



