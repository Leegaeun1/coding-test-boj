from collections import defaultdict,deque

def solution(n, edge):
    answer = 0
    
    depth = defaultdict(int)
    depth[1] = 1
    
    nodes = defaultdict(list)
    for a, b in edge:
        nodes[a].append(b)
        nodes[b].append(a)
    
    visited = [False]*(n+1)
    visited[1] = True
    queue = deque([(1,1)]) # 노드번호, depth
    
    while queue:
        node, dep = queue.popleft()
        
        for x in nodes[node]:
            if not visited[x]:
                queue.append((x,dep+1))
                depth[dep+1] += 1
                visited[x] = True
    return depth[len(depth)]