import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li.sort(key=lambda x:abs(x))
dp = [0] * (n+1)

diff = float('inf')
res = []

for i in range(n):
    dp[i+1] = dp[i] + li[i]
              
for i in range(2,n+1):
    num = dp[i] - dp[i-2]
    if abs(num) < abs(diff):
        diff = num
        res = [li[i-2],li[i-1]]

res.sort()
print(*res)