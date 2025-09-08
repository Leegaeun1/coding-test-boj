import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = list(map(int,input().split()))
li.sort()
cnt = 0

s, e = 0, n-1

while s < e:
    if li[s] + li[e] == m:
        cnt += 1
        s += 1
        e -= 1
    elif li[s] + li[e] < m:
        s += 1 
    elif li[s] + li[e] > m:
        e -= 1 

print(cnt)