import sys,heapq
input = sys.stdin.readline

n = int(input())
li = []
room = []

for i in range(n):
    num, s, e = map(int,input().split())
    heapq.heappush(li,[s,e])

for i in range(n):
    s, e = heapq.heappop(li)
    if len(room) == 0:
        heapq.heappush(room,e)
    else:
        room_e = heapq.heappop(room)
        if room_e <= s:
            heapq.heappush(room,e)
        else:
            heapq.heappush(room,room_e)
            heapq.heappush(room,e)
    #print(room, li)
print(len(room))