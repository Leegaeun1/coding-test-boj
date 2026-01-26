import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
computers = []
res = 0
parent = [0] * (n+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a, b, c = map(int,input().split())
    computers.append((c, a, b))

for i in range(1, n+1):
    parent[i] = i

computers.sort()

for c, a, b in computers:
    if find(a) != find(b):
        union(a,b)
        res += c

print(res)
