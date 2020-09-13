'''
File: 4.py
Project: 201703
File Created: Monday, 7th September 2020 8:44:50 pm
Author: zyk
-----
Last Modified: Sunday, 13th September 2020 11:58:44 am
Modified By: zyk
-----
2020 - HUST
'''

n, m = map(int, input().split())

xs = list()
ys = list()
ds = list()
idxs = [i for i in range(m)]

ans = 0
fa = [i for i in range(n)] # union find set
def find(x):
    if fa[x] == x:
        return x
    else:
        return find(fa[x])

for i in range(m):
    x, y, d = map(int, input().split())
    xs.append(x - 1)
    ys.append(y - 1)
    ds.append(d)

idxs.sort(key=(lambda x: ds[x]))

for i in idxs:
    fax = find(xs[i])
    fay = find(ys[i])
    if fax == fay:
        continue
    else:
        fa[fay] = fax
        ans = ds[i]
        if find(0) == find(n - 1):
            print(ans)
            exit()
