n = int(input())
li = list(map(int,input().split()))
stu = int(input())

for i in range(len(li)):
    if li[i] == 0:
        li[i] = False
    else:
        li[i] = True

def male(num):
    for i in range(num,len(li),num+1):
        li[i] = not li[i]

def female(num):
    f = num - 1
    e = num + 1
    li[num] = not li[num]
    while f >= 0 and e < len(li) and li[f] == li[e]:
        li[f] = not li[f]
        li[e] = not li[e]
        f -= 1
        e += 1

def solution():
    st = ''

    for _ in range(stu):
        
        s, num = list(map(int,input().split())) # 성별, 번호
        if s == 1 : # 남학생은 자신 숫자의 배수인 스위치 상태 바꿈
            male(num-1)
        else: # 여학생은 자신 숫자 스위치 중심으로 좌우 대칭인 구간 상태 바꿈 
            female(num-1)
    
    for i in range(len(li)):
        print('1' if li[i] else '0', end=' ')
        if (i + 1) % 20 == 0:  # 줄바꿈 (옵션)
            print()
        

solution()