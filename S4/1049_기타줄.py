n, m = list(map(int,input().split()))
li = []
total = 0

for i in range(m):
    li.append(list(map(int,input().split())))

price_list = sorted(li) # 패키지 가격기준 정렬
indiv_list = sorted(li,key = lambda x:x[1]) # 개별 가격기준 정렬

while n > 0:
    total += min(price_list[0][0],indiv_list[0][1]*(min(6,n)))
    n -= 6

print(total)