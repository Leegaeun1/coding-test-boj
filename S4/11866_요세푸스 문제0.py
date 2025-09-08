# 모두 제거될때까지 k번째 사람 제거. 
from collections import deque

n, k = map(int,input().split())
queue = deque(range(1,n+1))
ans = []
st='<'

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

for i in ans:
    st += str(i)+", "

st = st[:-2]+">"
print(st)