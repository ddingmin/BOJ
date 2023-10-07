import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# input
arr = [list(map(int, input().split())) for _ in range(5)]


def solve(r, c):
    if arr[r][c] == 1:
        return 0
    q = deque()
    q.append([r, c])
    visit = [[0] * 5 for _ in range(5)]
    visit[r][c] = 1
    move = 1
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not (0 <= x < 5 and 0 <= y < 5): continue
                if visit[x][y] == 1 or arr[x][y] == -1: continue
                if arr[x][y] == 1:
                    return move
                visit[x][y] = 1
                q.append([x, y])
        move += 1
    return -1


r, c = map(int, input().split())
print(solve(r, c))
