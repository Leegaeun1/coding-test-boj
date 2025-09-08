import sys
input = sys.stdin.readline

n, m = map(int,input().split())
li = [0] + list(map(int,input().split()))
D = [0] *(n+1)
max_money = 0

for i in range(1, n+1):
    D[i] = D[i-1] + li[i]

for i in range(0,n + 1 - m):
    if D[i+m]-D[i] > max_money:
        max_money = D[i+m]-D[i]

print(max_money)