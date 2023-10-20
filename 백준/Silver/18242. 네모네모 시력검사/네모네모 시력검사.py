import sys
from collections import deque
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
cx, cy = [-1, 1, 1, -1], [1, 1, -1, -1]

# solve
def find(r, c):
    for size in range(2, 51):

        check = 0
        # 범위 가능한지 체크
        for k in range(4):
            x, y = r + cx[k] * size, c + cy[k] * size
            if not(0 <= x < n and 0 <= y < m): return
            if not(arr[x][y] == '#'): check = 1
        if check == 1: continue

        cnt = [0, 0, 0, 0]
        # UP 체크
        x = r + size * -1
        for y in range(c - size + 1, c + size):
            if arr[x][y] == '#': cnt[0] += 1
        x = r + size * 1
        for y in range(c - size + 1, c + size):
            if arr[x][y] == '#': cnt[1] += 1
        y = c + size * -1
        for x in range(r - size + 1, r + size):
            if arr[x][y] == '#': cnt[2] += 1
        y = c + size * 1
        for x in range(r - size + 1, r + size):
            if arr[x][y] == '#': cnt[3] += 1

        ans = 0
        for k in range(3):
            if cnt[k] + 1 == cnt[k + 1]:
                return k
        return 3


# input
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        temp = find(i, j)
        if temp == 0:
            print('UP')
        elif temp == 1:
            print('DOWN')
        elif temp == 2:
            print('LEFT')
        elif temp == 3:
            print('RIGHT')
