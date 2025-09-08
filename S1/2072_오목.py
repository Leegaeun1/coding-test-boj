# 19 * 19 바둑판에서 진행
# 승패가 갈리는게 몇번째 수인지? 없으면 -1
# 홀수는 흑, 짝수는 백 

li = [[-1]*19 for _ in range(19)]
n = int(input())

dirs = [(1,0),(0,1),(1,1),(1,-1)]  # 가로, 세로, 대각선 

def isFinish(x,y,color):
    for dx,dy in dirs:
        cnt = 1
        # 정방향
        nx, ny = x+dx, y+dy
        while 0 <= nx < 19 and 0 <= ny < 19 and li[nx][ny] == color:
            cnt += 1
            nx += dx
            ny += dy
        # 역방향
        nx, ny = x-dx, y-dy
        while 0 <= nx < 19 and 0 <= ny < 19 and li[nx][ny] == color:
            cnt += 1
            nx -= dx
            ny -= dy
        if cnt == 5:
            return True
    return False


# 진행 
def main():
    for i in range(n):
        x,y = map(int,input().split())
        if i % 2 == 0: # 흑
            li[x-1][y-1] = 0
            color = 0
        else: # 백
            li[x-1][y-1] = 1
            color = 1
        if isFinish(x-1,y-1,color):
            print(i+1)
            return
    print("-1")

main()