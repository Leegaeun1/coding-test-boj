import sys
input = sys.stdin.readline

n = int(input())
crain = list(map(int, input().split()))
crain.sort(reverse=True)

m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

# 제일 무거운 박스를 가장 센 크레인도 못 들면 불가능
if crain[0] < box[0]:
    print(-1)
    exit()

positions = [0] * n       # 각 크레인이 확인할 박스 인덱스
checked = [False] * m     # 박스 처리 여부
cnt = 0
move = 0

while move < m:
    for i in range(n):  # 각 크레인마다
        while positions[i] < m:
            if not checked[positions[i]] and crain[i] >= box[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                move += 1
                break
            positions[i] += 1
    cnt += 1

print(cnt)
