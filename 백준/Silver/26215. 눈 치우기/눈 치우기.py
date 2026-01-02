import heapq

n = int(input())
tmp = list(map(int,input().split()))
h = []
for i in tmp:
    heapq.heappush(h,-i)

ans = 0

while len(h) > 1:
    f = -(heapq.heappop(h))
    s = -(heapq.heappop(h))
    ans += s
    if f-s > 0:
        heapq.heappush(h,-(f-s))
    
if len(h) == 1:
    ans += -(heapq.heappop(h))

if ans > 1440:
    print(-1)
else:
    print(ans)