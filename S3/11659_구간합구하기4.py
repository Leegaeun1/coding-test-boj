import sys
input = sys.stdin.readline
n,m = map(int,input().split())

li = list(map(int,input().split()))
sum_li = [0]

for i in range(n):
    sum_li.append(sum_li[i] + li[i])

for i in range(m):
    i, j = map(int,input().split())
    print(sum_li[j]-sum_li[i-1])