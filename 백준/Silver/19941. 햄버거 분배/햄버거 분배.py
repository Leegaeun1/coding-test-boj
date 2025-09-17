n, k = map(int,input().split())
line = list(input())
cnt = 0

for i in range(n):
    if line[i] == "P":
        idx_min = max(i-k,0)
        idx_max = min(i+k,n-1)

        while idx_min <= idx_max:
            if line[idx_min] == "H":
                line[idx_min] = "G"
                cnt += 1
                break
            idx_min += 1
           
print(cnt)