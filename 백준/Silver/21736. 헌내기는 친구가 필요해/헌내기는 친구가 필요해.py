import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]



def find(i, j):
    visit = [[0] * m for _ in range(n)]
    q = deque()
    q.append([i, j])
    visit[i][j] = 1

    ans = 0

    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y] == 1 or arr[x][y] == "X": continue
            if arr[x][y] == "P": ans += 1
            visit[x][y] = 1
            q.append([x, y])
    if ans:
        return ans
    return "TT"


for i in range(n):
    for j in range(m):
        if arr[i][j] == "I":
            print(find(i, j))
            break
