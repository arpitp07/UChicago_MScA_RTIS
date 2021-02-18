# import pandas_datareader as pdr
# import pandas as pd
# from matplotlib import pyplot as plt
# import numpy as np
# import math

# start_date = '2006-01-01'
# end_date = '2021-02-11'

# # GME = pdr.get_data_yahoo('GME', start=start_date, end=end_date)

# try:
#     GME = pd.read_pickle('gme.pkl')
# except :
#     GME.to_pickle('gme.pkl')

# GME.describe()
# GME['Adj Close'].pct_change()
# GME['Adj Close'].resample('M').mean()
# GME['20_day_avg'] = GME['Adj Close'].rolling(20).mean()
# GME['100_day_avg'] = GME['Adj Close'].rolling(100).mean()

# GME['pos'] = np.where(GME['20_day_avg'] > GME['100_day_avg'], 1, 0)
# GME['order'] = GME['pos'].diff()
# GME[(GME['order']==1)]
# GME[(GME['order']==-1)]

# # fig = plt.figure()
# # ax1 = fig.add_subplot(111, ylabel='Price ($)')
# # ax1()

# orders = GME[['Adj Close', 'order']]
# orders['timestamp'] = GME.index
# orders['cash'] = 1000

# for i in range(len(orders)):
#     # try:
#     orders.loc([i], ['cash']) = np.where(orders[i, 'order'] == 0, orders[i-1, 'cash'], np.where(orders[i, 'order'] == 1, orders[i-1, 'cash'] - orders[i, 'Adj Close'], orders[i-1, 'cash'] + orders[i, 'Adj Close']))

# # orders['cash'] = np.where(orders['order'] == 1, orders['Adj Close'])

import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Gamestop: GME
start_date = "2006-01-01"
end_date = "2021-02-11"

gme = pdr.get_data_yahoo("GME",start = start_date,end = end_date)

try:
    gme=pd.read_pickle('gme.pkl') ## read the file gme.pkl
except:
    gme.to_pickle('gme.pkl') ## store this dataframe into a pkl file if this file doesn't exist


signals=pd.DataFrame(index=gme.index)
signals['price']=gme['Adj Close']
signals['small']=signals['price'].rolling(20).mean()
signals['long']=signals['price'].rolling(100).mean()
signals['position']=np.where(signals['small']>signals['long'],1.0,0.0)
signals['order']=signals['position'].diff()

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
signals['price'].plot(ax=ax1, color='r', lw=2)
ax1.plot(signals.loc[signals.order == 1.0].index,
        signals.price[signals.order == 1.0], '^', markersize = 10,
        color='m')

ax1.plot(signals.loc[signals.order == -1.0].index,
        signals.price[signals.order == -1.0], 'v', markersize = 10,
        color='k')

plt.show()

initial_capital = 10000
number_of_shares = 10
positions=pd.DataFrame(index=signals.index).fillna(0.0)
positions['gme'] = number_of_shares*signals['position']

pfl = positions.multiply(signals['price'], axis = 0)

pos_diff = signals['order']
pfl['holdings']=(positions.multiply(signals['price'], axis=0))
pfl['cash'] = initial_capital - (pos_diff.multiply(signals['price']*number_of_shares,axis =0)).cumsum()

pfl['total']=pfl['holdings']+pfl['cash']

pfl['total'].plot()
plt.show()
