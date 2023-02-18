import sys
input = sys.stdin.readline


def solve(adj, v):
    visit = [0] * (v + 1)
    far_node = 0
    far_dist = 0
    def dfs(cur, dist):
        nonlocal visit
        nonlocal far_node
        nonlocal far_dist
        
        if dist > far_dist:
            far_node = cur
            far_dist = dist
            
        for next_node, next_dist in adj[cur]:
            if visit[next_node] == 0:
                visit[next_node] = 1
                dfs(next_node, next_dist + dist)
                visit[next_node] = 0
    visit[1] = 1
    dfs(1, 0)
    visit[1] = 0
    far_dist = 0
    visit[far_node] = 1
    dfs(far_node, 0)
    return far_dist

v = int(input())
adj = [[] for _ in range(v + 1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    cur = temp[0]
    for i in range((len(temp) - 2) // 2):
        idx = i * 2 + 1
        adj[cur].append((temp[idx], temp[idx + 1]))
print(solve(adj, v))