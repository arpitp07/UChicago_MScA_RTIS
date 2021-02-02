class last_que():
    def __init__(self, data):
        self.data = data
    
    def zscore(self):
        self.data = [(x - sum(self.data) / len(self.data)) / std(self.data) for x in self.data]
                
    def moving_avg(self):
        i = 0
        sum_list = []
        for i in range(len(self.data)-n):
            return sum_list.append(sum(self.data[i:i+n])/n)
            i += 1
    
    def cumu_sum(self):
        total = 0
        for x in self.data:
            total += x
            return total
                
    def std(self):
        return sqrt(avg([(x - avg(self.data))**2 for x in self.data]))
    
    def tup(self):
        return (min(self.data), max(self.data))
    
    def avg(self):
        return sum(self.data) / len(self.data)
    
    def median(self):
        if len(self.data)%2 == 0:
            median1 = self.data[n//2] 
            median2 = self.data[n//2 - 1] 
            return (median1 + median2)/2
        else: 
            return self.data[n//2]