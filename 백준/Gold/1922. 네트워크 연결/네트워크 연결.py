import heapq
import sys
input = sys.stdin.readline

def solve(n, adj):
    hq = []
    visit = [-1] * (n + 1)
    heapq.heappush(hq, [0, 1])

    while hq:
        cur_cost, cur_node = heapq.heappop(hq)
        if visit[cur_node] != -1: continue
        
        visit[cur_node] = cur_cost
        for next_node, next_cost in adj[cur_node]:
            heapq.heappush(hq, [next_cost, next_node])
    return sum(visit[1:])
    
n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    adj[s].append([e, cost])
    adj[e].append([s, cost])
print(solve(n, adj))