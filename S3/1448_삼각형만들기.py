import sys
input = sys.stdin.readline  # 반복 input()보다 훨씬 빠름

def main():
    n = int(input())
    num = []

    for i in range(n):
        num.append(int(input()))

    num.sort(reverse=True)
    for i in range(n-2):
        a, b, c = num[i], num[i+1],  num[i+2]
        if a < b + c:
            print(a+b+c)
            return
        
    print(-1)
    return

main()
