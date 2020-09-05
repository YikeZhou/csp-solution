'''
File: 1.py
Project: 201703
File Created: Saturday, 5th September 2020 10:04:48 am
Author: zyk
-----
Last Modified: Saturday, 5th September 2020 10:22:33 am
Modified By: zyk
-----
2020 - HUST
'''

n, k = map(int, input().split())

a = list(map(int, input().split()))

result = 0
current = 0

for i in a:
    current += i
    if current >= k:
        result += 1
        current = 0
    
if 0 < current and current < k:
    result += 1
    
print(result)
