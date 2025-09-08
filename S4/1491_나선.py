n, m = map(int, input().split())
visited = [[False] * n for _ in range(m)]

x, y = m - 1, 0
visited[x][y] = True
d = 1
cnt = 1
a = b = 0

while cnt < n * m:
    dx = [0, -1, 0, 1]  # 오른쪽, 위쪽, 왼쪽, 아래
    dy = [1, 0, -1, 0]
    dir = d%4 - 1

    nx, ny = x + dx[dir], y + dy[dir]
    if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
        d += 1
        continue

    x, y = nx, ny
    visited[x][y] = True
    cnt += 1

    if dir == 0:
        a += 1
    elif dir == 1:
        b += 1
    elif dir == 2:
        a -= 1
    else:
        b -= 1

print(a, b)
