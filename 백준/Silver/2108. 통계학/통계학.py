import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
li = []
max_num = 0
max_li = []

for i in range(n):
    li.append(int(input()))

li.sort()

cnt = Counter(li)
max_count = max(cnt.values())

for c in cnt:
    if max_count == cnt[c]:
        max_li.append(c)
max_li.sort()

print(round(sum(li)/n))
print(li[n//2])

if len(max_li) == 1:
    print(max_li[0])
else:
    print(max_li[1])

print(max(li)-min(li))