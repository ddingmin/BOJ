import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n, m, r = map(int, input().split())

adj =[[] for _ in range(n + 1)]
visit = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, n + 1):
    adj[i].sort(reverse=1)

ans = [0] * (n + 1)
level = 1

def dfs(cur):
    global level
    visit[cur] = 1
    ans[cur] = level
    level += 1

    for next in adj[cur]:
        if visit[next] == 0:
            dfs(next)
    
dfs(r)

for i in range(1, n + 1):
    print(ans[i])