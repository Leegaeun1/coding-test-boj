def solution(signals):
    answer = 0
    y_time = [] # 노란불 시간 [[시작,끝+1]]
    times = []
    period = [sum(s) for s in signals] # 각각 주기 
    length = len(signals)
    for r, y, g in signals:
        y_time.append([r+1,r+y+1])
        
    dictionary = {}
    
    for i in range(100000):
        for j in range(length):
            start, end = y_time[j]
            for s in range(start, end):
                tmp = s+period[j]*i
                if tmp not in dictionary:
                    dictionary[tmp] = 1
                else:
                    dictionary[tmp] += 1
                if dictionary[tmp] == length:
                    return tmp
            
    return -1