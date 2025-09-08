n = int(input())
li = [["#"]*50 for _ in range(50)]

# 시계 방향 (남, 서, 북, 동)
dirs = [(1,0), (0,-1), (-1,0), (0,1)]

# 시작 위치, 방향
x, y = 25, 25
d_idx = 0  # 0:남쪽 시작
dx, dy = dirs[d_idx]

li[x][y] = '.'
pos = [(x,y)]

m = input()
for alp in m:
    if alp == "F":
        x += dx
        y += dy
        li[x][y] = '.'
        pos.append((x,y))
    elif alp == "R":
        d_idx = (d_idx + 1) % 4
        dx, dy = dirs[d_idx]
    elif alp == "L":
        d_idx = (d_idx - 1) % 4
        dx, dy = dirs[d_idx]

# 방문한 좌표의 min/max 찾기
row_min = min(p[0] for p in pos)
row_max = max(p[0] for p in pos)
col_min = min(p[1] for p in pos)
col_max = max(p[1] for p in pos)

# 실제 그리드 출력 (잘라서)
for i in range(row_min, row_max+1):
    print("".join(li[i][col_min:col_max+1]))
