n = int(input())
cnt = 1
s,e = 1, 1
sum = 1

while e != n:
    if sum < n:
        e += 1
        sum += e
    elif sum == n:
        cnt += 1
        e += 1
        sum += e
    elif sum > n:
        sum -= s
        s += 1
    

print(cnt)