from collections import defaultdict
def solution(n, costs):
    answer = 0
    li = [float('inf') for _ in range(n)]
    visited = [False]*n
    # 0 : [[1,1]] 이런식으로 dic에 저장
    dic = defaultdict(list)
    for a,b,co in costs:
        dic[a].append([b,co])
        dic[b].append([a,co])

    stand = 0 # 첫번째 기준!
    for i in dic:
        if len(dic[i]) > 0: # 개수가 0이아닌 처음
            stand = i
            li[i] = 0
            break
    
    for _ in range(n):
        for b,co in dic[stand]:
            if not visited[b]: # 확정 X
                if li[b] > co: # li에 저장된 값 > cost이면 저장!
                    li[b] = co
        visited[stand] = True # 확정!
        tmp = float('inf')
        for i in range(n):
            if not visited[i]: # 확정 X 중 가장 작은 값을 stand로 갱신
                if tmp > li[i]:
                    stand = i
                    tmp = li[i]
                
    return sum(li)