from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 1:
            graph[i+1].append(j+1)

travel = list(map(int,input().split()))

# 연결 컴포넌트 구하기
visited = [False] * (n+1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

# 첫 도시에서 시작해서 연결된 도시들 탐색
bfs(travel[0])

# 여행 계획에 있는 도시들이 모두 같은 컴포넌트인지 확인
if all(visited[city] for city in travel):
    print("YES")
else:
    print("NO")
