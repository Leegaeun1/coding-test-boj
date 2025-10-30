n = int(input())
d = [0] * 1000
d[0] = 1
d[1] = 2

for i in range(2,1000):
    d[i] = d[i-1] + d[i-2]

print(d[n-1]%10007)