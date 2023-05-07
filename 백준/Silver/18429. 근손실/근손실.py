n, k = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
visit = [0] * n

def bt(day, power):
    global answer
    if power < 500:
        return
    if day == n:
        answer += 1

    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            bt(day + 1, power - k + nums[i])
            visit[i] = 0
    
bt(0, 500)
print(answer)