import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solve(n, m, maps):
    dp = [[-1] * m for _ in range(n)]
    
    def dfs(i, j):
        if (i, j) == (n - 1, m - 1):
            return 1
        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = 0
        for dir in range(4):
            x, y = i + dx[dir], j + dy[dir]
            if not(0 <= x < n and 0 <= y < m): continue
            if maps[i][j] > maps[x][y]:
                dp[i][j] += dfs(x, y)
    
        return dp[i][j]
    
    return dfs(0, 0)

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, maps))