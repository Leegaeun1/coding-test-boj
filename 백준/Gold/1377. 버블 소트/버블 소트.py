import sys
input = sys.stdin.readline

n = int(input())
li = []
idx = []

for i in range(n):
    li.append([int(input()),i])

li.sort()

for i in range(n):
    idx.append(li[i][1] - i)

print(max(idx) + 1)