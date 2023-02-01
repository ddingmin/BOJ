from collections import deque

input = __import__('sys').stdin.readline
n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bf(i):
    q = deque()
    visit[i] = 1
    q.append(i)
    while q:
        cur = q.popleft()
        for next_node in adj[cur]:
            if not visit[next_node]:
                visit[next_node] = 1
                q.append(next_node)
                
answer = 0
for i in range(1, n + 1):
    if not visit[i]:
        answer += 1
        bf(i)

print(answer)