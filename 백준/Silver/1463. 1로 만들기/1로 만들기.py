from collections import deque

n = int(input())
queue = deque([(n,0)])

while True:
    n,cnt = queue.popleft()
    if n % 3 == 0:
        queue.append((n//3,cnt + 1))
    if n % 2 ==0:
        queue.append((n//2,cnt + 1))

    queue.append((n-1,cnt + 1))
    
    if n == 1:
        break

print(cnt)