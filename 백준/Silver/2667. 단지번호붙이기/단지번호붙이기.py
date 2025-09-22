from collections import deque

n = int(input())
graph = []
visited = [[False]*n for _ in range(n)]
direct = [[0,1],[0,-1],[1,0],[-1,0]]
res = 0
li = []

for i in range(n):
    graph.append(list(map(int,input())))

def bfs(graph,x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    cnt = 0

    while queue:
        x,y = queue.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = True
                queue.append((nx,ny))
    
    return cnt

for i in range(n):
    for j in range(n):
        cnt = 1
        flag = False
        if not visited[i][j] and graph[i][j] == 1:
            cnt += bfs(graph,i,j)
            res += 1
            flag = True
            li.append(cnt)
print(res)
li.sort()
for i in li:
    print(i)