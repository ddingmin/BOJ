import sys
import heapq
from collections import deque
from bisect import bisect_left
import math
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(n, m , adj):
    visit = [float('inf')] * (n + 1)
    visit[1] = 0

    hq = []
    heapq.heappush(hq, [0, 1])
    while hq:
        cost, cur = heapq.heappop(hq)
        if visit[cur] != cost: continue
        for next, plus in adj[cur]:
            if cost + plus < visit[next]:
                heapq.heappush(hq, [cost + plus, next])
                visit[next] = cost + plus
    return visit[n]

# input
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    adj[b].append([a, c])

print(solve(n, m , adj))