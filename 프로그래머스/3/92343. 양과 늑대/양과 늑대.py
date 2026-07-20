def solution(info, edges):
    answer = 1
    graph = {i:[] for i in range(len(info))}
    for x, y in edges:
        graph[x].append(y)
    able = []
    def dfs(stand, wolf, sheeps, able):
        nonlocal answer
        
        if len(able) == 0: # 가능한 노드가 없다,
            return

        for x in able:
            new_able = able[:]
            new_able.remove(x) # 해당 노드는 빼기
            new_able.extend(graph[x]) # 자식 노드 추가하기 
            
            if info[x] == 0: # 양
                answer = max(answer, sheeps + 1)
                dfs(x, wolf, sheeps + 1, new_able)
            else: # 늑대
                if wolf + 1 < sheeps: # 양보다 적어야 갈 수 있음.
                    dfs(x, wolf + 1, sheeps, new_able)
        
        
    dfs(0, 0, 1, graph[0])            
    return answer