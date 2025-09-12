import sys
input = sys.stdin.readline

n = int(input())
dic = {}
li = list(map(int,input().split()))

for i in range(n):
    dic[li[i]] = 1

m = int(input())
tmp = list(map(int,input().split()))

for i in range(m):
    num = dic.get(tmp[i],0)
    print(num,end=" ")