import timeit
import random
import heapq

# TC 1
k = 3
p = [1, 4, 4, 3, 1, 2, 6]
q = [1, 5, 5, 5, 2, 2, 2]

# # TC4
# k = 30089
# p = [random.randint(1, 99999) for i in range(71229)]
# q = [random.randint(2, 99992) for i in range(14809)]

# # TC6
# k = 8799
# p = [random.randint(1, 99996) for i in range(54156)]
# q = [random.randint(1, 100000) for i in range(37788)]

# # TC7
# k = 19276
# p = [random.randint(4, 99993) for i in range(25557)]
# q = [random.randint(1, 100000) for i in range(95812)]

# # TC8
# k = 87744
# p = [random.randint(2, 99998) for i in range(97804)]
# q = [random.randint(1, 100000) for i in range(61171)]

def kthPerson(k, p, q):
    ret = [0]*len(q)
    q_sort = sorted([(x[1], x[0]) for x in enumerate(q)])
    bus_heap = p[:k]
    p_dup = p[k:]
    index = k
    j_last = None
    heapq.heapify(bus_heap)
    if k > len(p):
        return ret
    for (i, (j, j_ret)) in enumerate(q_sort):
        if j == j_last:
            ret[j_ret] = index
        else:
            try:
                while bus_heap[0] < j:
                    heapq.heapreplace(bus_heap, p_dup.pop(0))
                    index += 1
                ret[j_ret] = index
                j_last = j
            except IndexError:
                break
    return ret


start = timeit.default_timer()
print(kthPerson(k, p, q))
stop = timeit.default_timer()
execution_time = stop - start
print(f"Program executed in {execution_time}")