n = int(input())
stack = []

for _ in range(n):
    st = input().split()
    if len(st) == 2:
        stack.append(int(st[-1]))
    else:
        if st[0] == "top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        elif st[0] == "size":
            print(len(stack))
        elif st[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif st[0] == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())