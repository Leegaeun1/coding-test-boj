s, p = map(int, input().split())
st = input()
st_cnt = list(map(int, input().split()))  # [A, C, G, T] 최소 요구 개수
res = 0

# 현재 윈도우 문자 개수
cur_cnt = [0, 0, 0, 0]

# 문자 → 인덱스 매핑
idx = {"A": 0, "C": 1, "G": 2, "T": 3}

# 초기 윈도우 채우기
for i in range(p):
    cur_cnt[idx[st[i]]] += 1

# 조건 만족 확인 함수
def check():
    for i in range(4):
        if cur_cnt[i] < st_cnt[i]:
            return False
    return True

if check():
    res += 1

# 슬라이딩 윈도우
for i in range(p, s):
    # 새로 들어온 문자
    cur_cnt[idx[st[i]]] += 1
    # 빠져나간 문자
    cur_cnt[idx[st[i - p]]] -= 1

    if check():
        res += 1

print(res)
