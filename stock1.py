from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from datetime import *
from dateutil.relativedelta import relativedelta
import numpy as np
style.use('ggplot')


# 1a representative major stock indexes:
ticker = {'NASDAQ Composite: Yahoo! ticker': '^IXIC', 'NYSE Composite: Yahoo! ticker': '^NYA',
		  'Dow Jones Industrial Average: Yahoo! ticker': '^DJI', 'S&P 500: Yahoo! ticker': '^GSPC',
		  'Shanghai Composite': '000001.SS', 'Euro STOXX 50: Yahoo! ticker': '^STOXX50E'}

# 1b picks the values and transforms them into a list
ticker_list = (list(ticker.values()))

#2 input individual tickers
new_ticker = input("Input the individual tickers here in all in one line, with comma, & without space")
stockList = (new_ticker.split(',')) #split tickers by comma as a delimiter
print(stockList)


# Combined all tickers into 1 list
all_tickers = ticker_list + stockList
print(all_tickers)



# 3a Take today's date and 24 month old date
end_date = date.today()
start_date = date.today() + relativedelta(months=-24)
print("Start date: {}\nEnd date: {}".format(start_date, end_date))


# Use pandas_reader.data.DataReader to load the desired data.
panel_data = data.DataReader(all_tickers,"yahoo", start_date, end_date)


# The index in this DataFrame is the major index of the panel_data.
adj_close = panel_data.ix['Adj Close']

# Getting all weekdays between start and end dates
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# reindex adj_close using all_weekdays as the new index
adj_close = adj_close.reindex(all_weekdays)

 # fill the missing by replacing them with the latest available price for each instrument.
adj_close = adj_close.fillna(method='ffill')

print(type(adj_close))
adj_close.to_csv('adjclose.csv', sep=' ')

# Calculating the the correlation by generating a time series
# print(adj_close['all_tickers[2]'].corr(adj_close['all_tickers[1]']))



# Creating a correlation matrix of all the stock tickers
correlation_matrix = np.corrcoef(percentage_change_list________)


# Visualize data here usign ggplot
# def visualize_data():
#     DataFrame = pd.read_csv('adjclose.csv')
#     DataFrame['AAPL'].plot()
#     plt.show()
#
# visualize_data()