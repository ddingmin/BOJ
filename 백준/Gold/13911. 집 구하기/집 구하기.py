import sys
import heapq
# sys.setrecursionlimit(100001)
input = __import__('sys').stdin.readline

# Input
n, m = map(int, input().split()) # x가 목적지
adj = [[] for _ in range(n + 3)] # 양방향인접리스트의 뼈대

macV = n + 1
starV = n + 2

for i in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    adj[b].append([a, c])

mac, macinHome = map(int, input().split())
macList = list(map(int, input().split()))
star, starinHome = map(int, input().split())
starList = list(map(int, input().split()))

# 가상의 노드에 연결
for i in macList:
    adj[macV].append([i, 0])
    adj[i].append([macV, 0])

for i in starList:
    adj[starV].append([i, 0])
    adj[i].append([starV, 0])

# mac -> 집의 최소경로들
hq = []
cost = [float('inf')] * (n + 3)
cost[macV] = 0
heapq.heappush(hq, [0, macV])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (adj[x]): # nx는 노드, nt는 가중치
        # 가상의 노드를 지날순 없음
        if nx == macV or nx == starV: continue

        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])


# star -> 집의 최소경로들
hq = []
costt = [float('inf')] * (n + 3)
costt[starV] = 0
heapq.heappush(hq, [0, starV])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if costt[x] != t: continue
    for nx, nt in (adj[x]): # nx는 노드, nt는 가중치
        # 가상의 노드를 지날순 없음
        if nx == macV or nx == starV: continue
        
        if costt[nx] > t + nt:
            costt[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [costt[nx], nx])

ans = float('inf')
for i in range(1, n + 1):
    if i in macList: continue
    if i in starList: continue
    if cost[i] <= macinHome and costt[i] <= starinHome: ans = min(ans, cost[i] + costt[i])
if ans == float('inf'): print(-1)
else: print(ans)