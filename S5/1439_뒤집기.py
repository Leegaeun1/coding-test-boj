# 1과 0의 처음 인덱스의 갯수/2가 답임
num = input()
cri = "-1"
li = []

for n in num:
    if n != cri:
        li.append(n)
        cri = n

print(len(li)//2)