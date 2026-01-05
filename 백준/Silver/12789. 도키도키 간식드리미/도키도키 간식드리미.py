n = int(input())
li = list(map(int,input().split()))
tmp = []

num = 1

while True:
    if num == n:
        print("Nice")
        break
    if num in li:
        while True:
            p = li.pop(0)
            if p == num:
                num += 1
                break
            else:
                tmp = [p] + tmp
    else:
        if tmp[0] == num:
            tmp.pop(0)
            num += 1
        else:
            print("Sad")
            break
        