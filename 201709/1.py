'''
File: 1.py
Project: 201709
File Created: Saturday, 5th September 2020 10:33:24 am
Author: zyk
-----
Last Modified: Saturday, 5th September 2020 10:38:30 am
Modified By: zyk
-----
2020 - HUST
'''

N = int(int(input()) / 10)

result = int(N / 5) * 7

N = N % 5

result += int(N / 3) * 4

N = N % 3

result += N

print(int(result))