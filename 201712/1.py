'''
File: 1.py
Project: 201712
File Created: Sunday, 6th September 2020 9:34:54 am
Author: zyk
-----
Last Modified: Sunday, 6th September 2020 9:37:20 am
Modified By: zyk
-----
2020 - HUST
'''

n = int(input())

xs = list(sorted(map(int, input().split())))

result = 10000

for (a, b) in zip(xs[:-1], xs[1:]):
    if (b - a) < result:
        result = b - a

print(result)
