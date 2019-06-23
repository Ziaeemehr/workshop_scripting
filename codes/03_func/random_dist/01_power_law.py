import powerlaw
import numpy as np
import pylab as pl
from numpy import power
from numpy import pi, exp
from powerlaw import plot_pdf, Fit, pdf

#--------------------------------------------------------------#


def generate_power_law_dist(N, e, xmin, xmax):
    '''
    generate a power law distribution of floats 
    parameters :
        N: number of data in powerlaw distribution (pwd).
        e: exponent of the pwd.
        xmin: min value in pwd.
        xmax: max value in pwd.
    '''

    from numpy.random import rand, randint

    data = np.zeros(N)
    x0p = power(xmin, (e+1.0))
    x1p = power(xmax, (e+1.0))
    alpha = 1.0/(e+1.0)

    for i in range(N):
        r = rand()
        data[i] = (power((x1p - x0p)*r + x0p, alpha))
    return data
#--------------------------------------------------------------#


def plot_distribution(x, exp, ax):

    fit = powerlaw.Fit(x, discrete=True)  # xmin=xmin
    ax = fit.plot_pdf(linewidth=2, label=str('%.2f' % exp))
    fit.power_law.plot_pdf(c='k', linestyle='--', lw=2, ax=ax)

    ax.set_ylabel("Probability P(k)", fontsize=16)
    ax.set_xlabel("k", fontsize=16)
    ax.legend(frameon=False, loc='best')
#--------------------------------------------------------------#


x = generate_power_law_dist(100000, -3, 5, 10000)
print x
print "%.5f" % np.min(x)
print "%.5f" % np.max(x)
fig, ax = pl.subplots(1)
plot_distribution(x, -3, ax)
pl.savefig('f')
