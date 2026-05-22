from collections import deque

def solution(board):
    N = len(board)

    INF = float('inf')

    # 동 남 서 북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    # cost[x][y][dir]
    cost = [[[INF]*4 for _ in range(N)] for _ in range(N)]

    queue = deque()

    # 시작 방향 2개
    for d in [0,1]:
        nx = dx[d]
        ny = dy[d]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
            cost[nx][ny][d] = 100
            queue.append((nx, ny, d, 100))

    while queue:
        x, y, d, money = queue.popleft()

        for nd in range(4):
            nx = x + dx[nd]
            ny = y + dy[nd]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:

                # 방향 같으면 직선
                if d == nd:
                    new_cost = money + 100
                else:
                    new_cost = money + 600

                if cost[nx][ny][nd] > new_cost:
                    cost[nx][ny][nd] = new_cost
                    queue.append((nx, ny, nd, new_cost))

    return min(cost[N-1][N-1])