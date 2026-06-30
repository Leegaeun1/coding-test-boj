from collections import deque
def solution(n, roads, sources, destination):
    answer = [float('inf')] * n
    answer[destination-1] = 0
    ans = []
    # 다익스트라. 최단거리! destination부터 시작하고 가장 작은것부터 탐색하기
    graph = [[] for _ in range(n+1)]
    
    for x, y in roads:
        graph[x] += [y]
        graph[y] += [x]
    
    # 기준부터 시작.
    def bfs(graph,destination):
        visited = [False]*n
        queue = deque([(destination-1)])
        visited[destination-1] = True
        
        while queue:
            v = queue.popleft()
            for i in graph[v+1]: # 방문안함
                if not visited[i-1]:
                    queue.append(i-1)
                    visited[i-1] = True
                    answer[i-1] = min(answer[i-1],answer[v]+1)

    bfs(graph,destination)
    for s in sources:
        if answer[s-1] == float('inf'):
            ans.append(-1)
        else:
            ans.append(answer[s-1])
    return ans