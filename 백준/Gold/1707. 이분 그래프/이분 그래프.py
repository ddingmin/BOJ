import sys
from collections import deque

input = sys.stdin.readline

def init(n, e):
    visit = [-1] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    return visit, adj

def solve(n, e, visit, adj):
    for cur in range(1, n + 1):
        if visit[cur] != -1: continue
        visit[cur] = 1
        q = deque()
        q.append(cur)
        while q:
            cur = q.popleft()
            for next in adj[cur]:
                if visit[next] == -1: 
                    visit[next] = visit[cur] ^ 1
                    q.append(next)
                if visit[next] == visit[cur]:
                    return "NO"
                else:
                    continue
    return 'YES'

            
for _ in range(int(input())):
    n, e = map(int, input().split())
    visit, adj = init(n, e)
    print(solve(n, e, visit, adj))