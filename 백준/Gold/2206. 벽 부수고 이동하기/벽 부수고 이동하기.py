from collections import deque

n, m = map(int,input().split())
li = []
direct = [[0,1],[0,-1],[1,0],[-1,0]]
res = float('inf')

for i in range(n):
    li.append(list(map(int,input())))
    
def bfs():
    cnt = 1
    queue = deque([(0,0,0,cnt)])
    visited = [[[False]*2 for _ in range(m)]for _ in range(n)]
    visited[0][0][0] = True

    while queue:
        x, y,broken, cnt = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt
        
        for nx, ny in direct:
            dx = x + nx
            dy = y + ny
            if 0 <= dx < n and 0 <= dy < m:
                # 안깸. 그냥 이동
                if li[dx][dy] == 0 and not visited[dx][dy][broken] :
                    visited[dx][dy][broken] = True
                    queue.append((dx,dy,broken,cnt+1))
                elif broken == 0 and li[dx][dy] == 1:
                    visited[dx][dy][1] = True
                    queue.append((dx,dy,1,cnt+1))
    
    return -1

print(bfs())