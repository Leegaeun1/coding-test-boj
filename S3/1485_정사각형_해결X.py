def dot(p1,p2,p3,p4):
    a = [p2[0]-p1[0],p2[1]-p1[1]]
    b = [p4[0]-p3[0],p4[1]-p3[1]]
    return a[0]*b[0] + a[1]*b[1]

n = int(input())

for i in range(n):
    li = []
    for _ in range(4):
        li.append(list(map(int,input().split())))
    
    if dot(li[0],li[1],li[2],li[3]) == 0:
        print(1)
    elif dot(li[0],li[2],li[1],li[3]) == 0:
        print(1)
    elif dot(li[0],li[3],li[1],li[2]) == 0:
        print(1)
    else:
        print(0)
