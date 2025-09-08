n , m , k = map(int,input().split())
stairs = [[0] for i in range(n)]
res = 0

for i in range(n):
    stairs[i] +=list(map(int,input()))

for i in range(n): # 누적합으로 좌석 갯수..
    for j in range(1,m+1):
        stairs[i][j] += stairs[i][j-1]

# 각 행마다 되는곳있는지
for i in range(n):
    for j in range(m-k+1):
        if stairs[i][j+k] - stairs[i][j] == 0:
            res += 1

print(res)