from collections import deque

n, L, R = map(int,input().split())
direct = [(-1,0),(1,0),(0,-1),(0,1)]
board = [list(map(int,input().split())) for _ in range(n)]

def bfs(r,c,visited):
    cnt = 1 
    queue = deque([(r,c)])
    visited[r][c] = True
    person = board[r][c]
    tmp = [[r,c]]
    while queue:
        r,c = queue.popleft()
        for x, y in direct:
            dx = x + r
            dy = y + c
            if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy]:
                if L <= abs(board[r][c] - board[dx][dy]) <= R:
                    person += board[dx][dy]
                    cnt += 1
                    queue.append([dx,dy])
                    visited[dx][dy] = True
                    tmp.append([dx,dy])
    for x, y in tmp:
        board[x][y] = person // cnt
    return cnt,visited

res = 0

while True:
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                t_cnt, visited= bfs(i,j,visited)
                cnt += t_cnt
                if t_cnt > 1:
                    flag = True
    if not flag:
        break
    res += 1
print(res)