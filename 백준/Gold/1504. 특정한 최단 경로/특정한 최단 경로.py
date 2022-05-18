import sys
import heapq
# sys.setrecursionlimit(100001)
input = __import__('sys').stdin.readline

# Input
n, m = map(int, input().split()) # x가 목적지
adj = [[] for _ in range(n + 1)] # 인접리스트의 뼈대
radj = [[] for _ in range(n + 1)] # r인접리스트의 뼈대
aadj = [[] for _ in range(n + 1)] # 양방향인접리스트의 뼈대

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([b, c]) # 단방향 연결
    radj[b].append([a, c]) # e단방향 연결
    aadj[a].append([b, c])
    aadj[b].append([a, c])

u, v = map(int, input().split())

ans = 0
# 1 -> u 가는 최소 경로
hq = []
cost = [float('inf')] * (n + 1)
cost[1] = 0
heapq.heappush(hq, [0, 1])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (aadj[x]): # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])
ans += cost[u]
# --------------------
# u -> v 로 가는 최소 경로
hq = []
cost = [float('inf')] * (n + 1)
cost[u] = 0
heapq.heappush(hq, [0, u])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (aadj[x]): # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])
ans += cost[v]
#--------------------
# v -> n으로 가는 최소 경로
hq = []
cost = [float('inf')] * (n + 1)
cost[v] = 0
heapq.heappush(hq, [0, v])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (aadj[x]): # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])
ans += cost[n]

# 1 -> v -> u -> n   ----------------------

ans2 = 0
# 1 -> v 가는 최소 경로
hq = []
cost = [float('inf')] * (n + 1)
cost[1] = 0
heapq.heappush(hq, [0, 1])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (aadj[x]): # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])
ans2 += cost[v]
# --------------------
# v -> u 로 가는 최소 경로
hq = []
cost = [float('inf')] * (n + 1)
cost[v] = 0
heapq.heappush(hq, [0, v])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (aadj[x]): # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])
ans2 += cost[u]
#--------------------
# u -> n으로 가는 최소 경로
hq = []
cost = [float('inf')] * (n + 1)
cost[u] = 0
heapq.heappush(hq, [0, u])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (aadj[x]): # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])
ans2 += cost[n]


ans = min(ans, ans2)
if ans == float('inf'): print(-1)
else: print(ans)