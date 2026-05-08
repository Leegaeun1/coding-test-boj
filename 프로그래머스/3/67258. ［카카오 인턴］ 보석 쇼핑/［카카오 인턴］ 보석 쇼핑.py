from collections import defaultdict

def solution(gems):
    total = len(set(gems))

    dic = defaultdict(int)

    left = 0
    answer = [0, len(gems) - 1]

    for right in range(len(gems)):
        dic[gems[right]] += 1 # 오른쪽으로 이동!

        # 모든 종류 포함하면
        while len(dic) == total:
            # 더 짧은 구간 갱신
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

            # 왼쪽 축소
            dic[gems[left]] -= 1

            if dic[gems[left]] == 0: # 존재 X
                del dic[gems[left]]

            left += 1

    return [answer[0] + 1, answer[1] + 1]