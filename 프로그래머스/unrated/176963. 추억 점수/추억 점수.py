def solution(name, yearning, photo):
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    answer = []
    for p in photo:
        temp = 0
        for n in p:
            if n in score:
                temp += score[n]
        answer.append(temp)
    return answer