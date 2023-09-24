import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# input
arr = [[0] * 201 for _ in range(201)]
ans = 0

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(2 * a, 2 * c):
        for j in range(2 * b, 2 * d):
            if arr[i][j] == 0:
                ans += 1
            arr[i][j] = 1

print(ans // 4)