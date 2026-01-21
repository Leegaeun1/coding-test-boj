import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = [[float('inf')]*n for _ in range(n)]

for _ in range(m):
    a, b, p = map(int,input().split())
    li[a-1][b-1] = min(p,li[a-1][b-1])


for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(n):
                if j != k and i != k:
                    li[j][k] = min(li[j][i] + li[i][k], li[j][k])

for i in range(n):
    for j in range(n):
        if li[i][j] == float('inf'):
            li[i][j] = 0
        print(li[i][j], end=" ")
    print()

