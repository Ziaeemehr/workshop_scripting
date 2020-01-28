import patsy
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg

### from least square fitting
y = np.array([1, 2, 3, 4, 5])
x1 = np.array([6, 7, 8, 9, 10])
x2 = np.array([11, 12, 13, 14, 15])

X = np.vstack([np.ones(5), x1, x2, x1 * x2]).T
# print(X)
beta, res, rank, sval = np.linalg.lstsq(X, y, rcond=None)
# print (beta)
# [-5.55555556e-01  1.88888889e+00 -8.88888889e-01 -1.11022302e-15]


### DesignMatrix: to create a dictionary data that maps the variable
# names to the corresponding data arrays
data = {"y": y, "x1": x1, "x2": x2}
y, X = patsy.dmatrices("y ~ 1 + x1 + x2 + x1 * x2", data)
# print (X)

### DesignMatrix from data frame
df_data = pd.DataFrame(data)
y, X = patsy.dmatrices("y ~ 1 + x1 + x2 + x1:x2", df_data, return_type="dataframe")
# print(X)


# ordinary linear regression (OLS)
# we can use the class OLS from the statsmodels library instead of
# using the lower-level method np.linalg.lstsq
model = sm.OLS(y, X)
result = model.fit()
# print(result.params)
# Intercept   -5.555556e-01
# x1           1.888889e+00
# x2          -8.888889e-01
# x1:x2       -7.771561e-16
# dtype: float64
# print(result.params["x1:x2"])

# we can directly pass the Patsy formula for the model when we create
# a model instance, which completely eliminates the need for first
# creating the design matrices
model = smf.ols("y ~ 1 + x1 + x2 + x1:x2", df_data)
result = model.fit()
# print(result.params)
# Intercept   -5.555556e-01
# x1           1.888889e+00
# x2          -8.888889e-01
# x1:x2       -7.771561e-16
# dtype: float64

from collections import defaultdict
data = defaultdict(lambda: np.array([]))
print(patsy.dmatrices("y ~ a", data=data)[1].design_info.term_names)
# ['Intercept', 'a']
print(patsy.dmatrices("y ~ 1 + a + b", data=data)[1].design_info.term_names)
# ['Intercept', 'a', 'b']
print(patsy.dmatrices("y ~ -1 + a + b", data=data)[1].design_info.term_names)
# ['a', 'b']
print(patsy.dmatrices("y ~ a * b", data=data)[1].design_info.term_names)
# ['Intercept', 'a', 'b', 'a:b']
print(patsy.dmatrices("y ~ a * b * c", data=data)[1].design_info.term_names)
# ['Intercept', 'a', 'b', 'a:b', 'c', 'a:c', 'b:c', 'a:b:c']
print(patsy.dmatrices("y ~ a * b * c - a:b:c", data=data)[1].design_info.term_names)
# ['Intercept', 'a', 'b', 'a:b', 'c', 'a:c', 'b:c']





