import heapq

n = int(input())
li = []
ans = 0
for _ in range(n):
    li.append(int(input()))

if n == 1:  # 후보 1명이면 끝
    print(0)
else:
    # li[1:]을 최대 힙처럼 사용하기 위해 부호 반전
    new_li = [-x for x in li[1:]]
    heapq.heapify(new_li)

    while li[0] <= -new_li[0]:  # 가장 큰 값과 비교
        max_val = -heapq.heappop(new_li)  # 최대값 꺼냄
        max_val -= 1                      # 한 표 줄이기
        ans += 1
        li[0] += 1                        # 내 표 하나 늘리기
        heapq.heappush(new_li, -max_val)   # 다시 최대 힙에 넣기

    print(ans)
