import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader.data as web
import datetime
import mpl_finance
import matplotlib.ticker as ticker
# import matplotlib.mplfinance as matfin

# 1
# plt.plot([1, 2, 3, 4])
# plt.show()

# x = range(0, 100)
# y = [v*v for v in x]
# plt.plot(x, y, 'g+')
# plt.show()

# 2
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(2, 1, 2)

# x = range(0, 100)
# y = [v*v for v in x]

# ax1.plot(x, y)
# ax2.bar(x, y)

# plt.show()

# 3
# x = np.arange(0.0, 2*np.pi, 0.1)
# sin_y = np.sin(x)
# cos_y = np.cos(x)

# fig = plt.figure()
# ax1 = fig.add_subplot(211)
# ax2 = fig.add_subplot(212)

# ax1.plot(x, sin_y, 'b--')
# ax2.plot(x, cos_y, 'r--')

# ax1.set_xlabel('x')
# ax1.set_ylabel('sin(x)')

# ax2.set_xlabel('x')
# ax2.set_ylabel('cos(x)')

# plt.show()

# 4
# lg = web.DataReader("066570.KS", "yahoo")
# samsung = web.DataReader("0059030.KS", "yahoo")

# plt.plot(lg.index, lg['Adj Close'], label="LG Electronics")
# plt.plot(samsung.index, samsung['Adj Close'], label="Samsung Electronics")

# plt.legend(loc='upper left')
# plt.show()

# 5
# fig, ax_list = plt.subplots(2, 2)

# ax_list[0][0].plot([1, 2, 3, 4])
# plt.show()

# 6
# sk_hynix = web.DataReader("000660.KS", "yahoo")

# fig = plt.figure(figsize=(12, 8))

# top_axes = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
# bottom_axes = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)
# bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)

# top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label='Adjusted Close')
# bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])

# plt.tight_layout()
# plt.show()

# 7
start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 31)
skhynix = web.DataReader("000660.KS", "yahoo", start, end)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# day_list = range(len(skhynix))
day_list = []
name_list = []

for i, day in enumerate(skhynix.index):
    if day.dayofweek == 0:
        day_list.append(i)
        name_list.append(day.strftime('%Y-%m-%d')+'(Mon)')

# for day in skhynix.index:
#     name_list.append(day.strftime('%d'))

ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))


mpl_finance.candlestick2_ohlc(ax, skhynix['Open'], skhynix['High'],
                              skhynix['Low'], skhynix['Close'], width=0.5, colorup='r', colordown='b')

plt.grid()
plt.show()
