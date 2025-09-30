n = int(input())
li = set()
cnt = 0

for _ in range(n):
    s = input().strip()
    if s == "ENTER":
        cnt += len(li)
        li = set()
    else:
        li.add(s)
if len(li) > 0:
    cnt += len(li)

print(cnt)