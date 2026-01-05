n, k = map(int,input().split())

li = [i for i in range(1,n+1)]
res = []
i = 0

while len(res) < n :
    if i % k != k - 1:
        li.append(li[i])
    else:
        res.append(li[i])
    i+= 1

st = "<"
for i in res:
    st += str(i) + ', '
st = st[:-2]+">"

print(st)
    