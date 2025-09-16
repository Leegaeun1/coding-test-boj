a, b = map(int,input().split())
cnt = 1

while a < b:
    if b % 2 == 0:
        b //= 2 
    else:
        st = str(b)
        if st[-1] == "1":
            st = st[:-1]
        else:
            break
        b = int(st)
    cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)