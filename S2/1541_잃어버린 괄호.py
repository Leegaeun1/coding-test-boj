n = input()
total = 0
num_list = n.split("-")
f = list(map(int,num_list[0].split("+")))
total += sum(f)
    
for i in range(1,len(num_list)):
    f = list(map(int,num_list[i].split("+")))
    total -= sum(f)
print(total)
