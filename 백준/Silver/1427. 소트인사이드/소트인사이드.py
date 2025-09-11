n = input()
li = []

for i in range(len(n)):
    li.append(int(n[i]))

for i in range(len(n)):
    max_idx = i
    for j in range(i+1,len(n)):
        if li[j] > li[max_idx]:
            max_idx = j
    li[i], li[max_idx] = li[max_idx], li[i]

for i in li:
    print(str(i),end="")