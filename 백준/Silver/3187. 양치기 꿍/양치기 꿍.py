import sys
import heapq
import math
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(input().strip()))

visit = [[0] * m for _ in range(n)]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visit[i][j] = 1
    k, v = 0, 0
    
    if maps[i][j] == 'k':
        k += 1
    elif maps[i][j] == 'v':
        v += 1
    while q:
        i, j = q.popleft()
        for dir in range(4):
            x, y = i + dx[dir], j + dy[dir]
            if not(0 <= x < n and 0 <= y < m): continue
            if maps[x][y] == '#' or visit[x][y] == 1: continue
            q.append([x, y])
            visit[x][y] = 1
            if maps[x][y] == 'k':
                k += 1
            elif maps[x][y] == 'v':
                v += 1
    if k > v:
        return k, 0
    else:
        return 0, v
            
k, v = 0, 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == '#' or visit[i][j] == 1: continue
        a, b = bfs(i, j)
        k += a
        v += b

print(k, v)
        