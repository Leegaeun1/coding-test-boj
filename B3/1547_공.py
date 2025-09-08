m=int(input())
dic = {1:0,2:1,3:2}
for i in range(m):
    x,y=map(int,input().split())
    f,s = dic[x],dic[y]
    dic[x],dic[y] = s,f

for i in dic:
    if dic[i] == 0:
        print(i)


