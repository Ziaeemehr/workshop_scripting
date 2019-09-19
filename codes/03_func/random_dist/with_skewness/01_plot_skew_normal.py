from scipy import linspace
from scipy import pi, sqrt, exp
from scipy.special import erf
import pylab as pl


def pdf(x):
    return 1.0/sqrt(2*pi) * exp(-x**2/2)


def cdf(x):
    return (1 + erf(x/sqrt(2.0))) / 2.0


def skewed_normal_distribution(x, location=0, scale=1, skewness=0):
    t = (x-location) / scale
    return 2.0 / scale * pdf(t) * cdf(skewness*t)
    # You can of course use the scipy.stats.norm versions
    # return 2 * norm.pdf(t) * norm.cdf(a*t)


n = 2**10

location = 0.0
scale = 1.0
skewness = [-5, 0, 5]

x = linspace(-10, 10, n)  # range of values

for i in skewness:
    p = skewed_normal_distribution(x, location, scale, i)
    pl.plot(x, p, label=i)

pl.legend()
pl.savefig("fig.png", dpi=150)
# pl.show()
