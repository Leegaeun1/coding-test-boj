n = int(input())
p = list(map(int,input().split()))
s = list(map(int,input().split()))

start = p[:] # 시작 상태
right = [i%3 for i in range(n)] # 올바른 상태

cnt = 0

while True:
    if p == right: # 올바른 상태
        print(cnt)
        break

    tmp = [0] * n
    for i in range(n):
        tmp[s[i]] =p[i] # s[i]번째를 p[i]번째로

    p = tmp

    cnt += 1
    if p == start: # 시작 상태와 같아지면 -1
        print(-1)
        break