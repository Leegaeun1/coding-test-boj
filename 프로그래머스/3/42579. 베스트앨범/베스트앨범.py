def solution(genres, plays):
    answer = []
    cnt_dict = {}
    idx_dict = {}
    for g in range(len(genres)):
        if genres[g] not in cnt_dict:
            cnt_dict[genres[g]] = plays[g]
            idx_dict[genres[g]] = [[plays[g],g]]
        else:
            cnt_dict[genres[g]] += plays[g]
            idx_dict[genres[g]].append([plays[g],g])

    while cnt_dict:
        max_total = 0
        max_g = ''
        for g in cnt_dict:
            if max_total < cnt_dict[g]: # 젤 큰거 
                max_total = cnt_dict[g]
                max_g = g
        del cnt_dict[max_g] # 젤 큰거 삭제
        idx_dict[max_g].sort(key=lambda x:[-x[0],x[1]]) # 정렬
        
        answer.append(idx_dict[max_g][0][1])
        if len(idx_dict[max_g]) > 1:
            answer.append(idx_dict[max_g][1][1])
    return answer