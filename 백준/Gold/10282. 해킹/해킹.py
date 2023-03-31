import sys
import heapq
from collections import deque
from bisect import bisect_left

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(n, d, c, adj):
    # 컴퓨터 수, 시간
    answer = [0, 0]
    dists = [float('inf')] * (n + 1)
    hq = []
    heapq.heappush(hq, [0, c])
    dists[c] = 0
    while hq:
        cost, cur = heapq.heappop(hq)
        if dists[cur] != cost:
            continue
        for next, next_cost in adj[cur]:
            nc = cost + next_cost
            if nc < dists[next]:
                dists[next] = nc
                heapq.heappush(hq, [nc, next])

    for i in dists:
        if i == float('inf'):
            continue 
        else:
            answer[1] = max(answer[1], i)
            answer[0] += 1
            
    return answer

# input
t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append([a, s])
    print(*solve(n, d, c, adj))