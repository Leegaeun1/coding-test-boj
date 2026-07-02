def solution(s):
    answer = 0
    for i in range(len(s)+1):
        #print(i)
        for j in range(i+1,len(s)+1):
            tmp = s[i:j]
            #print(j,s[i:j],tmp[::-1])
            if s[i:j] == tmp[::-1]: # 앞 뒤 같음
                #print(i,j)
                answer = max(answer,len(s[i:j]))

    return answer