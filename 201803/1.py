'''
File: 1.py
Project: 201803
File Created: Sunday, 6th September 2020 9:16:12 pm
Author: zyk
-----
Last Modified: Sunday, 6th September 2020 9:19:13 pm
Modified By: zyk
-----
2020 - HUST
'''

xs = list(map(int, input().split()))

ans = 0
last = 1

for x in xs:
    if x == 0:
        break
    elif x == 1:
        ans += 1
        last = 1
    else:
        if last == 1:
            last = 2
            ans += last
        else:
            last += 2
            ans += last

print(ans)
