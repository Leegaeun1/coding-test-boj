n = int(input())
no = 0

for _ in range(n):
    dic = {}
    st = list(input())
    for i in range(len(st)):
        if st[i] in dic:
            if dic[st[i]] + 1 == i:
                dic[st[i]] += 1
            else:
                no += 1
                break
        else:
            dic[st[i]] = i
print(n-no)
    