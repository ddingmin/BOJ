import heapq

def solve(adj, n, m, k, x):
    dists = [float('inf')] * (n + 1)
    hq = []
    dists[x] = 0
    heapq.heappush(hq, [0, x])
    while hq:
        cur_cost, cur_node = heapq.heappop(hq)
        if dists[cur_node] != cur_cost: continue

        for next_node in adj[cur_node]:
            next_cost = cur_cost + 1
            if next_cost < dists[next_node]:
                dists[next_node] = next_cost
                heapq.heappush(hq, [next_cost, next_node])
    flag = False
    for i in range(1, n + 1):
        if dists[i] == k: 
            print(i)
            flag = True
    if not flag: print(-1)
    return

n, m, k, x = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
solve(adj, n, m, k, x)
