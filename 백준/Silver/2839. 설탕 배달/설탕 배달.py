n=int(input())
m=0
for a in range(1001):
    for b in range(1668):
        if(5*a+3*b==n):
            m=a+b
if(m==0):
    print("-1")
else:
    print(m)