n = int(input())
li = list(map(int, input().split()))

up = [1] * n # 뒤가 더 큼
down = [1] * n # 앞이 더 큼

for i in range(n-1):
    if li[i] >= li[i+1]:
        down[i+1] += down[i]

for i in range(n-1):
    if li[i] <= li[i+1]:
        up[i+1] += up[i]

print(max(max(down),max(up)))