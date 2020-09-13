'''
File: P2196.py
Project: miscellaneous
File Created: Wednesday, 9th September 2020 2:30:22 pm
Author: zyk
-----
Last Modified: Sunday, 13th September 2020 10:09:12 am
Modified By: zyk
-----
2020 - HUST
'''

n = int(input())

mines = list(map(int, input().split()))
c = list()

for i in range(n - 1):
    cons = list(map(int, input().split()))
    while len(cons) != n:
        cons.insert(0, 0)
    # add cons to c[i][j]
    c.append(cons)

pre = [-1 for i in range(n)]
res = [0 for i in range(n)]

for i in range(n):
    # 1. find the max{a[j]} (0 <= j < i)
    cur_max = 0
    cur_idx = -1
    for j in range(i):
        if c[j][i] and res[j] > cur_max:
            cur_max = res[j]
            cur_idx = j
    # 2. a[i] = max{a[j]} + mines[i] if c[j][i] == 1
    res[i] = cur_max + mines[i]
    pre[i] = cur_idx

# print trace
ans = max(res)
idx = res.index(ans)
tr = list()
while idx >= 0:
    tr.insert(0, idx + 1)
    idx = pre[idx]
print(' '.join(map(str, tr)))
print(ans)
