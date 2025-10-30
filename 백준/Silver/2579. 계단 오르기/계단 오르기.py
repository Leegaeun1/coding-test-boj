n = int(input())
d = [[0,0] for _ in range(n)]

for i in range(n):
    now = int(input())
    if i < 2:
        if i == 0:
            d[i] = [0,now]
        else:
            d[i] = [now,now+d[0][1]]
    else:
        d[i] = [max(d[i-2]) + now , d[i-1][0] + now]
    
print(max(d[-1]))