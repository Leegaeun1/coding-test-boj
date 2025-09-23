from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
li = []

direct = [[0,1],[0,-1],[1,0],[-1,0]]
res = [0,0]

for i in range(n):
    li.append(list(input()))

def color_bfs(li, i, j):
    queue = deque([(i,j)])
    visited_color[i][j] = True
    stand = li[i][j]

    while queue:
        x, y = queue.popleft()

        for dx, dy in direct:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n and not visited_color[nx][ny]:
                if stand == "B":
                    if li[nx][ny] != "B":
                        continue 
                else:
                    if li[nx][ny] == "B":
                        continue
                visited_color[nx][ny] = True
                queue.append((nx,ny))

def bfs(li, i, j):
    queue = deque([(i,j)])
    visited[i][j] = True
    stand = li[i][j]

    while queue:
        x, y = queue.popleft()

        for dx, dy in direct:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if stand == li[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))


visited_color = [[False] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited_color[i][j]:
            color_bfs(li,i,j)
            res[1] += 1
        if not visited[i][j]:
            bfs(li,i,j)
            res[0] += 1
print(*res)