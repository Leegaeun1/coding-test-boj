from collections import deque

n = int(input())
s = []

for i in range(n):
    s.append(list(input().split()))

l = list(input().split())


for st in l:
    flag = False
    for i in range(n):
        if len(s[i]) > 0:

            if s[i][0] == st:
                s[i].pop(0)
                flag = True
                break
    if flag == False:
        print("Impossible")
        break



if flag:
    res = "Possible"
    for i in s:
        if i:
            res = "Impossible"
            break
    print(res)