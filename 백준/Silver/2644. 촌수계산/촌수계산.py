import sys
import heapq
import math
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
s, e = map(int, input().split())
m = int(input())

visit = [0] * (n + 1)
adj = [[]for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

q = deque()
q.append(s)
visit[s] = 1

count = 0

while q:
    for _ in range(len(q)):
        cur = q.popleft()
        for next in adj[cur]:
            if visit[next] == 0:
                visit[next] = visit[cur] + 1
                q.append(next)

if visit[e] == 0:
    print(-1)
else:
    print(visit[e] - 1)
                
    