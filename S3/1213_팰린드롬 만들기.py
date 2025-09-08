name = input()
alpha,num = [],[]
new = ['0'] * len(name) # 새로운 리스트를 만들어서 '0'으로 초기화하기. 

# 각 알파벳을 alpha에 저장. 중복 X
for i in name:
    if i in alpha:
        num[alpha.index(i)] += 1 # 갯수를 num에 저장. 
    else:
        alpha.append(i)
        num.append(1)

for i in range(len(alpha)-1):
    for j in range(i+1, len(alpha)):
        if alpha[i] > alpha[j]:
            alpha[i], alpha[j] = alpha[j], alpha[i]
            num[i], num[j] = num[j], num[i]
idx = 0
odd = 0

for i in num:
    if i%2==1:
        odd+=1


if odd > 1:
    print("I'm Sorry Hansoo") # 홀수개인거 
else:
    for i in range(len(alpha)):
        while num[i] > 0:
            if num[i] == 1:
                
                new[len(name)//2] = alpha[i]
                num[i] -= 1
            else:
                new[idx] = alpha[i]
                new[-idx-1] = alpha[i]
                num[i] -= 2
                idx += 1
    print(''.join(new))