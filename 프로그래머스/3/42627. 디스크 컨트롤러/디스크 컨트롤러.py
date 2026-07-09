import heapq

def solution(jobs):
    jobs.sort()      # 요청 시간 기준 정렬

    heap = []        # (소요시간, 요청시간)
    time = 0
    answer = 0
    idx = 0
    n = len(jobs)

    while idx < n or heap: # 작업 다했거나 heap 안에 있거나 

        # 현재 시간까지 도착한 작업 모두 heap에 추가
        while idx < n and jobs[idx][0] <= time: # idx가 범위안 + 현재 시간보다 이하여야함.
            start, remain = jobs[idx]
            heapq.heappush(heap, (remain, start))
            idx += 1

        if heap: # heap이 비어있지 X 
            remain, start = heapq.heappop(heap)

            time += remain                 # 작업 수행
            answer += time - start         # 반환시간 = 종료 - 요청

        else:
            # 아직 도착한 작업이 없으면 시간을 다음 요청 시각으로 이동
            time = jobs[idx][0]

    return answer // n