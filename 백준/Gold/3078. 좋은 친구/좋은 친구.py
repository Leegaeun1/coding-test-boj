import sys
input = sys.stdin.readline

n, k = map(int, input().split())

groups = [[] for _ in range(21)]  # 이름 길이 최대 20

for i in range(n):
    name_len = len(input().strip())
    groups[name_len].append(i)

res = 0

for g in groups:
    left = 0
    for right in range(len(g)):
        # 범위 벗어나면 left 이동
        while g[right] - g[left] > k:
            left += 1
        # right 기준으로 가능한 개수 추가
        res += right - left

print(res)
