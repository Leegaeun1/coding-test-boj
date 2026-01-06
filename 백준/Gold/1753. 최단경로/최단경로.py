import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
dist = [float('inf')] * (v+1)

for _ in range(e):
    u, v2, w = map(int, input().split())
    graph[u].append((v2, w))

pq = []
dist[k] = 0
heapq.heappush(pq, (0, k))

while pq:
    cur_dist, cur = heapq.heappop(pq)

    # 이미 더 짧은 경로 있으면 스킵
    if cur_dist > dist[cur]:
        continue

    for nxt, w in graph[cur]:
        nd = cur_dist + w
        if nd < dist[nxt]:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

for i in range(1, v+1):
    print(dist[i] if dist[i] != float('inf') else "INF")
