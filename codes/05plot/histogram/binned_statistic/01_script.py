import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(0, 5, num=500)
x_pdf = stats.maxwell.pdf(x)
samples = stats.maxwell.rvs(size=10000)

bin_means, bin_edges, binnumber = stats.binned_statistic(
    x, x_pdf,
    statistic='mean',
    bins=25)
# print(len(binnumber))
bin_std, bin_edges, binnumber = stats.binned_statistic(
    x, x_pdf,
    statistic='std',
    bins=25)

bin_width = (bin_edges[1] - bin_edges[0])
bin_centers = bin_edges[1:] - bin_width / 2


plt.figure()
# plt.hist(samples, bins=50, density=True, histtype='stepfilled',
#          alpha=0.2, label='histogram of data')
plt.plot(x, x_pdf, 'r-', label='analytical pdf')
# plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:], colors='g', lw=2,
#            label='binned statistic of data')
# plt.plot((binnumber - 0.5) * bin_width, x_pdf, 'g.', alpha=0.5)
plt.errorbar(bin_centers, bin_means , yerr=bin_std, fmt="--")
plt.legend(fontsize=10)
plt.show()
