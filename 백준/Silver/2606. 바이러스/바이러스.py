from collections import deque

input = __import__('sys').stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(int(input())):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

answer = 0
q = deque()
visit[1] = 1
q.append(1)

while q:
    cur = q.popleft()
    for next in adj[cur]:
        if visit[next] == 0:
            visit[next] = 1
            q.append(next)
            answer += 1

print(answer)