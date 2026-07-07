def solution(key, lock):
    m = len(key)
    n = len(lock)
    # 행을 열로. 0행을 2열로, 1행을 1열로, 2행을 0열로. -> 0행 -> n-1열, 1행 -> n-2열,. n-1행 -> 0열
    direct = [[0,1],[0,-1],[-1,0],[1,0]]
    
    def rotate(board): # 회전하기
        m = len(board)
        tmp = [[0]*m for _ in range(m)]
        for row in range(m): # 행
            for col in range(m): # 열
                tmp[col][m-row-1] = board[row][col]
        return tmp[:]
    
    # 가운데 lock 부분이 모두 1인지 확인
    def check(board):
        for i in range(n):
            for j in range(n):
                if board[i+n][j+n] != 1:
                    return False
        return True

    # 3N x 3N 보드 생성
    new_lock = [[0] * (3*n) for _ in range(3*n)]

    # 가운데에 lock 배치
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 회전 4번
    for _ in range(4):
        key = rotate(key)

        # 모든 위치에 이동
        for x in range(2*n):
            for y in range(2*n):

                # key 더하기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                # 열리는지 검사
                if check(new_lock):
                    return True

                # 원상복구
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False