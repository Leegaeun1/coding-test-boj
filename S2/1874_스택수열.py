n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

num = 1 # 오름차순 숫자
tmp,new_li = [],[] # 임시로 저장할 스택, li처럼 만들 스택
idx = 0 # 기준 인덱스 
res = [] # +, - 값을 저장할 리스트

while idx < n:
    if len(tmp) == 0:  # 비어있으면 무조건 넣기 
        tmp.append(num)
        res.append("+")
        num += 1
        continue
    if num <= n: # 도달하고자하는 숫자 전까지
        if tmp[-1] == li[idx]: # 빼내야하는 수와 같으면 빼서 새로운 스택에 저장
            new_li.append(tmp.pop())
            idx += 1
            res.append("-")
        else: # 다르면 계속 추가
            tmp.append(num)
            num += 1
            res.append("+")
    else: # 도달하고자하는 숫자에 도달했으면 빼내기 
        new_li.append(tmp.pop())
        res.append("-")
        idx += 1

if li != new_li: # 만들수없으면 NO 
    print("NO")
else:
    for i in res:
        print(i)