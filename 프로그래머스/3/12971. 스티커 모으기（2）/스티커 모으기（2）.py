def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    def repeat(dp):
        for i in range(1,len(dp)):
            if i == 1:
                dp[i] = max(dp[i-1],dp[i])
            else:
                dp[i] = max(dp[i-1],dp[i-2]+dp[i])
        return dp
    dp1 = repeat(sticker[:-1])
    dp2 = repeat(sticker[1:])

    

    return max(max(dp1),max(dp2))