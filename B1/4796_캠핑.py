cnt = 0
while True:
    cnt += 1
    l,p,v = list(map(int,input().split()))
    if l == 0 and p == 0 and v ==0:
        break

    print(f"Case {cnt}: {v//p * l + (v- (l* (v//p)))%l}")