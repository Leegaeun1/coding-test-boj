n = int(input())
c, s = 100, 100

for _ in range(n):
    sc, ss = list(map(int,input().split()))
    if sc < ss:
        c -= ss
    elif sc > ss:
        s -= sc

print(c)
print(s)