def solution(board, skill):
    n = len(board)
    m = len(board[0])

    # 누적합 배열
    acc = [[0] * (m + 1) for _ in range(n + 1)]

    # 스킬 적용
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1: # 공격
            degree = -degree
        acc[r1][c1] += degree
        acc[r1][c2 + 1] -= degree
        acc[r2 + 1][c1] -= degree
        acc[r2 + 1][c2 + 1] += degree

    # 가로 누적합
    for i in range(n + 1):
        for j in range(1, m + 1):
            acc[i][j] += acc[i][j - 1]

    # 세로 누적합
    for j in range(m + 1):
        for i in range(1, n + 1):
            acc[i][j] += acc[i - 1][j]

    # board에 적용하면서 정답 계산
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + acc[i][j] > 0:
                answer += 1

    return answer