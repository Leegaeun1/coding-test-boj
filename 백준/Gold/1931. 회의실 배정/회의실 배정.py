n = int(input())
room = []

for i in range(n):
    room.append(list(map(int,input().split())))

room.sort(key = lambda x:[x[1],x[0]])
time = 0
cnt = 0

for r in room:
    s, e = r
    if time <= s:
        time = e
        cnt += 1
        

print(cnt)