from collections import deque

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

direct = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs():
    visited = [[False]*m for _ in range(n)]
    queue = deque([(0,0)])
    visited[0][0] = True

    air = [[False]*m for _ in range(n)] # 공기인가
    air[0][0] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in direct:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] == 0: # 공기?
                    visited[nx][ny] = True
                    air[nx][ny] = True
                    queue.append((nx,ny))
    return air


time = 0

while True:
    air = bfs()
    melt = [] # 녹는거 

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1: # 치즈
                cnt = 0
                for dx, dy in direct:
                    nx, ny = i+dx, j+dy
                    if air[nx][ny]: # 공기임
                        cnt += 1
                if cnt >= 2:
                    melt.append((i,j))

    if not melt: # 더이상 녹는거 없으면 break
        break

    for x, y in melt: # 녹음
        board[x][y] = 0

    time += 1

print(time)