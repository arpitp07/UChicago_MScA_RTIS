class WrongSideOrder(Exception):
    pass
    
class book:
    #constructor
    def __init__(self):
        self.buy = []
        self.sell = []
    
    def insert_order(self, order):
        if order['side'] == 'buy':
            self.buy.append(order)
            #store copy instead of reference
            # self.buy.append(order.copy())
            self.buy.sort(key = lambda x:x['price'])
        elif order['side'] == 'sell':
            self.sell.append(order)
            #store copy instead of reference
            # self.sell.append(order.copy())
            self.sell.sort(key = lambda x:x['price'], reverse=True)
        else:
            raise WrongSideOrder('wrong side order')
    
    def __repr__(self):
        ret = "Buy:\n"
        for o in self.buy:
            ret+= str(o)
        ret += '\n Sell: \n'
        for o in self.sell:
            ret+= str(o)
        return ret


b1 = book()

o1 = {'quantity': 10, 'price': 1, 'side': 'buy', 'id': 1}
b1.insert_order(o1)

o2 = {'quantity': 10, 'price': 4, 'side': 'sell', 'id': 2}
b1.insert_order(o2)

try:
    o_err = {'quantity': 10, 'price': 4, 'side': 'blah', 'id': 2}
    b1.insert_order(o_err)
except WrongSideOrder as e:
    print(e)

o3 = {'quantity': 10, 'price': 3, 'side': 'buy', 'id': 3}
b1.insert_order(o3)

o4 = {'quantity': 10, 'price': 2, 'side': 'buy', 'id': 4}
b1.insert_order(o4)


#same order stored thrice with the latest price, as the object points to the same location in memory thrice
o1['price'] = 2
b1.insert_order(o1)

o1['price'] = 3
b1.insert_order(o1)

print(b1.buy)
print(b1.sell)