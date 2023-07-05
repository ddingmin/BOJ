import sys
from collections import deque

input = sys.stdin.readline

a, k = map(int, input().split())

q = deque()
visit = [0] * (k + 1)
q.append(a)
visit[a] = 1

count = 0
while q:
    for _ in range(len(q)):
        cur = q.popleft()
        if cur == k:
            print(count)
            exit()
        # 1 더하기
        next = cur + 1
        if 0 <= next <= k and visit[next] == 0:
            visit[next] = 1
            q.append(next)
        
        next = cur * 2
        if 0 <= next <= k and visit[next] == 0:
            visit[next] = 1
            q.append(next)
    count += 1

            
    
