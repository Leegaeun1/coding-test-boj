import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = [0] * m
prefix = 0

cnt[0] = 0

for x in numbers:
    prefix = (prefix + x) % m
    cnt[prefix] += 1 # 누적합이 같은것의 개수 증가

res = cnt[0] # 나머지가 0인 경우

for c in cnt:
    res += c * (c - 1) // 2 # 같은 나머지가 나온 개수가 C일때 만들 수 있는 쌍의 개수

print(res)
