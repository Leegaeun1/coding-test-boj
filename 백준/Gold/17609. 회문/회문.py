def is_palin(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def check(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if is_palin(s, left + 1, right) or is_palin(s, left, right - 1):
                return 1
            else:
                return 2
        left += 1
        right -= 1
    return 0

n = int(input())
for _ in range(n):
    print(check(input()))
