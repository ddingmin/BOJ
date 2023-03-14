import sys
from collections import deque


input = sys.stdin.readline


n = int(input())
parent = list(map(int, input().split()))
del_node = int(input())

root = None
adj = [[] for _ in range(n)]
for i in range(n):
    if parent[i] == -1:
        root = i
    if i == del_node or parent[i] == del_node: continue
    
    if parent[i] >= 0:
        adj[parent[i]].append(i)
    
if root ==  del_node:
    print(0)
    exit()
q = deque()
q.append(root)
visit = [0] * n
visit[root] = 1

count = 0

while q:
    cur = q.popleft()
    if len(adj[cur]) == 0:
        count += 1
    for next in adj[cur]:
        if not visit[next]:
            q.append(next)
            visit[next] = 1

print(count)