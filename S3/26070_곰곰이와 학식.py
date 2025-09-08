# 치킨 a, 피자 b, 햄버거 c마리. 
# 학생식당에서 사용 가능한 치킨 x, 피자 y, 햄버거 z장. 
# 치킨 3장 -> 피자 1장, 피자 3장 -> 햄버거 1장, 햄버거 3장 -> 치킨 1장.
import sys
input = sys.stdin.readline

def use(want, have, cnt):
    # 일단 사용가능한거 사용하기
    for i in range(3):
        if want[i] > have[i]: # 원하는게 더 많으면 
            want[i] -= have[i]
            cnt += have[i]
            have[i] = 0 
        else:
            have[i] -= want[i]
            cnt += want[i]
            want[i] = 0
    return want,have,cnt


def change(want, have, cnt):
    # 남는 식권이 있으면 바꾸기.
    for i in range(3):
        if have[i] > 0:
            have[(i+1)%3] += (have[i]//3)
            have[i] -=(have[i]//3) * 3
            want,have,cnt = use(want, have, cnt)

    return want, have, cnt

def main():
    want = list(map(int, input().split()))
    have = list(map(int, input().split()))
    cnt = 0

    while True:
        if (all(have[i] < 3 for i in range(3))):
            break
        want,have,cnt = use(want, have, cnt)
        want, have, cnt = change(want, have, cnt)
        
    print(cnt)
    
main()