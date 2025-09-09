n = int(input())
li = input()
li = li.split(" ")
for i in range(n):
    li[i] = int(li[i])
li.sort()

sum = 0
total = 0
for i in li:
    sum += i
    total += sum
print(total)