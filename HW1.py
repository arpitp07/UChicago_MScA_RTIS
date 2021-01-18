import timeit
import heapq

k = 3
p = [1, 4, 4, 3, 1, 2, 6]
q = [1, 2, 3, 4, 5, 6, 7]

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

def kthPerson(k, p, q):
    ret = [1]*len(q)
    for i in range(len(q)):
        if ret[i] == 0:
            continue
        elif len([x for x in p if x >= q[i]]) < k:
            ret = [x*(y<q[i]) for x,y in zip(ret,q)]
        else:
            ret[i] = [x for x,y in enumerate(p) if y>=q[i]][k-1]+1
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

