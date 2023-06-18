from collections import deque
from itertools import combinations as cb
import sys
import copy

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# input
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

virus = []
need_detect = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            need_detect += 1
        elif arr[i][j] == 2:
            virus.append([i, j])

# func
def solve(q, count, arr):
    if count == 0:
        return 0
    level = 0
    visit = [[0] * n for _ in range(n)]
    for x, y in q:
        visit[x][y] = 1

    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for dir in range(4):
                x, y = i + dx[dir], j + dy[dir]
                if not(0 <= x < n and 0 <= y < n): continue
                if arr[x][y] != 1 and visit[x][y] == 0:
                    visit[x][y] = 1
                    q.append([x, y])
                    if arr[x][y] == 0:
                        count -= 1
        level += 1
        if count == 0:
            return level
    return float('inf')


answer = float('inf')


for a in cb(virus, m):
    q = deque()
    for i in a:
        x, y = i
        q.append(i)
    answer = min(solve(q, need_detect, arr), answer)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
    