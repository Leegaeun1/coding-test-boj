def solution(user_id, banned_id):
    result = set()

    # 매칭 체크 함수
    def check(user, banned):
        if len(user) != len(banned):
            return False
        for i in range(len(user)):
            if banned[i] == '*':
                continue
            if user[i] != banned[i]:
                return False
        return True

    def dfs(bid, visited):
        # 모든 banned_id를 다 매칭한 경우
        if bid == len(banned_id):
            selected = []
            for i in range(len(user_id)):
                if visited[i]:
                    selected.append(user_id[i])
            
            # 순서 제거 위해 정렬 후 tuple
            result.add(tuple(sorted(selected)))
            return

        for i in range(len(user_id)):
            if not visited[i] and check(user_id[i], banned_id[bid]):
                visited[i] = True
                dfs(bid + 1, visited)
                visited[i] = False

    dfs(0, [False] * len(user_id))
    return len(result)