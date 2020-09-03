'''
File: 1.py
Project: 202006
File Created: Tuesday, 25th August 2020 6:44:45 pm
Author: zyk
-----
Last Modified: Thursday, 3rd September 2020 4:15:32 pm
Modified By: zyk
-----
2020 - HUST
'''

# 线性分类器

yes = "Yes"
no = "No"

n, m = map(int, input().split())

# dots
xs = list()
ys = list()
ts = list()

for i in range(n):
    x, y, t = input().split()
    x, y = map(int, (x, y))
    # a: true, b: false
    xs.append(x)
    ys.append(y)
    ts.append(t[0] == 'A')

# lines
for i in range(m):
    k0, k1, k2 = map(int, input().split())
    # k0 + k1*x + k2*y ?= 0
    reverse = 0
    for x, y, t in zip(xs, ys, ts):
        if reverse == 0:
            # 判断 A 类型的点是否 >0
            if (k0 + k1 * x + k2 * y > 0 and t) or (k0 + k1 * x + k2 * y < 0 and not t):
                reverse = 1
            else:
                reverse = -1
        if t == ((k0 + k1 * x + k2 * y) * reverse > 0):
            continue
        else:
            print(no)
            break
    else:
        print(yes)
