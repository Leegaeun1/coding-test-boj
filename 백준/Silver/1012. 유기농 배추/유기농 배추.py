from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
direc = [[1,0],[-1,0],[0,-1],[0,1]] # 상하좌우


def bfs(farm,r,c):
    queue = deque([(r,c)])
    visited[r][c] = True
    while queue:
        nx,ny = queue.popleft()
        for x,y in direc:
            dx, dy = nx + x, ny + y
            if 0 <= dx < len(farm) and 0 <= dy < len(farm[0]) and not visited[dx][dy] and farm[dx][dy] == 1:
                queue.append([dx,dy])
                visited[dx][dy] = True
  
  

for _ in range(t):
    cnt = 0
    m,n,k = map(int,input().split())
    farm = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
  
  
    for j in range(k):
        x, y = map(int,input().split())
        farm[y][x] = 1 # 배추 심긴 곳
  
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and farm[i][j] == 1:
                bfs(farm,i,j)
                cnt += 1
        
    print(cnt)
