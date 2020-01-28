'''
https://pandas.pydata.org/pandas-docs/stable/10min.html
'''

import pandas as pd
import numpy as np
import pylab as pl

np.random.seed(123)

# Creating a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# Creating a DataFrame
dates = pd.date_range('20130101', periods=6)

# print dates
df = pd.DataFrame(np.random.randn(6, 4),
                  index=dates,
                  columns=list('ABCD'))
# print df

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

# print df2
# print df2.dtypes
# print df.head()
# print df.tail(3)
# print df.index
# print df.columns
# print df.values
# print df.describe()
# print df.sort_values(by='B')
df["A"] = range(6)
print(df)  # df['A']
# print df.iloc[0]
