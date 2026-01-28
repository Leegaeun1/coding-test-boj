import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int,input().split())
parent = [i for i in range(v+1)]
li = []
res = 0

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(e):
    a, b, c = map(int,input().split())
    li.append((c,a,b))

li.sort()

for c, a, b in li:
    if find(a) != find(b):
        union(a,b)
        res += c

print(res)