n = int(input())

if n == 1:
    print(1)
else:
    d = [0] * n
    d[0], d[1] = 1, 3
    for i in range(2, n):
        d[i] = d[i-1] + d[i-2] * 2
    print(d[-1] % 10007)