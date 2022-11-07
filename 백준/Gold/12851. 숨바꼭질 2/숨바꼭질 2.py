from collections import deque

n, k = map(int, input().split())

# 이동 규칙 3가지
def move(dir, now):
    if dir == 0:
        return now - 1
    if dir == 1:
        return now + 1
    if dir == 2:
        return now * 2

# [이전 좌표]
visit = [-1] * (100001)
ans = [0] * (100001)
answer = 0
def dfs(now):
    global answer
    q = deque()
    q.append((now, 0))  # 현재 위치, 현재까지 이동시간
    visit[now] = 1
    ans[now] = 1
    flag = 1
    while q and flag:
        for _ in range(len(q)):
            now, cnt = q.popleft()
            
            if now == k:
                answer = cnt    # 시간 출력 저장
                flag = 0        # 이번 턴 까지 찾은 숫자만 유효
                continue
                    
            for dir in range(3):
                next = move(dir, now)
                
                if not (0 <= next < 100001): continue
                if visit[next] == -1:
                    ans[next] = ans[now]
                    visit[next] = cnt + 1
                    q.append((next, cnt + 1))
                elif visit[next] == cnt + 1:
                    ans[next] += ans[now]

dfs(n)
print(answer)
print(ans[k])