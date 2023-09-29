import sys
import math
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque


sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dx, dy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]

# input
n = int(input())

def find(i, j, tx, ty, size):
    if i == tx and j == ty:
        return 0
    q = deque()
    q.append([i, j])
    visit = [[0] * size for _ in range(size)]
    visit[i][j] = 1

    ans = 1
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in range(8):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= x < size and 0 <= y < size):
                    continue
                if visit[x][y] == 1:
                    continue
                if x == tx and y == ty:
                    return ans
                visit[x][y] = 1
                q.append([x, y])
        ans += 1


for _ in range(n):
    size = int(input())
    i, j = map(int, input().split())
    tx, ty = map(int, input().split())
    print(find(i, j, tx, ty, size))
