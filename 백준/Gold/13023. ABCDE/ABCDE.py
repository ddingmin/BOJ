import sys

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visit = [0] * n
def dfs(depth, cur):
    if depth == 5:
        print(1)
        exit()
    for next in adj[cur]:
        if not visit[next]:
            visit[next] = 1
            dfs(depth + 1, next)
            visit[next] = 0
    return 0

answer = 0
for i in range(n):
    visit[i] = 1
    answer = dfs(1, i)
    visit[i] = 0

print(0)