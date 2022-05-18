import sys
import heapq

# sys.setrecursionlimit(100001)
input = __import__('sys').stdin.readline

# Input
n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)] # 인접리스트의 뼈대

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([b, c]) # 단방향 연결
start, dest = map(int, input().split())

cost = [float('inf')] * (n + 1)
hq = [[0, start]] # 시작 노드 넣어주기 [간선의 비용, 간선]
cost[start] = 0 # 시작 노드 -> 시작 노드 가는 비용은 0

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in adj[x]: # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])

print(cost[dest])