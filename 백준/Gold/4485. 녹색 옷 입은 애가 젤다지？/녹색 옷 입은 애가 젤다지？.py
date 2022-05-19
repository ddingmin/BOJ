import heapq
input = __import__('sys').stdin.readline

# Input
num = 1
while 1:
    n = int(input())
    if n == 0: exit(0)
    adj = [[] for _ in range(n ** 2 + 1)]

    arr = []
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    k = 1
    for i in range(n):
        for j in range(n):
            g = 0
            for d in dir:
                dx, dy = i + d[0], j + d[1]
                if 0 <= dx < n and 0 <= dy < n:
                    if g == 0: adj[k].append([k + n, arr[dx][dy]])
                    if g == 1: adj[k].append([k - n, arr[dx][dy]])
                    if g == 2: adj[k].append([k + 1, arr[dx][dy]])
                    if g == 3: adj[k].append([k - 1, arr[dx][dy]])
                g += 1
            k += 1

    # mac -> 집의 최소경로
    hq = []
    cost = [float('inf')] * (n ** 2 + 1)
    cost[1] = arr[0][0]
    heapq.heappush(hq, [arr[0][0], 1])

    while hq:
        t, x = heapq.heappop(hq) # t: 현재까지의 가중치, x는 현재 노드
        if cost[x] != t: continue
        for nx, nt in (adj[x]): # nx는 노드, nt는 가중치
            if cost[nx] > t + nt:
                cost[nx] = t + nt # nx비용 초기화
                heapq.heappush(hq, [cost[nx], nx])
    ans = cost[n**2]
    print("Problem {}: {}".format(num, ans))
    num += 1
