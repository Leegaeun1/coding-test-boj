a, b, c = map(int,input().split())

def power(a, b, c):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % c
            b -= 1
        a = (a * a) % c
        b //= 2
    return res

def power2(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = power2(a, n // 2)
        return (half * half) % c
    else:
        half = power2(a, (n - 1) // 2)
        return (half * half * a) % c
    
print(power2(a,b)%c)