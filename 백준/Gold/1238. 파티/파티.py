import sys
import heapq


def dijkstra(start, reverse):
    cost = [float('inf')] * (n + 1)
    hq = [[0, start]]
    cost[start] = 0

    while hq:
        t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
        if cost[x] != t: continue
        for nx, nt in (adj[x] if not reverse else radj[x]): # nx는 노드, nt는 가중치
            if cost[nx] > t + nt:
                cost[nx] = t + nt # nx비용 초기화
                heapq.heappush(hq, [cost[nx], nx])
    return cost

# sys.setrecursionlimit(100001)
input = __import__('sys').stdin.readline

# Input
n, m, dest = map(int, input().split()) # x가 목적지
adj = [[] for _ in range(n + 1)] # 인접리스트의 뼈대
radj = [[] for _ in range(n + 1)] # r인접리스트의 뼈대

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([b, c]) # 단방향 연결
    radj[b].append([a, c])

stod = dijkstra(dest, 1)
dtos = dijkstra(dest, 0)

print(max(stod[i] + dtos[i] for i in range(1, n + 1)))
