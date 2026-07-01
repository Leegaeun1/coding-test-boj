def solution(sequence):
    answer = -1
    dp1 = [0]*len(sequence)
    dp2 = [0]*len(sequence)
    dp1[0] = sequence[0]*(-1)
    dp2[0] = sequence[0]
    for i in range(1,len(sequence)):
        if i % 2 == 0:
            dp1[i] = dp1[i-1]+sequence[i]*(-1)
            dp2[i] = dp2[i-1]+sequence[i]
        else:
            dp2[i] = dp2[i-1]+sequence[i]*(-1)
            dp1[i] = dp1[i-1]+sequence[i]
    dp1 = [0] + dp1[:]
    dp2 = [0] + dp2[:]

    # 누적합 최대를 구해야함.
    min1 = dp1[0]
    min2 = dp2[0]

    for i in range(1, len(dp1)):
        answer = max(answer, dp1[i]-min1)
        answer = max(answer, dp2[i]-min2)

        min1 = min(min1, dp1[i])
        min2 = min(min2, dp2[i])
    return answer