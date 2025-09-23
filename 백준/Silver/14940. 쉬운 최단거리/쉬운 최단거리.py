from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
li = []
des_x, des_y = -1,-1
direct = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(m):
        if tmp[j] == 2:   # 목표지점 위치 저장
            des_x, des_y = i, j
    li.append(tmp)

# 거리 기록 배열 (-1로 초기화)
dist = [[-1]*m for _ in range(n)]

def bfs(sx,sy):
    queue = deque([(sx,sy)])
    dist[sx][sy] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if li[nx][ny] != 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))

bfs(des_x, des_y)

for i in range(n):
    for j in range(m):
        if li[i][j] == 0:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
