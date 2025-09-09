n=int(input())

li=[str(input()) for i in range(n)]
li=list(set(li))
li.sort()
li.sort(key=len)
for i in li:
    print(i)


