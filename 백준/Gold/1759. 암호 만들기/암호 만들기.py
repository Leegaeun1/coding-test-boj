l, c = map(int, input().split())
alp = sorted(input().split())

vowels = {'a', 'e', 'i', 'o', 'u'}

def dfs(start, path):
    if len(path) == l:
        v_cnt = 0
        for ch in path:
            if ch in vowels:
                v_cnt += 1
        
        if v_cnt >= 1 and l - v_cnt >= 2:
            print(''.join(path))
        return

    for i in range(start, c):
        dfs(i + 1, path + [alp[i]])

dfs(0, [])