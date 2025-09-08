import sys
input = sys.stdin.readline

n, m = map(int,input().split())
A = [0] + list(map(int,input().split()))
D = [0] * (n+1)
cnt = 0

# 구간합 구하기
for i in range(1,n+1):
    D[i] = D[i-1] + A[i]

s, e = 0, 0

while e <= n:
    current = D[e] - D[s]

    if current == m:
        cnt += 1
        e += 1   # 오른쪽 확장
    elif current < m:
        e += 1   # 합이 부족 → 오른쪽 확장
    else:
        s += 1   # 합이 초과 → 왼쪽 줄이기

print(cnt)