from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def solution():
    n, k = map(int,input().split())
    time = list(map(int,input().split()))
    
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    dp = [0]*(n+1)  # 해당 건물까지 걸리는 최대 시간
    
    for _ in range(k):
        x, y = map(int,input().split())
        graph[x].append(y)
        indegree[y] += 1
    
    target = int(input())
    
    queue = deque()
    
    # 진입차수 0 초기화
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = time[i-1]
    
    while queue:
        now = queue.popleft()
        for next_node in graph[now]:
            indegree[next_node] -= 1

            dp[next_node] = max(dp[next_node], dp[now] + time[next_node-1])
            
            if indegree[next_node] == 0:
                queue.append(next_node)
    
    return dp[target]

for _ in range(t):
    print(solution())