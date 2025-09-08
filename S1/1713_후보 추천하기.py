m = int(input())
li = []

n = int(input())
num = list(map(int,input().split()))

for i in range(n):   
    inside = False
    if len(li) < m : # m개까지는 삭제할필요 X
        for j in range(len(li)):
            if li[j][1] == num[i]: # 동일한것이 있으면 횟수 추가
                li[j][0]+=1
                inside = True
                break
        if inside == False: # 새로운 학생이면 추천횟수, 번호, 들어온 순서를 저장함
            li.append([1,num[i],i])
    else: # 후보가 다 찼을 때
        for j in range(m):
            if li[j][1] == num[i]:
                li[j][0]+=1
                inside = True
                break
        if inside == False:
            li.pop(0) # 가장 추천횟수 적은 후보+ 오래된 후보 삭제
            li.append([1,num[i],i])
            
    li.sort(key=lambda x:[x[0],x[2]]) # 추천횟수 순서로 오름차순 후 2순위로 들어온순서로 정렬
    
li.sort(key=lambda x:x[1]) # 후보번호를 오름차순으로 정렬
for i in li:
    print(i[1],end=" ")