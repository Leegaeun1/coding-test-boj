def solution(signals):
    t = 0

    while t <= 10000000:

        ok = True

        for r,y,g in signals:
            p = r+y+g
            mod = t % p

            if not (r < mod <= r+y):
                ok = False
                break

        if ok:
            return t

        t += 1
    return -1