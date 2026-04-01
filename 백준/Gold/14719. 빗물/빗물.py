h, w = map(int, input().split())
height = list(map(int, input().split()))

result = 0

for i in range(h):
    block = False
    cnt = 0
    for j in range(w):
        if height[j] > i:
            result += cnt
            cnt = 0
            block = True
        else:
            if block:
                cnt += 1

print(result)