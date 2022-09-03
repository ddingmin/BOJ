from collections import deque
# input
input = __import__('sys').stdin.readline
n = int(input())
arr = []
q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    arr.append(list(map(int, input().split())))

def solve():
    visit = [[0] * n for _ in range(n)]
    q.append((0, 0))
    visit[0][0] = 1
    while q:
        for _ in range(len(q)):
            i, j,  = q.popleft()
            move = arr[i][j]
            if arr[i][j] == -1: return "HaruHaru"
            for k in range(4):
                x, y = i + dx[k] * move, j + dy[k] * move
                if not(0 <= x < n and 0 <= y < n): continue
                if visit[x][y] == 0:
                    visit[x][y] = 1
                    q.append((x, y))
    return "Hing"

print(solve())