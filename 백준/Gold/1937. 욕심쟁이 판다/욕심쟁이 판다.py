import sys
from collections import deque

dx, dy = [[-1, 1, 0, 0], [0, 0, -1, 1]]


def solve(n, arr, data):
    dp = [[0] * n for _ in range(n)]
    q = deque(data)
    ans = 0

    while q:
        cur, i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not (0 <= x < n and 0 <= y < n): continue
            if arr[x][y] > arr[i][j] and dp[i][j] + 1 > dp[x][y]:
                dp[x][y] = dp[i][j] + 1
                q.append([arr[x][y], x, y])
                ans = max(ans, dp[x][y])

    return ans + 1


def main():
    n = int(input())
    arr = []
    data = []
    for i in range(n):
        line = list(map(int, input().split()))
        arr.append(line)
        for j in range(n):
            data.append([arr[i][j], i, j])

    data = sorted(data)

    print(solve(n, arr, data))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
