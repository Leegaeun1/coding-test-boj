n = int(input())
li = []
min_dp = [[0]*3 for _ in range(2)]
max_dp = [[0]*3 for _ in range(2)]


li.append(list(map(int,input().split())))

min_dp[0] = li[0]
max_dp[0] = li[0]

if n == 1:
    print(max(li[-1]),min(li[-1]))
    exit()

for i in range(1,n):
    li = list(map(int,input().split()))
    min_dp[1][0] = min(min_dp[0][0],min_dp[0][1]) + li[0]
    min_dp[1][1] = min(min_dp[0][0],min_dp[0][1],min_dp[0][2]) + li[1]
    min_dp[1][2] = min(min_dp[0][1],min_dp[0][2]) + li[2]
    max_dp[1][0] = max(max_dp[0][0],max_dp[0][1]) + li[0]
    max_dp[1][1] = max(max_dp[0][0],max_dp[0][1],max_dp[0][2]) + li[1]
    max_dp[1][2] = max(max_dp[0][1],max_dp[0][2]) + li[2]
    #print(min_dp,max_dp)
    min_dp[0] = min_dp[1][:]
    max_dp[0] = max_dp[1][:]


print(max(max_dp[-1]), min(min_dp[-1]))