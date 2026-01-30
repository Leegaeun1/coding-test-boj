from collections import deque
n, m = map(int,input().split())

li = []

for _ in range(n):
    li.append(list(map(int,input().split())))

direct = [[0,1],[0,-1],[1,0],[-1,0]]

visited = [[False]*m for i in range(n)]
max_res = 0
cnt = 0

def bfs(x, y):
    queue = deque([(x,y)])
    res = 1
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for nx, ny in direct:
            dx = x + nx
            dy = y + ny
            if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy] and li[dx][dy] == 1:
                queue.append((dx,dy))
                visited[dx][dy] = True
                res += 1
    return res 

for i in range(n):
    for j in range(m):
        if not visited[i][j] and li[i][j] == 1:
            res = bfs(i, j)
            max_res = max(max_res,res)
            cnt += 1

print(cnt)
print(max_res)