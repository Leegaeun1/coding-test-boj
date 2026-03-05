l, c = map(int,input().split())
alp = list(input().split())
alp.sort()
tmp = []
v = ['a','e','i','o','u']

visited = [False] * len(alp)

def dfs(li):
    if len(li) == l:
        tmp.append(li)
        #print(li)
        return
    
    for a in range(len(alp)):
        if not visited[a]:
            visited[a] = True
            if len(li) == 0 or len(li) > 0 and li[-1] <= alp[a]:
                dfs(li+[alp[a]])
            visited[a] = False

dfs([])


for l in tmp:
    v_cnt = 0
    w_cnt = 0
    for i in l:
        if i in v:
            v_cnt += 1
        else:
            w_cnt += 1
    if v_cnt >= 1 and w_cnt >=2:
        print(''.join(l))