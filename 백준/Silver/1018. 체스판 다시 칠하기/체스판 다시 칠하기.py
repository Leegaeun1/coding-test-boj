from collections import deque
import copy

n, m = map(int,input().split())

checkBoard = []
direct = [[0,1],[0,-1],[1,0],[-1,0]]
min_res = float('inf')

for _ in range(n):
    checkBoard.append(list(input()))

def bfs(a,b,ch):
    res = 0
    check = copy.deepcopy(checkBoard)
    if check[a][b] != ch:
        check[a][b] = ch
        res += 1
    queue = deque([(a,b)])
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for nx, ny in direct:
            dx = x + nx
            dy = y + ny
            if a <= dx < a+8 and b <= dy < b+8:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    if check[x][y] == check[dx][dy]:
                        if check[dx][dy] == "B":
                            check[dx][dy] = "W"  
                        else:
                            check[dx][dy] = "B"
                        res += 1
                    queue.append((dx,dy))
    return res 

for i in range(n-7):
    for j in range(m-7):
        res1 = bfs(i,j,"W")
        res2 = bfs(i,j,"B")
        min_res = min(min_res,res1,res2)

print(min_res)
