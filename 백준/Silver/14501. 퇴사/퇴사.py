n = int(input())
d = [0]*(n+1)

t = [0]*(n+1)
p = [0]*(n+1)

for i in range(1,n+1):
    t[i],p[i] = list(map(int,input().split()))

for i in range(1,n+1):
    if i + t[i] > n+1:
        continue
    d[i+t[i]-1] = max(max(d[:i])+p[i],d[i+t[i]-1])

print(max(d))