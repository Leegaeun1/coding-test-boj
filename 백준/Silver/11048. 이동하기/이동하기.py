from collections import deque
n, m = map(int,input().split())
li = []
dp = [[0]*m for _ in range(n)]

for _ in range(n):
    li.append(list(map(int,input().split())))
    
dp[0][0] = li[0][0]

for x in range(n):
    for y in range(m):
        # 위쪽 가능
        if x >= 1:
            dp[x][y] = max(dp[x][y],dp[x-1][y]+li[x][y])
        # 왼쪽 가능
        if y >= 1:
            dp[x][y] = max(dp[x][y],dp[x][y-1]+li[x][y])
        # 대각선 가능
        if x >= 1 and y >=1:
            dp[x][y] = max(dp[x][y],dp[x-1][y-1]+li[x][y])
print(dp[n-1][m-1])
