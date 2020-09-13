'''
File: 2.py
Project: 202006
File Created: Thursday, 3rd September 2020 4:13:00 pm
Author: zyk
-----
Last Modified: Thursday, 3rd September 2020 4:43:53 pm
Modified By: zyk
-----
2020 - HUST
'''

# 稀疏向量

n, a, b = map(int, input().split())

u_index = list()
v_index = list()
u_value = list()
v_value = list()

for i in range(a):
    index, value = map(int, input().split())
    u_index.append(index)
    u_value.append(value)

for i in range(b):
    index, value = map(int, input().split())
    v_index.append(index)
    v_value.append(value)

ui = 0
vi = 0

prod = 0

while True:
    if ui >= a or vi >= b:
        break
    if u_index[ui] == v_index[vi]:
        prod += u_value[ui] * v_value[vi]
        ui += 1
        vi += 1
    elif u_index[ui] < v_index[vi]:
        ui += 1
    else:
        vi += 1

print(prod)
