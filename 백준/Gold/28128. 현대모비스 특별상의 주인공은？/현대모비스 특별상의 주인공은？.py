import sys
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ddx, ddy = [2, 0], [0, 2]
n, m = map(int, input().split())
maps = [list(input().split())for _ in range(n)]

answer = {}

def is_answer(i, j):
    for dir in range(4):
        x, y = i + dx[dir], j + dy[dir]
        if not(0 <= x < n and 0 <= y < m): continue
        if maps[i][j] == maps[x][y]:
            return True
    return False

def is_answer_three_box(i, j):
    for dir in range(2):
        x, y = i + ddx[dir], j + ddy[dir]
        if not(0 <= x < n and 0 <= y < m):
            continue
        if maps[i][j] == maps[x][y]:
            return True
    return False

for i in range(n):
    for j in range(m):
        if is_answer(i, j) or is_answer_three_box(i, j):
            answer[maps[i][j]] = True

answer = sorted(answer.keys())
if answer:
    for ans in answer:
        print(ans)
else:
    print("MANIPULATED")