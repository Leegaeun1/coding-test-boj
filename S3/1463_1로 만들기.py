# 3으로 나눠 떨어지면 3으로 나누기
# 2로 나눠 떨어지면 2로 나누기
# 1빼기

# 최소가 되려면 최대한 3으로 나누는게 좋음.  ==> 
# 1. 3으로 나눌수있으면 바로 나누기 + 1빼서 3의 배수 되는거면 1 빼기
# 2. 2로 나눌수있으면 2로 나누기 
# 3. 1 빼기
from collections import deque

n = int(input())
queue = deque([(n,0)])

while True:
    n,cnt = queue.popleft()
    if n % 3 == 0:
        queue.append((n//3,cnt + 1))
    if n % 2 ==0:
        queue.append((n//2,cnt + 1))

    queue.append((n-1,cnt + 1))
    
    if n == 1:
        break

print(cnt)