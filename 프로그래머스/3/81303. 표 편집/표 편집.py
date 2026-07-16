def solution(n, k, cmd):
    answer = ['O']*n
    # 삭제될 때 [위치] <- 추가
    # 복구 시 여기서 빼서 위치에 insert 하기 
    # current = 행 idx . 첨엔 k -> 삭제하고 난뒤 아래 행 선택. 만약 마지막이면 윗행 선택.
    # 처음꺼 순서대로 저장하고 삭제된것만 X 처리하면 됨. 
    delete = []
    current = k # 현재 행
    
    prev = [i-1 for i in range(n)] # 이전 행
    next = [i+1 for i in range(n)] # 다음 행
    next[-1] = -1
    
    for c in cmd:
        tmp = c.split()
        if tmp[0] == "C": # 지우기
            # 삭제 정보를 저장
            delete.append((current, prev[current], next[current]))

            # 연결 끊기
            if prev[current] != -1:
                next[prev[current]] = next[current]

            if next[current] != -1:
                prev[next[current]] = prev[current]

            # 현재 위치 이동
            if next[current] != -1:
                current = next[current]
            else:
                current = prev[current]
            
        elif tmp[0] == "Z": # 되돌리기
            node, p, nnode = delete.pop()

            if p != -1:
                next[p] = node

            if nnode != -1:
                prev[nnode] = node

            prev[node] = p
            next[node] = nnode 
            
        elif tmp[0] == "U": # X칸 위에 있는 행 선택
            x = int(tmp[1])
            for _ in range(x):
                current = prev[current]
                
        elif tmp[0] == "D": # X칸 아래에 있는 행 선택
            x = int(tmp[1])
            for _ in range(x):
                current = next[current]
            
    while delete:
        node, _, _ = delete.pop()
        answer[node] = 'X'

    return ''.join(answer)