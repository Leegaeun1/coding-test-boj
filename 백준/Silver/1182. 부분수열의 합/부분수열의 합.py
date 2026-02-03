n, s = map(int,input().split())

li = list(map(int,input().split()))
cnt = 0

def dfs(x,sum):
    global cnt
        
    if x == n:
        if sum == s:
            cnt += 1
        return
    dfs(x+1, sum+li[x]) # 더함 
    dfs(x+1, sum) # 안 더함 


dfs(0,0)

if s == 0:
    cnt -= 1

print(cnt)