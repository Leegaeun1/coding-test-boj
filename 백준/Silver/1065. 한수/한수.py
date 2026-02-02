num = int(input())
res = [i for i in range(1,100)]

if num < 100:
    print(num)
else:
    for i in range(100,num+1):
        num_tmp = i
        tmp = []
        while i > 0:
            tmp.append(i%10)
            i //= 10
        for i in range(len(tmp)-2):
            if tmp[i] - tmp[i+1] == tmp[i+1] - tmp[i+2]:
                res.append(num_tmp)
    if num < 1000:
        print(len(res))
    else:
        print(len(res)-1)