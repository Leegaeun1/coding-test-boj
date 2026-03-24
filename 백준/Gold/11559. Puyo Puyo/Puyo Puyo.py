from collections import deque
board = []
puyo = []
direct = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(12):
    tmp = list(input())
    for j in range(6):
        if tmp[j] != '.':
            puyo.append([i,j])
    board.append(tmp)

def bfs(r,c,visited):
    queue = deque([(r,c)])
    target = board[r][c]
    cnt =1
    li = [[r,c]]
    while queue:
        r, c = queue.popleft()
        for x, y in direct:
            dx = r + x
            dy = c + y
            if 0 <= dx < 12 and 0 <= dy < 6 and not visited[dx][dy] and board[dx][dy] == target:
                queue.append([dx,dy])
                li.append([dx,dy])
                visited[dx][dy] = True
                cnt += 1
    #print(cnt)
    if cnt <= 3:
        return False,board,visited 
    else:
        #print(li)
        for x, y in li:
            while (1 <= x < 12 and 0 <= y < 6) and board[x][y] != '.':
                #print(x,y)
                board[x][y] = board[x-1][y]
                x -= 1
            if board[x][y] != '.':
                board[x][y] = '.'
        return True,board,visited 
    
res = 0
prev = -1
#print(puyo)
while prev != res:
    prev = res
    visited = [[False]*6 for _ in range(12)]
    puyo = []
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                puyo.append([i,j])

    #print(puyo)
    tmp = 0
    for x, y in puyo:
        if not visited[x][y]:
            #print(x,y,'임')
            visited[x][y] = True
            flag, board,visited =bfs(x,y,visited)
            if flag:
                #print(board)
                tmp += 1
    if tmp > 0:
        res += 1
    #print(prev)

print(res)