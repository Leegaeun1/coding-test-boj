from collections import deque
import sys
input = sys.stdin.readline

def solution():
    m, n, h = map(int, input().split())
    box = []
    q = deque()
    no_grow = 0  # 안 익은 토마토 개수

    # 입력
    for f in range(h):
        floor = []
        for x in range(n):
            row = list(map(int, input().split()))
            for y in range(m):
                if row[y] == 1:
                    q.append((f, x, y))
                elif row[y] == 0:
                    no_grow += 1
            floor.append(row)
        box.append(floor)

    # 처음부터 다 익어있으면 0일
    if no_grow == 0:
        print(0)
        return

    # 6방향
    df = [0, 0, 0, 0, 1, -1]
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]

    days = 0

    while q:
        size = len(q)   # 오늘 처리할 개수
        for _ in range(size):
            f, x, y = q.popleft()
            for d in range(6):
                nf = f + df[d]
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nf < h and 0 <= nx < n and 0 <= ny < m:
                    if box[nf][nx][ny] == 0:
                        box[nf][nx][ny] = 1
                        no_grow -= 1
                        q.append((nf, nx, ny))
        days += 1

        if no_grow == 0:
            print(days)
            return

    # 끝까지 돌았는데 안 익은 토마토가 남아있으면
    print(-1)

solution()
