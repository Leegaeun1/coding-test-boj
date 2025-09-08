n,m = list(map(int,input().split()))
li = [0]*n
st = ''
for i in range(m):
    i,j,k = list(map(int,input().split()))
    for idx in range(i,j+1):
        li[idx-1] = k
    
for s in li:
    st += str(s) + ' '

print(st[:-1])