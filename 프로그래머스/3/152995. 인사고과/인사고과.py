from collections import defaultdict

def solution(scores):
    answer = -1
    wanho = scores[0][:] # 완호

    total = defaultdict(list)
    total_tmps = []

    for i in range(len(scores)):
        scores[i].append(i) # 인덱스 추가

    scores.sort(key=lambda x: (x[0], -x[1])) # 앞은 오름차순, 뒤는 내림차순 

    max_second = 0

    # 뒤에서부터 확인
    for i in range(len(scores)-1, -1, -1):
        first, second, idx = scores[i]

        # 인센티브 제외
        if second < max_second:
            if idx == 0:      # 완호가 제외되면
                return -1
            continue

        max_second = max(max_second, second)

        s = first + second
        total[s].append(idx)
        total_tmps.append(s)

    total_tmps.sort(reverse=True)
    #print(total, total_tmps)
    rank = 1
    for s in range(len(total_tmps)):
        if 0 in total[total_tmps[s]]:
            #print(1)
            return s+1
        #rank += len(total[s])

    return answer