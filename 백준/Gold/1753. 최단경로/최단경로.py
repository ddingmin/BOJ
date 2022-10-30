import heapq
input = __import__('sys').stdin.readline

v, e = map(int, input().split())
start = int(input())

adj = [[] for _ in range(v + 1)] # 인접리스트의 뼈대
for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    
hq = []
cost = [float('inf')] * (v + 1)
cost[start] = 0
heapq.heappush(hq, [0, start])
while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (adj[x]): # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])

for i in cost[1::]:
    if i == float('inf'): print("INF")
    else: print(i)