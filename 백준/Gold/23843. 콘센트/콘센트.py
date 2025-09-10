import sys,heapq
input = sys.stdin.readline

n, m = map(int,input().split())
el = list(map(int,input().split()))
el.sort(reverse=True)

con = [0] * m

for i in range(n):
    tmp = heapq.heappop(con)
    heapq.heappush(con, tmp+el[i])

print(max(con))