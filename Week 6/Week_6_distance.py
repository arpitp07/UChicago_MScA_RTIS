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
        self.finger = {}
    def __repr__(self):
        return f'{self.data}'


class CircularLinkedList:
    # implement here. see case 2 below for required attribute
    def __init__(self):
        self.head = None
    
    def sorted_insert(self, node):
        
        curr = self.head
        if not self.head:
            self.head = node
            self.head.next = self.head
            return
        elif curr.next == self.head:
                node.next = curr.next
                curr.next = node
        else:
            while True:
                if distance(curr.id, node.id) + distance(node.id, curr.next.id) == distance(curr.id, curr.next.id):
                    node.next = curr.next
                    curr.next = node
                    return
                curr = curr.next

    def get_list(self):
        curr = self.head
        ls = []
        while True:
            ls.append([curr.id, curr.data, curr.finger])
            if curr.next == self.head:
                break
            curr = curr.next
        return ls

def distance(a, b, k=k_bit):
    # implement here. measures the clockwise distance from node a to node b with respect to the id.
    if a > b:
        return 2**k - (a - b)
    else:
        return b - a

def find_node(start, key):
    # takes an existing node in the list as the start value and searchs for the node which is responsible for the given key
    curr = start
    while True:
        if distance(curr.id, key) + distance(key, curr.next.id) == distance(curr.id, curr.next.id):
            return curr.next
        curr = curr.next

def store(start, key, value):
    # finds the node responsible for the key starting from the "start" node and returns the value of the key stored in that node
    node = find_node(start, key)
    node.data[key] = value
    return

def lookup(start, key):
    #find the value stored at the key starting at the node "start" and traversing the list
    node = find_node(start, key)
    return node.data[key]

def update(node, k=k_bit):
    # updates the finger table for given node
    for i in range(k):
        finger_key = (node.id + 2**i)%2**k
        node.finger[i+1] = find_node(node, finger_key)

def find_finger(node, key, k=k_bit):
    # use the nodes finger table to get the node closest to the key
    curr = node
    i = 1
    dist = distance(curr.id, key)
    while True:
        if distance(curr.id, key) + distance(key, curr.next.id) == distance(curr.id, curr.next.id):
            return curr.next
        elif distance(curr.finger[i].id, key) > dist:
            curr = curr.finger[i-1]
            dist = distance(curr.id, key)
            i=1
        elif i==k:
            curr = curr.finger[i]
            dist = distance(curr.id, key)
            i=1
        else:
            i+=1

def finger_lookup(start, key):
    # find the value stored at the key using finger table lookups starting with node "start"
    node = find_finger(start, key)
    return node.data

def finger_store(start, key, value):
    # store key value pair using finger tables starting with node "start"
    node = find_finger(start, key)
    node.data = value
    return
    
    
def case3():
    # what is the largest possible node id in the network if k=32?
    answer = 2**32
    print(str(answer)+ '\n')
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


def case1():
    node = Node({}, k_bit)
    print(str(node.id) + '\n')
    print(str(node.data) + '\n') 
    print(str(node.next) + '\n')
    print(str(node.finger) + '\n')

def case2():
    cll = CircularLinkedList()
    print(str(cll.head) + '\n')
    l = [cll.sorted_insert(Node({}, k_bit)) for x in range(10)]
    cllist = cll.get_list()
    for e in cllist:
        for d in e:
            print(str(d) + ' ')
        print('\n')

def case4():
    d1 = distance(10, 10)
    d2 = distance(10, 100)
    d3 = distance(100, 10)
    print(str(d1) + '\n')
    print(str(d2) + '\n')
    print(str(d3) + '\n')

def case5():
    cll = CircularLinkedList()
    l = [cll.sorted_insert(Node({}, k_bit)) for x in range(10)]
    node = find_node(cll.head, 462568970)
    print(str(node.id) + '\n')
    print(str(node.data) + '\n')
    print(str(node.next.id) + '\n')

def case6():
    cll = CircularLinkedList()
    l = [cll.sorted_insert(Node({}, k_bit)) for x in range(10)]
    store(cll.head, 1606153229, 4)
    value = lookup(cll.head, 1606153229)
    print(str(value) + '\n')

def case7():
    # tests speed of regular insert
    arr = [x for x in range(0, 2 ** 12)]
    start = CircularLinkedList()
    start_time = time.time()
    for i in range(len(arr)):
        temp = Node(arr[i])
        start.sorted_insert(temp)
    process_time = time.time() - start_time
    print("SortedInsert took {} seconds".format(process_time))

def case8():
    cll = setup1()
    node = find_node(cll.head, 344973245)
    print(str(node.data)+'\n')
    n28 = node.finger[28]
    n30 = node.finger[30]
    print(str(n28.data)+ '\n')
    print(str(n30.data) + '\n')

def case9():
    cll = setup1()
    value = finger_lookup(cll.head, 344973245)
    print(str(value)+'\n')
    new_k = 2415140493
    finger_store(cll.head, new_k, 701)
    val = finger_lookup(cll.head, new_k)
    print(str(val) + '\n')
    node = find_node(cll.head, new_k)
    print(str(node.data) + '\n')
    print(str(node.id) + '\n')

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     case_num = input()
#     globals()['case' + str(case_num)]()
#     .close()

########## QC ##########

cll = setup1()
l_node = []
curr = cll.head
while True:
    l_node.append(curr)
    curr = curr.next
    if curr == cll.head: break
l_id = [x.id for x in l_node]

index = 3
l_node[index].finger = {}
update(l_node[index])

node = find_finger(l_node[29], l_node[28].id-1)
# node = find_node(l_node[0], cll.head.id)
print(node.data, node.id)

########## Test Cases ##########

# case1()    
# case2()
# case3()
# case4()
# case5()
# case6()
# case7()
# case8()
# case9()