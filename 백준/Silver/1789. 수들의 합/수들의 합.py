n= int(input())
num = 1
cnt = 0
while n >= num:
    n -= num
    num += 1
    cnt += 1
print(cnt)