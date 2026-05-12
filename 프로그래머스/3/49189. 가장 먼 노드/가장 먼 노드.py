from collections import defaultdict, deque

def solution(n, edge):
    nodes = defaultdict(list)

    # 그래프 저장
    for a, b in edge:
        nodes[a].append(b)
        nodes[b].append(a)

    # 각 노드까지 거리 저장
    depth = [-1] * (n + 1)
    depth[1] = 0

    queue = deque([1])

    # BFS
    while queue:
        node = queue.popleft()

        for x in nodes[node]:
            if depth[x] == -1:   # 방문 안 한 경우
                depth[x] = depth[node] + 1
                queue.append(x)

    max_depth = max(depth)

    return depth.count(max_depth)