import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


# input
n, m, r = map(int, input().split())
items = {}
arr = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] not in items:
            items[arr[i][j]] = [[i, j]]
        else:
            items[arr[i][j]].append([i, j])

name = input().strip()

can_eat = float('inf')
cnt = {}

for i in name:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1

for k in cnt:
    if k not in items:
        can_eat = 0
    else:
        can_eat = min(len(items[k]) // cnt[k], can_eat)

ate = [[0] * m for _ in range(n)]
# solve
ans = [0, ""]


def get_dist(i, j, x, y):
    return abs(i - x) + abs(j - y)


def get_cmd(i, j, x, y):
    result = ""
    if i > x:
        result += "U" * (i - x)
    else:
        result += "D" * (x - i)

    if j > y:
        result += "L" * (j - y)
    else:
        result += "R" * (y - j)
    return result + "P"


def backtracking(i, j, need_idx, words):
    global ans
    if need_idx and need_idx % len(name) == 0:
        ans = [need_idx // len(name), words + get_cmd(i, j, n - 1, m - 1)[:-1]]
        if ans[0] == can_eat:
            print(ans[0], len(ans[1]))
            print(ans[1])
            exit()

    for x, y in items[name[need_idx % len(name)]]:
        if ate[x][y]:
            continue
        ate[x][y] = 1
        backtracking(x, y, need_idx + 1, words + get_cmd(i, j, x, y))
        ate[x][y] = 0


if can_eat == 0:
    ans = [0, get_cmd(0, 0, n - 1, m - 1)[:-1]]
    print(ans[0], len(ans[1]))
    print(ans[1])
    exit()

backtracking(0, 0, 0, "")
