li = []
num = 0
idx = 0
for i in range(3):
    tmp = input()
    li.append(tmp)
    if tmp.isdigit():
        num = int(tmp)
        idx = i

next_num = num + 3-idx 

if next_num % 3 == 0 and next_num % 5 == 0:
    print("FizzBuzz")
elif next_num % 3 == 0 and next_num % 5 != 0:
    print("Fizz")
elif next_num % 3 != 0 and next_num % 5 == 0:
    print("Buzz")
else:
    print(next_num)