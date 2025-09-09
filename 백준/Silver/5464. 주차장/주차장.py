import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
R = [int(input()) for _ in range(n)]  # 주차 요금 단위
W = [int(input()) for _ in range(m)]  # 차량 무게

empty = list(range(n))  # 비어 있는 자리 (0 ~ n-1)
heapq.heapify(empty)

waiting = []            # 대기열
pos = [-1] * m          # 각 차가 어디에 있는지
money = 0

for _ in range(2*m):
    x = int(input())

    if x > 0:  # 차량 들어옴
        car = x-1
        if empty:  # 빈자리 있으면
            spot = heapq.heappop(empty)
            pos[car] = spot
        else:     # 빈자리 없으면 대기
            waiting.append(car)

    else:  # 차량 나감
        car = -x-1
        spot = pos[car]
        money += R[spot] * W[car]
        pos[car] = -1
        heapq.heappush(empty, spot)

        # 대기차 있으면 즉시 배치
        if waiting:
            nxt = waiting.pop(0)
            spot = heapq.heappop(empty)
            pos[nxt] = spot

print(money)
