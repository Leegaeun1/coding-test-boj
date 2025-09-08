import sys
input = sys.stdin.readline

def main():   
    n = int(input())
    li = list(map(int,input().split()))
    li.sort()
    cnt = 0
    
    for k in range(n):
        find = li[k]
        s, e= 0, n-1

        while s < e:
            sum = li[s] + li[e]
            if sum == find:
                if s != k and e != k:
                    cnt += 1
                    break
                elif s == k:
                    s += 1
                elif e == k:
                    e -= 1

            elif sum < find:
                s += 1
            elif sum > find:
                e -= 1
    
    print(cnt)

main()