import sys
from collections import deque
input = sys.stdin.readline

n, m , v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
res_dfs = []
res_bfs = []

for _ in range(m):
    x, y =map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):
    graph[i].sort()

def dfs(v):
    visited_dfs[v]=True
    res_dfs.append(v)
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(graph, v):
    queue = deque([v])
    visited_bfs[v] = True
    res_bfs.append(v)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
                res_bfs.append(i)

dfs(v)
bfs(graph,v)

for i in res_dfs:
    print(i,end=" ")
print()
for i in res_bfs:
    print(i,end=" ")