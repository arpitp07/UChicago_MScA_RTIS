#!/bin/python3

import math
import os
import random
import re
import sys
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#
# Complete the 'case1' function below.
#
# The function accepts STRING_ARRAY fp_data as parameter.
#

def case1(financial_data):
    # Print First 5 rows of MSFT
    # Print Last 5 rows of MSFT
    # Print Describe MSFT
    print(financial_data.head(5))
    print(financial_data.tail(5))
    print(financial_data.describe())

def case2(financial_data):
    #Resample to monthly data
    #Display the first 5 rows
    print(financial_data.resample('M').mean().head(5))


def case3_decorator(fn):
    def wrapper(data):
        d = fn(data)
        print(d.pct_change().dropna())
    wrapper.unwrapped = fn
    return wrapper

@case3_decorator
def case3(financial_data):
    # Create a variable daily_close and copy Adj Close from financial_data
    # Print daily returns
    daily_close = pd.DataFrame(data=financial_data['Adj Close'].values,
                                columns=['Adj Close'],
                                index = financial_data.index)
    # print(daily_close.pct_change().dropna())
    return daily_close


def case4(financial_data):
    # Calculate the cumulative daily returns
    # Print it
    daily_close = case3.unwrapped(financial_data)
    print(((daily_close - daily_close.iloc[0,:])/daily_close.iloc[0,:]).iloc[1:,:]+1)

def case5(financial_data):
    # Resample the cumulative daily return to cumulative monthly return
    daily_close = case3.unwrapped(financial_data)
    print((((daily_close - daily_close.iloc[0,:])/daily_close.iloc[0,:]).iloc[1:,:]+1).resample('M').mean())

def case6(financial_data):
    # Isolate the adjusted closing prices and store it in a variable
    # Calculate the moving average for a window of 20
    # Display the last 20 moving average number
    daily_close = case3.unwrapped(financial_data)
    print(daily_close.rolling(20).mean())


def case7(financial_data):
    # Calculate the volatility for a period of 100 don't forget to multiply by square root
    # don't forget that you need to use pct_change
    daily_close = case3.unwrapped(financial_data)
    print(daily_close.pct_change().rolling(100).std()*math.sqrt(100))

def case8_decorator(fn):
    def wrapper(data):
        d = fn(data)
        print(d)
    wrapper.unwrapped = fn
    return wrapper

@case8_decorator
def case8(financial_data):
    # Initialize the short rolling window (window=50)
    # Initialize the long rolling window (window=100)
    window_short = 50
    window_long = 100
    
    # You will create a signals dataframe
    # using the index of financial_data
    signals = pd.DataFrame(index=financial_data.index)
    
    # You will assign 0 to the column signal of the dataframe signals
    signals['signal'] = 0
    # Create short simple moving average over the short window  
    signals['short_mavg'] = financial_data['Close'].rolling(window_short).mean().fillna(financial_data['Close'].expanding().mean())
    # Create long simple moving average over the long window
    signals['long_mavg'] = financial_data['Close'].rolling(window_long).mean().fillna(financial_data['Close'].expanding().mean())
    
    # You will not populate the value 1 when the small window moving average
    # is higher than the long window moving average else 0
    signals['signal']=np.where(signals['short_mavg']>signals['long_mavg'],1.0,0.0)
    
    
    # Generate trading orders by inserting in a new column orders
    # 1 if it is a buy order -1 if it is a sell order
    # you should just use the diff command on the column signal
    signals['orders']=signals['signal'].diff()
    
    # Print the dataframe signals
    return signals
    
    


def case9(financial_data):
    # You will need to use the dataframe signals
    signals = case8.unwrapped(financial_data)
    

    # You are going to set your initial amount of money you want
    # to invest --- here it is 10,000
    budget = 10000
    number_of_shares = 10
    
    # You are going to create a new dataframe positions
    # Remember the index is still the same as signals
    position = pd.DataFrame(index = signals.index)
    
    # You are going to buy 10 shares of MSFT when signal is 1
    # You are going to sell 10 shares of MSFT when signal is -1
    # You will assign these values to the column MSFT of the
    # dataframe positions
    position['MSFT'] = (signals['signal']*financial_data['Adj Close']*number_of_shares).fillna(0)
    position['holdings'] = position['MSFT']
    position['cash'] = (budget - financial_data['Adj Close'].multiply(signals['orders']*number_of_shares, axis = 0).cumsum()).fillna(budget)
    position['total'] = position['holdings'] + position['cash']
    position['returns'] = position['total'].pct_change()
    # You are now going to calculate the notional (quantity x price)
    # for your portfolio. You will multiply Adj Close from
    # the dataframe containing prices and the positions (10 shares)
    # You will store it into the variable portfolio
    
    
    # Add `holdings` to portfolio
    
    
    # You will store positions.diff into pos_diff
    
    # You will now add a column cash in your dataframe portfolio
    # which will calculate the amount of cash you have
    # initial_capital - (the notional you use for your different buy/sell)
    
    
    # You will now add a column total to your portfolio calculating the part of holding
    # and the part of cash
    
    
    # Add `returns` to portfolio
    
    
    # Print the first lines of `portfolio`
    print(position)

    

if __name__ == '__main__':