#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque



#
# Complete the 'TradingStrategy' class below.
#
#



# Python program to get average of a list
def average(lst):
    return sum(lst) / len(lst)

class TradingStrategy:
    def __init__(self):
        self.small_window=deque()
        self.large_window=deque()
        self.long_signal=False
        self.position=0
        self.cash=10000
        self.total=0
        self.holdings=0
        
    def onPriceUpdate(self,price_update):
        # you should store 50 close prices for the small window
        # you should store 100 close prices for the large window
        # when the number of close prices is higher than 50, you need to discard the older one (small window)
        # when the number of close prices is higher than 100, you need to discard the older one (large window)
        # you compare the small window vs the large window
        # if small window > large window generate long signal
        # if not long signal = false
        # Call the function checkSignal
        self.small_window.append(price_update['close'])
        # print(average(self.small_window))
        if len(self.small_window)>50:self.small_window.popleft()
        
        self.large_window.append(price_update['close'])
        if len(self.large_window)>100:self.large_window.popleft()
        
        if average(self.small_window)>average(self.large_window):
            self.long_signal = True
        elif (average(self.small_window)<=average(self.large_window)) & (len(self.large_window)>=100):
            self.long_signal = False
        
        if len(self.small_window)==50:
            self.checkSignal(price_update)

    def checkSignal(self,price_update):
        # if there is a long signal and the position is 0 
        # you should send an order
        # for that you will use print, you will display the timestamp and write that you send a buy order
        #     example:
        #     print(price_update['date'] +
        #          " send buy order for 10 shares price=" + str(price_update['adjprice']))
        # You need to update the position
        # You need to update the cash
        if (self.long_signal) & (self.position==0):
            print(price_update['date'] + " send buy order for 10 shares price=" + str(price_update['adjprice']))
            self.position = 1
            self.cash -= 10*price_update['adjprice']
        
        
        if (self.long_signal==False) & (self.position!=0):
            print(price_update['date']+ " send sell order for 10 shares price=" + str(price_update['adjprice']))
            self.position = 0
            self.cash += 10*price_update['adjprice']
        # Now if the position is positive and there is no long signal any more
        # You need to send a sell order
        #    print(price_update['date']+
        #          " send sell order for 10 shares price=" + str(price_update['adjprice']))
        # You need to update the position
        # You need to update the cash
        
        # For each iteration, you need to manage holdings
        # For each iteration, you need to know how much in total you have (total=holdings + cash)
        # You need to display the following for each iteration
        
        self.holdings = self.position*10*price_update['adjprice']
        self.total = self.holdings + self.cash
        # if price_update['date'] == '2001-08-23':
        #     print(average(self.small_window)<=average(self.large_window))
        #     print(self.long_signal)
        #     print('%s total=%d, holding=%d, cash=%d' %
        #       (price_update['date'],self.total, self.holdings, self.cash))
        
        print('%s total=%d, holding=%d, cash=%d' %
            (price_update['date'],self.total, self.holdings, self.cash))


if __name__ == '__main__':
    
    ts=TradingStrategy()
    nb_of_rows = int(input().strip())
    market_data_header = input().strip()

    for _ in range(nb_of_rows):
        row = input().strip().split(',')
        ts.onPriceUpdate({'date' : row[0],
                            'close' : float(row[4]),
                            'adjprice' : float(row[6])})
