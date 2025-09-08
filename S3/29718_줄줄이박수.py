import sys
input = sys.stdin.readline

n, m = map(int,input().split())
col_sum = [0] * (m+1)

for i in range(n):
    tmp = [0] + list(map(int,input().split()))
    for j in range(1, m+1):
        col_sum[j] += tmp[j]

for i in range(1,m+1):
    col_sum[i] += col_sum[i-1]

max_clap = 0
a = int(input())

for i in range(m-a+1):
    sum = col_sum[i+a] - col_sum[i] 
    max_clap = max(sum, max_clap)

print(max_clap)