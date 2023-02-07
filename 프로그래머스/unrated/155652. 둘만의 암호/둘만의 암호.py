def convert(c, index, jump):
    for i in range(len(jump)):
        if jump[i] == c:
            return jump[(i + index) % len(jump)]

def solution(s, skip, index):
    jump = []
    for i in range(ord('a'), ord('z') + 1):
        flag = True
        for j in range(len(skip)):
            if skip[j] == chr(i):
                flag = False
                break

        if flag:
            jump.append(chr(i))
    
    answer = ''
    for c in s:
        answer += convert(c, index, jump)
    return answer