n = int(input())
w, h = [0]*n, [0]*n 
min_w, min_h = [0]*n, [0]*n 
cnt = [1] * n

for i in range(n):
    w[i],h[i] = map(int,input().split())

for i in range(n):
    for j in range(n):
        if w[i] > w[j]:
            min_w[i] += 1
        if h[i] > h[j]:
            min_h[i] += 1

for i in range(n):
    for j in range(n):
        if min_w[i] < min_w[j] and min_h[i] < min_h[j]:
            cnt[i] += 1

print(*cnt)