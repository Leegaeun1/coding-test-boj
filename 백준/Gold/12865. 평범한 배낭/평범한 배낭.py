n, k = map(int, input().split())
items = []
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    v, w = map(int, input().split())
    items.append((w, v)) # 무게, 가치

for i in range(1, n + 1):        # 물건
    v, w = items[i - 1]
    for j in range(1, k + 1):    # 무게
        if w > j: # 최대 배낭 무게보다 크면 
            dp[i][j] = dp[i - 1][j]   # 이전 물건 그대로
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w]) # 선택 O, 선택 X

print(dp[n][k])   # 최대 가치
