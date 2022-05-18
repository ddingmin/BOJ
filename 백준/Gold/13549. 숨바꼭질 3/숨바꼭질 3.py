import sys
import heapq
# sys.setrecursionlimit(100001)
input = __import__('sys').stdin.readline

# Input
n, m = map(int, input().split()) # x가 목적지
adj = [[] for _ in range(100001)] # 양방향인접리스트의 뼈대

make = max(n, m) + 1
for i in range(100001):
    if 0 <= i + 1 <= 100000: adj[i].append([i + 1, 1])
    if 0 <= i - 1 <= 100000: adj[i].append([i - 1, 1])
    if 0 <= i * 2 <= 100000: adj[i].append([i * 2, 0])

# 1 -> u 가는 최소 경로
hq = []
cost = [float('inf')] * (100001)
cost[n] = 0
heapq.heappush(hq, [0, n])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (adj[x]): # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])
ans = cost[m]
print(ans)