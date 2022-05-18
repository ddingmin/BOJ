import sys
import heapq
# sys.setrecursionlimit(100001)
input = __import__('sys').stdin.readline

# Input
n, m, k = map(int, input().split()) # x가 목적지
adj = [[] for _ in range(n + 1)] # 인접리스트의 뼈대
radj = [[] for _ in range(n + 1)] # r인접리스트의 뼈대

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([b, c]) # 단방향 연결
    radj[b].append([a, c])

# 면접장
destlist = list(map(int, input().split()))
hq = []

cost = [float('inf')] * (n + 1)
for i in destlist:
    cost[i] = 0
    heapq.heappush(hq, [0,i])

while hq:
    t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
    if cost[x] != t: continue
    for nx, nt in (radj[x]): # nx는 노드, nt는 가중치
        if cost[nx] > t + nt:
            cost[nx] = t + nt # nx비용 초기화
            heapq.heappush(hq, [cost[nx], nx])

ans = 0
temp = 0

for i in range(1, n + 1):
    if cost[i] > temp:
        ans = i
        temp = cost[i]

print(ans)
print(temp)