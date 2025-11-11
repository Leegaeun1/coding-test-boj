n = int(input())
max_c,max_r = 0,0
xy = []
cnt = 0

for i in range(n):
    p, q = map(int,input().split())
    max_c = max(max_c,p+10)
    max_r = max(max_r,q+10)
    xy.append([q,p])

li = [[False]*max_c for _ in range(max_r)]

for x,y in xy:
    for dx in range(x,x+10):
        for dy in range(y,y+10):
            li[dx][dy] = True
for i in li:
    cnt += i.count(True)
print(cnt)