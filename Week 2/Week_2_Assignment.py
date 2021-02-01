#!/bin/python3

import math
import os
import random
import re
import sys

temp_bank_account = 0
seb_bank_account = 0
nic_bank_account = 0
current_thread = ""
seb_thread_acq = False
nic_thread_acq = False

class lock():
    def __init__(self):
        self.lock_flag = False
        self.thread_acq = ""
    def acquire(self):
        global current_thread
        if self.lock_flag == False:
            self.lock_flag = True
            self.thread_acq = current_thread
        else:
            return "Locked"
    def release(self):
        self.lock_flag = False
        self.thread_acq = ""

# The class lock() contains the methods acquire() and release()

bank_account = 0
var_lock = lock()

def transaction(seb, nic):
    
    # In this function you need to complete the code using some of the threading functions
    # provided above. Assume that the loop continues running (thread continues running) until
    # both Seb and Nic has completed their prearranged number of transactions
    #
    # In order to make the following function work you need to implement thread controls using
    # the lock class implemented above (var_lock)
    #
    # Think about when each global variable is being used and how to handle multiple threads
    # trying to access the global variable at the same time
    #
    # Try to describe what you think each line of the following code does in a live threading
    # environment
    
    global bank_account
    global seb_thread_acq
    global nic_thread_acq
    global var_lock
    global current_thread
    
    seb_runs = seb
    nic_runs = nic
    
    while seb_runs > 0 or nic_runs > 0:
        
        current_thread = run_thread(seb_runs, nic_runs)

        var_status = thread_acquire_var(current_thread)
                
        if var_status == "Locked":
            continue
        
        if current_thread == "Seb":
            if seb_thread_acq == False:
                var_lock.acquire()
                seb_runs += seb_thread()
                seb_thread_acq = True
                continue
            else:
                update_thread()
                var_lock.release()
                seb_thread_acq = False
                seb_runs -= 1
        else:
            if nic_thread_acq == False:
                var_lock.acquire()
                nic_runs += nic_thread()
                nic_thread_acq = True
                continue
            else:
                update_thread()
                var_lock.release()
                nic_thread_acq = False
                nic_runs -= 1
    
    return bank_account

def seb_thread():
    global var_lock
    global temp_bank_account
    global bank_account
    if not var_lock.lock_flag or (var_lock.lock_flag and var_lock.thread_acq == "Seb"):
        temp_bank_account = seb_bank_account + 1
        return 0
    else:
        return 1


def nic_thread():
    global var_lock
    global temp_bank_account
    global bank_account
    if not var_lock.lock_flag or (var_lock.lock_flag and var_lock.thread_acq == "Nic"):
        temp_bank_account = nic_bank_account - 1
        return 0
    else:
        return 1


def update_thread():
    global bank_account
    global temp_bank_account
    bank_account = temp_bank_account


def thread_acquire_var(user):
    global seb_bank_account
    global nic_bank_account
    global bank_account
    global var_lock
    if user == "Seb":
        if (var_lock.lock_flag and var_lock.thread_acq == "Seb") or not var_lock.lock_flag:
            seb_bank_account = bank_account
            return "Seb"
        else:
            return "Locked"
    else:
        if (var_lock.lock_flag and var_lock.thread_acq == "Nic") or not var_lock.lock_flag:
            nic_bank_account = bank_account
            return "Nic"
        else:
            return "Locked"


def run_thread(seb_runs, nic_runs):
    if seb_runs == 0:
        return "Nic"
    if nic_runs == 0:
        return "Seb"
    rnd = random.random()
    if rnd > 0.5:
        return "Seb"
    else:
        return "Nic"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    seb = 2

    nic = 2

    result = transaction(seb, nic)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()