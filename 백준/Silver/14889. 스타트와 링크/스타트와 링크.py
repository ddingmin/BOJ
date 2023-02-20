from itertools import combinations as cb

def solve(n, people):
    answer = float('inf')
    max_team = n // 2
    def calc(team):
        scores = [0, 0]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if team[i] == team[j]:
                    scores[team[i]] += people[i][j] + people[j][i]
        return abs(scores[0] // 2 - scores[1] // 2)
    
    temp = []
    for i in range(n):
        temp.append(i)
    for i in cb(temp, max_team):
        team = [0] * n
        for j in i:
            team[j] = 1
        answer = min(answer, calc(team))
        
    return answer

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, people))