N, r, c = map(int,input().split())

n = 2 ** N
cnt = 0

def conq(x, y, n):
    global cnt
    if x == r and y == c:
        print(cnt)
        exit()
    if n == 1:
        cnt += 1
        return
    half = n//2
    if not(x<=r<x+n and y<=c<y+n):
        cnt += n*n 
        return

    
    conq(x,y,half)
    conq(x,y+half,half)
    conq(x+half,y,half)
    conq(x+half,y+half,half)

conq(0,0,n)