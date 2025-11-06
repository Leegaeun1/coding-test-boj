n = int(input())

def iscorrect(st):
    stack = []
    for i in range(len(st)):
        if st[i] == "(":
            stack.append(st[i])
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

for _ in range(n):
    st = input()
    if iscorrect(st):
        print("YES")
    else:
        print("NO")