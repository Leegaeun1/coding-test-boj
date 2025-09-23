from collections import deque

n, k = map(int,input().split())
visited = set()

def bfs(n):
    queue = deque([(n,0)])
    visited.add(n)
    res = 0
    flag = False
    min_cnt = float('inf')

    while queue:
        x, cnt = queue.popleft()
        visited.add(x)
        if flag:
            if min_cnt < cnt:
                return [min_cnt,res]
        
        if x == k:
            min_cnt = min(min_cnt,cnt)
            if min_cnt == cnt:
                flag = True
                res += 1

        if x*2 not in visited and x < k or x*2 == k :
            queue.append((x*2,cnt+1))
        if x-1 not in visited and x > 0 or x-1 == k :
            queue.append((x-1,cnt+1))
        if x+1 not in visited and x < k or x+1 == k:
            queue.append((x+1,cnt+1))
    return [min_cnt,res]

cnt, res = bfs(n)
print(cnt)
print(res)