#!/bin/python3

import math
import os
import random
import re
import sys
import time

random.seed(123)
k_bit = 32


#
# Complete the Node and CircularLinkedList class below.
#

class Node:
    # implement here. see case1 below for required attributes
    def __init__(self, data, k=k_bit):
        self.id = random.getrandbits(k)
        self.data = data
        self.next = None
        self.finger = data
    

class CircularLinkedList:
    # implement here. see case 2 below for required attribute
    def __init__(self):
        self.head = Node()
    pass
    
def distance(a, b, k=k_bit):
    # implement here. measures the clockwise distance from node a to node b with respect to the id.
    pass
    
def find_node(start, key):
    # takes an existing node in the list as the start value and searchs for the node which is responsible for the given key
    pass
    
def store(start, key, value):
    # finds the node responsible for the key starting from the "start" node and returns the value of the key stored in that node
    pass
    
def lookup(start, key):
    #find the value stored at the key starting at the node "start" and traversing the list
    pass
    
def update(node, k=k_bit):
    # updates the finger table for given node
    pass
    
def find_finger(node, key, k=k_bit):
    # use the nodes finger table to get the node closest to the key
    pass
    
def finger_lookup(start, key):
    # find the value stored at the key using finger table lookups starting with node "start"
    pass

def finger_store(start, key, value):
    # store key value pair using finger tables starting with node "start"
    pass
    
    
def case3(fptr):
    # what is the largest possible node id in the network if k=32?
    # answer = #
    # fptr.write(str(answer)+ '\n')
    pass

def setup1():
    arr = [x for x in range(0, 2 ** 5)]
    cll = CircularLinkedList()
    for i in range(len(arr)):
        temp = Node(arr[i])
        cll.sorted_insert(temp)
    current = cll.head
    while True:
        update(current)
        current = current.next
        if current == cll.head: break
    return cll


def case1(fptr):
    node = Node({}, k_bit)
    fptr.write(str(node.id) + '\n')
    fptr.write(str(node.data) + '\n') 
    fptr.write(str(node.next) + '\n')
    fptr.write(str(node.finger) + '\n')
    
def case2(fptr):
    cll = CircularLinkedList()
    fptr.write(str(cll.head) + '\n')
    l = [cll.sorted_insert(Node({}, k_bit)) for x in range(10)]
    cllist = cll.get_list()
    for e in cllist:
        for d in e:
            fptr.write(str(d) + ' ')
        fptr.write('\n')
        
def case4(fptr):
    d1 = distance(10, 10)
    d2 = distance(10, 100)
    d3 = distance(100, 10)
    fptr.write(str(d1) + '\n')
    fptr.write(str(d2) + '\n')
    fptr.write(str(d3) + '\n')
    
def case5(fptr):
    cll = CircularLinkedList()
    l = [cll.sorted_insert(Node({}, k_bit)) for x in range(10)]
    node = find_node(cll.head, 462568970)
    fptr.write(str(node.id) + '\n')
    fptr.write(str(node.data) + '\n')
    fptr.write(str(node.next.id) + '\n')
    
def case6(fptr):
    cll = CircularLinkedList()
    l = [cll.sorted_insert(Node({}, k_bit)) for x in range(10)]
    store(cll.head, 1606153229, 4)
    value = lookup(cll.head, 1606153229)
    fptr.write(str(value) + '\n')
    
def case7(fptr):
    # tests speed of regular insert
    arr = [x for x in range(0, 2 ** 12)]
    start = CircularLinkedList()
    start_time = time.time()
    for i in range(len(arr)):
        temp = Node(arr[i])
        start.sorted_insert(temp)
    process_time = time.time() - start_time
    print("SortedInsert took {} seconds".format(process_time))
    
def case8(fptr):
    cll = setup1()
    node = find_node(cll.head, 344973245)
    fptr.write(str(node.data)+'\n')
    n28 = node.finger[28]
    n30 = node.finger[30]
    fptr.write(str(n28.data)+ '\n')
    fptr.write(str(n30.data) + '\n')
    
def case9(fptr):
    cll = setup1()
    value = finger_lookup(cll.head, 344973245)
    fptr.write(str(value)+'\n')
    new_k = 2415140493
    finger_store(cll.head, new_k, 701)
    val = finger_lookup(cll.head, new_k)
    fptr.write(str(val) + '\n')
    node = find_node(cll.head, new_k)
    fptr.write(str(node.data) + '\n')
    fptr.write(str(node.id) + '\n')
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    case_num = input()
    
    globals()['case' + str(case_num)](fptr)

    fptr.close()
