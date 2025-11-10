n,m = map(int,input().split())
li = [i for i in range(1,n+1)]

visited = [False]*n

# 1부터 n까지 중복없이 m개 고른 수열
def dfs(tmp,visited):

    if len(tmp) >= m:
        print(*tmp)
        visited = [False]*n
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(tmp+li[i:i+1],visited)
            visited[i] = False

dfs([],visited)