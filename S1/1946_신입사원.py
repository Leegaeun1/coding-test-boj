n = int(input())

for _ in range(n):
    num = int(input())
    li = []
    for i in range(num):
        a, b = map(int, input().split())
        li.append((a, b))

    li.sort()  # 서류 기준 정렬

    count = 1  # 첫 번째 사람은 항상 선발
    best_interview = li[0][1]

    for i in range(1, num):
        if li[i][1] < best_interview:  # 면접 점수가 더 우수하면
            count += 1
            best_interview = li[i][1]

    print(count)
