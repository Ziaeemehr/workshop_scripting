import patsy
import numpy as np
import pylab as pl
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg

np.random.seed(4582)

N = 1000
x1 = np.random.randn(N)
x2 = np.random.randn(N)
data = pd.DataFrame({"x1": x1, "x2": x2})
data["y_true"] = 1 + 2 * x1 + 3 * x2 + 4 * x1 * x2

e = 0.5 * np.random.randn(N)
data["y"] = data["y_true"] + e

model = smf.ols("y ~ x1 + x2", data=data)
result = model.fit()

# print(result.summary())
# print(result.rsquared)
# print(result.resid.head())
z, p = stats.normaltest(result.fittedvalues.values)
# print(p)

fig, ax = pl.subplots(1, figsize=(6, 5))
smg.qqplot(result.resid, ax=ax)
pl.show()