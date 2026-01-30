import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for _ in range(n)]
ans = 0
visited = [False] * n

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, cnt):
    global ans
    visited[x] = True
    if cnt == 4:
        ans = 1
        return
    for y in graph[x]:
        if not visited[y]:
            visited[y] = True
            dfs(y,cnt+1)
            if ans:
                return
            visited[y] = False

    return
            
for i in range(n):
    visited = [False] * n
    dfs(i,0)

print(ans)