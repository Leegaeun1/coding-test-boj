n = int(input())
electronic = []
li = []
res = 0

for _ in range(n):
    electronic.append(list(map(int,input().split())))

electronic.sort() # 정렬

for a, b in electronic:
    li.append(b)

def lis(li):
    dp = [1] * len(li)
    for i in range(len(li)):
        for j in range(i):
            if li[i] > li[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return len(li) - max(dp)

print(lis(li))