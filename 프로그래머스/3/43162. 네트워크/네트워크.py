def solution(n, computers):
    parent = [i for i in range(n)]
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if rank[x] < rank[y]: # 높이가 더 높은쪽에 붙임
            parent[x] = y
        elif rank[x] > rank[y]: # 높이가 더 높은쪽에 붙임
            parent[y] = x
        else: # 높이가 같음. 암데나 붙임
            parent[y] = x
            rank[x] += 1

    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i != j and computers[i][j] == 1:
                union(i, j)

    return len(set(parent))