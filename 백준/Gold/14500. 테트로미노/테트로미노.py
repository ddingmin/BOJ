def check_two_three(blocks):
    sum_score = sum(blocks)
    score = 0
    score = max(score, sum_score - blocks[0] - blocks[1])
    score = max(score, sum_score - blocks[1] - blocks[2])
    score = max(score, sum_score - blocks[3] - blocks[4])
    score = max(score, sum_score - blocks[4] - blocks[5])

    score = max(score, sum_score - blocks[0] - blocks[2])
    score = max(score, sum_score - blocks[3] - blocks[5])

    score = max(score, sum_score - blocks[0] - blocks[5])
    score = max(score, sum_score - blocks[3] - blocks[2])

    score = max(score, sum_score - blocks[0] - blocks[3])
    score = max(score, sum_score - blocks[2] - blocks[5])
    return score

def check_three_two(blocks):
    sum_score = sum(blocks)
    score = 0
    score = max(score, sum_score - blocks[0] - blocks[2])
    score = max(score, sum_score - blocks[2] - blocks[4])
    score = max(score, sum_score - blocks[1] - blocks[3])
    score = max(score, sum_score - blocks[3] - blocks[5])

    score = max(score, sum_score - blocks[0] - blocks[4])
    score = max(score, sum_score - blocks[1] - blocks[5])

    score = max(score, sum_score - blocks[0] - blocks[5])
    score = max(score, sum_score - blocks[1] - blocks[4])

    score = max(score, sum_score - blocks[0] - blocks[1])
    score = max(score, sum_score - blocks[4] - blocks[5])
    return score

def check_four(n, m, arr):
    score = 0
    for i in range(n):
        for j in range(m - 3):
            cur_score = 0
            for k in range(4):
                cur_score += arr[i][j + k]
            score = max(score, cur_score)
    
    for i in range(n - 3):
        for j in range(m):
            cur_score = 0
            for k in range(4):
                cur_score += arr[i + k][j]
            score = max(score, cur_score)
            
    return score

def solve(n, m, arr):
    answer = check_four(n, m, arr)
    
    for i in range(n - 1):
        for j in range(m - 2):
            temp = arr[i][j:j + 3] + arr[i + 1][j: j + 3]
            answer = max(answer, check_two_three(temp))

    for i in range(n - 2):
        for j in range(m - 1):
            temp = arr[i][j:j + 2] + arr[i + 1][j:j + 2] + arr[i + 2][j:j + 2]
            answer = max(answer, check_three_two(temp))

    return answer

n, m = map(int, input().split())
arr = [(list(map(int, input().split()))) for _ in range(n)]

print(solve(n, m, arr))