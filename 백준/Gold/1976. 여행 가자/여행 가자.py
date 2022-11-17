from collections import deque

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]

for a in range(1, n + 1):
    temp = list(map(int, input().split()))
    for b in range(len(temp)):
        if temp[b] == 1:
            adj[a].append(b + 1)

path = list(map(int, input().split()))

def dfs(start, end):
    visit = [0] * (n + 1)
    visit[start] = 1
    q = deque()
    q.append(start)
    while q:
        startNode = q.popleft()
        if startNode == end:
            return True
        for nextNode in adj[startNode]:
            if visit[nextNode] == 0:
                visit[nextNode] = 1
                q.append(nextNode)
    return False

for idx in range(1, len(path)):
    start, end = path[idx - 1], path[idx]
    if dfs(start, end): continue
    else:
        print("NO")
        exit()
print("YES")
    