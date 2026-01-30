from collections import deque
m, n = map(int,input().split())

li = []
direct = [[0,1],[0,-1],[1,0],[-1,0]]
max_res = 0

for _ in range(m):
    li.append(list(input()))

def bfs(x, y, cnt):
    visited = [[False]*n for _ in range(m)]
    queue = deque([(x,y,cnt)])
    res = 0
    visited[x][y] = True
    while queue:
        x, y, cnt = queue.popleft()
        
        for nx, ny in direct:
            dx = x + nx
            dy = y + ny
            if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy] and li[dx][dy] == 'L':
                queue.append((dx,dy,cnt+1))
                visited[dx][dy] = True
                res = max(res,cnt+1)
    return res

for i in range(m):
    for j in range(n):
        if li[i][j] == 'L':
            res = bfs(i,j, 0)
            max_res = max(res,max_res)
print(max_res)
