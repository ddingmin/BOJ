import sys
sys.setrecursionlimit(100001)
input = __import__('sys').stdin.readline

# Input
n, m = map(int, input().split())

users = list(map(int, input().split()))
adj = [[] for _ in range(n)]
goodjob = [0] * n

def dfs(x):
    for nx in adj[x]:
        goodjob[nx] += goodjob[x]
        dfs(nx)

for i in range(1, n):
    adj[users[i] - 1].append(i)

for _ in range(m):
    i, w = map(int, input().split())
    goodjob[i-1] += w

dfs(0)
print(*goodjob)