n, k = map(int,input().split())
li = []
dp = [float('inf')]*(100001)
dp[0] = 0

for _ in range(n):
    li.append(int(input()))

for i in li:
    dp[i] = 1

for i in range(2,k+1):
    for coin in li:
        if i >= coin:
            dp[i] = min(dp[i],dp[i-coin]+1)
    #print(dp[:k+1])
    

if dp[k] != float('inf'):
    print(dp[k])
else:
    print(-1)
