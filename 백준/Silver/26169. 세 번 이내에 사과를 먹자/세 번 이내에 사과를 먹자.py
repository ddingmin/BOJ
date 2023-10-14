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
def solve(r, c, depth, count, visit):
    global answer
    if depth == 3:
        if count >= 2:
            answer = 1
        return
    for k in range(4):
        x, y = r + dx[k], c + dy[k]
        if not(0 <= x < 5 and 0 <= y < 5): continue
        if visit[x][y] == 0 and arr[x][y] != -1:
            visit[x][y] = 1
            temp = 0
            if arr[x][y] == 1:
                temp = 1
            solve(x, y, depth + 1, count + temp, visit)
            visit[x][y] = 0


# input
arr = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
visit = [[0] * 5 for _ in range(5)]
visit[r][c] = 1

answer = 0
solve(r, c, 0, 0, visit)
print(answer)

