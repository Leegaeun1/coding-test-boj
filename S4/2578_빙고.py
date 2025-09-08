# 빙고 판을 채우기
# 사회자가 부르는수 지워나가기. 몇번째에 3개 빙고하는지?
bingo = []
talk = []
new= []
isFind = False

def init(): # 빙고판 초기화 및 사회자가 부르는 수 정리
    for _ in range(10):
        if _ < 5:
            bingo.append(list(map(int,input().split())))
        else:
            new.append(list(map(int,input().split())))
    for i in new:
        for j in i:
            talk.append(j)

def isbingo():
    isBingo = 0
    # 가로 빙고
    for i in range(5):
        ok = True
        for j in range(5):
            if bingo[i][j] != 0:
                ok = False
                break
        if ok:
            isBingo += 1

    # 세로 빙고
    for j in range(5):
        ok = True
        for i in range(5):
            if bingo[i][j] != 0:
                ok = False
                break
        if ok:
            isBingo += 1

    # 대각선 
    ok = True
    for i in range(5):
        if bingo[i][i] != 0:
            ok = False
            break
    if ok:
        isBingo += 1

    # 대각선 
    ok = True
    for i in range(5):
        if bingo[i][4 - i] != 0:
            ok = False
            break
    if ok:
        isBingo += 1

    return isBingo
    
def solution():
    for t in range(25):
        isFind = False
        for i in range(5):
            for j in range(5):
                if talk[t] == bingo[i][j]:
                    bingo[i][j] = 0
                    isFind = True
                    break
            if isFind:
                break
        if isbingo() >= 3:
            print(t+1)
            break

init()
solution()
