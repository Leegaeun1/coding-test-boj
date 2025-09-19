import sys
input = sys.stdin.readline

n, k = map(int,input().split())
tem = list(map(int,input().split()))


max_sum = sum(tem[:k])
tmp_sum = max_sum
s, e = 1, k

while e < n:
    tmp_sum -= tem[s-1]
    tmp_sum += tem[e]
    s += 1
    e += 1
    if max_sum < tmp_sum:
        max_sum = tmp_sum
print(max_sum)