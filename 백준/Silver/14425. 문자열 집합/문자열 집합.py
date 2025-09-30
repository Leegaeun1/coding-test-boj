n, m = map(int,input().split())
dic = []
comp = []
cnt = 0

for _ in range(n):
    dic.append(input().strip())

for _ in range(m):
    comp.append(input().strip())

for d in comp:
    if d in dic:
        cnt += 1

print(cnt)