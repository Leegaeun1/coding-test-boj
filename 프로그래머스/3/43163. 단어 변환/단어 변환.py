min_res = float('inf')

def dfs(stand,target,cnt,visited,words):
    global min_res
    #print('-------기준-----------',stand)
    if stand == target:
        #print('같음',cnt)
        min_res = min(min_res,cnt)
    if cnt > len(words): # 깊이 벗어남
        return
    for i in range(len(words)):
        diff = 0
        if not visited[i]: # 방문 X
            #print(i,'번째')
            for t in range(len(stand)):
                if stand[t] != words[i][t]:
                    diff += 1
            if diff == 1:# 1개만 다름
                #print('1개',words[i])
                visited[i] = True
                dfs(words[i],target,cnt+1,visited,words)
                visited[i] = False

        

def solution(begin, target, words):
    answer = 0
    visited = [False]*len(words)
    if target not in words: # 단어안에 없으면
        return 0
    dfs(begin,target,0,visited,words)
    if min_res == float('inf'):
        return 0
    return min_res