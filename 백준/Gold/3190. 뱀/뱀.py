from collections import deque

n = int(input())
k = int(input())

board = [[0]*n for _ in range(n)]

# 사과
for _ in range(k):
    x, y = map(int,input().split())
    board[x-1][y-1] = 2

l = int(input())
trans = {}
for _ in range(l):
    t, d = input().split()
    trans[int(t)] = d

# 동 남 서 북
dir = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0

snake = deque()
snake.append((0,0))
board[0][0] = 1

time = 0

while True:
    time += 1
    
    head_r, head_c = snake[-1]
    nr = head_r + dir[d][0]
    nc = head_c + dir[d][1]
    
    # 벽 or 자기 몸
    if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc] == 1:
        break
    
    # 이동
    if board[nr][nc] == 2:  # 사과 있음
        board[nr][nc] = 1
        snake.append((nr,nc))
    else:  # 사과 없음
        board[nr][nc] = 1
        snake.append((nr,nc))
        tr, tc = snake.popleft()
        board[tr][tc] = 0
    
    # 방향 전환
    if time in trans:
        if trans[time] == 'D':
            d = (d+1) % 4
        else:
            d = (d-1) % 4

print(time)