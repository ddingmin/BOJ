def solution(numbers):
    answer = [-1] * len(numbers)
    
    stack = []
    for i in range(len(numbers)):
        if not stack or numbers[i] <= stack[-1][1]:
            stack.append([i, numbers[i]])
        else:
            while stack and numbers[i] > stack[-1][1]:
                a, b = stack.pop()
                answer[a] = numbers[i]
            stack.append([i, numbers[i]])
        
    return answer