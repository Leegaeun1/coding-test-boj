from collections import deque

n, m = map(int,input().split())
miro = []
direct = [[1,0],[-1,0],[0,1],[0,-1]]
res_cnt = 1

for i in range(n):
    miro.append(list(map(int,input())))

def bfs(x,y,cnt):
    queue = deque([(x,y,cnt)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    min_cnt = float('inf')

    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0<= nx < n and 0 <= ny < m and not visited[nx][ny] and miro[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append([nx,ny,cnt+1])
                if nx == n-1 and ny == m-1:
                    min_cnt = min(min_cnt,cnt+1)
    
    return min_cnt

res_cnt = bfs(0,0,res_cnt)
print(res_cnt)