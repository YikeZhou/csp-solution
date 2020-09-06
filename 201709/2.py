'''
File: 2.py
Project: 201709
File Created: Saturday, 5th September 2020 10:40:25 am
Author: zyk
-----
Last Modified: Sunday, 6th September 2020 9:33:05 am
Modified By: zyk
-----
2020 - HUST
'''

n, k = map(int, input().split())

xs = list() # (time, 1: borrow / 0: return, key number)


for i in range(k):
    w, s, c = map(int, input().split())
    # borrow
    xs.append((s, 1, w))
    # return
    xs.append((s + c, 0, w))

xs.sort()

result = list(range(1, n + 1))
for (time, is_borrow, key) in xs:
    if is_borrow == 1:
        result[result.index(key)] = 0 # borrow
    else:
        result[result.index(0)] = key # return

print(' '.join(map(str, result)))
