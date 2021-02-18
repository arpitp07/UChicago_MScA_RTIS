#!/bin/python3

import math
import os
import random
import re
import sys



import numpy as np
import pandas as pd
#
# Complete the 'maximumProfit' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY price as parameter.
#

def maximumProfit(price):
    next_max = max(price)
    holdings = 0
    profit = 0
    for i in range(len(price)):
        if price[i] < next_max:
            profit-=price[i]
            holdings+=1
        else:
            profit+=holdings*price[i]
            holdings = 0
            try:
                next_max = max(price[i+1:])
            except ValueError:
                return profit
    return profit
    # Write your code here  
#     num_shares = 0
#     df = pd.DataFrame()
#     df['price'] = price
#     df['order'] = np.sign(df['price'].diff(-1).fillna(1))
#     count = 0
#     holdings = []
#     for i in df['order']:
#         if i == -1:
#             holdings.append(1)
#             count+=1
#         elif i == 1:
#             holdings.append(count)
#             count = 0
#         else:
#             holdings.append(count)
#             pass
#     df['holdings'] = holdings
#     df['total'] = df['price'].multiply(df['order'], axis = 0).multiply(df['holdings'], axis = 0)
#     print( sum(df['total']))

print(maximumProfit([3, 4, 5, 5, 5, 6, 2]))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         price = list(map(int, input().rstrip().split()))

#         profit = maximumProfit(price)

#         fptr.write(str(profit) + '\n')

#     fptr.close()
