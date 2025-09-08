n = int(input())
first = list(map(int,input().split()))
second = list(map(int,input().split()))

first.sort()
second.sort(reverse=True)
answer = 0
for i in range(n):
    answer += first[i] * second[i]

print(answer)
