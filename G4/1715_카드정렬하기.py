import heapq

n = int(input())
heap = []
if n == 0:
    print(0)

for i in range(n):
    heapq.heappush(heap,int(input()))

total = 0
while len(heap) > 1:
    #제일 작은거 꺼내서 두개 꺼내서 합친거 다시 넣기
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    total += a + b
    heapq.heappush(heap,a+b)

print(total)