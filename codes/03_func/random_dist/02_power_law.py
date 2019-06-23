import powerlaw
import matplotlib
import numpy as np
import matplotlib.pyplot as pl
from sys import exit


def generate_power_law_dist_bounded(N, e, xmin, xmax):
    '''
    generate a power law distribution of floats 
    parameters :
        N: number of data in powerlaw distribution (pwd).
        e: exponent of the pwd.
        xmin: min value in pwd.
        xmax: max value in pwd.
    '''

    from numpy.random import rand, randint
    from numpy import power

    data = np.zeros(N)
    x0p = power(xmin, (e+1.0))
    x1p = power(xmax, (e+1.0))
    alpha = 1.0/(e+1.0)

    for i in range(N):
        r = rand()
        data[i] = (power((x1p - x0p)*r + x0p, alpha))
    return data
#--------------------------------------------------------------#


def generate_power_law_dist(N, a, xmin):
    '''
    generate power law random numbers p(k) ~ x^(-a) for a>1
    N is the number of random numbers
    a is the exponent
    xmin is the minimum value of distribution
    '''
    import powerlaw
    # generates random variates of power law distribution
    vrs = powerlaw.Power_Law(xmin=xmin, parameters=[a]).generate_random(N)

    return vrs
#--------------------------------------------------------------#


def plot_distribution(vrs, N, a, xmin):

    # plotting the PDF estimated from variates
    bin_min, bin_max = np.min(vrs), np.max(vrs)
    bins = 10**(np.linspace(np.log10(bin_min), np.log10(bin_max), 100))
    counts, edges = np.histogram(vrs, bins, density=True)
    centers = (edges[1:] + edges[:-1])/2.

    # plotting the expected PDF
    xs = np.linspace(bin_min, bin_max, N)
    pl.plot(xs, [(a-1)*xmin**(a-1)*x**(-a) for x in xs], color='red')
    pl.plot(centers, counts, '.')
    pl.xscale('log')
    pl.yscale('log')

    pl.savefig('powerlaw_variates.png')
#--------------------------------------------------------------#

N = 1000
a = 6.0
xmin = 5
xmax = 10000

fig, ax = pl.subplots(1)
vrs = generate_power_law_dist_bounded(N, -a, xmin, xmax)
# vrs = vrs/np.max(vrs)
print np.min(vrs), np.max(vrs)
plot_distribution(vrs, N, a, xmin)


vrs = vrs*2.0-1.0
print len(vrs[vrs>0])

np.savetxt("vrs.txt", np.sort(vrs/np.max(vrs)*2.0 - 1.0), fmt="%.6f")
#--------------------------------------------------------------#
