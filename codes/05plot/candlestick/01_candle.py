import numpy as numpy
import pylab as pl
import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc


# datetime: We will use this one to define our desired time span
# matplotlib.dates: This library will convert our dates into the necessary number format
# pandas_datareader: The module that will load the desired stock data
# candlestick_ohlc from mpl_finance: Our main library for plotting

start = dt.datetime(2010, 1, 1)
end = dt.datetime.now()

df = web.DataReader("AAPL", "yahoo", start, end)
print(df.head())
df = df[['Open', 'High', 'Low', 'Close']]

# Our date doesn’t have the right format and since it is the index,
# we cannot manipulate it. Therefore, we need to reset the index and
# then convert our datetime to a number.

df.reset_index(inplace=True)
df['Date'] = df['Date'].map(mdates.date2num)

ax = plt.subplot()
candlestick_ohlc(ax, df.values, width=5, colorup='g', colordown='r')
ax.xaxis_date()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('AAPL Share Price')  # , color='white')
# ax.set_facecolor('black')
# ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x')  # , colors='white')
ax.tick_params(axis='y')  # , colors='white')
ax.xaxis_date()
plt.show()
