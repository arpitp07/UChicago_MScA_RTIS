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
        # self.head = Node(None, k_bit)
        self.head = None
        # self.head.next = self.head

    # def sorted_insert(self, node):
        
    #     if self.head.id > node.id:
    #         self.head.data = node.data
    #         self.head.finger = node.finger
    #         return
        
    #     curr = self.head
    #     node.next = curr.next
    #     curr.next = node
        
    #     while curr.next != self.head:
    #         if node.id > node.next.id and node.next!=self.head:
    #             curr.next = node.next
    #             node.next = curr.next.next
    #             curr.next.next = node
    #             curr = curr.next
    #         else:
    #             break
    
    def sorted_insert(self, node):
            
        if not self.head:
            self.head = node
            self.head.next = self.head
            # self.tail = node
            # self.tail.next = self.head
            # self.head.next = self.tail
            return
        
        if self.head.next == self.head:
            self.head.next = node
            node.next = self.head
            return
        
        if node.id < self.head.id:
            curr = self.head
            while True:
                if curr.id < node.id or curr.next == self.head:
                    node.next = curr.next
                    curr.next = node
                    return
        
        else:
            curr = self.head
            while True:
                if curr.next.id > node.id or curr.next == self.head:
                    node.next = curr.next
                    curr.next = node
                    return

    def sorted_insert(self, node):
        
        if not self.head:
            self.head = node
            self.head.next = self.head
            # self.tail = node
            # self.tail.next = self.head
            # self.head.next = self.tail
            return
        
        if self.head.next == self.head:
            self.head.next = node
            node.next = self.head
            return
        
        if node.id < self.head.id:
            curr = self.head
            while True:
                if curr.id < node.id or curr.next == self.head:
                    node.next = curr.next
                    curr.next = node
                    self.head = node
                    return
                curr = curr.next
        
        else:
            curr = self.head
            while True:
                if curr.next.id > node.id or curr.next == self.head:
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
        if (curr.id < key) & (curr.next.id >= key):
            return curr
        if curr.next == start:
            return CircularLinkedList.head
        curr = curr.next
    
def store(start, key, value):
    # finds the node responsible for the key starting from the "start" node and returns the value of the key stored in that node
    curr = start
    while True:
        if curr.id >= key:
            curr.data[key] = value
            return
        if curr.next == start:
            return
        curr = curr.next
    # pass
    
def lookup(start, key):
    #find the value stored at the key starting at the node "start" and traversing the list
    curr = start
    while True:
        if curr.id >= key:
            return curr.data[key]
        if curr.next == start:
            return
        curr = curr.next
    
def update(node, k=k_bit):
    # updates the finger table for given node
    # curr = node
    # l = []
    # while True:
    #     l.append(curr)
    #     curr = curr.next
    #     if curr.next == node: break
    # l.sort()
    curr = node
    for i in range(k):
        finger_key = (node.id + 2**i)%2**k
        next_id = curr.next.id
        while True:
            if curr.next.id >= finger_key:
                node.finger[i+1] = curr.next
                # curr = curr.next
                break
            if (curr.next.id < curr.id) & (finger_key > curr.id) & (finger_key > curr.next.id):
                node.finger[i+1] = curr.next
                # curr = curr.next
                break
            curr = curr.next
        # node.finger[i+1] = [x for x in l if x.id >= (node.id + 2**i)%2**k][0]
    
def find_finger(node, key, k=k_bit):
    # use the nodes finger table to get the node closest to the key
    curr = node
    i = k
    while True:
        if key >= curr.finger[i].id:
            curr = curr.finger[i]
            i=k
        elif (i == 1) & (curr.finger[i].id > key):
            return curr.finger[i]
        elif (key < curr.id) & (curr.id < curr.next.id):
            curr = curr.finger[k]
            i=k
        else:
            i-=1

    
def finger_lookup(start, key):
    # find the value stored at the key using finger table lookups starting with node "start"
    pass

def finger_store(start, key, value):
    # store key value pair using finger tables starting with node "start"
    pass
    
    
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
    
    
# case2()
# case3()
cll = setup1()

# case8()

# if __name__ == '__main__':
#      = open(os.environ['OUTPUT_PATH'], 'w')
    
#     case_num = input()
    
#     globals()['case' + str(case_num)]()

#     .close()
l_node = []
curr = cll.head
while True:
    l_node.append(curr)
    curr = curr.next
    if curr == cll.head: break

index = 3
l_node[index].finger = {}
update(l_node[index])

node = find_finger(l_node[3], 7174963)