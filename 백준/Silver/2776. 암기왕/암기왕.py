import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    note_one = set(map(int, input().split()))
    m = int(input())
    note_two = list(map(int, input().split()))

    for x in note_two:
        if x in note_one:
            print(1)
        else:
            print(0)
