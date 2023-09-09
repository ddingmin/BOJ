import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s, e = map(int, input().split())

visit = [float('inf')] * (n + 1)
visit[s] = 0

q = deque()
q.append(s)

while q:
    cur = q.popleft()
    for k in range(1, n + 1):
        # 점프량 + 현재 위치
        next = arr[cur - 1] * k + cur
        if 0 < next < n + 1:
            if visit[cur] + 1 < visit[next]:
                visit[next] = visit[cur] + 1
                q.append(next)
        else:
            break
    
    for k in range(1, n + 1):
        # 점프량 + 현재 위치
        next = -(arr[cur - 1] * k) + cur
        if 0 < next < n + 1:
            if visit[cur] + 1 < visit[next]:
                visit[next] = visit[cur] + 1
                q.append(next)
        else:
            break
if visit[e] == float('inf'):
    print(-1)
else:
    print(visit[e])
