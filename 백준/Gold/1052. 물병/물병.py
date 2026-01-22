import sys
input = sys.stdin.readline

def solution():
    buy = 0
    n, k = map(int,input().split())
    li = []

    if n <= k:
        print("0")
        return
    li.append([2,n//2])
    if n % 2 == 1:
        li.append([1,1])
    
    while True:
        a, b =li[0]
        if b <= 0:
            break
        li[0] = [a*2,b//2]
        if b % 2 == 1:
            li.append([a,1])
    li.sort(reverse=True)

    while True:
        cnt = 0
        for x, y in li:
            cnt += y
        
        if cnt <= k:
            break
        if li[-1][0] != li[-2][0]:
            f, s = li.pop()
            buy += f
            #print(f,buy)
            li.append([f*2,1])
        else:
            f, s = li.pop()
            li[-1] = [f*2,1]

    print(buy)
solution()
