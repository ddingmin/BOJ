import sys
import math
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque

# sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
MOD = 10_007
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# solve
def solve(n, m, arr):
    visit = [[0] * m for _ in range(n)]
    count = 0

    for r in range(n):
        for c in range(m):
            if visit[r][c] == 0 and arr[r][c] == '#':
                q = deque()
                count += 1
                visit[r][c] = 1
                q.append([r, c])
                while q:
                    i, j = q.popleft()
                    for k in range(4):
                        x, y = i + dx[k], j + dy[k]
                        if not (0 <= x < n and 0 <= y < m): continue
                        if visit[x][y] == 0 and arr[x][y] == '#':
                            visit[x][y] = 1
                            q.append([x, y])
    return count


# input
n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    print(solve(n, m, arr))
