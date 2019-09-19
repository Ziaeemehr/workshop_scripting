import numpy as np
import pylab as pl
from scipy.stats import skew


def rand_skew_norm(alpha, location, scale):
    sigma = alpha / np.sqrt(1.0 + alpha**2)

    u0, v0 = np.random.randn(2)
    u1 = sigma*u0 + np.sqrt(1.0 - sigma**2) * v0

    if u0 >= 0:
        return u1*scale + location
    return (-u1)*scale + location
# ------------------------------------------------------------------#


def randn_skew(N, alpha=0.0, location=0.0, scale=1.0):
    return [rand_skew_norm(alpha, location, scale) for x in range(N)]
# ------------------------------------------------------------------#


def randn_skew_fast(N, alpha=0.0, loc=0.0, scale=1.0):
    sigma = alpha / np.sqrt(1.0 + alpha**2)
    u0 = np.random.randn(N)
    v = np.random.randn(N)
    u1 = (sigma*u0 + np.sqrt(1.0 - sigma**2)*v) * scale
    u1[u0 < 0] *= -1
    u1 = u1 + loc
    return u1
# ------------------------------------------------------------------#


def skweness_to_alpha(gamma):

    assert(np.abs(gamma) < 0.995217)

    a = np.abs(gamma)**(2.0/3.0)
    denominator = 1.0/(a + (0.5*(4.0 - np.pi))**(2.0/3.0))
    delta = np.sqrt(0.5*np.pi*a*denominator)

    alpha = delta/np.sqrt(1.0-delta*delta)
    if gamma >= 0:
        return alpha
    return -alpha


NUM_SAMPLES = 100000
# skweness is between -0.9952717, -0.9952717
SKEWNESS = [-0.5, 0, 0.5]
ALPHA = [skweness_to_alpha(i) for i in SKEWNESS]

# lets check they at least visually match the PDF:
pl.subplots(figsize=(12, 4))
for i in range(len(ALPHA)):
    p = randn_skew(NUM_SAMPLES, ALPHA[i])
    # p = randn_skew_fast(NUM_SAMPLES, ALPHA[i])
    print "skewness = %g" % skew(p)
    pl.hist(p, bins=100, alpha=0.5, label=str(SKEWNESS[i]), density=True)

pl.title("histogram")
pl.ylabel("probability")
pl.xlabel("value")
pl.legend()
pl.savefig("fig1.png", dpi=150)
# pl.show()
