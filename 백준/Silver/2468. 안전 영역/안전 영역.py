import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
space = []
max_len, res = 0, 0
direct = [[0,1],[0,-1],[1,0],[-1,0]]

for _ in range(n):
    tmp = list(map(int,input().split()))
    max_len = max(max(tmp),max_len)
    space.append(tmp)

def bfs(l, space, i, j):
    queue = deque([(i,j)])
    visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if space[nx][ny] > l and not visited[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = True

for l in range(max_len):

    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and space[i][j] > l:
                bfs(l,space,i,j)
                cnt += 1
    res = max(res,cnt)
print(res)