import timeit
import random
import heapq

# TC 1
k = 2
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

# heapq.heapify(p)
# def kthPerson(k, p, q):
#     ret = [0]*len(q)
#     q_max_0 = max(q)+1
#     for i in range(len(q)):
#         if q[i] >= q_max_0:
#             # ret.append(0)
#             continue
#         # # if min(sorted(p, reverse = True)[0:k]) < q[i]:
#         elif len([x for x in p if x >= q[i]]) < k:
#             # ret.append(0)
#             q_max_0 = q[i]
#         else:
#             # ret.append([x for x,y in enumerate(p) if y>=q[i]][k-1]+1)
#             ret[i]=[x for x,y in enumerate(p) if y>=q[i]][k-1]+1
#     return ret

# def kthPerson(k, p, q):
#     ret = [1]*len(q)
#     for i, j in enumerate(q):
#         if ret[i] == 0:
#             continue
#         elif j in q[0:i]:
#             ret[i] = ret[q.index(j)]
#         elif len([x for x in p if x >= j]) < k:
#             ret = [x*(y<j) for x,y in zip(ret,q)]
#         else:
#             ret[i] = [x for x,y in enumerate(p) if y>=j][k-1]+1
#     return ret

# def kthPerson(k, p, q):
#     ret = []
#     _=0
#     for i, j in enumerate(q):
#         if _==1 & (j >= q[ret.index(0)]):
#             ret.append(0)
#         elif j in q[0:i]:
#             ret.append(ret[q.index(j)])
#         if len([x for x in p if x >= j]) >= k:
#             try:
#                 ret.append([x for x,y in enumerate(p) if y>=j][k-1]+1)
#             except IndexError:
#                 ret.append(0)
#                 _=1
#     return ret

# def kthPerson(k, p, q):
#     ret = [1]*len(q)
#     for i, j in enumerate(q):
#         if k > len(p):
#             ret = [0]*len(q)
#             break
#         elif ret[i] == 0:
#             continue
#         elif j in q[:i]:
#             ret[i] = ret[q.index(j)]
#         else:
#             try:
#                 p_dup = p[k:]
#                 bus_heap = p[:k]
#                 heapq.heapify(bus_heap)
#                 while bus_heap[0] < j:
#                     heapq.heapreplace(bus_heap, p_dup.pop(0))
#                 ret[i] = len(p) - len(p_dup)
#             except IndexError:
#                 ret = [x*(y<j) for x,y in zip(ret,q)]
#     return ret

# def kthPerson(k, p, q):
#     ret = [0]*len(q)
#     q_sort = [(x[1], x[0]) for x in enumerate(q)]
#     heapq.heapify(q_sort)
#     q_sort = [heapq.heappop(q_sort) for i in range(len(q_sort))]
#     bus_heap = p[:k]
#     p_dup = p[k:]
#     heapq.heapify(bus_heap)
    
#     for (i, (j, j_ret)) in enumerate(q_sort):
#         if k > len(p):
#             break
#         elif j == [x for x,y in q_sort][i-1]:
#             ret[j_ret] = ret[q_sort[i-1][1]]
#         else:
#             try:
#                 while bus_heap[0] < j:
#                     heapq.heapreplace(bus_heap, p_dup.pop(0))
#                 ret[j_ret] = len(p) - len(p_dup)
#             except IndexError:
#                 break
#     return ret

def kthPerson(k, p, q):
    ret = [0]*len(q)
    q_sort = sorted([(x[1], x[0]) for x in enumerate(q)])
    bus_heap = p[:k]
    # p_dup = p[k:]
    index = k
    j_last = None
    heapq.heapify(bus_heap)
    
    for (i, (j, j_ret)) in enumerate(q_sort):
        if k > len(p):
            break
        elif j == j_last:
            ret[j_ret] = index
            
        else:
            while bus_heap[0] < j:
                bus_heap = p[index-1:index + k-1]
                if len(bus_heap) < k:
                    return ret
                heapq.heapify(bus_heap)
                index += 1
            ret[j_ret] = index
            j_last = j
    return ret


start = timeit.default_timer()
print(kthPerson(k, p, q))
stop = timeit.default_timer()
execution_time = stop - start
print(f"Program executed in {execution_time}")


# ret = []
# for i in range(len(q)):
#     p_heap = [(x[1], x[0]) for x in list(enumerate(p))]
#     heapq.heapify(p_heap)
#     [heapq.heappop(p_heap) for i in range(sum([x[0]<q[i] for x in p_heap]))]
#     p_heap = [(x[1], x[0]) for x in p_heap]
#     heapq.heapify(p_heap)
#     try:
#         ret.append([heapq.heappop(p_heap) for i in range(k)][-1][0]+1)
#     except IndexError:
#         ret.append(0)

# print(ret)

# def kthPerson(k, p, q):
#     # Write your code here
#     ret = []
#     q = sorted(enumerate(q), key=lambda x:x[1])
#     for i in range(len(q)):
#         # if min(sorted(p, reverse = True)[0:k]) < q[i]:
#         if len([x for x in p if x >= q[i][1]]) < k:
#             ret += [0]*(len(q)-i)
#             break
#         else:
#             ret.append([x for x,y in enumerate(p) if y>=q[i][1]][k-1]+1)
#     return [x for x,y in sorted(zip(ret, [x for x,y in q]), key=lambda x:x[1])]