import sys
input = sys.stdin.readline

m, n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
res = []
a.sort()
b.sort()

a_st, b_st = 0, 0

while b_st < len(b) and a_st < len(a):    
    if a[a_st] < b[b_st]:
        res.append(a[a_st])
        a_st += 1
    elif a[a_st] > b[b_st]:
        b_st += 1
    else:
        a_st += 1
        b_st += 1

while a_st < len(a):
    res.append(a[a_st])
    a_st += 1

new = list(set(res))
le = len(new)
print(le)
new.sort()
print(*new)