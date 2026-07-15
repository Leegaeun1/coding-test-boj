def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)

    # 첫 번째 점수 오름차순, 두 번째 점수 내림차순
    scores.sort(key=lambda x: (x[0], -x[1]))

    max_second = 0
    rank = 1

    # 뒤에서부터 탐색
    for first, second in reversed(scores):

        # 인센티브 대상 제외
        if second < max_second: # 뒤에꺼보다 작음
            if [first, second] == wanho:
                return -1
            continue

        max_second = max(max_second, second)

        # 완호보다 점수 합이 높으면 순위 증가
        if first + second > wanho_sum:
            rank += 1

    return rank