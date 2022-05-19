import heapq
# sys.setrecursionlimit(100001)
input = __import__('sys').stdin.readline

# Input
t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) # x가 목적지
    adj = [[] for _ in range(n + 1)] # 양방향인접리스트의 뼈대

    for i in range(m):
        a, b, c = map(int, input().split())
        adj[a].append([b, c])
        adj[b].append([a, c])

    k = int(input())
    friend = list(map(int, input().split()))
    ans = [0] * (n + 1)
    # friend -> 각 방 최소 경로
    for start in friend:
        hq = []
        cost = [float('inf')] * (n + 1)
        cost[start] = 0
        heapq.heappush(hq, [0, start])

        while hq:
            t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
            if cost[x] != t: continue
            for nx, nt in (adj[x]): # nx는 노드, nt는 가중치
                if cost[nx] > t + nt:
                    cost[nx] = t + nt # nx비용 초기화
                    heapq.heappush(hq, [cost[nx], nx])
        for i in range(1, n + 1):
            ans[i] += cost[i]

    temp = float('inf')
    aa = 0
    for i in range(1, n + 1):
        if ans[i] < temp: 
            aa = i
            temp = ans[i]
    print(aa)