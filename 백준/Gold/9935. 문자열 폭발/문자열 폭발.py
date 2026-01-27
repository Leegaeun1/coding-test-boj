import sys
input = sys.stdin.readline
st = input().rstrip()
boom = input().rstrip()
boom_len = len(boom)
stack = []

for ch in st:
    stack.append(ch)
    # 최근 boom_len 만큼이 boom이면 제거
    if len(stack) >= boom_len:
        if ''.join(stack[-boom_len:]) == boom:
            for _ in range(boom_len):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")