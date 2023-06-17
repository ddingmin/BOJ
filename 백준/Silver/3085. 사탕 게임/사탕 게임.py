import sys
input = sys.stdin.readline


n = int(input())
arr = [list(input().strip()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

def cal():
    max_eat = 0
    for i in range(n):
        row = 1
        col = 1
        for j in range(1, n):
            if arr[i][j - 1]== arr[i][j]:
                row += 1
            else:
                row = 1
            if arr[j - 1][i] == arr[j][i]:
                col += 1
            else:
                col = 1
            max_eat = max(max_eat, row, col)
    return max_eat

for i in range(n):
    for j in range(n):
        for dir in range(4):
            x, y = i + dx[dir], j + dy[dir]
            if not(0 <= x < n and 0 <= y < n): continue
            if arr[x][y] == arr[i][j]: continue
            # 사탕 변경
            arr[x][y], arr[i][j] = arr[i][j], arr[x][y]
            answer = max(answer, cal())
            arr[x][y], arr[i][j] = arr[i][j], arr[x][y]

print(answer)