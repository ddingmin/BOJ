import sys
from collections import deque
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

# input
n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

#######################

# solve
def calc(n, arr, r, c, d1, d2):
    sizes = [0, 0, 0, 0, 0]
    tarr = [[0] * n for _ in range(n)]

    # 범위 세팅
    for i in range(d1 + 1):
        tarr[r + i][c - i] = 5
    for i in range(d2 + 1):
        tarr[r + i][c + i] = 5
    for i in range(d2 + 1):
        tarr[r + d1 + i][c - d1 + i] = 5
    for i in range(d1 + 1):
        tarr[r + i + d2][c - i + d2] = 5

    # 구역 계산
    for i in range(r + d1):
        for j in range(c + 1):
            if tarr[i][j] == 5:
              break
            tarr[i][j] = 1

    for i in range(r + d2 + 1):
        for j in range(n - 1, c, -1):
            if tarr[i][j] == 5:
                break
            tarr[i][j] = 2

    for i in range(r + d1, n):
        for j in range(c - d1 + d2):
            if tarr[i][j] == 5:
                break
            tarr[i][j] = 3

    for i in range(r + d2 + 1, n):
        for j in range(n - 1, c - d1 + d2 -1, -1):
            if tarr[i][j] == 5:
                break
            tarr[i][j] = 4

    # 최소 최대 계산
    for i in range(n):
        for j in range(n):
            if tarr[i][j] == 1:
                sizes[0] += arr[i][j]
            elif tarr[i][j] == 2:
                sizes[1] += arr[i][j]
            elif tarr[i][j] == 3:
                sizes[2] += arr[i][j]
            elif tarr[i][j] == 4:
                sizes[3] += arr[i][j]
            else:
                sizes[4] += arr[i][j]

    return max(sizes) - min(sizes)


ans = float('inf')
for i in range(n):
    for j in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if not(0 <= j - d1 < j < j + d2 < n
                and 0 <= i < i + d1 + d2 < n):
                    continue
                ans = min(ans, calc(n, arr, i, j, d1, d2))

print(ans)

