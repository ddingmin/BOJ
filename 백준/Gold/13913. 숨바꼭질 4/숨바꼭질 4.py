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

def dfs(now):
    q = deque()
    q.append((now, 0))  # 현재 위치, 현재까지 이동시간
    visit[now] = 0
    
    while q:
        now, cnt = q.popleft()
        
        if now == k:    # 가장 빠르게 도달하면
            print(cnt)  # 시간 출력
            route = ""  # 이동 경로를 visit 배열을 통해 구함
            for _ in range(cnt + 1):
                route = str(now) + " " + route
                now = visit[now]
            print(route)
            exit()
                
        for dir in range(3):
            next = move(dir, now)
            
            if not (0 <= next < 100001): continue
            if visit[next] == -1:
                visit[next] = now   # visit엔 이전 위치 좌표를 기록
                q.append((next, cnt + 1))

dfs(n)