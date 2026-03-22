from collections import deque
n, m = map(int,input().split())
board = []
direct = [[0,1],[0,-1],[1,0],[-1,0]]


def isrange(x, y):
    if 0 <= x < n and 0 <= y < m and board[x][y] !='#':
        return True
    return False
    
def move(dx,dy,r_r,r_c,b_r,b_c):
    prev = [r_r,r_c,b_r,b_c]
    isfin = False
    blue_hole = False
    while True:
        red_move = True
        blue_move = True
        r_r += dx
        r_c += dy
        if isrange(r_r, r_c)==False or [r_r,r_c] == [b_r,b_c]: # 움직이지 못함
            r_r -= dx
            r_c -= dy
            red_move = False
        elif hole == [r_r,r_c]:
            isfin = True
            r_r += dx
            r_c += dy
            
        
        b_r += dx
        b_c += dy
        if isrange(b_r, b_c)==False or [r_r,r_c] == [b_r,b_c]:# 움직이지 못함
            b_r -= dx
            b_c -= dy
            blue_move = False
        elif hole == [b_r,b_c]:
            blue_hole = True
            break
        
        if not blue_move and not red_move: # 못 움직임
            break
        if prev == [r_r,r_c,b_r,b_c]:
            break
        prev = [r_r,r_c,b_r,b_c]
    return r_r,r_c,b_r,b_c,isfin,blue_hole

def main():
    queue = deque([(red[0],red[1],blue[0],blue[1],0)])
    visited = set()
    min_res = float('inf')
    
    while queue:
        r_r,r_c,b_r,b_c,cnt = queue.popleft()
        upper = False
        
        if cnt > 10: # 10 이상이면 x
            if min_res == float('inf') or min_res == 11:
                upper = True
            break
        if (r_r,r_c,b_r,b_c) not in visited:
            for dx, dy in direct: # 상하좌우
                if (isrange(r_r+dx, r_c+dy) and board[r_r+dx][r_c+dy] != '#') or (isrange(b_r+dx, b_c+dy) and board[b_r+dx][b_c+dy] !='#'):
                    rr,rc,br,bc,isfin,blue_hole = move(dx,dy,r_r,r_c,b_r,b_c)
                    #print(rr,rc,br,bc,isfin,cnt+1,dx,dy)
                    
                    if isfin and not blue_hole:
                        min_res = min(min_res,cnt+1)
                    if not blue_hole:
                        queue.append([rr,rc,br,bc,cnt+1])
            visited.add((r_r,r_c,b_r,b_c))
    if min_res > 0 and min_res != float('inf') and not upper:
        print(min_res)
    else:
        print(-1)
    
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == 'B':
            blue = [i,j]
        elif tmp[j] == 'R':
            red = [i,j]
        elif tmp[j] == 'O':
            hole = [i,j]
    board.append(tmp)

main()