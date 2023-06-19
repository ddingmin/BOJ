def solution(survey, choices):
    score = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    
    for i in range(len(survey)):
        cur = "".join(sorted(survey[i]))
        if cur == survey[i]:
            score[cur] -= choices[i] - 4
        else:
            score[cur] += choices[i] - 4
            
            
    answer = ''
    for key in score:
        if score[key] >= 0:
            answer += key[0]
        else:
            answer += key[1]
    return answer