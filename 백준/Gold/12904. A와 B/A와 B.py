alp = input()
res = input()

while len(alp) < len(res):
    if res[-1] == "A":
        res= res[:-1]
    else:
        res = res[:-1]
        res = res[::-1]

if alp == res:
    print(1)
else:
    print(0)