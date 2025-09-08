n, m = map(int,input().split())
li = [0] + list(map(int,input().split()))

for i in range(1, n+1):
    li[i] += li[i-1] 

s, e= 0, n
min_len = float("inf")

while s < n:
    sum = li[e] - li[s]
    #print(sum, e, s)
    if sum >= m:
        min_len = min(min_len,e-s)
        e -= 1
    else:
        s += 1
        e += 1
    if e == n+1:
        e -= 1

if min_len == float("inf"):
    min_len = 0

print(min_len)