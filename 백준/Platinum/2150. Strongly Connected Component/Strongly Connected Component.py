import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 코사라주 알고리즘

def solve(v, e, adj, radj):
    answer = []
    visit = [0] * (v + 1)
    stack = []
    temp = []

    def dfs(cur):
        if visit[cur]: 
            return
        visit[cur] = 1
        for nxt in adj[cur]:
            if not visit[nxt]: dfs(nxt)
        stack.append(cur)

    def rdfs(cur):
        if visit[cur]: return
        visit[cur] = 1
        temp.append(cur)
        for nxt in radj[cur]:
            if not visit[nxt]: rdfs(nxt)

    # 정방향 dfs로 stack에 담기
    for i in range(1, v + 1):
        dfs(i)
    visit = [0] * (v + 1)

    # 스택에서 빼가며 역방향 dfs
    for _ in range(len(stack)):
        cur = stack.pop()
        # 방문한 정점이면 pass
        if visit[cur]: continue
        temp = []
        rdfs(cur)
        answer.append(sorted(temp) + [-1])

    return [[len(answer)]] + sorted(answer)

# input
v, e = map(int, input().split())
adj = [[] for _ in range(v + 1)]
radj = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    adj[a].append(b)
    radj[b].append(a)

# 오름차순 정렬
for i in range(1, v + 1):
    adj[i].sort()
    radj[i].sort()

answer = solve(v, e, adj, radj)
for a in answer:
    print(*a)