def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        if len(stack) == 0:
            stack.append([i,numbers[i]])
        else:
            while True:
                if stack and (stack[-1][1] >= numbers[i]):
                    stack.append([i,numbers[i]])
                    break
                else:
                    if stack:
                        idx,num = stack.pop()
                        answer[idx] = numbers[i]
                        
                    else:
                        stack.append([i,numbers[i]])
                        break
    
    return answer