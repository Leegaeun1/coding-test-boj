import heapq

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])

start, end = map(int,input().split())

distance = [float('inf')] * (n+1)
distance[start] = 0

q = []
heapq.heappush(q,(0,start))

while q:
    x, y = heapq.heappop(q) # 비용, 기준점
    if distance[y] < x: # 비용이 원래보다 작다면 필요없음
        continue
    for g in graph[y]: # 그래프에 있는거 
        cost = x + g[1]
        if distance[g[0]] > cost: # 원래 비용보다 크면 갱신 
            distance[g[0]] = cost
            heapq.heappush(q,(cost,g[0]))
    
print(distance[end])