import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visit[1] = 1
q = deque()
q.append(1)

turn = 0
answer = 0
while q and turn < 2:
    for _ in range(len(q)):
        cur = q.popleft()
        for next in adj[cur]:
            if visit[next] == 0:
                answer += 1
                visit[next] = 1
                q.append(next)
    turn += 1

print(answer)