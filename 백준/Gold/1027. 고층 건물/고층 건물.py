n = int(input())
building_height = [0] + list(map(int,input().split()))

res = [0] * (n+1)

for x1 in range(1,n+1):
    for x2 in range(x1+1,n+1):
        y1, y2 = building_height[x1], building_height[x2]
        flag = True
        for k in range(x1+1,x2):
            f = ((y2-y1)/(x2-x1))*(k-x1) + y1
            
            if building_height[k] >= f:
                flag = False
        if flag:     
            res[x1] += 1
            res[x2] += 1

print(max(res))