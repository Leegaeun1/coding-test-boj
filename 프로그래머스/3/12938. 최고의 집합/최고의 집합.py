def solution(n, s):
    if n > s:
        return [-1]
    if n == s:
        return [1]*n
    if n == 2:
        return [s//n,s-s//n]
    stand = s // n # 기준
    div = s % n # 남은것
    answer = [stand]*n
    for i in range(div):
        answer[i] += 1
    answer.sort()
    return answer