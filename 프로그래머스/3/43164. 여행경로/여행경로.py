def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)

    def dfs(cur, path):
        # 모든 티켓 사용
        if len(path) == len(tickets) + 1:
            return path

        for i in range(len(tickets)):
            start, end = tickets[i]

            if not visited[i] and start == cur:
                visited[i] = True

                result = dfs(end, path + [end])

                if result:   # 정답 찾으면 바로 반환
                    return result

                visited[i] = False

    return dfs("ICN", ["ICN"])