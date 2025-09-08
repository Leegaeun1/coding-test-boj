n,m = list(map(int,input().split()))
li = [_ for _ in range(1,n+1)]

for i in range(m):
    i,j = list(map(int,input().split()))
    li[i-1],li[j-1] = li[j-1],li[i-1]

for s in li:
    print(s,end=' ')