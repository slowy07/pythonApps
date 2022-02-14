import datetime as dt

import matplotlib.pyplot as plt
import pandas_datareader as pd_reader

crypto = "BTC"
currency = "USD"


start_date = dt.datetime(2021, 1, 10)
end_date = dt.datetime.now()

btc = pd_reader.DataReader(f"{crypto}-{currency}", "yahoo", start_date, end_date)
eth = pd_reader.DataReader(f"ETH-{currency}", "yahoo", start_date, end_date)


"""plt.yscale("log")"""
plt.plot(btc["Close"], label="BTC")
plt.plot(eth["Close"], label="ETH")
plt.legend(loc="upper left")
plt.show()

# mpf.plot(btc, type='candle', volume = True, style = 'yahoo')
"""plt.plot(data['Close'])
plt.show()"""
