import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 
party = [] # 각 파티에 참여 사람

def find(x):
    if parent[x] != x: # 루트노드와 다르면
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

# 부모 초기화
for i in range(1, n+1):
    parent[i] = i

# 진실 아는 사람 입력
real = list(map(int, input().split()))
if real[0] == 0:
    real = []
else:
    real = real[1:]

# 파티 입력
for _ in range(m):
    tmp = list(map(int, input().split()))
    party.append(tmp[1:])

# 같은 파티 사람들 union
for p in party:
    for i in range(len(p)-1):
        union(p[i], p[i+1])

# 진실 아는 사람 root 저장
real_root = set(find(x) for x in real)

# 거짓말 가능한 파티 카운트
cnt = 0
for p in party:
    can_lie = True
    for person in p:
        if find(person) in real_root:
            can_lie = False
            break
    if can_lie:
        cnt += 1

print(cnt)