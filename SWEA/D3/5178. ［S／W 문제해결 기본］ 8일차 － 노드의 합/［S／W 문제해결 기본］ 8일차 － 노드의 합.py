# n까지 node만들어서 자식 노드 저장
T = int(input())

for i in range(1,T+1):
    n, m, l = map(int, input().split())
    node = {idx:[] for idx in range(1,n+1)} # 자식 노드 저장하는 곳
    total = {idx:0 for idx in range(1,n+1)} # 합 저장하는 곳
    for j in range(m): # m번 반복
        child, cost = map(int,input().split())
        total[child] = cost
    if n == 1:
        print(f"#{i} {total[i]}")
        continue
    t, n_idx = 2, 1
    while t < n + 1: # node에 자식 노드 저장
        node[n_idx].append(t)
        t += 1
        if t == n+1:
            break
        node[n_idx].append(t)
        t += 1
        n_idx += 1

    # 노드의 합 저장
    for t_idx in range(n,0,-1):
        if len(node[t_idx]) > 0:
            for c in node[t_idx]:
                total[t_idx] += total[c]
    print(f"#{i} {total[l]}")