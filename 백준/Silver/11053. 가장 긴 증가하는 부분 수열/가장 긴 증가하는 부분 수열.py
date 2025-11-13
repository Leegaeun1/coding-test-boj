n = int(input())
d = [1] * n
li = list(map(int,input().split()))

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if li[i] > li[j]:
            d[i] = max(d[j]+1,d[i])
print(max(d))