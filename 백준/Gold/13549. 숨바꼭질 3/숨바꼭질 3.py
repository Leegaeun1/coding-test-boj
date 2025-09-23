from collections import deque

n, k = map(int,input().split())
visited = set()

def bfs(n):
    queue = deque([(n,0)])
    visited.add(n)

    while queue:
        x, cnt = queue.popleft()
        
        if x == k:
            return cnt
        if x*2 not in visited and x < k:
            queue.append((x*2,cnt))
            visited.add((x*2))
        if x-1 not in visited:
            queue.append((x-1,cnt+1))
            visited.add(x-1)
        if x+1 not in visited and x < k:
            queue.append((x+1,cnt+1))
            visited.add(x+1)

print(bfs(n))