from queue import PriorityQueue
import sys
input = sys.stdin.readline
n = int(input())
li = []
room = PriorityQueue()

for i in range(n):
    li.append(list(map(int,input().split())))

li.sort(key= lambda x:[x[0],x[1]])
room.put(li[0][1])

for i in range(1,n):
    e = room.get()
    if e <= li[i][0]:
        room.put(li[i][1])
    else:
        room.put(li[i][1])
        room.put(e)
print(room.qsize())