import patsy
import numpy as np
import pylab as pl
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg

np.random.seed(145)

x = np.arange(0, 10, 0.1)
y = 5 * np.random.rand(len(x)) + x

pl.scatter(x, y, s=10)


data = {"y": y, "x": x}
df_data = pd.DataFrame(data)

# use ordinary least squares (ols)
model = smf.ols("y ~ x", df_data)
# 
result = model.fit()
print(result.params)
pl.plot(x, result.fittedvalues, lw=2, c="k",
        label="y=ax+b, a=%.3f, b=%.3f" % (result.params["x"],
                                          result.params["Intercept"]))
pl.legend()
pl.xlabel("x", fontsize=14)
pl.ylabel("y", fontsize=14)
pl.savefig("example.png")
# pl.show()


X = np.vstack([np.ones(len(x)), x]).T
beta, res, rank, sval = np.linalg.lstsq(X, y, rcond=None)
print(beta)
