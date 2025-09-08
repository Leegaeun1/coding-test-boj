n = int(input())
max_weight = 0
li = []
for i in range(n):
    li.append(int(input()))

li.sort()
# 1개일때
for i in li:
    if max_weight < i:
        max_weight = i

# 2개~ n개까지 중량
for i in range(2,n+1):
    if li[-i] * i > max_weight:
        max_weight = li[-i] * i

print(max_weight)