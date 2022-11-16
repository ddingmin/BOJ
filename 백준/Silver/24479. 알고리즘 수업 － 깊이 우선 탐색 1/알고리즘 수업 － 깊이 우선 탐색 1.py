from collections import deque
import sys

input = __import__('sys').stdin.readline
sys.setrecursionlimit(10**5)

n, m, r = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(len(adj)):
    if adj[i]:
        adj[i] = sorted(adj[i])

visit = [0] * (n + 1)

idx = 1
def dfs(startNode):
    global idx
    visit[startNode] = idx


    for nextNode in adj[startNode]:
        if visit[nextNode] == 0:
            idx += 1
            dfs(nextNode)
            

dfs(r)
for p in visit[1:]:
    print(p)
