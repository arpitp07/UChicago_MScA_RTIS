import threading
import math

a = [1]*16
b = [1]*16

flag = threading.Lock()
sum = 0

def dot_product(a, b):
    global sum
    sum_1 = 0
    for i in range(len(a)):
        sum_1+=a[i]*b[i]
    flag.acquire()
    sum+=sum_1
    flag.release()


threads = []
for i in range(4):
    thread = threading.Thread(target=dot_product, args=(a[i*math.floor(len(a)/4):(i+1)*math.floor(len(a)/4)], b[i*math.floor(len(b)/4):(i+1)*math.floor(len(b)/4)]))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(sum)