dic = {"c=":1,"c-":1,"dz=":1,"d-":1,"lj":1,"nj":1,"s=":1,"z=":1}

st = input()
idx = 0
n = len(st)
li = [False] * n
total = 0

while idx < n:
    tmp = st[idx:idx+2]
    if tmp == "dz" and idx + 2 <= n:
        if st[idx:idx+3] == "dz=":
            idx += 3
            li[idx:idx+3] = [True] * 3
            total+=1
            continue
    if dic.get(tmp,0) == 1:
        li[idx:idx+2] = [True] * 2
        idx += 2
    else:
        li[idx] = True
        idx += 1
    total+=1
print(total)