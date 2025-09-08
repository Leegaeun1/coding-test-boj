n = int(input())
li = []

for i in range(n):
    num = int(input())
    if num != 0:
        li.append(num)
    else:
        li.pop()

print(sum(li))