'''
File: 2.py
Project: 201712
File Created: Sunday, 6th September 2020 9:39:30 am
Author: zyk
-----
Last Modified: Sunday, 13th September 2020 12:24:59 pm
Modified By: zyk
-----
2020 - HUST
'''

n, k = map(int, input().split())

result = list(range(1, n + 1))
valid = [1 for i in range(n)]

cur = 0
p = 0

while sum(valid) > 1:
    cur += 1
    while valid[p] == 0:
        p = (p + 1) % n
    
    if cur % k == 0 or cur % 10 == k:
        valid[p] = 0
    p = (p + 1) % n
    
print(result[valid.index(1)])
