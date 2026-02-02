num = 1
no = []
real = num

while real < 10000:
    tmp = real
    s = real
    while tmp > 0:
        s += tmp % 10
        tmp //= 10

    if s not in no:
        no.append(s)
    real+=1
no.sort()

for i in range(1,10000):
    if i not in no:
        print(i)