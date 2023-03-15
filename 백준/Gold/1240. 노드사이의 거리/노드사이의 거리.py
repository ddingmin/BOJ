import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, cost = map(int, input().split())
    adj[a].append([b, cost])
    adj[b].append([a, cost])


def bfs(start, end):
    q = deque()
    q.append([start, 0])
    visit = [0] * (n + 1)
    visit[start] = 1
    
    while q:
        cur, cur_cost = q.popleft()
        if cur == end:
            return cur_cost
        for next, next_cost in adj[cur]:
            if visit[next]: continue
            visit[next] = 1
            q.append([next, cur_cost + next_cost])
    return 0

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e))