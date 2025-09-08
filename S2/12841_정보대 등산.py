import sys
input = sys.stdin.readline

n = int(input())
cross =  list(map(int,input().split()))
left = [0] + list(map(int,input().split()))
right = [0] + list(map(int,input().split()))
min_total = float("inf")
min_idx = -1
for i in range(1, n):
    left[i] += left[i-1]
    right[i] += right[i-1]

for c in range(n):
    # 왼쪽 먼저
    le_f = left[c] + (right[n-1] -right[c]) + cross[c]

    if min_total > le_f:
        min_idx = c + 1
        min_total = le_f

print(min_idx,min_total)