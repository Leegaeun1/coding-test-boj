import heapq
import sys
input = sys.stdin.readline
n = int(input())
li = []
room = []

for i in range(n):
    li.append(list(map(int,input().split())))

li.sort(key= lambda x:[x[0],x[1]])
heapq.heappush(room,li[0][1])

for i in range(1,n):
    e = heapq.heappop(room)
    if e <= li[i][0]:
        heapq.heappush(room,li[i][1])
    else:
        heapq.heappush(room,li[i][1])
        heapq.heappush(room,e)
print(len(room))