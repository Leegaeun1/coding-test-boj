from collections import deque

def solution(stones, k):
    # k 크기 윈도우에서 최댓값들 중 최솟값 찾기
    dq = deque()
    result = float('inf')
    
    for i in range(len(stones)):
        # 윈도우 크기 유지
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # 현재 값보다 작은 인덱스 제거 (최댓값 유지)
        while dq and stones[dq[-1]] < stones[i]:
            dq.pop()
        
        dq.append(i)
        
        # 윈도우가 k 크기가 되면 최댓값 확인
        if i >= k - 1:
            result = min(result, stones[dq[0]])
    
    return result