import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def cal():
    p = input().strip()
    n = int(input())
    arr = input().strip()

    # [] 처리
    if n == 0:
        dq = deque()
    else:
        dq = deque(map(int, arr[1:-1].split(',')))

    rev = False  # 뒤집기 여부
    for cmd in p:
        if cmd == 'R':
            rev = not rev
        elif cmd == 'D':
            if not dq:
                return "error"
            if rev:
                dq.pop()
            else:
                dq.popleft()

    if rev:
        dq.reverse()

    return "[" + ",".join(map(str, dq)) + "]"

for _ in range(t):
    print(cal())
