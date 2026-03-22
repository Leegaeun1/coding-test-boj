from collections import deque

n, m = map(int,input().split())
board = []
direct = [(0,1),(0,-1),(1,0),(-1,0)]

def roll(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#':
        x += dx
        y += dy
        cnt += 1
        if [x,y] == hole:
            break
    return x, y, cnt

def bfs():
    queue = deque()
    queue.append((red[0], red[1], blue[0], blue[1], 0))
    visited = set()
    visited.add((red[0], red[1], blue[0], blue[1]))

    while queue:
        r_r, r_c, b_r, b_c, cnt = queue.popleft()

        if cnt >= 10:
            continue

        for dx, dy in direct:
            nr_r, nr_c, r_cnt = roll(r_r, r_c, dx, dy)
            nb_r, nb_c, b_cnt = roll(b_r, b_c, dx, dy)

            # 파란 구슬 먼저 빠지면 실패
            if [nb_r, nb_c] == hole:
                continue

            # 빨간 구슬만 빠지면 성공
            if [nr_r, nr_c] == hole:
                return cnt + 1

            # 같은 위치면 조정
            if nr_r == nb_r and nr_c == nb_c:
                if r_cnt > b_cnt:
                    nr_r -= dx
                    nr_c -= dy
                else:
                    nb_r -= dx
                    nb_c -= dy

            if (nr_r, nr_c, nb_r, nb_c) not in visited:
                visited.add((nr_r, nr_c, nb_r, nb_c))
                queue.append((nr_r, nr_c, nb_r, nb_c, cnt+1))

    return -1


# 입력
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == 'R':
            red = [i,j]
        elif tmp[j] == 'B':
            blue = [i,j]
        elif tmp[j] == 'O':
            hole = [i,j]
    board.append(tmp)

print(bfs())