def solution(n, times):
    left = 1
    right = max(times) * n # 최대 시간!

    answer = right

    while left <= right:
        mid = (left + right) // 2

        # mid 시간 동안 처리 가능한 사람 수
        total = 0
        for t in times:
            total += mid // t

        # 가능하면 시간 줄여보기
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer