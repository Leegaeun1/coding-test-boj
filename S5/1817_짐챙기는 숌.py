n, max_w = map(int,input().split())
if n == 0:
    print(0)
else:
    li =list(map(int,input().split()))

    idx = 0
    m = max_w
    total = 0

    while idx < n:
        if m >= li[idx]:
            m -= li[idx]
            idx += 1
        else:
            total += 1
            m = max_w
    if m < max_w:
        total += 1

    print(total)
        