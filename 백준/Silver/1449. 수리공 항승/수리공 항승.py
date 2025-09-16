n, l = map(int,input().split())
li = list(map(int,input().split()))
tape = []
cnt = 0
li.sort()

for i in li:
    if len(tape) == 0:
        tape = [i,i+l]
        cnt += 1
    else:
        if i < tape[0]  or i >= tape[1]:
            cnt += 1
            tape = [i,i+l]
print(cnt)
