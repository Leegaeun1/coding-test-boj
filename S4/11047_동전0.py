n,k = list(map(int,input().split()))
li = []
cnt = 0

for i in range(n):
    li.append(int(input()))

for i in range(n-1,-1,-1):
    if li[i] <= k:
        cnt += k //li[i]
        k %= li[i]

print(li,cnt)