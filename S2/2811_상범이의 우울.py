n = int(input())
dep = list(map(int,input().split()))
flower = [0] * n # 꽃 개수

# 우울한 날이 언제 있는지 저장하기
length = 0
max_length = 0

# 날짜 리스트에서 우울 기간 x2 만큼 꽃을 채움
for i in range(n - 1, -1, -1):
    if dep[i] < 0:
        length += 1
        continue

    for j in range(0, length * 2):
        if (i - j) > -1:
            flower[i - j] = 1
    
    # 우울 기간 중 최장 기간을 구함
    max_length = max(max_length, length)
    length = 0

ans = sum(flower)

max_cnt = 0
length = 0

# 최장 우울 기간들 중에서
for i in range(n - 1, -1, -1):
    if dep[i] < 0:
        length += 1
        continue
	
    if length == max_length:
        count = 0
        # 꽃을 가장 많이 채울 수 있는 구간을 찾음
        for j in range(0, length * 3):
            if (i - j) > -1 and flower[i - j] == 0:
                count += 1
		
        # 꽃을 가장 많이 채울 수 있는 기간의 카운트 값
        if count > max_cnt:
            max_cnt = count

    length = 0

print(ans + max_cnt)