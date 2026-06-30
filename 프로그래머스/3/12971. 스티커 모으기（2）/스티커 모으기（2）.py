def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    dp1 = sticker[:-1]
    dp2 = sticker[1:]

    
    for i in range(1,len(dp1)):
        if i == 1:
            dp1[i] = max(dp1[i-1],dp1[i])
        else:
            dp1[i] = max(dp1[i-1],dp1[i-2]+dp1[i])
    for i in range(1,len(dp2)):
        if i == 1:
            dp2[i] = max(dp2[i-1],dp2[i])
        else:
            dp2[i] = max(dp2[i-1],dp2[i-2]+dp2[i])
            
    return max(max(dp1),max(dp2))