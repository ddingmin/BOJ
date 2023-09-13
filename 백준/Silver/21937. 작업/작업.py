import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
visit = [0] * (n + 1)
nodes = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    nodes[b].append(a)
t = int(input())

visit[t] = 1
q = deque()
q.append(t)
ans = 0
while q:
    cur = q.popleft()
    for next in nodes[cur]:
        if visit[next] == 0:
            visit[next] = 1
            q.append(next)
            ans += 1
print(ans)
            