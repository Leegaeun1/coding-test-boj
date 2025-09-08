n = int(input())
m = input()

# 세로, 가로 흔적을 따로 기록
vert = [[False] * n for _ in range(n)]
horiz = [[False] * n for _ in range(n)]

x, y = 0, 0
move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

for d in m:
    dx, dy = move[d]
    nx, ny = x + dx, y + dy

    # 범위를 벗어나면 이동/표시 모두 무시
    if not (0 <= nx < n and 0 <= ny < n):
        continue

    if d in 'UD':
        vert[x][y] = True
        vert[nx][ny] = True
    else:
        horiz[x][y] = True
        horiz[nx][ny] = True

    x, y = nx, ny

# 결과 출력
for i in range(n):
    row = []
    for j in range(n):
        if vert[i][j] and horiz[i][j]:
            row.append('+')
        elif vert[i][j]:
            row.append('|')
        elif horiz[i][j]:
            row.append('-')
        else:
            row.append('.')
    print(''.join(row))
