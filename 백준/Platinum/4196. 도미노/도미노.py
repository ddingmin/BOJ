import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 7)

def solve(n, m, adj):
    visit = [0] * (n + 1)
    count = 0

    # dfs
    def dfs(cur):
        visit[cur] = 1
        for next in adj[cur]:
            if visit[next] == 0:
                dfs(next)
        scc.append(cur)

    # scc dfs
    def scc_dfs(cur):
        visit[cur] = 1
        for next in adj[cur]:
            if visit[next] == 0:
                scc_dfs(next)
    
    # scc 구하기
    scc = []
    for i in range(1, n + 1):
        if visit[i] != 0: continue
        # 정방향 dfs로 나열
        dfs(i)

    # scc[top]이 영향이 가장 큰 도미노
    visit = [0] * (n + 1)
    for node in scc[::-1]:
        if visit[node] == 0:
            count += 1
            # 가장 영향이 큰 도미노 부터 dfs
            scc_dfs(node)

    return count

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    adj_reverse = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)

    print(solve(n, m, adj))