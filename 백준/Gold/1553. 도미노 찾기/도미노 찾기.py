import sys

sys.setrecursionlimit(10 ** 5)

dx, dy = [0, 1], [1, 0]

# input
arr = [list(map(int, list(input().strip()))) for _ in range(8)]

visit_shape = [[0] * 7 for _ in range(7)]

for i in range(7):
    for j in range(7):
        if i > j:
            visit_shape[i][j] = 1

##################################################

# solve
ans = 0
visit = [[0] * 7 for _ in range(8)]


def dfs(cnt):
    global ans

    i, j = cnt // 7, cnt % 7
    # 종료 조건
    if cnt == 56:
        ans += 1
        return

    # 이미 자리가 차 있으면 넘기는 조건
    if visit[i][j] == 1:
        dfs(cnt + 1)
        return

    for k in range(2):
        x, y = i + dx[k], j + dy[k]
        if not (0 <= x < 8 and 0 <= y < 7):
            continue
        left, right = min(arr[i][j], arr[x][y]), max(arr[i][j], arr[x][y])
        if visit[x][y] == 0 and visit_shape[left][right] == 0:
            visit[x][y] = 1
            visit[i][j] = 1
            visit_shape[left][right] = 1
            dfs(cnt + 1)
            visit[x][y] = 0
            visit[i][j] = 0
            visit_shape[left][right] = 0

dfs(0)

print(ans)
