n,m = list(map(int,input().split()))
li = [_ for _ in range(1,n+1)]

for _ in range(m):
    i,j = list(map(int,input().split()))
    fir = i - 1
    end = j - 1
    while fir < end:
        
        li[fir],li[end] = li[end],li[fir]
        fir += 1
        end -= 1
for s in li:  
    print(s,end= ' ')