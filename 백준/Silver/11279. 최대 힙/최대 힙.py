import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
queue = PriorityQueue()

for i in range(n):
    x = int(input())

    if x == 0:
        if queue.empty():
            print("0")
        else:
            print(str(-queue.get()))
    else:
        queue.put(-x)