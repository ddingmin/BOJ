import sys
sys.setrecursionlimit(10 ** 5)
max_score = 0.1
answer = []

def find(temp):
    ans = temp[-1]
    for idx in range(len(temp) - 1):
        
        for i in range(10 ,-1 ,-1):
            if ans[i] == temp[idx][i]:
                continue
            elif ans[i] > temp[idx][i]:
                break
            else:
                ans = temp[idx]
    return ans
            

def cal_score(apeach, lion):
    a, l = 0, 0
    for i in range(10):
        if apeach[i] == lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            a += 10 - i
        else:
            l += 10 - i
    return l - a

def dfs(depth, n, apeach, lion, idx):
    global max_score
    global answer
    if depth == n:
        score = cal_score(apeach, lion)
        if score >= max_score:
            if not(score == max_score):
                answer = []
            max_score = score
            answer.append(lion.copy())
        return
    for i in range(idx, 11):
        lion[i] += 1
        dfs(depth + 1, n, apeach, lion, i)
        lion[i] -= 1
        

def solution(n, info):
    dfs(0, n, info, [0] * 11, 0)
    if len(answer) == 0:
        return [-1]
    elif len(answer) == 1:
        return answer[0]
    return find(answer)