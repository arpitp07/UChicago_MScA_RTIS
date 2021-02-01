# import threading
# import time

# def f1():
#     for i in range(10):
#         print(f'loop 1 : {i}')
#         time.sleep(1)

# def f2():
#     for i in range(10):
#         print(f'loop 2 : {i}')
#         time.sleep(1)

# # f1()
# # f2()

# t1 = threading.Thread(target=f1)
# t2 = threading.Thread(target=f2)


# t1.start()
# t2.start()
# t1.join()
# t2.join()

# flag = threading.Lock()

# balance = 1500000
# num_times = 10^7

# def deposit(num_times):
#     global balance
#     for i in range(num_times):
#         flag.acquire()
#         balance+=1
#         flag.release()

# def withdraw(num_times):
#     global balance
#     for i in range(num_times):
#         flag.acquire()
#         balance-=1
#         flag.release()

# seb = threading.Thread(target=deposit, args = (num_times,))
# nick = threading.Thread(target=withdraw, args = (num_times,))

# seb.start()
# nick.start()

# seb.join()
# nick.join()

# print(f"balance = {balance}")

import threading
import time
count=0

def f1():
    global count
    for i in range(10000):
        count+=1

def f2():
    global count
    for i in range(10000):
        count+=1


Yue=threading.Thread(target=f1)
Arpit=threading.Thread(target=f2)
Yue.start()
Arpit.start()
Yue.join()
Arpit.join()
# # f1()
# f2()
print("result:",count)

# import threading

# balance=0
# nb_of_operations=1000000

# flag=threading.Lock()

# def deposit(nb_times):
#     global balance
#     for i in range(nb_times):
#         flag.acquire()  # raise the flag
#         balance+=1
#         flag.release() # remove the flag

# def withdraw(nb_times):
#     global balance
#     for i in range(nb_times):
#         flag.acquire()  # raise the flag
#         balance-=1
#         flag.release() # remove the flag


# seb=threading.Thread(target=deposit,args=(nb_of_operations,))
# nic=threading.Thread(target=withdraw,args=(nb_of_operations,))
# seb.start()
# nic.start()
# seb.join()
# nic.join()
# print("balance:",balance)


balance=0
nb_of_operations=1000000

flag=threading.Lock()

def deposit(nb_times):
    global balance
    balance1=0
    for i in range(nb_times):
        balance1+=1
    flag.acquire()
    balance+=balance1
    flag.release()

def withdraw(nb_times):
    global balance
    balance2=0
    for i in range(nb_times):
        balance2-=1
    flag.acquire()
    balance+=balance2
    flag.release()

seb=threading.Thread(target=deposit,args=(nb_of_operations,))
nic=threading.Thread(target=withdraw,args=(nb_of_operations,))
seb.start()
nic.start()
seb.join()
nic.join()
print("balance:",balance)