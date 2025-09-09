import sys
n=int(sys.stdin.readline())
li=[int(sys.stdin.readline()) for i in range(n)]
li=list(set(li))
li.sort()
for i in li:
    print(i)