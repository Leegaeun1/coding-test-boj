n, m = map(int, input().split())
board = [input() for _ in range(n)]

min_res = float('inf')

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0  # 시작이 W
        cnt2 = 0  # 시작이 B

        for x in range(8):
            for y in range(8):
                cur = board[i + x][j + y]
                if (x + y) % 2 == 0:
                    if cur != 'W':
                        cnt1 += 1
                    if cur != 'B':
                        cnt2 += 1
                else:
                    if cur != 'B':
                        cnt1 += 1
                    if cur != 'W':
                        cnt2 += 1

        min_res = min(min_res, cnt1, cnt2)

print(min_res)
