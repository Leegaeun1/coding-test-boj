n = int(input())
card = {}
card_list = []

for _ in range(n):
    num = int(input())
    if num in card:
        card[num] += 1
    else:
        card[num] = 1

for c in card:
    card_list.append([c,card[c]])

card_list.sort(key = lambda x:x[1], reverse=True)

max = card_list[0][1]
res = float('inf')

for c in card_list:
    if max == c[1]:
        res = min(res,c[0])

print(res)