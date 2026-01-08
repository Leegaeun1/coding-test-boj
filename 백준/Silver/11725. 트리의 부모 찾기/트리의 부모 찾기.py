from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
queue = deque([1])
root = [1] * (n+1)

for i in range(n-1):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

while queue:
    pop = queue.popleft()
    visited[pop] = True

    for i in graph[pop]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            root[i] = pop

for i in root[2:]:
    print(i)