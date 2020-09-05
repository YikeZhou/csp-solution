'''
File: 2.py
Project: 201703
File Created: Saturday, 5th September 2020 10:25:04 am
Author: zyk
-----
Last Modified: Saturday, 5th September 2020 10:32:00 am
Modified By: zyk
-----
2020 - HUST
'''

n = int(input())
m = int(input())

result = list(range(1, n + 1))

for i in range(m):
    p, q = map(int, input().split())
    # apply move
    i = result.index(p)
    result.remove(p)
    result.insert(i + q, p)

print(' '.join(map(str, result)))
