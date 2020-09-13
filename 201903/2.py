'''
File: 2.py
Project: 201903
File Created: Monday, 7th September 2020 4:34:54 pm
Author: zyk
-----
Last Modified: Sunday, 13th September 2020 12:07:22 pm
Modified By: zyk
-----
2020 - HUST
'''

n = int(input())

for i in range(n):
    exp = input().replace('x', '*').replace('/', '//')
    
    if eval(exp) == 24:
        print('Yes')
    else:
        print('No')
