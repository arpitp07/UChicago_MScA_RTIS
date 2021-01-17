import timeit

k = 2
p = [1, 4, 4, 3, 1, 2, 6]
q = [1, 2, 3, 4, 5, 6, 7]

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
            ret[i]=[x for x,y in enumerate(p) if y>=q[i]][k-1]+1
    return ret

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

start = timeit.default_timer()
print(kthPerson(k, p, q))
stop = timeit.default_timer()
execution_time = stop - start
print(f"Program executed in {execution_time}")