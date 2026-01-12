import sys
input = sys.stdin.readline

t = int(input())

def issame(n):
    li = []
    for i in range(n):
        li.append(input().strip())
    li.sort()
    #print(li)
    for i in range(len(li)-1):
        st_len = len(li[i])
        if li[i+1][:st_len] == li[i]:
            return "NO"


    return "YES"

for _ in range(t):
    n = int(input())
    print(issame(n))