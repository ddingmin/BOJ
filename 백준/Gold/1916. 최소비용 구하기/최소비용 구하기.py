import heapq

def solve(n, adj, start, end):
    hq = []
    visit = [float('inf')] * (n + 1)
    heapq.heappush(hq, [0, start])
    visit[start] = 0
    while hq:
        cur_cost, cur_node = heapq.heappop(hq)
        if visit[cur_node] != cur_cost: continue
        for next_node, next_cost in adj[cur_node]:
            if visit[next_node] > cur_cost + next_cost:
                visit[next_node] = cur_cost + next_cost
                heapq.heappush(hq, [cur_cost + next_cost, next_node])
    return visit[end]
    
n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    adj[s].append([e, cost])
start, end = map(int, input().split())
print(solve(n, adj, start, end))