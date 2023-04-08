import sys
from collections import deque
input = sys.stdin.readline

def get_dist(x, y, a, b):
    return abs(x - a) + abs(y - b)

def solve(n, adj):
    start, target = 0, n + 1
    visit = [0] * (n + 2)
    q = deque()
    q.append(start)
    visit[start] = 1
    
    while q:
        cur = q.popleft()
        if cur == target: return "happy"
        for next in adj[cur]:
            if visit[next]: continue
            q.append(next)
            visit[next] = 1
    return "sad"

t = int(input())
for _ in range(t):
    n = int(input())
    adj = [[] for _ in range(n + 2)]
    xy = []
    for i in range(n + 2):
        a, b = map(int, input().split())
        xy.append([a, b, i])
    
    for i in range(n + 2):
        a, b, i = xy[i]
        for j in range(n + 2):
            x, y, j = xy[j]
            if i == j: continue
            if get_dist(a, b, x, y) <= 1000:
                adj[i].append(j)
                adj[j].append(i)
    
    print(solve(n, adj))