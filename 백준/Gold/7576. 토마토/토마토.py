from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int,input().split())
li = []
one_idx = [] # 익은 토마토 위치 저장
visited = [[False] * m for _ in range(n)]
direct = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(m):
        if tmp[j] == 1:
            one_idx.append([i,j])
    li.append(tmp)

def bfs(li,one_idx):
    queue = deque()
    for x,y in one_idx:
        queue.append((x,y,0))
        visited[x][y] = True
    max_cnt = 0  
    while queue:
        x, y, cnt = queue.popleft()
        max_cnt = max(max_cnt, cnt)  # 가장 마지막 날 저장
        for dx, dy in direct:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and li[nx][ny] == 0:
                visited[nx][ny] = True
                li[nx][ny] = 1
                queue.append((nx,ny,cnt + 1))
            
    return max_cnt

def main(li):
    cnt = bfs(li,one_idx)
    for i in li:
        if i.count(0) > 0:
            print(-1)
            return
            
    print(cnt)

main(li)
