import heapq
input = __import__('sys').stdin.readline

V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    adj[b].append([a, c])

# 1번 노드부터 시작
mst = [-1] * (V + 1)
H = []
heapq.heappush(H, [0, 1])

while H:
    power, node = heapq.heappop(H)
    if mst[node] != -1: continue
    
    mst[node] = power
    for next_node, get_power in adj[node]:
        heapq.heappush(H, [get_power, next_node])

print(sum(mst[1:]))
