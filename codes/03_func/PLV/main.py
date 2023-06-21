import time
from numba import jit
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
from scipy.signal import hilbert


np.random.seed(2)

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time elapsed: ", end - start)
        return result
    return wrapper

@timer
def compute_plv(x):
    ''' 
    compute phase locking value (PLV) from time series

    Parameters
    ----------
    x: 2d array
        time series of shape (n_channels, n_time)

    '''
    n = x.shape[0]
    plv = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1, n):
            phi1 = instant_phase(x[i, :])
            phi2 = instant_phase(x[j, :])
            plv[i, j] = plv[j, i] = phase_locking_value(phi1, phi2)
    return plv

def instant_phase(x):
    '''
    compute instantaneous phase from time series
    '''

    return np.unwrap(np.angle(hilbert(x)))

def phase_locking_value(theta1, theta2):
    '''
    compute phase locking value (PLV) from two time series

    Parameters
    ----------
    theta1: 1d array
        time series
    theta2: 1d array
        time series

    Returns
    -------
    plv: float
        phase locking value
    '''
    dtheta = theta1 - theta2
    complex_phase_diff = np.exp(1j*(dtheta))
    _plv = np.abs(np.sum(complex_phase_diff))/len(theta1)
    return _plv




# n = len(x)
#     cor = np.zeros((n, n))

#     for i in range(n):
#         for j in range(i, n):
#             cor[j, i] = cor[i, j] = np.cos(x[j] - x[i])

#     cor = cor + np.diag(np.ones(n))

#     return cor


@jit
def Kuramoto_corr(x):

    n = len(x)
    cor = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1, n):
            cor[i, j] = np.cos(x[i] - x[j])

    return cor

@timer
@jit(forceobj=True)
def kuramoto_correlation_avg(x, decimate=10):

    nn, nt = x.shape
    cor = np.zeros((nn, nn))
    indices = np.arange(0, nt, decimate, dtype=int)

    for it in indices:
        x0 = x[:, it]
        cor += Kuramoto_corr(x0)
    cor = cor + cor.T
    cor = cor/len(indices)
    cor = cor + np.diag(np.ones(nn))

    return cor


def phase_lag_index(theta1, theta2, kind=0):

    phase_diff = theta1 - theta2
    phase_diff = (phase_diff + np.pi) % (2 * np.pi) - np.pi
    return abs(np.mean(np.sign(phase_diff)))


def compute_pli(x):
    ''' 
    compute phase lag index (PLI) from time series

    Parameters
    ----------
    x: 2d array
        time series of shape (n_channels, n_time)

    '''
    n = x.shape[0]
    pli = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1, n):
            phi1 = instant_phase(x[i, :])
            phi2 = instant_phase(x[j, :])
            pli[i, j] = pli[j, i] = phase_lag_index(phi1, phi2)

    return pli


def carpet_plot(t, ts, ax, ylabel='Region', fontsize=14, **kwargs):
    '''
    plot carpet plot

    parameters
    ----------
    t: np.ndarray [n_samples]
        time vector
    ts: np.ndarray [n_channels, n_samples]
        signal to plot

    '''
    nn = ts.shape[0]
    ax.plot(t, ts.T/np.max(ts)*2 + np.r_[:nn], **kwargs)
    ax.set_yticks(np.r_[::10])
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_xlabel("Time [s]", fontsize=fontsize)
    ax.set_yticks(np.arange(0, nn, 10))
    ax.margins(x=0, y=0)

def indep_roll(arr, shifts, axis=1):
    """Apply an independent roll for each dimensions of a single axis.

    Parameters
    ----------
    arr : np.ndarray
        Array of any shape.

    shifts : np.ndarray
        How many shifting to use for each dimension. Shape: `(arr.shape[axis],)`.

    axis : int
        Axis along which elements are shifted. 
    """
    arr = np.swapaxes(arr,axis,-1)
    all_idcs = np.ogrid[[slice(0,n) for n in arr.shape]]

    # Convert to a positive shift
    shifts[shifts < 0] += arr.shape[-1] 
    all_idcs[-1] = all_idcs[-1] - shifts[:, np.newaxis]

    result = arr[tuple(all_idcs)]
    arr = np.swapaxes(result,-1,axis)
    return arr


# x = np.arange(25).reshape(5, 5)
# print(x)

# shifts = np.array([1, 2, 3, 4, 5])
# print(indep_roll(x, shifts, axis=1))

# exit(0)

nn = 20
t = np.arange(0, 10, 0.01)
x = np.sin(2*np.pi*t) + np.random.randn(nn, len(t))*0.1
x = indep_roll(x, np.arange(0,nn, dtype=int), axis=1)

# x = np.tile(x, (nn, 1))
# x += np.random.normal(0, 0.1, x.shape)
# x = np.random.normal(0,1, size=(nn, len(t)))
# x = np.ones((nn, len(t)))


plv = compute_plv(x)
pli = compute_pli(x)

km = kuramoto_correlation_avg(x, 10)
km = kuramoto_correlation_avg(x, 10)


fig, ax = plt.subplots(1, 4, figsize=(20, 5))
carpet_plot(t[::10], x[:5, ::10], ax[0], ylabel='Region',
            fontsize=14, color='k', alpha=0.5)
ax[1].imshow(plv, cmap='jet', aspect='auto')
ax[2].imshow(pli, cmap='jet', aspect='auto')
ax[3].imshow(km, cmap='jet', aspect='auto')
# add colorbar
plt.colorbar(ax=ax[1], mappable=ax[1].images[0])
plt.colorbar(ax=ax[2], mappable=ax[2].images[0])
plt.colorbar(ax=ax[3], mappable=ax[3].images[0])
ax[0].set_title('Time series')
ax[1].set_title('PLV')
ax[2].set_title('PLI')
ax[3].set_title("KM")
plt.savefig('plv_pli.png')
# plt.show()