import numpy as np
from scipy.optimize import curve_fit
import pylab as pl 

x = np.arange(0,3,0.1)
y = x*x + np.random.rand(len(x))


def fit_func(x, a, b):
    return a*x*x + b


params = curve_fit(fit_func, x, y)

[a, b] = params[0]

pl.plot(x,y,label='data')
pl.plot(x, fit_func(x, a, b), 
label="fit: ax^2+b, a=%g, b=%g" %(a,b))
pl.legend()
pl.show()