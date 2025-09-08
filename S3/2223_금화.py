# 금화를 주머니에 담을때 소리 -> 몬스터가움직임. -> 주워담는거 멈추면 다시 원래의 자리로 돌아감. 
# t단위동안 금화주워담을수 있음, 이동안 x개 담을수있음. 
# m개의 몬스터, d만큼의 거리에 위치, 단위시간동안 s만큼움직임. 

# 몬스터들 중 하나라도 다음턴에 플레이어에게 닿을것 같다면 멈추기-> 몬스터 원래 위치로 돌아감.


def main():
    t, x, m = map(int,input().split())
    if m == 0: # 몬스터 없으면..
        print(t * x)
        return

    minV = float('inf')
    for _ in range(m):
        d, s = map(int, input().split())
        # 안전하게 금화 담을 수 있는 최대 시간
        minV = min(minV, (d - 1) // s)

    if minV <= 0:
        print(0)
    elif t <= minV:
        print(t * x)
    else:
        print((minV + (t - minV) // 2) * x)

main()
