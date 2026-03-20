from collections import deque

N = int(input())
sea = [] # 바다
baby = [] # 아기 상어 위치,크기
direct = [[0,1],[0,-1],[1,0],[-1,0]]
eat_fish = 0
time = 0

for r in range(N):
    tmp = list(map(int,input().split()))
    for c in range(N):
        if tmp[c] == 9:
            baby = [r,c,2]
            tmp[c] = 0
    
    sea.append(tmp)

def bfs():
    r,c,size = baby

    queue = deque([(r,c,0)])
    visited = [[False]*N for _ in range(N)]
    visited[r][c] = True
    min_dis = float('inf')
    min_pos = [float('inf'),float('inf')]
    while queue:
        r, c, dis = queue.popleft()
        if dis > min_dis: # 이미 가까운거 찾으면 스킵
            continue

        for x, y in direct:
            dx = r + x
            dy = c + y
            if 0 <= dx < N and 0 <= dy < N:
                if not visited[dx][dy] and sea[dx][dy] <= size:
                    visited[dx][dy] = True

                    if 0 < sea[dx][dy] < size: # 먹을 수 있음
                        if dis + 1 < min_dis: # 최소 갱신
                            min_dis = dis + 1
                            min_pos = [dx, dy]
                        elif dis + 1 == min_dis: # 같으면 행 우선
                            if dx < min_pos[0] or (dx == min_pos[0] and dy < min_pos[1]):
                                min_pos = [dx, dy]

                    queue.append((dx,dy,dis+1))
    if min_dis == float('inf'):
        return -1, [-1, -1]
    
    return min_dis, min_pos # 최소 거리, 위치

def move():
    global time
    min_dis, min_pos = bfs()

    if min_dis == -1:   # 더 이상 먹을 물고기 없음
        return False
    
    sea[min_pos[0]][min_pos[1]] = 0 
    baby[0], baby[1] = min_pos
    #print(min_dis)
    time += min_dis
    return True

def eat():
    global eat_fish
    if eat_fish == baby[2]:
        baby[2] += 1
        eat_fish = 0
    if not move(): # 더 못움직임
        return False
    eat_fish += 1
    return True
    

while True:
    if not eat():
        print(time)
        break
