import sys,heapq
input= sys.stdin.readline

n, m = map(int,input().split())
heap = list(map(int,input().split()))
heapq.heapify(heap)

for i in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap,x+y)
    heapq.heappush(heap,x+y)

print(sum(heap))