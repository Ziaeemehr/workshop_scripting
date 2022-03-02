"""
Timeseries plot with error bands
================================

_thumb: .48, .45

"""
import pylab as pl
import seaborn as sns
sns.set(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

print(fmri.head())

# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri, err_style='band')
pl.savefig("errorband.png")
pl.close()